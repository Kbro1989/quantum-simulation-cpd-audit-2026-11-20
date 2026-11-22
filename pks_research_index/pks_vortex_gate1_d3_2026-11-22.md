# Gate 1 — D3 temporal and spatial convergence

**Date:** 2026-11-22
**Script:** `cpd_vortex_gate1_d3_convergence_2026-11-22.py`
**Measurements:** `pks_research_index/quantum_vortex_gate1_d3.json`

Separate validation gate from GPE stationarity. Acceptance condition: *localization
error remains bounded and converges under refinement over the declared interval.*

---

## 1. Method

Detector under test: **phase-winding centroid**.
Independent reference: **deepest central local density minimum** — a different
physical observable (density, no phase).

The first version of the reference used the **global** density minimum. That failed
exactly like the old corner detector: for a regularised vortex in a Gaussian envelope
the box-edge tail is lower than the core, so the reference jumped to `(−5, −5)` and
its windings read 0/−1. Corrected to a **local** minimum inside a declared region
r ≤ 3, with competing minima counted.

Swept: N ∈ {48, 64} × dt ∈ {0.005, 0.0025}, steps 0–200, frames every 20,
z ∈ {−2, 0, +2}, loop radii {2, 3, 4}.

## 2. Result — the reference does not move

| run | reference core (every frame, every slice) |
|---|---|
| N=48 dt=0.005 | (0.0000, 0.0000) |
| N=48 dt=0.0025 | (0.0000, 0.0000) |
| N=64 dt=0.005 | (0.0000, 0.0000) |
| N=64 dt=0.0025 | (0.0000, 0.0000) |

The vortex core stays on the axis for the whole 200 steps. That is physically
consistent: the harmonic trap is symmetric about the origin, so a centred vortex has
no torque to move it.

## 3. Result — the detector does not converge

Detector-vs-reference error at z = 0:

| step | N=48 dt=.005 | N=48 dt=.0025 | N=64 dt=.005 | N=64 dt=.0025 |
|---|---|---|---|---|
| 0 | 0.0000 | 0.0000 | 0.1326 | 0.1326 |
| 20 | 0.0000 | 0.0000 | 0.1326 | 0.1326 |
| 40 | 0.0000 | 0.0000 | 1.9556 | 0.1326 |
| 60 | — | 1.7678 | 2.5633 | 1.6447 |
| 80 | — | 1.2019 | 2.5633 | 1.9556 |
| 100 | — | 1.7678 | 1.9556 | 1.9556 |
| 120 | — | 2.3570 | 2.1333 | 2.5633 |
| 140 | — | 2.3570 | 2.5837 | 2.5633 |
| 160 | — | 2.3570 | 0.1326 | 2.5633 |
| 180 | — | 2.3570 | 1.0599 | 2.5633 |
| 200 | — | 1.4142 | 0.8529 | 1.9556 |

Refining the grid makes it **worse**, not better (N=64 peaks at 2.58 vs N=48 at 2.36).
Halving the timestep changes almost nothing. So the drift is neither physical motion
nor a resolution/timestep effect.

## 4. Diagnosis — detector bias

| test | outcome |
|---|---|
| Physical motion? | **No** — reference stable at (0,0) in all 4 runs, all slices, all frames |
| Numerical instability? | **No** — `competing_minima = 1` throughout; dt 0.005 vs 0.0025 nearly identical |
| Grid convergence? | **No** — error grows with N |
| Winding around the detector | **+1 at r = 3 and r = 4** throughout; occasional 0 at r = 2 |

The winding measurement is robust; the **centroid** is not. The ±1 hit-list is a
disc whose radius is set by the loop radius, and when the core structure spreads the
disc becomes large and ambiguous, so its centroid wanders. The estimator is
ill-conditioned, not the physics.

## 5. Verdict

**Gate 1 FAILS its acceptance condition.** Localization error is bounded (≤ 2.6
grid units) but does **not** converge under refinement, and the reference shows the
vortex is stationary. D3 remains `PARTIAL — TEMPORAL DRIFT`, reclassified as
**detector bias** rather than physical motion.

Full vortex-line evolution: **NOT_CERTIFIED**.

## 6. What would fix D3

- Replace the centroid with a **localised** estimator: intersect the ±1 discs from
  two different loop radii, or bisect the winding-sign boundary.
- Track the **density local minimum** as the primary localizer (stable here) and use
  winding only as the topological confirmation.
- Report the disc radius alongside the centroid, so an ambiguous localization is
  visible rather than silent.

## 7. Gate 2 — not run here

GPE stationarity remains `NOT_TESTED`. It is a separate gate and is not started in
this pass.
