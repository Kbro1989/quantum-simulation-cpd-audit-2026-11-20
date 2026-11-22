# Regularized vortex + independent circulation

**Date:** 2026-11-22
**Script:** `cpd_vortex_regularized_2026-11-22.py`
**Measurements:** `pks_research_index/quantum_vortex_regularized.json`

Closes two open gates from the audit: the non-regular initial state, and a
circulation measurement that restated the winding number.

---

## 1. The initial-state defect

The state used until now was

$$\psi = A\,e^{-r^2/4\sigma^2}\,e^{i\theta}$$

Its amplitude is **maximal** on the axis, so it is a singular, non-regular field:
the phase is undefined where the amplitude is largest. A regular singly-quantized
vortex requires $\psi \sim f(r)e^{i\theta}$ with $f(r)\to0$ as $r\to0$.

The corrected profile:

$$\psi = A\,r_\perp\,e^{-(r_\perp^2+z^2)/4\sigma^2}\,e^{i\theta},
\qquad r_\perp=\sqrt{x^2+y^2}$$

vanishes linearly on the axis and keeps unit winding.

## 2. Independent circulation

Detector v3 computed $\Gamma$ from the same phase increments used for the winding
number, so D4 restated D2. Here $\Gamma$ comes from the **velocity field**

$$\mathbf v=\frac{\hbar}{m}\,\mathrm{Im}\!\left(\frac{\nabla\psi}{\psi}\right)$$

integrated around the loop — a different numerical route (gradient of the complex
field, no phase-difference sum).

## 3. Measurements

Both grids have the origin exactly on a node (N even), confirming again that
`Grid3D` uses `dx = (hi-lo)/N`.

### D1 — core depletion: **PASSES**

| grid | axis ρ | annulus ρ (1.5<r<2.5) | depleted |
|---|---|---|---|
| N=48 | 0.000000 | 0.016170 → 0.016428 | **yes**, every frame |
| N=64 | 0.000000 | 0.016420 → 0.016693 | **yes**, every frame |

The regularized profile fixes what the earlier Gaussian could not: the axis is now
genuinely density-depleted at every step.

### D2 — winding: **PASSES**

$+1.000$ at $r = 2, 3, 4$, at every frame, on both grids.

### D4 — independent circulation: **PASSES, qualified**

| grid | ratio Γ/(h/m) across radii and frames |
|---|---|
| N=48 | 0.9912 – 1.0155 |
| N=64 | 0.9954 – 1.0088 |

The finer grid is closer to 1, so the residual is discretization error, not a wrong
topology. The spread is ~1% at N=48 and ~0.5% at N=64.

### D3 — blind localisation: **still time-limited**

| step | N=48 error | N=64 error |
|---|---|---|
| 0 | **0.0000** | 0.1326 |
| 10 | **0.0000** | 0.1326 |
| 20 | **0.0000** | 0.1326 |
| 30 | 1.7678 | 1.6447 |
| 40 | 1.2019 | 1.9556 |

Better than before — exact at t = 0–20 on N=48 — but the localiser still loses the
line late. D3 remains `INITIAL_CONDITION_VALIDATED_ONLY` for the evolved state; the
early-time agreement is new and recorded.

## 4. Disposition

| diagnostic | gaussian state (v3) | regularized state |
|---|---|---|
| D1 core depletion | FAIL | **PASS** |
| D2 winding = 1 | PASS with caveat | **PASS** |
| D3 localisation | exact at t=0 only | exact at t=0–20 (N=48); **still not certified late** |
| D4 circulation | restated D2 | **independent route, ratio 0.99–1.02** |

Full vortex-line evolution remains `NOT_CERTIFIED` — D3 degrades after step 20 and
the circulation residual is ~1% at N=48. Both are now measured rather than assumed.

## 5. Next

- D3 across later times and finer grids, to find where the localiser breaks.
- Circulation residual vs grid resolution, to confirm it converges to 1.
- A Gross–Pitaevskii evolution of the regularized state, to test whether the core
  profile is a stationary solution or relaxes.
