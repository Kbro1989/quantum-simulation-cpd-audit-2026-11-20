"""Domain 11: CPU/GPU numerical equivalence.

Compares SplitOperatorSolver (numpy vs cupy) and SplitStep3DSolver vs
SplitStep3DGPU on identical inputs; reports max|dpsi|.
"""
import numpy as np

from quantumlab.core.grid import Grid1D, Grid2D, Grid3D
from quantumlab.core.wavefunction import WaveFunction1D, WaveFunction2D, WaveFunction3D
from quantumlab.potentials.oscillator import HarmonicOscillator
from quantumlab.solvers.split_operator import SplitOperatorSolver
from quantumlab.solvers.split_step_3d import SplitStep3DSolver

print("=== Domain 11: CPU/GPU numerical equivalence ===")
hbar, m, dt = 1.0, 1.0, 0.01

# warm-up GPU (context init, FFT plans)
g0 = Grid1D(32, -4.0, 4.0)
SplitOperatorSolver(g0, None, dt, backend='cupy').step(
    WaveFunction1D.gaussian(g0, 0.0, 0.5, 0.5))
print("11 GPU warm-up step completed")

# 11a. 1D
g1 = Grid1D(128, -10.0, 10.0)
V1 = HarmonicOscillator(1.3, m=1.0)
psi0 = WaveFunction1D.gaussian(g1, 0.7, 0.9, 0.6)
cpu = SplitOperatorSolver(g1, V1, dt, hbar=hbar, m=m, backend='numpy')
gpu = SplitOperatorSolver(g1, V1, dt, hbar=hbar, m=m, backend='cupy')
wc, wg = psi0, psi0
for _ in range(50):
    wc = cpu.step(wc)
    wg = gpu.step(wg)
d = np.max(np.abs(wc.psi - wg.psi))
print("11a 1D 50 steps: max|dpsi| = %.3e   (norm cpu=%.15f gpu=%.15f)"
      % (d, wc.norm(), wg.norm()))

# 11b. 2D
g2 = Grid2D(48, -8.0, 8.0, 48, -8.0, 8.0)
V2 = HarmonicOscillator(1.0, m=1.0)
psi0 = WaveFunction2D.gaussian(g2, 0.4, -0.3, 0.5, 0.2, 0.6, 0.7)
cpu = SplitOperatorSolver(g2, V2, dt, hbar=hbar, m=m, backend='numpy')
gpu = SplitOperatorSolver(g2, V2, dt, hbar=hbar, m=m, backend='cupy')
wc, wg = psi0, psi0
for _ in range(30):
    wc = cpu.step(wc)
    wg = gpu.step(wg)
d = np.max(np.abs(wc.psi - wg.psi))
print("11b 2D 30 steps: max|dpsi| = %.3e" % d)

# 11c. 3D dedicated GPU solver vs CPU 3D solver
g3 = Grid3D(20, -6.0, 6.0, 20, -6.0, 6.0, 20, -6.0, 6.0)
V3 = HarmonicOscillator(1.0, m=1.0)
psi0 = WaveFunction3D.gaussian(g3, 0.2, 0.1, -0.1, 0.3, 0.2, 0.1, 0.5, 0.6, 0.7)
cpu3 = SplitStep3DSolver(g3, V3, dt, hbar=hbar, m=m)
try:
    from quantumlab.solvers.split_step_3d_gpu import SplitStep3DGPU
    gpu3 = SplitStep3DGPU(g3, V3, dt, hbar=hbar, m=m)
    wc, wg = psi0, psi0
    for _ in range(20):
        wc = cpu3.step(wc)
        wg = gpu3.step(wg)
    d = np.max(np.abs(wc.psi - wg.psi))
    print("11c 3D 20 steps: max|dpsi| = %.3e  (gpu backend=%s)"
          % (d, gpu3.backend))
except Exception as exc:
    print("11c 3D GPU comparison NOT_RUN: %s: %s" % (type(exc).__name__, exc))
print("=== end Domain 11 ===")
