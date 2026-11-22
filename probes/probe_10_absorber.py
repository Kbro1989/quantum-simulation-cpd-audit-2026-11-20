"""Domain 10: Absorbing-boundary behaviour.

Measures mask properties, norm loss rate, wraparound/reflection suppression,
and stability for absorber polynomial orders 1..6.
"""
import numpy as np

from quantumlab.core.grid import Grid1D
from quantumlab.core.wavefunction import WaveFunction1D
from quantumlab.core.absorbing_boundary import AbsorbingBoundaryLayer
from quantumlab.solvers.split_operator import SplitOperatorSolver

print("=== Domain 10: Absorbing-boundary behaviour ===")
L, N = 24.0, 512
grid = Grid1D(N, -L / 2.0, L / 2.0)

# 10a. mask properties for orders 1..6
print("10a mask properties (boundary_width=3):")
masks = {}
for order in range(1, 7):
    abl = AbsorbingBoundaryLayer(grid, boundary_width=3.0, order=order)
    m = abl.mask
    masks[order] = m
    interior = (grid.x > -L / 2.0 + 3.0) & (grid.x < L / 2.0 - 3.0)
    print("10a order=%d  min=%.6f max=%.6f  mask[0]=%.6f mask[-1]=%.6f  interior all 1: %s"
          % (order, m.min(), m.max(), m[0], m[-1], bool(np.all(m[interior] == 1.0))))
print("10a order1==order2==order3 masks: %s ; order3!=order4: %s"
      % (np.array_equal(masks[1], masks[2]) and np.array_equal(masks[2], masks[3]),
         not np.array_equal(masks[3], masks[4])))

# 10b. norm loss rate and wraparound suppression.
# Packet starts at x=0 and moves right; the left region is only reached if the
# packet wraps around the periodic grid.  Sampled after t>4 (past the wrap).
dt = 0.01
x_start, k0, sigma = 0.0, 3.0, 0.5
nsteps = 800


def run(use_absorber, order=3):
    abl = AbsorbingBoundaryLayer(grid, boundary_width=3.0, order=order) \
        if use_absorber else None
    sol = SplitOperatorSolver(grid, None, dt=dt, absorber=abl)
    wf = WaveFunction1D.gaussian(grid, x_start, k0, sigma)
    norms = [wf.norm()]
    left_density = []
    for n in range(nsteps):
        wf = sol.step(wf)
        norms.append(wf.norm())
        if (n + 1) * dt > 4.0:
            left_density.append(np.max(np.abs(wf.psi[grid.x < -L / 2.0 + 4.0]) ** 2))
    return np.array(norms), np.array(left_density), wf


n_abs, left_abs, wf_abs = run(True)
n_no, left_no, wf_no = run(False)
print("10b norm: no absorber start=%.6f end=%.6f ; absorber start=%.6f end=%.6f"
      % (n_no[0], n_no[-1], n_abs[0], n_abs[-1]))
print("10b norm loss (absorbed fraction) = %.6f" % (1.0 - n_abs[-1]))
print("10b max left-region density after t>4 (wraparound): no-absorber=%.4e absorber=%.4e"
      % (left_no.max(), left_abs.max()))
print("10b suppression factor = %.2e" % (left_abs.max() / max(left_no.max(), 1e-300)))
# instantaneous norm loss rate at the end
rate = (n_abs[-2] - n_abs[-1]) / dt
print("10b instantaneous norm loss rate |dn/dt| at end = %.4e" % abs(rate))

# 10c. stability across orders 1..6 (packet injected into the layer)
print("10c stability (300 steps, packet started inside the right layer):")
for order in range(1, 7):
    abl = AbsorbingBoundaryLayer(grid, boundary_width=3.0, order=order)
    sol = SplitOperatorSolver(grid, None, dt=dt, absorber=abl)
    wf = WaveFunction1D.gaussian(grid, L / 2.0 - 2.0, -2.0, 0.6)
    ok = True
    for _ in range(300):
        wf = sol.step(wf)
        if not np.all(np.isfinite(wf.psi)):
            ok = False
            break
    print("10c order=%d finite=%s  norm_end=%.6e  max|psi|=%.4e"
          % (order, ok, wf.norm(), np.max(np.abs(wf.psi))))
print("=== end Domain 10 ===")
