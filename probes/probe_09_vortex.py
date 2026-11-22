"""Domain 9: Vortex winding and topological charge.

Builds analytic vortex / vortex-antivortex states, runs vortex_positions, and
independently recomputes each winding number with a contour integral
(1/2pi) * sum of wrapped phase differences around a circle sampled with
scipy.ndimage.map_coordinates.
"""
import numpy as np
from scipy.ndimage import map_coordinates

from quantumlab.core.grid import Grid2D, Grid3D
from quantumlab.core.wavefunction import WaveFunction2D, WaveFunction3D
from quantumlab.observables import vortex_positions

print("=== Domain 9: Vortex winding and topological charge ===")
L, N = 12.0, 160
grid = Grid2D(N, -L / 2.0, L / 2.0, N, -L / 2.0, L / 2.0)
X, Y = grid.X, grid.Y


def contour_winding(psi, xv, yv, R, M=720):
    """Independent winding number from a circular contour integral."""
    th = np.linspace(0.0, 2.0 * np.pi, M, endpoint=False)
    xs = xv + R * np.cos(th)
    ys = yv + R * np.sin(th)
    coords = np.vstack([(xs - grid.x[0]) / grid.dx, (ys - grid.y[0]) / grid.dy])
    vals = map_coordinates(psi, coords, order=1, mode='nearest')
    ph = np.angle(vals)
    dphi = np.diff(np.concatenate([ph, ph[:1]]))
    dphi = (dphi + np.pi) % (2.0 * np.pi) - np.pi
    return dphi.sum() / (2.0 * np.pi)


# --- single vortex with a hollow core (core deliberately off-grid) ---
x0, y0 = -1.37, 0.83
r = np.sqrt((X - x0) ** 2 + (Y - y0) ** 2)
theta = np.arctan2(Y - y0, X - x0)
sigma = 1.2
psi = (r / sigma) * np.exp(-r ** 2 / (4.0 * sigma ** 2)) * np.exp(1j * theta)
wf = WaveFunction2D(grid, psi)
wf.normalize()
pos, q = vortex_positions(wf, min_density=0.05, smoothing=0.6)
print("9a single vortex: detected %d vortex(es)" % len(pos))
for (px, py), qq in zip(pos, q):
    w = contour_winding(wf.psi, px, py, R=0.8)
    print("9a  pos=(%+.4f, %+.4f)  q_reported=%+d  q_contour=%+.4f  (true core at %+.2f, %+.2f)"
          % (px, py, qq, w, x0, y0))
if len(pos):
    print("9a  position error = %.4f" % np.min(np.hypot(pos[:, 0] - x0, pos[:, 1] - y0)))
else:
    print("9a  position error = NOT_RUN (no vortex detected)")

# --- vortex-antivortex pair ---
x1, y1 = -2.13, 0.17
x2, y2 = 2.07, -0.11
th1 = np.arctan2(Y - y1, X - x1)
th2 = np.arctan2(Y - y2, X - x2)
r1 = np.sqrt((X - x1) ** 2 + (Y - y1) ** 2)
r2 = np.sqrt((X - x2) ** 2 + (Y - y2) ** 2)
psi2 = np.exp(-(r1 ** 2 + r2 ** 2) / (8.0 * sigma ** 2)) * np.exp(1j * (th1 - th2))
wf2 = WaveFunction2D(grid, psi2)
wf2.normalize()
pos2, q2 = vortex_positions(wf2, min_density=0.05, smoothing=0.6)
print("9b pair: detected %d vortex(es), charges %s, sum = %+d"
      % (len(pos2), q2.tolist(), int(np.sum(q2))))
for (px, py), qq in zip(pos2, q2):
    w = contour_winding(wf2.psi, px, py, R=0.8)
    print("9b  pos=(%+.4f, %+.4f)  q_reported=%+d  q_contour=%+.4f" % (px, py, qq, w))

# --- no vortex ---
psi3 = np.exp(-(X ** 2 + Y ** 2) / (4.0 * sigma ** 2))
wf3 = WaveFunction2D(grid, psi3)
wf3.normalize()
pos3, q3 = vortex_positions(wf3)
print("9c Gaussian (no vortex): detected %d vortex(es) (expect 0)" % len(pos3))

# --- 3D guard ---
g3 = Grid3D(8, -2, 2, 8, -2, 2, 8, -2, 2)
wf3d = WaveFunction3D(g3, np.exp(-(g3.X ** 2 + g3.Y ** 2 + g3.Z ** 2) / 2.0)
                      * np.exp(1j * np.arctan2(g3.Y, g3.X)))
try:
    vortex_positions(wf3d)
    print("9d 3D input: NO ERROR (unexpected)")
except TypeError as exc:
    print("9d 3D input: TypeError: %s" % exc)
print("=== end Domain 9 ===")
