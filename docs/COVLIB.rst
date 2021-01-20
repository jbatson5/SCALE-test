.. _10-2:

SCALE Nuclear Data Covariance Library
=====================================

*M. L. Williams, D. Wiarda, G. Arbanas, and B. L. Broadhead*

ABSTRACT

An updated cross section covariance library has been created for use
with the sensitivity and uncertainty modules in SCALE 6.2. The data has
been assembled from a variety sources, including high-fidelity
covariance evaluations from ENDF/B-VII.1 as well as approximate
uncertainties obtained from a collaborative project performed by
Brookhaven National Laboratory, Los Alamos National Laboratory, and Oak
Ridge National Laboratory. This document describes the assumptions in
generating the data, the library contents, and processing procedure for
the SCALE 56-group and 252-group covariance libraries. The SCALE
44-group covariance library distributed with SCALE 6.0 and SCALE 6.1 is
retained for backwards compatibility.

ACKNOWLEDGMENT

We gratefully acknowledge the sponsorship of the US Department of Energy
Nuclear Criticality Safety Program in the development of the SCALE 6.2
covariance libraries.

.. _10-2-1:

Introduction
------------

The SCALE 6.2 covariance library is based on available ENDF/B-VII.1 :cite:`chadwick_endfb-vii_2011`
data for 187 nuclides, combined with the previous SCALE 6.1 covariance
data are retained for the ~215 nuclides not available in ENDF/B‑VII.1.
The ENDF/B-VII.1 uncertainties were modified for a few nuclides, as
described in :ref:`10-2-2-3`. In addition, the covariance library now has
a 56-group structure for broad group analysis, as well as the 252-group
structure for fine-group analysis. These covariance libraries were
generated for compatibility with the ENDF/B-VII.1 cross section
libraries distributed with SCALE 6.2, and they may also be applied for
the 238-group ENDF/B-VII.0 library. The previous SCALE 6.0 and SCALE 6.1
44‑group library (44groupcov) was based on older covariance data and is
retained in SCALE 6.2 for backwards compatibility. However, the 56- and
252-group covariance libraries (56groupcov7.1 and 252groupcov7.1) are
now recommended for all applications. The 56-group library—which is
default for SCALE uncertainty analysis—and the 252 fine-group library
generally produce similar results, except for some threshold reactions
such as (n,2n). The 252-group library may be used to improve uncertainty
estimates from these types of data, but it typically takes more
execution time than the default 56-group library. Because the 56- and
252-group covariance data in many cases are based on newer uncertainty
evaluations than the previous 44-group library, some differences will
occur between these sets of results.

The covariance data correspond to relative uncertainties assembled from
a variety of sources, including evaluations from ENDF/B-VII.1,
ENDF/B-VI, and approximated uncertainties from a collaborative project
performed by Brookhaven National Laboratory (BNL), Los Alamos National
Laboratory (LANL), and Oak Ridge National Laboratory (ORNL). Because
SCALE uncertainty data come from several different sources, the
application of a single generic covariance library to all multigroup
cross section libraries raises questions about consistency with any
given data evaluation. In reality, much of the approximate uncertainty
data in the library is based on simplifying approximations that do not
depend on specific ENDF evaluations and thus can be applied to all cross
section libraries within the limitations of the assumed methodology. In
other cases in which a covariance evaluation has been taken from a
specific nuclear data file (e.g., ENDF/B-VII.1, ENDF/B-VI, or JENDL), it
is assumed that the same *relative* (rather than *absolute*)
uncertainties can be applied to all cross section libraries, even if
these are not strictly consistent with the nuclear data evaluations. The
assumption is partially justified by the fact that different evaluations
often use many of the same experimental measurements since there is a
limited amount of this information available. In some cases, older data
evaluations have been carried over into the newer ENDF versions. Also,
because many important nuclear data are now known rather well, newer
evaluations in many instances correspond to rather modest variations
from previous ones and are expected to lie within the earlier
uncertainties. As shown by plots in :ref:`11-3a`, the nuclear data
evaluations from ENDF/B-VII, ENDF/B-VI, JEF-3.1, and JENDL-3.3 tend to
agree well for many types of cross sections, so it is reasonable to
assume that the uncertainties in these data are similar.

No inherently “true” uncertainty can be defined for nuclear data. For
example, in theory, two independent evaluations could produce similar
nuclear data with very different uncertainties. Differences in nuclear
data evaluations directly impact calculations that can be affirmed by
comparisons with benchmark experiments; but there is no established
procedure to quantify the reliability of uncertainty estimates. In
general, the SCALE covariance library should be viewed as a
best-estimate assessment of data uncertainties based upon the specific
methodology described in the following section. While this methodology
is not unique and other approaches could have been used, the SCALE
covariance library is a reasonable representation of the nuclear data
uncertainties for most applications given the current lack of
information. Furthermore, it is the only available comprehensive library
that has been created in a well-defined, systematic manner.

.. _10-2-2:

Covariance Data Description
---------------------------

.. _10-2-2-1:

Evaluated covariances from nuclear data files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A rigorous, modern evaluation of nuclear data typically uses a
regression algorithm that adjusts parameters in a nuclear physics model
(e.g., Reich-Moore resonance formula, optical model, etc.), to fit a set
of differential experimental measurements that have various sources of
statistical and systematic uncertainties :cite:`larson_systematic_2006`. Information from the
regression analysis of the model parameters can be propagated to
uncertainties and correlations in the evaluated differential data. In
this manner, the differential nuclear data and covariances are
consistent and are coupled together by evaluation processes.
Unfortunately, only a limited number of cross section evaluations have
produced high-fidelity covariances in this rigorous manner. All other
nuclear data uncertainties must be estimated from approximations in
which the uncertainty assessment is decoupled from the original
evaluation procedure.

The SCALE covariance library is based on several different uncertainty
approximations with varying degrees of fidelity relative to the actual
nuclear data evaluation. The library includes high-fidelity evaluated
covariances obtained from ENDF/B-VII.1, and ENDF/B-VI whenever
available. As discussed in :ref:`10-2-1`, it is assumed that covariances
taken from one data evaluation, such as ENDF/B-VI, can also be applied
to other evaluations of the same data, such as ENDF/B-VII.1. If this is
done judiciously for cases in which the nuclear data evaluations are
similar, then the covariances taken from one source should be a
reasonable representation of uncertainties for the other evaluations.

.. _10-2-2-2:

Approximate covariance data
~~~~~~~~~~~~~~~~~~~~~~~~~~~

At the other end of the spectrum from high fidelity data, low-fidelity
(lo-fi) covariances are defined to be those estimated independently of a
specific data evaluation. The approximate covariance data in SCALE are
based on results from a collaborative project funded by the US
Department of Energy Nuclear Criticality Safety Program to generate
lo-fi covariances over the energy range from 10\ :sup:`-5` eV to 20 MeV
for materials without covariances in ENDF/B-VII.1. Nuclear data experts
at BNL, LANL, and ORNL devised simple procedures to estimate data
uncertainties in the absence of high fidelity covariance evaluations.
The result of this project is a set of covariance data in ENDF/B file 33
format that can be processed into multigroup covariances :cite:`little_low-fidelity_2008`. Some of
these data were later revised and included in ENDF/B‑VII.1, while others
were carried over from SCALE 6.1 to the SCALE 6.2 library. In this
documentation, these data are known as BLO (BNL-LANL-ORNL) uncertainty
data, which were generated as described below.

ORNL used uncertainties in integral experiment measurements of thermal
cross sections, resonance integrals, and potential cross sections to
approximate the standard deviations of capture, fission, and elastic
scattering reactions for the thermal (<0.5 eV) and resonance ranges (0.5
eV- 5 keV). Full energy correlation was assumed for the covariances
within each of these respective ranges :cite:`williams_approximate_2007,williams_scale-6_2008` This
procedure was originally introduced for the approximate uncertainty data
in SCALE 5.1. However, the current version includes updated integral
measurement uncertainties, using the more recent values tabulated by
Mughabghab in the *Atlas of Neutron Resonances* :cite:`mughabghab_atlas_2006`. The lo-fi relative
uncertainty is computed as the absolute uncertainty in the integral
parameter (i.e., thermal cross section or resonance integral) taken from
the *Atlas*, divided by the average of the measured parameter and the
calculated value computed from ENDF/B-VII differential data:

.. math::
  :label: eq10-2-1

  \mathrm{U}=\frac{\Delta_{\mathrm{I}}}{0.5 \times\left(\mathrm{X}_{\mathrm{I}}+\mathrm{X}_{\mathrm{D}}\right)} ,

where:

  U is the relative lo-fi uncertainty included in SCALE,

  Δ\ :sub:`I` is the absolute uncertainty in the integral measurement
  (obtained from Mughabghab), and

  X\ :sub:`I` and X\ :sub:`D` are the measured and computed (from
  ENDF/B differential data) integral parameter values, respectively.

In some cases the integral measurement value from the Mughabghab
*Atlas*\ :sup:`6` and the corresponding value computed from the
ENDF/B-VII differential evaluation are inconsistent—defined here as
having a difference greater than two standard deviations in the measured
and computed integral parameters. In these cases, the lo-fi relative
standard deviation is defined as half the difference relative to the
average of the measured and calculated values:

.. math::
  :label: eq10-2-2

  \mathrm{U}=\frac{\left|\mathrm{X}_{\mathrm{I}}-\mathrm{X}_{\mathrm{D}}\right|}{\mathrm{X}_{\mathrm{I}}+\mathrm{X}_{\mathrm{D}}} ; \text { for }\left|\mathrm{X}_{\mathrm{I}}-\mathrm{X}_{\mathrm{D}}\right|>2 \Delta_{\mathrm{I}} .

In some instances this expression may exceed 100%. For these cases, a
100% uncertainty was assigned. Also, the *Atlas* does not include
uncertainties in integral measurements for several isotopes, which
typically are not of great interest for most applications. In this case
the integral uncertainty was defined as a +/-5 in the least significant
digit for these materials; e.g., 1.23 is assign an uncertainty of +/-
5E-3.

BNL and LANL provided estimates in the fast energy range from 5 keV to
20 MeV for covariances of capture, fission, elastic, inelastic, (n,2n)
cross sections, and prompt nubar. BNL used optical model calculations
with estimated uncertainties in model parameters to compute covariances
in the fast range for about 300 structural isotopes, fission products,
and non-fissionable heavy nuclei. Estimated uncertainties in model
parameters were based on previous work and expert judgment :cite:`pigni_extensive_2009`.
Covariances for 14 actinide isotopes were obtained from earlier work
performed by BNL for Subgroup-26 (SG-26) :cite:`rochman_preliminary_2007`. The SG-26 actinide
covariances cover the full energy range, including thermal, resonance,
and fast regions. If the thermal data uncertainties estimated by the
SG-26 approach exceed the thermal uncertainty given in reference 6, the
thermal data covariances are represented by ORNL’s integral uncertainty
technique.

LANL produced covariances in the fast range for an additional 47
actinide materials. The LANL actinide covariances were based on
empirical estimates of nuclear reaction models :cite:`kawano_evaluation_2008`. Full energy range
covariances were also produced by LANL for 16 light isotopes ranging
from hydrogen to fluorine :cite:`hale_covariances_2008`. These included high fidelity
covariances from R-matrix analyses for :sup:`1`\ H, :sup:`6`\ Li, and
:sup:`10`\ B, along with lo-fi uncertainties for the other materials,
based on approximations such as least-squares fitting to experimental
data, statistical model calculations at higher energies, or sometimes
simply best-judgment estimation :cite:`little_low-fidelity_2008`.

.. _10-2-2-3:

Modifications to covariance data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In generating earlier covariance libraries, some omissions or
inconsistencies were identified and corrected in the current covariance
library:

-  If the absolute correlation is larger than 1, it is set to 1.

-  If a relative uncertainty is larger than 1, it is set to 1.

-  If cross section data exist but covariance data do not span the
   entire range, then the diagonal element for the higher energy groups
   is repeated for the lower energy groups.

-  If total inelastic scattering covariance is not supplied, it is
   calculated from the uncertainties in the discrete level inelastic
   data.

-  If total nubar covariance is not supplied, it is calculated from the
   the prompt and delayed nubar uncertainties

A few inconsistencies were found in the ENDF/B-VII.1 uncertainty data,
and these were modified for the SCALE 6.2 covariance library :cite:`williams_applications_2014`. The
corrections were also conveyed to the National Nuclear Data Center,
where they were added to the ENDF/A file for possible inclusion in the
future release of ENDF/B-VII.2. These modifications are summarized
below:

(a) :sup:`235`\ U thermal nubar: standard deviation was decreased from
    0.7% to 0.3% in energy range from 0.0 to 0.5 eV, consistent with
    JENDL-3.3.

(b) :sup:`239`\ Pu thermal nubar: standard deviation was increased from
    0.01% to 0.15% in energy range from 0.0 to 0.01 eV, consistent with
    ENDF/B-VII.1 uncertainty at 0.01 eV.

(c) H thermal capture: standard deviation reduced from 2.5% to 0.2%,
    consistent with Williams and Rearden 2008 :cite:`williams_scale-6_2008`,

(d) :sup:`103`\ Rh thermal capture: reduced from ~4% to 1.04%,
consistent with Williams and Rearden 2008 :cite:`williams_scale-6_2008`.

(e) :sup:`151`\ Sm thermal capture: modified to ~1.8%, consistent with
Williams and Rearden 2008 :cite:`williams_scale-6_2008`.

(f) :sup:`147`\ Pm: standard deviation was reduced from 24% to 5% in the
energy range 0.5–5000 eV, consistent with the quoted resonance integral
uncertainty in Williams and Rearden 2008 :cite:`williams_scale-6_2008`.

Several modifications were also made to the uncertainties obtained from
the original BLO data used in SCALE 6.1. The energy boundary between the
thermal and resonance covariance blocks was modified from 0.5 to 0.625
eV in order to coincide with a 56-group boundary. The BLO lo-fi data do
not include thermal or resonance range uncertainties for isotope
reactions that do not have integral uncertainties given in the
Mughabghab text :cite:`mughabghab_atlas_2006`. These occur mainly for relatively unimportant
data such as elastic cross sections of several fission products.
Therefore in these cases the uncertainties were estimated using
different approaches. For example, the thermal data uncertainty was
sometimes used to represent the epithermal uncertainty if it was not
available in the Mughabghab tabulation, and sometimes the high-energy
uncertainty was extended to lower energies. The uncertainty in the
:sup:`149`\ Sm resonance capture integral is not provided in the 2006
edition of Mughabghab’s text, so it was set to the value of 5.7%, which
was obtained from an earlier tabulation by Mughabghab :cite:`mughabghab_thermal_2003`.

.. _10-2-2-4:

Covariance data for fission spectra
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As of ENDF/B-VII.1, covariance matrices are now provided for the fission
exit energy distribution. The data are given as a function of incident
energy. The incident energy grid is very broad, and the exit energy
distribution is constant over a given incident energy group. Since the
COVERX library file only allows one multigroup fission spectrum (χ)
covariance matrix per nuclide, the exit energy spectrum is used for the
average energy of fission. If ν is nubar, *f* is fission, and *w* is the
appropriate flux, then the average energy of fission is calculated as:

.. math::
  :label: eq10-2-3

  10^{7}exp\left( - \frac{\sum_{}^{}{\text{vfw}\frac{1}{2}\left( \log\left( \frac{10^{7}}{E_{g1}} \right) + log\left( \frac{10^{7}}{E_{g2}} \right) \right)}}{\sum_{}^{}\text{νfw}} \right) ,

where the sum is over all groups and E\ :sub:`g1` and E\ :sub:`g2` are
the group boundaries for group g. ENDF/B-VII.1 provides covariance data
for exit energy distributions for 64 nuclides. This includes all
nuclides for which fission spectrum (χ) covariance matrices where
provided in the previous covariance library. Some additional
χ-covariance matrices were taken from JENDL-4.0. The new 56-group and
252-group fission spectrum covariances are more complete and
significantly improved compared to the earlier 44-group chi uncertainty
data, which were based on the Watt fission spectrum in ENDF/B-V. (see
:ref:`10-2-5`).

.. _10-2-3:

Multigroup Covariance Processing
--------------------------------

Covariance data were processed with the AMPX code PUFF-IV. PUFF-IV has
major improvements in the treatment of the resolved and unresolved
resonance parameter uncertainties over previous code versions :cite:`wiarda_recent_2008`. All
nuclides with resonance parameter uncertainty files were processed with
the full sensitivity option in PUFF-IV.

.. _10-2-4:

Contents of the SCALE 6.2 Covariance Library
--------------------------------------------

The SCALE covariance library provides uncertainty data in 56- and
252-group formats for a total of 456 materials, including some
duplication for materials with multiple thermal scattering kernels.
:numref:`tab10-2-1` describes the contents of the library using the following
nomenclature:

1. ENDF/B-VII.1: evaluated covariance data released with ENDF/B-VII.1

2. ENDF/B-VII.2-prelim: recently evaluated data proposed for future
   release of ENDF/B-VII.2

3. ENDF/B-VI: evaluated covariance data released with ENDF/B-VI

4. BLO approximate data: lo-fi covariances from BLO project

5. SG-26: approximate covariances from WPEC Subgroup-26

6. JENDL-4.0: evaluated covariance data released with JENDL-4.0

Several covariance evaluations include cross correlations between
reactions. These are summarized in :numref:`tab10-2-2`.

.. tabularcolumns:: |m{2cm}|m{2cm}|m{3cm}|m{7cm}|

.. _tab10-2-1:
.. table:: Contents of SCALE 6.2 covariance libraries.
  :align: center
  :class: longtable

  +-----------------+-----------------+-----------------+-----------------+
  | **SCALE name**  | **SCALE ID**    | **Data source** | **Comment**     |
  +=================+=================+=================+=================+
  | ac-225          | 89225           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ac-226          | 89226           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ac-227          | 89227           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ag-107          | 47107           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ag-109          | 47109           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ag-110m         | 1047110         | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ag-111          | 47111           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | al-27           | 13027           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | albound         | 1013027         | ENDF/B-VII.1    | Duplicate of    |
  |                 |                 |                 | al-27           |
  +-----------------+-----------------+-----------------+-----------------+
  | am-240          | 95240           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | am-241          | 95241           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |                 |                 | χ covariance    |                 |
  |                 |                 | JENDL-4.0       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | am-242          | 95242           | SG-26           | Thermal         |
  |                 |                 |                 | uncertainty     |
  |                 |                 |                 | replaced by     |
  |                 |                 |                 | Mughabghab      |
  |                 |                 |                 | value           |
  +-----------------+-----------------+-----------------+-----------------+
  |                 |                 | χ covariance    |                 |
  |                 |                 | JENDL-4.0       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | am-242m         | 1095242         | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | am-243          | 95243           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |                 |                 | χ covariance    |                 |
  |                 |                 | JENDL-4.0       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | am-244          | 95244           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |                 |                 | χ covariance    |                 |
  |                 |                 | JENDL-4.0       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | am-244m         | 1095244         | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ar-36           | 18036           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ar-38           | 18038           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ar-40           | 18040           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | as-74           | 33074           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | as-75           | 33075           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | au-197          | 79197           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | b-10            | 5010            | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | b-11            | 5011            | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ba-130          | 56130           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ba-132          | 56132           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ba-133          | 56133           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ba-134          | 56134           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ba-135          | 56135           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ba-136          | 56136           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ba-137          | 56137           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ba-138          | 56138           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ba-140          | 56140           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | be-7            | 4007            | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | be-9            | 4009            | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | be-beo          | 5004009         | ENDF/B-VII.1    | Duplicate of    |
  |                 |                 |                 | be-9            |
  +-----------------+-----------------+-----------------+-----------------+
  | bebound         | 3004009         | ENDF/B-VII.1    | Duplicate of    |
  |                 |                 |                 | be-9            |
  +-----------------+-----------------+-----------------+-----------------+
  | bi-209          | 83209           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | bk-245          | 97245           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | bk-246          | 97246           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | bk-247          | 97247           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | bk-248          | 97248           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | bk-249          | 97249           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | bk-250          | 97250           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | br-79           | 35079           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | br-81           | 35081           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | c               | 6000            | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ca              | 20000           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | dataca          |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ca-40           | 20040           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ca-42           | 20042           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ca-43           | 20043           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ca-44           | 20044           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ca-46           | 20046           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ca-48           | 20048           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cd              | 48000           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cd-106          | 48106           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cd-108          | 48108           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cd-110          | 48110           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cd-111          | 48111           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cd-112          | 48112           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cd-113          | 48113           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cd-114          | 48114           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cd-115m         | 1048115         | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cd-116          | 48116           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ce-136          | 58136           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ce-138          | 58138           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ce-139          | 58139           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ce-140          | 58140           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ce-141          | 58141           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ce-142          | 58142           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ce-143          | 58143           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ce-144          | 58144           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cf-246          | 98246           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cf-248          | 98248           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cf-249          | 98249           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cf-250          | 98250           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cf-251          | 98251           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cf-252          | 98252           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cf-253          | 98253           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cf-254          | 98254           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cl              | 17000           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cl-35           | 17035           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cl-37           | 17037           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cm-240          | 96240           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cm-241          | 96241           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cm-242          | 96242           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cm-243          | 96243           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cm-244          | 96244           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cm-245          | 96245           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cm-246          | 96246           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cm-247          | 96247           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cm-248          | 96248           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cm-249          | 96249           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cm-250          | 96250           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | co-58           | 27058           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | co-58m          | 1027058         | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | co-59           | 27059           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cr-50           | 24050           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cr-52           | 24052           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cr-53           | 24053           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cr-54           | 24054           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cs-133          | 55133           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cs-134          | 55134           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cs-135          | 55135           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cs-136          | 55136           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cs-137          | 55137           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cu-63           | 29063           | ENDF/B-VI       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | cu-65           | 29065           | ENDF/B-VI       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | d               | 1002            | ENDF/B-VII.1    | Duplicate of    |
  |                 |                 |                 | h-2             |
  +-----------------+-----------------+-----------------+-----------------+
  | d-cryo_ortho    | 4001002         | ENDF/B-VII.1    | Duplicate of    |
  |                 |                 |                 | h-2             |
  +-----------------+-----------------+-----------------+-----------------+
  | d-cryo_para     | 5001002         | ENDF/B-VII.1    | Duplicate of    |
  |                 |                 |                 | h-2             |
  +-----------------+-----------------+-----------------+-----------------+
  | dfreegas        | 8001002         | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | dy-156          | 66156           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | dy-158          | 66158           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | dy-160          | 66160           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | dy-161          | 66161           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | dy-162          | 66162           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | dy-163          | 66163           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | dy-164          | 66164           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | er-162          | 68162           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | er-164          | 68164           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | er-166          | 68166           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | er-167          | 68167           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | er-168          | 68168           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | er-170          | 68170           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | es-251          | 99251           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | es-252          | 99252           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | es-253          | 99253           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | es-254          | 99254           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | es-254m         | 1099254         | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | es-255          | 99255           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | eu-151          | 63151           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | eu-152          | 63152           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | eu-153          | 63153           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | eu-154          | 63154           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | eu-155          | 63155           | ENDF/B-VII.1    | Uses            |
  |                 |                 |                 | ENDF/B-VII.1    |
  |                 |                 |                 | data            |
  |                 |                 |                 | uncertainty in  |
  |                 |                 |                 | the thermal     |
  |                 |                 |                 | range for       |
  |                 |                 |                 | MT=102          |
  +-----------------+-----------------+-----------------+-----------------+
  | eu-156          | 63156           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | eu-157          | 63157           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | f-19            | 9019            | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | fe-54           | 26054           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | fe-56           | 26056           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | fe-57           | 26057           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | fe-58           | 26058           | ENDF/B-VI       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | febound         | 1026000         | ENDF/B-VII.1    | Duplicate of    |
  |                 |                 |                 | fe-56           |
  +-----------------+-----------------+-----------------+-----------------+
  | fm-255          | 100255          | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ga              | 31000           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ga-69           | 31069           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ga-71           | 31071           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | gd-152          | 64152           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | gd-153          | 64153           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | gd-154          | 64154           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | gd-155          | 64155           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | gd-156          | 64156           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | gd-157          | 64157           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | gd-158          | 64158           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | gd-160          | 64160           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ge-70           | 32070           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ge-72           | 32072           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ge-73           | 32073           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ge-74           | 32074           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ge-76           | 32076           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | graphite        | 3006000         | ENDF/B-VII.1    | Duplicate of c  |
  +-----------------+-----------------+-----------------+-----------------+
  | h               | 1001            | ENDF/B-VII.2    | Duplicate of h1 |
  |                 |                 | prelim          |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | h-3             | 1003            | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | h-benzene       | 6001001         | ENDF/B-VII.2    | Duplicate of    |
  |                 |                 | prelim          | h-1             |
  +-----------------+-----------------+-----------------+-----------------+
  | h-benzene       | 5006000         | ENDF/B-VII.1    | Duplicate of c  |
  +-----------------+-----------------+-----------------+-----------------+
  | h-cryo_ortho    | 4001001         | ENDF/B-VII.2    | Duplicate of    |
  |                 |                 | prelim          | h-1             |
  +-----------------+-----------------+-----------------+-----------------+
  | h-cryo_para     | 5001001         | ENDF/B-VII.2    | Duplicate of    |
  |                 |                 | prelim          | h-1             |
  +-----------------+-----------------+-----------------+-----------------+
  | h-liquid_ch4    | 1001001         | ENDF/B-VII.2    | Duplicate of    |
  |                 |                 | prelim          | h-1             |
  +-----------------+-----------------+-----------------+-----------------+
  | h-poly          | 9001001         | ENDF/B-VII.2    | Duplicate of    |
  |                 |                 | prelim          | h-1             |
  +-----------------+-----------------+-----------------+-----------------+
  | h-solid_ch4     | 2001001         | ENDF/B-VII.2    | Duplicate of    |
  |                 |                 | prelim          | h-1             |
  +-----------------+-----------------+-----------------+-----------------+
  | h-zrh2          | 7001001         | ENDF/B-VII.2    | Duplicate of    |
  |                 |                 | prelim          | h-1             |
  +-----------------+-----------------+-----------------+-----------------+
  | he-3            | 2003            | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | he-4            | 2004            | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | hf              | 72000           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | hf-174          | 72174           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | hf-176          | 72176           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | hf-177          | 72177           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | hf-178          | 72178           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | hf-179          | 72179           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | hf-180          | 72180           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | hfreegas        | 8001001         | ENDF/B-VII.2    |                 |
  |                 |                 | prelim          |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | hg-196          | 80196           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | hg-198          | 80198           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | hg-199          | 80199           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | hg-200          | 80200           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | hg-201          | 80201           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | hg-202          | 80202           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | hg-204          | 80204           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ho-165          | 67165           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ho-166m         | 1067166         | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | i-127           | 53127           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | i-129           | 53129           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | i-130           | 53130           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | i-131           | 53131           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | i-135           | 53135           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | in              | 49000           | ENDF/B-VI       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | in-113          | 49113           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | in-115          | 49115           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ir-191          | 77191           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ir-193          | 77193           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | k               | 19000           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | k-39            | 19039           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | k-40            | 19040           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | k-41            | 19041           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | kr-78           | 36078           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | kr-80           | 36080           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | kr-82           | 36082           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | kr-83           | 36083           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | kr-84           | 36084           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | kr-85           | 36085           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | kr-86           | 36086           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | la-138          | 57138           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | la-139          | 57139           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | la-140          | 57140           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | li-6            | 3006            | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | li-7            | 3007            | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | lu-175          | 71175           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | lu-176          | 71176           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | mg              | 12000           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | mg-24           | 12024           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | mg-25           | 12025           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | mg-26           | 12026           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | mn-55           | 25055           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | mo              | 42000           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | mo-100          | 42100           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | mo-92           | 42092           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | mo-94           | 42094           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | mo-95           | 42095           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | mo-96           | 42096           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | mo-97           | 42097           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | mo-98           | 42098           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | mo-99           | 42099           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | n-14            | 7014            | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | n-15            | 7015            | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | na-23           | 11023           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | nb-93           | 41093           | ENDF/B-VI       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | nb-94           | 41094           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | nb-95           | 41095           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | nd-142          | 60142           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | nd-143          | 60143           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | nd-144          | 60144           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | nd-145          | 60145           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | nd-146          | 60146           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | nd-147          | 60147           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | nd-148          | 60148           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | nd-148          | 60148           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | nd-150          | 60150           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ni-58           | 28058           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ni-59           | 28059           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ni-60           | 28060           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ni-61           | 28061           | ENDF/B-VI       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ni-62           | 28062           | ENDF/B-VI       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ni-64           | 28064           | ENDF/B-VI       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | np-234          | 93234           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | np-235          | 93235           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | np-236          | 93236           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | np-237          | 93237           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |                 |                 | χ covariance    |                 |
  |                 |                 | JENDL-4.0       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | np-238          | 93238           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | np-239          | 93239           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | o-16            | 8016            | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | o-17            | 8017            | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | o-beo           | 5008016         | ENDF/B-VII.1    | Duplicate of    |
  |                 |                 |                 | o-16            |
  +-----------------+-----------------+-----------------+-----------------+
  | o-uo2           | 1008016         | ENDF/B-VII.1    | Duplicate of    |
  |                 |                 |                 | o-16            |
  +-----------------+-----------------+-----------------+-----------------+
  | p-31            | 15031           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pa-229          | 91229           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pa-230          | 91230           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pa-231          | 91231           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |                 |                 | χ covariance    |                 |
  |                 |                 | JENDL-4.0       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pa-232          | 91232           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pa-233          | 91233           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |                 |                 | χ covariance    |                 |
  |                 |                 | JENDL-4.0       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pb-204          | 82204           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pb-206          | 82206           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pb-207          | 82207           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pb-208          | 82208           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pd-102          | 46102           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pd-104          | 46104           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pd-105          | 46105           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pd-106          | 46106           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pd-107          | 46107           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pd-108          | 46108           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pd-110          | 46110           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pm-147          | 61147           | ENDF/B-VII.1    | Thermal and     |
  |                 |                 |                 | resonance range |
  |                 |                 |                 | uncertainty     |
  |                 |                 |                 | values from     |
  |                 |                 |                 | Mughabghab      |
  |                 |                 |                 |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pm-148          | 61148           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pm-148m         | 1061148         | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pm-149          | 61149           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pm-151          | 61151           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pr-141          | 59141           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pr-142          | 59142           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pr-143          | 59143           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pu-236          | 94236           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pu-237          | 94237           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pu-238          | 94238           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pu-239          | 94239           | ENDF/B-VII.2    |                 |
  |                 |                 | prelim          |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pu-240          | 94240           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pu-241          | 94241           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |                 |                 | χ covariance    |                 |
  |                 |                 | JENDL-4.0       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pu-242          | 94242           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pu-243          | 94243           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pu-244          | 94244           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | pu-246          | 94246           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | rb-85           | 37085           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | rb-86           | 37086           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | rb-87           | 37087           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | re-185          | 75185           | ENDF/B-VI       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | re-187          | 75187           | ENDF/B-VI       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | rh-103          | 45103           | ENDF/B-VII.1    | Uses            |
  |                 |                 |                 | ENDF/B-VII.1    |
  |                 |                 |                 | data            |
  |                 |                 |                 | uncertainty in  |
  |                 |                 |                 | the thermal     |
  |                 |                 |                 | range for       |
  |                 |                 |                 | MT=102          |
  +-----------------+-----------------+-----------------+-----------------+
  | rh-105          | 45105           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ru-100          | 44100           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ru-101          | 44101           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ru-102          | 44102           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ru-103          | 44103           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ru-104          | 44104           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ru-105          | 44105           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ru-106          | 44106           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ru-96           | 44096           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ru-98           | 44098           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ru-99           | 44099           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | s               | 16000           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | s-32            | 16032           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | s-33            | 16033           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | s-34            | 16034           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | s-36            | 16036           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sb-121          | 51121           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sb-123          | 51123           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sb-124          | 51124           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sb-125          | 51125           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sb-126          | 51126           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sc-45           | 21045           | ENDF/B-VI       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | se-74           | 34074           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | se-76           | 34076           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | se-77           | 34077           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | se-78           | 34078           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | se-79           | 34079           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | se-80           | 34080           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | se-82           | 34082           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | si              | 14000           | ENDF/B-VI       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | si-28           | 14028           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | si-29           | 14029           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | si-30           | 14030           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | si-28 in        | 14728           | ENDF/B-VII.1    | Duplicate of    |
  | SiO\ :sub:`2`   |                 |                 | si-28           |
  +-----------------+-----------------+-----------------+-----------------+
  | si-29 in        | 14729           | ENDF/B-0VII.1   | Duplicate of    |
  | SiO\ :sub:`2`   |                 |                 | si-29           |
  +-----------------+-----------------+-----------------+-----------------+
  | si-30 in        | 14730           | ENDF/B-VII.1    | Duplicate of    |
  | SiO\ :sub:`2`   |                 |                 | si-30           |
  +-----------------+-----------------+-----------------+-----------------+
  | sm-144          | 62144           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sm-147          | 62147           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sm-148          | 62148           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sm-149          | 62149           | ENDF/B-VII.1    | Uses            |
  |                 |                 |                 | ENDF/B-VII.1    |
  |                 |                 |                 | data            |
  |                 |                 |                 | uncertainty in  |
  |                 |                 |                 | the thermal     |
  |                 |                 |                 | range for       |
  |                 |                 |                 | MT=102          |
  +-----------------+-----------------+-----------------+-----------------+
  | sm-149          | 62149           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sm-150          | 62150           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sm-151          | 62151           | ENDF/B-VII.1    | Uses            |
  |                 |                 |                 | ENDF/B-VII.1    |
  |                 |                 |                 | data            |
  |                 |                 |                 | uncertainty in  |
  |                 |                 |                 | the thermal     |
  |                 |                 |                 | range for       |
  |                 |                 |                 | MT=102          |
  +-----------------+-----------------+-----------------+-----------------+
  | sm-152          | 62152           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sm-153          | 62153           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sm-154          | 62154           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sn-112          | 50112           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sn-113          | 50113           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sn-114          | 50114           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sn-115          | 50115           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sn-116          | 50116           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sn-117          | 50117           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sn-118          | 50118           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sn-119          | 50119           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sn-120          | 50120           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sn-122          | 50122           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sn-123          | 50123           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sn-124          | 50124           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sn-125          | 50125           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sn-126          | 50126           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sr-84           | 38084           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sr-86           | 38086           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sr-87           | 38087           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sr-88           | 38088           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sr-89           | 38089           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | sr-90           | 38090           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ta-181          | 73181           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ta-182          | 73182           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | tb-159          | 65159           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | tb-160          | 65160           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | tc-99           | 43099           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | te-120          | 52120           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | te-122          | 52122           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | te-123          | 52123           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | te-124          | 52124           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | te-125          | 52125           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | te-126          | 52126           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | te-127m         | 1052127         | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | te-128          | 52128           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | te-129m         | 1052129         | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | te-130          | 52130           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | te-132          | 52132           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | th-227          | 90227           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | th-228          | 90228           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | th-229          | 90229           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | th-230          | 90230           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | th-231          | 90231           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | th-232          | 90232           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |                 |                 | χ covariance    |                 |
  |                 |                 | JENDL-4.0       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | th-233          | 90233           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | th-234          | 90234           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ti              | 22000           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ti-46           | 22046           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ti-47           | 22047           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ti-48           | 22048           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ti-49           | 22049           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ti-50           | 22050           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | tl-203          | 81203           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | tl-205          | 81205           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | tm-169          | 69169           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | tm-170          | 69170           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | u-230           | 92230           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | u-231           | 92231           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | u-232           | 92232           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | u-233           | 92233           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |                 |                 | χ covariance    |                 |
  |                 |                 | JENDL-4.0       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | u-234           | 92234           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | u-235           | 92235           | ENDF/B-VII.2    |                 |
  |                 |                 | prelim          |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | u-236           | 92236           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | u-237           | 92237           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | u-238           | 92238           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | u-239           | 92239           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | u-240           | 92240           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | u-241           | 92241           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | u-uo2           | 1092235         | ENDF/B-VII.1    | Duplicate of    |
  |                 |                 |                 | u-235           |
  +-----------------+-----------------+-----------------+-----------------+
  | v               | 23000           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | w               | 74000           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | w-180           | 74180           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | w-182           | 74182           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | w-183           | 74183           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | w-184           | 74184           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | w-186           | 74186           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | xe-123          | 54123           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | xe-124          | 54124           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | xe-126          | 54126           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | xe-128          | 54128           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | xe-129          | 54129           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | xe-130          | 54130           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | xe-131          | 54131           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | xe-132          | 54132           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | xe-133          | 54133           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | xe-134          | 54134           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | xe-135          | 54135           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | xe-136          | 54136           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | y-89            | 39089           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | y-90            | 39090           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | y-91            | 39091           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | zr              | 40000           | BLO             |                 |
  |                 |                 | approximation   |                 |
  |                 |                 | data            |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | zr-90           | 40090           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | zr-91           | 40091           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | zr-92           | 40092           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | zr-93           | 40093           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | zr-94           | 40094           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | zr-95           | 40095           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | zr-96           | 40096           | ENDF/B-VII.1    |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | zr-90-zr5h8     | 1040090         | ENDF/B-VII.1    | Duplicate of    |
  |                 |                 |                 | zr-90           |
  +-----------------+-----------------+-----------------+-----------------+
  | zr-91-zr5h8     | 1040091         | ENDF/B-VII.1    | Duplicate of    |
  |                 |                 |                 | zr-91           |
  +-----------------+-----------------+-----------------+-----------------+
  | zr-92-zr5h8     | 1040092         | ENDF/B-VII.1    | Duplicate of    |
  |                 |                 |                 | zr-92           |
  +-----------------+-----------------+-----------------+-----------------+
  | zr-93-zr5h8     | 1040093         | ENDF/B-VII.1    | Duplicate of    |
  |                 |                 |                 | zr-93           |
  +-----------------+-----------------+-----------------+-----------------+
  | zr-94-zr5h8     | 1040094         | ENDF/B-VII.1    | Duplicate of    |
  |                 |                 |                 | zr-94           |
  +-----------------+-----------------+-----------------+-----------------+
  | zr-95-zr5h8     | 1040095         | ENDF/B-VII.1    | Duplicate of    |
  |                 |                 |                 | zr-95           |
  +-----------------+-----------------+-----------------+-----------------+
  | zr-96-zr5h8     | 1040096         | ENDF/B-VII.1    | Duplicate of    |
  |                 |                 |                 | zr-96           |
  +-----------------+-----------------+-----------------+-----------------+

.. _tab10-2-2:
.. table::  Covariance data with cross-correlations between nuclide reactions.
  :align: center


  +----------------+------------+----------------+-------------------+
  | Nuclide 1      | Reaction 1 | Nuclide 2      | Reaction 2        |
  +================+============+================+===================+
  | :sup:`239`\ Pu | Fission    | :sup:`6`\ Li   | Triton production |
  +----------------+------------+----------------+-------------------+
  | :sup:`239`\ Pu | Fission    | :sup:`197`\ Au | Capture           |
  +----------------+------------+----------------+-------------------+
  | :sup:`239`\ Pu | Fission    | :sup:`235`\ U  | Fission           |
  +----------------+------------+----------------+-------------------+
  | :sup:`239`\ Pu | Fission    | :sup:`238`\ U  | Fission           |
  +----------------+------------+----------------+-------------------+
  | :sup:`235`\ U  | Fission    | :sup:`197`\ Au | Capture           |
  +----------------+------------+----------------+-------------------+
  | :sup:`235`\ U  | Fission    | :sup:`6`\ Li   | Triton production |
  +----------------+------------+----------------+-------------------+
  | :sup:`238`\ U  | Capture    | :sup:`197`\ Au | Capture           |
  +----------------+------------+----------------+-------------------+
  | :sup:`238`\ U  | Capture    | :sup:`235`\ U  | Fission           |
  +----------------+------------+----------------+-------------------+

.. _10-2-5:

SCALE 6.1 44-group covariance library
-------------------------------------

The older 44-group covariance library distributed with SCALE 6.0 and
SCALE 6.1 is included with this distribution for backwards
compatibility. The 44-group covariance library provides uncertainty data
for a total of 401 materials, including some duplication for materials
with multiple thermal scattering kernels. However, the 44-group library
was created prior to the official release of ENDF/B-VII.1. Therefore, it
is recommended that the 56- or 252-group covariances be used rather than
the 44-group. As discussed in :ref:`10-2-1`, it is assumed that
covariances taken from one data evaluation such as ENDF/B-VI or
JENDL-3.3 can also be applied to other evaluations of the same data,
such as ENDF/B-VII. If this is done judiciously for cases in which the
nuclear data evaluations are similar, then the covariances taken from
one source should be a reasonable representation of uncertainties for
the other evaluations. Among the materials in the SCALE 44-group library
with covariances taken from high-fidelity nuclear data evaluations are
the following:

a) ENDF/B-VII evaluations *(includes both VII.0 and pre-release
covariances proposed for VII.1, but no official ENDF/B-VII.1)*:

   Au, :sup:`209`\ Bi, :sup:`59`\ Co, :sup:`152,154,155,156`\ Gd,
   :sup:`191,193`\ I, :sup:`7`\ Li, :sup:`23`\ Na, :sup:`93`\ Nb,
   :sup:`58`\ Ni, :sup:`99`\ Tc,\ :sup:`232`\ Th, :sup:`48`\ Ti,
   :sup:`239`\ Pu, :sup:`233,235,238`\ U,V

(b) ENDF/B-VI evaluations:

   Al, :sup:`241`\ Am, :sup:`10`\ B, :sup:`12`\ C,
   :sup:`50,52,53,54`\ Cr, :sup:`63,65`\ Cu, :sup:`54,56,57`\ Fe, In,
   :sup:`55`\ Mn, :sup:`60,61,62,64`\ Ni, :sup:`206,207,208`\ Pb,
   :sup:`242`\ Pu, :sup:`28,29`\ Si

(c) JENDL-3.3 evaluations:

   :sup:`11`\ B, :sup:`1`\ H, :sup:`16`\ O, :sup:`240,241`\ Pu

Two modifications were also made to the ENDF/B-VII evaluated nubar
covariances. These nubar uncertainties are believed to be more
realistic. The ENDF/B-VII.0 :sup:`235`\ U thermal nubar uncertainty of
0.71% was revised to the JENDL-3.3 value of 0.31%. In addition, the
thermal nubar certainty in the pre-released ENDF/B-VII.1 :sup:`233`\ U
evaluation was modified to the value in a recent ORNL data
evaluation :cite:`leal_233_2008`. This ORNL :sup:`233`\ U cross section evaluation also
provided the thermal and resonance cross sections for the prereleased
ENDF/B‑VII.1 data. The ENDF/B-VII.1 pre-release nubar data for
:sup:`239`\ Pu was incomplete when the 44-group covariance library was
generated, so :sup:`239`\ Pu nubar data are included from ENDF/B-V, the
most current data available at that time. This value is much higher than
the current estimated uncertainty in :sup:`239`\ Pu nubar. The basic
ENDF/B uncertainty files that were changed are described in
:numref:`tab10-2-3`.

Several modifications were also made to the uncertainties obtained from
the BLO data. The BLO thermal uncertainties for :sup:`1`\ H capture and
elastic and for :sup:`16`\ O elastic were modified to the JENDL-3.3
values of 0.5% and 0.1%, respectively. Similarly, the uncertainty in the
:sup:`10`\ B (n,alpha) thermal cross section was modified to the
ENDF/B-VI value of about 0.2%, since this is more consistent with the
Mughabghab integral uncertainty. The uncertainty in the :sup:`149`\ Sm
resonance capture integral is not provided in the 2006 edition of
Mughabghab’s text; therefore it was set to the value of 5.7% which was
obtained from an earlier tabulation by Mughabghab :cite:`mughabghab_thermal_2003`.

.. _tab10-2-3:
.. table:: Summary of changes made to covariance evaluations for the 44-group library.
  :align: center

  +-----------------------------------+-----------------------------------+
  | ENDF/B-VII.1 pre-release          | Data were incomplete at time of   |
  |                                   | library generation, so ENDF/B-V   |
  | :sup:`239`\ Pu                    | data were used for nubar.         |
  +===================================+===================================+
  | ENDF/B-VII                        | Thermal nubar modified to         |
  |                                   | JENDL-3.3 value                   |
  | :sup:`235`\ U                     |                                   |
  +-----------------------------------+-----------------------------------+
  | ENDF/B-VII                        | Thermal nubar modified to value   |
  |                                   | from ORNL internal evaluation     |
  | :sup:`233`\ U                     |                                   |
  +-----------------------------------+-----------------------------------+
  | ENDF/B-VI                         | Thermal uncertainties were added  |
  |                                   | to total cross section (set equal |
  | :sup:`241`\ Am                    | to capture uncertainties)         |
  +-----------------------------------+-----------------------------------+
  | ENDF/B-VI                         | In elastic scatter uncertainty,   |
  |                                   | corrected cross reference to      |
  | :sup:`28`\ Si, :sup:`29`\ Si,     | MT=102 from original value of     |
  | :sup:`30`\ Si, :sup:`206`\ Pb,    | MT=1.02                           |
  | :sup:`57`\ Fe                     |                                   |
  +-----------------------------------+-----------------------------------+
  | ENDF/B-VI                         | Removed MT=3 due to inconsistency |
  |                                   | with other MT values, resulting   |
  | :sup:`208`\ Pb, :sup:`207`\ Pb    | in very large uncertainty         |
  |                                   | predictions                       |
  +-----------------------------------+-----------------------------------+

At the time of the preparation of the 44-group covariance library,
ENDF/B did not provide fission spectra uncertainty estimates. The
methodology used to construct these data for the 44-group covariance
library is described in Broadhead and Wagschal :cite:`broadhead_fission_2004`. In this approach,
the fission spectrum is represented as either a Watt or Maxwellian
distribution. These energy distributions are widely used to represent
fission spectra and have been commonly employed in many ENDF/B
evaluations. For example, Watt and Maxwellian expressions were used
almost exclusively to describe fission spectra in ENDF/B-V and also for
many ENDF/B-VI evaluations. More recent evaluations for some important
fissionable nuclides have replaced the simple Watt and Maxwellian
analytical expressions by distributions such as the Madland-Nix spectrum
obtained from more phenomenological nuclear fission models. However, it
is assumed here that uncertainties based on an appropriate Watt or
Maxwellian representation of the fission spectrum can be transferred to
the actual fission spectra contained in the different multigroup cross
section libraries.

The methodology in Broadhead and Wagschal :cite:`broadhead_fission_2004` determines
energy-dependent covariances from uncertainties and correlations in the
*a* and *b* parameters for the Watt spectrum or the *T* parameter for a
Maxwellian spectrum, appearing the analytical expressions given below:

Watt Spectrum:  :math:`\chi(\mathrm{E})=\frac{\mathrm{e}^{-\mathrm{E} / \mathrm{a}}}{\mathrm{I}} \sinh (\sqrt{\mathrm{bE}})`

Maxwellian Spectrum:  :math:`\chi(\mathrm{E})=\frac{\sqrt{\mathrm{E}} \mathrm{e}^{-\mathrm{E} / \mathrm{T}}}{\mathrm{I}}`

In these expressions, the parameter “I” is the normalization factor
required to normalize the integrated spectrum to unity. The value of “I”
is fixed by the values of the other parameters. Due to the normalization
constraint, the fission spectrum covariance includes anti-correlations.
The assumed fission spectra parameters and uncertainties are given in
Maerker, Marable, and Wagschal 1980 :cite:`maerker_estimation_1980` and in Howerton and Doyas
1971 :cite:`howerton_fission_1971`.

:numref:`tab10-2-4` shows that fission spectra covariances are not provided for
all fissionable materials in the SCALE multigroup cross sections.
:numref:`tab10-2-5` lists the fissionable nuclides without fission spectra
covariances on the 44-group covariance library.

.. |t| replace:: :sup:`16`
.. |n| replace:: :sup:`17`
.. _tab10-2-4:
.. table:: Source of fission spectrum parameters and uncertainties
  :align: center

  +---------+---------+---------+---------+---------+---------+---------+
  | Watt    | *a* or  | *b*     | Source  | ∂\ *a*  | ∂\ *b*  | Source  |
  | spectru\| *T*     |         | of      | or      |         | of      |
  | m       |         |         | paramet\| ∂\ *T*  | (%)     | uncerta\|
  |         |         |         | ers     | (%)     |         | inty    |
  +=========+=========+=========+=========+=========+=========+=========+
  | :sup:`2\| 0.988   | 2.249   | ENDF/B-\| 1.2     | 5.9     |TANS\ |t||
  | 35`\ U  |         |         | V       |         |         |         |
  |         |         |         |         |         |         |         |
  +---------+---------+---------+---------+---------+---------+---------+
  | :sup:`2\| 0.881   | 3.401   | ENDF/B-\| 1.2     | 5.9     |TANS\ |t||
  | 38`\ U  |         |         | V       |         |         |         |
  |         |         |         |         |         |         |         |
  +---------+---------+---------+---------+---------+---------+---------+
  | :sup:`2\| 0.977   | 2.546   | ENDF/B-\| 1.2     | 5.9     |TANS\ |t||
  | 33`\ U  |         |         | V       |         |         |         |
  |         |         |         |         |         |         |         |
  +---------+---------+---------+---------+---------+---------+---------+
  | :sup:`2\| 0.966   | 2.842   | ENDF/B-\| 1.2     | 5.9     |TANS\ |t||
  | 39`\ Pu |         |         | V       |         |         |         |
  |         |         |         |         |         |         |         |
  +---------+---------+---------+---------+---------+---------+---------+
  | :sup:`2\| 1.0888  | 1.6871  | ENDF/B-\| 1.2     | 5.9     |TANS\ |t||
  | 32`\ Th |         |         | V       |         |         |         |
  |         |         |         |         |         |         |         |
  +---------+---------+---------+---------+---------+---------+---------+
  | :sup:`2\| 1.025   | 2.926   | ENDF/B-\| 1.2     | 5.9     |TANS\ |t||
  | 52`\ Cf |         |         | V       |         |         |         |
  |         |         |         |         |         |         |         |
  +---------+---------+---------+---------+---------+---------+---------+
  | Maxwell\|         |         |         |         |         |         |
  | ian     |         |         |         |         |         |         |
  | Spectru\|         |         |         |         |         |         |
  | m       |         |         |         |         |         |         |
  +---------+---------+---------+---------+---------+---------+---------+
  | :sup:`2\| 1.330   | —       | ENDF/B-\| 3.01    | —       |NSE\ |n| |
  | 38`\ Pu |         |         | V       |         |         |         |
  +---------+---------+---------+---------+---------+---------+---------+
  | :sup:`2\| 1.346   | —       | ENDF/B-\| 2.97    | —       |NSE\ |n| |
  | 40`\ Pu |         |         | V       |         |         |         |
  +---------+---------+---------+---------+---------+---------+---------+
  | :sup:`2\| 1.3597  | —       | ENDF/B-\| 2.50    | —       |NSE\ |n| |
  | 41`\ Pu |         |         | V       |         |         |         |
  +---------+---------+---------+---------+---------+---------+---------+
  | :sup:`2\| 1.337   | —       | ENDF/B-\| 5.24    | —       |NSE\ |n| |
  | 42`\ Pu |         |         | V       |         |         |         |
  +---------+---------+---------+---------+---------+---------+---------+

.. _tab10-2-5:
.. table:: Fissionable nuclides with missing fission spectrum uncertainty data in covariance library.
  :align: center

  +----------------+----------------+----------------+
  | :sup:`241`\ Am | :sup:`244`\ Cm | :sup:`238`\ Pu |
  +================+================+================+
  | :sup:`242`\ Am | :sup:`245`\ Cm | :sup:`243`\ Pu |
  +----------------+----------------+----------------+
  | :sup:`243`\ Am | :sup:`246`\ Cm | :sup:`244`\ Pu |
  +----------------+----------------+----------------+
  | :sup:`249`\ Bk | :sup:`247`\ Cm | :sup:`230`\ Th |
  +----------------+----------------+----------------+
  | :sup:`249`\ Cf | :sup:`248`\ Cm | :sup:`232`\ U  |
  +----------------+----------------+----------------+
  | :sup:`250`\ Cf | :sup:`237`\ Np | :sup:`234`\ U  |
  +----------------+----------------+----------------+
  | :sup:`251`\ Cf | :sup:`238`\ Np | :sup:`236`\ U  |
  +----------------+----------------+----------------+
  | :sup:`253`\ Cf | :sup:`239`\ Np | :sup:`237`\ U  |
  +----------------+----------------+----------------+
  | :sup:`242`\ Cm | :sup:`231`\ Pa |                |
  +----------------+----------------+----------------+
  | :sup:`243`\ Cm | :sup:`233`\ Pa |                |
  +----------------+----------------+----------------+

*Table 10.2.6 describes the contents of the library using the following
nomenclature:*

1. ENDF/B-VII.0: evaluated covariance data released with ENDF/B-VII.0

2. ENDF/B-VII-p: recently evaluated data proposed for future release of
   ENDF/B-VII.1

3. ENDF/B-VI: evaluated covariance data released with ENDF/B-VI

4. JENDL-3.3: evaluated covariance data in JENDL-3.3

5. BLO approximate data: lo-fi covariances from BLO project

6. BLO LANL evaluation: LANL R-matrix evaluation from BLO project

7. SG-26: approximate covariances from WPEC Subgroup-26

.. tabularcolumns:: |m{3cm}|m{5em}|m{7cm}|

.. _tab10-2-6:
.. table:: Contents of SCALE 6.1 44-group covariance library.
  :align: center
  :class: longtable

  +-----------------------+-----------------------+-----------------------+
  | **SCALE name**        | **Data source**       | **Comments**          |
  +-----------------------+-----------------------+-----------------------+
  | ac-225                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ac-226                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ac-227                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ag-107                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ag-109                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ag-110m               | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ag-111                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | al-27                 | ENDF/B-VI             |                       |
  +-----------------------+-----------------------+-----------------------+
  | am-241                | ENDF/B-VI             | MT=452 added          |
  |                       |                       | corrections for total |
  |                       |                       | and elastic)          |
  +-----------------------+-----------------------+-----------------------+
  | am-242                | SG-26                 | Thermal uncertainty   |
  |                       |                       | replaced by           |
  |                       |                       | Mughabghab value      |
  +-----------------------+-----------------------+-----------------------+
  | am-242m               | SG-26                 | Thermal uncertainty   |
  |                       |                       | replaced by           |
  |                       |                       | Mughabghab value      |
  +-----------------------+-----------------------+-----------------------+
  | am-243                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | am-244                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | am-244m               | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ar-36                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ar-38                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ar-40                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | as-74                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | as-75                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | au-197                | ENDF/B-VII-p          | Pre-released          |
  |                       |                       | evaluation proposed   |
  |                       |                       | for ENDF/B-VII.1      |
  +-----------------------+-----------------------+-----------------------+
  | b-10                  | BLO LANL evaluation   | LANL high-fidelity    |
  |                       | +ENDF/B-VI            | covariance, with      |
  |                       |                       | ENDF/B-VI for thermal |
  +-----------------------+-----------------------+-----------------------+
  | b-11                  | JENDL 3.3             |                       |
  +-----------------------+-----------------------+-----------------------+
  | ba-130                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ba-132                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ba-133                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ba-135                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ba-136                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ba-137                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ba-138                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ba-140                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | be-7                  | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | be-9                  | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | Bebound               | BLO approximate data  | Duplicate of          |
  |                       |                       | :sup:`9`\ Be          |
  +-----------------------+-----------------------+-----------------------+
  | bi-209                | ENDF/B-VII-p          | Pre-released          |
  |                       |                       | evaluation proposed   |
  |                       |                       | for ENDF/B-VII.1      |
  +-----------------------+-----------------------+-----------------------+
  | bk-249                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | bk-250                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | br-79                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | br-81                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | C                     | ENDF/B-VI             |                       |
  +-----------------------+-----------------------+-----------------------+
  | C-graphite            | ENDF/B-VI             | Duplicate of carbon   |
  +-----------------------+-----------------------+-----------------------+
  | Ca                    | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ca-40                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ca-42                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ca-43                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ca-44                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ca-46                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ca-48                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | Cd                    | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cd-106                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cd-108                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cd-110                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cd-111                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cd-112                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cd-113                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cd-114                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cd-115m               | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cd-116                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cd-136                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cd-138                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cd-139                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cd-140                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cd-141                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cd-142                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ce-143                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ce-144                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cf-249                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cf-250                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cf-251                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cf-252                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cf-253                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cf-254                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | Cl                    | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cl-35                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cl-37                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cm-241                | BLO approximate data  | Thermal uncertainty   |
  +-----------------------+-----------------------+-----------------------+
  | cm-242                | SG-26                 | Mughabghab value      |
  +-----------------------+-----------------------+-----------------------+
  | cm-243                | SG-26                 | Thermal uncertainty   |
  |                       |                       | replaced by           |
  |                       |                       | Mughabghab value      |
  +-----------------------+-----------------------+-----------------------+
  | cm-244                | SG-26                 | Thermal uncertainty   |
  |                       |                       | replaced by           |
  |                       |                       | Mughabghab value      |
  +-----------------------+-----------------------+-----------------------+
  | cm-245                | SG-26                 | Thermal uncertainty   |
  |                       |                       | replaced by           |
  |                       |                       | Mughabghab value      |
  +-----------------------+-----------------------+-----------------------+
  | cm-246                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cm-247                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cm-248                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cm-249                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cm-250                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | co-58                 | BLO approximate data  | Pre-released          |
  |                       |                       | evaluation proposed   |
  | co-58m                | BLO approximate data  | for ENDF/B-VII.1      |
  |                       |                       |                       |
  | co-59                 | ENDF/B-VII-p          |                       |
  +-----------------------+-----------------------+-----------------------+
  | cr-50                 | ENDF/B-VI             | LB=8 representation   |
  |                       |                       | caused problematic    |
  |                       |                       | representation of     |
  |                       |                       | cross section         |
  |                       |                       | uncertainty due to    |
  |                       |                       | use of fine energy    |
  |                       |                       | group structure.      |
  |                       |                       | Tests were performed  |
  |                       |                       | to determine how to   |
  |                       |                       | handle this problem.  |
  |                       |                       | LB=8 data were        |
  |                       |                       | removed in the final  |
  |                       |                       | results.              |
  +-----------------------+-----------------------+-----------------------+
  | cr-52                 | ENDF/B-VI             | LB=8 representation   |
  |                       |                       | caused problematic    |
  |                       |                       | representation of     |
  |                       |                       | cross section         |
  |                       |                       | uncertainty due to    |
  |                       |                       | use of fine energy    |
  |                       |                       | group structure.      |
  |                       |                       | Tests were performed  |
  |                       |                       | to determine how to   |
  |                       |                       | handle this problem.  |
  |                       |                       | LB=8 data were        |
  |                       |                       | removed in the final  |
  |                       |                       | results.              |
  +-----------------------+-----------------------+-----------------------+
  | cr-53                 | ENDF/B-VI             | LB=8 representation   |
  |                       |                       | caused problematic    |
  |                       |                       | representation of     |
  |                       |                       | cross section         |
  |                       |                       | uncertainty due to    |
  |                       |                       | use of fine energy    |
  |                       |                       | group structure.      |
  |                       |                       | Tests were performed  |
  |                       |                       | to determine how to   |
  |                       |                       | handle this problem.  |
  |                       |                       | LB=8 data were        |
  |                       |                       | removed in the final  |
  |                       |                       | results.              |
  +-----------------------+-----------------------+-----------------------+
  | cr-54                 | ENDF/B-VI             | LB=8 representation   |
  |                       |                       | caused problematic    |
  |                       |                       | representation of     |
  |                       |                       | cross section         |
  |                       |                       | uncertainty due to    |
  |                       |                       | use of fine energy    |
  |                       |                       | group structure.      |
  |                       |                       | Tests were performed  |
  |                       |                       | to determine how to   |
  |                       |                       | handle this problem.  |
  |                       |                       | LB=8 data were        |
  |                       |                       | removed in the final  |
  |                       |                       | results.              |
  +-----------------------+-----------------------+-----------------------+
  | cs-133                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cs-134                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cs-135                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cs-136                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cs-137                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | cu-63                 | ENDF/B-VI             |                       |
  +-----------------------+-----------------------+-----------------------+
  | cu-65                 | ENDF/B-VI             |                       |
  +-----------------------+-----------------------+-----------------------+
  | dy-156                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | dy-158                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | dy-160                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | dy-161                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | dy-162                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | dy-163                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | dy-164                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | er-162                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | er-164                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | er-166                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | er-167                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | er-168                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | er-170                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | es-253                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | es-254                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | es-255                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | eu-151                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | eu-152                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | eu-153                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | eu-154                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | eu-155                | BLO approximate data  |                       |
  |                       | BLO approximate data  |                       |
  | eu-156                | BLO approximate data  |                       |
  |                       |                       |                       |
  | eu-157                |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | f-19                  | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | fe-54                 | ENDF/B-VI             | LB=8 representation   |
  |                       |                       | caused problematic    |
  |                       |                       | representation of     |
  |                       |                       | cross section         |
  |                       |                       | uncertainty due to    |
  |                       |                       | use of fine energy    |
  |                       |                       | group structure.      |
  |                       |                       | Tests were performed  |
  |                       |                       | to determine how to   |
  |                       |                       | handle this problem.  |
  |                       |                       | LB=8 data were        |
  |                       |                       | removed in the final  |
  |                       |                       | results.              |
  +-----------------------+-----------------------+-----------------------+
  | fe-56                 | ENDF/B-VI             | LB=8 representation   |
  |                       |                       | caused problematic    |
  |                       |                       | representation of     |
  |                       |                       | cross section         |
  |                       |                       | uncertainty due to    |
  |                       |                       | use of fine energy    |
  |                       |                       | group structure.      |
  |                       |                       | Tests were performed  |
  |                       |                       | to determine how to   |
  |                       |                       | handle this problem.  |
  |                       |                       | LB=8 data were        |
  |                       |                       | removed in the final  |
  |                       |                       | results.              |
  +-----------------------+-----------------------+-----------------------+
  | fe-57                 | ENDF/B-VI             | Error in file         |
  |                       |                       | corrected             |
  |                       |                       | LB=8 representation   |
  |                       |                       | caused problematic    |
  |                       |                       | representation of     |
  |                       |                       | cross section         |
  |                       |                       | uncertainty due to    |
  |                       |                       | use of fine energy    |
  |                       |                       | group structure.      |
  |                       |                       | Tests were performed  |
  |                       |                       | to determine how to   |
  |                       |                       | handle this problem.  |
  |                       |                       | LB=8 data were        |
  |                       |                       | removed in the final  |
  |                       |                       | results.              |
  +-----------------------+-----------------------+-----------------------+
  | fe-58                 | ENDF/B-VI             | LB=8 representation   |
  |                       |                       | caused problematic    |
  | fm-255                | BLO approximate data  | representation of     |
  |                       |                       | cross section         |
  |                       |                       | uncertainty due to    |
  |                       |                       | use of fine energy    |
  |                       |                       | group structure.      |
  |                       |                       | Tests were performed  |
  |                       |                       | to determine how to   |
  |                       |                       | handle this problem.  |
  |                       |                       | LB=8 data were        |
  |                       |                       | removed in the final  |
  |                       |                       | results. New material |
  |                       |                       | not in previous       |
  |                       |                       |                       |
  |                       |                       | SCALE 5.1 covariance  |
  |                       |                       | libraries.            |
  +-----------------------+-----------------------+-----------------------+
  | Ga                    | BLO approximate data  |                       |
  |                       |                       |                       |
  | ga-69                 | BLO approximate data  |                       |
  |                       |                       |                       |
  | ga-71                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | gd-152                | ENDF/B-VII.0          |                       |
  |                       |                       |                       |
  | gd-153                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | gd-154                | ENDF/B-VII.0          |                       |
  +-----------------------+-----------------------+-----------------------+
  | gd-155                | ENDF/B-VII.0          |                       |
  +-----------------------+-----------------------+-----------------------+
  | gd-156                | ENDF/B-VII.0          |                       |
  +-----------------------+-----------------------+-----------------------+
  | gd-157                | ENDF/B-VII.0          |                       |
  +-----------------------+-----------------------+-----------------------+
  | gd-158                | ENDF/B-VII.0          |                       |
  +-----------------------+-----------------------+-----------------------+
  | gd-160                | ENDF/B-VII.0          |                       |
  +-----------------------+-----------------------+-----------------------+
  | ge-70                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ge-72                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ge-73                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ge-74                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ge-76                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | h-1                   | BLO LANL evaluation   | LANL covariance above |
  |                       | +JENDL 3.3            | 5 keV;                |
  |                       |                       | JENDL values below 5  |
  |                       |                       | keV                   |
  +-----------------------+-----------------------+-----------------------+
  | h-ZrH                 | BLO LANL evaluation   | Duplicate of          |
  |                       | +JENDL 3.             | :sup:`1`\ H           |
  +-----------------------+-----------------------+-----------------------+
  | h-poly                | BLO LANL evaluation   | Duplicate of          |
  |                       | +JENDL 3.             | :sup:`1`\ H           |
  +-----------------------+-----------------------+-----------------------+
  | Hfreegas              | BLO LANL evaluation   | Duplicate of          |
  |                       | +JENDL 3.             | :sup:`1`\ H           |
  +-----------------------+-----------------------+-----------------------+
  | h-2                   | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | Dfreegas              | BLO approximate data  | Duplicate of          |
  |                       |                       | :sup:`2`\ H           |
  +-----------------------+-----------------------+-----------------------+
  | h-3                   | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | he-3                  | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | he-4                  | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | Hf                    | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | hf-174                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | hf-176                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | fh-177                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | hf-178                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | hf-179                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | hf-180                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | hg-196                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | hg-198                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | hg-199                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | hg-200                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | hg-201                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | hg-202                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | hg-204                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ho-165                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | i-127                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | i-129                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | i-130                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | i-131                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | i-135                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | In                    | ENDF/B-VI             |                       |
  +-----------------------+-----------------------+-----------------------+
  | in-113                | BLO approximate data  |                       |
  |                       |                       |                       |
  | in-115                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ir-191                | ENDF/B-VII.0          |                       |
  +-----------------------+-----------------------+-----------------------+
  | ir-193                | ENDF/B-VII.0          |                       |
  +-----------------------+-----------------------+-----------------------+
  | K                     | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | k-39                  | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | k-40                  | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | k-41                  | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | kr-78                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | kr-80                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | kr-82                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | kr-83                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | kr-84                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | kr-85                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | kr-86                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | la-138                | BLO approximate data  |                       |
  |                       | BLO approximate data  |                       |
  | la-139                |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | la-140                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | li-6                  | BLO-LANL evaluation   |                       |
  +-----------------------+-----------------------+-----------------------+
  | li-7                  | ENDF/B-VII.0          |                       |
  +-----------------------+-----------------------+-----------------------+
  | lu-175                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | lu-176                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | Mg                    | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | mg-24                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | mg-25                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | mg-26                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | mn-55                 | ENDF/B-VI             | LB=8 representation   |
  |                       |                       | caused problematic    |
  |                       |                       | representation of     |
  |                       |                       | cross section         |
  |                       |                       | uncertainty due to    |
  |                       |                       | use of fine energy    |
  |                       |                       | group structure.      |
  |                       |                       | Tests were performed  |
  |                       |                       | to determine how to   |
  |                       |                       | handle this problem.  |
  |                       |                       | LB=8 data were        |
  |                       |                       | removed in the final  |
  |                       |                       | results.              |
  +-----------------------+-----------------------+-----------------------+
  | Mo                    | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | mo-92                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | mo-94                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | mo-95                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | mo-96                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | mo-97                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | mo-98                 | BLO approximate data  |                       |
  |                       | BLO approximate data  |                       |
  | mo-99                 |                       |                       |
  |                       | BLO approximate data  |                       |
  | mo-100                |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | n-14                  | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | n-15                  | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | na-23                 | ENDF/B-VII-p          | Pre-released          |
  |                       |                       | evaluation proposed   |
  |                       |                       | for ENDF/B-VII.1      |
  +-----------------------+-----------------------+-----------------------+
  | nb-93                 | ENDF/B-VII-p          | Pre-released          |
  |                       |                       | evaluation proposed   |
  |                       |                       | for ENDF/B-VII.1      |
  +-----------------------+-----------------------+-----------------------+
  | nb-94                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | nb-95                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | nd-142                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | nd-143                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | nd-144                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | nd-145                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | nd-146                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | nd-147                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | nd-148                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | nd-150                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ni-58                 | ENDF/B-VII-p          | Pre-released          |
  |                       |                       | evaluation proposed   |
  | ni-59                 | BLO approximate data  | for ENDF/B-VII.1      |
  +-----------------------+-----------------------+-----------------------+
  | ni-60                 | ENDF/B-VI             | LB=8 representation   |
  |                       |                       | caused problematic    |
  |                       |                       | representation of     |
  |                       |                       | cross section         |
  |                       |                       | uncertainty due to    |
  |                       |                       | use of fine energy    |
  |                       |                       | group structure.      |
  |                       |                       | Tests were performed  |
  |                       |                       | to determine how to   |
  |                       |                       | handle this problem.  |
  |                       |                       | LB=8 data were        |
  |                       |                       | removed in the final  |
  |                       |                       | results.              |
  +-----------------------+-----------------------+-----------------------+
  | ni-61                 | ENDF/B-VI             | LB=8 representation   |
  |                       |                       | caused problematic    |
  |                       |                       | representation of     |
  |                       |                       | cross section         |
  |                       |                       | uncertainty due to    |
  |                       |                       | use of fine energy    |
  |                       |                       | group structure.      |
  |                       |                       | Tests were performed  |
  |                       |                       | to determine how to   |
  |                       |                       | handle this problem.  |
  |                       |                       | LB=8 data were        |
  |                       |                       | removed in the final  |
  |                       |                       | results.              |
  +-----------------------+-----------------------+-----------------------+
  | ni-62                 | ENDF/B-VI             | LB=8 representation   |
  |                       |                       | caused problematic    |
  |                       |                       | representation of     |
  |                       |                       | cross section         |
  |                       |                       | uncertainty due to    |
  |                       |                       | use of fine energy    |
  |                       |                       | group structure.      |
  |                       |                       | Tests were performed  |
  |                       |                       | to determine how to   |
  |                       |                       | handle this problem.  |
  |                       |                       | LB=8 data were        |
  |                       |                       | removed in the final  |
  |                       |                       | results.              |
  +-----------------------+-----------------------+-----------------------+
  | ni-64                 | ENDF/B-VI             | LB=8 representation   |
  |                       |                       | caused problematic    |
  |                       |                       | representation of     |
  |                       |                       | cross section         |
  |                       |                       | uncertainty due to    |
  |                       |                       | use of fine energy    |
  |                       |                       | group structure.      |
  |                       |                       | Tests were performed  |
  |                       |                       | to determine how to   |
  |                       |                       | handle this problem.  |
  |                       |                       | LB=8 data were        |
  |                       |                       | removed in the final  |
  |                       |                       | results.              |
  +-----------------------+-----------------------+-----------------------+
  | np-235                | BLO approximate data  | Thermal uncertainty   |
  |                       |                       | replaced by           |
  | np-236                | BLO approximate data  | Mughabghab value      |
  |                       |                       |                       |
  | np-237                | SG-26                 |                       |
  +-----------------------+-----------------------+-----------------------+
  | np-238                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | np-239                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | o-16                  | JENDL 3.3+BLO         | BLO covariances from  |
  |                       |                       | LANL used above 5 keV |
  +-----------------------+-----------------------+-----------------------+
  | o-17                  | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | p-31                  | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pa-231                | BLO approximate data  |                       |
  |                       |                       |                       |
  | pa-232                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pa-233                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pb-204                | BLO approximate data  | Error in file         |
  |                       | ENDF/B-VI             | corrected             |
  | pb-206                |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | pb-207                | ENDF/B-VI             | MT=3 removed, Error   |
  |                       |                       | in file corrected     |
  +-----------------------+-----------------------+-----------------------+
  | bp-208                | ENDF/B-VI             | MT=3 removed, Error   |
  |                       |                       | in file corrected     |
  +-----------------------+-----------------------+-----------------------+
  | pd-102                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pd-104                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pd-105                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pd-106                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pd-107                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pd-108                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pd-110                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pm-147                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pm-148                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pm-148m               | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pm-149                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pm-151                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pr-141                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pr-142                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pr-143                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pu-236                | BLO approximate data  | Thermal uncertainty   |
  |                       |                       | replaced by           |
  | pu-237                | BLO approximate data  | Mughabghab value      |
  |                       |                       |                       |
  | pu-238                | SG-26                 |                       |
  +-----------------------+-----------------------+-----------------------+
  | pu-239                | ENDF/B-VII-p          | Pre-released          |
  |                       |                       | evaluation proposed   |
  |                       |                       | for ENDF/B-VII.1;     |
  |                       |                       | nubar data from       |
  |                       |                       | ENDF/B-V              |
  |                       |                       |                       |
  |                       |                       | | Cross               |
  |                       |                       |   nuclide-to-nuclide  |
  |                       |                       |   matrices present;   |
  |                       |                       |   covariances due to  |
  |                       |                       |   fission cross       |
  |                       |                       |   sections / nubar    |
  |                       |                       |   for each nuclide    |
  |                       |                       | | :numref:`tab10-2-2` |
  +-----------------------+-----------------------+-----------------------+
  | pu-240                | JENDL 3.3             | Cross                 |
  |                       |                       | nuclide-to-nuclide    |
  |                       |                       | matrices present;     |
  |                       |                       | covariances due to    |
  |                       |                       | fission cross         |
  |                       |                       | sections / nubar for  |
  |                       |                       | each nuclide (\       |
  |                       |                       | :numref:`tab10-2-2`). |
  +-----------------------+-----------------------+-----------------------+
  | pu-241                | JENDL 3.3             | Cross                 |
  |                       |                       | nuclide-to-nuclide    |
  |                       |                       | matrices present;     |
  |                       |                       | covariances due to    |
  |                       |                       | fission cross         |
  |                       |                       | sections / nubar for  |
  |                       |                       | each nuclide (\       |
  |                       |                       | :numref:`tab10-2-2`). |
  +-----------------------+-----------------------+-----------------------+
  | pu-242                | ENDF/B-VI             |                       |
  +-----------------------+-----------------------+-----------------------+
  | pu-243                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pu-244                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | pu-246                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | rb-85                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | rb-86                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | rb-87                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | re-185                | ENDF/B-VI             | MT=2 added from       |
  |                       |                       | Mughabghab. LB=8      |
  |                       |                       | representation caused |
  |                       |                       | problematic           |
  |                       |                       | representation of     |
  |                       |                       | cross section         |
  |                       |                       | uncertainty due to    |
  |                       |                       | use of fine energy    |
  |                       |                       | group structure.      |
  |                       |                       | Tests were performed  |
  |                       |                       | to determine how to   |
  |                       |                       | handle this problem.  |
  |                       |                       | LB=8 data were        |
  |                       |                       | removed in the final  |
  |                       |                       | results.              |
  +-----------------------+-----------------------+-----------------------+
  | re-187                | ENDF/B-VI             | MT=2 added from       |
  |                       |                       | Mughabghab. LB=8      |
  |                       |                       | representation caused |
  |                       |                       | problematic           |
  |                       |                       | representation of     |
  |                       |                       | cross section         |
  |                       |                       | uncertainty due to    |
  |                       |                       | use of fine energy    |
  |                       |                       | group structure.      |
  |                       |                       | Tests were performed  |
  |                       |                       | to determine how to   |
  |                       |                       | handle this problem.  |
  |                       |                       | LB=8 data were        |
  |                       |                       | removed in the final  |
  |                       |                       | results.              |
  +-----------------------+-----------------------+-----------------------+
  | rh-103                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | rh-105                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ru-96                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ru-98                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ru-103                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ru-99                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ru-100                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ru-101                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ru-102                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ru-104                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ru-105                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ru-106                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | S                     | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | s-32                  | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | s-33                  | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | s-34                  | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | s-36                  | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sb-123                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sb-124                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sb-125                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sb-126                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sc-45                 | ENDF/B-VI             |                       |
  +-----------------------+-----------------------+-----------------------+
  | se-74                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | se-76                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | se-77                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | se-78                 | BLO approximate data  |                       |
  |                       | BLO approximate data  |                       |
  | se-79                 |                       |                       |
  +-----------------------+-----------------------+-----------------------+
  | se-80                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | se-82                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | Si                    | ENDF/B-VI             |                       |
  +-----------------------+-----------------------+-----------------------+
  | si-28                 | ENDF/B-VI             | Error in file         |
  |                       |                       | corrected LB=8        |
  |                       |                       | representation caused |
  |                       |                       | problematic           |
  |                       |                       | representation of     |
  |                       |                       | cross section         |
  |                       |                       | uncertainty due to    |
  |                       |                       | use of fine energy    |
  |                       |                       | group structure.      |
  |                       |                       | Tests were performed  |
  |                       |                       | to determine how to   |
  |                       |                       | handle this problem.  |
  |                       |                       | LB=8 data were        |
  |                       |                       | removed in the final  |
  |                       |                       | results.              |
  +-----------------------+-----------------------+-----------------------+
  | si-29                 | ENDF/B-VI             | Error in file         |
  |                       |                       | corrected LB=8        |
  |                       |                       | representation caused |
  |                       |                       | problematic           |
  |                       |                       | representation of     |
  |                       |                       | cross section         |
  |                       |                       | uncertainty due to    |
  |                       |                       | use of fine energy    |
  |                       |                       | group structure.      |
  |                       |                       | Tests were performed  |
  |                       |                       | to determine how to   |
  |                       |                       | handle this problem.  |
  |                       |                       | LB=8 data were        |
  |                       |                       | removed in the final  |
  |                       |                       | results.              |
  +-----------------------+-----------------------+-----------------------+
  | si-30                 | ENDF/B-VI             | Error in file         |
  |                       |                       | corrected LB=8        |
  |                       |                       | representation caused |
  |                       |                       | problematic           |
  |                       |                       | representation of     |
  |                       |                       | cross section         |
  |                       |                       | uncertainty due to    |
  |                       |                       | use of fine energy    |
  |                       |                       | group structure.      |
  |                       |                       | Tests were performed  |
  |                       |                       | to determine how to   |
  |                       |                       | handle this problem.  |
  |                       |                       | LB=8 data were        |
  |                       |                       | removed in the final  |
  |                       |                       | results.              |
  +-----------------------+-----------------------+-----------------------+
  | sm-144                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sm-147                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sm-148                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sm-149                | BLO approximate data  | Resonance range       |
  |                       |                       | uncertainty from      |
  |                       |                       | Kawano 2008           |
  +-----------------------+-----------------------+-----------------------+
  | sm-150                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sm-151                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sm-152                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sm-153                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sm-154                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sn-112                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sn-113                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sn-114                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sn-115                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sn-116                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sn-117                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sn-118                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sn-119                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sn-120                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sn-122                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sn-123                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sn-124                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sn-125                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sr-84                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sr-86                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sr-87                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sr-88                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sr-89                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | sr-90                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ta-181                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ta-182                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | tb-159                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | tb-160                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | tc-99                 | ENDF/B-VII.0          |                       |
  +-----------------------+-----------------------+-----------------------+
  | te-120                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | te-122                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | te-123                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | te-124                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | te-125                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | te-126                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | te-127m               | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | te-128                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | te-129m               | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | te-130                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | th-227                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | th-228                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | th-229                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | th-230                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | th-232                | ENDF/B-VII.0          | | Cross               |
  |                       |                       |   nuclide-to-nuclide  |
  | th-233                | BLO approximate data  |   matrices present;   |
  |                       |                       |   covariances due to  |
  | th-234                | BLO approximate data  |   fission cross       |
  |                       |                       |   sections / nubar    |
  | Ti                    | BLO approximate data  |   for each nuclide (\ |
  |                       |                       | | :numref:`tab10-2-2`)|
  | ti-46                 | BLO approximate data  |                       |
  |                       |                       | Pre-released          |
  | ti-47                 | BLO approximate data  | evaluation proposed   |
  |                       |                       | for ENDF/B-VII.1      |
  | ti-48                 | ENDF/B-VII-p          |                       |
  +-----------------------+-----------------------+-----------------------+
  | ti-49                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | ti-50                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | u-232                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | u-233                 | ENDF/B-VII-p          | Pre-released          |
  |                       |                       | evaluation proposed   |
  |                       |                       | for ENDF/B-VII.1;     |
  |                       |                       | nubar uncertainty     |
  |                       |                       | from Ref. 14Cross     |
  |                       |                       | nuclide-to-nuclide    |
  |                       |                       | matrices present;     |
  |                       |                       | covariances due to    |
  |                       |                       | fission cross         |
  |                       |                       | sections / nubar for  |
  |                       |                       | each nuclide (\       |
  |                       |                       |                       |
  |                       |                       | :numref:`tab10-2-2`). |
  +-----------------------+-----------------------+-----------------------+
  | u-234                 | SG-26                 | Thermal uncertainty   |
  |                       |                       | replaced by           |
  |                       |                       | Mughabghab value      |
  +-----------------------+-----------------------+-----------------------+
  | u-235                 | ENDF/B-VII-p          | Pre-released          |
  |                       |                       | evaluation proposed   |
  |                       |                       | for ENDF/B-VII.1;     |
  |                       |                       | nubar uncertainty     |
  |                       |                       | from JENDL-3.1 Cross  |
  |                       |                       | nuclide-to-nuclide    |
  |                       |                       | matrices present;     |
  |                       |                       | covariances due to    |
  |                       |                       | fission cross         |
  |                       |                       | sections / nubar for  |
  |                       |                       | each nuclide (\       |
  |                       |                       | :numref:`tab10-2-2`). |
  +-----------------------+-----------------------+-----------------------+
  | u-236                 | SG-26                 | Thermal uncertainty   |
  |                       |                       | replaced by           |
  |                       |                       | Mughabghab value      |
  +-----------------------+-----------------------+-----------------------+
  | u-237                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | u-238                 | ENDF/B-VII-p          | Pre-released          |
  |                       |                       | evaluation proposed   |
  | u-239                 | BLO approximate data  | for ENDF/B-VII.1      |
  |                       |                       | Cross                 |
  | u-240                 | BLO approximate data  | nuclide-to-nuclide    |
  |                       |                       | matrices present;     |
  | u-241                 | BLO approximate data  | covariances due to    |
  |                       |                       | fission cross         |
  |                       |                       | sections / nubar for  |
  |                       |                       | each nuclide (\       |
  |                       |                       | :numref:`tab10-2-2`). |
  +-----------------------+-----------------------+-----------------------+
  | V                     | ENDF/B-VII-p          | Pre-released          |
  |                       |                       | evaluation proposed   |
  |                       |                       | for ENDF/B-VII.1      |
  +-----------------------+-----------------------+-----------------------+
  | W                     | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | w-182                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | w-183                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | w-184                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | w-186                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | xe-123                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | xe-124                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | xe-126                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | xe-128                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | xe-129                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | xe-130                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | xe-131                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | xe-132                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | xe-134                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | xe-135                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | xe-136                | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | y-89                  | ENDF/B-VI             |                       |
  +-----------------------+-----------------------+-----------------------+
  | y-90                  | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | y-91                  | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | Zr                    | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | zr-90                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | zr-91                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | zr-92                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | zr-93                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | zr-94                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | zr-95                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+
  | zr-96                 | BLO approximate data  |                       |
  +-----------------------+-----------------------+-----------------------+

.. _tab10-2-7:
.. table:: Covariance data with cross correlations between nuclide reactions.
  :align: center

  +----------------+------------+----------------+------------+
  | Nuclide 1      | Reaction 1 | Nuclide 2      | Reaction 2 |
  +================+============+================+============+
  | :sup:`240`\ Pu | Fission    | :sup:`239`\ Pu | Fission    |
  +----------------+------------+----------------+------------+
  | :sup:`240`\ Pu | Fission    | :sup:`233`\ U  | Fission    |
  +----------------+------------+----------------+------------+
  | :sup:`240`\ Pu | Fission    | :sup:`238`\ U  | Fission    |
  +----------------+------------+----------------+------------+
  | :sup:`241`\ Pu | Fission    | :sup:`239`\ Pu | Fission    |
  +----------------+------------+----------------+------------+
  | :sup:`241`\ Pu | Fission    | :sup:`240`\ Pu | Fission    |
  +----------------+------------+----------------+------------+
  | :sup:`241`\ Pu | Fission    | :sup:`233`\ U  | Fission    |
  +----------------+------------+----------------+------------+
  | :sup:`241`\ Pu | Fission    | :sup:`235`\ U  | Fission    |
  +----------------+------------+----------------+------------+
  | :sup:`241`\ Pu | Fission    | :sup:`238`\ U  | Fission    |
  +----------------+------------+----------------+------------+
  | :sup:`235`\ U  | Fission    | :sup:`240`\ Pu | Fission    |
  +----------------+------------+----------------+------------+

.. bibliography:: bibs/COVLIB.bib
