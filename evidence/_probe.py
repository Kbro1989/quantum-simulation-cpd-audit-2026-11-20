"""Cheap read-only probes: shapes/dtypes/invariants. No GPU, no full suite."""
import numpy as np
import quantumlab
from quantumlab.core.grid import Grid1D, Grid2D, Grid3D
from quantumlab.core.wavefunction import WaveFunction1D, WaveFunction2D, WaveFunction3D
from quantumlab.core.absorbing_boundary import AbsorbingBoundaryLayer
from quantumlab.core import spectral
from quantumlab.potentials import SoftCoulomb, HarmonicTrap
from quantumlab import strongfield as sf

print("version", quantumlab.__version__)
g1 = Grid1D(8, -4.0, 4.0)
print("Grid1D x", g1.x.shape, g1.x.dtype, "k", g1.k.shape, g1.k.dtype, "dx", g1.dx, "dk", g1.dk, "L", g1.L)
g2 = Grid2D(4, -2.0, 2.0, 6, -3.0, 3.0)
print("Grid2D X", g2.X.shape, g2.X.dtype, "K_x", g2.K_x.shape, "dk_x", g2.dk_x, "dk_y", g2.dk_y)
g3 = Grid3D(4, -2.0, 2.0, 4, -2.0, 2.0, 4, -2.0, 2.0)
print("Grid3D X", g3.X.shape, "K_z", g3.K_z.shape, "dk_z", g3.dk_z)

for cls, g in ((WaveFunction1D, g1), (WaveFunction2D, g2), (WaveFunction3D, g3)):
    wf = cls(g)
    print(cls.__name__, "psi", wf.psi.shape, wf.psi.dtype, "pd", wf.probability_density.dtype,
          "norm", wf.norm(), "ft", wf.fourier_transform().shape, wf.fourier_transform().dtype)

wf = WaveFunction1D.gaussian(g1, 0.0, 1.0, 1.0)
print("gaussian norm", wf.norm(), "pd sum*dx", np.sum(wf.probability_density) * g1.dx)
ft = wf.fourier_transform()
print("Parseval 1D", np.sum(np.abs(ft) ** 2) * g1.dk, "vs", np.sum(wf.probability_density) * g1.dx)

for order in (1, 2, 3, 4, 5, 6):
    m = AbsorbingBoundaryLayer(g1, 1.0, order=order).mask
    print("ABL order", order, "finite", np.all(np.isfinite(m)), "min", float(m.min()), "max", float(m.max()))

print("k_volume_element exists:", hasattr(spectral, "k_volume_element"),
      "value g1:", spectral.k_volume_element(g1), "g2:", spectral.k_volume_element(g2))
print("volume_element", spectral.volume_element(g1), spectral.volume_element(g2), spectral.volume_element(g3))
print("ndim", spectral.ndim(g1), spectral.ndim(g2), spectral.ndim(g3))
print("wf_class", spectral.wavefunction_class(g1).__name__, spectral.wavefunction_class(g3).__name__)

b, r, e = sf.classical_returns(2000)
print("classical_returns max/Up", float(e.max()), "at birth deg", float(np.degrees(b[np.argmax(e)])))
print("wavelength_to_omega(800)", sf.wavelength_to_omega(800.0))
print("intensity_to_field(1e14)", sf.intensity_to_field(1e14))
print("ponderomotive", sf.ponderomotive_energy(sf.intensity_to_field(1e14), sf.wavelength_to_omega(800.0)))

sc = SoftCoulomb()
print("SoftCoulomb V(0) 2D", float(sc.evaluate(g2)[2, 3]), "grad shapes", [a.shape for a in sc.gradient(g2)])
