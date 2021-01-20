.. _7-5:

PMC: A Program to Produce Multigroup Cross Sections Using Pointwise Energy Spectra from CENTRM
==============================================================================================

*M. L. Williams, D. F. Hollenbach, U. Merteryuk*

ABSTRACT

PMC generates problem-dependent multigroup cross sections from an
existing multigroup cross-section library, a pointwise nuclear data
library, and a pointwise neutron flux file produced by the CENTRM
continuous-energy transport code. In the SCALE sequences, PMC is a
computational module called from XSProc to produce self-shielded
multigroup (MG) cross-sections over a specified energy range (e.g.,
resolved resonance range) of individual nuclides in the system of
interest. The self-shielded cross sections are obtained by integrating
the pointwise (PW) nuclear data using the CENTRM problem-specific,
continuous-energy flux as a weight function for each spatial mixture in
the system. Several options are available in PMC to specify various
types of weighting methods for the one-dimensional and two-dimensional
MG data. PMC outputs problem-dependent self-shielded cross sections that
can be used in XSDRNPM, KENO, NEWT or other MG transport codes.

ACKNOWLEDGMENTS

The authors acknowledge the suggestions and direct contributions of L.
M. Petrie of Oak Ridge National Laboratory, and former ORNL staff
N. M. Greene, and R. M. Westfall.

.. _7-5-1:

Introduction
------------

PMC is a computational module used for the CENTRM/PMC self-shielding
method performed by the XSProc driver module [see :ref:`7-1`].
It can also be run in standalone mode. PMC (**P**\ roduce
**M**\ ultigroup **C**\ ross sections) computes multigroup (MG)
cross sections by utilizing the pointwise (PW) neutron spectra
calculated in CENTRM :cite:`williams_computation_1995` to weight cross sections in a
continuous-energy (CE) library file. This provides problem-dependent,
self-shielded MG data representative of the fine-structure variation in
the neutron energy spectrum for the system of interest. PMC only
computes shielded cross sections within the energy interval of the
CENTRM PW flux calculation, defined by the energy limits DEMIN and
DEMAX. By default the lower limit is DEMIN=0.001 eV, and the upper
energy is DEMAX=20,000 eV; however these parameters can be modified by
the user in the CENTRM DATA input block. Outside of this energy
interval, the shielded cross sections previously computed with the
Bondarenko method in BONAMI are retained. PMC is automatically called
from the XSProc driver module during execution of a SCALE sequence, and
the resulting zone-averaged, problem-dependent cross sections can be
passed to MG transport solvers (e.g., KENO, NEWT, XSDRNPM, etc.) called
by the sequence.

.. _7-5-1-1:

Description of PMC input nuclear data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The nuclear data input to PMC consists of both MG and CE cross sections.
Input MG data are obtained from the MG library specified in the sequence
input. During SCALE execution, CE data used by both CENTRM and PMC are
prepared by the code CRAWDAD (:ref:`7-7`), which reads CE files for
individual nuclides, interpolates the data to the appropriate
temperatures for the specified mixtures, and concatenates the data into
a one problem-specific, multiple-nuclide CENTRM PW library. In general
each nuclide has its own unique energy mesh defined such that the cross
section at any energy value can be interpolated linearly from the
library point data to accuracy better than 0.1%. Although cross sections
in the original CE data files include values over the full energy range
of 0-20 MeV, CRAWDAD reduces the energy range to interval of the CENTRM
PW calculation (i.e., DEMIN→DEMAX). It is this combined PW library that
is accessed by PMC. The format of the CENTRM PW library is described in
:ref:`7-4`.

.. _7-5-1-2:

Description of PMC input pointwise flux data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the input nuclear data, PMC also requires PW flux values
calculated in CENTRM to be provided. Depending on the CENTRM transport
approximation, the flux data includes the PW scalar flux spectrum as a
function of energy and spatial-zone, and also may include PW spherical
harmonic moments of the angular flux (e.g., the current), which can be
used in processing MG scattering matrices for higher-order Legendre
moments. The non-uniform energy-mesh of the PW flux is determined during
the CENTRM calculation in order to represent the spectrum variation with
a minimum number of energy points. Like the CE cross section data, the
flux spectrum at any energy value can be obtained within a specified
tolerance by linear interpolation of the PW flux values.

.. _7-5-2:

Code Features
-------------

Two types of MG data are processed by PMC: 1-D cross sections and 2-D
scatter matrices. The 1-D cross sections are weighted-average values
over each energy group, by nuclide and reaction type. If there are “G”
energy groups on the input library, then the 1-D cross section for each
reaction type can be viewed as a 1-D vector with G values (of course
some may be zero). Depending on the options and PW energy range
specified, PMC will generally only re-compute and replace some of the
G-group data. The 2‑D cross sections correspond to group-to-group
transfers (and corresponding Legendre moments) associated with various
types of scatter reactions. These data can be arranged into a 2-D G by
G matrix. For most materials this matrix is quite sparse. The 2-D data
depend not only on the cross-section data, but also on the
energy/angular distributions of the secondary neutrons, which are
represented by Legendre moments. PMC always re-normalizes the 2-D
elastic and inelastic scattering matrices (including moments) to be
consistent with the respective self-shielded 1-D data. In the case of
elastic scattering, PMC also has rigorous options that can be used to
modify the secondary energy distribution to account for self-shielding
effects, such as by correcting the group removal cross section.

.. _7-5-2-1:

Options for treatment of 1-D cross sections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PMC computes new MG data for each reaction type (MT) and each nuclide on
the input MG library, which also has CE data on the CENTRM PW library.
Cross sections for reactions on the input MG library which do not have
corresponding PW reaction data are not replaced; i.e., the original MG
values are retained. SCALE CE library files for individual nuclides
contain all reaction types included in the ENDF/B data; however the
CRAWDAD module, executed prior to PMC, only includes certain ones when
it produces the problem-specific CENTRM library. By default the CENTRM
PW nuclear data library always includes cross sections for the total
(MT-1), radiative capture (MT-102), and elastic scattering reactions
(MT-2) of all nuclides; as well as fission (MT-18), and prompt, delayed,
and total-nubar values (MTs-456, 455, 452, respectively) for fissionable
nuclides. The (n,alpha) cross sections (MT-107) for B-10 and Li-6 are
also always included if these nuclides are present in a mixture. If the
CENTRM PW transport calculation includes the inelastic scattering
option, indicated by CENTRM input parameter nmf6 >= 0, the
discrete-level PW inelastic (MTs 50-90) and continuum inelastic (MT-91)
data are also included in the CENTRM PW library.

PW data for the unresolved resonance range are infinitely dilute on the
CENTRM library; therefore PMC does not use PW cross sections to compute
self-shielded data for the unresolved range. Instead, self-shielded
cross sections in the unresolved range are calculated using the
Bondarenko method in BONAMI prior to the CENTRM and PMC calculations.
This step is automatically performed by XSProc in the SCALE calculation
sequences.

PMC offers two methods to compute the total cross section. In the first
method the MG value for the total cross section (MT=1) is processed
directly from the PW MT-1 data on the CENTRM library. Total cross
sections are generally considered the most accurate type of evaluated
reaction data (due to measurement techniques); however if PW data for
MT-1 are processed as an independent cross section, there is no
guarantee that the sum of the partial cross sections will sum to the
total. These small imbalances in cross sections affect the neutron
balance, and may impact eigenvalue calculations. For this reason the PMC
default option does not compute the total cross section by weighting the
MT-1 PW data, but rather by summing the MG partial cross sections
(including the original MG data not re-processed in PMC).

The 1-D cross sections can be weighted using either the P\ :sub:`0`
(scalar flux) or P\ :sub:`1` (current) PW Legendre moment. In almost all
cases flux weighting is more desirable, since resonance reaction rates
are usually the dominant factor in the PW range. However,
current-weighting may be more accurate for certain problems where
spatial transport and leakage strongly influence the spectrum in the
resonance range, such as when the leakage spectrum is greatly impacted
by cross section interference minima such as occur in iron media. The
current-weighting option has been successfully applied for criticality
calculations involving mixtures of highly-enriched uranium and iron. An
alternative approach to using the current-weighted total cross section
is to include a Legendre expansion of the angular-flux-weighted total
cross section, which modifies the diagonal elements of the 2D elastic
scattering moments.\ :sup:`7` This option is specified by setting PMC
input parameter n2d=±2, as discussed in :ref:`7-5-2-4`.

.. _7-5-2-2:

Spatial averaging of 1D cross sections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PMC computes MG microscopic cross sections for each material mixture in
a given CENTRM calculation, using the spatially averaged PW spectrum
within the mixture. In SCALE this method is called “zone-weighting”, and
it is the default for PMC. Zone-weighted cross sections are generated
for every mixture zone in the unit cell. In configurations containing
fuel/absorber mixtures (e.g., lattices) in multiple unit cells,
CENTRM/PMC calculations may be performed for each mixture, resulting in
multiple mixture-weighted cross sections for the same nuclide ID. For
this reason, both the nuclide ID and a mixture number are generally
required to uniquely identify any specific cross section data generated
by PMC.

PMC also has an option to calculate “cell-weighted” (i.e., homogenized)
MG data, which applies disadvantage factors to preserve the
cell-averaged reaction rates for the entire unit cell. This is not
typically done, except for treating doubly-heterogeneous cells with
SCALE. In this case the PMC cell-weighting option is performed to
produce homogenized MG cross sections for the low level heterogeneity
(e.g., fuel grain in a fuel pebble). The XSProc control module
automatically sets the correct PMC weighing flag based on the type of
unit cell.

.. _7-5-2-3:

Energy ranges for multigroup weighting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The energy range of the MG and CE libraries in SCALE typically spans
10\ :sup:`−5` to 2*10\ :sup:`7` eV. In general this encompasses the (a)
thermal region where upscatter is treated, (b) resolved and unresolved
resonance ranges, and (c) high energy region above the resonance ranges.
The thermal range for the current SCALE libraries is defined to be below
5 eV. Energy limits for the resolved and unresolved resonance ranges are
defined by the individual ENDF/B evaluations for each nuclide, and these
limits are included in the CENTRM PW library.

As discussed in section 8.3, the CENTRM PW flux file contains values of
the zone-flux (and moments) per unit lethargy, calculated over the
entire energy range 10\ :sup:`−5` eV to 20 MeV; however, only the fluxes
in the energy range from DEMAX to DEMIN are computed from the PW
transport solution and exhibit the spectral fine-structure due to
resonance reactions. The flux outside interval [DEMAX, DEMIN] is
represented by the smoother “pseudo-pointwise” values obtained from
CENTRM’s MG solution. PMC provides two options to define the
nuclide-specific energy range for computing problem-dependent MG data:

Option (1). Compute MG cross sections of a given nuclide only over the
resolved resonance range of the nuclide. If the CENTRM PW calculation
does not encompass the entire resolved resonance range for the nuclide,
pseudo-point fluxes are be used in the self-shielding calculations for
some groups in the resolved regions. The pseudo-point fluxes are
generally a good representation for the gross spectrum shape, but do not
reflect fine-structure effects caused by resonance absorption; therefore
with this option, the user should take care that the CENTRM PW limits
are appropriate for the resonance nuclides of interest.

Option (2). Compute MG cross sections for a given nuclide over the
entire energy range for which PW flux values are calculated in the
CENTRM. In this case PMC computes MG cross sections only over the
portion of the PW data that is contained within the PW flux range; i.e.,
the pseudo PW spectrum is not used to process any data. Shielded cross
sections for groups not included in the PW calculation are based on the
BONAMI self-shielding method.

Option (2) above is default in PMC. SCALE-6.2 has DEMIN and DEMAX
default values of 0.001 eV and 20 keV. This is sufficient for resonance
self-shielding of essentially all actinide and important fission product
nuclides; but some structural materials such as iron have resonances
above 20 keV which would be shielded by BONAMI (:ref:`7-3`).

.. _7-5-2-4:

Options for treatment of 2-D cross sections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The input parameter N2D defines five PMC options for processing
problem-dependent, 2-D elastic scattering matrices. The first approach,
N2D=0, simply multiplies the elastic scattering matrices by the ratio of
the new to old 1-D elastic cross sections for the specified reaction
process, where the “old” data are the 1-D values in the original MG
library, and the “new” data are the problem-dependent MG cross sections
processed using the PW flux as described above. The P\ :sub:`ℓ` Legendre
moments as well as the P\ :sub:`0` matrix are scaled by the same ratio
for a given group. This method is also always used for discrete-level
and continuum inelastic cross sections, as well as any other 2-D data
other than elastic. The basic assumption is that the relative
group-to-group scattering distribution does not change from the
distribution in the original MG library, which is processed with an
infinitely dilute spectrum— i.e., self-shielding only affects the total
scatter rate. This approach gives good results for many applications,
and is very efficient computationally. However, for intermediate and
high mass materials, the elastic removal rate from a group may be
sensitive to the problem-dependent CE spectrum. In these cases the
scaling approximation may not give the correct elastic removal rate from
the group, because the within-group elastic cross section will be in
error. In these cases the alternate approaches described below can be
used.

The option N2D= −1 corrects for the impact of resonance self-shielding
on the elastic removal from an energy group. This option recomputes a
new value for the within-group cross section by applying a correction
factor based on the ratio of shielded versus unshielded removal
probabilities for *s*-wave scatter (isotropic center-of-mass scatter).
The P\ :sub:`0` out-scattering cross sections are then renormalized to
give the correct 1D shielded cross section for the group. This approach
provides a reasonable and computationally efficient approximation to
process 2D elastic matrices in the resolved resonance range of actinide
nuclides. However the assumption of s-wave scatter may not be valid in
the resolved resonance range of a structural material such as iron;
therefore users should beware when applying the approximation if the PW
range is extended above 50 keV, for systems with large sensitivity to
structural materials.

Option N2D=1 uses the CENTRM PW flux to recompute the entire set of
group-to-group scatter data (including Legendre moments) using PW thermal scattering kernel data for the thermal energy range and
assuming
*s*-wave kinematics for the epithermal energy range.
Since the CENTRM PW flux is used as the weighting
function, this approach is sometimes more accurate for groups with large
spectral gradients as discussed above. As with the N2D=-1 option, the
main limitation is the *s*-wave scattering approximation for the
secondary energy distribution. This option requires more computation
time than the N2D methods discussed previously, and usually gives
similar results as N2D=-1.

A rigorous derivation of the MG transport equation from the CE equation results
in a directionally dependent total cross section. PMC option N2D=2 uses the
method in :cite:`bell_nuclear_1970` to address this effect by modifying the
Legendre moments of the 2D elastic matrix. For cross section moment “n”, the
diagonal term (i.e., within-group scatter) is modified by adding a term equal to
the difference in the MG total cross section weighted with the PW scalar flux
and the MG total cross section weighted with the n\ :sub:`th` Legendre moment of
the PW flux. When using MoC (NPXS=6), since default ISCT is 0, there are no Pn
flux moments on CENTRM PW flux file. Therefore, no diagonal P\ :sub:`n` correction will
be applied to cross section moments.

Option N2D=-2 is essentially a combination of options N2D=2 and N2D=-1.
This option applies the elastic removal correction to the diagonal term
of the P\ :sub:`0` moment of the elastic 2D matrix, and applies the PL
correction described above to the diagonal term of the PL Legendre
moment of the elastic matrix.

The thermal energy range presents a particularly difficult challenge for
processing problem-dependent 2‑D scattering data, due to the complicated
kinematics associated with molecular motion, chemical binding, and
coherent scattering effects. PMC currently uses the scaling approximation
(N2D=0 option) for the thermal energy range with any input
value of N2D except for N2D=1.

.. _7-5-3:

Calculation of Problem-Dependent Multigroup Cross Sections
----------------------------------------------------------

.. _7-5-3-1:

1-D cross sections
~~~~~~~~~~~~~~~~~~

.. math::
  :label: eq7-5-1

  \sigma_{z, r, g}^{j}=\frac{\int_{\Delta E_{g}} \sigma_{z, r}^{j}(E) \Phi_{z}(E) d E}{\int_{\Delta E_{g}} \Phi_{z}(E) d E}=\frac{\int_{\Delta E_{g}} \sigma_{z, r}^{j}(E) \Phi_{z}(E) d E}{\Phi_{z, g}}

where

  Φ\ :sub:`z,g` is the multigroup zone flux,

  σ\ :sup:`j`\ :sub:`z,r,g` is the zone-average, group cross section, and

  ∆E\ :sub:`g` is the energy interval of group g.

The integration in :eq:`eq7-5-1` is performed by summing over a discrete energy
mesh within the group boundaries. Since the CE cross section and the PW
flux generally have different energy grids, the integration mesh for the
numerator is formed by taking the union of the two. The CE
cross sections and the PW flux are mapped onto the union mesh, and the
integral is evaluated using the trapezoidal method. :eq:`eq7-5-1` is used to
compute weighted group data for all MT’s for which CE data are available
on the CENTRM library, except in the case of the fission neutron yield
ν. Instead of using the PW scalar flux as the weighting function, the MG
value for ν is weighted by the product of the PW flux and the PW fission
cross section for the material.

.. _7-5-3-2:

2-D scattering cross sections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The 2-D MG cross section moments are defined as the weighted
group-average of terms appearing in a Legendre (PL) expansion of the CE
double-differential scatter cross section, which describes the transfer
of neutrons from one energy to another, for a given angle of scatter.
The PL Legendre moments on the original MG library are fully consistent
with the ENDF/B kinematic specifications. Thus the specified anisotropy
in elastic or inelastic data in the center-of-mass (CM) system is
reflected in the PL scattering matrices; however the library MG data are
processed with an infinitely dilute flux spectrum. PMC provides several
options for modifying these data to correct for problem-specific
spectral effects, such as self-shielding. First, consider the scaling
method (N2D=0) in which all the elements of the original scatter matrix
(i.e., on the input Master library) for a given initial group are
multiplied by the ratio of 1-D scatter cross sections. This has the
effect of normalizing the original scatter matrix to the
problem-dependent value calculated for the 1-D scatter data. In this
case the l\ :sub:`th` Legendre moment of the 2-D multigroup
cross section for reaction type “s” of nuclide “j” in zone “z” (at a
specified temperature), for scatter from initial group g′ to final
group g, is computed by:

.. math::
  :label: eq7-5-2

  \sigma_{l, z, s, g^{\prime} \rightarrow g}^{j}=\frac{\left(\sigma_{z, s, g^{\prime}}^{j}\right)_{n e w}}{\left(\sigma_{s, g^{\prime}}^{j}\right)_{o r i g}} \times\left(\sigma_{l, s, g^{\prime} \rightarrow g}^{j}\right)_{o r i g}

where the subscripts “\ *orig*\ ” and “\ *new,*\ ” respectively, refer
to the original MG data on the Master library, and the new
problem-dependent data computed by PMC. The types of reactions for which
problem-dependent 2-D cross sections may be processed using the scaling
method are elastic (MT=2), discrete-level inelastic (MT’s 50–89),
continuum inelastic (MT=90), and (n,2n) (MT=16). This approach is also
applied to obtain problem-dependent thermal scatter matrices, which
contain upscatter as well as down-scatter reactions. The CENTRM nuclear
data libraries include PW cross sections for incoherent (MT=1007) and
coherent (MT=1008, if available) thermal scattering reactions, which can
be processed into 1-D MG data by PMC in the same manner as other
reaction types. The 1-D weighted thermal scattering data are then used
to normalize the 2-D thermal matrices on the input Master library. For
materials with both coherent and incoherent thermal scatter data, each
matrix is scaled by the corresponding type of 1-D data. The coherent
scattering matrix only contains within-group terms.

The option N2D= −1 recomputes the P\ :sub:`0` within-group elastic
cross section based on the assumption of s-wave scatter kinematics, and
scales the other terms of the original P0 elastic matrix by the modified
removal rate. This procedure approximately corrects for effects of
resonance self-shielding on the group removal probability, without
having to recompute the entire matrix assuming *s*-wave scatter, as done
for N2D=1. Suppressing the zone index for simplicity, the P\ :sub:`0`
within-group XS is defined as:

.. math::
  :label: eq7-5-3

  \sigma_{\mathrm{g}, \mathrm{g}} \equiv \frac{\int_{\mathrm{g}} \sigma_{\mathrm{s}}(\mathrm{E})\left[1-\mathrm{p}_{\mathrm{r}}(\mathrm{E})\right] \Phi(\mathrm{E}) \mathrm{d} \mathrm{E}}{\int_{\mathrm{g}} \Phi(\mathrm{E}) \mathrm{d} \mathrm{E}}

where p\ :sub:`r`\ (E) is the probability that a neutron at energy E,
within group g, will scatter to an energy below the lower boundary of
the group. For *s*-wave scattering this equation becomes,

.. math::
  :label: eq7-5-4

  \sigma_{\text{g,g}} = \frac{\int^{\text{min}\left(\text{E}_{\text{Hi}}, \frac{\text{E}_{\text{Lo}}}{\alpha}\right)}_{\text{E}_{\text{Lo}}} \sigma_{\text{s}}(\text{E})\left[\frac{\text{E}-\text{E}_{\text{L}}}{\text{E}(1-\alpha)}\right] \Phi(\text{E})\text{dE}}{\int_{\text{g}}\Phi(\text{E})\text{dE}}


The N2D= −1 option recomputes a modified P\ :sub:`0` within-group
cross section from the expression,

.. math::
  :label: eq7-5-5

  \left(\sigma_{\mathrm{g}, \mathrm{g}}\right)_{\text {new}}=\frac{\widetilde{\sigma}_{\mathrm{g}, \mathrm{g}}^{(\varphi)}}{\widetilde{\sigma}_{\mathrm{g}, \mathrm{g}}^{\infty}}\left(\sigma_{\mathrm{g}, \mathrm{g}}\right)_{\text {orig}}

where

  (σ\ :sub:`g,g`)\ :sub:`orig` is the original within-group
  cross section on the MG library, based on actual kinematics and weighted
  with an infinitely dilute spectrum;

  :math:`\widetilde{\sigma}_{\mathrm{g}, \mathrm{g}}^{(\infty)}` is the infinitely dilute within-group cross section based on
  s-wave kinematics, which is computed from :eq:`eq7-5-4`  using an infinitely
  dilute spectrum

  :math:`\widetilde{\sigma}_{\mathrm{g}, \mathrm{g}}^{(\varphi)}` is the self-shielded within-group based on s-wave kinematics,
  computed from :eq:`eq7-5-4` using Φ(E) →CENTRM PW flux.

If the effects of resonance self-shielding are small, then there will be
little change in the original within-group value, since in this case
:math:`\widetilde{\sigma}_{\mathrm{g}, \mathrm{g}}^{(\varphi)} \sim \widetilde{\mathrm{O}}_{\mathrm{g}, \mathrm{g}}^{(\infty)}`.

The P\ :sub:`0` group-to-group out-scatter terms for N2D=-1 are scaled
as follows:

.. math::
  :label: eq7-5-6

  \sigma_{g \rightarrow g^{\prime}}=\frac{\left(\sigma_{\mathrm{s}, \mathrm{g}}\right)_{\mathrm{new}}-\widetilde{\sigma}_{\mathrm{g}, \mathrm{g}}^{(\varphi)}}{\left(\sigma_{\mathrm{s}, \mathrm{g}}^{\infty}\right)_{\mathrm{new}}-\widetilde{\sigma}_{\mathrm{g}, \mathrm{g}}^{\infty}} \times\left(\sigma_{\mathrm{g} \rightarrow \mathrm{g}^{\prime}}\right)_{\mathrm{orig}}

Again if there is little self-shielding, the change in off-diagonal
matrix elements is small, so that the original secondary energy
distribution is preserved. Finally the entire modified P\ :sub:`0`
scatter matrix is renormalized to correspond to the self-shielded 1-D
scatter cross section.

For the option N2D=1, an entirely new PL elastic scattering matrix is
computed. The l\ :sub:`th` Legendre moment of the 2-D MG elastic
cross section of nuclide “j” in zone “z” (at a specified temperature),
for scattering from initial group g′ to final group g is rigorously
defined as, :cite:`bell_nuclear_1970`

.. math::
  :label: eq7-5-7

  \sigma_{l, g^{\prime} \rightarrow g}^{j}=\frac{\int_{\Delta E_{g}} \int_{\Delta E_{g^{\prime}}} \sigma_{l}^{j}\left(E^{\prime} \rightarrow E\right) \Phi_{l, z}\left(E^{\prime}\right) d E^{\prime} d E}{\int_{\Delta E_{g^{\prime}}} \Phi_{l, z}\left(E^{\prime}\right) d E^{\prime}}=\frac{\int_{\Delta E_{g}} \int_{\Delta E_{g^{\prime}}} \sigma^{j}\left(E^{\prime}\right) f_{l}^{j}\left(E^{\prime} \rightarrow E\right) \Phi_{l, z}\left(E^{\prime}\right) d E^{\prime} d E}{\int_{\Delta E_{g^{\prime}}} \Phi_{l, z}\left(E^{\prime}\right) d E^{\prime}}

where σ\ :sub:`z`\ (E) is the CE elastic cross-section data from the
CENTRM nuclear data file, evaluated at the appropriate temperature for
zone z;\ :math:`f_{l}^{j}` (E′→E) is the secondary neutron energy distribution
from elastic scattering; and Φ\ :sub:`l,z`\ (E) is the lth PW flux
moment averaged over zone Z. PMC assumes *s*-wave scattering from
stationary nuclei to evaluate the scattering distribution, and uses the
P\ :sub:`0` flux moment (i.e., scalar flux) as for the weighting
function for all PL matrices; therefore the expression evaluated by PMC
for N2D=1 is:

.. math::
  :label: eq7-5-8

  \sigma_{l, z, g^{\prime} \rightarrow g}^{j}=\frac{\int_{g^{\prime}} \int_{g} \frac{\sigma_{z}^{j}(\mathrm{E}) \Phi_{z}\left(E^{\prime}\right) P_{l}\left(G^{j}\right)}{\left(1-\alpha^{j}\right) E^{\prime}} d E^{\prime} d E}{\int_{g} \Phi_{z}\left(E^{\prime}\right) d E^{\prime}}

here P\ *l* is the *l*\ :sub:`th` order Legendre polynomial; and
G\ :sup:`j` is the kinematics relation expressing the cosine of the
scattering angle as a function of E and E’, for elastic scattering from
nuclear mass A\ :sup:`j`. The kinematics function for nuclide j is
defined as,

.. math::
  :label: eq7-5-9

  \mathrm{G}^{\mathrm{j}}\left(\mathrm{E}^{\prime}, \mathrm{E}\right)=\frac{\mathrm{A}^{\mathrm{j}}+1}{2} \sqrt{\frac{\mathrm{E}}{\mathrm{E}^{\prime}}}-\frac{\mathrm{A}^{\mathrm{j}}-1}{2} \sqrt{\frac{\mathrm{E}^{\prime}}{\mathrm{E}}} ,

where G\ :sup:`j`\ (E′,E) is equal to the cosine of the angle of scatter
between the initial and final directions. The integral over the final
group (g) is evaluated analytically using routines developed by
J. A. Bucholz :cite:`bucholz_method_1978`. Integration over the initial group (g′) is then
performed numerically using the same method as for evaluating the
problem-dependent 1-D cross sections.

Option N2D=2 adds the following term to the diagonal of the *l*\ :sub:`th`
moment of the PL elastic scatter matrix,

.. math::
  :label: eq7-5-10

  \left(\sigma_{l ; g, g}^{j}\right)_{n e w}=\left(\sigma_{l ; g, g}^{j}\right)_{o r i g}+\sigma_{t ; g}^{j}-\sigma_{t, l ; g}^{j} ; \quad 0<l<i s c t

where isct is the order of scatter specified in CENTRM calculation [see :ref:`7-4`]; :math:`\sigma_{t ; g}^{j}`
is the standard 1D total cross section weighted with the
scalar flux, and :math:`\sigma_{t, l ; g}^{j}` is the total cross section weighted with the *l*\ :sub:`th`
Legendre moment of the angular flux; i.e.,

.. math::
  :label: eq7-5-11

  \sigma_{t, l ; g}^{j}=\frac{\int_{g} \sigma_{t}^{j}(E) \Phi_{l}(E) d E}{\int_{g} \Phi_{l}(E) d E}

.. _7-5-3-3:

Problem-dependent fission spectra
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fission spectra (chi) describing the energy distribution of secondary
neutrons produced by fission depend upon the energy of the neutron
causing the fission, thus the MG chi data should be a 2-D matrix,
χ\ :sub:`g→g′`. However, neutron transport codes in SCALE expect a 1-D
distribution, χ\ :sub:`g′`; therefore the production of fission neutrons
in group g′ by neutrons in group g is approximated as,

.. math::
  :label: eq7-5-12

  \mathrm{P}_{\mathrm{g} \rightarrow \mathrm{g}^{\prime}}=\chi_{\mathrm{g}^{\prime}} \cdot \mathrm{v}_{\mathrm{g}} \sigma_{\mathrm{f}, \mathrm{g}} \Phi_{\mathrm{g}}

and the total number of secondary neutrons generated in group g’ is,

.. math::
  :label: eq7-5-13

  \mathrm{P}_{\mathrm{g}^{\prime}}=\chi_{\mathrm{g}^{\prime}} \sum_{\mathrm{g}} v_{\mathrm{g}} \sigma_{\mathrm{f}, \mathrm{g}} \Phi_{\mathrm{g}}

SCALE MG libraries contain “generic” 1-D chi distributions for each
fissionable nuclide. These are processed from the evaluated ENDF/B
fission data, weighted by the standard weighting function used to
process the SCALE MG libraries (i.e., Maxwellian in thermal energy
range, 1/E in epithermal range, fission spectrum in fast range). The
SCALE MG libraries also contain 2-D chi distributions processed from
ENDF/B fission data, can be processed with a problem-dependent weighting
function to create a more representative 1-D chi. This procedure is done
in PMC for each fissionable nuclide, using the following equation that
preserves the secondary neutron energy distribution:

.. math::
  :label: eq7-5-14

  \chi_{\mathrm{g}^{\prime}}=\frac{\sum_{\mathrm{g}} \chi_{\mathrm{g} \rightarrow \mathrm{g}^{\prime}} v_{\mathrm{g}} \sigma_{\mathrm{f}, \mathrm{g}} \Phi_{\mathrm{g}}}{\sum_{\mathrm{g}} v_{\mathrm{g}} \sigma_{\mathrm{f}, \mathrm{g}} \Phi_{\mathrm{g}}}

In the above equation, :math:`v_{\mathrm{g}}, \sigma_{\mathrm{f}, \mathrm{g}}, \text { and } \Phi_{\mathrm{g}}` are
problem-dependent 1-D data computed by PMC using the PW fluxes
calculated by CENTRM, and :math:`\chi_{\mathrm{g} \rightarrow \mathrm{g}^{\prime}}`, are the 2-D MG fission spectra data
on the AMPX multigroup Master library. The 1D prompt chi computed by PMC
includes all fission components (first-chance-fission,
second-chance-fission, etc) given in the ENDF/B files, weighted by the
relative fission-source fraction associated with each channel. PMC also
computes an effective delayed neutron fission spectra, and this is
combined with the prompt chi, using the appropriate delayed neutron
fraction, to obtain the final 1-D fission spectra. The 1-D chi computed
by PMC replaces the generic 1-D values for MT-1018 that were originally
in the Master library.

.. _7-5-3-4:

Definition of background cross sections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The value of the “background cross section (σ\ :sub:`0`)” may be used in
PMC to determine which materials are considered to be infinitely dilute,
in which case no cross section processing is done for the material. No
processing is performed for material “j” if its background cross section
exceeds the value of input parameter *XS_dilute* ; i.e., if :math:`\sigma_{0}^{(\mathrm{j})}` >
XS_dilute. The expression used in PMC to compute the background cross
section :math:`\sigma_{0}^{(\mathrm{j})}` is given in the BONAMI section.

.. _7-5-4:

PMC Input Data
--------------

The Fido input blocks shown in this section are only required when
executing PMC as a standalone module. In the more typical case where PMC
is executed through the XSProc module during a SCALE sequence
calculation, the default parameter values are automatically defined
within XSProc. Default values for XSProc execution can be overridden
using keyword input in the CENTRM DATA block (see :ref:`7-4-4`). The
keyword input names correspond to the variable names given in this
section.

.. centered:: **DATA BLOCK 1**

**0$$ LOGICAL UNIT ASSIGNMENTS** (8 entries. Default values given in
parenthesis)\*

1. LIBM = Input AMPX Master nuclear data library (22)

2. LIBX = Input CENTRM pointwise nuclear data library (90)

3. LIBF = Pointwise flux file produced by CENTRM (91)

4. LIBNM = Output problem-dependent Master library created by PMC (92)

5. LIBSC = Scratch unit (18)

6. LIBSX = Scratch unit (24)

*(*) Parameters in the 0$$ array cannot be modified for XSProc
execution.*


**1$$ INTEGER PARAMETERS** (10 entries )

1. MRANGE

    = 0, obsolete option

    = 1, Compute new group cross sections over resolved resonance range of
    pointwise nuclides [from EUPR to ELOR given in CENTRM data library]

    = 2, Compute new group cross sections over pointwise flux range [from
    DEMAX to DEMIN in CENTRM flux calculation] (2).

2. N2D

    = -2, Apply removal correction to P0 elastic scatter matrix AND
    apply consistent PN correction to higher order Legendre components;
    normalize to 1D.

    −1, Apply elastic removal correction to P0 elastic scatter matrix;
    normalize to 1D.

    = 0, Normalize P\ :sub:`N` components of original elastic scattering
    matrix to new 1-D elastic value.

    = 1, Compute new P\ :sub:`N` components of elastic matrix, using scalar
    flux as weighting function.

    = 2, Modify diagonal elements of the PN moments of the elastic matrix
    using the consistent PN method (-1).

3. NTHRM

    = 0 Treatment of thermal scatter kernels [not functional] (0)

4. NPRT

    = −1, Minimum printed output;

    = 0, Standard print out;

    = 1, Also print new weighted cross sections for MT’s 1, 2, 18, and 102.

    = 2, Maximum amount of printed output includes 2D matrices (−1).

5. NWT

    = 0, Generate zone-weighted multigroup data;

    = 1, Generate cell-weighted multigroup data (0).

6. MTT

    = 0, Process all MT’s included in LIBX. [**NOTE:** With this
    option, total cross section may not equal to sum of partials];

    = 1, Process all MT’s except 1, 27, 101; then compute:

      MT 101 = sum of MT’s 102-114,

      MT 27 = sum of MT’s 18 and 101,

      MT 1 = sum of MT’s 2, 4, 16, 17, and 27 (1).

7. PMC_OMIT

    = 0, Process all pointwise nuclides used in CENTRM
    calculation;

    = 1, Process only nuclides in fuel zones.

    > 1, Process all materials except those in 2$$ array

8. IXTR2

    = 0, PMC run in CSAS standard sequence;

    = 1, PMC run in stand-alone mode (1);

    = 2 PMC run in CSAS double-heterogeneous cell sequence

9. IXTR3

    = −1, Process new data for all Legendre components on the input
    AMPX master library up to P\ :sub:`7`.

    = N, Process new data through P\ :sub:`N` moments. [N=Scattering
    Order+1] (−1).

10. N1D

    = 0 Use CENTRM scalar flux for weighting function;

    = 1, Use the absolute value of CENTRM current for weighting function
    (0).

*1*\* REAL PARAMETERS** (10 entries)

1. XS_DILUTE = background cross section (barns) considered to be
infinitely dilute (10\ :sup:`10`)

2-10. Fill with 0.0

              **T [ TERMINATE DATA BLOCK 1 ]**

.. centered:: DATA BLOCK 2 :  INDIVIDUAL NUCLIDES OMITTED FROM PROCESSING

.. note:: This data cannot be entered for XSProc execution.

**2$$ ISOTOPE IDENTIFIERS** (PMC_OMIT entries). Only enter PMC_OMIT > 1

[IDs of nuclides to be omitted from pointwise processing]

              **T [TERMINATE DATA BLOCK**


                **END OF PMC INPUT DATA**

.. _7-5-4-1:

Notes for PMC users
~~~~~~~~~~~~~~~~~~~

1. N2D specifies the method used to process the P\ :sub:`N` components
of the 2-D elastic scattering matrices. In the option N2D=0, the
P\ :sub:`N` components of the original elastic scattering matrix are
simply re‑normalized using the new, problem-dependent 1-D elastic
values. This simple scaling approach often works well, but it does not
account for the impact of resonance self-shielding on the group removal
probability. The default option N2D= −1 approximately corrects the P0
elastic matrix for removal self-shielding effects on and is usually
preferred to N2D=0, except for fast systems. Option N2D=1 re-computes
all the P\ :sub:`N` components of 2-D elastic cross sections using the
scalar flux as a weighting function, along with the the use of PW
thermal scattering kernel data and  assumption of
*s*-wave scattering within the epithermal  PW energy range. This approach takes
significantly more execution time than N2D=-1, and usually is not
necessary. Option N2D=2 corrects the diagonal terms of the Legendre
moments, using the consistent PN expression. Option N2D=-2 is similar to
N2D=2, except the elastic removal correction is applied to the P0 moment
(Like for N2D=-1). Option N2D=-2 has been found to improve results for
many infinite lattice cases.

2. NWT specifies whether the new multigroup cross sections are
zone-weighted or cell-weighted. When PMC is executed through XSProc,
nuclides are always zone-weighted unless the double-heterogeneous option
is specified in the CELLDATA block of the sequence input. Except for
double-heterogeneous cells, cell-weighting of the MG cross sections
should be done by the multigroup XSDRNPM calculation.

3. PMC_OMIT is used to indicate which pointwise nuclides are processed
when computing new group cross sections. If PMC_OMIT=1, only nuclides in
fuel mixtures are processed. Fuel mixtures are defined as having at
least one material with Z ≥ 90. Option PMC_OMIT>1 only works for PMC
standalone runs, since there is no mechanism for inputting the 2$$ array
in sequences.

4. IXTR3 is used to indicate through what Legendre order the scattering
matrices are to be processed. By default, in stand-alone mode all
P\ :sub:`N` moments on the Master library are processed, where as in a
SCALE sequence only through order N=5 are processed. With few
exceptions, the SCALE multigroup libraries contain scattering data
through P\ :sub:`5`.

5. If input parameter XS_DILUTE > 0.0, PMC computes background cross
sections (σ\ :sub:`0`) for each material, and bypasses processing
materials with σ\ :sub:`0` > XS_DILUTE. The default of XS_DILUTE
=10\ :sup:`10` barns causes essentially all materials to be processed
regardless of dilution. Smaller XS_DILUTE values may reduce the number
of materials being processed, and hence reduce the execution time;
however, XS_DILUTE should not be so low that important absorbers are not
shielded.

.. _7-5-5:

Example Case
------------

Usually PMC is executed through one of the automated SCALE sequences
such as CSAS or TRITON where it is called by XSProc in conjunction with
other SCALE modules, such as CRAWDAD which provides the pointwise
nuclear data library and CENTRM which provides pointwise fluxes. In such
cases the user does not have to prepare input directly for PMC.

.. _7-5-5-1:

PMC input for example case
~~~~~~~~~~~~~~~~~~~~~~~~~~

An example of PMC stand-alone execution is given below, but it should be
noted that this PMC case cannot be executed unless it is linked to the
output data files produced by other modules. The example problem given
in the CENTRM chapter shows the coupled execution of several stand-alone
modules, including PMC, which mimics the function of XSProc.

.. highlight:: scale

::

  =pmc
  0$$      -42      81      15     -42      18      19      17
  1$$     2   -1    0   0    0    1    0    0    5    0
   1t
  end

.. _7-5-5-2:

PMC output for example case
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Only the printed output produced by PMC for the example problem is shown
here. In this case the “standard” PMC editing option (NPRT=0) was
specified. The XSProc default of “minimum” print in the SCALE sequences
produces considerably less output.

.. highlight:: none

::

                    program verification information

                code system:    scale  version:    6.0



            program:  pmc

      creation date:  18_nov_2008

            library:  /scale/scale6/Linux_x86_64/bin

      production code:  pmc

            version:  6.0.9

            jobname:  xmw

        machine name:  node12.ornl.gov

    date of execution:  05_dec_2008

    time of execution:  13:22:19.23

::

  1

       0$ array      7 entries read

       1$ array     10 entries read

       1t

            **** LOGICAL UNITS ****

       nin   =   5   Card Image Input Unit
       nout  =   6   Print Output Unit
       libm  = -42   Input Master Library
       libx  =  81   Input Pointwise XS Library
       libf  =  15   Input Pointwise Flux File
       libnm = -42   Output Master Library
       libsc =  18   Scratch Unit 1
       libsx =  19   Scratch Unit 2
       libsm =  17   scratch unit (master library)



            **** INPUT PARAMETERS ****

       mrange =  2   Option for choosing energy range     0   Averaging over pointwise xs limits
                                                          1   Averaging over resolved resonance range
                                                          2   Averaging over pointwise flux limits

       n2d    = -1   Option for 2-D scat. calculation    -1  Recompute self-scatter, then normalize 2-D elastic
                                                              data to shielded 1-D value
                                                          0   Normalize 2-D elastic data to shielded 1-D value
                                                          1   Recompute 2-D elastic using flux and s-wave kernel
                                                          2   Recompute 2-D moments with flux-moments weighting

       nthrm  =  0   Option for thermal scatter kernal
                        (NOT FUNCTIONAL)

       nprt   =  0   Option for PMC print output         -1   Minimum data printed
                                                          0   Standard printed output
                                                          1   Print 1-D XSs
                                                          2   Print both 1-D and 2-D XSs

       nwt    =  0   Option for XS averaging              0   Zone average
                                                          1   Cell average

       mtt    =  1   Option for total XS calculation      0   Average independently
                                                          1   As sum of partial XS

       ixtr(1)=  0   Option for Processing PW Materials   0   Process all Pointwise Materials Used in CENTRM
                                                          N   Omit N Materials

       ixtr(2)=  0   Option for calculation sequence      0   CSAS Standard Sequence
                                                          1   Independant (stand-alone) Execution
                                                          2   CSAS Doubly-Heterogeneous Cell Sequence

       ixtr(3)=  5   Legendre expansion order            -1   Process all Legendre expansion moments found on AMPX LIB.
                                                    =0,...N   Process only up through PN moments

       n1d    =  0   Option for 1-D cross-sections        0   Weight using using scalar flux
                                                          1   Weight using using abs value of current (1st moment)

::

  **** POINTWISE CROSS SECTION LIBRARY ****

       tape identifier                   66666
       No. of nuclides                       9
       Max no. of temperatures               2
       Max no. of processes                  9
       Max no. of energy points         174194



            **** POINTWISE FLUX FILE ****

       No. of nuclides                      10
       No. flux moments                      1
       No. of zones                          3
       No. of energy points              48313
       Upper energy limit,demax    0.25000E+05
       Lower energy limit,demin    0.10000E-02



            **** AMPX INPUT MASTER LIBRARY ****

       ID of the tape              238000
       No. of nuclides                 10
       No. of neutron groups          238
       No. of gamma groups              0


            **** POINTWISE CROSS SECTION DIRECTORY ****

      ZA     Pointwise   Pointwise  Unresolved   Resolved    Resolved
               EMAX        EMIN        EMAX        EMAX        EMIN
      8016  0.2500E+05  0.1000E-02  0.0000E+00  0.0000E+00  0.0000E+00
     40090  0.2500E+05  0.1000E-02  0.4000E+06  0.6000E+05  0.0000E+00
     40091  0.2500E+05  0.1000E-02  0.1000E+06  0.2000E+05  0.0000E+00
     40092  0.2500E+05  0.1000E-02  0.1000E+06  0.7100E+05  0.0000E+00
     40094  0.2500E+05  0.1000E-02  0.1000E+06  0.9000E+05  0.0000E+00
     40096  0.2500E+05  0.1000E-02  0.1000E+06  0.1000E+06  0.0000E+00
     92235  0.2500E+05  0.1000E-02  0.2500E+05  0.2250E+04  0.0000E+00
     92238  0.2500E+05  0.1000E-02  0.1490E+06  0.2000E+05  0.0000E+00
      1001  0.2500E+05  0.1000E-02  0.0000E+00  0.0000E+00  0.0000E+00

::

  **** NUCLIDES IN POINTWISE FLUX CALCULATION ****
        Zone   IR(# of nuclides)     Temperature
          1           3                  900.0
          2           5                  600.0
          3           2                  600.0

                 -- Nuclide  by Zone --
                  0 -- no;  1 -- yes

       ID::       1008016     3008016     2040090     2040091     2040092     2040094
     ZONE::
       1            1           0           0           0           0           0
       2            0           0           1           1           1           1
       3            0           1           0           0           0           0
       ID::       2040096     1092235     1092238     3001001
     ZONE::
       1            0           1           1           0
       2            1           0           0           0
       3            0           0           0           1

               -- Atom Density by Zone --
       ID::      1008016     3008016     2040090     2040091     2040092     2040094
     ZONE::
       1      4.5968E-02  0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00
       2      0.0000E+00  0.0000E+00  2.5714E-02  5.6076E-03  8.5714E-03  8.6863E-03
       3      0.0000E+00  2.3831E-02  0.0000E+00  0.0000E+00  0.0000E+00  0.0000E+00

               -- Averaged Cell Atom Density    --
              2.2461E-02  1.0506E-02  1.8133E-03  3.9544E-04  6.0445E-04  6.1255E-04


       ID::      2040096     1092235     1092238     3001001
     ZONE::
       1      0.0000E+00  4.8838E-04  2.2480E-02  0.0000E+00
       2      1.3994E-03  0.0000E+00  0.0000E+00  0.0000E+00
       3      0.0000E+00  0.0000E+00  0.0000E+00  4.7662E-02

               -- Averaged Cell Atom Density    --
              9.8685E-05  2.3863E-04  1.0984E-02  2.1012E-02



            **** INPUT MASTER LIB. DIRECTORY ****

       nmt:   No. of 1-D Neutron Processes
       nbond: No. of Sets of Bondarenko Data
       nrec:  No. of Records for this Nuclide

          id          za          nmt        nbond     nrec

       1008016      8016.0         49          0          3
       3008016      8016.0         49          0          3
       2040090     40090.0         86          0          3
       2040091     40091.0         45          0          3
       2040092     40092.0         47          0          3
       2040094     40094.0         39          0          3
       2040096     40096.0         32          0          3
       1092235     92235.0         77          0          3
       1092238     92238.0         77          0          3
       3001001      1001.0         10          0          3

::

  P r o c e s s i n g   N u c l i d e  1008016

  Energy Range for Multigroup Averaging of this Data
  EH = 2.50000E+04  EL = 1.00000E-03

        INFORMATION ON CENTRM POINTWISE XS LIB:

     MT    ENERGY POINTS      TEMPERATURE (K)
      1        459            600.0    900.0
      2        459            600.0    900.0
    102        459            600.0    900.0

             <<<<< ZONE:    1 >>>>>

  PROCESSING MT =     1
       Generating new multigroup data from group   55 through group  234
  PROCESSING MT =     2
       Generating new multigroup data from group   55 through group  234
  PROCESSING MT =   102
       Generating new multigroup data from group   55 through group  234

  ====>> Done Processing Shielded Zone-Averaged Cross Section  1008016


  P r o c e s s i n g   N u c l i d e  3008016

  Energy Range for Multigroup Averaging of this Data
  EH = 2.50000E+04  EL = 1.00000E-03

        INFORMATION ON CENTRM POINTWISE XS LIB:

     MT    ENERGY POINTS      TEMPERATURE (K)
      1        459            600.0    900.0
      2        459            600.0    900.0
    102        459            600.0    900.0

             <<<<< ZONE:    3 >>>>>

  PROCESSING MT =     1
       Generating new multigroup data from group   55 through group  234
  PROCESSING MT =     2
       Generating new multigroup data from group   55 through group  234
  PROCESSING MT =   102
       Generating new multigroup data from group   55 through group  234

  ====>> Done Processing Shielded Zone-Averaged Cross Section  3008016

::

  P r o c e s s i n g   N u c l i d e  2040090

    Energy Range for Multigroup Averaging of this Data
    EH = 2.50000E+04  EL = 1.00000E-03

            INFORMATION ON CENTRM POINTWISE XS LIB:

         MT    ENERGY POINTS      TEMPERATURE (K)
          1       4488            600.0
          2       4488            600.0
        102       4488            600.0

                 <<<<< ZONE:    2 >>>>>

      PROCESSING MT =     1
           Generating new multigroup data from group   55 through group  234
      PROCESSING MT =     2
           Generating new multigroup data from group   55 through group  234
      PROCESSING MT =   102
           Generating new multigroup data from group   55 through group  234

    ====>> Done Processing Shielded Zone-Averaged Cross Section  2040090


      P r o c e s s i n g   N u c l i d e  2040091

    Energy Range for Multigroup Averaging of this Data
    EH = 2.50000E+04  EL = 1.00000E-03

            INFORMATION ON CENTRM POINTWISE XS LIB:

         MT    ENERGY POINTS      TEMPERATURE (K)
          1      24295            600.0
          2      24295            600.0
        102      24295            600.0

                 <<<<< ZONE:    2 >>>>>

      PROCESSING MT =     1
           Generating new multigroup data from group   55 through group  234
      PROCESSING MT =     2
           Generating new multigroup data from group   55 through group  234
      PROCESSING MT =   102
           Generating new multigroup data from group   55 through group  234

    ====>> Done Processing Shielded Zone-Averaged Cross Section  2040091

::


      P r o c e s s i n g   N u c l i d e  2040092

    Energy Range for Multigroup Averaging of this Data
    EH = 2.50000E+04  EL = 1.00000E-03

            INFORMATION ON CENTRM POINTWISE XS LIB:

         MT    ENERGY POINTS      TEMPERATURE (K)
          1       8142            600.0
          2       8142            600.0
        102       8142            600.0

                 <<<<< ZONE:    2 >>>>>

      PROCESSING MT =     1
           Generating new multigroup data from group   55 through group  234
      PROCESSING MT =     2
           Generating new multigroup data from group   55 through group  234
      PROCESSING MT =   102
           Generating new multigroup data from group   55 through group  234

    ====>> Done Processing Shielded Zone-Averaged Cross Section  2040092


      P r o c e s s i n g   N u c l i d e  2040094

    Energy Range for Multigroup Averaging of this Data
    EH = 2.50000E+04  EL = 1.00000E-03

            INFORMATION ON CENTRM POINTWISE XS LIB:

         MT    ENERGY POINTS      TEMPERATURE (K)
          1       8068            600.0
          2       8068            600.0
        102       8068            600.0

                 <<<<< ZONE:    2 >>>>>

      PROCESSING MT =     1
           Generating new multigroup data from group   55 through group  234
      PROCESSING MT =     2
           Generating new multigroup data from group   55 through group  234
      PROCESSING MT =   102
           Generating new multigroup data from group   55 through group  234

    ====>> Done Processing Shielded Zone-Averaged Cross Section  2040094


      P r o c e s s i n g   N u c l i d e  2040096

    Energy Range for Multigroup Averaging of this Data
    EH = 2.50000E+04  EL = 1.00000E-03

            INFORMATION ON CENTRM POINTWISE XS LIB:

         MT    ENERGY POINTS      TEMPERATURE (K)
          1       4944            600.0
          2       4944            600.0
        102       4944            600.0

                 <<<<< ZONE:    2 >>>>>

      PROCESSING MT =     1
           Generating new multigroup data from group   55 through group  234
      PROCESSING MT =     2
           Generating new multigroup data from group   55 through group  234
      PROCESSING MT =   102
           Generating new multigroup data from group   55 through group  234

    ====>> Done Processing Shielded Zone-Averaged Cross Section  2040096

::

  P r o c e s s i n g   N u c l i d e  1092235

    Energy Range for Multigroup Averaging of this Data
    EH = 2.50000E+04  EL = 1.00000E-03

            INFORMATION ON CENTRM POINTWISE XS LIB:

         MT    ENERGY POINTS      TEMPERATURE (K)
          1      59851            900.0
          2      59851            900.0
         18      59851            900.0
        102      59851            900.0
         51         94              0.0
         52         74              0.0
        452         48              0.0
        455          6              0.0
        456         48              0.0

                 <<<<< ZONE:    1 >>>>>

      PROCESSING MT =     1
           Generating new multigroup data from group   55 through group  234
      PROCESSING MT =     2
           Generating new multigroup data from group   55 through group  234
      PROCESSING MT =    18
           Generating new multigroup data from group   55 through group  234
      PROCESSING MT =   102
           Generating new multigroup data from group   55 through group  234
      PROCESSING MT =    51
           Generating new multigroup data from group   55 through group  234
      PROCESSING MT =    52
           Generating new multigroup data from group   55 through group  234
      PROCESSING MT =   452
           Generating new multigroup data from group   55 through group  234
      PROCESSING MT =   455
           Generating new multigroup data from group   55 through group  234
      PROCESSING MT =   456
           Generating new multigroup data from group   55 through group  234
      PROCESSING MT =  1018
       Collapsing 2D chi to effective 1D

    ====>> Done Processing Shielded Zone-Averaged Cross Section  1092235

::

  P r o c e s s i n g   N u c l i d e  1092238

  Energy Range for Multigroup Averaging of this Data
  EH = 2.50000E+04  EL = 1.00000E-03

        INFORMATION ON CENTRM POINTWISE XS LIB:

     MT    ENERGY POINTS      TEMPERATURE (K)
      1     174194            900.0
      2     174194            900.0
     18     174194            900.0
    102     174194            900.0
    452         10              0.0
    455          4              0.0
    456         10              0.0

             <<<<< ZONE:    1 >>>>>

  PROCESSING MT =     1
       Generating new multigroup data from group   55 through group  234
  PROCESSING MT =     2
       Generating new multigroup data from group   55 through group  234
  PROCESSING MT =    18
       Generating new multigroup data from group   55 through group  234
  PROCESSING MT =   102
       Generating new multigroup data from group   55 through group  234
  PROCESSING MT =   452
       Generating new multigroup data from group   55 through group  234
  PROCESSING MT =   455
       Generating new multigroup data from group   55 through group  234
  PROCESSING MT =   456
       Generating new multigroup data from group   55 through group  234
  PROCESSING MT =  1018
   Collapsing 2D chi to effective 1D

  ====>> Done Processing Shielded Zone-Averaged Cross Section  1092238


  P r o c e s s i n g   N u c l i d e  3001001

  Energy Range for Multigroup Averaging of this Data
  EH = 2.50000E+04  EL = 1.00000E-03

        INFORMATION ON CENTRM POINTWISE XS LIB:

     MT    ENERGY POINTS      TEMPERATURE (K)
      1        324            600.0
      2        324            600.0
    102        324            600.0

             <<<<< ZONE:    3 >>>>>

  PROCESSING MT =     1
       Generating new multigroup data from group   55 through group  234
  PROCESSING MT =     2
       Generating new multigroup data from group   55 through group  234
  PROCESSING MT =   102
       Generating new multigroup data from group   55 through group  234

  ====>> Done Processing Shielded Zone-Averaged Cross Section  3001001


  elapsed time   0.01 min.

::

  Number of nuclides in new master library  10

    The Output AMPX Master Library Produced by PMC

           Logical Unit No.                           -42
           Tape ID No.                             238000
           No. of Weighted Cross Section Sets          10
           No. of Neutron Groups                      238
           No. of Gamma Groups                          0
           First Thermal Neutron Group                149

    Contents of Output Master Library

           o16 825 endfb7 rel8 rev7 mod3                   08/13/08                           ID    1008016
           o16 825 endfb7 rel8 rev7 mod3                   08/13/08                           ID    3008016
           zr90 4025 endfb7 rel0 rev7 mod1                 08/13/08                           ID    2040090
           zr91 4028 endfb7 rel0 rev7 mod1                 08/13/08                           ID    2040091
           zr92 4031 endfb7 rel3 rev7 mod4                 08/13/08                           ID    2040092
           zr94 4037 endfb7 rel3 rev7 mod1                 08/13/08                           ID    2040094
           zr96 4043 endfb7 rel0 rev7 mod1                 08/13/08                           ID    2040096
           u235 9228 endfb7 rel0 rev7 mod7                 08/13/08                           ID    1092235
           u238 9237 endfb7 rel6 rev7 mod5                 08/13/08                           ID    1092238
           h_h2o 1 endfbv7 rel0 rev7 mod0                  09/29/08                           ID    3001001

     elapsed time   0.02 min.

            **** PMC CALCULATION COMPLETED ****

.. _7-5-6:

Formats of Data Files
---------------------

The CENTRM chapter of the SCALE manual describes the format for the CENTRM
PW nuclear data library and the format of the output PW flux file produced by
CENTRM, which is input to the PMC code.


.. bibliography:: bibs/PMC.bib
