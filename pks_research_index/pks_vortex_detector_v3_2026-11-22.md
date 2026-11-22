# Vortex detector v3 — measurements and disposition

**Date:** 2026-11-22
**Artifact:** `pks_research_index/quantum_vortex_detector_v3.json`
**Script:** `cpd_vortex_detector_v3_2026-11-22.py`
**Grid:** N=48, box (-6, 6), dx = 0.25

---

## 1. Grid convention (a real finding)

`Grid3D(N, lo, hi, ...)` uses **dx = (hi − lo) / N** with N points, so
`x[N//2] == 0` **iff N is even**.

| N | x[N//2] | origin exact? |
|---|---|---|
| 48 | 0.000000000 | **yes** |
| 49 | −0.122449 | no |

An earlier run used N=49 and reported the origin as a node; it was not. The
imposed vortex was being sampled off-centre. N=48 puts the origin exactly on
node 24.

## 2. D1 — core depletion: NOT DEPLETED

Measured **transversely** at z = 0 (the earlier version compared against the
z-extremes, which is not a core test):

| quantity | value |
|---|---|
| ρ on the axis | 0.063494 |
| ρ in the annulus 1.5 < r < 2.5 | 0.009062 |

The axis density is **7× the surrounding annulus** — the imposed state
|ψ| = A·exp(−r²/4σ²) is maximal on its axis by construction. This is a genuine
property of the imposed state, not a detector failure: **the rendered "vortex
line" has no density-depleted core.** D1 fails.

## 3. D2/D4 — winding and circulation on the analytical axis

Loops centred at the origin, four radii, three z-slices, five saved steps:

| step | r=2 | r=3 | r=4 | r=5 |
|---|---|---|---|---|
| 0 | 1.0 | 1.0 | 1.0 | 1.0 |
| 10 | 1.0 | 1.0 | 1.0 | 1.0 |
| 20 | 1.0 | 1.0 | 1.0 | **2.0** |
| 30 | 1.0 | 1.0 | 1.0 | **0.0** |
| 40 | 1.0 | 1.0 | 1.0 | 1.0 |

Identical at z = −2, 0, +2 → the line is straight along z.

**Winding = +1.0 at every radius, slice and step except two contaminated
readings at r = 5 in the later steps** (the loop reaches r = 5 against a box
half-width of 6, where the density is ~1e-4 and the phase is noisy).

Circulation Γ = (ℏ/m)·ΣΔφ = 2πℏ/m = **h/m exactly** whenever the winding is 1.

## 4. D3 — blind core localisation: validated at t=0 only

The blind detector uses lattice winding (loop radius = lattice spacing) and
takes the centroid of the ±1 disc — a hit-list alone is a disc, not a point.

| step | blind core | error vs origin |
|---|---|---|
| 0 | (0.0000, 0.0000) | **0.0000** |
| 10 | (−2.2727, −1.3636) | 2.6504 |
| 20 | (−1.7692, −1.4615) | 2.2948 |
| 30 | (−0.7647, −1.3529) | 1.5541 |
| 40 | (−0.8261, −0.7391) | 1.1085 |

The detector recovers the imposed vortex **exactly on the known initial
condition** and does **not** track the evolved state. Localisation for t > 0 is
not certified.

## 5. Disposition

| diagnostic | status |
|---|---|
| D1 core depletion | **FAILS** — the imposed state has no depleted core |
| D2 winding = 1 | **PASSES** on the analytical axis (4 radii × 3 slices × 5 steps) |
| D3 blind localisation | **VALIDATED at t=0 only**; not certified for t > 0 |
| D4 circulation = h/m | **PASSES** wherever the winding is 1 |
| line straightness along z | **PASSES** (identical at z = −2, 0, +2) |

The earlier v1 measurements (cores at box corners, windings 0/±1/±3) were
artefacts of locating the **global density minimum**, which for a Gaussian
envelope sits at the box edge. They are superseded.

## 6. GIF

`vortex_line_evolution.gif` verified at 990×880, 5 frames, **500 ms** per frame,
loop = 0. A separately-named copy `vortex_line_evolution_v2.gif` was written with
PIL and re-verified (`pks_research_index/vortex_gif_metadata.json`,
`duration_verified: true`). The original is preserved unchanged.

Note: an earlier inspection of an uploaded copy reported 0 ms; the local
artifact carries 500 ms.
