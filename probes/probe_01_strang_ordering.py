"""Domain 1: Schrodinger evolution and split-operator ordering.

Checks the Strang sequence V/2, T, V/2 in split_step_1d.py and
split_operator.py against an independent manual product, and checks the
self-adjointness (S^dagger S = I) that a symmetric splitting must have.
"""
import numpy as np
from numpy.fft import fft, ifft, fft2, ifft2

from quantumlab.core.grid import Grid1D, Grid2D
from quantumlab.core.wavefunction import WaveFunction1D, WaveFunction2D
from quantumlab.potentials.oscillator import HarmonicOscillator
from quantumlab.solvers.split_step_1d import SplitStep1DSolver
from quantumlab.solvers.split_operator import (
    SplitOperatorSolver, YOSHIDA_W0, YOSHIDA_W1)

print("=== Domain 1: Strang ordering V/2, T, V/2 ===")
hbar, m, dt = 1.0, 1.0, 0.05
grid = Grid1D(128, -12.0, 12.0)
V = HarmonicOscillator(omega=1.3, m=m)
sol = SplitStep1DSolver(grid, V, dt, hbar=hbar, m=m)
psi0 = WaveFunction1D.gaussian(grid, x0=1.0, k0=0.7, sigma=0.6)

# 1a. manual V/2, T, V/2 product
psi = psi0.psi.copy()
psi *= sol.U_V
psi = ifft(fft(psi) * sol.U_T)
psi *= sol.U_V
num = sol.step(psi0)
print("1a split_step_1d  max|step - manual(V/2,T,V/2)| = %.3e"
      % np.max(np.abs(num.psi - psi)))

# 1b. unitarity: S^dagger S = I.  S = U_V K U_V with K = ifft(U_T fft(.)),
# so S^dagger = U_V^* K^dagger U_V^* (U_V is complex, K^dagger = ifft(U_T^* fft(.))).
Spsi = num.psi
adj = Spsi * np.conj(sol.U_V)
adj = ifft(np.conj(sol.U_T) * fft(adj))
adj *= np.conj(sol.U_V)
print("1b split_step_1d  max|S^dagger S psi - psi|      = %.3e"
      % np.max(np.abs(adj - psi0.psi)))
print("1b norm(S psi) = %.15f   norm(psi) = %.15f"
      % (np.sum(np.abs(Spsi) ** 2) * grid.dx, psi0.norm()))

# 1b2. backward-then-forward: S(dt) S(-dt) = I (time-reversal property)
sol_back = SplitStep1DSolver(grid, V, -dt, hbar=hbar, m=m)
back = sol_back.step(num)
print("1b2 split_step_1d max|S(-dt) S(dt) psi - psi|    = %.3e"
      % np.max(np.abs(back.psi - psi0.psi)))

# 1c. ordering matters: Strang vs naive full-V then T
psi = psi0.psi.copy()
psi *= np.exp(-1j * sol.V * dt / hbar)
psi = ifft(fft(psi) * sol.U_T)
print("1c split_step_1d  max|Strang - naive(V,T)|       = %.3e"
      % np.max(np.abs(num.psi - psi)))

# 1d. split_operator order=2 manual product
sol2 = SplitOperatorSolver(grid, V, dt, hbar=hbar, m=m, order=2)
UV = np.exp(-1j * sol2.potential_at(0.0) * dt / (2.0 * hbar))
UT = np.exp(-1j * sol2._T_k * dt / hbar)
psi = ifft(fft(psi0.psi * UV) * UT) * UV
print("1d split_operator o2 max|step - manual(V/2,T,V/2)| = %.3e"
      % np.max(np.abs(sol2.step(psi0).psi - psi)))

# 1e. Yoshida weights and order-4 composition
print("1e YOSHIDA_W1 = %.12f  YOSHIDA_W0 = %.12f  2*W1+W0 = %.15f"
      % (YOSHIDA_W1, YOSHIDA_W0, 2.0 * YOSHIDA_W1 + YOSHIDA_W0))
sol4 = SplitOperatorSolver(grid, V, dt, hbar=hbar, m=m, order=4)
print("1e order-4 substeps = %s  sum = %.15f"
      % (tuple(sol4._substeps), sum(sol4._substeps)))
psi = psi0.psi.copy()
for w in sol4._substeps:
    h = w * dt
    UVw = np.exp(-1j * sol4.potential_at(0.0) * h / (2.0 * hbar))
    UTw = np.exp(-1j * sol4._T_k * h / hbar)
    psi = ifft(fft(psi * UVw) * UTw) * UVw
print("1e split_operator o4 max|step - manual composition| = %.3e"
      % np.max(np.abs(sol4.step(psi0).psi - psi)))

# 1f. split_operator 2D ordering
grid2 = Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0)
V2 = HarmonicOscillator(omega=1.0, m=1.0)
sol2d = SplitOperatorSolver(grid2, V2, dt, hbar=hbar, m=m, order=2)
psi0_2d = WaveFunction2D.gaussian(grid2, 0.5, -0.3, 0.4, 0.2, 0.6, 0.7)
UV2 = np.exp(-1j * sol2d.potential_at(0.0) * dt / (2.0 * hbar))
UT2 = np.exp(-1j * sol2d._T_k * dt / hbar)
psi = ifft2(fft2(psi0_2d.psi * UV2) * UT2) * UV2
print("1f split_operator 2D o2 max|step - manual(V/2,T,V/2)| = %.3e"
      % np.max(np.abs(sol2d.step(psi0_2d).psi - psi)))

# 1g. unitarity of split_operator order 2 (2D)
S2 = sol2d.step(psi0_2d).psi
adj = S2 * np.conj(UV2)
adj = ifft2(np.conj(UT2) * fft2(adj)) * np.conj(UV2)
print("1g split_operator 2D o2 max|S^dagger S psi - psi| = %.3e"
      % np.max(np.abs(adj - psi0_2d.psi)))
print("=== end Domain 1 ===")
