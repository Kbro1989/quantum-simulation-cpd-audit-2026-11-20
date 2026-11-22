#!/usr/bin/env python3
"""Runtime probe L5: confirm the split_operator runner path silently drops gpu=True.

Builds a real 3-D config (solver: split_operator, gpu: true), runs the repo's
runner as a subprocess, and reports the backend label the log prints.
"""
import os
import subprocess
import sys

REPO = r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main"
AUD = r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20"
CFG = os.path.join(AUD, "evidence", "L5_config.yaml")
os.makedirs(os.path.dirname(CFG), exist_ok=True)
cfg = """output_dir: output/evidence_L5
simulations:
  s1:
    dimension: 3
    gpu: true
    solver: split_operator
    backend: numpy
    grid:
      N: 16
      L: 8.0
    wavefunction:
      x0: 0.0
      sigma: 1.0
      k0_x: 0.0
    potential:
      type: gaussian_3d_barrier
      params:
        V0: 2.0
        width: 1.0
        x0: 0.0
        y0: 0.0
        z0: 0.0
    dt: 0.005
    num_steps: 1
    snapshot_interval: 1
    log_interval: 1
"""
open(CFG, "w", encoding="utf-8").write(cfg)

launcher = os.path.join(AUD, "evidence", "_l5_launcher.py")
launcher_code = (
    "import sys\n"
    "sys.path.insert(0, " + repr(REPO) + ")\n"
    "import yaml, quantumlab.runner as rn\n"
    "rn.SimulationRunner(" + repr(CFG) + ").run()\n"
)
open(launcher, "w", encoding="utf-8").write(launcher_code)
r = subprocess.run([sys.executable, launcher], cwd=REPO,
                   capture_output=True, text=True,
                   env={**os.environ, "PYTHONPATH": REPO})
print("=== stdout ===")
print(r.stdout)
print("=== stderr ===")
print(r.stderr[-3000:] if r.stderr else "")
print("exit:", r.returncode)
