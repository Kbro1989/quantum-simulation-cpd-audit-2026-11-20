"""Domain 3: Wavefunction normalization.

Constructs Gaussians on 1D/2D/3D grids, checks the analytic norm, and measures
norm drift under free-particle and harmonic-oscillator propagation.
"""
import numpy as np

from quantumlab.core.grid import Grid1D, Grid2D, Grid3D
from quantumlab.core.wavefunction import WaveFunction1D, WaveFunction2D, WaveFunction3D
from quantumlab.potentials.oscillator import HarmonicOscillator
from quantumlab.solvers.split_operator import SplitOperatorSolver

print("=== Domain 3: Wavefunction normalization ===")
hbar, m = 1.0, 1.0

# --- analytic norm of the class Gaussians ---
g1 = Grid1D(256, -12.0, 12.0)
w1 = WaveFunction1D.gaussian(g1, 0.5, 0.8, 0.6)
g2 = Grid2D(64, -8.0, 8.0, 64, -8.0, 8.0)
w2 = WaveFunction2D.gaussian(g2, 0.3, -0.2, 0.5, 0.1, 0.6, 0.7)
g3 = Grid3D(24, -6.0, 6.0, 24, -6.0, 6.0, 24, -6.0, 6.0)
w3 = WaveFunction3D.gaussian(g3, 0.2, 0.1, -0.1, 0.4, 0.2, 0.1, 0.5, 0.6, 0.7)
print("3a norm 1D Gaussian = %.15f" % w1.norm())
print("3a norm 2D Gaussian = %.15f" % w2.norm())
print("3a norm 3D Gaussian = %.15f" % w3.norm())

# --- free particle: U_T is unitary, U_V = 1 -> norm must be preserved ---
dt = 0.01
sol_free = SplitOperatorSolver(g1, None, dt, hbar=hbar, m=m)
wf = w1
n0 = wf.norm()
drift_free = []
for _ in range(300):
    wf = sol_free.step(wf)
    drift_free.append(wf.norm() - n0)
print("3b free 300 steps: norm0 = %.15f  norm_end = %.15f  max|drift| = %.3e"
      % (n0, wf.norm(), np.max(np.abs(drift_free))))

# --- harmonic oscillator: unitary Strang, norm preserved to roundoff ---
V = HarmonicOscillator(omega=1.0, m=1.0)
sol_ho = SplitOperatorSolver(g1, V, dt, hbar=hbar, m=m)
wf = w1
n0 = wf.norm()
drift_ho = []
for _ in range(300):
    wf = sol_ho.step(wf)
    drift_ho.append(wf.norm() - n0)
print("3c HO 300 steps  : norm0 = %.15f  norm_end = %.15f  max|drift| = %.3e"
      % (n0, wf.norm(), np.max(np.abs(drift_ho))))

# --- 2D / 3D free drift ---
sol2 = SplitOperatorSolver(g2, None, dt, hbar=hbar, m=m)
wf2 = w2
n0 = wf2.norm()
for _ in range(100):
    wf2 = sol2.step(wf2)
print("3d 2D free 100 steps: norm0 = %.15f  norm_end = %.15f  |drift| = %.3e"
      % (n0, wf2.norm(), abs(wf2.norm() - n0)))

sol3 = SplitOperatorSolver(g3, None, dt, hbar=hbar, m=m)
wf3 = w3
n0 = wf3.norm()
for _ in range(50):
    wf3 = sol3.step(wf3)
print("3e 3D free 50 steps : norm0 = %.15f  norm_end = %.15f  |drift| = %.3e"
      % (n0, wf3.norm(), abs(wf3.norm() - n0)))
print("=== end Domain 3 ===")
