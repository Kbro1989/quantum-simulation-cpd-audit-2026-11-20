import numpy as np
from scipy.ndimage import gaussian_filter
from quantumlab.core.grid import Grid2D
from quantumlab.core.wavefunction import WaveFunction2D
from quantumlab.observables import vortex_positions

L, N = 12.0, 160
grid = Grid2D(N, -L / 2, L / 2, N, -L / 2, L / 2)
X, Y = grid.X, grid.Y
x0, y0 = -1.5, 0.8
r = np.sqrt((X - x0) ** 2 + (Y - y0) ** 2)
theta = np.arctan2(Y - y0, X - x0)
sigma = 1.2
psi = (r / sigma) * np.exp(-r ** 2 / (4.0 * sigma ** 2)) * np.exp(1j * theta)
wf = WaveFunction2D(grid, psi)
wf.normalize()
rho = wf.probability_density
print("rho max", rho.max(), "rho at core", rho[np.argmin(np.abs(grid.x - x0)), np.argmin(np.abs(grid.y - y0))])
for smoothing in (0.3, 0.6, 1.0):
    rs = gaussian_filter(rho, sigma=(smoothing / grid.dx, smoothing / grid.dy), mode='constant')
    i = np.argmin(np.abs(grid.x - x0)); j = np.argmin(np.abs(grid.y - y0))
    print("smoothing", smoothing, "smoothed max", rs.max(), "at core", rs[i, j],
          "ratio", rs[i, j] / rs.max())
pos, q = vortex_positions(wf, min_density=0.05, smoothing=0.6)
print("detected", len(pos), pos, q)
# raw circulation map
phase = np.angle(wf.psi)
def wrapped(a, b):
    return (b - a + np.pi) % (2 * np.pi) - np.pi
circ = (wrapped(phase[:-1, :-1], phase[1:, :-1]) + wrapped(phase[1:, :-1], phase[1:, 1:])
        + wrapped(phase[1:, 1:], phase[:-1, 1:]) + wrapped(phase[:-1, 1:], phase[:-1, :-1]))
nz = np.argwhere(np.abs(circ) > 0.1)
print("raw circulation nonzero plaquettes:", len(nz))
for i, j in nz[:10]:
    print("  plaquette", i, j, "circ", circ[i, j], "rho", rho[i, j])
