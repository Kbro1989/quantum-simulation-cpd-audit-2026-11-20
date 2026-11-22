"""Domain 5: Potential dimensionality and units.

Evaluates every potential class on 1D/2D/3D grids, checks shape/finiteness,
checks dimensionality guards, and checks unit consistency against analytic
values (including harmonic-oscillator and soft-Coulomb ground-state energies
from the stationary eigensolver).
"""
import numpy as np

from quantumlab.core.grid import Grid1D, Grid2D, Grid3D
from quantumlab.potentials import (
    GaussianBarrier, RectangularBarrier, PotentialStep, MultipleBarriers,
    ResonantTunnelingDiode, Gaussian2DBarrier, Gaussian3DBarrier,
    InfiniteSquareWell, FiniteSquareWell, DoubleWell, HarmonicOscillator,
    CrystalPotential, RandomDisorder, CustomPotential, HarmonicTrap,
    ApertureScreen, StadiumBilliard, SoftCoulomb,
    DipoleDrive, TimeDependentCustomPotential, sin2_envelope)
from quantumlab.stationary.eigensolver import eigenstates

print("=== Domain 5: Potential dimensionality and units ===")
g1 = Grid1D(64, -8.0, 8.0)
g2 = Grid2D(24, -6.0, 6.0, 24, -6.0, 6.0)
g3 = Grid3D(12, -5.0, 5.0, 12, -5.0, 5.0, 12, -5.0, 5.0)

cases = [
    ("GaussianBarrier", GaussianBarrier(2.0, 0.8, 0.5), (g1, g2, g3)),
    ("RectangularBarrier", RectangularBarrier(3.0, 1.2, 0.0), (g1, g2, g3)),
    ("PotentialStep", PotentialStep(1.5, 0.0), (g1, g2, g3)),
    ("MultipleBarriers", MultipleBarriers(2.0, 0.6, [-2.0, 0.0, 2.0]), (g1, g2, g3)),
    ("ResonantTunnelingDiode", ResonantTunnelingDiode(2.0, 0.5, 1.5, 0.0), (g1, g2, g3)),
    ("Gaussian2DBarrier", Gaussian2DBarrier(2.0, 0.8, 0.0, 0.0), (g2, g3)),
    ("Gaussian3DBarrier", Gaussian3DBarrier(2.0, 0.8, 0.0, 0.0, 0.0), (g3,)),
    ("InfiniteSquareWell", InfiniteSquareWell(4.0, 0.0), (g1, g2)),
    ("FiniteSquareWell", FiniteSquareWell(2.0, 4.0, 0.0), (g1, g2)),
    ("DoubleWell", DoubleWell(2.0, 2.0, 0.0), (g1, g2)),
    ("HarmonicOscillator", HarmonicOscillator(1.3, m=1.0, position=0.4), (g1, g2, g3)),
    ("CrystalPotential", CrystalPotential(1.5, 1.0, 0.0), (g1, g2)),
    ("RandomDisorder", RandomDisorder(1.0, 0.5, seed=3), (g1, g2)),
    ("CustomPotential", CustomPotential(lambda *c: sum(x ** 2 for x in c)), (g1, g2, g3)),
    ("HarmonicTrap", HarmonicTrap(1.3, m=1.0, center=(0.4,)), (g1,)),
    ("HarmonicTrap", HarmonicTrap((1.3, 0.9), m=1.0), (g2,)),
    ("HarmonicTrap", HarmonicTrap((1.3, 0.9, 0.7), m=1.0), (g3,)),
    ("ApertureScreen", ApertureScreen(50.0, 0.0, 0.6, 3.0, 1.0, 2), (g2, g3)),
    ("StadiumBilliard", StadiumBilliard(50.0, 2.0, 4.0), (g2,)),
    ("SoftCoulomb", SoftCoulomb(1.0, np.sqrt(2.0)), (g1, g2, g3)),
    ("DipoleDrive", DipoleDrive(None, 1.0, 2.0, axis='x'), (g1, g2, g3)),
    ("TimeDependentCustom", TimeDependentCustomPotential(lambda *c: c[-1]), (g1, g2, g3)),
]

for name, pot, grids in cases:
    for g in grids:
        try:
            V = pot.evaluate(g)
            ok = (np.shape(V) == g.shape and np.all(np.isfinite(V))
                  and np.all(np.isreal(V)))
            print("5a %-24s %s shape=%s finite/real/shape-ok=%s"
                  % (name, type(g).__name__, np.shape(V), ok))
        except Exception as exc:
            print("5a %-24s %s EXCEPTION %s: %s"
                  % (name, type(g).__name__, type(exc).__name__, exc))

# dimensionality guards
print("5b guards:")
for name, pot, grid in (("Gaussian2DBarrier->1D", Gaussian2DBarrier(1.0, 1.0), g1),
                        ("Gaussian3DBarrier->2D", Gaussian3DBarrier(1.0, 1.0), g2),
                        ("ApertureScreen->1D", ApertureScreen(1.0), g1),
                        ("StadiumBilliard->3D", StadiumBilliard(1.0, 1.0, 1.0), g3)):
    try:
        pot.evaluate(grid)
        print("5b %-24s NO ERROR (unexpected)" % name)
    except TypeError as exc:
        print("5b %-24s TypeError: %s" % (name, exc))

# unit consistency: analytic values
print("5c analytic values:")
V = HarmonicOscillator(omega=3.0, m=2.0).evaluate(g1)
print("5c HO m=2,w=3 at x=1.0: V = %.6f (expect 0.5*2*9*1 = 9)" % V[np.argmin(np.abs(g1.x - 1.0))])
V = GaussianBarrier(2.0, 0.8, 0.5).evaluate(g1)
i0 = np.argmin(np.abs(g1.x - 0.5))
ip = np.argmin(np.abs(g1.x - (0.5 + 0.8)))
x_act = g1.x[ip]
print("5c GaussianBarrier V(x0) = %.6f (expect 2)  V(x=%.3f) = %.6f (expect 2*exp(-((x-0.5)/0.8)^2) = %.6f)"
      % (V[i0], x_act, V[ip], 2.0 * np.exp(-((x_act - 0.5) / 0.8) ** 2)))
V = CrystalPotential(1.5, 1.0, 0.0).evaluate(g1)
i0 = np.argmin(np.abs(g1.x - 0.0))
ia = np.argmin(np.abs(g1.x - 1.0))
print("5c Crystal V(x=0) = %.6f  V(x=a=1) = %.6f (period a)" % (V[i0], V[ia]))
V = DoubleWell(2.0, 2.0, 0.0).evaluate(g1)
i0 = np.argmin(np.abs(g1.x - 0.0))
i1 = np.argmin(np.abs(g1.x - 2.0))
print("5c DoubleWell V(0) = %.6f (expect 2)  V(+-d=2) = %.6f (expect 0)"
      % (V[i0], V[i1]))
V = SoftCoulomb(1.0, np.sqrt(2.0)).evaluate(g1)
i0 = np.argmin(np.abs(g1.x))
print("5c SoftCoulomb V(0) = %.6f (expect -1/sqrt(2) = %.6f)"
      % (V[i0], -1.0 / np.sqrt(2.0)))
# HarmonicTrap scalar vs HarmonicOscillator
Vt = HarmonicTrap(1.3, m=1.0, center=(0.4,)).evaluate(g1)
Vo = HarmonicOscillator(1.3, m=1.0, position=0.4).evaluate(g1)
print("5c HarmonicTrap(scalar) vs HarmonicOscillator 1D max|diff| = %.3e"
      % np.max(np.abs(Vt - Vo)))
# RandomDisorder determinism and range
V1 = RandomDisorder(2.0, 0.5, seed=5).evaluate(g1)
V2 = RandomDisorder(2.0, 0.5, seed=5).evaluate(g1)
print("5c RandomDisorder same-seed identical = %s ; range [%.4f, %.4f] (expect [-1,1])"
      % (np.array_equal(V1, V2), V1.min(), V1.max()))
# DipoleDrive value at a zero of the force
dd = DipoleDrive(HarmonicOscillator(1.0, m=1.0), F0=2.0, omega=1.0, axis='x', phase=0.0)
Vb = dd.evaluate_at(g1, 0.0)
Vbase = dd.base.evaluate(g1)
print("5c DipoleDrive V(t=0) == V_base (sin0=0): max|diff| = %.3e"
      % np.max(np.abs(Vb - Vbase)))
dd2 = DipoleDrive(None, F0=2.0, omega=3.0, axis='x', phase=0.5,
                  envelope=sin2_envelope(2.0))
env025 = float(np.sin(np.pi * 0.25 / 2.0) ** 2)
print("5c DipoleDrive force(0.25) = %.6f (expect F0*env*sin(wt+phi) = %.6f)"
      % (dd2.force(0.25), 2.0 * env025 * np.sin(3.0 * 0.25 + 0.5)))

# ground-state energies from the eigensolver (unit consistency hbar/m/omega)
print("5d eigensolver ground-state energies:")
ge1 = Grid1D(256, -12.0, 12.0)
for omega, m in ((1.0, 1.0), (2.0, 1.0)):
    E, _ = eigenstates(ge1, HarmonicOscillator(omega, m=m), n_states=1, method='lanczos')
    print("5d 1D HO omega=%.1f m=%.1f  E0 = %.10f  (expect hbar*omega/2 = %.10f)"
          % (omega, m, E[0], 0.5 * omega))
E, _ = eigenstates(ge1, HarmonicOscillator(1.0, m=2.0), n_states=1, method='lanczos')
print("5d 1D HO omega=1 m_pot=2 (solver m=1) E0 = %.10f (mismatch -> 0.5*sqrt(2) = %.10f)"
      % (E[0], 0.5 * np.sqrt(2.0)))
E, _ = eigenstates(ge1, SoftCoulomb(1.0, np.sqrt(2.0)), n_states=1, method='lanczos')
print("5d 1D SoftCoulomb Z=1 a^2=2    E0 = %.10f  (expect -0.5)" % E[0])
ge2 = Grid2D(28, -8.0, 8.0, 28, -8.0, 8.0)
E, _ = eigenstates(ge2, HarmonicOscillator(1.0, m=1.0), n_states=1, method='lanczos')
print("5d 2D HO omega=1 m=1           E0 = %.10f  (expect hbar*omega = 1.0)" % E[0])
ge3 = Grid3D(14, -6.0, 6.0, 14, -6.0, 6.0, 14, -6.0, 6.0)
E, _ = eigenstates(ge3, HarmonicOscillator(1.0, m=1.0), n_states=1, method='lanczos')
print("5d 3D HO omega=1 m=1           E0 = %.10f  (expect 3*hbar*omega/2 = 1.5)" % E[0])
print("=== end Domain 5 ===")
