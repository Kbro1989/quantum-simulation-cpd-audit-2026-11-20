"""Domain 6: Time-dependent Hamiltonians.

Checks DipoleDrive / sin2_envelope / flat_top_envelope evaluate_at behaviour,
instruments the times at which SplitOperatorSolver samples V(r,t), and checks
whether the legacy solvers honour time dependence.
"""
import numpy as np

from quantumlab.core.grid import Grid1D
from quantumlab.core.wavefunction import WaveFunction1D
from quantumlab.potentials.base import Potential
from quantumlab.potentials.oscillator import HarmonicOscillator
from quantumlab.potentials.time_dependent import (
    DipoleDrive, sin2_envelope, flat_top_envelope)
from quantumlab.solvers.split_operator import SplitOperatorSolver
from quantumlab.solvers.split_step_1d import SplitStep1DSolver

print("=== Domain 6: Time-dependent Hamiltonians ===")
grid = Grid1D(128, -12.0, 12.0)

# 6a. DipoleDrive force and evaluate_at
dd = DipoleDrive(HarmonicOscillator(1.0, m=1.0), F0=2.0, omega=3.0,
                 axis='x', phase=0.5, envelope=sin2_envelope(2.0))
ts = np.array([0.0, 0.25, 0.5, 1.0, 1.5, 2.0, 2.5])
for t in ts:
    expect = 2.0 * float(np.sin(np.pi * t / 2.0) ** 2) * np.sin(3.0 * t + 0.5) \
        if 0.0 < t < 2.0 else 0.0
    print("6a t=%.2f force=%.10f expect=%.10f diff=%.2e"
          % (t, dd.force(t), expect, abs(dd.force(t) - expect)))
Vb = dd.base.evaluate(grid)
V = dd.evaluate_at(grid, 0.7)
F = dd.force(0.7)
print("6a max|evaluate_at(t) - (V_base - F(t) x)| = %.3e"
      % np.max(np.abs(V - (Vb - F * grid.x))))

# 6b. sin2_envelope shape
env = sin2_envelope(2.0)
print("6b sin2: env(0)=%.3f env(2)=%.3f env(1)=%.6f (expect 1) env(-1)=%.3f env(3)=%.3f"
      % (env(0.0), env(2.0), env(1.0), env(-1.0), env(3.0)))
# 6c. flat_top_envelope
ft = flat_top_envelope(4.0, 1.0)
print("6c flat_top: f(0)=%.3f f(4)=%.3f f(0.5)=%.6f f(2)=%.6f f(3.5)=%.6f"
      % (ft(0.0), ft(4.0), ft(0.5), ft(2.0), ft(3.5)))

# 6d. instrument evaluate_at call times in SplitOperatorSolver
class LoggingPotential(Potential):
    time_dependent = True

    def __init__(self):
        self.calls = []

    def evaluate(self, grid):
        return np.zeros(grid.shape)

    def evaluate_at(self, grid, t):
        self.calls.append(float(t))
        return np.zeros(grid.shape)


for order in (2, 4):
    lp = LoggingPotential()
    sol = SplitOperatorSolver(grid, lp, dt=0.1, order=order)
    psi0 = WaveFunction1D.gaussian(grid, 0.5, 0.0, 0.5)
    sol.step(psi0)
    print("6d order=%d evaluate_at times = %s" % (order, np.array(lp.calls)))

# 6e. legacy solver freezes V at t=0 (evaluate(grid) -> evaluate_at(grid, 0.0))
dd2 = DipoleDrive(HarmonicOscillator(1.0, m=1.0), F0=5.0, omega=4.0, axis='x', phase=0.0)
legacy = SplitStep1DSolver(grid, dd2, dt=0.05)
print("6e legacy V == DipoleDrive.evaluate_at(grid,0) (force=0): %s"
      % np.allclose(legacy.V, dd2.evaluate_at(grid, 0.0)))
print("6e legacy V == V_base: %s" % np.allclose(legacy.V, dd2.base.evaluate(grid)))

# 6f. legacy vs time-dependent-aware solver diverge
psi0 = WaveFunction1D.gaussian(grid, 0.5, 0.5, 0.5)
sol_td = SplitOperatorSolver(grid, dd2, dt=0.05, order=2)
wf_l = psi0
wf_t = psi0
for _ in range(20):
    wf_l = legacy.step(wf_l)
    wf_t = sol_td.step(wf_t)
print("6f after 20 steps max|psi_legacy - psi_td| = %.6f (nonzero => legacy ignores drive)"
      % np.max(np.abs(wf_l.psi - wf_t.psi)))
print("=== end Domain 6 ===")
