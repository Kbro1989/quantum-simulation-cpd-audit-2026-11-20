"""Domain 4: Fourier-space operators.

Checks fftfreq ordering, Parseval normalization, periodicity/spectral
derivatives, and aliasing of a mode near the Nyquist limit.
"""
import numpy as np
from numpy.fft import fft, ifft, fftfreq

from quantumlab.core.grid import Grid1D
from quantumlab.core.wavefunction import WaveFunction1D

print("=== Domain 4: Fourier-space operators ===")
N, L = 64, 16.0
dx = L / N
grid = Grid1D(N, -L / 2.0, L / 2.0)

# 4a. fftfreq ordering
k_ref = 2.0 * np.pi * fftfreq(N, dx)
print("4a max|grid.k - 2*pi*fftfreq(N,dx)| = %.3e"
      % np.max(np.abs(grid.k - k_ref)))
print("4a k[0:4] = %s   k[N-3:N] = %s"
      % (np.array2string(grid.k[:4], precision=4),
         np.array2string(grid.k[-3:], precision=4)))
print("4a dk = %.6f  2*pi/L = %.6f" % (grid.dk, 2 * np.pi / L))

# 4b. Parseval: int |psi|^2 dx == int |phi|^2 dk
psi = WaveFunction1D.gaussian(grid, 0.4, 1.1, 0.7)
phi = psi.fourier_transform()
lhs = np.sum(np.abs(psi.psi) ** 2) * dx
rhs = np.sum(np.abs(phi) ** 2) * grid.dk
print("4b Parseval: sum|psi|^2 dx = %.15f   sum|phi|^2 dk = %.15f   diff = %.3e"
      % (lhs, rhs, abs(lhs - rhs)))

# 4c. periodicity: spectral derivative of each grid mode is exact
err = 0.0
for j in range(N):
    mode = np.exp(1j * grid.k[j] * grid.x)
    d = ifft(1j * grid.k * fft(mode))
    err = max(err, np.max(np.abs(d - 1j * grid.k[j] * mode)))
print("4c max_j max_x |ifft(i k fft(e^{ik_j x})) - i k_j e^{ik_j x}| = %.3e" % err)

# 4d. aliasing: a mode above Nyquist folds back by -2*k_Nyq.
# k_Nyq = 32*dk for N=64, so k = 34*dk aliases to -30*dk (bin 34).
k_nyq = np.pi / dx
for mult, label in ((2, "k_Nyq + 2*dk = 34*dk"),
                    (-2, "k_Nyq - 2*dk = 30*dk"),
                    (0, "k_Nyq (exact)"),
                    (1, "k_Nyq + dk  = 33*dk")):
    k_test = k_nyq + mult * grid.dk
    mode = np.exp(1j * k_test * grid.x)
    spec = np.abs(fft(mode))
    j = int(np.argmax(spec))
    k_alias = k_test - 2 * k_nyq
    print("4d %-24s -> peak bin %2d, k = %+.4f, |peak| = %.3f ; alias predicts %+.4f"
          % (label, j, grid.k[j], spec[j], k_alias))

# 4e. kinetic phase at Nyquist
T_nyq = grid.k[int(N / 2)] ** 2 / 2.0
print("4e k_Nyq = %.6f   T_k(k_Nyq)/hbar = %.6f" % (k_nyq, T_nyq))
print("=== end Domain 4 ===")
