# PKS printed mathematics — recovery and verification

**Date:** 2026-11-22
**Source:** `Berechnung_Ei-Kurve.pdf` — Harthun & Rennert, _Die Ei-Kurve als Schnitt
des Hyperbolischen Kegels_. Archived copy used:
`pks_research_index/pks_capture_bodies/20201029223404_*.bin`
(SHA-256 `ec4358df4aabe6f5c588…`, 157,656 B, **byte-identical across the 2020-10-29,
2024-04-15 and 2026-07-11 captures** — so this is a fixed reference, not a moving target).
Pages rendered to `pks_research_index/pks_eikurve_pages/` at 200 DPI and read
visually; the PDF text layer fragments fractions and radicals, so the printed page is
the authority.

---

## 1. Recovered printed equations

### Equation (1) — explicit form (page 6)

$$\bar x = \pm\sqrt{\frac{1}{\left(z_0-\bar y\sin\alpha\right)^{2}}-\left(\bar y\cos\alpha\right)^{2}}
\qquad 0\le\alpha\le 90^{\circ},\ \bar y\neq 0$$

Matches the earlier transcription (EQ-04). The transcription is now **high confidence**.

### Equation (2) — parameter form (page 6)

$$r=\frac{1}{2\cos\varphi\sin\alpha}\left[\,z_0\pm\sqrt{\,z_0^{2}-\frac{4\cos\varphi\sin\alpha}
{\sqrt{\sin^{2}\varphi+\cos^{2}\varphi\cos^{2}\alpha}}}\,\right]$$

$$x=r\sin\varphi,\qquad y=r\cos\varphi,\qquad \varphi\neq 0,\ \varphi\le 2\pi$$

The earlier transcription of this equation was glyph fragments and is **superseded**.
This is the closed-form parameterisation the audit said was the blocker.

### Volume equation (page 9, unnumbered)

$$V=\frac{\pi}{\cos\alpha}\left[\frac{z_1+z_2}{\left(z_1z_0-\tan\alpha\right)\left(z_2z_0+\tan\alpha\right)}
-\frac{1}{3}\left(\frac{1}{z_1^{3}}+\frac{1}{z_2^{3}}\right)\right]$$

The earlier transcription of this equation was wrong and is **superseded**.
The source states the result for the "Oktav-Ei" as **V = 0,4045** with
$z_1=1$, $z_2=2$, and that the length 0→1 is the unit (1 cm ⇒ cm³).

---

## 2. Verification performed

Parameters: $z_1=1$, $z_2=2$ → $z_0=\frac{6}{7}=0.857142857143$,
$\tan\alpha = 1-\frac{z_0}{z_1}=\frac17$, $\alpha=8.130102354^\circ$.

### 2.1 Equation (2) closes — PROVEN

Scanning $\varphi\in(0,2\pi]$:

| root | behaviour |
|---|---|
| **negative** | bounded: $x\in[-1.191474,\,1.191474]$, $y\in[-1.010152,\,1.601886]$ |
| positive | unbounded ($|x|$ up to ~795) — the "flat mountain" cut the text describes |

**Convergence test.** The endpoint gap $|P(2\pi)-P(\varepsilon)|$ as the refinement
scale shrinks:

| ε | gap |
|---|---|
| 0.008 | 0.01281497 |
| 0.004 | 0.00640753 |
| 0.002 | 0.00320377 |
| 0.001 | 0.00160189 |
| 0.0005 | 0.00080094 |
| 0.0001 | 0.00016019 |

gap/ε = **1.601886** at every scale — the gap is exactly the sampling offset, first
order, so it vanishes in the limit.

**Analytic closure.** As $\varphi\to0^+$: $\cos\varphi\to1$, $\sin\varphi\to\varphi$,
$\sqrt{\sin^2\varphi+\cos^2\varphi\cos^2\alpha}\to\cos\alpha$, so

$$r^*=\frac{z_0-\sqrt{z_0^{2}-4\tan\alpha}}{2\sin\alpha}=1.6018862051$$

and $P(0^+)=(0,r^*)$. At $\varphi=2\pi$: $\cos\varphi=1,\ \sin\varphi=0$, giving the
same $r^*$ and $P(2\pi)=(0,r^*)$. **Both endpoints coincide — the closed egg profile
is established analytically, not just numerically.**

The earlier open-branch result came from equation (1), which describes one
half-branch, not the closed curve.

### 2.2 Volume — three-way disagreement, preserved

| source of the number | value |
|---|---|
| printed volume equation (recovered above) | **5.986907** |
| numerical volume of the actual closed curve, $\pi\int x^{2}\,dy$ | **7.736654** |
| source's stated result | **0.4045** |

These three do not agree. **The discrepancy is preserved, not forced.**

Possible causes, none confirmed: the printed equation may use a different
normalisation or a different pair of variables than $z_1=1,z_2=2$; the stated
0,4045 may refer to a differently scaled egg; or the printed equation and the
printed number may genuinely disagree in the source. Resolving it requires the
diagram conventions on pages 7–8 (the two-point and point-slope forms), which were
not recoverable in this pass.

---

## 3. Status changes

| equation | previous status | new status |
|---|---|---|
| EQ-04 | TRANSCRIPTION_CONDITIONALLY_EVALUATED | **ALGEBRAICALLY_VERIFIED_UNDER_STATED_INPUTS** (printed form matches; describes a half-branch, not the closed curve) |
| EQ-05 | NOT_VERIFIED | **NUMERICALLY_CLOSED** — the negative-root branch closes; the closed egg profile is established |
| EQ-10 | NOT_VERIFIED | **DISCREPANCY_PRESERVED** — equation recovered, but it does not reproduce the source's own stated value, and the closed-curve integral disagrees with both |

EQ-07, EQ-08, EQ-09 are unchanged: algebraic consistency under stated inputs, with
EQ-09's sign convention still requiring the page-7 diagram.

---

## 4. What this does and does not establish

**Established:** the closed egg curve exists as a parameterised curve, and its
parameter form is recoverable from a byte-stable archived document.

**Not established:** that the source's volume equation is correct, that its stated
0,4045 is reproducible, or that the geometry has any physical significance. The
audit's rule holds — a historical claim does not validate a mathematical identity,
and a mathematical identity does not establish a physical mechanism.

**Still open:** the page-7/8 diagram conventions (angle sign, vertex definitions),
which decide EQ-09 and may explain the volume discrepancy.
