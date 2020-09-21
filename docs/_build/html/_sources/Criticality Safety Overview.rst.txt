Criticality Safety Overview
===========================

**Introduction by B. T. Rearden**

SCALE provides a suite of computational tools for criticality safety
analysis that is primarily based on the KENO Monte Carlo code for
eigenvalue neutronics calculations :cite:`goluoglu_monte_2011`. Two variants of KENO provide
identical solution capabilities with different geometry packages. KENO
V.a uses a simple and efficient geometry package sufficient for modeling
many systems of interest to criticality safety and reactor physics
analysts. KENO-VI uses the SCALE Generalized Geometry Package, which
provides a quadratic-based geometry system with much greater flexibility
in problem modeling but with slower runtimes. Both versions of KENO
perform eigenvalue calculations for neutron transport primarily to
calculate multiplication factors (*k\ eff*) and flux distributions of
fissile systems in both continuous energy and multigroup modes. They are
typically accessed through the integrated SCALE sequences described
below. KENO’s grid geometry capability extends region-based features for
accumulating data for source or biasing parameter specifications, as
well as for tallying results from a calculation for visualization or
communication of data into or out of a calculation. Criticality safety
analysts may also be interested in the sensitivity and uncertainty
analysis techniques that can be applied for code and data validation as
described elsewhere in this document.

**Criticality Safety Analysis Sequences**

The Criticality Safety Analysis Sequences (CSAS) with KENO V.a (CSAS5)
and KENO-VI (CSAS6**)** provide a reliable, efficient means of
performing *k\ eff* calculations for systems routinely encountered in
engineering practice. The CSAS sequences implement XSProc to process
material input and provide a temperature and resonance-corrected cross
section library based on the physical characteristics of the problem
being analyzed. If a continuous energy cross section library is
specified, no resonance processing is needed, and the continuous energy
cross sections are used directly in KENO, with temperature corrections
provided as the cross sections are loaded.

A search capability is available with CSAS5 to find desired values of
*k\ eff* as a function of dimensions or densities. The two basic search
options offered are (1) an optimum search seeking a maximum or minimum
value of *k\ eff* and (2) a critical search seeking a fixed value of
*k\ eff*.

For continuous energy calculations, reaction rate tallies can be
requested within the CSAS input, and for multigroup calculations,
reaction rate calculations are performed using the KENO Module for
Activity-Reaction Rate Tabulation (KMART) post-processing tools. A
conversion tool is provided to up-convert KENO V.a input to KENO-VI
either as a direct KENO input (K5toK6) or, more commonly, as a CSAS
sequence (C5toC6).

**STARBUCS: Burnup-Credit Analysis Sequence**

The Standardized Analysis of Reactivity for Burnup Credit using SCALE
(STARBUCS) :cite:`gauld_starbucs_2001,radulescu_enhancements_2009` is a control module to perform
criticality calculations for spent fuel systems employing burnup credit.
STARBUCS automates the criticality safety analysis of spent fuel
configurations by coupling the depletion and criticality aspects of the
analysis, thereby eliminating the need to manually process the spent
fuel nuclide compositions into a format compatible with criticality
safety codes.

STARBUCS performs a depletion analysis calculation for each spatially
varying burnup region (if an axial or horizontal burnup profile is
specified) of a spent fuel assembly using the ORIGEN-ARP methodology of
SCALE. If a multigroup calculation is to be performed in KENO, the spent
fuel compositions are then used to generate resonance self-shielded
cross sections for each burnup-dependent fuel region. Finally, a
KENO criticality calculation is performed to determine the neutron
multiplication factor for the system.

The STARBUCS input format has been designed around the existing
depletion analysis and criticality safety sequences of SCALE. Only a
minimal amount of input beyond that typically required for a fresh-fuel
calculation is needed to perform a burnup-credit calculation.

STARBUCS was developed to facilitate studies of major burnup-credit
phenomena, such as those identified in the US Nuclear Regulatory
Commission’s *Interim Staff Guidance 8*, :cite:`us_nuclear_regulatory_commission_burnup_2012` but it is restricted to
modeling one assembly type with the same starting enrichment loaded
throughout the transportation or storage model. Greater flexibility is
available by computing individual assembly burnup compositions with the
ORIGAMI code and then creating a KENO model to implement these
compositions.

For burnup loading curve iterative calculations, STARBUCS employs the
search algorithm from CSAS5 to determine initial fuel enrichments that
satisfy a convergence criterion for the calculated *k\ eff* value of the
spent fuel configuration.

**Sourcerer: Hybrid Method for Starting Source Distribution**

As the fidelity of criticality models continues to increase, especially
for storage and transportation systems, the ability of the Monte Carlo
codes to consistently provide a converged fission source can be
challenging. Studies have shown that using a starting fission
distribution similar to the true fission distribution can reduce the
number of skipped generations required for fission source convergence,
and it can significantly improve the reliability of the final *k\ eff*
result :cite:`ibrahim_acceleration_2011`. The Sourcerer sequence applies the
Denovo :cite:`evans_denovo_2010` discrete ordinates code to generate a starting fission
source distribution in a KENO Monte Carlo calculation. The discrete
ordinates calculation is performed on a user-defined Cartesian grid
geometry where macroscopic material definitions are automatically
created from the Monte Carlo model and multigroup group cross sections
are appropriately generated.

For many criticality safety applications, the additional step of
performing a deterministic calculation to initialize the starting
fission source distribution is not necessary. However, for challenging
criticality safety analyses such as as-loaded spent nuclear fuel
transportation packages with a mixed loading of low- and high-burnup
fuel, even a low-fidelity deterministic solution for the fission source
produces more reliable results than the typical starting distributions
of uniform or cosine functions over the fissionable regions, as
demonstrated in a recent study :cite:`ibrahim_hybrid_2013`.

**Criticality Accident Alarm System Analysis with KENO and MAVRIC**

Criticality accident alarm systems (CAAS) safety analyses modeling
presents challenges because the analysis consists of a criticality
problem and a deep-penetration shielding problem :cite:`peplow_criticality_2009`. Modern codes are
typically optimized to handle one of these types of problems, but not
both. The two problems also differ in size—the criticality problem
depends on materials relatively close to the fissionable materials,
whereas the shielding problem can cover a much larger range.

CAAS analysis can be performed using the CSAS6 criticality sequence and
the MAVRIC shielding sequence. First, the fission distribution (in space
and energy) is determined via CSAS6. This information is collected on a
grid geometry that overlies the physical geometry model and is saved as
a Monaco mesh source file. The mesh source is then used as the source
term in MAVRIC. The absolute source strength is set by the user to the
total number of fissions (based on the total power released) during the
criticality excursion. MAVRIC can be optimized to calculate a specific
detector response at one location or to calculate multiple
responses/locations with roughly the same relative uncertainty.

.. bibliography:: bibs/CriticalitySafety.bib
