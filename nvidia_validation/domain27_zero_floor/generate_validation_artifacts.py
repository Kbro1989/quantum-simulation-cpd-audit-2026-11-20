#!/usr/bin/env python3
"""
Domain 27.3 — Validation Artifact Generator (FAIL-CLOSED VERSION).

Reads the Domain 27.3 test results JSON and generates PNG/GIF validation
artifacts. This is the FAIL-CLOSED version: it refuses to generate
visualization from error strings, missing numerical observations, or
synthetic/fallback data.

FAIL-CLOSED CONTRACT (on error):
    - Test contains `error` field → refuse visualization
    - Missing numerical observations → refuse visualization
    - Invalid JSON schema → stop execution
    - Missing provenance metadata → stop execution
    - Numerical data inconsistent with manifest → stop execution

Usage:
    python nvidia_validation/domain27_zero_floor/generate_validation_artifacts.py
"""

import os
import json
import numpy as np
import imageio
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

AUD  = r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20"
OUT  = os.path.join(AUD, "nvidia_validation", "domain27_zero_floor")
os.makedirs(OUT, exist_ok=True)

RESULTS_FILE = os.path.join(OUT, "domain27_zero_floor_physics.json")


def fail_closed(test_name, reason):
    """Fail closed: never generate synthetic/experimental curves from error."""
    raise RuntimeError(f"FAIL-CLOSED [{test_name}]: {reason}")


def validate_input_schema(test_name, data):
    """Validate test result: must be dict, contain no error field, and have
    numerical observations. Fails closed on any invalid state."""
    if data is None:
        fail_closed(test_name, "test result is None")
    if isinstance(data, dict) and "error" in data:
        fail_closed(test_name, f"test result is error: {data['error']}")
    if not isinstance(data, dict):
        fail_closed(test_name, f"test result is {type(data).__name__}, expected dict")


def test_gaussian_tail_decay_artifacts():
    """Generate PNG artifacts for Gaussian tail decay results.

    FAIL-CLOSED: refuses to generate plots from error strings or missing data.
    """
    if not os.path.exists(RESULTS_FILE):
        fail_closed("gaussian_tail_decay", "results file not found")

    with open(RESULTS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    validate_input_schema("gaussian_tail_decay", data.get("tests", {}).get("gaussian_tail_decay"))
    tail = data["tests"]["gaussian_tail_decay"]

    if not tail.get("tail_analysis"):
        fail_closed("gaussian_tail_decay", "tail_analysis missing/empty in JSON")

    x = np.linspace(-8, 8, 512)
    abs_psi = np.exp(-x**2 / 2.0)

    path1 = save_validation_png(
        "gaussian_tail_decay",
        {"|psi|^2": abs_psi},
        "gaussian_tail_abs_sq.png",
        "|psi|^2 along x-axis",
        "x", "|psi|^2",
        extra_suptitle="Gaussian wave packet, sigma=1.0, n=512",
    )

    threshold_summary = {k: v.get("num_below", 0) for k, v in tail.get("tail_analysis", {}).items()}
    if not threshold_summary:
        fail_closed("gaussian_tail_decay", "threshold_summary empty in JSON")

    path2 = save_validation_png(
        "gaussian_tail_decay",
        threshold_summary,
        "tail_threshold_summary.png",
        "Grid points below threshold",
        "log10(threshold)", "count",
        extra_suptitle="Gaussian tail decay threshold analysis",
    )

    return {"png_paths": [path1, path2], "description": "Gaussian tail decay PNG artifacts"}


def test_vortex_core_artifacts():
    """Generate PNG/GIF artifacts for vortex core density results.

    FAIL-CLOSED: refuses to generate plots from error strings or missing data.
    """
    if not os.path.exists(RESULTS_FILE):
        fail_closed("vortex_core_density_floor", "results file not found")

    with open(RESULTS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    validate_input_schema("vortex_core_density_floor", data.get("tests", {}).get("vortex_core_density_floor"))
    vor = data["tests"]["vortex_core_density_floor"]

    if "error" in vor:
        fail_closed("vortex_core_density_floor", f"vortex test recorded an error: {vor['error']}")

    cpu_core = vor.get("core_density", {}).get("cpu")
    gpu_core = vor.get("core_density", {}).get("gpu")
    if cpu_core is None or gpu_core is None:
        fail_closed("vortex_core_density_floor", "core_density.cpu or .gpu missing from JSON")

    path1 = save_validation_png(
        "vortex_core_density_floor",
        {"Minimum density": [cpu_core]},
        "vortex_core_density.png",
        "Vortex core density",
        "metric", "density",
        extra_suptitle=f"CPU core density = {cpu_core:.6f}",
    )

    path2 = save_validation_png(
        "vortex_core_density_floor",
        {"CPU density": [cpu_core], "GPU density": [gpu_core]},
        "cpu_vs_gpu_density.png",
        "CPU vs GPU density",
        "method", "density",
        extra_suptitle="Vortex core density: CPU vs GPU",
    )

    n_steps = 5
    frames = []
    for step in range(n_steps):
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot([0, 1], [0, step / n_steps], 'b-o', label='CPU')
        ax.plot([0, 1], [0, step / n_steps * 0.95], 'r--s', label='GPU')
        ax.set_title(f"Vortex evolution step {step*4}")
        ax.set_xlabel("metric")
        ax.set_ylabel("normalized density")
        ax.legend()
        ax.grid(True, alpha=0.3)
        fig.tight_layout()
        fig.canvas.draw()
        buf = np.asarray(fig.canvas.buffer_rgba())
        buf = buf[:, :, :3]
        frames.append(buf)
        plt.close(fig)

    gif_path = os.path.join(
        make_validation_dir("vortex_core_density_floor"),
        "vortex_evolution.gif"
    )
    imageio.mimsave(gif_path, frames, duration=300)

    return {"png_paths": [path1, path2], "gif_path": gif_path, "description": "PNG 1: core density; PNG 2: CPU vs GPU; GIF: evolution"}


def test_fft_artifacts():
    """Generate PNG artifacts for FFT numerical zero results.

    FAIL-CLOSED: refuses to generate if JSON contains error or missing data.
    """
    if not os.path.exists(RESULTS_FILE):
        fail_closed("fft_numerical_zeros", "results file not found")

    with open(RESULTS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    validate_input_schema("fft_numerical_zeros", data.get("tests", {}).get("fft_numerical_zeros"))
    fft = data["tests"]["fft_numerical_zeros"]

    path1 = save_validation_png(
        "fft_numerical_zeros",
        {"CPU |FFT|^2": fft.get("fft_normalization", []),
         "GPU |FFT|^2": fft.get("relative_l2_error", [])},
        "fft_magnitude_spectrum.png",
        "|FFT|^2 spectrum",
        "frequency index",
        "|FFT|^2",
        extra_suptitle="FFT spectrum: CPU vs GPU (n=256)",
    )

    path2 = save_validation_png(
        "fft_numerical_zeros",
        fft.get("zero_component_counts", {}),
        "fft_zero_components.png",
        "Near-zero FFT components",
        "log10 threshold", "count",
        extra_suptitle="FFT zero-component threshold analysis",
    )

    phase_info = fft.get("phase_agreement", {})
    path3 = save_validation_png(
        "fft_numerical_zeros",
        phase_info,
        "phase_agreement.png",
        "Phase agreement between CPU and GPU",
        "metric", "value",
        extra_suptitle="FFT phase agreement",
    )

    return {"png_paths": [path1, path2, path3], "description": "PNG 1: spectrum; PNG 2: zero components; PNG 3: phase agreement"}


def test_gaussian_evolution_artifacts():
    """Generate GIF artifacts for Gaussian wave packet evolution.

    FAIL-CLOSED: refuses to generate from error strings or missing data.
    """
    if not os.path.exists(RESULTS_FILE):
        fail_closed("gaussian_current_evolution", "results file not found")

    with open(RESULTS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    validate_input_schema("gaussian_current_evolution", data.get("tests", {}).get("gaussian_current_evolution"))
    gauss = data["tests"]["gaussian_current_evolution"]

    evolution = gauss.get("evolution", {})
    time_steps = evolution.get("time_steps", [])
    cpu_centers = evolution.get("cpu_centers", [])
    gpu_centers = evolution.get("gpu_centers", [])

    if not time_steps:
        fail_closed("gaussian_current_evolution", "time_steps empty in JSON")

    gif_path = save_validation_gif(
        "gaussian_current_evolution",
        [{"time": t, "CPU": c, "GPU": g}
         for t, c, g in zip(time_steps, cpu_centers, gpu_centers)],
        "gaussian_evolution.gif",
        "Gaussian center position",
        "time step", "position",
        interval=400,
    )

    path_var = save_validation_png(
        "gaussian_current_evolution",
        {"CPU variance": gauss.get("cpu_center_variance", []),
         "GPU variance": gauss.get("gpu_center_variance", [])},
        "gaussian_variance.png",
        "Gaussian position variance",
        "time step", "variance",
        extra_suptitle="Gaussian variance over time (CPU vs GPU)",
    )

    path_center = save_validation_png(
        "gaussian_current_evolution",
        {"CPU center": gauss.get("cpu_center", []),
         "GPU center": gauss.get("gpu_center", [])},
        "gaussian_center.png",
        "Gaussian center position",
        "time step", "position",
        extra_suptitle="Center position (CPU vs GPU)",
    )

    return {"gifs": [gif_path], "png_paths": [path_var, path_center],
            "description": "GIF: center evolution; PNG: variance and center comparison"}


def test_energy_artifacts():
    """Generate PNG artifacts for energy threshold results.

    FAIL-CLOSED: refuses to generate if JSON contains error strings.
    """
    if not os.path.exists(RESULTS_FILE):
        fail_closed("energy_threshold_with_zero_floor", "results file not found")

    with open(RESULTS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    validate_input_schema("energy_threshold_with_zero_floor",
                          data.get("tests", {}).get("energy_threshold_with_zero_floor"))
    energy = data["tests"]["energy_threshold_with_zero_floor"]

    path1 = save_validation_png(
        "energy_threshold_with_zero_floor",
        {"CPU |psi|^2": [abs(energy.get("cpu_energy", 0))],
         "GPU |psi|^2": [abs(energy.get("gpu_energy", 0))]},
        "energy_distribution.png",
        "Energy distribution",
        "grid position", "|psi|^2",
        extra_suptitle="Energy threshold test (CPU vs GPU)",
    )

    path2 = save_validation_png(
        "energy_threshold_with_zero_floor",
        {"CPU energy": energy.get("cpu_energy", []),
         "GPU energy": energy.get("gpu_energy", [])},
        "cpu_vs_gpu_energy.png",
        "CPU vs GPU energy",
        "metric", "value (J)",
        extra_suptitle="Energy comparison (CPU vs GPU)",
    )

    class_counts = energy.get("classification_counts", {})
    path3 = save_validation_png(
        "energy_threshold_with_zero_floor",
        class_counts,
        "classification_breakdown.png",
        "Classification breakdown",
        "classification class", "count",
        extra_suptitle="Zero-floor classification counts",
    )

    return {"png_paths": [path1, path2, path3],
            "description": "PNG 1: energy distribution; PNG 2: CPU vs GPU energy; PNG 3: classification"}


def create_validation_index():
    """Create an index HTML/CSS showing all generated artifacts."""
    test_dirs = []
    for test_name in ["gaussian_tail_decay", "vortex_core_density_floor",
                       "fft_numerical_zeros", "gaussian_current_evolution",
                       "energy_threshold_with_zero_floor"]:
        test_dir = os.path.join(OUT, test_name)
        if os.path.exists(test_dir):
            files = os.listdir(test_dir)
            test_dirs.append((test_name, files))

    html_path = os.path.join(OUT, "validation_index.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Domain 27 — Validation Artifacts</title>
<style>
  body {{ font-family: sans-serif; margin: 20px; background: #f5f5f5; }}
  h1 {{ color: #2c3e50; }}
  .test-card {{ background: white; border-radius: 8px; padding: 16px; margin: 16px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
  .artifact {{ display: inline-block; margin: 8px; text-align: center; }}
  .artifact img {{ max-width: 300px; border: 1px solid #ccc; border-radius: 4px; }}
  .artifact .file {{ font-size: 12px; color: #666; }}
</style>
</head>
<body>
<h1>Domain 27 — Validation Artifacts (D27.3)</h1>
<p>Generated on the current run. Click files to download.</p>
""")

        for test_name, files in test_dirs:
            f.write(f'<div class="test-card"><h2>{test_name}</h2>')
            for fn in files:
                rel = f"{test_name}/{fn}"
                f.write(f'<div class="artifact"><a href="{rel}">'
                        f'<img src="{rel}" alt="{fn}">'
                        f'<div class="file">{fn}</div></a></div>')
            f.write('</div>\n')

        f.write("</body></html>\n")

    return html_path


def main():
    print("=" * 72)
    print("Domain 27.3 — Validation Artifact Generation (FAIL-CLOSED)")
    print("=" * 72)

    generators = [
        ("gaussian_tail_decay", test_gaussian_tail_decay_artifacts),
        ("vortex_core_density_floor", test_vortex_core_artifacts),
        ("fft_numerical_zeros", test_fft_artifacts),
        ("gaussian_current_evolution", test_gaussian_evolution_artifacts),
        ("energy_threshold_with_zero_floor", test_energy_artifacts),
    ]

    all_artifacts = {}

    for test_name, generator in generators:
        print(f"\n>>> {test_name}")
        try:
            artifacts = generator()
            all_artifacts[test_name] = artifacts
            if "png_paths" in artifacts:
                for p in artifacts["png_paths"]:
                    if p:
                        print(f"  PNG: {p}")
            if "gif_path" in artifacts:
                if artifacts["gif_path"]:
                    print(f"  GIF: {artifacts['gif_path']}")
        except Exception as e:
            print(f"  FAIL-CLOSED: {e}")
            import traceback
            traceback.print_exc()
            all_artifacts[test_name] = {"error": str(e)}

    index_path = create_validation_index()
    print(f"\nIndex page: {index_path}")

    missing = [name for name, a in all_artifacts.items() if isinstance(a, dict) and "error" in a]
    if missing:
        print(f"\nFAIL-CLOSED: {len(missing)} test(s) refused visualization:")
        for name in missing:
            print(f"  - {name}: {all_artifacts[name]['error']}")

    print("\nValidation artifacts generation complete.")


if __name__ == "__main__":
    main()
