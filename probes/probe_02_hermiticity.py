"""Domain 2: Hamiltonian construction and Hermiticity.

Checks that the k-space kinetic operator is real, non-negative and symmetric
under k -> -k, and that the discrete Hamiltonian H = -hbar^2/2m laplacian + V
is Hermitian (matrix and matrix-free tests) for a non-trivial potential.
"""
import numpy as np
from numpy.fft import fft, ifft

from quantumlab.core.grid import Grid1D, Grid2D
from quantumlab.core.spectral import k_squared
from quantumlab.potentials.oscillator import HarmonicOscillator
from quantumlab.stationary.hamiltonian import apply_hamiltonian

print("=== Domain 2: Hamiltonian construction and Hermiticity ===")
hbar, m = 1.0, 1.0

# --- 1D matrix construction ---
N, L = 32, 16.0
grid = Grid1D(N, -L / 2.0, L / 2.0)
V = HarmonicOscillator(omega=1.7, m=m).evaluate(grid)
T_k = hbar ** 2 * grid.k ** 2 / (2.0 * m)

print("2a T_k all real        :", bool(np.all(np.isreal(T_k))))
print("2a T_k min             : %.6e  (must be >= 0)" % T_k.min())
idx = np.mod(-np.arange(N), N)
print("2a T_k[j] == T_k[-j]   :", bool(np.allclose(T_k, T_k[idx])))
print("2a T_k symmetric matrix:", bool(np.allclose(np.diag(T_k), np.diag(T_k)[idx])))

F = fft(np.eye(N))                       # F[j,k] = exp(-2 pi i jk/N)
Hkin = (F.conj().T @ (T_k[:, None] * F)) / N
H = Hkin + np.diag(V)
print("2b max|H - H^dagger|   : %.3e" % np.max(np.abs(H - H.conj().T)))
print("2b max|H - H^T| (real) : %.3e" % np.max(np.abs(H - H.T)))
print("2b max|Im(H)|          : %.3e  (roundoff; H is real-symmetric)"
      % np.max(np.abs(np.imag(H))))

rng = np.random.default_rng(7)
psi = rng.standard_normal(N) + 1j * rng.standard_normal(N)
E = np.vdot(psi, H @ psi)
print("2c <psi|H|psi>         : %.12f %+.12ej  (imag must be ~0)"
      % (E.real, E.imag))

# matrix-free apply_hamiltonian vs explicit matrix
Hpsi = apply_hamiltonian(psi, grid, V, hbar=hbar, m=m)
print("2d max|apply_hamiltonian - H@psi| : %.3e"
      % np.max(np.abs(Hpsi - H @ psi)))

# matrix-free Hermiticity: <psi|H|phi> == <H psi|phi>
phi = rng.standard_normal(N) + 1j * rng.standard_normal(N)
lhs = np.vdot(psi, apply_hamiltonian(phi, grid, V, hbar=hbar, m=m))
rhs = np.vdot(apply_hamiltonian(psi, grid, V, hbar=hbar, m=m), phi)
print("2e |<psi|H|phi> - <Hpsi|phi>|    : %.3e" % abs(lhs - rhs))

# --- 2D matrix-free Hermiticity with a non-trivial potential ---
grid2 = Grid2D(24, -8.0, 8.0, 24, -8.0, 8.0)
V2 = HarmonicOscillator(omega=1.3, m=1.0).evaluate(grid2)
T2 = hbar ** 2 * k_squared(grid2) / (2.0 * m)
print("2f 2D T_k all real     :", bool(np.all(np.isreal(T2))),
      " min: %.6e" % T2.min())
p2 = rng.standard_normal(grid2.shape) + 1j * rng.standard_normal(grid2.shape)
q2 = rng.standard_normal(grid2.shape) + 1j * rng.standard_normal(grid2.shape)
lhs2 = np.vdot(p2, apply_hamiltonian(q2, grid2, V2, hbar=hbar, m=m))
rhs2 = np.vdot(apply_hamiltonian(p2, grid2, V2, hbar=hbar, m=m), q2)
print("2g 2D |<psi|H|phi> - <Hpsi|phi>| : %.3e" % abs(lhs2 - rhs2))
print("=== end Domain 2 ===")
