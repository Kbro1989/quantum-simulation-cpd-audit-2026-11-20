#!/usr/bin/env python3
"""
cpd_quantum_3d_assets.py

Produce real 3D mesh assets from the quantum-simulation physics, using the
repository's own isosurface extractor (quantumlab/visualization/volume_3d.py,
marching cubes) and its production SplitOperatorSolver.

Subject: a charged vortex line (m=+1) in a 3D harmonic trap -- the building
block of the rotated-BEC vortex lattice added upstream in f8f1653, and the
exact topology targeted by defects CPD-V1 / CPD-V2.

Outputs (per isosurface level):
  <name>.ply   vertex-coloured mesh (colour = local quantum phase arg psi)
  <name>.obj   Wavefront OBJ for Godot / Blender / USD import
  manifest.json  SHA-256 of every artifact + generation parameters

Reads the repository read-only; writes only inside the audit workspace.
"""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
from matplotlib.colors import hsv_to_rgb

REPO = Path(r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main")
AUD = Path(r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20")
OUT = AUD / "quantum_3d_assets"
sys.path.insert(0, str(REPO))

from quantumlab.core.grid import Grid3D
from quantumlab.core.wavefunction import WaveFunction3D
from quantumlab.potentials.traps import HarmonicTrap
from quantumlab.solvers.split_operator import SplitOperatorSolver
from quantumlab.visualization.volume_3d import extract_isosurface

# ---- case parameters (recorded verbatim in the manifest) --------------------
N = 48
BOX = (-6.0, 6.0)
DT = 0.005
STEPS = 40
HBAR = 1.0
MASS = 1.0
TRAP_OMEGA = 1.0
VORTEX_CHARGE = 1
SIGMA = 1.0
LEVELS = (0.50, 0.15, 0.03)   # fractions of max|psi|^2


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def vortex_line_state(grid: Grid3D, sigma: float, charge: int) -> WaveFunction3D:
    """psi = N exp(-r^2 / 4 sigma^2) exp(i m theta), theta = atan2(y, x)."""
    X, Y, Z = grid.X, grid.Y, grid.Z
    theta = np.arctan2(Y, X)
    psi = np.exp(-(X ** 2 + Y ** 2 + Z ** 2) / (4.0 * sigma ** 2)) * np.exp(1j * charge * theta)
    wf = WaveFunction3D(grid, psi.astype(complex))
    wf.normalize()
    return wf


def phase_colours(psi: np.ndarray, verts: np.ndarray, grid: Grid3D) -> np.ndarray:
    """HSV colour from local arg(psi), trilinearly sampled (same method as volume_3d)."""
    from scipy.ndimage import map_coordinates
    idx = np.stack([(verts[:, 0] - grid.x[0]) / grid.dx,
                    (verts[:, 1] - grid.y[0]) / grid.dy,
                    (verts[:, 2] - grid.z[0]) / grid.dz])
    re = map_coordinates(psi.real, idx, order=1, mode="nearest")
    im = map_coordinates(psi.imag, idx, order=1, mode="nearest")
    hue = (np.arctan2(im, re) / (2.0 * np.pi)) % 1.0
    sat = np.ones_like(hue)
    val = np.ones_like(hue)
    return hsv_to_rgb(np.stack([hue, sat, val], axis=1))


def write_ply(path: Path, verts: np.ndarray, faces: np.ndarray, rgb: np.ndarray) -> None:
    """Binary-independent ASCII PLY with vertex colours (v x y z r g b / f i j k)."""
    lines = ["ply", "format ascii 1.0",
             f"element vertex {len(verts)}",
             "property float x", "property float y", "property float z",
             "property uchar red", "property uchar green", "property uchar blue",
             f"element face {len(faces)}",
             "property list uchar int vertex_indices",
             "end_header"]
    rgb8 = np.clip(np.round(rgb * 255.0), 0, 255).astype(int)
    for v, c in zip(verts, rgb8):
        lines.append(f"{v[0]:.6f} {v[1]:.6f} {v[2]:.6f} {c[0]} {c[1]} {c[2]}")
    for f in faces:
        lines.append(f"3 {int(f[0])} {int(f[1])} {int(f[2])}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_obj(path: Path, verts: np.ndarray, faces: np.ndarray, rgb: np.ndarray) -> None:
    """Wavefront OBJ: v x y z r g b / f i j k (1-based)."""
    rgb6 = np.clip(rgb, 0.0, 1.0)
    lines = ["# quantum-simulation isosurface — colour = local arg(psi)"]
    for v, c in zip(verts, rgb6):
        lines.append(f"v {v[0]:.6f} {v[1]:.6f} {v[2]:.6f} {c[0]:.4f} {c[1]:.4f} {c[2]:.4f}")
    for f in faces:
        lines.append(f"f {int(f[0])+1} {int(f[1])+1} {int(f[2])+1}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)

    grid = Grid3D(N, BOX[0], BOX[1], N, BOX[0], BOX[1], N, BOX[0], BOX[1])
    trap = HarmonicTrap(omegas=TRAP_OMEGA, m=MASS)
    psi0 = vortex_line_state(grid, SIGMA, VORTEX_CHARGE)

    solver = SplitOperatorSolver(grid, trap, DT, HBAR, MASS, order=2, backend="numpy")
    psi = psi0
    for _ in range(STEPS):
        psi = solver.step(psi)

    rho = np.abs(psi.psi) ** 2
    rho_max = float(rho.max())
    t_final = STEPS * DT

    manifest = {
        "generator": "cpd_quantum_3d_assets.py",
        "repository": str(REPO),
        "repository_head": "44f30e30654c064b75f760833741ab55b392ff20",
        "case": {
            "grid_N": N, "box": BOX, "dt": DT, "steps": STEPS, "t_final": t_final,
            "hbar": HBAR, "m": MASS, "trap_omega": TRAP_OMEGA,
            "vortex_charge": VORTEX_CHARGE, "sigma": SIGMA,
            "solver": "SplitOperatorSolver(order=2, backend=numpy)",
            "isosurface_levels_fraction_of_rho_max": list(LEVELS),
        },
        "measured": {
            "rho_max": rho_max,
            "norm": float(psi.norm()),
            "vortex_charge_measured": None,
        },
        "artifacts": [],
    }

    from quantumlab.observables.current import vortex_positions
    try:
        vpos = vortex_positions(rho, grid, min_density=0.0)
        manifest["measured"]["vortex_positions_min_density_0"] = [
            [float(a), float(b)] for a, b in np.atleast_2d(vpos)
        ]
        manifest["measured"]["vortex_count"] = int(np.atleast_2d(vpos).shape[0])
    except Exception as exc:
        manifest["measured"]["vortex_positions_error"] = f"{type(exc).__name__}: {exc}"

    for frac in LEVELS:
        level = frac * rho_max
        iso = extract_isosurface(rho, level, grid)
        if iso is None:
            print(f"level {frac:.2f} (rho={level:.3e}): outside field range, skipped")
            continue
        verts, faces, _normals = iso
        rgb = phase_colours(psi.psi, verts, grid)
        tag = f"rho_{frac:.2f}".replace(".", "p")
        ply = OUT / f"vortex_line_{tag}.ply"
        obj = OUT / f"vortex_line_{tag}.obj"
        write_ply(ply, verts, faces, rgb)
        write_obj(obj, verts, faces, rgb)

        # read-back verification: re-parse what was written
        ply_txt = ply.read_text(encoding="utf-8").splitlines()
        hdr_end = ply_txt.index("end_header")
        n_v = int([l for l in ply_txt[:hdr_end] if l.startswith("element vertex")][0].split()[-1])
        n_f = int([l for l in ply_txt[:hdr_end] if l.startswith("element face")][0].split()[-1])
        ok = (n_v == len(verts)) and (n_f == len(faces))

        rec = {
            "level_fraction": frac, "level_value": float(level),
            "vertices": int(len(verts)), "faces": int(len(faces)),
            "ply": {"path": str(ply), "bytes": ply.stat().st_size, "sha256": sha256(ply),
                    "readback_vertices": n_v, "readback_faces": n_f, "readback_matches": bool(ok)},
            "obj": {"path": str(obj), "bytes": obj.stat().st_size, "sha256": sha256(obj)},
        }
        manifest["artifacts"].append(rec)
        print(f"level {frac:.2f}: {len(verts)} verts, {len(faces)} faces -> {ply.name} "
              f"({ply.stat().st_size} B) readback_ok={ok}")

    mpath = OUT / "manifest.json"
    mpath.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print("norm:", manifest["measured"]["norm"], "rho_max:", rho_max)
    print("vortices:", manifest["measured"].get("vortex_count"),
          manifest["measured"].get("vortex_positions_min_density_0"))
    print("manifest:", mpath)


if __name__ == "__main__":
    main()
