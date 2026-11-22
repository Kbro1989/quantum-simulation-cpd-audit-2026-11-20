"""Domain 7: Numerical convergence order on a harmonic-oscillator coherent state.

Exact reference (hbar = m = omega = 1), initial
  psi(x,0) = pi^-1/4 exp(-(x-x0)^2/2) exp(i p0 x - i p0 x0/2),
  X(t) = x0 cos t + p0 sin t,  P(t) = p0 cos t - x0 sin t,
  psi(x,t) = pi^-1/4 exp(-(x-X)^2/2) exp(i [P x - P X/2 - t/2]).
The potential is non-commuting (harmonic), so dt-refinement measures the
splitting order, not roundoff.
"""
import numpy as np

from quantumlab.core.grid import Grid1D
from quantumlab.core.wavefunction import WaveFunction1D
from quantumlab.potentials.oscillator import HarmonicOscillator
from quantumlab.solvers.split_operator import SplitOperatorSolver

print("=== Domain 7: Convergence order (harmonic oscillator coherent state) ===")
hbar = m = 1.0
omega = 1.0
x0, p0 = 2.0, 1.5
T = 0.5
L, N = 40.0, 256
grid = Grid1D(N, -L / 2.0, L / 2.0)
V = HarmonicOscillator(omega=omega, m=m)


def exact(t):
    X = x0 * np.cos(omega * t) + (p0 / (m * omega)) * np.sin(omega * t)
    P = p0 * np.cos(omega * t) - m * omega * x0 * np.sin(omega * t)
    psi = np.pi ** -0.25 * np.exp(-(grid.x - X) ** 2 / 2.0) \
        * np.exp(1j * (P * grid.x - P * X / 2.0 - 0.5 * omega * t))
    return psi, X, P


psi0 = WaveFunction1D(grid, exact(0.0)[0])

# warm-up on the timed code path (builds FFT plans / caches)
warm = SplitOperatorSolver(grid, V, dt=T / 64, hbar=hbar, m=m, order=2)
for _ in range(5):
    warm.step(psi0)
print("7 warm-up: 5 steps at dt=%.5f completed" % (T / 64.0))

psi_ex, X_ex, P_ex = exact(T)
print("7 exact X(T)=%.10f P(T)=%.10f" % (X_ex, P_ex))

for order in (2, 4):
    print("7 order=%d:" % order)
    errs = []
    dts = []
    for nsteps in (64, 128, 256, 512, 1024):
        dt = T / nsteps
        sol = SplitOperatorSolver(grid, V, dt=dt, hbar=hbar, m=m, order=order)
        wf = psi0
        for _ in range(nsteps):
            wf = sol.step(wf)
        err = float(np.max(np.abs(wf.psi - psi_ex)))
        ov = abs(np.vdot(psi_ex, wf.psi) * grid.dx)
        errs.append(err)
        dts.append(dt)
        print("7  nsteps=%4d dt=%.6f  max|dpsi|=%.4e  1-|overlap|=%.4e"
              % (nsteps, dt, err, 1.0 - ov))
    orders = [np.log(errs[i] / errs[i + 1]) / np.log(dts[i] / dts[i + 1])
              for i in range(len(errs) - 1)]
    print("7  empirical orders = %s" % np.array2string(np.array(orders), precision=3))
print("=== end Domain 7 ===")
