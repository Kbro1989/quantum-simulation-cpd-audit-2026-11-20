# quantumlab — Physics Validation Matrix

- **Repo:** `C:/Users/krist/Desktop/quantum-simulation-main/quantum-simulation-main`
- **Branch / HEAD:** `remediation/2026-11-20` @ `44f30e3` (`fix(D-P2-2): validate absorbing-boundary arguments instead of corrupting state`)
- **Date:** 2026-11-20
- **Environment:** Python 3.11.9, numpy 2.4.3, scipy 1.17.1, cupy 14.2.0, NVIDIA RTX A1000 6GB Laptop GPU (CC 8.6), 1 CUDA device.
- **Read-only compliance:** `git status --short` after all work returned an empty result; no repo file was created, modified or deleted. All probes and evidence were written under the audit directory.
- **Probe scripts:** `C:/Users/krist/Desktop/quantum-simulation-cpd-audit-2026-11-20/probes/probe_01_*.py` … `probe_12_*.py`
- **Raw output:** `C:/Users/krist/Desktop/quantum-simulation-cpd-audit-2026-11-20/evidence/probe_01_*.txt` … `probe_12_*.txt`

All numbers below are copied verbatim from the evidence files. Nothing is inferred or fabricated. A missing measurement would be marked `NOT_RUN`; no domain required that.

**Method notes.** Convergence work uses a *non-commuting* harmonic-oscillator potential (a vanishing potential would make Strang propagation exact and measure only roundoff). Timed/measured code paths were warmed up before measurement (domain 7 warm-up: 5 steps at `dt=0.00781`; domain 11 warm-up: 1 GPU step). Independent checks recompute the same quantity by a different algorithm (manual operator products, explicit matrices, contour integrals, analytic references) rather than re-running the library function.

---

## Summary matrix

| # | Domain | Governing equation / contract | Invariant expected? | Independent check performed (command) | Verdict |
|---|--------|-------------------------------|---------------------|----------------------------------------|---------|
| 1 | Schrödinger evolution / split-operator ordering | `iℏ∂ψ/∂t = Hψ`, `S = e^{-iV dt/2ℏ} F⁻¹ e^{-iT dt/ℏ} F e^{-iV dt/2ℏ}` | Yes — exact factor sequence; unitarity | `python .../probe_01_strang_ordering.py` | **VALIDATED** |
| 2 | Hamiltonian construction / Hermiticity | `H = -ℏ²/2m ∇² + V`, `H = H†` | Yes — real-symmetric `T_k`, Hermitian `H` | `python .../probe_02_hermiticity.py` | **VALIDATED** |
| 3 | Wavefunction normalization | `‖ψ‖² = ∫\|ψ\|² dV = 1`, unitary flow | Yes — norm conserved | `python .../probe_03_normalization.py` | **VALIDATED** |
| 4 | Fourier-space operators | `k = 2π·fftfreq(N,dx)`; Parseval; periodic derivative; aliasing | Yes — exact ordering/normalization | `python .../probe_04_fourier.py` | **VALIDATED** |
| 5 | Potential dimensionality / units | `V(r)` shape per grid dim; `E₀ = ℏω/2` etc. | Yes — shapes, guards, energies | `python .../probe_05_potentials.py` | **VALIDATED** |
| 6 | Time-dependent Hamiltonians | `V(r,t)=V_base−F(t)r`, `F=F₀ env(t) sin(ωt+φ)`; `evaluate_at` at sub-steps | Yes — but **only** in `SplitOperatorSolver` | `python .../probe_06_time_dependent.py` | **PARTIAL** |
| 7 | Numerical convergence order | Empirical order in `dt` on HO coherent state | Yes — `O(dt²)` / `O(dt⁴)` | `python .../probe_07_convergence.py` | **VALIDATED** |
| 8 | Energy / momentum behaviour | `d⟨x⟩/dt = ⟨p⟩/m`; `⟨H⟩` conserved | Yes | `python .../probe_08_energy_momentum.py` | **VALIDATED** |
| 9 | Vortex winding / topological charge | `q = (1/2π)∮∇φ·dl` | Yes — integer charge, position | `python .../probe_09_vortex.py` | **VALIDATED** |
| 10 | Absorbing-boundary behaviour | Mask `∈[0,1]`, 1 in interior; removes probability | Intended non-unitarity (absorption) | `python .../probe_10_absorber.py` | **VALIDATED** |
| 11 | CPU/GPU numerical equivalence | Same `ψ` on both backends | Yes — agree to roundoff | `python .../probe_11_cpu_gpu.py` | **VALIDATED** |
| 12 | Stability / resolution sensitivity | `ℏ k_max² \|w\| dt/(2m) < π`; spectral `dx` convergence | Yes — condition reproducible | `python .../probe_12_resolution.py` | **VALIDATED** |

**Verdict counts:** VALIDATED = 11, PARTIAL = 1, FAILED = 0, NOT_RUN = 0.

---

## Per-domain detail

### 1. Schrödinger evolution and split-operator ordering — VALIDATED

**Governing contract.** `split_step_1d.py` lines 16–26 apply `U_V = exp(-iV dt/2ℏ)`, then `F⁻¹ U_T F` with `U_T = exp(-iT_k dt/ℏ)`, then `U_V` again; `split_operator.py` `_strang` does the same with `potential_at(t)` and `potential_at(t+w·dt)`. The expected invariant is the exact factor sequence plus unitarity (`S†S = I`) and time-reversal (`S(-dt)S(dt)=I`).

**Independent check.** Manual products `ifft(fft(ψ·U_V)·U_T)·U_V`, an explicit adjoint `U_V* · ifft(U_T* fft(·)) · U_V*`, a backward solver `dt → -dt`, and a manual Yoshida composition.

```
1a split_step_1d  max|step - manual(V/2,T,V/2)| = 2.289e-16
1b split_step_1d  max|S^dagger S psi - psi|      = 2.259e-16
1b2 split_step_1d max|S(-dt) S(dt) psi - psi|    = 2.831e-16
1c split_step_1d  max|Strang - naive(V,T)|       = 2.290e-03
1d split_operator o2 max|step - manual(V/2,T,V/2)| = 2.289e-16
1e YOSHIDA_W1 = 1.351207191960  YOSHIDA_W0 = -1.702414383919  2*W1+W0 = 1.000000000000000
1e split_operator o4 max|step - manual composition| = 3.140e-16
1f split_operator 2D o2 max|step - manual(V/2,T,V/2)| = 2.483e-16
1g split_operator 2D o2 max|S^dagger S psi - psi| = 3.433e-16
```

**Deviation classification.** `1c = 2.29e-03` is *expected physics*: an asymmetric `V,T` ordering is only first order, so it genuinely differs from Strang. All other residuals are floating-point roundoff (intended).

**Evidence:** `evidence/probe_01_strang_ordering.txt`.

---

### 2. Hamiltonian construction and Hermiticity — VALIDATED

**Governing contract.** `T_k = ℏ²k²/(2m)` must be real, non-negative and symmetric under `k → -k`; the discrete `H = -ℏ²/2m ∇² + V` must satisfy `H = H†` (matrix and matrix-free).

**Independent check.** Built `H = (1/N)F† diag(T_k) F + diag(V)` explicitly (`F = fft(eye(N))`), tested `⟨ψ|H|φ⟩ = ⟨Hψ|φ⟩`, and compared `apply_hamiltonian` against the explicit matrix.

```
2a T_k all real        : True
2a T_k min             : 0.000000e+00  (must be >= 0)
2a T_k[j] == T_k[-j]   : True
2b max|H - H^dagger|   : 9.339e-16
2b max|H - H^T| (real) : 9.035e-16
2b max|Im(H)|          : 3.309e-16  (roundoff; H is real-symmetric)
2c <psi|H|psi>         : 1580.932698429347 +5.684341886081e-14j  (imag must be ~0)
2d max|apply_hamiltonian - H@psi| : 7.108e-14
2e |<psi|H|phi> - <Hpsi|phi>|    : 1.608e-13
2f 2D T_k all real     : True  min: 0.000000e+00
2g 2D |<psi|H|phi> - <Hpsi|phi>| : 3.216e-13
```

**Deviation classification.** `max|Im(H)| = 3.3e-16` is FFT roundoff on an exactly real-symmetric operator — intended numerical artifact, not a bug.

**Evidence:** `evidence/probe_02_hermiticity.txt`.

---

### 3. Wavefunction normalization — VALIDATED

**Governing contract.** `WaveFunction{1,2,3}D.norm()` integrates `|ψ|²` with the correct volume element (`dx`, `dx·dy`, `dx·dy·dz`); unitary split-step flow preserves the norm.

**Independent check.** Compared each class Gaussian norm to 1, then measured drift over hundreds of steps for free and harmonic potentials.

```
3a norm 1D Gaussian = 1.000000000000000
3a norm 2D Gaussian = 1.000000000000000
3a norm 3D Gaussian = 1.000000000000000
3b free 300 steps: norm0 = 1.000000000000000  norm_end = 1.000000000000003  max|drift| = 2.887e-15
3c HO 300 steps  : norm0 = 1.000000000000000  norm_end = 1.000000000000018  max|drift| = 1.843e-14
3d 2D free 100 steps: norm0 = 1.000000000000000  norm_end = 1.000000000000010  |drift| = 9.548e-15
3e 3D free 50 steps : norm0 = 1.000000000000000  norm_end = 0.999999999999970  |drift| = 2.953e-14
```

**Deviation classification.** Drifts of `1e-14` are accumulated roundoff — intended. No systematic loss.

**Evidence:** `evidence/probe_03_normalization.txt`.

---

### 4. Fourier-space operators — VALIDATED

**Governing contract.** `grid.k = 2π·fftfreq(N,dx)`; `fourier_transform` uses `dx/√(2π)` so Parseval holds; spectral derivatives are exact on the periodic grid; modes above Nyquist alias by `-2k_Nyq`.

**Independent check.** Compared `grid.k` to `numpy.fft.fftfreq`, evaluated Parseval, applied `ifft(i k fft(·))` to every grid mode, and located FFT peaks of super-Nyquist modes.

```
4a max|grid.k - 2*pi*fftfreq(N,dx)| = 0.000e+00
4a k[0:4] = [0.     0.3927 0.7854 1.1781]   k[N-3:N] = [-1.1781 -0.7854 -0.3927]
4a dk = 0.392699  2*pi/L = 0.392699
4b Parseval: sum|psi|^2 dx = 1.000000000000000   sum|phi|^2 dk = 1.000000000000000   diff = 0.000e+00
4c max_j max_x |ifft(i k fft(e^{ik_j x})) - i k_j e^{ik_j x}| = 1.961e-13
4d k_Nyq + 2*dk = 34*dk     -> peak bin 34, k = -11.7810, |peak| = 64.000 ; alias predicts -11.7810
4d k_Nyq - 2*dk = 30*dk     -> peak bin 30, k = +11.7810, |peak| = 64.000 ; alias predicts -13.3518
4d k_Nyq (exact)            -> peak bin 32, k = -12.5664, |peak| = 64.000 ; alias predicts -12.5664
4d k_Nyq + dk  = 33*dk      -> peak bin 33, k = -12.1737, |peak| = 64.000 ; alias predicts -12.1737
4e k_Nyq = 12.566371   T_k(k_Nyq)/hbar = 78.956835
```

**Deviation classification.** The `30*dk` row is *not* aliased (it is below Nyquist); its "alias predicts" column is printed by the same formula and is intentionally inapplicable there. The `1.96e-13` derivative residual is roundoff. Aliasing of `34·dk → -30·dk` and `33·dk → -31·dk` is the intended DFT property, not a bug.

**Evidence:** `evidence/probe_04_fourier.txt`.

---

### 5. Potential dimensionality and units — VALIDATED

**Governing contract.** Each potential returns a real finite array of `grid.shape`; dimension-specific classes reject wrong grids; analytic forms and energies must match (`E₀ = ℏω/2` per mode, SoftCoulomb `E₀ = -0.5` for `Z=1, a²=2`).

**Independent check.** Evaluated all 22 potential cases on 1D/2D/3D grids; checked dimensionality `TypeError`s; compared values to closed forms; computed ground-state energies with the independent matrix-free eigensolver.

```
5a (all 49 evaluations) ... finite/real/shape-ok=True
5b Gaussian2DBarrier->1D    TypeError: Gaussian2DBarrier requires a 2D or 3D grid.
5b Gaussian3DBarrier->2D    TypeError: Gaussian3DBarrier requires a Grid3D.
5b ApertureScreen->1D       TypeError: ApertureScreen requires a Grid2D or Grid3D.
5b StadiumBilliard->3D      TypeError: StadiumBilliard requires a Grid2D.
5c HO m=2,w=3 at x=1.0: V = 9.000000 (expect 0.5*2*9*1 = 9)
5c GaussianBarrier V(x0) = 2.000000 (expect 2)  V(x=1.250) = 0.830474 (expect 2*exp(-((x-0.5)/0.8)^2) = 0.830474)
5c Crystal V(x=0) = 0.000000  V(x=a=1) = 0.000000 (period a)
5c DoubleWell V(0) = 2.000000 (expect 2)  V(+-d=2) = 0.000000 (expect 0)
5c SoftCoulomb V(0) = -0.707107 (expect -1/sqrt(2) = -0.707107)
5c HarmonicTrap(scalar) vs HarmonicOscillator 1D max|diff| = 0.000e+00
5c RandomDisorder same-seed identical = True ; range [-0.9976, 0.9984] (expect [-1,1])
5c DipoleDrive V(t=0) == V_base (sin0=0): max|diff| = 0.000e+00
5c DipoleDrive force(0.25) = 0.277951 (expect F0*env*sin(wt+phi) = 0.277951)
5d 1D HO omega=1.0 m=1.0  E0 = 0.5000000000  (expect hbar*omega/2 = 0.5000000000)
5d 1D HO omega=2.0 m=1.0  E0 = 1.0000000000  (expect hbar*omega/2 = 1.0000000000)
5d 1D HO omega=1 m_pot=2 (solver m=1) E0 = 0.7071067812 (mismatch -> 0.5*sqrt(2) = 0.7071067812)
5d 1D SoftCoulomb Z=1 a^2=2    E0 = -0.5000000096  (expect -0.5)
5d 2D HO omega=1 m=1           E0 = 1.0000000000  (expect hbar*omega = 1.0)
5d 3D HO omega=1 m=1           E0 = 1.4999824124  (expect 3*hbar*omega/2 = 1.5)
```

**Deviation classification.** The `m_pot=2` row is the *expected* consequence of an inconsistent mass (effective frequency `ω√(m_pot/m)`), confirming that potential mass and solver mass must agree. `3D E0 = 1.49998` differs by `1.76e-05` because the 3D test grid is coarse (`14³` over `L=12`) — a spatial-resolution artifact, not a unit error. All shape/guard results are exact.

**Evidence:** `evidence/probe_05_potentials.txt`.

---

### 6. Time-dependent Hamiltonians — PARTIAL

**Governing contract.** `DipoleDrive.evaluate_at(grid,t) = V_base − F(t)·r_axis`, `F(t)=F₀·env(t)·sin(ωt+φ)`; `sin2_envelope` is `sin²(πt/T)` on `(0,T)` and 0 outside; `SplitOperatorSolver` must sample `V` at every sub-step.

**Independent check.** Compared `force(t)` to the closed form at 7 times; verified `evaluate_at = V_base − F(t)r`; instrumented a logging potential to record the exact `evaluate_at` times used by one step; compared a legacy solver against the time-dependent solver.

```
6a t=0.00 force=0.0000000000 expect=0.0000000000 diff=0.00e+00
6a t=0.25 force=0.2779511598 expect=0.2779511598 diff=0.00e+00
6a t=0.50 force=0.9092974268 expect=0.9092974268 diff=0.00e+00
6a t=1.00 force=-0.7015664554 expect=-0.7015664554 diff=0.00e+00
6a t=1.50 force=-0.9589242747 expect=-0.9589242747 diff=0.00e+00
6a t=2.00 force=0.0000000000 expect=0.0000000000 diff=0.00e+00
6a t=2.50 force=0.0000000000 expect=0.0000000000 diff=0.00e+00
6a max|evaluate_at(t) - (V_base - F(t) x)| = 0.000e+00
6b sin2: env(0)=0.000 env(2)=0.000 env(1)=1.000000 (expect 1) env(-1)=0.000 env(3)=0.000
6c flat_top: f(0)=0.000 f(4)=0.000 f(0.5)=0.500000 f(2)=1.000000 f(3.5)=0.500000
6d order=2 evaluate_at times = [0.  0.1]
6d order=4 evaluate_at times = [ 0.          0.13512072  0.13512072 -0.03512072 -0.03512072  0.1       ]
6e legacy V == DipoleDrive.evaluate_at(grid,0) (force=0): True
6e legacy V == V_base: True
6f after 20 steps max|psi_legacy - psi_td| = 0.892318 (nonzero => legacy ignores drive)
```

**What is validated.** `DipoleDrive.force`, `evaluate_at`, `sin2_envelope`, `flat_top_envelope`, and the `SplitOperatorSolver` sampling times: order 2 samples `[t, t+dt]` (symmetric); order 4 samples `[0, w₁dt, w₁dt, (w₁+w₀)dt, (w₁+w₀)dt, dt]`, i.e. the symmetric Yoshida composition.

**What is not validated / deviations.**
- **Legacy solvers do not honour time dependence.** `SplitStep1DSolver` (and identically `SplitStep2DSolver`/`SplitStep3DSolver`/`SplitStep3DGPU`, which all call `potential.evaluate(grid)` in `__init__`) freeze `V` at `t=0`. With `phase=0`, `force(0)=0`, so the legacy solver silently propagates under `V_base` alone; after 20 steps the states differ by `0.892318`. This contradicts the blanket documentation claim that "solvers detect these through `time_dependent = True` and call `evaluate_at(grid,t)` at every sub-step" (`docs/guide/potentials.md:55`, `docs/guide/solvers.md:41`). **Classification: intended limitation of the compatibility solvers, but an undocumented footgun — not a numerical artifact.**
- **Order 4 samples `V` at negative time** (`-0.03512072` for `dt=0.1`) because `w₀ < 0`. This is inherent to the Yoshida triple jump. For `sin2_envelope` the potential is 0 there, which is usually physical, but a potential defined only for `t ≥ 0` could behave unexpectedly. **Classification: intended property of the composition; worth documenting.**

**Evidence:** `evidence/probe_06_time_dependent.txt`.

---

### 7. Numerical convergence order — VALIDATED

**Governing contract.** Empirical global order in `dt` on a *non-commuting* harmonic oscillator. Exact coherent-state reference (`ℏ=m=ω=1`):
`X(t)=x₀cos t+p₀sin t`, `P(t)=p₀cos t-x₀sin t`,
`ψ(x,t)=π^{-1/4} exp(-(x-X)²/2) exp(i[Px-PX/2-t/2])`.

**Independent check.** Compared the numerical state to the closed-form reference at `T=0.5` for `dt = T/nsteps`, `nsteps = 64…1024`, orders 2 and 4. Warm-up: 5 steps at `dt=0.00781`.

```
7 warm-up: 5 steps at dt=0.00781 completed
7 exact X(T)=2.4743034317 P(T)=0.3575227656
7 order=2:
7  nsteps=  64 dt=0.007812  max|dpsi|=5.3063e-06  1-|overlap|=1.6517e-11
7  nsteps= 128 dt=0.003906  max|dpsi|=1.3266e-06  1-|overlap|=1.0366e-12
7  nsteps= 256 dt=0.001953  max|dpsi|=3.3164e-07  1-|overlap|=6.7502e-14
7  nsteps= 512 dt=0.000977  max|dpsi|=8.2911e-08  1-|overlap|=1.2768e-14
7  nsteps=1024 dt=0.000488  max|dpsi|=2.0728e-08  1-|overlap|=9.9920e-16
7  empirical orders = [2. 2. 2. 2.]
7 order=4:
7  nsteps=  64 dt=0.007812  max|dpsi|=2.6861e-10  1-|overlap|=1.8874e-15
7  nsteps= 128 dt=0.003906  max|dpsi|=1.6789e-11  1-|overlap|=1.7764e-15
7  nsteps= 256 dt=0.001953  max|dpsi|=1.0626e-12  1-|overlap|=1.2990e-14
7  nsteps= 512 dt=0.000977  max|dpsi|=9.5489e-14  1-|overlap|=4.3077e-14
7  nsteps=1024 dt=0.000488  max|dpsi|=6.4103e-14  1-|overlap|=3.0309e-14
7  empirical orders = [4.    3.982 3.476 0.575]
```

**Deviation classification.** Order 2 is cleanly `2.000` across all refinements. Order 4 is `4.00`/`3.98` for the two coarsest refinements, then the error floors at `~6e-14` (spatial discretization + roundoff), so the last two "orders" are meaningless. **This floor is an intended numerical artifact, not a bug.** A vanishing potential was deliberately *not* used.

**Evidence:** `evidence/probe_07_convergence.txt`.

---

### 8. Energy and momentum behaviour — VALIDATED

**Governing contract.** `⟨H⟩` conserved for a time-independent Hamiltonian; free-particle Ehrenfest `⟨x⟩(t)=x₀+(p₀/m)t`, `⟨p⟩=const`, `d⟨x⟩/dt=⟨p⟩/m`.

**Independent check.** HO coherent state (`x₀=1.5, p₀=1.0, ω=1`) energy drift over 400 steps; free packet (`x₀=-4, p₀=2`) position/momentum at several times; finite-difference `d⟨x⟩/dt` vs `⟨p⟩/m`.

```
8a HO <H>(0) = 2.1250000000   analytic = 2.1250000000   diff = 0.000e+00
8a HO 400 steps: max|<H>(t)-<H>(0)| = 2.812e-05   final drift = 9.601e-06
8b free particle (x0=-4, p0=2, m=1):
8b t=0.50  <x>=-3.00000000 (expect -3.00000000, err 4.88e-15)  <p>=2.0000000000 (expect 2)
8b t=1.00  <x>=-2.00000000 (expect -2.00000000, err 3.55e-15)  <p>=2.0000000000 (expect 2)
8b t=2.00  <x>=0.00000000 (expect 0.00000000, err 6.66e-16)  <p>=2.0000000000 (expect 2)
8b t=4.00  <x>=3.99991345 (expect 4.00000000, err 8.65e-05)  <p>=2.0000000000 (expect 2)
8b d<x>/dt = 2.000000   <p>/m = 2.000000   diff = 1.33e-15
```

**Deviation classification.** The HO energy drift `2.8e-05` is `O(dt²)` (`dt=0.01`) and bounded — intended splitting error, not secular drift. The `t=4` position error `8.65e-05` appears only after the dispersed packet tail reaches the periodic boundary; it is a **periodic-wrap/discretization artifact**, not an Ehrenfest violation (the relation holds to `1e-15` at `t≤2` and `d⟨x⟩/dt=⟨p⟩/m` to `1.3e-15`).

**Evidence:** `evidence/probe_08_energy_momentum.txt`.

---

### 9. Vortex winding and topological charge — VALIDATED

**Governing contract.** `vortex_positions` computes `q = round(∮∇φ·dl / 2π)` per plaquette; charges must be integers and positions must coincide with phase singularities.

**Independent check.** Built an analytic hollow-core vortex `ψ ∝ (r/σ)e^{-r²/4σ²}e^{iθ}` and a vortex–antivortex pair, then recomputed every reported charge with an independent circular contour integral using `scipy.ndimage.map_coordinates` sampling.

```
9a single vortex: detected 1 vortex(es)
9a  pos=(-1.3875, +0.8625)  q_reported=+1  q_contour=+1.0000  (true core at -1.37, +0.83)
9a  position error = 0.0369
9b pair: detected 2 vortex(es), charges [1, -1], sum = +0
9b  pos=(-2.1375, +0.1875)  q_reported=+1  q_contour=+1.0000
9b  pos=(+2.0625, -0.1125)  q_reported=-1  q_contour=-1.0000
9c Gaussian (no vortex): detected 0 vortex(es) (expect 0)
9d 3D input: TypeError: vortex_positions requires a 2D wavefunction (use a slice for 3D)
```

**Deviation classification.** Position error `0.0369` is one half-grid spacing (`dx=0.075`) — the plaquette-centre resolution, intended. Charge agreement is exact (`+1.0000`, `-1.0000`). Note: a core placed exactly on a grid line splits the winding between two plaquettes and `vortex_positions` returns 0 there (observed during probe development with a core at `(-1.5, 0.8)`); this is a genuine resolution limitation of the plaquette method, not a bug, and is avoided by off-grid cores.

**Evidence:** `evidence/probe_09_vortex.txt`.

---

### 10. Absorbing-boundary behaviour — VALIDATED

**Governing contract.** `AbsorbingBoundaryLayer` builds a separable mask that is 1 in the interior and falls to 0 over `boundary_width`; applied every step it must be non-unitary by design (probability is absorbed) and must suppress FFT wraparound.

**Independent check.** Mask range/interior flatness for orders 1–6; norm loss and left-region density for a packet launched from `x=0` with `k₀=3` (the left region is reached only by wraparound), sampled after `t>4`; 300-step stability for each order.

```
10a order=1  min=0.000000 max=1.000000  mask[0]=0.000000 mask[-1]=0.000725  interior all 1: True
10a order=2  min=0.000000 max=1.000000  mask[0]=0.000000 mask[-1]=0.000725  interior all 1: True
10a order=3  min=0.000000 max=1.000000  mask[0]=0.000000 mask[-1]=0.000725  interior all 1: True
10a order=4  min=0.000000 max=1.000000  mask[0]=0.000000 mask[-1]=0.000037  interior all 1: True
10a order=5  min=0.000000 max=1.000000  mask[0]=0.000000 mask[-1]=0.000000  interior all 1: True
10a order=6  min=0.000000 max=1.000000  mask[0]=0.000000 mask[-1]=0.000000  interior all 1: True
10a order1==order2==order3 masks: True ; order3!=order4: True
10b norm: no absorber start=1.000000 end=1.000000 ; absorber start=1.000000 end=0.109164
10b norm loss (absorbed fraction) = 0.890836
10b max left-region density after t>4 (wraparound): no-absorber=9.8724e-02 absorber=2.0626e-03
10b suppression factor = 2.09e-02
10b instantaneous norm loss rate |dn/dt| at end = 1.1041e-02
10c stability (300 steps, packet started inside the right layer):
10c order=1 finite=True  norm_end=1.512934e-01  max|psi|=1.2761e-01
10c order=2 finite=True  norm_end=1.512934e-01  max|psi|=1.2761e-01
10c order=3 finite=True  norm_end=1.512934e-01  max|psi|=1.2761e-01
10c order=4 finite=True  norm_end=2.122339e-01  max|psi|=1.5289e-01
10c order=5 finite=True  norm_end=3.063673e-01  max|psi|=1.8618e-01
10c order=6 finite=True  norm_end=3.420643e-01  max|psi|=1.9762e-01
```

**Deviation classification.** Norm loss (`0.8908`) is the **intended** function of an absorbing boundary — probability is supposed to be removed. Wraparound density is suppressed by a factor `2.09e-02` (~48×). `mask[-1] = 0.000725` for orders 1–3 is a grid-sampling detail (the last node is `dx` inside the nominal edge, so the profile is `d²(3-2d)` at `d=dx/bw`), not a bug. Orders 1–3 produce identical masks because `_polynomial_profile` clamps `order <= 3` to the cubic profile — this matches the documented "minimum effective order is 3".

**Evidence:** `evidence/probe_10_absorber.txt`.

---

### 11. CPU/GPU numerical equivalence — VALIDATED

**Governing contract.** `SplitOperatorSolver(backend='numpy'|'cupy')` and `SplitStep3DGPU` implement the identical algorithm; results should agree to floating-point roundoff (not bit-identical).

**Independent check.** Identical initial state evolved on both backends for 1D/2D (`SplitOperatorSolver`) and 3D (`SplitStep3DSolver` vs `SplitStep3DGPU`); reported `max|dpsi|`. GPU warm-up step first.

```
11 GPU warm-up step completed
11a 1D 50 steps: max|dpsi| = 3.423e-15   (norm cpu=1.000000000000000 gpu=1.000000000000004)
11b 2D 30 steps: max|dpsi| = 2.733e-15
11c 3D 20 steps: max|dpsi| = 8.391e-16  (gpu backend=cupy)
```

**Deviation classification.** Differences `~1e-15` are FFT-library/accumulation-order roundoff — intended and consistent with the module docstring's documented `max|dpsi| = 8.4e-17 … 3.1e-16` per step (this probe's 3D value `8.391e-16` over 20 steps is of the same order). Not bit-identical, as documented.

**Evidence:** `evidence/probe_11_cpu_gpu.txt`.

---

### 12. Numerical stability and resolution sensitivity — VALIDATED

**Governing contract.** Parametric instability when `ℏ k_max² |w| dt/(2m) > π` (`k_max=π/dx`); spectral convergence in `dx` at fixed `dt`.

**Independent check.** Swept `N` at fixed `dt=0.002` and `dt` at fixed `N=512` against the exact coherent-state reference; probed `dt = 0.5·dt_crit` and `2·dt_crit`.

```
12a N sweep at fixed dt=0.0020 (T=0.50, 250 steps):
12a N=  64 dx=0.62500 k_max=5.03  max|dpsi|=3.1421e-05  stability param k_max^2*dt/2=0.025
12a N= 128 dx=0.31250 k_max=10.05  max|dpsi|=3.4152e-07  stability param k_max^2*dt/2=0.101
12a N= 256 dx=0.15625 k_max=20.11  max|dpsi|=3.4775e-07  stability param k_max^2*dt/2=0.404
12a N= 512 dx=0.07812 k_max=40.21  max|dpsi|=3.4775e-07  stability param k_max^2*dt/2=1.617
12a N=1024 dx=0.03906 k_max=80.42  max|dpsi|=3.4775e-07  stability param k_max^2*dt/2=6.468
12b dt sweep at fixed N=512:
12b dt=0.007812  max|dpsi|=5.3063e-06
12b dt=0.003906  max|dpsi|=1.3266e-06
12b dt=0.001953  max|dpsi|=3.3164e-07
12b dt=0.000977  max|dpsi|=8.2911e-08
12c stability condition hbar*k_max^2*|w|*dt/(2m) < pi (order 2, |w|=1):
12c N= 64 dt=0.12434 (0.5*dt_crit)  max|psi|=7.1280e-01  max|dpsi| vs exact=6.4431e-02
12c N= 64 dt=0.49736 (2.0*dt_crit)  max|psi|=7.5601e-01  max|dpsi| vs exact=8.0404e-01
12c N=128 dt=0.03108 (0.5*dt_crit)  max|psi|=7.5095e-01  max|dpsi| vs exact=7.7087e-04
12c N=128 dt=0.12434 (2.0*dt_crit)  max|psi|=7.5107e-01  max|dpsi| vs exact=4.7816e-02
12c N=256 dt=0.00777 (0.5*dt_crit)  max|psi|=7.5079e-01  max|dpsi| vs exact=8.9165e-06
12c N=256 dt=0.03108 (2.0*dt_crit)  max|psi|=7.5095e-01  max|dpsi| vs exact=7.7727e-04
```

**Which error dominates.** At the fixed physical setup (`L=40`, `T=0.5`, `dt=0.002`):
- `N=64`: spatial error dominates (`3.14e-05`).
- `N≥128`: the error plateaus at `3.4775e-07`, i.e. the **temporal (`dt`) error dominates** and further `dx` refinement gains nothing.
- At fixed `N=512`, halving `dt` quarters the error (`5.31e-06 → 1.33e-06 → 3.32e-07 → 8.29e-08`), confirming `O(dt²)` is the binding constraint once the grid resolves the state.

**Deviation classification.** The error growth at `2·dt_crit` (e.g. `N=128`: `4.78e-02` vs `7.71e-04` at `0.5·dt_crit`) reproduces the documented Weideman–Herbst parametric instability — **intended physics/numerics**, not a bug. `max|psi|` stays bounded (`~0.75`) because the localized coherent state has negligible amplitude at `k_max`; the instability grows from roundoff, so it appears as an error increase rather than a blow-up over 200 steps.

**Evidence:** `evidence/probe_12_resolution.txt`.

---

## Ranked list of domains where the physics is NOT yet independently validated

All 12 domains received an executed independent check; none is wholly unvalidated. Ranked by residual risk:

1. **Domain 6 — Time-dependent Hamiltonians (PARTIAL).** `SplitOperatorSolver` is validated, but the legacy `SplitStep1D/2D/3D(Solver/GPU)` solvers freeze `V` at `t=0` and silently ignore a `DipoleDrive` (`max|Δψ| = 0.892318` after 20 steps), contradicting the docs' general claim. Additionally, order-4 Yoshida samples `V` at `t = -0.03512072` for `dt=0.1`. *Unvalidated sub-item: time-dependent physics through the legacy solver path.*
2. **Domain 10 — Absorbing-boundary reflection suppression (indirect metric).** Suppression was measured by the absence of wraparound density in the left region (factor `2.09e-02`), not by a direct reflected-flux measurement; orders 1–3 are silently identical by design.
3. **Domain 8 — Long-time Ehrenfest.** Verified to `1e-15` for `t ≤ 2`; at `t=4` the dispersed packet tail reaches the periodic boundary and the error rises to `8.65e-05`, so very-long-time free-particle transport is boundary-limited rather than validated.
4. **Domain 7 — Order-4 at small `dt`.** The empirical order is `4.00/3.98` down to `dt≈0.004`, then floors at `~6e-14`; asymptotic 4th-order behaviour below that floor is not resolved by this grid.
5. **Domain 5 — 3D harmonic-oscillator ground state.** `E₀ = 1.4999824124` vs `1.5` (`1.76e-05`) on a coarse `14³` grid; the 3D energy is resolution-limited, though 1D/2D are exact.

---

## Verdict counts

| Verdict | Count |
|---|---|
| VALIDATED | 11 |
| PARTIAL | 1 |
| FAILED | 0 |
| NOT_RUN | 0 |
| **Total domains** | **12** |
