.. _6-0:

Snesitivity and Uncertainty Analysis Overview
=============================================

**Introduction by B. T. Rearden**

SCALE provides a suite of computational tools for sensitivity and
uncertainty analysis to (1) identify important processes in safety
analysis and design, (2) provide a quantifiable basis for neutronics
validation for criticality safety and reactor physics analysis based on
similarity assessment, and (3) quantify the effects of uncertainties in
nuclear data and physical parameters for safety
analysis. [1]_\ :sup:`,`\  [2]_

Sensitivity Analysis and Uncertainty Quantification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sensitivity analysis provides a unique insight into system performance
in that the predicted response of the system to a change in some input
process is quantified. Important processes can be identified as those
that cause the largest changes in the response per unit change in the
input. In neutron transport numerical simulations, calculating important
responses such as *k*\ :sub:`eff`, reaction rates, and reactivity coefficients
requires many input parameters, including material compositions, system
geometry, temperatures, and neutron cross section data. Because of the
complexity of nuclear data and its evaluation process, the response of
neutron transport models to the cross section data can provide valuable
information to analysts. The SCALE sensitivity and uncertainty (S/U)
analysis sequences—known as the Tools for Sensitivity and Uncertainty
Analysis Methodology Implementation (TSUNAMI)—quantify the predicted
change in *k*\ :sub:`eff`, reaction rates, or reactivity differences due to
changes in the energy-dependent, nuclide-reaction–specific cross section
data, whether continuous-energy or multigroup.

Uncertainty quantification is useful for identifying potential sources
of computational biases and highlighting parameters important to code
validation. When applying uncertainties in the neutron cross section
data, the sensitivity of the system to the cross section data can be
applied to propagate the uncertainties in the cross section data to an
uncertainty in the system response. Additionally, SCALE provides the
ability to stochastically sample uncertainties in nuclear data or any
other model input parameter (e.g., dimensions, densities, temperatures)
and propagate these input uncertainties to uncertainties not only as
traditional TSUNAMI responses of *k*\ :sub:`eff`, reaction rates, and
reactivity, but also in any general output quantity such as burnup
isotopics, dose rates, etc. Additionally, where the same input
quantities are used in multiple models, the sampling techniques can be
applied to quantify the correlation in uncertainties of multiple systems
due to the use of the same uncertain parameters across these systems.

Validation of Codes and Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Modern neutron transport codes such as the KENO Monte Carlo codes in the
SCALE code system can predict *k*\ :sub:`eff` with a high degree of precision.
Still, computational biases of one percent or more are often found when
using these codes to model critical benchmark experiments. The primary
source of this computational bias is believed to be errors in the cross
section data as bounded by their uncertainties. These errors can be
tabulated in cross section covariance data. To predict or bound the
computational bias for a design system of interest, the *American
National Standards for Nuclear Criticality Safety in Operations with
Fissionable Material Outside Reactors* (ANSI/ANS-8.1-1998) [3]_ and the
*American National Standard for Validation of Neutron Transport Methods
for Nuclear Criticality Safety Calculations* (ANSI/ANS-8.24-2007) [4]_
allow calculations to be used to determine subcritical limits for the
design of fissionable material systems. The standards require validation
of the analytical methods and data used in nuclear criticality safety
calculations to quantify any computational bias and the uncertainty in
the bias. The validation procedure must be conducted through comparison
of computed results with experimental data, and the design system for
which the subcritical limit is established must fall within the area of
applicability of the experiments chosen for validation. The ANS-8.1
standard defines the area(s) of applicability as “the limiting ranges of
material compositions, geometric arrangements, neutron-energy spectra,
and other relevant parameters (e.g., heterogeneity, leakage,
interaction, absorption, etc.) within which the bias of a computational
method is established.”

TSUNAMI Techniques for Code Validation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The TSUNAMI software provides a unique means to determine the similarity
of nuclear criticality experiments to safety applications. [5]_ The
TSUNAMI validation techniques are based on the assumption that
computational biases are primarily caused by errors in cross section
data, the potential for which are quantified in cross section covariance
data. TSUNAMI provides two methods to establish the computational bias
introduced through cross section data.

For the first method, instead of using one or more average physical
parameters to characterize a system, TSUNAMI determines the
uncertainties in the computed response that are shared between two
systems due to cross section uncertainties. These shared uncertainties
directly relate to the bias shared by the two systems. To accomplish
this, the sensitivity to each group-wise nuclide-reaction–specific cross
section is computed for all systems considered in the analysis.
Correlation coefficients are developed by propagating the uncertainties
in neutron cross section data to uncertainties in the computed response
for experiments and safety applications through sensitivity
coefficients. The bias in the experiments, as a function of correlated
uncertainty with the intended application, is extrapolated to predict
the bias and bias uncertainty in the target application. This
correlation coefficient extrapolation method is useful where many
experiments with uncertainties that are highly correlated to the target
application are available.

For the second method, data adjustment or data assimilation techniques
are applied to predict computational biases, and more general responses,
including but not limited to *k*\ :sub:`eff`, can be addressed
simultaneously.\ :sup:`5` This technique uses S/U data to identify a
single set of adjustments to nuclear data and experimental responses,
taking into account their correlated uncertainties, which would improve
the agreement between the response values from the experimental results
and computational simulations. The same data adjustments are then used
to predict an unbiased response (e.g., *k*\ :sub:`eff`) value for the
application and an uncertainty on the adjusted response value. The
difference between the originally calculated response value and the new
post-adjustment response value represents the bias in the original
calculation, and the uncertainty in the adjusted value represents the
uncertainty in this bias. If experiments are available to validate the
use of a particular nuclide in the application, the uncertainty of the
bias for this nuclide may be reduced. If similar experiments are not
available, the uncertainty in the bias for the given nuclide is high.
Thus, with a complete set of experiments to validate important
components in the application, a precise bias with a small uncertainty
can be predicted. Where the experimental coverage is lacking, a bias can
be predicted with an appropriately large uncertainty. The data
assimilation method presents many advantages over other techniques in
that biases can be projected from an agglomeration of benchmark
experiments, each of which may represent only a small component of the
bias of the target application. Also, contributors to the computational
bias can be analyzed on an energy-dependent nuclide-reaction–specific
basis. However, this technique requires additional data that are not
generally available and must be quantified or approximated by the
analyst, specifically the correlation coefficients that quantify the
relative independence of experimental measurements that use the same
equipment, whether nuclear fuel, reactivity devices, or measurement
tools.

Sensitivity and Uncertainty Analysis Tools in SCALE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **TSUNAMI-1D**, **TSUNAMI-2D** and **TSUNAMI-3D** analysis sequences
compute the sensitivity of *k*\ :sub:`eff` and reaction rates to
energy-dependent cross section data for each reaction of each nuclide in
a system model. The one-dimensional (1D) transport calculations are
performed with XSDRNPM, two-dimensional (2D) transport calculations are
preformed using NEWT, and the three-dimensional (3D) calculations are
performed with KENO V.a or KENO-VI. The Monte Carlo capabilities of
TSUNAMI-3D provide for S/U analysis from either continuous-energy or
multigroup neutron transport, where the deterministic capabilities of
TSUNAMI-1D and TSUNAMI-2D only operate in multigroup mode. SAMS
(Sensitivity Analysis Module for SCALE) is applied within each analysis
sequence to provide the requested S/U data. Whether performing a
continuous-energy or multigroup calculation, energy-dependent
sensitivity data are stored in multigroup-binned form in a sensitivity
data file (SDF) for subsequent analysis. Additionally, these sequences
use the energy-dependent cross section-covariance data to compute the
uncertainty in the response value due to the cross section-covariance
data. As TSUNAMI-2D operates as an extension of the TRITON sequence, it
is documented in the “Reactor Physics” section of this document.

**TSAR** (Tool for Sensitivity Analysis of Reactivity Responses)
computes the sensitivity of the reactivity change between two *k*\ :sub:`eff`
calculations, using SDFs from TSUNAMI-1D, TSUNAMI-2D, and/or TSUNAMI-3D.
TSAR also computes the uncertainty in the reactivity difference due to
the cross section covariance data.

**TSUNAMI-IP** (TSUNAMI Indices and Parameters) uses the SDFs generated
from TSUNAMI-1D, TSUNAMI-2D, TSUNAMI-3D, or TSAR for a series of systems
to compute correlation coefficients that determine the amount of shared
uncertainty between each target application and each benchmark
experiment considered in the analysis. TSUNAMI-IP offers a wide range of
options for more detailed assessment of system-to-system similarity.
Additionally, TSUNAMI-IP can generate input for the **USLSTATS** (Upper
Subcritical Limit Statistical Software) [6]_ trending analysis and
compute a penalty, or additional margin, needed for the gap analysis.
USLSTATS is distributed as a graphical user interface with SCALE, but
its use is documented in the TSUNAMI Primer, [7]_ not in this
documentation chapter.

**TSURFER** (Tool for S/U Analysis of Response Functions Using
Experimental Results) is a bias and bias uncertainty prediction tool
that implements the generalized linear least-squares (GLLS) approach to
data assimilation and cross section data adjustment that also uses the
SDFs generated from TSUNAMI-1D, TSUNAMI-2D, TSUNAMI-3D, or TSAR. The
data adjustments produced by TSURFER are not used to produce adjusted
cross section data libraries for subsequent use; rather, they are used
only to predict biases in application systems.

The TSUNAMI Primer also documents the use of the graphical user
interfaces for TSUNAMI, specifically ExSITE (Extensible SCALE
Intelligent Text Editor) that facilitates analysis with TSUNAMI–IP,
TSURFER, TSAR, and USLSTATS as well as VIBE (Validation, Interpretation
and Bias Estimation) for examining SDF files, creating sets of benchmark
experiments for subsequent analysis, and gathering additional
information about each benchmark experiment.

**Sampler** is a “super-sequence” that performs general uncertainty
analysis by stochastically sampling uncertain parameters that can be
applied to any type of SCALE calculation, propagating uncertainties
throughout a computational sequence. Sampler treats uncertainties from
two sources: (1) nuclear data and (2) input parameters. Sampler
generates the uncertainty in any result generated by any computational
sequence through stochastic means by repeating numerous passes through
the computational sequence, each with a randomly perturbed sample of the
requested uncertain quantities. The mean value and uncertainty in each
parameter is reported, along with the correlation in uncertain
parameters where multiple systems are simultaneously sampled with
correlated uncertainties.

Used in conjunction with nuclear data covariances available in SCALE,
Sampler is a general technique to obtain uncertainties for many types of
applications. SCALE includes covariances for multigroup neutron cross
section data, as well as for fission product yields, and radioactive
decay data, which allow uncertainty calculations to be performed for
most MG computational sequences in SCALE. At the present time, nuclear
data sampling cannot be applied to SCALE CE Monte Carlo calculations,
although the fundamental approach is still valid.

Used in conjunction with uncertainties in input data, Sampler can
determine the uncertainties and correlations in computed results due to
uncertainties in dimensions, densities, distributions of material
compositions, temperatures, or any quantities that are defined in the
user input for any SCALE computational sequence. This methodology was
developed to produce uncertainties and correlations in criticality
safety benchmark experiments, [8]_ but it has a wide range of
applications in numerous scenarios in nuclear safety analysis and
design. The input sampling capabilities of Sampler also include a
parametric capability to determine the response of a system to a
systematic variation of an input parameter.

**References**

.. [1]
   B. T. Rearden, M. L. Williams, M. A. Jessee, D. E. Mueller, and D. A.
   Wiarda, “Sensitivity and Uncertainty Analysis Capabilities and Data
   in SCALE,” *Nucl. Technol*. **174(2)**, 236–288 (2011).

.. [2]
   M. L. Williams, G. Ilas, M. A. Jessee, B. T. Rearden, D. Wiarda, W.
   Zwermann, L. Gallner, M. Klein, B. Krzykacz-Hausmann, and A. Pautz,
   “A Statistical Sampling Method for Uncertainty Analysis with SCALE
   and XSUSA,” *Nucl. Tech.* **183**, 515–526 (2013).

.. [3]
      . *American National Standard for Nuclear Criticality Safety in
      Operations with Fissionable Materials outside Reactors,*
      ANSI/ANS-8.1-1998, American Nuclear Society (1998).

.. [4]
      . *American National Standard for Validation of Neutron Transport
      Methods for Nuclear Criticality Safety Calculations,*
      ANSI/ANS-8.24-2007, American Nuclear Society (2007).

.. [5]
      . B. L. Broadhead et al., “Sensitivity- and Uncertainty-Based
      Criticality Safety Validation Techniques,” *Nucl. Sci. Eng*.
      **146**, 340–366 (2004).

.. [6]
      . J. J. Lichtenwalter et al., *Criticality Benchmark Guide for
      Light-Water-Reactor Fuel in Transportation and Storage Packages,*
      NUREG/CR-6361 (ORNL/TM-13211), Oak Ridge National Laboratory
      (1997).

.. [7]
   . B. T. Rearden, D. E. Mueller, S. M. Bowman, R. D. Busch, and S. J.
   Emerson, *TSUNAMI Primer: A Primer for Sensitivity/Uncertainty
   Calculations with SCALE*, ORNL/TM‑2009/027, Oak Ridge National
   Laboratory (2009).

.. [8]
      . W. J. Marshall and B. T. Rearden, “Determination of Experimental
      Correlations Using the Sampler Sequence within SCALE 6.2,” *ICNC
      2015*, Charlotte, NC (2015).
