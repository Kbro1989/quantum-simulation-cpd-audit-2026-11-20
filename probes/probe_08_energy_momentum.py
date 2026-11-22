"""Domain 8: Energy and momentum behaviour.

Harmonic-oscillator coherent-state energy conservation and free-particle
Ehrenfest theorem ( <x>(t) = x0 + p0 t/m , <p> = const , d<x>/dt = <p>/m ).
"""
import numpy as np

from quantumlab.core.grid import Grid1D
from quantumlab.core.wavefunction import WaveFunction1D
from quantumlab.observables import (
    position_expectation, momentum_expectation, total_energy_expectation)
from quantumlab.potentials.oscillator import HarmonicOscillator
from quantumlab.solvers.split_operator import SplitOperatorSolver

print("=== Domain 8: Energy and momentum behaviour ===")
hbar, m = 1.0, 1.0
grid = Grid1D(256, -16.0, 16.0)
dt = 0.01

# --- harmonic oscillator coherent state ---
x0, p0, omega = 1.5, 1.0, 1.0
V = HarmonicOscillator(omega=omega, m=m)
sol = SplitOperatorSolver(grid, V, dt=dt, hbar=hbar, m=m)
wf = WaveFunction1D.gaussian(grid, x0, p0, sigma=1.0 / np.sqrt(2.0))
E0 = total_energy_expectation(wf, V, hbar=hbar, m=m)
E_analytic = 0.5 * (p0 ** 2 + (m * omega * x0) ** 2) / m + 0.5 * hbar * omega
print("8a HO <H>(0) = %.10f   analytic = %.10f   diff = %.3e"
      % (E0, E_analytic, abs(E0 - E_analytic)))
drift = []
for _ in range(400):
    wf = sol.step(wf)
    drift.append(total_energy_expectation(wf, V, hbar=hbar, m=m) - E0)
print("8a HO 400 steps: max|<H>(t)-<H>(0)| = %.3e   final drift = %.3e"
      % (np.max(np.abs(drift)), drift[-1]))

# --- free particle Ehrenfest ---
sol_free = SplitOperatorSolver(grid, None, dt=dt, hbar=hbar, m=m)
wf = WaveFunction1D.gaussian(grid, -4.0, 2.0, sigma=0.8)
print("8b free particle (x0=-4, p0=2, m=1):")
prev_x = position_expectation(wf)
prev_t = 0.0
for n in (50, 100, 200, 400):
    while sol_free.steps_taken < n:
        wf = sol_free.step(wf)
    t = sol_free.steps_taken * dt
    x = position_expectation(wf)
    p = momentum_expectation(wf, 'x', hbar=hbar)
    print("8b t=%.2f  <x>=%.8f (expect %.8f, err %.2e)  <p>=%.10f (expect 2)"
          % (t, x, -4.0 + 2.0 * t, abs(x - (-4.0 + 2.0 * t)), p))
# d<x>/dt vs <p>/m
wf = WaveFunction1D.gaussian(grid, -4.0, 2.0, sigma=0.8)
sol_free2 = SplitOperatorSolver(grid, None, dt=dt, hbar=hbar, m=m)
x_a = position_expectation(wf)
wf = sol_free2.step(wf)
x_b = position_expectation(wf)
p_avg = 0.5 * (momentum_expectation(wf, 'x') + momentum_expectation(wf, 'x'))
print("8b d<x>/dt = %.6f   <p>/m = %.6f   diff = %.2e"
      % ((x_b - x_a) / dt, p_avg / m, abs((x_b - x_a) / dt - p_avg / m)))
print("=== end Domain 8 ===")
