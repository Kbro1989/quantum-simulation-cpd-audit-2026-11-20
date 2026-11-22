"""Domain 12: Numerical stability and resolution sensitivity.

Sweeps N at fixed physical setup (harmonic-oscillator coherent state) and
sweeps dt at fixed N, and checks the documented parametric-instability
condition hbar*k_max^2*|w|*dt/(2m) < pi.
"""
import numpy as np

from quantumlab.core.grid import Grid1D
from quantumlab.core.wavefunction import WaveFunction1D
from quantumlab.potentials.oscillator import HarmonicOscillator
from quantumlab.solvers.split_operator import SplitOperatorSolver

print("=== Domain 12: Stability and resolution sensitivity ===")
hbar = m = 1.0
omega = 1.0
x0, p0 = 2.0, 1.5
T = 0.5
L = 40.0
V = HarmonicOscillator(omega=omega, m=m)


def exact(grid, t):
    X = x0 * np.cos(omega * t) + (p0 / (m * omega)) * np.sin(omega * t)
    P = p0 * np.cos(omega * t) - m * omega * x0 * np.sin(omega * t)
    return np.pi ** -0.25 * np.exp(-(grid.x - X) ** 2 / 2.0) \
        * np.exp(1j * (P * grid.x - P * X / 2.0 - 0.5 * omega * t))


# 12a. sweep N at fixed dt
dt_fixed = 0.002
print("12a N sweep at fixed dt=%.4f (T=%.2f, %d steps):" % (dt_fixed, T, int(T / dt_fixed)))
for N in (64, 128, 256, 512, 1024):
    grid = Grid1D(N, -L / 2.0, L / 2.0)
    psi0 = WaveFunction1D(grid, exact(grid, 0.0))
    sol = SplitOperatorSolver(grid, V, dt=dt_fixed, hbar=hbar, m=m)
    wf = psi0
    for _ in range(int(T / dt_fixed)):
        wf = sol.step(wf)
    err = float(np.max(np.abs(wf.psi - exact(grid, T))))
    kmax = np.pi / grid.dx
    print("12a N=%4d dx=%.5f k_max=%.2f  max|dpsi|=%.4e  stability param k_max^2*dt/2=%.3f"
          % (N, grid.dx, kmax, err, kmax ** 2 * dt_fixed / 2.0))

# 12b. sweep dt at fixed N
N_fixed = 512
grid = Grid1D(N_fixed, -L / 2.0, L / 2.0)
psi0 = WaveFunction1D(grid, exact(grid, 0.0))
print("12b dt sweep at fixed N=%d:" % N_fixed)
for nsteps in (64, 128, 256, 512):
    dt = T / nsteps
    sol = SplitOperatorSolver(grid, V, dt=dt, hbar=hbar, m=m)
    wf = psi0
    for _ in range(nsteps):
        wf = sol.step(wf)
    err = float(np.max(np.abs(wf.psi - exact(grid, T))))
    print("12b dt=%.6f  max|dpsi|=%.4e" % (dt, err))

# 12c. parametric instability threshold
print("12c stability condition hbar*k_max^2*|w|*dt/(2m) < pi (order 2, |w|=1):")
for N in (64, 128, 256):
    grid = Grid1D(N, -L / 2.0, L / 2.0)
    kmax = np.pi / grid.dx
    dt_crit = 2.0 * np.pi / kmax ** 2
    psi0 = WaveFunction1D(grid, exact(grid, 0.0))
    for factor in (0.5, 2.0):
        dt = factor * dt_crit
        sol = SplitOperatorSolver(grid, V, dt=dt, hbar=hbar, m=m)
        wf = psi0
        for _ in range(200):
            wf = sol.step(wf)
        err = float(np.max(np.abs(wf.psi - exact(grid, 200 * dt))))
        print("12c N=%3d dt=%.5f (%.1f*dt_crit)  max|psi|=%.4e  max|dpsi| vs exact=%.4e"
              % (N, dt, factor, np.max(np.abs(wf.psi)), err))
print("=== end Domain 12 ===")
