# Schauberger–Egg Geometry / Classical & Quantum Vortex — Research Atlas (seed)

**Saved:** 2026-11-22
**Workspace:** `C:\Users\krist\Desktop\quantum-simulation-cpd-audit-2026-11-20`
**Status:** RESEARCH SEED — not certified. Every claim below carries an evidence
class. Nothing here has been independently re-derived or re-fetched in the saving
session except where the verification log in §15 says so.

## 0. How to read this document

| Class | Meaning |
|---|---|
| **RECOVERED** | Recovered from prior sessions of this project (Sept 27, Oct 25–26 2026 per the source). Not re-verified this session. |
| **SOURCED** | Supplied by an external research pass, with a URL. **Not yet fetched.** Treat as a lead, not as fact. |
| **DERIVED** | Arithmetic or algebra performed in the source pass. Reproducible, but the inputs are SOURCED. |
| **PROPOSED** | Future work. Not executed. |

Standing rule carried in from the sovereign-stack method: **map original
mechanism → identify inversions/obfuscations → classify drift.** Mathematical
resemblance is never treated as proof of a shared physical mechanism.

---

## 1. Recovered research — where the thread left off

Elements previously identified in this project (**RECOVERED**):

- `MHD-Propulsion-Controller-Simulator-main` — Schauberger-derived project.
- `vortexTension`, `implosionScore`
- `kingwen_schauberger_layer`
- `_compute_schauberger_metrics()`
- Quantum-density grids; Hamiltonian / eigenmode terminology.
- 1D, 2D, 3D split-step wavepacket simulations, CPU and GPU paths.

One previously examined expression (**DERIVED**, flagged in the source as a
computational metric, *not* an established physical law):

$$\text{vortex\_tension} = \frac{\text{upper}\cdot\text{lower}}{49}$$

**September 27 — centripetal egg vortices** (**RECOVERED**): the phrase
"8 Biomes, Schauberger Centripetal Egg Vortices"; an elevation field built from a
deterministic superposition of a Schauberger-inspired centripetal vortex wave and
trigram indices; a possible reversible geometry/state representation linking
hexagram state, phase, expected-value perturbations and 3D geometry.

**Open issue carried forward:** several distinct vortex formulas existed
(trigram-index constructions and emotional-vector constructions) and it was
**never established that they represent the same physical quantity**. The source
explicitly marks this as a starting point, not something to discard.

---

## 2. The strongest lead: the mathematics of the egg

**Norbert Harthun and Ines Rennert — _Die Ei-Kurve als Schnitt des Hyperbolischen
Kegels_ (The Egg Curve as a Section of the Hyperbolic Cone).** — **SOURCED**
PKS host: <https://pks.or.at/wp-content/uploads/Berechnung_Ei-Kurve.pdf>

### 2.1 Walter Schauberger's starting equation

String length × frequency:

$$l\,f = 1 \quad\Rightarrow\quad l = \tfrac{1}{n},\; f = n$$

Generalised as the _Tongesetz_ (Tonal Law):

$$\boxed{\tfrac{1}{n}\cdot n = 1}$$

Setting $l = x$, $f = y$ gives $\boxed{xy = 1}$ — an equilateral hyperbola.

Two separate recognitions (**DERIVED**, and the source is explicit about the split):

1. The inverse relation is mathematically valid.
2. The claim that it is a *universal law governing physical nature* is a much
   larger hypothesis and **is not established by the identity itself.**

### 2.2 Hyperbolic cone and egg curve

Construction sequence (**SOURCED**):

1. Begin with the positive branch of $xy = 1$.
2. Rotate about the $y$-axis → three-dimensional surface.
3. Project a hyperbolic spiral onto that surface.
4. Intersect with an inclined plane.
5. The intersection can produce an egg-shaped curve.

Key geometric distinction: **the egg is not simply an ellipse, nor necessarily a
conventional ellipsoid.**

Parameters: $z_0$ (height where the cutting plane meets the vertical axis),
$\alpha$ (inclination of the cutting plane), $\bar x, \bar y$ (coordinates in the
resulting plane). One derived representation:

$$\bar x = \pm\sqrt{ \frac{1}{(z_0 - \bar y \sin\alpha)^2} - (\bar y \cos\alpha)^2 }$$

Consequence: the geometry is **parameterisable**, not an arbitrary egg-shaped mesh.

### 2.3 Research lineage named in the document (**SOURCED**)

| Researcher | Contribution |
|---|---|
| Walter Schauberger | Original tonal law and hyperbolic-cone construction |
| Max Mack | Identified the egg-shaped planar sections |
| Norbert Harthun | 1972–73 harmonic egg-curve investigations |
| Heinrich Riffer | General derivation of the egg-curve equation, 1973 |
| Christoph Kirfel | Further geometric investigations |
| Horst von Hasselbach | Egg-shadow and planetary geometry |
| Ines Rennert | Re-derived and systematised the egg-curve equations |

Also referenced: Claus Radlberger, _Der hyperbolische Kegel nach Walter
Schauberger_ (1999).

---

## 3. Viktor versus Walter — a distinction the research must keep

| | Viktor Schauberger | Walter Schauberger |
|---|---|---|
| emphasis | natural water movement, river engineering, spiral conduits, vortex formation, flow resistance, water transport | hyperbolic cones, egg geometry, tonal mathematics, harmonic relationships, reaction vessels, non-Euclidean constructions |
| IP | **AT138296B** (1934) water flow | **GB1084286A** (1963 application, 1967 published) egg-shaped reaction chamber; 1966 whirlpool water-purification patent |

Resulting research sequence (**PROPOSED**):

**Viktor's observed fluid behaviour → Walter's geometric abstraction → engineered
reaction chambers → modern CFD validation.**

The source's own assessment: this sequence is far more concrete than jumping from
Schauberger's philosophy straight to quantum mechanics.

---

## 4. Patent leads (**SOURCED**)

**GB1084286A — Vortex reactor; continuous discharge mixing apparatus** —
Schauberger Biotechnik AG, 1963 application, published 1967.
<https://patents.google.com/patent/GB1084286A/en>

Reported contents: egg-/heart-/pear-shaped longitudinal profile; narrower and
wider end; tangential fluid inlets; axial outlet; vortex-based continuous mixing;
applications to liquids, gases and particulate material. Value: a real engineering
configuration with an actual geometry and flow arrangement.

**AT138296B — Water flow (1934).** <https://patents.google.com/patent/AT138296B/en>
Reported: dividing the outer flow region into individual vortex structures, curved
guide surfaces and grooves producing secondary spiral motion while the central
flow region advances — a direct connection to boundary-layer manipulation,
secondary flow and vortex organisation.

---

## 5. Modern fluid dynamics — a bridge that exists

### 5.1 TU Delft thesis

**Teja Donepudi — _Vortices in Hyperbolic Funnels as Aeration Systems: A Numerical
Study_** (2021). <https://repository.tudelft.nl/record/uuid%3A408b37f5-9de2-45f5-987a-f60f8bbcc2a3>

Reported findings: multiple vortex regimes under different imposed flows; a
twisted vortex structure with higher gas-dissolution rates; 3D transient CFD;
Euler–Euler multiphase and Volume-of-Fluid; SST $k$–$\omega$ turbulence modelling;
secondary-flow instabilities analogous to Taylor vortices; increased interfacial
area and mixing in the twisted regime. Secondary-flow instabilities transport
bulk liquid toward the air–water interface, improving gas transfer. **The outflow
was still undersaturated under the tested conditions.**

### 5.2 Peer-reviewed follow-up

**Donepudi et al. (2024) — _Numerical analysis of vortex dynamics in hyperbolic
funnels using computational fluid dynamics._** Physics of Fluids 36, 095171.
<https://pure.tudelft.nl/ws/portalfiles/portal/222293630/095171_1_5.0222216.pdf>

Funnel profile:

$$\boxed{z = \frac{0.079}{r^2}}$$

Two regimes investigated: **Straight** and **Twisted Schauberger**, with
experimental measurements validating the CFD.

| Parameter | Published study |
|---|---|
| coarse mesh | 507,620 cells |
| intermediate | 1,105,716 cells |
| selected | 2,023,896 cells |
| largest | 3,057,147 cells |
| selected mesh cost | ≈ 10,000 CPU hours |
| largest mesh cost | ≈ 19,000 CPU hours |

< 5 % difference in selected variables between the ~1 M and ~2 M cell meshes.

**Distinction the paper draws, and which must be preserved:** curved streamlines
are not the same as local fluid rotation. $u_\theta \propto 1/r$ describes an
irrotational vortex outside its singular core; $u_\theta \propto r$ describes
solid-body rotation with non-zero vorticity.

Vortex regimes depend on funnel geometry and tangential inlet velocity — i.e.
**systematically variable parameters.**

### 5.3 A geometric discrepancy worth investigating (**open**)

| construction | equation | provenance |
|---|---|---|
| PKS / Walter Schauberger | $xy = 1$, rotated hyperbola, inclined-plane sections | Harthun & Rennert |
| 2024 CFD funnel | $z = 0.079/r^{2}$ | Donepudi et al. |

These are **not automatically the same surface.** The reciprocal-square profile
differs from the simplest rotated $xy = 1$ construction. Before any coincidence is
claimed, establish: coordinate mapping, exponent, dimensional scaling, and the
surface definition. Candidate explanations: a genuinely different hyperbolic
geometry; a later engineering adaptation; a coordinate transformation; or two
constructions sharing only a general description.

---

## 6. The quantum-vortex connection

### 6.1 Quantised vortices in BEC

**Alexander L. Fetter and Anatoly Svidzinsky (2001)** — _Vortices in a Trapped
Dilute Bose–Einstein Condensate._ <https://arxiv.org/abs/cond-mat/0102003>

Gross–Pitaevskii equation:

$$i\hbar\frac{\partial\psi}{\partial t} = \left[ -\frac{\hbar^2}{2m}\nabla^2 + V + g|\psi|^2 \right]\psi$$

Hydrodynamic form $\psi = \sqrt{\rho}\,e^{iS}$ gives the velocity field:

$$\boxed{\mathbf v = \frac{\hbar}{m}\nabla S}$$

So the wavefunction carries a density field, a phase field, a velocity field from
phase gradients, and quantised circulation around vortex cores. For a singly
quantised vortex:

$$\boxed{\oint_C \mathbf v \cdot d\mathbf l = \frac{h}{m}}$$

The vortex core is where amplitude vanishes and phase becomes singular.

### 6.2 Relevance to the existing 1D/2D/3D solvers

Proposed computational layering (**PROPOSED**):

| layer | content |
|---|---|
| geometry | Schauberger hyperbolic cone, egg boundaries, funnel geometry, adjustable eccentricity |
| physical field | density, phase, velocity, vorticity, pressure, circulation, energy |
| 1D | wavepacket and nonlinear phase evolution |
| 2D | vortex nucleation and circulation |
| 3D | vortex lines, rings, reconnections |
| validation | conservation, energy spectra, vortex topology, circulation quantisation, boundary conditions, convergence |

**Implementation warning carried in the source:** a conventional *linear*
split-step Schrödinger solver is **not automatically** a Gross–Pitaevskii solver.
The nonlinear term $g|\psi|^2$ must be implemented, and physical normalisation and
boundary conditions must be correct. Existing 1D/2D/3D CPU/GPU work could provide
the numerical foundation, **but each solver needs independent verification.**

### 6.3 Elliptic vortices — prioritised by the source

**Wladimir Lyra (2021)** — _Vortex Solution in Elliptic Coordinates._
<https://arxiv.org/abs/2108.04013>

Vortices with closed elliptic streamlines can be exact nonlinear solutions of the
compressible Euler equation; constant-vorticity flow expresses simply in elliptic
coordinates.

Why prioritised: connects eccentricity directly to vortex geometry; provides a
*derived* flow rather than a visually inferred spiral; supplies another coordinate
representation to compare against the egg; gives a route to testing whether an
egg-shaped boundary changes vortex organisation. Assessed as a stronger bridge
than observing that both systems contain spirals.

### 6.4 Quantum turbulence

**Bradley, Neely, Yu and Anderson (2026)** — _Turbulence in Quantum Gases:
Vortices, Waves, and Cascades._ <https://arxiv.org/abs/2607.22244>

Covers quantised circulation; compressible/incompressible kinetic-energy spectra;
vortex-resolved correlations; 2D Onsager clustering; 3D vortex-line turbulence;
Kelvin-wave dynamics; sound-wave interactions; energy cascades and spectral fluxes.

**Rule the source proposes adopting:** a power-law energy spectrum alone does not
establish a turbulent cascade. Additional diagnostics required — energy fluxes,
forcing and damping scales, vortex correlations, decay laws.

### 6.5 Vortex rings and reconnections

Quantum vortex-ring motion and decay in superfluid helium (dissipation, thermal
component). Connection worth exploring: whether confining-geometry parameters
affect ring stability, radius, reconnection frequency, energy dissipation,
Kelvin-wave excitation, vortex-line density — all measurable.

---

## 7. Computational geometry resources (**SOURCED**)

Wolfram Language vector analysis — `Grad`, `Div`, `Curl`, `Laplacian`,
`CoordinateTransform`, `TransformedField`. Documented coordinate systems include
elliptic cylindrical, prolate spheroidal, oblate spheroidal, toroidal, confocal
ellipsoidal.

Coordinate systems to investigate together (**PROPOSED**):

| system | use |
|---|---|
| elliptic cylindrical | eccentric vortex cross-sections |
| prolate spheroidal | elongated egg-like geometry |
| toroidal | vortex rings |
| spherical | baseline / comparison geometry |

Central question: **does a hyperbolic-cone-derived egg geometry produce a
measurable advantage over cylindrical, spherical or ellipsoidal geometries when
physical conditions are held constant?**

---

## 8. Historical archives (**SOURCED**)

Internet Archive CDX index for `pks.or.at`:

| capture date | material | value |
|---|---|---|
| 1998-12-02 | original PKS homepage | early organisational history |
| 2000-06-21 | `bio-vs.html` | Viktor biography |
| 2000-06-21 | `bio-ws.html` | Walter biography |
| 2007-07-30 | `1upper_en.html` | older English-language material |
| 2019-05-06 | English PKS homepage | later presentation |
| 2019-07-19 | calculations / energy / water pages | historical development |

Capture dates are **not** publication dates. Research task: identify which
equations, geometries and interpretations were present in earlier editions and
which were introduced or revised later.

CDX query:
<https://web.archive.org/cdx/search/cdx?url=pks.or.at%2F*&output=json&filter=statuscode:200&collapse=urlkey&fl=timestamp,original>

---

## 9. Research matrix (**PROPOSED**)

| domain | core question | evidence |
|---|---|---|
| Schauberger hydrodynamics | how does spiral flow change transport and resistance? | patents, experiments |
| egg geometry | exact equations and surface intersections | PKS mathematical papers |
| hyperbolic funnels | which geometries give stable vortex regimes | TU Delft CFD |
| classical vortex dynamics | vorticity, circulation, secondary flow | Euler / Navier–Stokes |
| quantum vortices | phase singularities, quantised circulation | Gross–Pitaevskii |
| quantum turbulence | energy exchange between lines, rings, waves | arXiv, experiments |
| computational geometry | same geometry across different physical models | Wolfram + existing solvers |

---

## 10. Variables to track (**PROPOSED**)

**Classical:** Reynolds number $Re$; swirl number $S$; vorticity $\boldsymbol\omega$;
circulation $\Gamma$; pressure $P$; velocity $\mathbf u$; boundary-layer thickness;
curvature and eccentricity; interfacial area; hydraulic retention time.

**Quantum:** wavefunction $\psi$; density $|\psi|^2$; phase $S$; healing length $\xi$;
quantised circulation; winding number; vortex-line density; Kelvin-wave spectrum;
compressible and incompressible energy spectra.

**Geometry:** hyperbolic-cone parameters; egg-curve parameters; eccentricity; aspect
ratio; surface curvature; coordinate transformations; boundary conditions; volume
and surface-area ratios.

---

## 11. Hypotheses worth testing (**PROPOSED — none executed**)

- **H1 geometric vortex organisation** — egg/hyperbolic boundary vs cylindrical
  boundary, with $Re$, inlet conditions and fluid properties held constant.
- **H2 secondary vortex formation** — does the geometry encourage Taylor-like
  secondary vortices as in the hyperbolic-funnel work?
- **H3 energy transport** — does geometry change the kinetic-energy distribution
  between large-scale flow and smaller vortical structures?
- **H4 quantum confinement** — can egg-shaped / hyperbolic external potentials
  alter vortex nucleation, stability or eigenmode structure in Gross–Pitaevskii?
- **H5 geometric scaling** — dimensionless relations between funnel eccentricity,
  vortex-core dimensions, circulation and energy spectra.
- **H6 classical/quantum correspondence** — whether analogous geometric
  organisation survives across models **while respecting the different governing
  equations**. Explicitly: do not expect the same microscopic physics.

---

## 12. Consolidated reading list

**Historical / original**
1. Viktor Schauberger — PKS <https://pks.or.at/en/viktorschauberger/>
2. Walter Schauberger — PKS <https://pks.or.at/en/walterschauberger/>
3. PKS patent inventory <https://pks.or.at/en/patents/>
4. _Die Ei-Kurve_ — <https://pks.or.at/wp-content/uploads/Berechnung_Ei-Kurve.pdf>
5. GB1084286A — <https://patents.google.com/patent/GB1084286A/en>
6. Schauberger primary-source patent archive <https://schaubergerfiles.com/vortex-file/>

**Engineering / fluid dynamics**
7. Donepudi et al. (2024) — <https://pure.tudelft.nl/ws/portalfiles/portal/222293630/095171_1_5.0222216.pdf>
8. Donepudi (2021) thesis — <https://repository.tudelft.nl/record/uuid%3A408b37f5-9de2-45f5-987a-f60f8bbcc2a3>
9. Lyra (2021) — <https://arxiv.org/abs/2108.04013>
10. Wolfram vector analysis — <https://reference.wolfram.com/language/tutorial/VectorAnalysis.html.en>
11. Wolfram coordinate systems — <https://reference.wolfram.com/language/VectorAnalysis/guide/CoordinateSystems.html>

**Quantum physics**
12. Fetter & Svidzinsky — <https://arxiv.org/abs/cond-mat/0102003>
13. Bradley et al. (2026) — <https://arxiv.org/abs/2607.22244>
14. Tang et al. — quantum vortex-ring dissipation <https://arxiv.org/abs/2211.01560>
15. Fetter & Svidzinsky (review copy) — <https://boulderschool.yale.edu/sites/default/files/files/Vortices.pdf>

**Historical archives**
16. Wayback PKS CDX — <https://web.archive.org/cdx/search/cdx?url=pks.or.at%2F*&output=json&filter=statuscode:200&collapse=urlkey&fl=timestamp,original>
17. Internet Archive — <https://archive.org/>
18. OEIS — <https://oeis.org/>

---

## 13. Proposed next experiment (**PROPOSED — not executed or certified**)

Geometry comparison: **A** cylinder (baseline), **B** egg-curve, **C** hyperbolic
funnel, **D** toroidal — under **two independent physical models**: classical CFD
(Navier–Stokes, multiphase where required) and quantum simulation
(Gross–Pitaevskii). Common measurements: energy distribution, vortex topology,
circulation, stability, boundary sensitivity, geometry-dependent mode structure.

Certification requirements: analytical baseline; mesh/grid convergence;
independent numerical implementation; conservation checks; reproducible parameter
sweeps; experimental comparison where physical data exists.

**Constraint:** the same geometry may be compared across models, but classical and
quantum systems require their own dimensionless parameters and boundary conditions.
They cannot share identical numerical settings.

---

## 14. Boundaries — what is explicitly NOT concluded

- That Schauberger discovered quantum vortex physics.
- That implosion represents a new energy source.
- That the Tonal Law is a universal physical law.

None follows from the evidence above. The source's own assessment: the egg
mathematics is real and recoverable; the hyperbolic-funnel research has reached
peer-reviewed engineering; quantum vortices give a rigorous independent domain.
Enough to justify serious mathematical and computational investigation — **as a
separate, independently validated branch**, preserving existing solver evidence
rather than mixing new hypotheses into established solver results.

---

## 15. Verification log

**URLs fetched and content-checked 2026-11-22** (live fetch, not from the source
pass). All seven load-bearing sources resolve and match the description given above.

| # | source | result |
|---|---|---|
| 1 | `pks.or.at/.../Berechnung_Ei-Kurve.pdf` | **VERIFIED.** Title _Die Ei-Kurve als Schnitt des Hyperbolischen Kegels / Das „Tongesetz" nach Walter Schauberger_, authors Norbert Harthun; Ines Rennert. Confirms the monochord derivation $l \cdot f = 1$, the generalisation $\frac1n \cdot n = 1$, and that Walter raised it to „Urgesetz des Universums". **The document itself labels that universal-law step as Walter's individual thesis** („Diese eigenwillige Darstellung und These ist völlig neuartig und absolut individuell mit dem Namen Walter Schaubergers verbunden") — independent corroboration of the caution in §2.1. Full text cached at `cache/web/pks.or.at-9892e85ff2.md`. |
| 2 | arXiv:2108.04013 | **VERIFIED.** _Vortex solution in elliptic coordinates_, Wladimir Lyra, submitted 2021-07-26, RNAAS Research Notes. Abstract matches verbatim: closed elliptic streamlines are exact nonlinear solutions of the compressible Euler equation; constant-vorticity flow reduces to $\dot\mu = 0$, $\dot\nu = \mathrm{const}$ along the streamline matching the vortex eccentricity. |
| 3 | arXiv:cond-mat/0102003 | **VERIFIED.** _Vortices in a trapped dilute Bose-Einstein condensate_ — review; Gross–Pitaevskii mean field, single-vortex structure/energy/dynamics/normal modes/stability, vortex arrays, thermal quasiparticles. |
| 4 | arXiv:2607.22244 | **VERIFIED.** _Turbulence in Quantum Gases: Vortices, Waves, and Cascades_. Abstract states the diagnostics that „show why power laws alone are insufficient evidence for a cascade" — direct confirmation of the rule proposed in §6.4. |
| 5 | GB1084286A | **VERIFIED.** GB patent, prior-art keywords reactor / chamber / materials / axial; classifications B01D 53/34 and 53/62 (gas purification, carbon oxides); cited materials span liquid, gas, particulate, solid, radiation, sterilising. Consistent with the reported vortex-reactor contents. |
| 6 | TU Delft repository record | **VERIFIED.** _Vortices in Hyperbolic Funnels as Aeration Systems: A Numerical Study_, T. Donepudi, Master thesis, TU Delft Mechanical Engineering, graduation 2021-08-27. Abstract confirms Twisted regime highest gas dissolution, secondary-flow instabilities, and undersaturated outflow at the tested conditions. |
| 7 | arXiv:2211.01560 | **VERIFIED.** _Imaging the decay of quantized vortex rings to decipher quantum dissipation_ — superfluid He II, quantised vortex rings decorated with solidified deuterium tracer particles. |

| item | status |
|---|---|
| This document saved | 2026-11-22 |
| URLs fetched | **7 / 7 verified** (table above) |
| Equations re-derived | pending — $\bar x$ representation and $z = 0.079/r^2$ not yet checked against the sources |
| `xy=1` vs `z=0.079/r²` discrepancy resolved | **open** |
| H1–H6 tested | none |
| Relation to existing CPD audit | see `cpd_vortex_provenance_2026-11-22.md` — this atlas concerns the *introducing* (Schauberger) referent; the audit's vortex findings concern the *adopted* (quantum) referent |
