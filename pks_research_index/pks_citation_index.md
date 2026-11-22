# Citation index — schauberger_sources_2026-11-22

Built 2026-11-22. Bibliographic fields are extracted from the arXiv abs pages
and PDF text layers; hashes, byte sizes and page counts are derived from disk.

10 records: the original six-PDF collection plus the four primary
references retrieved on 2026-11-22 (reference audit step 4).

## Evidence populations (kept separate)

- **gpe_bec** — mean-field Gross-Pitaevskii / trapped BEC
- **two_fluid_helium** — coupled normal-fluid + superfluid helium models
- **classical_cfd** — classical fluid / CFD methodology
- **classical_geometry** — classical vortex geometry and coordinate systems

## Records

| id | year | population | version | title | venue | id/DOI | pages | sha256 |
|---|---|---|---|---|---|---|---|---|
| fetter_svidzinsky_2001_jopcm | 2001 | gpe_bec | published | Vortices in a trapped dilute Bose-Einstein condensate | Journal of Physics: Condensed Matter 13 (2001) R135-R194 | cond-mat/0102003 | 60 | `1d8758790b1c0aac` |
| fetter_svidzinsky_2001_arxiv | 2001 | gpe_bec | preprint | Vortices in a trapped dilute Bose-Einstein condensate | arXiv preprint | cond-mat/0102003 | 50 | `d8de900ebb0d59ed` |
| tang_2022_vortex_rings | 2022 | two_fluid_helium | preprint | Imaging the decay of quantized vortex rings to decipher quantum dissipation | arXiv preprint | 2211.01560 | 10 | `5f0c01e7cebc6fee` |
| bradley_2026_turbulence | 2026 | gpe_bec | preprint | Turbulence in Quantum Gases: Vortices, Waves, and Cascades | arXiv preprint | 2607.22244 | 32 | `35528d246c4d7937` |
| lyra_2021_elliptic | 2021 | classical_geometry | preprint | Vortex solution in elliptic coordinates | arXiv preprint | 2108.04013 | 7 | `4aafc1c8cec1e73e` |
| donepudi_2024_pof | 2024 | classical_cfd | published | Numerical analysis of vortex dynamics in hyperbolic funnels using computational fluid dynamics | Physics of Fluids 36, 095171 (2024) | 10.1063/5.0222216 | 12 | `e9e46e483f10344d` |
| dalfovo_1999_rmp | 1999 | gpe_bec | preprint | Theory of Bose-Einstein condensation in trapped gases | Reviews of Modern Physics 71, 463 (1999); arXiv preprint 1998 | cond-mat/9806038 | 69 | `66bd2946d9763efe` |
| castin_dum_1999_epjd | 1999 | gpe_bec | preprint | Bose-Einstein condensates with vortices in rotating traps | European Physical Journal D 7, 399-412 (1999) | cond-mat/9906144 | 31 | `05627909dd3bea87` |
| galantucci_2020_foucault | 2020 | two_fluid_helium | preprint | A new self-consistent approach of quantum turbulence in superfluid helium | arXiv preprint | 2001.01616 | 20 | `dc8f563af7ce55ca` |
| yui_2017_two_fluid | 2017 | two_fluid_helium | preprint | Three-Dimensional Coupled Dynamics of Two-Fluid Model in Superfluid 4He: Deformed Velocity Profile of Normal Fluid in Thermal Counterflow | arXiv preprint | 1711.02814 | 8 | `5cb51dfec7a5b5e0` |

## Relevance to the QuantumLab simulator

- **fetter_svidzinsky_2001_jopcm** (gpe_bec): Primary GPE reference for the QuantumLab 1D/2D/3D solver and BEC vortex physics.
- **fetter_svidzinsky_2001_arxiv** (gpe_bec): Same as the published version; useful for cross-checking pagination and equations.
- **tang_2022_vortex_rings** (two_fluid_helium): Bridge into 3D vortex-ring dynamics and dissipation; NOT a single-component GPE validation.
- **bradley_2026_turbulence** (gpe_bec): Literature map for later numerical and experimental vortex work in the GPE setting.
- **lyra_2021_elliptic** (classical_geometry): Geometric / mathematical reference (metric factors, differential geometry), not a quantum-vortex solution.
- **donepudi_2024_pof** (classical_cfd): Classical vortex geometry and CFD methodology; separate from quantum-simulation validation.
- **dalfovo_1999_rmp** (gpe_bec): Core BEC theory reference for the solver's mean-field layer.
- **castin_dum_1999_epjd** (gpe_bec): Directly relevant to rotating-trap vortex states and energy estimates.
- **galantucci_2020_foucault** (two_fluid_helium): Self-consistent two-fluid quantum-turbulence modelling; not a single-component GPE validation.
- **yui_2017_two_fluid** (two_fluid_helium): Coupled two-fluid dynamics; separate population from the GPE solver.
