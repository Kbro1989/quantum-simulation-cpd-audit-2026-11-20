#!/usr/bin/env python3
"""
cpd_quantum_3d_asset_suite.py

Real, reusable 3D assets derived from the quantum-simulation physics, plus the
PNG/GIF evidence for every tested output.

Why this exists: the repository's 3D claim is a PNG-over-time rendering path
(matplotlib isosurfaces written frame by frame).  That is a picture of a 3D
object, not a 3D asset.  This suite emits actual geometry (PLY + OBJ) that a
3D tool can import, alongside the frame evidence, and records GPU/CPU parity
so "the GPU ran" is measured rather than asserted.

Cases
  A  vortex_line        m=+1 vortex line in a 3D harmonic trap (evolving)
  B  bec_ground_state   Gross-Pitaevskii condensate, imaginary-time relaxation
  C  gpu_parity         case A evolved on numpy and on cupy; parity measured

Writes only inside the audit workspace.  Reads the repository read-only.
"""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np
from matplotlib.colors import hsv_to_rgb

REPO = Path(r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main")
AUD = Path(r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20")
OUT = AUD / "quantum_3d_asset_suite"
sys.path.insert(0, str(REPO))

from quantumlab.core.grid import Grid3D
from quantumlab.core.wavefunction import WaveFunction3D
from quantumlab.potentials.traps import HarmonicTrap
from quantumlab.solvers.split_operator import SplitOperatorSolver
from quantumlab.visualization.volume_3d import extract_isosurface, IsosurfaceRenderer

LEVELS = (0.50, 0.15, 0.03)
FRAMES = (0, 10, 20, 30, 40)      # step indices rendered to PNG/GIF


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def vortex_line_state(grid: Grid3D, sigma: float = 1.0, charge: int = 1) -> WaveFunction3D:
    X, Y, Z = grid.X, grid.Y, grid.Z
    theta = np.arctan2(Y, X)
    psi = np.exp(-(X ** 2 + Y ** 2 + Z ** 2) / (4.0 * sigma ** 2)) * np.exp(1j * charge * theta)
    wf = WaveFunction3D(grid, psi.astype(complex))
    wf.normalize()
    return wf


def phase_colours(psi: np.ndarray, verts: np.ndarray, grid: Grid3D) -> np.ndarray:
    from scipy.ndimage import map_coordinates
    idx = np.stack([(verts[:, 0] - grid.x[0]) / grid.dx,
                    (verts[:, 1] - grid.y[0]) / grid.dy,
                    (verts[:, 2] - grid.z[0]) / grid.dz])
    re = map_coordinates(psi.real, idx, order=1, mode="nearest")
    im = map_coordinates(psi.imag, idx, order=1, mode="nearest")
    hue = (np.arctan2(im, re) / (2.0 * np.pi)) % 1.0
    return hsv_to_rgb(np.stack([hue, np.ones_like(hue), np.ones_like(hue)], axis=1))


def write_ply(path: Path, verts, faces, rgb) -> None:
    rgb8 = np.clip(np.round(rgb * 255.0), 0, 255).astype(int)
    L = ["ply", "format ascii 1.0", f"element vertex {len(verts)}",
         "property float x", "property float y", "property float z",
         "property uchar red", "property uchar green", "property uchar blue",
         f"element face {len(faces)}", "property list uchar int vertex_indices", "end_header"]
    for v, c in zip(verts, rgb8):
        L.append(f"{v[0]:.6f} {v[1]:.6f} {v[2]:.6f} {c[0]} {c[1]} {c[2]}")
    for f in faces:
        L.append(f"3 {int(f[0])} {int(f[1])} {int(f[2])}")
    path.write_text("\n".join(L) + "\n", encoding="utf-8")


def write_obj(path: Path, verts, faces, rgb) -> None:
    L = ["# quantum-simulation isosurface -- colour = local arg(psi)"]
    for v, c in zip(verts, np.clip(rgb, 0, 1)):
        L.append(f"v {v[0]:.6f} {v[1]:.6f} {v[2]:.6f} {c[0]:.4f} {c[1]:.4f} {c[2]:.4f}")
    for f in faces:
        L.append(f"f {int(f[0])+1} {int(f[1])+1} {int(f[2])+1}")
    path.write_text("\n".join(L) + "\n", encoding="utf-8")


def emit_meshes(case_dir: Path, tag: str, psi: np.ndarray, grid: Grid3D) -> list:
    rho = np.abs(psi) ** 2
    rho_max = float(rho.max())
    out = []
    for frac in LEVELS:
        iso = extract_isosurface(rho, frac * rho_max, grid)
        if iso is None:
            continue
        verts, faces, _ = iso
        rgb = phase_colours(psi, verts, grid)
        ply = case_dir / f"{tag}_rho_{str(frac).replace('.', 'p')}.ply"
        obj = case_dir / f"{tag}_rho_{str(frac).replace('.', 'p')}.obj"
        write_ply(ply, verts, faces, rgb)
        write_obj(obj, verts, faces, rgb)
        txt = ply.read_text(encoding="utf-8").splitlines()
        he = txt.index("end_header")
        nv = int([l for l in txt[:he] if l.startswith("element vertex")][0].split()[-1])
        nf = int([l for l in txt[:he] if l.startswith("element face")][0].split()[-1])
        out.append({"level_fraction": frac, "level_value": float(frac * rho_max),
                    "vertices": int(len(verts)), "faces": int(len(faces)),
                    "ply": {"path": str(ply), "bytes": ply.stat().st_size, "sha256": sha256(ply),
                            "readback_ok": bool(nv == len(verts) and nf == len(faces))},
                    "obj": {"path": str(obj), "bytes": obj.stat().st_size, "sha256": sha256(obj)}})
    return out


def emit_frames(case_dir: Path, tag: str, frames: dict, grid: Grid3D) -> list:
    """frames: {step_index: psi}. Renders PNG per frame and one GIF over them."""
    import imageio.v2 as imageio
    renderer = IsosurfaceRenderer(grid, levels=LEVELS)
    pngs = []
    for k in sorted(frames):
        p = case_dir / f"{tag}_frame_{k:03d}.png"
        renderer.save(frames[k], p, t=k, title=f"{tag}  step {k}", dpi=110)
        pngs.append(p)
    gif = case_dir / f"{tag}_evolution.gif"
    imgs = [imageio.imread(p) for p in pngs]
    imageio.mimsave(gif, imgs, duration=0.5, loop=0)
    renderer.close()
    return {"pngs": [{"path": str(p), "bytes": p.stat().st_size, "sha256": sha256(p)} for p in pngs],
            "gif": {"path": str(gif), "bytes": gif.stat().st_size, "sha256": sha256(gif)},
            "png_count": len(pngs)}


def case_vortex_line(manifest: dict) -> None:
    case_dir = OUT / "A_vortex_line"
    case_dir.mkdir(parents=True, exist_ok=True)
    grid = Grid3D(48, -6, 6, 48, -6, 6, 48, -6, 6)
    trap = HarmonicTrap(omegas=1.0, m=1.0)
    psi = vortex_line_state(grid)
    solver = SplitOperatorSolver(grid, trap, 0.005, 1.0, 1.0, order=2, backend="numpy")
    frames = {0: psi.psi.copy()}
    for k in range(1, 41):
        psi = solver.step(psi)
        if k in FRAMES:
            frames[k] = psi.psi.copy()
    meshes = emit_meshes(case_dir, "vortex_line", psi.psi, grid)
    ev = emit_frames(case_dir, "vortex_line", frames, grid)
    manifest["cases"].append({
        "case": "A_vortex_line", "grid_N": 48, "box": [-6, 6], "dt": 0.005, "steps": 40,
        "trap": "HarmonicTrap(omegas=1.0, m=1.0)", "vortex_charge": 1,
        "final_norm": float(psi.norm()),
        "mesh_artifacts": meshes, "frame_evidence": ev,
    })
    print(f"A_vortex_line: {len(meshes)} meshes, {ev['png_count']} PNGs, norm={psi.norm():.12f}")


def case_bec_ground_state(manifest: dict) -> None:
    case_dir = OUT / "B_bec_ground_state"
    case_dir.mkdir(parents=True, exist_ok=True)
    grid = Grid3D(32, -6, 6, 32, -6, 6, 32, -6, 6)
    trap = HarmonicTrap(omegas=(0.7, 2.5, 2.5), m=1.0)
    psi0 = vortex_line_state(grid, sigma=1.5, charge=0)
    solver = SplitOperatorSolver(grid, trap, 0.005, 1.0, 1.0, order=2,
                                 nonlinearity=600.0, imaginary_time=True, backend="numpy")
    frames = {}
    psi = psi0
    for k in range(1, 301):
        psi = solver.step(psi)
        if k in (0, 100, 200, 300):
            frames[k] = psi.psi.copy()
    meshes = emit_meshes(case_dir, "bec_ground_state", psi.psi, grid)
    ev = emit_frames(case_dir, "bec_ground_state", frames, grid)
    manifest["cases"].append({
        "case": "B_bec_ground_state", "grid_N": 32, "box": [-6, 6], "dtau": 0.005, "steps": 300,
        "trap": "HarmonicTrap(omegas=(0.7,2.5,2.5))", "g": 600.0, "imaginary_time": True,
        "final_norm": float(psi.norm()),
        "mesh_artifacts": meshes, "frame_evidence": ev,
    })
    print(f"B_bec_ground_state: {len(meshes)} meshes, {ev['png_count']} PNGs, norm={psi.norm():.12f}")


def case_gpu_parity(manifest: dict) -> None:
    """Same state on numpy and cupy; assert the GPU actually executed."""
    case_dir = OUT / "C_gpu_parity"
    case_dir.mkdir(parents=True, exist_ok=True)
    grid = Grid3D(48, -6, 6, 48, -6, 6, 48, -6, 6)
    trap = HarmonicTrap(omegas=1.0, m=1.0)
    psi0 = vortex_line_state(grid)

    cpu = SplitOperatorSolver(grid, trap, 0.005, 1.0, 1.0, order=2, backend="numpy")
    cpu_backend = cpu.backend
    p_cpu = psi0.psi.copy()
    for _ in range(40):
        p_cpu = cpu.step(WaveFunction3D(grid, p_cpu)).psi

    rec = {"case": "C_gpu_parity", "grid_N": 48, "steps": 40,
           "cpu_backend": cpu_backend, "cpu_norm": float(np.linalg.norm(p_cpu))}

    try:
        import cupy  # noqa: F401
        gpu = SplitOperatorSolver(grid, trap, 0.005, 1.0, 1.0, order=2, backend="cupy")
        gpu_backend = gpu.backend
        p_gpu = psi0.psi.copy()
        for _ in range(40):
            p_gpu = gpu.step(WaveFunction3D(grid, p_gpu)).psi
        d = float(np.max(np.abs(p_gpu - p_cpu)))
        rec.update({"gpu_backend": gpu_backend, "gpu_norm": float(np.linalg.norm(p_gpu)),
                    "max_abs_diff": d, "parity_ok": bool(d < 1e-9)})
        meshes = emit_meshes(case_dir, "gpu_parity", p_gpu, grid)
        rec["mesh_artifacts"] = meshes
        print(f"C_gpu_parity: cpu={cpu_backend} gpu={gpu_backend} max|dpsi|={d:.3e} ok={d < 1e-9}")
    except Exception as exc:
        rec.update({"gpu_backend": None, "error": f"{type(exc).__name__}: {exc}"})
        print(f"C_gpu_parity: cpu={cpu_backend} GPU ERROR {rec['error']}")
    manifest["cases"].append(rec)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {
        "suite": "cpd_quantum_3d_asset_suite",
        "purpose": ("Real geometry (PLY/OBJ) from quantumlab physics, plus PNG/GIF "
                    "evidence per tested output, plus measured GPU/CPU parity. "
                    "Replaces the PNG-over-time-only 3D claim."),
        "repository": str(REPO),
        "repository_head": "44f30e30654c064b75f760833741ab55b392ff20",
        "isosurface_levels_fraction_of_rho_max": list(LEVELS),
        "cases": [],
    }
    case_vortex_line(manifest)
    case_bec_ground_state(manifest)
    case_gpu_parity(manifest)
    p = OUT / "manifest.json"
    p.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    n_mesh = sum(len(c.get("mesh_artifacts", [])) for c in manifest["cases"])
    n_png = sum(c.get("frame_evidence", {}).get("png_count", 0) for c in manifest["cases"])
    print(f"\ntotal: {len(manifest['cases'])} cases, {n_mesh} meshes, {n_png} PNGs")
    print("manifest:", p)


if __name__ == "__main__":
    main()
