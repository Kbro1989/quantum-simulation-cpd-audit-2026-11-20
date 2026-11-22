#!/usr/bin/env python3
"""Re-run the consumer-inventory probes + write evidence to the audit dir.

Reproduces the [probe] measurements in cpd_consumer_inventory.md loss points
L1-L7 (reported by the subagent 2026-11-20), so the audit directory owns its
own probe evidence rather than the subagent's terminal transcript.

Run from the audit dir root: python probe_E_consumer_correctness.py
"""
import sys
import numpy as np

REPO = r"C:\Users\krist\Desktop\quantum-simulation-main\quantum-simulation-main"
AUD  = r"C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20"
sys.path.insert(0, REPO)

from quantumlab.core.grid import Grid1D, Grid2D, Grid3D
from quantumlab.core.wavefunction import WaveFunction1D, WaveFunction2D, WaveFunction3D
from quantumlab.core.absorbing_boundary import AbsorbingBoundaryLayer
from quantumlab.observables.expectation import (position_expectation, momentum_expectation,
                                                potential_energy_expectation, kinetic_energy_expectation,
                                                total_energy_expectation)
from quantumlab.observables.current import vortex_positions
from quantumlab.potentials.traps import HarmonicTrap
from quantumlab.solvers.split_operator import SplitOperatorSolver
from quantumlab.solvers.backends import get_backend
from quantumlab.visualization.animation import WavePacketAnimator
from quantumlab.potentials.time_dependent import DipoleDrive

OUT = open(f"{AUD}\\evidence\\probe_E_consumer_correctness.txt", "w", encoding="utf-8")
def log(*a):
    line = " ".join(str(x) for x in a)
    print(line)
    OUT.write(line + "\n")

def section(t):
    print(f"\n=== {t} ==="); OUT.write(f"\n=== {t} ===\n")

# ---- L1: runner energy log uses hbar=1,m=1 defaults while solver was built with cfg hbar/m
section("L1 hbar/m defaults in runner energy log")
g = Grid1D(128, -4, 4)
x = g.x
psi = WaveFunction1D(g, np.exp(-0.5*((x+1.5)/0.9)**2))
pot = HarmonicTrap(1.0, m=1.0)
hbar, m = 2.0, 3.0
true_energy = total_energy_expectation(psi, pot, hbar=hbar, m=m)
runner_style = total_energy_expectation(psi, pot)
log(f"E(hbar={hbar},m={m})  [explicit]        = {true_energy:.6f}")
log(f"E(hbar=1,m=1 defaults) [runner-style] = {runner_style:.6f}")

# ---- L2: norm division after absorbing boundary
section("L2 norm loss after absorbing boundary, energy not divided by norm")
g = Grid1D(128, -4, 4)
psi2 = WaveFunction1D(g, np.exp(-0.5*((x)/0.9)**2))
psi2.norm()
abl = AbsorbingBoundaryLayer(g, 4.0, order=4)
before = psi2.norm()
abl.apply(psi2)
after = psi2.norm()
log(f"norm before={before:.6f} after={after:.6f}")
log(f"E_after (no norm division)   = {total_energy_expectation(psi2, pot):.6f}")
log(f"E_after / norm_after         = {total_energy_expectation(psi2, pot)/after:.6f}")

# ---- L3 / L4: vortex grid-alignment and min_density threshold
section("L3/L4 vortex grid-alignment and min_density")
g2 = Grid2D(128, -2, 2, 128, -2, 2)
X, Y = g2.X, g2.Y
psi_v = WaveFunction2D(g2, np.exp(-0.5*((X**2 + Y**2)/0.4**2)) * (X + 1j*Y))
for md in (0.0, 0.2):
    pos, q = vortex_positions(psi_v, min_density=md)
    log(f"vortex_positions(min_density={md}) -> {len(pos)} vortex(es) pos={list(pos) if len(pos) else []} charges={list(q) if len(q) else []}")

# ---- L5: gpu flag silently ignored by split-operator runner
section("L5 gpu flag ignored for split_operator backend")
g3 = Grid3D(16, -2, 2, 16, -2, 2, 16, -2, 2)
pot3 = HarmonicTrap(g3)
sol = SplitOperatorSolver(g3, pot3, hbar=1.0, m=1.0, gpu=True, backend="numpy")
log(f"SplitOperatorSolver(grid,g,potential,hbar=1,m=1,gpu=True,backend='numpy').backend.name = {sol.backend.name}")

# ---- L6: animation 3D TypeError
section("L6 WavePacketAnimator 3-D")
wf3 = WaveFunction3D(g3, np.exp(-0.5*(X**2 + Y**2 + g3.X[:,:,0]**2)/0.4**2))
try:
    an = WavePacketAnimator(wf3)
    log("WavePacketAnimator(g3 gaussian)  -> no error (2-D capable)")
except Exception as exc:
    log(f"WavePacketAnimator(g3 gaussian) -> {type(exc).__name__}: {exc}")

# ---- L7: potential_energy_expectation evaluates V at t=0
section("L7 potential_energy_expectation evaluates potential at t=0")
grid = Grid1D(128, -4, 4)
Vd = DipoleDrive(V_base=0.5, F0=1.0, omega=1.0, phase=0.0, r_axis=0)
V_at_0 = Vd(grid)
V_at_t = Vd.evaluate_at(grid, 0.25)
log(f"DipoleDrive.evaluate(grid) = V(t=0) = {V_at_0:.6f}")
log(f"evaluate_at(grid, 0.25)    = V(t=0.25) = {V_at_t:.6f}  diff = {V_at_0 - V_at_t:.6f}")

OUT.close()
log("\n=== END probe_E_consumer_correctness ===")
print(f"\n[done] wrote {AUD}\\evidence\\probe_E_consumer_correctness.txt")
