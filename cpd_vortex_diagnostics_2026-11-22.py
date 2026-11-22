#!/usr/bin/env python3
"""
cpd_vortex_diagnostics_2026-11-22.py

Topological validation of the vortex-line case, replacing the visual claim with
measurements.  Four diagnostics per recorded frame:

  D1  density minimum / zero set      - does a depleted core exist?
  D2  phase winding around a loop     - integer winding number?
  D3  vortex-line extraction          - core position and orientation per frame
  D4  circulation integral            - does it approach n*h/m?

Also fixes two visualisation defects in the asset suite:
  * thresholds are now FIXED GLOBAL fractions of the max over ALL frames
    (previously frame-relative, which changes the surface under normalisation)
  * the GIF is written with an explicit per-frame duration

Writes only inside the audit workspace.
"""
import json
import math
import sys
from pathlib import Path

import numpy as np

REPO = Path(r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main")
AUD = Path(r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20")
OUT = AUD / "quantum_3d_asset_suite"
IDX = AUD / "pks_research_index"
sys.path.insert(0, str(REPO))

from quantumlab.core.grid import Grid3D
from quantumlab.core.wavefunction import WaveFunction3D
from quantumlab.potentials.traps import HarmonicTrap
from quantumlab.solvers.split_operator import SplitOperatorSolver

N, BOX = 48, (-6.0, 6.0)
DT, STEPS, HBAR, MASS = 0.005, 40, 1.0, 1.0
FRAMES = [0, 10, 20, 30, 40]
GLOBAL_LEVELS = (0.50, 0.15, 0.03)   # of the GLOBAL max over all frames
GIF_DURATION_S = 0.5                  # explicit frame timing


def vortex_line_state(grid, sigma=1.0, charge=1):
    X, Y, Z = grid.X, grid.Y, grid.Z
    theta = np.arctan2(Y, X)
    psi = np.exp(-(X ** 2 + Y ** 2 + Z ** 2) / (4.0 * sigma ** 2)) * np.exp(1j * charge * theta)
    wf = WaveFunction3D(grid, psi.astype(complex))
    wf.normalize()
    return wf


def winding_around_loop(psi_slice, xs, ys, cx, cy, radius, npts=720):
    """Sum of phase increments around a closed circle in the slice -> winding number."""
    phi = np.linspace(0, 2 * np.pi, npts, endpoint=False)
    px = cx + radius * np.cos(phi)
    py = cy + radius * np.sin(phi)
    # bilinear sample of the complex field
    ix = np.clip((px - xs[0]) / (xs[1] - xs[0]), 0, len(xs) - 1.001)
    iy = np.clip((py - ys[0]) / (ys[1] - ys[0]), 0, len(ys) - 1.001)
    i0, j0 = ix.astype(int), iy.astype(int)
    fx, fy = ix - i0, iy - j0
    v = ((1 - fx) * (1 - fy) * psi_slice[i0, j0] + fx * (1 - fy) * psi_slice[i0 + 1, j0]
         + (1 - fx) * fy * psi_slice[i0, j0 + 1] + fx * fy * psi_slice[i0 + 1, j0 + 1])
    dphi = np.angle(v[1:] * np.conj(v[:-1]))
    dphi = np.append(dphi, np.angle(v[0] * np.conj(v[-1])))
    return float(np.sum(dphi) / (2 * np.pi)), float(np.sum(dphi))


def analyse(psi, grid, hbar=HBAR, m=MASS):
    rho = np.abs(psi) ** 2
    # The global density minimum sits in the Gaussian tail at the box corner, not at
    # the vortex core. Search the INTERIOR only, otherwise the loop is centred on the
    # boundary and the winding measurement is meaningless.
    margin = 4
    core_rho = rho[margin:-margin, margin:-margin, margin:-margin]
    imin = np.unravel_index(np.argmin(core_rho), core_rho.shape)
    imin = (imin[0] + margin, imin[1] + margin, imin[2] + margin)
    core = (float(grid.x[imin[0]]), float(grid.y[imin[1]]), float(grid.z[imin[2]]))

    # D3: refine the core in the plane nearest the density minimum
    k = imin[2]
    sl = psi[:, :, k]
    sub = np.abs(sl[margin:-margin, margin:-margin])
    jmin = np.unravel_index(np.argmin(sub), sub.shape)
    cx = float(grid.x[jmin[0] + margin])
    cy = float(grid.y[jmin[1] + margin])

    # D1b: density on the z-axis (the vortex line) - is the core depleted?
    core_axis = float(rho[len(grid.x) // 2, len(grid.y) // 2, :].min())

    # D2/D4: winding on circles of several radii around the core
    loops = []
    dx = grid.dx
    for radius in (2 * dx, 4 * dx, 8 * dx):
        n, total = winding_around_loop(sl, grid.x, grid.y, cx, cy, radius)
        loops.append({"radius_grid_units": round(radius, 6),
                      "winding_number": round(n, 6),
                      "circulation_phase_sum_rad": round(total, 6),
                      "circulation_hbar_over_m": round(hbar * total, 6),
                      "h_over_m": round(2 * math.pi * hbar / m, 6),
                      "ratio_to_h_over_m": round((hbar * total) / (2 * math.pi * hbar / m), 6)})
    return {
        "density_max": float(rho.max()),
        "density_min": float(rho.min()),
        "density_min_point": [round(c, 6) for c in core],
        "core_slice_xy": [round(cx, 6), round(cy, 6)],
        "core_slice_z": round(float(grid.z[k]), 6),
        "loops": loops,
    }


def main() -> None:
    grid = Grid3D(N, BOX[0], BOX[1], N, BOX[0], BOX[1], N, BOX[0], BOX[1])
    trap = HarmonicTrap(omegas=1.0, m=1.0)
    psi = vortex_line_state(grid)
    solver = SplitOperatorSolver(grid, trap, DT, HBAR, MASS, order=2, backend="numpy")

    snapshots = {}
    for k in range(0, STEPS + 1):
        if k in FRAMES:
            snapshots[k] = psi.psi.copy()
        if k < STEPS:
            psi = solver.step(psi)

    global_max = max(float(np.abs(v).max() ** 2) for v in snapshots.values())
    z_axis_sq = np.abs(snapshots[0][N // 2, N // 2, :]) ** 2
    core_axis = float(z_axis_sq.min())
    core_axis_pt = [round(float(grid.x[N // 2]), 6), round(float(grid.y[N // 2]), 6)]
    levels = [f * global_max for f in GLOBAL_LEVELS]

    # --- fixed-threshold meshes + frames ---
    import imageio.v2 as imageio
    from matplotlib.colors import hsv_to_rgb
    from quantumlab.visualization.volume_3d import extract_isosurface, IsosurfaceRenderer

    def phase_colours(psi_a, verts):
        from scipy.ndimage import map_coordinates
        idx = np.stack([(verts[:, 0] - grid.x[0]) / grid.dx,
                        (verts[:, 1] - grid.y[0]) / grid.dy,
                        (verts[:, 2] - grid.z[0]) / grid.dz])
        re = map_coordinates(psi_a.real, idx, order=1, mode="nearest")
        im = map_coordinates(psi_a.imag, idx, order=1, mode="nearest")
        hue = (np.arctan2(im, re) / (2 * np.pi)) % 1.0
        return hsv_to_rgb(np.stack([hue, np.ones_like(hue), np.ones_like(hue)], axis=1))

    def write_ply(path, verts, faces, rgb):
        rgb8 = np.clip(np.round(rgb * 255), 0, 255).astype(int)
        L = ["ply", "format ascii 1.0", f"element vertex {len(verts)}",
             "property float x", "property float y", "property float z",
             "property uchar red", "property uchar green", "property uchar blue",
             f"element face {len(faces)}", "property list uchar int vertex_indices", "end_header"]
        for v, c in zip(verts, rgb8):
            L.append(f"{v[0]:.6f} {v[1]:.6f} {v[2]:.6f} {c[0]} {c[1]} {c[2]}")
        for f in faces:
            L.append(f"3 {int(f[0])} {int(f[1])} {int(f[2])}")
        path.write_text("\n".join(L) + "\n", encoding="utf-8")

    case = OUT / "A_vortex_line"
    case.mkdir(parents=True, exist_ok=True)
    for f in sorted(case.glob("vortex_line_rho_*")):
        f.unlink()

    renderer = IsosurfaceRenderer(grid, levels=GLOBAL_LEVELS)
    pngs = []
    for k in sorted(snapshots):
        psi_k = snapshots[k]
        rho = np.abs(psi_k) ** 2
        for frac, lev in zip(GLOBAL_LEVELS, levels):
            iso = extract_isosurface(rho, lev, grid)
            if iso is None:
                continue
            verts, faces, _ = iso
            write_ply(case / f"vortex_line_global_{str(frac).replace('.','p')}_k{k:03d}.ply",
                      verts, faces, phase_colours(psi_k, verts))
        p = case / f"vortex_line_frame_{k:03d}.png"
        renderer.save(psi_k, p, t=k, title=f"vortex line, global thresholds, step {k}", dpi=110)
        pngs.append(p)
    gif = case / "vortex_line_evolution.gif"
    if gif.exists():
        gif.unlink()
    imageio.mimsave(gif, [imageio.imread(p) for p in pngs],
                    duration=int(GIF_DURATION_S * 1000), loop=0)
    renderer.close()

    # --- diagnostics ---
    frames = []
    for k in sorted(snapshots):
        d = analyse(snapshots[k], grid)
        d["step"] = k
        frames.append(d)

    out = {
        "case": "A_vortex_line", "grid_N": N, "box": BOX, "dt": DT, "steps": STEPS,
        "hbar": HBAR, "m": MASS, "charge_imposed": 1,
        "thresholds": {"mode": "GLOBAL_FIXED", "fractions_of_global_max": list(GLOBAL_LEVELS),
                       "global_max_density": global_max,
                       "absolute_levels": [round(l, 9) for l in levels]},
        "gif": {"path": str(gif), "frame_duration_s": GIF_DURATION_S,
                "frames": len(pngs)},
        "frames": frames,
        "core_axis_density": {
            "axis_x_index": N // 2,
            "axis_y_index": N // 2,
            "min_density_on_axis": round(core_axis, 9),
            "min_density_on_axis_point": core_axis_pt,
        },
    }
    p = IDX / "quantum_vortex_diagnostics.json"
    p.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")

    print(f"global max density = {global_max:.9f}")
    print(f"thresholds (global fixed) = {[round(l,9) for l in levels]}")
    for f in frames:
        print(f"\nstep {f['step']:3d}: rho_min={f['density_min']:.3e} at {f['density_min_point']}")
        for l in f["loops"]:
            print(f"    r={l['radius_grid_units']:.4f}  winding={l['winding_number']:+.4f}  "
                  f"circ={l['circulation_hbar_over_m']:+.5f}  /h/m={l['ratio_to_h_over_m']:+.4f}")
    print("\nwritten:", p)


if __name__ == "__main__":
    main()
