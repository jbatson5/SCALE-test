.. _7-0:

Material Specification and Cross Section Processing Overview
============================================================

*Introduction by M. L. Williams and B. T. Rearden*

**XSProc** (Cross Section Processing) provides material input and
multigroup (MG) cross section preparation for most SCALE sequences.
XSProc allows users to specify problem materials using easily remembered
and easily recognizable keywords associated with mixtures, elements,
nuclides, and fissile solutions provided in the SCALE **Standard
Composition Library**. For MG calculations, XSProc provides cross
section temperature correction and resonance self-shielding as well as
energy group collapse and spatial homogenization for systems that can be
represented in *celldata* input as infinite media, finite 1D systems, or
repeating structures of 1D systems, such as uniform arrays of fuel
units. Improved resonance self-shielding treatment for nonuniform
lattices can be achieved through the use of the **MCDancoff** (Monte
Carlo Dancoff) code that generates Dancoff factors for generalized 3D
geometries for subsequent use in XSProc. Cross sections are generated on
a microscopic and/or macroscopic basis as needed. Although XSProc is
most often used as part of an integrated sequence, it can be run without
subsequent calculations to generate problem-dependent MG data for use in
other tools.

This chapter provides detailed descriptions of the methods and modules
used for self-shielding. Self-shielding calculations are effectively a
problem-specific extension of the processing procedures used to create
the SCALE cross section libraries. SCALE includes continuous energy (CE)
and several MG (MG) cross section libraries described in the chapter on
SCALE Cross Section Libraries. The AMPX nuclear data processing
system :cite:`wiarda_ampx_2015` was used to convert evaluated data from ENDF/B into CE cross
sections, which were then averaged into problem-independent MG data at a
reference temperature of 300K, weighted with a generic energy spectrum
(see the SCALE Cross Section Libraries chapter). After being transformed
in probability distributions by AMPX, the CE data require no further
modifications for application to a specific problem except for possible
interpolation to the required temperatures. However, in MG calculations,
reaction rates depend strongly on the problem-specific energy
distribution of the flux, which implies that the problem-independent MG
data on the library should be modified into problem-dependent values
representative of the actual flux spectrum rather than the library
generic spectrum. The neutron energy spectrum is especially sensitive to
the concentrations and heterogeneous arrangement of resonance absorbers,
which may dramatically reduce the flux at the resonance peaks of a
nuclide, thus reducing its own reaction rate —a phenomenon known as
self-shielding. In general, the higher the concentration of a resonance
nuclide and the more the interaction between heterogeneous lumps (e.g.
fuel pins), the greater the degree of self-shielding for the nuclide.

Reference :cite:`williams_resonance_2011` gives a general description of the SCALE self-shielding
methods. The individual computational modules perform distinct functions
within the overall all self-shielding methodology of XSProc. More
theoretical details about individual computational modules are given in
:ref:`7-2` through :ref:`7-7`. XSProc provides capabilities for two different types
of self-shielding methods, which are summarized below.

**Bondarenko Method**

The Bondarenko approach :cite:`ilich_bondarenko_group_1964` uses MG cross sections pre-computed over a
range of self-shielding conditions, varying from negligibly (infinitely
dilute) to highly self-shielded. Based on the following
approximations :cite:`stammler_methods_1983` it can be shown that the degree of self-shielding in
both homogeneous and heterogeneous systems depends only on a single
parameter called the background cross section, “sigma0,” and on the
Doppler broadening temperature:

(a) neglect of resonance interference effects,

(b) intermediate resonance approximation, and

(c) equivalence theory.

During the SCALE MG library processing with AMPX, self-shielded cross
sections are computed using a CE flux calculated at several background
cross section values and temperatures. These are used to calculate
ratios of the shielded to unshielded cross sections, called “Bondarenko
factors” (a.k.a. shielding factors or f-factors). As described in the
SCALE Cross Section Libraries chapter, Bondarenko factors are tabulated
on the SCALE libraries as a function of sigma0 values and Doppler
temperatures for all energy groups of each nuclide.

Bondarenko factors are multiplicative correction factors that convert
the generic unshielded data into problem-dependent self-shielded values.
The BONAMI computational module performs self-shielding calculations
with the Bondarenko method by using the input concentrations and unit
cell geometry to calculate a sigma0 value for each nuclide and then
interpolating the appropriate MG shielding factors from the tabulated
library values.

**CENTRM/PMC Method**

Self-shielding calculations with BONAMI are fast and are always
performed for all SCALE MG sequences. However, due to the approximations
(a)–(c) listed in the previous section, a more rigorous method is also
provided which can replace the BONAMI results over a specified energy
range, usually encompassing the resolved resonance ranges of important
absorber nuclides. This approach is designated as the CENTRM/PMC method,
named after the two main computational modules, although several
additional modules are also used. CENTRM/PMC eliminates the main
approximations of the BONAMI approach by performing detailed neutron
transport calculations with a combination of MG and CE cross sections
for the actual problem-dependent compositions and unit cell
descriptions :cite:`williams_computation_1995`. This provides a problem-dependent pointwise (PW) flux
spectrum for averaging MG cross sections, which reflects resonance
cross-interference effects, an accurate slowing down treatment, and
geometry-specific transport calculations using several available
options. Shielded MG cross sections processed with CENTRM/PMC are
usually more accurate than BONAMI, so it is the default for most SCALE
MG sequences. However, depending on the selected transport option,
CENTRM/PMC may run considerably longer than BONAMI alone.

The CENTRM/PMC methodology first executes BONAMI, which provides
shielded cross sections outside the specified range of the PW flux
calculation. Then the computational module CRAWDAD reads CE cross
section files and bound thermal scatter kernels and interpolates the
data to the desired temperatures for CENTRM. Using a combination of
shielded MG data from BONAMI and CE data from CRAWDAD, CENTRM calculates
PW flux spectra by solving the deterministic neutron transport equation
for all unit cells described in the input. CENTRM calculations cover the
energy interval 10\ :sup:`-5` eV to 2 × 10\ :sup:`7` eV spanned by the
SCALE MG libraries. This energy range is subdivided into three sections:
(a) upper MG range: E>\ *demax*, (b) PW range: *demin*\ <E<*demax*, and
(c) lower MG range: E<\ *demin*, where *demin* and *demax* are the
boundaries of the PW range, which can be defined by user input. The
default values are *demin*\ =10\ :sup:`-3` eV and *demax=*\ 2 ×
10\ :sup:`4`. The values encompass the resolved resonance ranges of
essentially all actinide and fission product nuclides. MG transport
calculations are performed in the upper and lower ranges, which are
coupled to the PW transport calculation by the scattering sources.

Several methods are available for the CENTRM transport solutions within
each energy range, and the default methods can be changed through
parameters in the XSProc input. The discrete S\ :sub:`n` method is
default for homogeneous media and for arbitrary one dimensional (1D)
slab, spherical, and cylindrical geometries with general boundary
conditions. A unit cell model is used for self-shielding arrays of
spherical or cylindrical fuel regions. For the common case of a
square-pitch lattice with cylindrical fuel pins, the default transport
solver is the 2D method of characteristics (MoC). The CENTRM MoC
solution exactly models the outer rectangular cell surface using a
reflected boundary condition. CENTRM also has an option for discrete
S\ :sub:`n` calculations using a 1D Wigner-Seitz cell with a white outer
boundary condition. The 1D cell model is always used for spherical fuel
arrays (e.g., pebbles), and can also be selected as a faster alternative
than MoC for cylindrical fuel lattices. Finally, a two-region collision
probability method can be used for any type of array. The two-region
solver executes very fast but is usually more approximate than the MoC
and S\ :sub:`n` methods.

After CENTRM computes the average PW flux for each material zone, PMC
uses the spectra to process the CE cross sections into problem-specific
MG values for each material zone. A typical energy grid for the flux
solution consists of 50,000–90,000 points, providing good resolution of
the spectral fine-structure caused by resonance self-shielding. PMC has
several options for processing the MG data, such as correcting for
resonance absorption effects on the elastic removal. Shielded cross
sections from PMC may also be used to perform an optional MG eigenvalue
calculation with the XSDRNPM S\ :sub:`n` module for cell-averaging
and/or group collapsing of the MG values.

A variation of the standard CENTRM/PMC method is used to perform
self-shielding for doubly heterogeneous cells in which cylindrical or
spherical fuel elements, composed of small spherical fuel particles
dispersed in a moderator material, are distributed in an array
configuration. Self-shielding of this type of system requires multiple
CENTRM/PMC passes, effectively representing the two levels of
heterogeneity :cite:`goluoglu_modeling_2005`. First-level CENTRM calculations are performed for
each type of fuel particle using a spherical unit cell to represent the
array of multi-layered fuel particles distributed in the moderator
matrix. Space-dependent CE fluxes from these calculations are used in
the CHOPS module to compute CE disadvantage factors (fuel-average flux
divided by cell-average flux) for generating cell-averaged, CE
cross sections representative of the homogenized fuel compact. The
spatially averaged CE cross sections are used in a second-level CENTRM
transport calculation corresponding to a 1D unit cell model for the
array of fuel elements, with homogenized number densities for the fuel
compact. The CE flux spectrum from this calculation is used in PMC to
process the final MG, problem-dependent cross sections. This entire
procedure is transparent to the user and has been automated in XSProc.
Reference 2 provides more details about the SCALE treatment for doubly
heterogeneous fuel.

**Treatment of Non-Uniform Lattice Effects**

For self-shielding of lattice configurations, both the BONAMI and
CENTRM/PMC approaches assume that the fuel is arranged in an infinite,
uniform array of identical cells. For most pins in an actual lattice,
the uniform-array approximation is satisfactory; however, self-shielding
of some cells may be affected by boundary effects along the edge of the
array or by the presence of water holes or control rods. These effects
can be treated by incorporating a nonuniform Dancoff factor into the
self-shielding calculations for the affected cells. The SCALE module
MCDancoff performs a simplified one-group Monte Carlo calculation to
compute Dancoff factors for arbitrary absorber mixtures within a complex
(nonuniform) 3D array. The input for MCDancoff is described in
:ref:`7-7`. This module must be run as a standalone executable prior to the
self-shielding calculations for a given sequence, and the computed
Dancoff factors must be entered as XSProc input. The input Dancoff
factor is used directly in defining the background cross section for
BONAMI calculations. In the CENTRM/PMC methodology, the input Dancoff
factor is used in CENTRM to calculate a Dancoff-equivalent unit cell,
which defines a uniform lattice pitch that produces the same Dancoff
value as the nonuniform lattice. The CENTRM transport calculation then
proceeds as usual using 2D MoC or 1D S\ :sub:`n` for the unit cell.

.. bibliography:: bibs/MaterialSpecificationandCrossSectionProcessing.bib
