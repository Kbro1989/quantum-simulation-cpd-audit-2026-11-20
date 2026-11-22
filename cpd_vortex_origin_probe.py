import numpy as np, math, sys
sys.path.insert(0, r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main")
from quantumlab.core.grid import Grid3D
from quantumlab.potentials.traps import HarmonicTrap
from quantumlab.solvers.split_operator import SplitOperatorSolver

N, BOX, DT, STEPS, HBAR, MASS = 48, (-6.0, 6.0), 0.005, 40, 1.0, 1.0
grid = Grid3D(N, BOX[0], BOX[1], N, BOX[0], BOX[1], N, BOX[0], BOX[1])
trap = HarmonicTrap(omegas=1.0, m=1.0)
X, Y, Z = np.meshgrid(grid.x, grid.x, grid.x, indexing="ij")
psi = np.exp(-(X**2 + Y**2 + Z**2) / 4.0) * np.exp(1j * np.arctan2(Y, X))
psi /= np.sqrt(np.mean(np.abs(psi)**2))
solver = SplitOperatorSolver(grid, trap, DT, HBAR, MASS, order=2)

print("z-slice index of the vortex line:", int(np.argmin(np.abs(grid.z))), "in the z=0 slice")
z_idx = int(np.argmin(np.abs(grid.z)))

ks = (0, 10, 20, 30, 40)
print("\nPhase winding around a loop of radius R=5 grid units, centred at the ORIGIN,",
      "on the z=0 slice:")
print(f"{'step':>4s}  {'vortex_charge':>12s}  {'circ_hbar_over_m':>15s}  {'ratio':>8s}")
for k in range(STEPS + 1):
    if k in ks:
        sl = psi[:, :, z_idx]
        phi = np.linspace(0, 2 * np.pi, 720, endpoint=False)
        px = 5.0 * np.cos(phi)
        py = 5.0 * np.sin(phi)
        ix = np.clip((px - grid.x[0]) / grid.dx, 0, len(grid.x) - 1.001)
        iy = np.clip((py - grid.y[0]) / grid.dy, 0, len(grid.y) - 1.001)
        i0, j0 = ix.astype(int), iy.astype(int)
        fx, fy = ix - i0, iy - j0
        v = ((1 - fx) * (1 - fy) * sl[i0, j0] + fx * (1 - fy) * sl[i0 + 1, j0]
             + (1 - fx) * fy * sl[i0, j0 + 1] + fx * fy * sl[i0 + 1, j0 + 1])
        dphi = np.angle(v[1:] * np.conj(v[:-1]))
        dphi = np.append(dphi, np.angle(v[0] * np.conj(v[-1])))
        W = float(np.sum(dphi) / (2 * np.pi))
        circ = float((HBAR / MASS) * np.sum(dphi))
        print(f"{k:4d}  {W:12.3f}  {circ:15.6f}  {circ / (2 * math.pi * HBAR / MASS):8.4f}")
    if k < STEPS:
        psi = solver.step(psi)

rho = np.abs(psi.psi) ** 2
axis = rho[N // 2, N // 2, :]
print(f"\n|m|2 along z at (x,y)=(0,0): min={float(axis.min()):.6f} max={float(axis.max()):.6f}")
