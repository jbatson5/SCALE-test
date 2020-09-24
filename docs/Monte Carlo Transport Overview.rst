.. _MCToverview:

Monte Carlo Transport Overview
==============================

*Introduction by B. T. Rearden*

SCALE Monte Carlo transport capabilities enable criticality safety,
shielding, depletion, and sensitivity and uncertainty analysis :cite:`rearden_monte_2014`.
SCALE provides separate Monte Carlo capabilities for eigenvalue
neutronics and fixed-source coupled neutron-gamma calculations, in the
KENO code :cite:`goluoglu_monte_2011` and fixed-source coupled neutron-gamma calculations in
the Monaco code :cite:`peplow_monte_2011` Although the eigenvalue and fixed-source
capabilities are provided in separate codes, many capabilities are
shared between them, including physics and geometry packages. The
foundational features shared between the codes are described below, with
specific implementations provided in subsequent sections. Generally, the
use of the Monte Carlo transport solvers in SCALE are best accessed
through the capability-specific sequences: CSAS and Sourcerer for
criticality safety, MAVRIC for shielding, TRITON for depletion,
TSUNAMI-3D for sensitivity and uncertainty analysis, and MCDancoff for
three-dimensional Dancoff factor calculations.

Multigroup Physics
------------------

The multigroup treatment implemented in SCALE has been in use since the
1960s and provides efficient, effective solutions with superior runtime
performance. Problem-dependent multigroup cross section data are
temperature interpolated and resonance self-shielded by other SCALE
modules before they are used in each Monte Carlo calculation. Without
proper resonance self-shielding, accurate multigroup calculations would
not be possible for thermal or intermediate energy spectrum systems.
After self-shielding has been accomplished and the two-dimensional
expansions have been summed into a Legendre expansion of the total
group-to-group transfer arrays, individual nuclide cross sections are
multiplied by their densities and summed into mixtures. These mixture
cross sections can then be used by the deterministic transport codes for
their calculations. The Monte Carlo codes convert the Legendre expansion
of the transfer arrays into probability distributions for the
group-to-group transfers and for the discrete scattering angles and
probabilities that preserve the moments of the Legendre expansion of
each group-to-group transfer. These transfer probabilities, angles, and
angle probabilities are then transformed so that the new group and angle
of scatter are efficiently selected through two random numbers with only
one multiplication and one addition operation. If the selected new group
is negative, it is reset to positive, and the new direction is chosen
isotropically. If the problem is run with P\ :sub:`1` scattering, the
scattering angle is chosen from a continuous distribution. For higher
order scattering, the polar scatter angle is discrete, and the azimuthal
angle is randomly selected from a uniform distribution. Multigroup
physics is implemented for neutron, photon, and neutron-photon coupled
particle transport modes.

Continuous-energy Physics
~~~~~~~~~~~~~~~~~~~~~~~~~

The continuous energy treatment in SCALE provides high resolution
solution strategies with explicit physics representation. The continuous
energy data represent thermal scattering using free gas and s(α,β), with
explicit point-to-point data provided through the thermal region. The
resolved resonance region is represented by pointwise data where the
energy point density is optimized for each reaction of each nuclide.
Data in the unresolved resonance region are represented by probability
tables, and data above the unresolved region implement pointwise data
with explicit point-to-point representation for secondary particles.
Photon yield data represent each discrete photon. Continuous energy
physics contains non-transport data handling to support various flux,
reaction rate, point detector tallies, and sensitivity analysis. In
addition, continuous energy data are converted from a double
differential data format to a lab format in a process where fast look-up
tables are provided during library generation. In SCALE 6.0–6.1,
calculations are performed only at temperatures available on the data
libraries by selecting the library temperature nearest to the desired
temperature for the calculation. Resonance upscattering techniques are
implemented via the Doppler Broadened Rejection Correction method :cite:`hart_implementation_2013`.
With SCALE 6.2, problem-dependent continuous energy cross sections at
the user specified temperature are generated at the beginning of the
calculation. Continuous energy physics is implemented for neutron,
photon, and neutron-photon coupled particle transport modes.

Geometry Packages
-----------------

Two variants of KENO provide identical solution capabilities with
different geometry packages. KENO V.a implements a simple and efficient
geometry package sufficient for modeling many systems of interest to
criticality safety and reactor physics analysts. KENO-VI implements the
SCALE Generalized Geometry Package (SGGP), which provides a
quadratic-based geometry system with much greater flexibility in
solution modeling. Monaco implements only the SGGP geometry package.
Both packages are based on solid bodies organized into reusable objects
called *units* that are constructed of material *regions*. Units can be
conveniently arranged in rectangular or hexagonal *arrays* of repeating
units. Additionally, nesting is available so that one unit can contain
another unit as a *hole*, or an array can be nested inside of a unit,
which itself can be repeated in another array. There is no limit to the
number of nesting levels available, so very complex systems can be
quickly generated.

KENO V.a models are constructed from regions of specific shapes
following strict rules which provide great efficiency in geometry
tracking. Allowed shapes are cubes, cuboids (rectangular
parallelepipeds), spheres, cylinders, hemispheres, and hemicylinders.
These shapes must be oriented along orthogonal axes, and they can be
translated, but they cannot be rotated. A major restriction applied to
KENO V.a geometry is that intersections are not allowed, and each region
of a unit must fully enclose the preceding region. An exception to this
rule is in the use of *holes* through which many units can be placed
within an enclosing unit. However, there is a runtime penalty in
geometry tracking for this flexibility, so this feature should be used
judiciously. KENO V.a provides *rectangular* arrays where the outer body
of each unit contained in the array must have a cuboidal shape, and
adjacent faces must have the same dimensions. The entire array must be
fully enclosed by the region in which it is placed.

SGGP is a quadratic-based geometry system that provides predefined
bodies including cone, cuboid, cylinder, dodecahedron, ecylinder
(elliptical cylinders), ellipsoid, hexprism, hopper (truncated pyramid),
parallelepiped, planes, rhombohedron, rhexprism (rotated hexprisms),
sphere, and wedge. Bodies not directly provided with SGGP can be
constructed from quadratic surfaces defined with coefficients entered by
the user. All bodies and surfaces can be rotated and translated to any
orientation and position within their respective unit. SGGP also
provides intersecting regions.

SGGP arrays may be composed of cuboids, hexprisms, rhexprisms, or
dodecahedrons. Like KENO V.a, the faces of adjacent units in an array
must have the same dimensions. An array boundary must be specified for
each array, and only the portion of the array within the boundary is
considered a part of the system. Also, the specified array must fill the
entire volume in the specified array boundary. The array boundary may be
any shape that can be specified using quadratic equations.

The use of holes is more flexible in SGGP than in KENO V.a. Within a
unit, holes cannot intersect other holes or the unit boundary, but they
can intersect region boundaries. The use of holes is not necessary to
build complex geometries; they are used primarily to more efficiently
build complex geometries and improve the tracking efficiency of the
simulation. In SGGP the distance to each surface in the unit must be
calculated after each collision. By moving some of the surfaces in a
unit into another unit that is included as a hole, all the surfaces in
the hole unit except the outer boundary are removed from the containing
unit. The judicious use of holes in SGGP can significantly speed up the
calculation.

Eigenvalue Analysis
-------------------

KENO performs eigenvalue calculations for neutron transport primarily to
calculate multiplication factors and flux distributions of fissile
systems in continuous energy and multigroup modes. Both codes allow
explicit geometric representation with their respective geometry
packages. KENO provides a multigroup adjoint capability which is
especially useful for sensitivity analysis. KENO implements standard
variance reduction techniques such as implicit capture, splitting, and
Russian roulette.

The initial fission source distribution in KENO can be specified with
nine options. These options include the default option of a uniform
distribution throughout the fissile material; an axially varying
distribution input by the user or defined as cos(Z) or
(1-cos(Z)):sup:`2`, where Z is the axial position; several options to
initialize the source at a given position (within a given volume, a
given unit, or a unit at a specified array index); or to specifically
provide the coordinates of each starting point.

KENO approximates the real *k­\ eff* variance using an iterative
approach and lagging covariance data between generations :cite:`ueki_error_1997`. KENO
provides a χ\ :sup:`2` test for the normality of *k­\ eff* and provides
plots of :math:`k_{eff}` by active and inactive generations. KENO reports a
*best estimate* of :math:`k_{eff}` that is computed as the minimum variance of
:math:`k_{eff}` based on generations skipped and generations run.

KENO provides track-length tallies for scalar flux and angular flux
moments needed for sensitivity analysis. Additionally, tallies are
provided for reaction rates, with isotopic tallies available only in CE
calculations. KENO also provides mesh tallies based on a user-input
orthogonal grid.

Matrix :math:`k_{eff}` calculations provide an additional method of calculating
the :math:`k_{eff}` of the system. Cofactor :math:`k_{eff}` and source vectors, which
describe the contribution to the system :math:`k_{eff}`\ from each unit, hole,
or array, are available.

KENO provides plots of *k­\ eff­*\ by generation and average :math:`k_{eff}`
for visual inspection of source convergence, followed by a *χ\ 2*
statistical assessment of convergence. Fission source convergence
diagnostic techniques are implemented in KENO to provide improved
confidence in the computed results and to reduce the simulation time for
some cases. Confirming the convergence of the fission source
distribution is especially useful to avoid the false convergence of
:math:`k_{eff}` that can be caused by insufficient sampling of important
portions of the system :cite:`ueki_stationarity_2005` KENO source convergence diagnostics rely on
Shannon entropy statistics of the mesh-based fission source data.

Parallel computation capabilities are available in both versions of KENO
to provide reductions in wall clock time, especially for sensitivity
analysis or Monte Carlo depletion on computer clusters. By introducing a
simple master-slave approach via message passing interface (MPI), KENO
runs different random walks concurrently on the replicated geometry
within the same generation. The fission source and other tallied
quantities are gathered at the end of each generation by the master
process, and then they are processed either for final edits or next
generations.

Shielding Analysis
------------------

Monaco is a fixed-source Monte Carlo shielding code that calculates
neutron and photon fluxes and response functions for specific geometry
regions, point detectors, and mesh tallies. Monaco has variance
reduction capabilities, such as source biasing and weight windows, which
can be automated via the MAVRIC sequence. MAVRIC performs radiation
transport on problems that are too challenging for standard, unbiased
Monte Carlo methods. Monaco provides multiple methods to enter the
radioactive source descriptions. Spatial distribution options include
volumetric sources and mesh sources which can be generated by other
codes such as KENO. Energy distributions can be entered by the user or
imported directly from emission data provided by ORIGEN. Spent fuel
analysis is simplified through direct coupling with the ORIGEN binary
concentration files.

.. bibliography:: bibs/MonteCarloTransport.bib
