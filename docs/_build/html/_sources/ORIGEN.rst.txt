.. _5-1:

Origen: Neutron Activation, Actinide Transmutation, Fission Product Generation, and Radiation Source Term Calculation
=====================================================================================================================

.. |rarr| replace:: :math:`\rightarrow`

W. Wieselquist, S. Hart, A. Isotalo [#f1]_, F. Havlůj [#f2]_,
S. Skutnik [#f3]_, R. Lefebvre, I. Gauld, D. Wiarda, J. Lefebvre,
G. Hu [#f4]_, N. Sly [#f3]_, and D. Lago [#f5]_

ABSTRACT

ORIGEN (Oak Ridge Isotope G\ eneration code) calculates time-dependent
concentrations, activities, and radiation source terms for a large
number of isotopes simultaneously generated or depleted by neutron
transmutation, fission, and radioactive decay. ORIGEN is used internally
within SCALE’s TRITON and Polaris sequences to perform depletion and
decay. As a stand-alone SCALE module, ORIGEN provides additional unique
capabilities to (1) simulate continuous nuclide feed and chemical
removal, which can be used to model reprocessing or liquid fuel systems,
and (2) generate alpha, beta, neutron and gamma decay emission spectra.
A standard decay library is provided to perform decay calculations. For
neutron activation and fuel depletion problems, neutron
spectrum-dependent ORIGEN libraries are required and may be created from
(1) user-defined spectrum and self-shielded cross sections using the
COUPLE module or (2) interpolation of existing ORIGEN reactor libraries
(precalculated by TRITON) using the Automated Rapid Processing (ARP)
module. Post-processing using the OPUS module allows calculated
isotopics and spectra to be sorted, ranked, and converted to other
units.

ACKNOWLEDGEMENTS

Development and maintenance of ORIGEN and related codes and methods have
been sponsored by many organizations including the US Nuclear Regulatory
Commission (NRC), the US Department of Energy (DOE), and nuclear power
and research institutions.

Version Information

.. centered:: Version 6.2 (2016)

**Code Responsible(s):** W. A. Wieselquist

The ORIGEN (Oak Ridge Isotope G\ eneration) code :cite:`bell_origen_1973` was developed
at Oak Ridge National Laboratory (ORNL) to calculate nuclide compositions
and radioactivity of fission products, activation products, and products
of heavy metal transmutation. Since 1991, ORIGEN has been developed as
the depletion/decay module in SCALE with support from the NRC. ORIGEN in
SCALE is the only version supported at ORNL, and it supersedes all
earlier versions. The following is a brief description of the major
enhancements in each version. Data are described in the ORIGEN Data
Resources chapter.

A major modernization effort for ORIGEN was initiated by I. Gauld in
2011 and has resulted in approximately 5 person-years of effort
refactoring the ORIGEN and related codes to be more efficient and easily
testable. The major enhancements and responsible parties are listed
below.

   -  Extensive refactor and modernization of Fortran 77 to Fortran 90+
      performed by F. Havlůj, including substantial extension of the output
      capability

   -  Implementation of an alpha and beta spectrum calculation by F. Havlůj
      and I. Gauld

   -  Introduction of C++ core data structures with Fortran bindings,
      implemented by S. Skutnik using R. Lefebvre’s C++/C/Fortran binding
      generator created for this purpose

   -  Testing suite developed by S. Skutnik, W. Wieselquist, D. Lago, and
      N. Sly

   -  Standardization of codebase while developing application programming
      interface (API) for high-performance depletion in the Consortium for
      Advanced Simulation of Light Water Reactors (CASL) and Nuclear Energy
      Advanced Modeling and Simulation (NEAMS) projects performed by W.
      Wieselquist

   -  Unification of readers/writers for ORIGEN data files developed by W.
      Wieselquist

   -  Improvement of binary formats for the ORIGEN library (f33) and ORIGEN
      concentration file (f71) by J. Lefebvre, R. Lefebvre, and W.
      Wieselquist

   -  Implementation of Chebyshev Rational Approximation Method (CRAM)
      solver by A. Isotalo

   -  Development of new input format (ORIGEN sequence only) by S. Hart and
      W. Wieselquist using the SCALE Object Notation (SON) syntax developed
      by R. Lefebvre

   -  Improvement of cubic spline interpolation scheme for ARP by S.
      Skutnik and W. Wieselquist with monotonicity fix-up determined by G.
      Hu

   -  Major revision of manuals by W. Wieselquist, combining ORIGEN, ARP,
      COUPLE, and OPUS into a single manual

Additional guidance provided by D. Wiarda and I. Gauld with testing by
J. W. Hu.

.. centered:: Version 6.1 (2011)

The following section acknowledgements appeared in the SCALE 6.1 manual.

ORIGEN


**Code Responsible(s):** I. C. Gauld

The ORIGEN code was first developed by M. J. Bell with contributions
from J. P. Nichols and other members of the Chemical Technology Division
at ORNL. Development of the ORIGEN code as a depletion module of the
SCALE code system was performed by O. W. Hermann with contributions from
R. M. Westfall, supported by the NRC.

COUPLE


**Code Responsible(s):** D. Wiarda and I. C. Gauld


The COUPLE code was originally developed by O. W. Hermann with guidance
from staff members including L. M. Petrie, N. M. Greene, W. E. Ford III,
and R. M. Westfall, who contributed greatly to formulation of the
methods, design of the data library interface with other modules, and
testing. Many valuable suggestions concerning code applications were
received from J. C. Ryman, J. R. Knight, and E. J. Allen.

ARP


**Code Responsible(s):** I. C. Gauld, S. M. Bowman, and J. E. Horwedel

The authors thank S. B. Ludwig for his support in earlier stages of this
work. The authors are grateful for the technical advice received from B.
L. Broadhead, M. D. DeHart, N. M. Greene, O. W. Hermann, C. V. Parks,
L. M. Petrie, and J. C. Ryman. The authors thank Germina Ilas and
Georgeta Radulescu for reviewing the manual and Willena Carter for
preparation of the manuscript.

OPUS


**Code Responsible(s):** I. C. Gauld and J. E. Horwedel

The work of O. W. Hermann in developing the PLORIGEN program, from which
OPUS was later developed, and the work of D. L. Barnett in developing
the original version of PlotOPUS, are acknowledged. Appreciation is
extended to J. C. Ryman for his review and testing of the program.
Finally the authors thank S. J. Poarch for formatting the manuscript.


.. [#f1] Aalto University, Finland

.. [#f2] ÚJV Řež, a. s., Czech Republic

.. [#f3] University of Tennessee, Knoxville

.. [#f4] University of Illinois, Urbana-Champaign

.. [#f5] Georgia Tech

.. _5-1-1:

Introduction
------------

ORIGEN solves the system of ordinary differential equations (ODEs) that
describe nuclide generation, depletion, and decay,

.. math::
  \frac{dN_{i}}{\text{dt}} = \sum_{j \neq i}{(l_{\text{ij}}
  \lambda_{j} + f_{\text{ij}}\sigma_{j}\Phi})N_{j}\left( t \right) -
  \left( \lambda_{i} + \sigma_{i}\Phi \right) N_{i}(t) + S_{i}(t)
  :label: eq-origen-odes

where

  - :math:`N_{i}` = amount of nuclide *i* (atoms)\ *,*

  - :math:`\lambda_{i}` = decay constant of nuclide *i* (1/s)\ *,*

  - :math:`l_{\text{ij}}` = fractional yield of nuclide *i* from decay of
    nuclide *j,*

  - :math:`\sigma_{i}` = spectrum-averaged removal cross section for
    nuclide *i* (barn)\ *,*

  - :math:`f_{\text{ij}}` = fractional yield of nuclide *i* from
    neutron-induced removal of nuclide *j*,

  - :math:`\Phi` = angle- and energy-integrated time-dependent neutron
    flux (neutrons/cm\ :sup:`2`-s), and

  - :math:`S_{i}` = time-dependent source/feed term (atoms/s).


Note that :eq:`eq-origen-odes` has no spatial dependence and can be interpreted as either
a solution at a point in space or the spatial average over some volume.
The latter interpretation is preferred here, such that :math:`\Phi` is
the spatially averaged neutron flux magnitude, and all energy-dependence
is embedded in the one-group flux-weighted average cross sections
:math:`\sigma_{i}` and reaction yields :math:`f_{\text{ij}}`. :eq:`eq-origen-odes` is
conveniently written in matrix form as

.. math::
  \frac{d\overrightarrow{N}}{dt} = \mathbf{A}
  \overrightarrow{N}\left( t \right) + \overrightarrow{S}(t)
  :label: eq-origen-tr-matrix

with a :math:`\mathbf{A}` commonly referred to as the "transition
matrix." The representation of the transition matrix as
:math:`\mathbf{A = A}_{\sigma}\Phi\mathbf{+}\mathbf{A}_{\lambda}`, where
:math:`\mathbf{A}_{\sigma}` is the part of the transition matrix
containing reaction terms and :math:`\mathbf{A}_{\lambda}` is the part
containing decay terms, is convenient, as the numerical solution of this
system of ODEs holds the reaction, flux, and feed terms constant over
step :math:`n`,

.. math::
  \frac{d\overrightarrow{N}}{\text{dt}} = \left( \mathbf
  {A}_{\sigma,n}\Phi_{n}\mathbf{+}\mathbf{A}_{\lambda} \right)
  \overrightarrow{N}\left( t \right) + {\overrightarrow{S}}_{n}
  :label: eq-origen-tr-matrix-soln

over time step :math:`t_{n - 1} \leq t \leq t_{n}.`

Adding a continuous removal process described with rate constant
:math:`\lambda_{i,rem}` simply modifies the decay constant,
:math:`\lambda_{i} \rightarrow \lambda_{i} + \lambda_{i,rem}`, whereas a
continuous feed process defines a nonzero component of the
:math:`{\overrightarrow{S}}` vector.

ORIGEN can also compute the alpha, beta, neutron, and gamma emission
spectra during decay. For the "stand-alone" ORIGEN calculations
described here, the transition matrix is loaded from an ORIGEN binary
library file (f33), which uses sparse-matrix storage to store one or
more transition matrices. The f33s may be created using COUPLE, saved
from TRITON depletion calculations, or interpolated using ARP from a set
of precompiled f33s distributed with SCALE.

Results from ORIGEN calculations may be stored on a binary concentration
file (f71), which facilitates transfer of isotopics to other codes in
SCALE. The f71 file can also store calculated emission spectra. Within
ORIGEN, the f71 can be used to restart calculations from an existing set
of compositions.

.. _5-1-2:

Methodology
-----------

This section describes the methodology used in performing the following
main functions:

  - generation of problem-dependent transition matrices,

  - solution of the system of depletion/decay equations,

  - conversion from power to flux (important for reactor applications),

  - calculation of emission spectra, and

  - interpolation of pregenerated sets of transition matrices.

.. _5-1-2-1:

Generation of Problem-dependent Transition Matrix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the transition matrix :math:`\mathbf{A}` from :eq:`eq-origen-tr-matrix`,
each matrix element :math:`a_{\text{ij}}` is the first-order rate constant for the
formation of nuclide *i* from nuclide *j* given below.

.. math::
  a_{ij} =
   \begin{cases}
   l_{ij}\lambda_{j} + f_{ij}\sigma_{j}\Phi & i \neq j \\
   \lambda_{i} - \sigma_{i} \phi & \text{otherwise}
   \end{cases}
  :label: eq-origen-trm-terms

The transition matrix coefficients for decay and reaction transitions
are stored separately and reaction transitions are always stored with
:math:`\Phi = 1` and later during solution of the system, depending on
the step-average flux level the actual transition matrix
:math:`{\mathbf{A}_{n}\mathbf{= A}}_{\sigma,n}\Phi_{n}\mathbf{+}\mathbf{A}_{\lambda}`
is reconstructed using step-average flux, :math:`\Phi_{n}`.

The decay coefficients :math:`l_{\text{ij}}\lambda_{j}` and
:math:`\lambda_{i}` are generated directly from ORIGEN decay resource
data. The reaction coefficients :math:`f_{\text{ij}}\sigma_{j}` and
:math:`\sigma_{i}` are generated using the following two-stage
procedure.

  1. Calculate all removal cross sections :math:`\sigma_{i}` and yields
     :math:`f_{\text{ij}}`, including isomeric branching ratios and
     fission yields, by folding provided flux spectrum :math:`\phi^{g}`
     with multigroup cross sections from the ORIGEN reaction resource
     and energy-dependent fission yield data from the ORIGEN yield
     resource.

  2. Overwrite specific removal cross sections and yields based on a
     provided multigroup cross section library **[SCALE Cross Section
     Libraries chapter]** and/or user-provided one-group cross sections
     and yields.


The second stage is optional, but it is important for cases which there
is significant self-shielding because ORIGEN's reaction resource assumes
infinite dilution for its multigroup data. The decay, reaction, and yeld
resources mentioned here are described in the ORIGEN Data Resources
chapter. The collapse to a one-group cross section in either stage is
given by

.. math::
  \sigma_{\text{ri}} = \frac{\sum_{g}{\sigma_{\text{ri}}^{g}\phi^{g}}}{\sum_{g}\phi^{g}}
  :label: eq-origen-collapse

for reaction type :math:`r`, nuclide :math:`i`, and provided multigroup
flux :math:`\phi^{g}`. Different reaction types are recognized by their
ENDF MT numbers [SCALE Cross Section Libraries chapter] on the
appropriate data resource For example, MT=16 is
:math:`\left( n,2n \right),` and MT=107 is
:math:`\left( n,\alpha \right)`. The removal cross section
:math:`\sigma_{i}` is simply calculated as the sum over all relevant
reactions for a particular nuclide,
:math:`\sigma_{i} = \ \sum_{r}\sigma_{\text{ri}}`. This type of
reaction-dependent multigroup data may be contained in either the data
sources available in stage 1 or 2 above. However, only two types of data
are expected to be available in stage 1 reaction resource data: (1)
isomeric branching and (2) fission yields.

The energy-dependent isomeric branching that describes the yield of each
excited level (metastable state) of a daughter nucleus is calculated in
a similar way,

.. math::
  f_{\text{rim}} = \frac{\sum_{g}{f_{\text{rim}}^{g} {\sigma_{\text{ri}}^{g}\phi}^{g}}}
                        {\sum_{g}{\sigma_{\text{ri}}^{g}\phi^{g}}}
  :label: eq-origen-meta-branching

where :math:`m` indicates the possible metastable states and the
fractions always satisfy :math:`\sum_{m}f_{\text{rim}}^{\ } = 1`.

Fission product yields are typically tabulated at discrete neutron
energies such as thermal (0.0253 eV), fission (500 keV), and high energy
(14 MeV). The yield for each fissionable nuclide is calculated in stage
1 by linearly interpolating the tabulated data using the computed
average energy of fission,

.. math::
   {\overline{E}}_{\text{fi}}  = \frac{\sum_{g}{{\overline{E}}^{g}{
   \sigma_{\text{fi}}^{g}\phi}^{g}}}{\sum_{g}{\sigma_{\text{fi}}^{g}\phi^{g}}}
   :label: eq-origen-fpy

where :math:`\sigma_{\text{fi}}^{g}` is the multigroup fission cross
section, and :math:`{\overline{E}}^{g}` is the average energy in
the group (simple midpoint energy used). In addition to generating
transition data for daughter/residual nuclides, the coefficients for
byproducts such as He-4/:math:`\alpha` byproducts from
:math:`\left( n,\alpha \right)` reactions are also retained in the
transition matrix and associated to an appropriate nuclide in the
system: hydrogen, deuterium, tritium, :sup:`3`\ He, or :sup:`4`\ He.

.. _5-1-2-2:

Solution of the Depletion/Decay Equations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ORIGEN includes two solver kernels that can solve the depletion/decay
equations of :eq:`eq-origen-tr-matrix-soln`:

  1. a hybrid matrix exponential/linear chains method (MATREX) and

  2. a Chebyshev Rational Approximation Method (CRAM).

They are described in the following sections.

.. _5-1-2-2-1:

MATREX
^^^^^^

Referring to the system of ODEs shown in :eq:`eq-origen-tr-matrix` and setting
the external feed/source :math:`S\left( t \right) = 0`, there is a formal
solution by matrix exponential (an analog to the solution of a single ODE of
this type by exponential),

.. math::
 \overrightarrow{N}\left(t \right) = \exp\left(\mathbf{A}t \right) \overrightarrow{N}\left( 0 \right)
 :label: eq-origen-homo-soln


where :math:`\overrightarrow{N}\left( 0 \right)` is a vector of initial
nuclide concentrations, by defining the series expansion of
:math:`exp(\mathbf{A}t\mathbf{)}` to be

.. math::
  \exp\left( \mathbf{A}t \right) = \mathbf{I + A}t +
  \frac{\left( \mathbf{A}t \right)^{2}}{2} + \ldots =
  \sum_{k = 0}^{\infty}\frac{\left( \mathbf{A}t \right)^{k}}{k!}
  :label: eq-origen-series-exp


with :math:`\mathbf{I}` the identity matrix. :eq:`eq-origen-homo-soln` and
:eq:`eq-origen-series-exp` describe the matrix exponential method, which
yields a complete solution to the problem. However, in certain instances
related to limitation in computer precision, difficulties occur in generating
accurate values of the matrix exponential function. Under these circumstances,
alternative procedures using either the generalized Bateman equations
:cite:`bateman_solution_1910` or Gauss-Seidel iterative techniques are applied. These
alternative procedures will be discussed in further sections.

A straightforward solution of :eq:`eq-origen-homo-soln` and
:eq:`eq-origen-series-exp` would require storage of the complete
transition matrix. To avoid excessive memory requirements, a recursion
relation has been developed. Substituting :eq:`eq-origen-series-exp` into
:eq:`eq-origen-homo-soln`,

.. math::
  \overrightarrow{N}\left( t \right)\mathbf{=}\left
  \lbrack \mathbf{I + A}t + \frac{\left( \mathbf{A}t \right)^{2}}{2}
  + \ldots \right\rbrack\overrightarrow{N}\left( 0 \right)
  :label: eq-origen-recursion

one may recognize a recursion relation for a particular nuclide,
:math:`N_{i}(t)`.

.. math::
  N_{i}\left( t \right) = N_{i}\left( 0 \right) + t\sum_{j}{a_{ij}N_{j}
  \left( 0 \right)}  + \frac{t}{2}\sum_{k}\left\lbrack a_{ik}
  t\sum_{j}{a_{kj} N_{j}\left( 0 \right)} \right\rbrack  \\
  + \frac{t}{3}\sum_{m}\left\{ a_{im} \frac{t}{2}\sum_{k}\left\lbrack a_{mk}t
  \sum_{j}{a_{kj} N_{j}\left( 0 \right)} \right\rbrack \right\} + \ldots
  :label: eq-origen-nuclide-recursion


where the range of indices, *j*, *k*, *m*, is 1 to *M* for matrix
:math:`\mathbf{A}` of size :math:`M \times M`. The result is a series of terms
that arise from the successive post-multiplication of the transition
matrix by the vector of nuclide concentration increments produced from
the computation of the previous terms. Within the accuracy of the series
expansion approximation, physical values of the nuclide concentrations
are obtained by summing a converged series of these vector terms. By
defining the terms :math:`C_{i}^{n}\left( t \right)` as

.. math::
  C_{i}^{0} = N_{i}\left( 0 \right) \\
  C_{i}^{n + 1} = \frac{t}{n + 1}\sum_{j}{a_{\text{ij}}C_{j}^{n}}
  :label: eq-origen-conc-soln-1


the solution for :math:`N_{i}\left( t \right)` is given as

.. math:: N_{i}\left( t \right) = \sum_{n = 0}^{\infty}C_{i}^{n}
   :label: eq-origen-conc-soln-2

The use of :eq:`eq-origen-conc-soln-1` and :eq:`eq-origen-conc-soln-2` requires
storage of only two vectors--:math:`{\overrightarrow{C}}^{n}` and
:math:`{\overrightarrow{C}}^{n + 1}` ----in addition to the current
value of the solution. However, the series summation solution in
:eq:`eq-origen-conc-soln-2` is not valid until a finite limit is
identified which can achieve a reasonable accuracy, i.e.,

.. math::
  N_{i}\left( t \right) = \sum_{n = 0}^{n_{\text{term}}}C_{i}^{n} + \epsilon_{\text{trunc}}
  :label: eq-origen-series-trunc

where :math:`n_{\text{term}}` is the number of terms and
:math:`\epsilon_{\text{trunc}}` is the truncation error. The key is to
split the nuclides into two sets: those that are long-lived and permit a
rapid, accurate solution via :eq:`eq-origen-series-trunc`, and those that are
short-lived and require an alternate solution.

.. _5-1-2-2-1-1:

Solution for Long-Lived Nuclides
""""""""""""""""""""""""""""""""

This section describes the various tests used to ensure that the
summations indicated in :eq:`eq-origen-series-trunc` do not lose accuracy
due to large changes in magnitudes or small differences between positive and
negative rate constants. Nuclides with large rate constants (short-lived) are
removed from the transition matrix and treated separately. For example,
in the decay chain :math:`\mathrm{A\rightarrow B \rightarrow C}`, if the
decay constant for B is large, a new rate constant is inserted in the matrix for
:math:`\mathrm{A \rightarrow C}`. This technique was originally employed by Ball
and Adams :cite:`ball_matexpgeneral_1967`. The key to determining which transitions should be
removed involves calculation of the matrix norm. The norm of matrix
:math:`\mathbf{A}` is defined by Lapidus and Luus :cite:`lapidus_optimal_1967` as being the
smaller of the maximum-row absolute sum and the maximum-column absolute sum,

.. math::
  \lbrack\mathbf{A}\rbrack = \min\left\{ {\max_{j}{\sum_{i}\left|
  a_{\text{ij}} \right|}}{,\max_{i}{\sum_{j}\left| a_{\text{ij}} \right|}\ } \right\}
  :label: eq-origen-tr-removal

To maintain precision in performing the summations of :eq:`eq-origen-series-trunc`,
the matrix norm is used to balance the user-specified time step, *t*, with
the precision associated with the word len>h employed in the machine
calculation. The constraint on the matrix norm has been chosen as

.. math::
  \left\lbrack \mathbf{A} \right\rbrack t \leq \ - 2\ \ln(0.001) = 13.8155
  :label: eq-origen-norm-constraint

The remainder of this section shows that this constraint serves two
purposes.

  - It allows reasonable accuracy for a reasonable number (20--60) of
    matrix exponential terms.

  - It defines what "short-lived" means over a particular time step,
    dictating which concentrations must be solved by alternate means.


A relationship between *m* digits of machine precision and *p*
significant digits required in all results can be stated by the
following inequality:

.. math::
 \text{(Largest term in series)} \times 10^{-m}
 \leq \text{(Series result)} \times 10^{-p}
 :label: eq-origen-precision-1

In this particular series, the relationship may be represented as

.. math::
  \max_{n}\frac{\left| \left\lbrack \mathbf{A} \right\rbrack t \right|^{n}}{n!}10^{- m}
  \leq \ e^{- \left\lbrack \mathbf{A} \right\rbrack t}10^{- p}`,
  :label: eq-origen-precision-2

or alternatively,

.. math::
  \max_{n}\frac{\left| \left\lbrack \mathbf{A} \right\rbrack t \right|^{n}}{n!}
  e^{\left\lbrack \mathbf{A} \right\rbrack t} \leq \ 10^{m - p}.
  :label: eq-origen-precision-3

Lapidus and Luus have shown that the maximum term in the summation for
any element in the matrix exponential function cannot exceed
:math:`\frac{\left( \left\lbrack \mathbf{A} \right\rbrack t \right)^{n}}{n!},\ `\ where
:math:`n` is the largest integer not larger than
:math:`\left\lbrack \mathbf{A} \right\rbrack t`. For the constraint in
:eq:`eq-origen-norm-constraint`, this yields *n*\ =13 and yields limit
:math:`\frac{\left( \left\lbrack \mathbf{A} \right\rbrack t \right)^{n}}{n!} \approx 10^{5}`.
With :math:`e^{\left\lbrack \mathbf{A} \right\rbrack t} \approx 10^{6}`
and standard double precision with *m=16*, :eq:`eq-origen-precision-3` evaluates
to :math:`10^{11} \leq 10^{16 - j}`, which indicates that five significant
figures will be maintained in values as small as 10\ :sup:`--6`. The
number of terms required to converge the matrix exponential series can
be investigated by a plot of the
:math:`\frac{\left| \left\lbrack \mathbf{A} \right\rbrack t \right|^{n}}{n!}e^{\left\lbrack \mathbf{A} \right\rbrack t}`
as a function of term index *n* in :eq:`eq-origen-precision-3`, as shown in :numref:`fig-series-conv`

.. _fig-series-conv:
.. figure:: figs/ORIGEN/fig1.png
  :align: center

  Values of terms in series for various values of the matrix norm.


The intersection between the black line in :numref:`fig-series-conv` and the
various curves indicates the number of terms needed to achieve
:math:`\epsilon_{\text{trunc}} \leq 0.1\%`. For example, with
:math:`\left\lbrack \mathbf{A} \right\rbrack t = 13.8155`,
:math:`n_{\text{term}} = 54` is required, and with
:math:`\left\lbrack \mathbf{A} \right\rbrack t = 13.8155/2`,
approximately :math:`n_{\text{term}} = 29` is required. This behavior
has been used to develop the heuristic

.. math::
  n_{\text{term}} = 7\ \lbrack\mathbf{A}\rbrack t/2 + 6.
  :label: eq-origen-solver-nterms

Thus it has been shown that the limit imposed in :eq:`eq-origen-norm-constraint` leads to a
maximum of :math:`n_{\text{term}} = 54` terms with
:math:`\epsilon_{\text{trunc}} \leq 0.1\%`.

It remains to be shown that any arbitrary system can be modified so that
it does not violate :eq:`eq-origen-norm-constraint`. Because the time step :math:`t` is
provided and fixed,
:math:`\left\lbrack \mathbf{A} \right\rbrack t \leq \ - 2\ \ln(0.001)`
cannot be satisfied unless the system is modified. The physical nature
of the system leads to
:math:`\max_{j}{\sum_{i}\left| a_{\text{ij}} \right|} \leq \max_{j}{2|a_{\text{jj}}|}`
based on production rates equal to loss rates when both parent and
daughter nuclide are included in the system. The maximum column sum in
:eq:`eq-origen-tr-removal` can then be bounded by twice the maximum diagonal term,
:math:`\max_{j}{2|a_{\text{jj}}|}`. Using this upper limit as the matrix
norm and substituting into :eq:`eq-origen-norm-constraint` yields

.. math::
   \left\lbrack \mathbf{A} \right\rbrack t \leq 2\max_{j}
   \left| a_{\text{jj}} \right| \leq - 2\ln\left( 0.001 \right)
   :label: eq-origen-sln-ineq-1


Rearranging :eq:`eq-origen-sln-ineq-1` leads to the condition

.. math::
   e^{-\|a_{jj}\|t} < 0.001
   :label: eq-origen-sln-ineq-2


which is used to mark nuclide *j* as a short-lived nuclide for this time
step, to be solved with linear chains instead of the series-based matrix
exponential. An alternative interpretation of the short-lived condition
can be made by rewriting :eq:`eq-origen-sln-ineq-2` in terms of an effective
half-life, :math:`t_{1/2} = \frac{\ln\left( 2 \right)}{|a_{\text{jj}}|}`, which
results in
:math:`t_{1/2} < \frac{{- ln}\left( 2 \right)}{\ln\left( 0.001 \right)}t \approx 0.1t`.
In other words, when a nuclide's effective half-life (including
destruction by both decay and reaction mechanisms) is less than 10% of
the time step, it can be considered short-lived.

Finally, as a note for applications where the nuclides of interest are
in long transmutation chains, it has been found that the above algorithm
may not yield accurate concentrations for those nuclides near the end of
the chain that are significantly affected by those near the beginning of
the chain. In these applications, specifying the minimum
:math:`n_{\text{term}}` as

.. math::
   n_{\text{term}} \geq \left| \Delta Z \right| + \left| \Delta A \right| + 5
   :label: eq-origen-sln-truncation


where :math:`\Delta Z` is the atomic number difference and
:math:`\Delta A` is the mass number difference, has been found to
ameliorate the issue.

.. _5-1-2-2-1-2:

Solution for Short-Lived Nuclides
"""""""""""""""""""""""""""""""""

The condition in :eq:`eq-origen-sln-ineq-2` forms the basis for declaring a
nuclide short-lived, and its solution is found via solution of the nuclide
chain equations. In conjunction with maintaining the transition matrix norm
below the prescribed level, a queue is formed of the short-lived
precursors of each long-lived isotope. These queues extend back up the
several chains to the last preceding long-lived precursor. According to
:eq:`eq-origen-sln-ineq-2`, the queues will include all nuclides whose effective
half-lives are less than 10% of the time interval. A generalized form of
the Bateman equations developed by Vondy :cite:`vondy_development_1963` is used to solve for
the concentrations of the short-lived nuclides at the end of the time step.
For an arbitrary forward-branching chain, Vondy's form of the Bateman
solution is given by,


.. math::
   N_{i}\left( t \right) = N_{i}\left( 0 \right)e^{- d_{i}t} + \sum_{k = 1}^{i - 1}
   {N_{k}(0)\left\lbrack \sum_{j = k}^{i - 1}\frac{e^{- d_{j}t}
   - e^{- d_{i}t}}{d_{i} - d_{j}}a_{j + 1,j}\prod_{\begin{matrix}
   n = k \\
   n \neq j \\
   \end{matrix}}^{i - 1}\frac{a_{n + 1,n}}{d_{n} - d_{j}} \right\rbrack}
   :label: eq-origen-vondy-soln


where :math:`N_{1}\left( 0 \right)` is the initial concentration of the
first precursor, :math:`N_{2}\left( 0 \right)` is that of the second
precursor, etc.

As in :eq:`eq-origen-trm-terms`, :math:`a_{\text{ij}}` is the first-order rate
constant, and :math:`d_{i} = {- a}_{\text{ii}}` which is the magnitude
of the diagonal element. Bell recast Vondy's form of the solution
through multiplication and division by
:math:`\prod_{n = k}^{i - 1}d_{n}` and rearranged to obtain

.. math::
   N_{i}\left( t \right) = N_{i}\left( 0 \right)e^{- d_{i}t} +
   \sum_{k = 1}^{i - 1}{N_{k}(0)\prod_{n = k}^{i - 1}\frac{a_{n + 1,n}}{d_{n}}
   \left\lbrack \sum_{j = k}^{i - 1}{d_{j}\frac{e^{- d_{j}t}
   - e^{- d_{i}t}}{d_{i} - d_{j}}}\prod_{
   \begin{matrix}
     n = k \\
     n \neq j \\
   \end{matrix}}^{i - 1}\frac{d_{n}}{d_{n} - d_{j}} \right\rbrack}
   :label: eq-origen-bell-soln


The first product over isotopes *n* is the fraction of atoms that
remains after the *k\ th* particular sequence of decays and captures. If
this product becomes less than 10\ :sup:`-6`, the contribution of this
sequence to the concentration of nuclide *i* is neglected. Indeterminate
forms that arise when *d\ i\ =d\ j* or *d\ n\ =d\ j* are evaluated using
L'Hôpital's rule. These forms occur when two isotopes in a chain have
the same diagonal element.

:eq:`eq-origen-bell-soln` is applied to calculate all contributions to the "queue
end-of-interval concentrations" of each short-lived nuclide from the
initial concentrations of all others in the queue described above. It is
also applied to calculate contributions from the initial concentrations
of all short-lived nuclides in the queue to the long-lived nuclide that
follows the queue, in addition to the total contribution to its daughter
products. These values are appropriately applied either before or after
the matrix expansion calculation is performed to correctly compute
concentrations of long-lived nuclides and the long-lived or short-lived
daughters. :eq:`eq-origen-bell-soln` is also used to adjust to certain elements
of the final transition matrix, which now excludes the short-lived
nuclides. The value of the element must be determined for the new
transition between the long-lived precursor and the long-lived daughter
of a short-lived queue. The element is adjusted so that the
end-of-interval concentration of the long-lived daughter calculated from
the single link between the two long-lived nuclides (using the new
element) is the same as what would be determined from the chain
including all short-lived nuclides. The method assumes zero
concentrations for precursors to the long-lived precursor. The computed
values asymptotically approach the correct value with successive steps
through time. For this reason, at least five to ten time intervals
during the decay of discharged fuel is reasonable, because long-lived
nuclides have built up by that time.

If a short-lived nuclide has a long-lived precursor, an additional
solution is required. First, the amount of short-lived nuclide *i* due
to the decay of the initial concentration of long-lived precursor *j* is
calculated as

.. math::
   N_{j \rightarrow i}\left( t \right) = N_{j}
   \left( 0 \right)a_{ij} \frac{e^{- d_{j}t}}{d_{i} - d_{j}}
   :label: eq-origen-lln-sln

from :eq:`eq-origen-vondy-soln`, assuming :math:`e^{- d_{i}t} \ll \ e^{- d_{j}t}`.
However, the total amount of nuclide *i* produced depends on the
contribution from the precursors of precursor *j*, in addition to that
given by :eq:`eq-origen-lln-sln`. The quantity of nuclide *j* not accounted for in
:eq:`eq-origen-lln-sln` is denoted by :math:`N_{j}'\left( t \right)`, the
end-of-interval concentration, minus the amount that would have remained
had there been no precursors to nuclide *j*:

.. math::
   N_{j}^{'\left( t \right)} = N_{j}\left( t \right) - N_{j}(0)e^{- d_{j}t}
   :label: eq-origen-lln-nef

Then the short-lived daughter and subsequent short-lived progeny are
assumed to be in secular equilibrium with their parents, which implies
that the time derivative is zero,


.. math::
   \frac{ dN_{i}}{\text{dt}} = \sum_{j}{a_{\text{ij}}N_{j}(t)} = 0.
   :label: eq-origen-sln-se

The queue end-of-interval concentrations of all the short-lived nuclides
following the long-lived precursor are augmented by amounts calculated
with :eq:`eq-origen-bell-soln`. The concentration of the long-lived precursor
used in :eq:`eq-origen-lln-nef` is that given by :eq:`eq-origen-lln-sln`.
The set of linear algebraic equations given by :eq:`eq-origen-sln-se`
is solved by the Gauss-Seidel iterative technique. This algorithm involves
an inversion of the diagonal terms and an iterated improvement of an estimate
for :math:`N_{i}(t)` through the expression

.. math::

   N_{i}^{k + 1} = - \frac{1}{a_{\text{ii}}}\sum_{j}{a_{\text{ij}}N_{j}^{k}}
   :label: eq-origen-sln-soln


Since short-lived isotopes are usually not their own precursors, this
iteration often reduces to a direct solution.

.. _5-1-2-2-1-3:

Solution of the Nonhomogeneous Equation
"""""""""""""""""""""""""""""""""""""""

The previous sections have presented the solution of the homogeneous
equation in :eq:`eq-origen-homo-soln`, applicable to fuel burnup, activation, and
decay calculations. However, the solution of a nonhomogeneous equation
is required to simulate reprocessing or other systems that require an
external feed term, :math:`S\left( t \right) \neq 0`. The nonhomogeneous
equation is given in matrix form (assumed constant over a step *n*) as


.. math::
   \frac{d\overrightarrow{N}}{\text{dt}} = \mathbf{A}
   \overrightarrow{N}\left( t \right) + {\overrightarrow{S}}
   :label: eq-origen-nhe-matrix


for a fixed feed or removal rate, :math:`{\overrightarrow{S}}`. A
particular solution of :eq:`eq-origen-nhe-matrix` will be determined and added
to the solution of the homogeneous equation given by :eq:`eq-origen-recursion`.
As before, the matrix exponential method is used for the long-lived nuclides,
and solution by linear chains is used for the short-lived nuclides. Assume
:math:`\overrightarrow{C}` an arbitrary vector with which to test a
particular solution of the form

.. math::
   \overrightarrow{N}\left( t \right) = \sum_{k = 0}^{\infty}
   \frac{\left( \mathbf{A}t \right)^{k}}{\left( k + 1 \right)!}\overrightarrow{C}t
   :label: eq-origen-nhe-matrix-soln-1


Substituting :eq:`eq-origen-nhe-matrix-soln-1` into :eq:`eq-origen-nhe-matrix`
yields

.. math::
   \sum_{k = 0}^{\infty}\frac{A^{k}t^{k}}{k!}\overrightarrow{C} = \sum_{k = 0}^{\infty}
   \frac{A^{k + 1}t^{k + 1}}{(k + 1)!}\overrightarrow{C} + \overrightarrow{S}
   :label: eq-origen-nhe-matrix-soln-2


in which the *k=0* term may be extracted from the LHS,

.. math::
   \overrightarrow{C} + \sum_{k = 1}^{\infty}
   \frac{A^{k}t^{k}}{k!}\overrightarrow{C} = \sum_{k = 0}^{\infty}
   \frac{A^{k + 1}t^{k + 1}}{\left( k+ 1 \right)!}\overrightarrow{C} + \overrightarrow{S}
   :label: eq-origen-nhe-matrix-soln-3


which allows the summations on the left and right to be easily
shown equal. This proves the particular solution is indeed
valid if the arbitrary vector is in fact the feed term
:math:`\overrightarrow{C} = \overrightarrow{S}`. The solution
to the nonhomogeneous problem is therefore (as a series),

.. math::
   \overrightarrow{N}\left( t \right) = \sum_{k= 0}^{\infty}
   \frac{\left( \mathbf{A}t \right)^{k}}{k!}\overrightarrow{N}
   \left( 0 \right) + \sum_{k = 0}^{\infty}\frac{\left( \mathbf{A}t \right)^{k}}{
   \left( k +1 \right)!}\overrightarrow{S}t
   :label: eq-origen-nhe-matrix-soln-4


For the second term in :eq:`eq-origen-nhe-matrix-soln-4`, a new recursion
relation is developed for the particular solution in the same manner as
was done for the homogeneous solution,

.. math::
   N_{i}^{P}\left( t \right) = \sum_{n = 1}^{\infty}D_{i}^{n}
   :label: eq-origen-nhe-particular-soln-1


where

.. math::
   D_{i}^{1} = S_{i}t;\ D_{i}^{n+ 1} = \frac{1}{n + 1}\sum_{j}^{\ }{a_{ij}D}_{j}^{n}
   :label: eq-origen-nhe-particular-soln-2


For the short-lived nuclides, the secular equilibrium equations are
modified to become


.. math::
   \frac{dN_{i}}{\text{dt}} =
   \sum_{j}{a_{\text{ij}}N_{j}\left( t \right) + S_{i}} = 0.
   :label: eq-origen-sln-se-eqns`


The Gauss-Seidel iterative method is applied to determine the solution.
The complete solution to the nonhomogeneous equation in
:eq:`eq-origen-nhe-matrix-soln-1` is given by the sum of the homogeneous
solutions described in previous sections and the particular solutions described
here.

.. _5-1-2-2-2:

CRAM
^^^^

The solver kernel based on the Chebyshev Rational Approximation Method
(CRAM) is described in detail in references
:cite:`pusa_computing_2010,pusa_rational_2011,isotalo_comparison_2011,pusa_numerical_2013`. Compared to the  MATREX solver,
CRAM generally has similar runtimes but is more accurate and robust on a
larger range of problems. CRAM relies on the lower upper (LU) decomposition,
so the SuperLU library has been used. The accuracy of CRAM is related to the
order, with an order 16 solution having a truncation error less than 0.01%
for all nuclides in most problems.

Unlike many methods for solving this type of system of ODEs, the len>h
of a step does not significantly affect the accuracy of CRAM. However,
any significant errors from CRAM will shrink rapidly over multiple steps
as long as there are no large changes in reaction rates. The CRAM solver
has an efficient internal substepping algorithm that can perform
multiple same-sized substeps (with the same transition matrix) very
efficiently by reusing the LU decomposition. When using internal
substepping, 2--4 substeps are typical, with a large gain in accuracy for
marginal increase in runtime.

.. _5-1-2-3:

Power Calculation
~~~~~~~~~~~~~~~~~

The following is formula is used to calculate power during irradiation
(:math:`\Phi > 0`),

.. math::
   P\left( t \right) = \sum_{i}
     {\left( \kappa_{fi} \sigma_{fi} + \kappa_{ci}
     \sigma_{ci} \right) \phi N_{i}\left( t \right)}
   :label: eq-origen-power


where :math:`\kappa_{\text{fi}}` and :math:`\kappa_{\text{ci}}` are
nuclide-dependent energy released per fission and "capture," with
*capture* defined as removal minus fission:
:math:`\sigma_{\text{ci}} = \sigma_{i} - \sigma_{\text{fi}}`. The
:math:`\sigma_{\text{fi}}` and :math:`\sigma_{\text{ci}}` terms are
extracted from the transition matrix itself, whereas the
:math:`\kappa_{\text{fi}}` and :math:`\kappa_{\text{ci}}` are available
from a separate ORIGEN energy resource (see ORIGEN Data Resources
chapter). If the flux :math:`\phi` is specified, then the power
can be calculated at any time according to :eq:`eq-origen-power`.
However in reactor fuel systems, it is convenient to be able to specify the power
produced by the system and internally to the depletion code, to convert
the power to an equivalent flux. Solving :eq:`eq-origen-power`
for the flux, however,

.. math::
   \Phi(t) = \frac{P}{\sum_{i}{{\left( \kappa_{\text{fi}}\sigma_{\text{fi}}
   + \kappa_{\text{ci}}\sigma_{\text{ci}} \right)N}_{i}\left( t \right)}}
   :label: eq-origen-flux


it is apparent that a fixed power over a time step :math:`n` does not
lead to a fixed flux, due to changing isotopics that produce different
amounts of power per fission and capture. ORIGEN performs a
flux-correction calculation to obtain an estimate of the average flux
over the step. The beginning-of-step flux is first calculated for the
initial compositions: :eq:`eq-origen-flux` is evaluated as
:math:`\Phi(t_{n - 1})`, and then :eq:`eq-origen-power` is solved
with that flux. The flux is then recalculated at the end of step :math:`\Phi(t_{n})` using
the estimated end-of-step isotopics, and the step-average flux
:math:`\Phi_{n}` is estimated as the simple average of the beginning and
end-of-step fluxes, i.e. :eq:`eq-origen-pc-flux`,

.. math::
   \Phi_{n} = 0.5\lbrack\Phi\left( t_{n} \right) +
   \Phi^{\text{pred}}\left( t_{n + 1} \right)\rbrack
   :label: eq-origen-pc-flux


noting that the "predicted" flux at end-of-step
:math:`\Phi^{\text{pred}}\left( t_{n + 1} \right)` is based on
"predicted" end-of-step isotopics, based on a beginning-of-step flux
level.

.. _5-1-2-4:

Decay Emission Sources Calculation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ORIGEN can calculate the emission sources (and spectra) during decay for
alpha, beta, neutron, and photon particles according to

.. math::
   R_{x}^{g}\left( t \right) = \sum_{i}{{\lambda_{i}N}_{i}\left( t
   \right)\int_{E^{g}}^{E^{g - 1}}{w_{i,x}\left( E \right)\text{dE}}}
   :label: eq-origen-decay


where :math:`w_{i,x}\left( E \right)` is the number of particles of type
:math::`x` emitted per disintegration of nuclide :math:`\text{i\ }`\ at
energy :math:`E`, using provided energy bins defined by energy bounds
:math:`E^{g}` to :math:`E^{g - 1},` where :math:`g` is an energy index.
The fundamental data resources for performing emission source
calculations are described in the ORIGEN Data Resources chapter.

.. _5-1-2-4-1:

Neutron Sources
^^^^^^^^^^^^^^^

Computed neutron sources include neutrons spontaneous fission, :math:`\left(\alpha,n \right)`
reactions, and delayed :math:`\left( \beta^-,n \right)` neutron emission,

.. math::
   w_{i,n}\left( E \right) = w_{i,SFn}\left( E \right) +
   w_{i,\left( \alpha,n \right)}(E) + w_{i,Dn}\left( E \right)
   :label: eq-origen-neutron

with components that will be described below. The method of computing
the spontaneous fission and delayed neutron source is independent of the
medium containing the fuel. However, :math:`\left(\alpha,n \right)` production varies
significantly with the composition of the medium. The homogeneous medium
:math:`\left(\alpha,n \right)` calculation methodology has been adopted from the Los Alamos code
SOURCES 4B :cite:`shores_data_2001,wilson_sources_2005`.

The total yield of spontaneous fission neutrons from decay of nuclide
*i* is

.. math::
   Y_{i,SFn} = \frac{\lambda_{i,SFn}}{\lambda_{i}}`
   :label: eq-origen-sfn-yield


where :math:`\frac{\lambda_{i,SFn}}{\lambda_{i}}` is the fraction of
decays which undergo spontaneous fission. The distribution of
spontaneous fission neutrons, :math:`w_{i,SFn}\left( E \right)` is given
by a Watt fission spectrum,

.. math::
   w_{i,SFn}\left( E \right) = Y_{i,SFn}\ C_{i}\ e^{- E/A_{i}}\sinh\sqrt{B_{i}E}
   :label: eq-origen-sfn-watt


where *A\ i*, *B\ i,* and *C\ i* are model parameters.

The :math:`\left(\alpha,n \right)` neutron source is strongly dependent on the low-Z content of
the medium containing the alpha-emitting nuclides and requires modeling
the slowing down of the alpha particles and the probability of neutron
production as the :math:`\alpha` particle slows down. The calculation assumes (1) a
homogeneous mixture in which the alpha-emitting nuclides are uniformly
intermixed with the target nuclides and (2) that the dimensions of the
target are much larger than the range of the alpha particles. Thus, all
alpha particles are stopped within the mixture. The yield of a
particular :math:`\alpha` is given by

.. math::
   Y^\ell_{i,\alpha} = f^\ell_{i,\ \alpha}\frac{\lambda_{i,\alpha}}{\lambda_{i}}
   :label: eq-origen-an

where :math:`\frac{\lambda_{i,\alpha}}{\lambda_{i}}` is the
relative probability of :math:`\alpha`--decay, and :math:`f^\ell_{i,\ \alpha}`
is the fraction of those :math:`\alpha`--decays producing an :math:`\alpha` particle with initial
energy :math:`E^\ell_{i,\alpha}`, and is considered fundamental
data. The *total* neutron yield from an alpha particle
:math:`\ell` emitted by nuclide *i* and interacting with target
*k* is given by the following,

.. math::
   Y^\ell_{i,k,\left( \alpha,n \right)} = Y^\ell_{i,\alpha}
   \frac{N_{k}}{N}\int_{0}^{E^\ell_{i,\alpha}}{\frac{\sigma_{k,
   \left(\alpha,n \right)}(E_{\alpha})}{S(E_{\alpha})}dE_{\alpha}\ }
   :label: eq-origen-an-alpha-per-target

where :math:`S\left( E_{\alpha} \right)` is the total stopping power of
the medium, :math:`\sigma_{k,\left( \alpha,n \right)}(E_{\alpha})` is
the :math:`\left(\alpha,n \right)` reaction cross section for target nuclide
*k*, and :math:`\frac{N_{k}}{N}` is the fraction of atoms in the medium
composed of nuclide *k*. This expression is used to calculate the neutron yield
for each target nuclide and from each discrete-energy alpha particle
emitted by all alpha-emitting nuclides in the material. The stopping
power for compounds, rather than pure elements, is approximated using
the Bragg-Kleeman additivity rule. The energy-dependent elemental
stopping cross sections are determined as parametric fits to evaluated
data. :eq:`eq-origen-an-alpha-per-target` is solved for the total
neutron yields from the alpha particle, as it slows down in the medium by
subdividing the maximum energy :math:`E^\ell_{i,\alpha}` into a number of
discrete energy bins and evaluating stopping power and
:math:`\left(\alpha,n \right)` reaction cross section at the midpoint energy of
the bin. The distribution of :math:`\left(\alpha,n \right)` neutrons as required
by :eq:`eq-origen-decay` is

.. math::
   w_{i,(\alpha,n)}\left( E \right) = \sum_{k}{\sum_{\ell \in i}
   Y^{\ell}_{i,k}\left( \alpha,n\right) X^{\ell}_{i,k}
   \left( \alpha,n \right)}\left( E \right)
   :label: eq:origen-an-dist

with the distribution of :math:`\left(\alpha,n \right)` neutrons in energy,
:math:`X^\ell_{i,k,\left( \alpha,n \right)}\left( E \right)`,
calculated using nuclear reaction kinematics, assuming that the :math:`\left(\alpha,n \right)`
reaction emits neutrons with an isotropic angular distribution in the
center-of-mass system. The maximum and minimum permissible energies of
the emitted neutron are determined by applying mass, momentum, and
energy balance for each product's nuclide energy level. The product
nuclide levels, the product level branching data, the :math:`\left(\alpha,n \right)` reaction
Q values, the excitation energy of each product nuclide level, and the
branching fraction of :math:`\left(\alpha,n \right)` reactions result in the production of
product levels. A more detailed discussion of the theory and derivation
of the kinematic equations can be found in :cite:`shores_data_2001`.

Delayed neutrons are emitted by decay of short-lived fission products.
The observed delay is due to the decay of the precursor nuclide. The
total yield of delayed neutrons from decay of nuclide *i* is

.. math::
   Y_{i,Dn} = \frac{\lambda_{i,Dn}}{\lambda_{i}}
   :label: eq-origen-dn-yield

where :math:`\frac{\lambda_{i,Dn}}{\lambda_{i}}` is the fraction of
decays which emit delayed neutrons. The delayed neutrons emitted per
decay of nuclide *i* at energy *E* is given by

.. math::
   w_{i,Dn}\left( E \right) = Y_{i,Dn} X_{i,Dn} \left( E \right)
   :label: eq-origen-dn-rate

where the spectrum :math:`X_{i,Dn}\left( E \right)` is fundamental library data.
Delayed neutrons are not important in typical spent fuel applications
due to the very short half-lives of the parent nuclides, dropping off
significantly after ~10 seconds, but they may be of value in specialized
applications where calculating time-dependent delayed neutron source
spectra is important.

.. _5-1-2-4-2:

Alpha Sources
^^^^^^^^^^^^^

An :math:`\alpha` slowing down calculation is performed as part of the :math:`\left(\alpha,n \right)` neutron
calculation. However, the alpha source (i.e. without considering slowing
down in the media) is also available, simply as the sum of delta
functions at the discrete initial alpha particle energies
:math:`w_{i,\alpha}\left( E \right) = \sum_{\ell \in i} {Y^{\ell}_{i,\alpha} \delta \left(E - E^{\ell}_{i,\alpha} \right)}`
with yields :math:`Y^{\ell}_{i,\alpha}`, as required by :eq:`eq-origen-decay`.

.. _5-1-2-4-3:

Beta Sources
^^^^^^^^^^^^

The beta source (i.e. without considering slowing down in the media) is
available as the sum of the continuous emission spectra for each
:math:`\beta^{-}` decay in nuclide *i*. The total yield of beta
particles from decay of nuclide *i* is

.. math::
 Y_{i,\beta} = \frac{\lambda_{i,\beta}}{\lambda_{i}}
 :label: eq-origen-beta-yield

where :math:`\frac{\lambda_{i,\beta}}{\lambda_{i}}` is the fraction of
decays which emit betas. The betas emitted by nuclide *i* at energy *E*
is given by

.. math::
   w_{i,\beta}\left( E \right) = Y_{i,\beta} X_{i,\beta}\left( E \right)
   :label: eq-origen-beta-rate

where the spectrum :math:`X_{i,\beta}(E)` is fundamental data,
independent of the media. The spectrum includes betas from allowed
transitions and first, second, and third forbidden transitions.

.. _5-1-2-4-4:

Photon Sources
^^^^^^^^^^^^^^

The total yield of photons from decay of nuclide *i* is

.. math::
  Y_{i,\gamma} = \frac{\lambda_{i,\gamma}}{\lambda_{i}}
  :label: eq-origen-gamma-yield

where :math:`\frac{\lambda_{i,\gamma}}{\lambda_{i}}` is the fraction of
decays which emit photons. The photons emitted by nuclide *i* at energy
*E* is given by

.. math::
   w_{i,\gamma}\left( E \right) = Y_{i,\gamma} X_{i,\gamma}\left( E \right)
   :label: eq-origen-gamma-rate

where the spectrum :math:`X_{i,\gamma}(E)` is fundamental data and
includes both line data from x-rays, gamma-rays and continuum data from
Bremsstrahlung, spontaneous fission gamma rays, and gamma rays
accompanying :math:`\left(\alpha,n \right)` reactions. The Bremsstrahlung component of the photon
source has been tabulated for various media and no on-the-fly slowing
down calculation is performed.

.. _5-1-2-5:

Library Interpolation
~~~~~~~~~~~~~~~~~~~~~

Accurate solution of fuel depletion with :eq:`eq-origen-odes` requires
coupling to self-shielding and neutron transport to accurately capture the
time-dependent change in space and energy flux distribution and 1‑group
cross sections with isotopic change. This is in generally a fairly
computationally intensive problem compared to stand-alone depletion. In
typical assembly design and analysis, the same basic assembly problem
must be solved repeatedly with variations in power history, different
periods of decay/burnup, different moderator density, etc. A question
naturally arises: could the isotopics from numerous well-constructed
cases be saved and interpolated to the actual system? Interpolating the
isotopics themselves is fraught with difficulty. For example, consider
two cases with the same burnup but different periods of decay between
cycles. A better approach---the ORIGEN Automated Rapid Processing
(ORIGEN-ARP)---was developed with the key realization that one can
reconstruct very accurate isotopics from stand-alone depletion
calculations by interpolating *transition matrices* rather than
*isotopics*.

The accuracy of the interpolation methodology compared to the coupled
transport/depletion solution (e.g., with TRITON) depends on the
suitability of the interpolation parameters and the deviation of the
desired system from the systems used to create the library. For example,
for thermal systems with uranium-based fuels, it was found that
enrichment, water density, and burnup were the dominant independent
variables and thus were best suited for interpolation. An example of the
variation of removal cross sections for key actinides is shown in
:numref:`fig-PWR-cx` for a Westinghouse 17 × 17 pressurized water reactor
(PWR) assembly type with 5% initial enrichment in :sup:`235`\ U. Each cross
section has been divided by its initial value at zero burnup to show the
variation more clearly. :sup:`240`\ Pu has been observed to have the
most variation with spectral changes, with ~60% reduction in cross
section from beginning to end of life. The variations in :sup:`240`\ Pu
with respect to enrichment and moderator density are shown in
:numref:`fig-BWR-CX-BU`, :numref:`fig-BWR-CX-mod`, :numref:`fig-BWR-CX-enr`,
and :numref:`fig-BWR-CX-BU-enr`.


.. _fig-PWR-CX:
.. figure:: figs/ORIGEN/fig2.png

   Relative removal cross section as a function of burnup for
   key actinides (Westinghouse 17 × 17 assembly with 5\\% enrichment).


.. _fig-BWR-CX-BU:
.. figure:: figs/ORIGEN/fig3.png

   :sup:`240`\ Pu-240 removal cross section as a function of
   burnup for various enrichments (GE 10 × 10 assembly).

.. _fig-BWR-CX-mod:
.. figure:: figs/ORIGEN/fig4.png

   :sup:`240`\ Pu removal cross section as a function of burnup
   for various moderator densities (GE 10 × 10 assembly).


.. _fig-BWR-CX-enr:
.. figure:: figs/ORIGEN/fig5.png

   :sup:`240`\ Pu removal cross section as a function of
   initial enrichment for various burnups (GE 10 × 10 assembly).


.. _fig-BWR-CX-BU-enr:
.. figure:: figs/ORIGEN/fig6.png

   :sup:`240`\ Pu removal cross section as a function of
   moderator density for various burnups (GE 10 × 10 assembly).

Currently there are two interpolation methods: a Lagrangian based on
low-order polynomials and a cubic spline with an optional monotonicity
fix-up.

.. _5-1-2-5-1:

Lagrangian Interpolation
^^^^^^^^^^^^^^^^^^^^^^^^

Lagrangian interpolation :cite:`funderlic_programmers_1968` seeks the unique *n-1* order polynomial
that will pass through *n*-points of the function and then interpolating
to the desired point by evaluating the polynomial,

.. math::
   y\left( x \right) = \prod_{i = 1}^{n}{\left( x - x_{i} \right)\sum_{k = 1}
   ^{n}\frac{y_{k}}{\left( x - x_{k} \right)\prod_{\begin{matrix}
   i = 1 \\
   i \neq k \\
   \end{matrix}}^{n}{(x_{k} - x_{i})}}}
   :label: eq-origen-lag-interp

where :math:`x_{i}` and :math:`y_{i}` are the known x- and y-values in
the neighborhood of the desired x-value *x*, with *n* the number of data
points/order of Lagrangian interpolation. Note that Lagrangian
interpolation is by definition *local*, involving only points in the
neighborhood of the desired value. Global alternatives such as Hermite
cubic splines use the entire data set to construct the interpolants.
Common interpolation methods based on polynomials can have difficulty
with data that vary quickly and have uneven *x‑*\ spacing, as is
expected with transition data. Polynomials tend to produce unphysical
oscillations in these cases. In cases with very small *y-*\ values
(~10\ :sup:`-10`), oscillations of the interpolant can produce negative
interpolated values.

.. _5-1-2-5-2:

Cubic Spline Interpolation
^^^^^^^^^^^^^^^^^^^^^^^^^^

Cubic spline interpolation has been observed to produce fewer, lower
frequency oscillations. Oscillations can be effectively eliminated by
enforcing monotonicity on the interpolation: that is, additional max
maxima or minima are not introduced by the interpolant between known
values of the function. Monotonic cubic splines :cite:`wolberg_energy-minimization_2002` have shown
particularly stable behavior and have been implemented as an
interpolation option.

.. _5-1-3:

ORIGEN Family of Modules
------------------------

This section describes how to perform the calculations and evaluations
described in :ref:`5-2` using the ORIGEN family of modules in SCALE.
These modules are summarized briefly below.

1. The COUPLE module is used to create ORIGEN libraries. The ORIGEN
   library contains transition matrices **A** and other relevant data in
   order to solve the depletion/decay equation of :eq:`eq-origen-odes`.
   COUPLE requires an input flux spectrum in order to perform the multigroup
   cross section collapse. Optionally, one-group self-shielded cross sections
   can be provided. Generally, in order to solve a non-decay problem, a
   library must be created with either COUPLE or ARP.

2. The ARP module is also used to create an ORIGEN library, but it is
   created by way of a special interpolation scheme on a set of existing
   libraries rather than by specifying a flux spectrum and one-group
   cross sections as in COUPLE. A set of ORIGEN libraries is distributed
   with SCALE for use with ARP and is described in ORIGEN Reactor
   Libraries chapter.

3. The ORIGEN module is used to solve depletion, decay, activation, and
   feed problems described by :eq:`eq-origen-odes`, as well as the decay
   emission calculations described by :eq:`eq-origen-decay`. For spent fuel
   calculations using the ARP interpolation methodology, it may be more
   convenient to use ORIGAMI, as described in ORIGAMI chapter.

4. The OPUS module is used to perform post processing and analysis on
   ORIGEN results contained in ORIGEN concentrations files, including
   sorting, ranking, and unit conversion.

Two types of files are an integral part of the ORIGEN family of modules:
the library file and the concentrations files.

-  The library file is a binary file, usually either with the complete
   filename “ft33f001” or with extension “.f33,” and it contains a
   collection of transition matrices **A**\ *,* usually corresponding to
   different burnups. It is typically called an “ORIGEN library,”
   “ft33,” or “f33” file.

-  The concentrations file is also a binary file, usually either with
   the complete filename “ft71f001” or with extension “.f71.” The f71 is
   a solution archive containing isotopics vectors
   :math:`{\overrightarrow{N}}_{\ }` corresponding to different
   materials or different points in time.

.. _5-1-3-1:

COUPLE Module
~~~~~~~~~~~~~

COUPLE is a coupling code that prepares the transition matrix **A** from
:eq:`eq-origen-tr-matrix`, which contains the decay and cross section
transition rate constants according to the procedures defined in
:ref:`5-1-2-1`. The transition matrix and other important data
are stored on an ORIGEN library (f33) file for use by other modules. COUPLE has
two distinct modes of operation:

  1. to create a new decay-only ORIGEN library from an ORIGEN decay
     resource, and

  2. to add new or to update existing reaction transitions yield resource,
     reaction resource, and optionally an AMPX working library containing
     multigroup cross sections.

Details on the decay, yield, and reaction resources may be found in the
ORIGEN Data Resources chapter.

.. _5-1-3-1-1:

Key Features
^^^^^^^^^^^^

This section briefly highlights some key features in COUPLE and
describes how they are used.

.. _5-1-3-1-1-1:

AMPX multi-group libraries
""""""""""""""""""""""""""

AMPX multigroup libraries contain multigroup cross sections by nuclide
and material-zone identifiers. If the working library is the result of a
multiregion transport calculation, then it is important to specify the
correct zone identifier, e.g. corresponding to the fuel in a problem
with moderator, clad, and fuel zones. The neutron flux is also stored on
the AMPX library associated with a nuclide and a zone as are the cross
sections. An AMPX library flux can be used to perform the cross section
collapse as an alternative to providing a flux spectrum in the COUPLE
input. New transitions may be added to the ORIGEN binary library for all
reactions for which there are data in the weighted AMPX library if both
the target and product nuclides are present in the ORIGEN library.

.. _5-1-3-1-1-2:

Nuclide Specification
"""""""""""""""""""""

In COUPLE, the following nuclide identifier is used:

.. code-block:: scale

   Nuclide identifier = Z \* 10000 + A \* 10 + I

where

   Z = atomic number,

   A = mass number,

   I = metastable/isomeric state (0 is ground/1 is first metastable)

Examples include 922350 for :sup:`235`\ U and 952421 for
:sup:`242m`\ Am. Note that this varies from the identifiers used in
other ORIGEN-related modules in which the isomeric state *I* comes
first, as in 1095242 for :sup:`242m`\ Am.

.. _5-1-3-1-1-3:

Adding new transitions and user-defined transitions
"""""""""""""""""""""""""""""""""""""""""""""""""""

The use of a transition matrix in ORIGEN allows any nuclide to
transition to any other nuclide. By default, when the reaction data on
the library is updated, then the transition matrix’s sparse storage is
expanded to include the new reaction transition if both the target and
the reaction product nuclide are in the library. The user may request
that the code does not add new transitions by setting Block1 ``1$$ JADD=0``.
This option ensures that the matrix structure on the input library is
identical to that of the output library. The user may explicitly set
one-group transition coefficients by setting Block1 ``1$$ LBUP=1`` and
entering Block6 and Block8 data.

.. _5-1-3-1-1-4:

Unit numbers and Aliases
""""""""""""""""""""""""

In COUPLE, a unit number is used instead of a full file name to specify
files, where unit number XY links to the data file “ftXYf001” in the
working directory. For example, unit number 33 means file ft33f001.
There are several predefined unit numbers that are controlled by a
special “origen_filenames” file, which creates an alias for the local
file “ftXYf001” to a file in the data directory. :numref:`table-couple-units`
shows the basic COUPLE unit numbers, their aliases, and a description of the
file.

.. _table-couple-units:
.. table:: Basic COUPLE unit numbers
   :widths: 8 15 40
   :align: center

   +----------+-----------+-------------------------------------------+
   | **Unit** | **Alias** | **Description**                           |
   +==========+===========+===========================================+
   | 17       | YIELDS    | ORIGEN Yield Resource                     |
   +----------+-----------+-------------------------------------------+
   | 21       | END7DEC   | ORIGEN library                            |
   |          |           |                                           |
   |          |           | *ENDF/B-VII-based decay transitions only* |
   +----------+-----------+-------------------------------------------+
   | 27       | DECAY     | ORIGEN Decay Resource                     |
   +----------+-----------+-------------------------------------------+
   | 80       | JEFF252G  | ORIGEN Reaction Resource (252 groups)     |
   +----------+-----------+-------------------------------------------+

.. _5-1-3-1-2:

Input Description
^^^^^^^^^^^^^^^^^

COUPLE uses the FIDO input system, except for title entries. The input
is arranged in blocks, with each block containing one or more arrays,
followed by the FIDO block terminator “t.” Each input parameter is named
and defined below in the order in which it appears, with the index of
the parameter in the array. Some options have been deprecated over time
and thus the first available entry may not correspond to index “1” and
some indices may be skipped. Default values are given in parentheses. In
the SCALE code system, COUPLE input appears between “=couple” and “end.”

.. _5-1-3-1-2-1:

Block1: titles, unit numbers, and case controls.
""""""""""""""""""""""""""""""""""""""""""""""""

TITLE – Title lines

   Title lines can provide information about the ORIGEN library created
   and printed when the library is used. The input Block1 ``1$$ NUMA``
   allows title lines to be copied from the input library to the output
   library.

   The first blank line terminates the title.

   A maximum of 40 lines can be included in the library.

   A special title of “DONE” in the first four columns marks the
   completion of a COUPLE input case.

0$$ Array – Logical Unit Assignments

   1. NOUT – Printed output unit number (6)

   2. LIBDEC – Unit number of ORIGEN decay resource (27)

   *Only used if 1$$ LBIN=1*

   3. JD – Unit number of ORIGEN reaction resource (80)

   4. ND – Input ORIGEN binary library file (21)

   *Only used if 1$$ LBIN=0*

   5. LD – Unit number of AMPX multigroup library file (0)

   *Only used if LD>0; energy group structure must be consistent with
   that on ORIGEN reaction resource (JD)*

   6. MD – Unit number for output ORIGEN library file (33)

   8. NY – Unit number of ORIGEN yield resource (17)

1$$ Array – Control Constants [19 entries]

   1. LBIN – 1/0 – Decay library creation/reaction update mode (0)

   *In decay library creation mode with LBIN=1, the reaction resource
   (0$$ JD) is not used, any input associated with reaction processing
   is ignored, and Block2 and Block8 may not be entered. In reaction
   update mode with LBIN=0, Block3 may not be entered.*

   2. PRT – 1/0 – Suppress all informational output / print
   informational output (0).

   3. LBUP – 1/0 – Update from user input cross sections (Block6 and
   Block8 Arrays) / no user update (0).

   4. JADD – 1/0 – Add/do not add new transitions to the library (1).

   5. JEDT – 1/0 – Edit input library only/normal library generation
   case (0).

   6. NXX – 1/0 – Allow/do not allow transitions with zero cross section
   (0).

   7. NMO – Current month (as integer) for output library (0).

   8. NDAY – Current day for output library (0).

   9. NYR – Current year for output library (two digits) (0).

   | 12. IDREF – Nuclide ID in AMPX multigroup library (0$$ LD)
     containing neutron flux weighting spectrum to use in cross section
     collapse (0).
   | *If IDREF=0, uses first nuclide found in NZONE. Only used if
     NWGT=0.*

   13. NZONE – Zone ID (usually a mixture ID) in AMPX multigroup library
   (0$$ LD)

   from which to add/update transitions (0).

   *If NZONE=0, the AMPX library must not contain zone IDs.*

   14. IEDOU – 1/0 – Edit/no edit of transition cross sections (0)

   15. NFISW – Number of nuclides with fission yields (-1)

   –1 fission yields included for all fissionable nuclides

   0 no yields added

   N input N nuclides with fission yields (Block2 7$$ Array)

   16. NUMA – Number of title lines to copy from the input ORIGEN
   library (``0$$ ND``) to the output ORIGEN library (``0$$ MD``) (0).

   18. NWGT – Flux spectrum source (0).

   0 flux spectrum from AMPX multigroup library (IDREF)

   N input N-group flux spectrum (Block2, 9*\* Array)

T – Block1 terminator.

.. _5-1-3-1-2-2:

Block2: nuclides with fission yields and weighting flux spectrum
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

This block is only read if in reaction update mode (Block1 0$$ LBIN=0).

``7$$`` Array – Nuclide IDs with fission yields [Block1 ``1$$ NFISW`` entries]

9*\* Array – Weighting flux spectrum [Block1 ``1$$ NWGT`` entries]

The flux spectrum must be given in order of descending neutron energy
according to the convention that group 1 is the highest energy group.
The group structure (number of groups and group boundaries) must be
consistent with the ORIGEN reaction resource (Block1 0$$ JD).

T – Block2 terminator.

.. _5-1-3-1-2-3:

Block3: array dimensions for decay library creation
"""""""""""""""""""""""""""""""""""""""""""""""""""

This block is only read if in decay library creation mode (Block1 0$$
LBIN=1). The default values usually apply. The values are used only
internally for memory allocation and may be set to a larger value than
is required.

3$ Array – Library constants

   18. ITMAX – Total number of nuclides in library (2600)

   19. ILMAX – Number of activation product nuclides (1000)

   –1, omits light-element library

   20. IAMAX – Number of actinide nuclides (200)

   –1, omits actinide library

   21. IFMAX – Number of fission-product nuclides (1400)

   –1, omits fission-product library

   22. IXMAX – Total number of decay transitions from one nuclide to
   another (40,000)

T – Block3 terminator.

.. _5-1-3-1-2-4:

Block6: number of user-defined transition coefficients
""""""""""""""""""""""""""""""""""""""""""""""""""""""

This block is only read if user-defined transition coefficients have
been specified in decay library creation mode (Block1 1$$ LBUP=1).

``15$$`` Array – Number of user update nuclides

   1. LBU – Total number of transitions to be entered in Block8 ``71$$``,
   ``72$$``, and ``73**`` Arrays (0)

T – Block6 terminator

.. _5-1-3-1-2-5:

Block8: user-defined transition coefficients
""""""""""""""""""""""""""""""""""""""""""""

Block8 is only required only if a nonzero value is entered in the Block6
``15$$`` array. The three arrays (``71$$``, ``72$$``, and ``73**``) represent the
parent, daughter, and coefficients for Block6 LBU user-defined
transitions, or the quantity :math:`f_{\text{ij}}\sigma_{j}` for a given
parent *j* and daughter *i* from :eq:`eq-origen-trm-terms`.

71$$ Array – Parent Nuclides [LBU entries]

   ISN1 – Parent Nuclide ID

72$$ Array – Daughter Nuclides or Reaction MT number [LBU entries]

   ISN2 – Daughter Nuclide ID for the reaction product of the
   corresponding entry in ISN1

   or reaction MT number

   .. note:: The reaction transition will be added if it does not already
     exist by setting Block1 1$$ JADD=1. Otherwise, new transitions are
     omitted.*

73*\* Array – Reaction Cross Sections [LBU entries].

   SIGMA – Reaction cross section (in barns) for the reaction described
   by ISN1 and ISN2

   There are two special rules to facilitate modifying fission cross
   sections :math:`\sigma_{\text{fj}}` and removal cross sections
   :math:`\sigma_{j}`.

   **if ISN1=ISN2,** the removal cross section is set equal to the
   corresponding SIGMA. Note that this overrides the automatic
   calculation of the removal cross section as the sum of all transition
   cross sections.

   **if ISN1=-ISN2,** the fission cross section is set equal to the
   corresponding SIGMA.

T –Block8 terminator.

**This concludes the input for a single case in COUPLE. COUPLE allows
for multiple cases in a single input and will automatically begin
processing the next case’s Block1 TITLE unless “**\ DONE” (without
quotes) is entered as the TITLE entry.

.. _5-1-3-2:

ARP Module
~~~~~~~~~~

.. _table-interp-opts:
.. table:: Interpolation options in ARP
  :widths: 25 25 50
  :align: center

  +--------------------+----------------------------+----------------------------+
  | **Type**           | **Interpolation keyword**  |  **Comments**              |
  +====================+============================+============================+
  | Nearest value      | nearest                    | Searches for closest value |
  |                    |                            | to the desired value       |
  +--------------------+----------------------------+----------------------------+
  | Linear             | linear                     | Uses nearest two values    |
  | interpolation      |                            | bounding the desired value |
  +--------------------+----------------------------+----------------------------+
  | Lagrangian         | lagrange(N)                | Uses N points near desired |
  | interpolation      |                            | value and creates a        |
  |                    |                            | polynomial of order N-1    |
  |                    | *with order N from 1 to 4* | using                      |
  |                    |                            | :eq:`eq-origen-lag-interp` |
  |                    +----------------------------+----------------------------+
  |                    | lagrange                   | The specification of       |
  |                    |                            | lagrange(1) is equivalent  |
  |                    | *same as lagrange(4)*      | to nearest and             |
  |                    |                            | lagrange(2) to linear.     |
  +--------------------+----------------------------+----------------------------+
  | Standard cubic     | stdspline                  | Standard, natural cubic    |
  | spline             |                            | spline (without            |
  |                    |                            | monotonicity fix-up).      |
  +--------------------+----------------------------+----------------------------+
  | Monotonic cubic    | spline                     | Natural cubic spline with  |
  | spline             |                            | a monotonicity fix-up      |
  |                    |                            | designed to prevent        |
  |                    |                            | nonphysical oscillations   |
  |                    |                            | that in some cases may     |
  |                    |                            | result in negative         |
  |                    |                            | interpolated cross         |
  |                    |                            | sections.                  |
  +--------------------+----------------------------+----------------------------+

Parametrizations for three types of problems have been developed:
uranium-based fuel, mixed-oxide (MOX) fuel, and general activation.

-  The parametrization for uranium-based fuel (e.g., UO\ :sub:`2`), as
   would be found in most LWRs, can interpolate on

   -  fuel enrichment,

   -  moderator density, and

   -  burnup.

-  The parametrization for MOX fuel contains a mixture of plutonium and
   uranium oxide and can interpolate on

   -  total plutonium content in the heavy metal,

   -  plutonium isotopic vector (Pu vector) that defines the relative
      concentrations of the Pu isotopes,

   -  moderator density, and

   -  burnup.

-  The parametrization for general activation problems has only
   one-dimensional interpolation on fluence.

Variation of the absorption cross sections was observed to be near
linear as a function of Pu content. Interpolation on the Pu vector is
more complex than the uranium enrichment for UO\ :sub:`2` fuel since the
vector is composed of five different isotopes: :sup:`238`\ Pu,
:sup:`239`\ Pu, :sup:`240`\ Pu, :sup:`241`\ Pu, and :sup:`242`\ Pu.
Furthermore, the elements in the vector depend on one another and can
therefore not be evaluated independently of one another since the entire
vector must sum to 100%. The scheme developed for the Pu vector was
based on an evaluation of a large database of plutonium compositions
from actual MOX fuel assemblies of European origin. It might be expect
edthat the parametrization would need to include all Pu isotopes.
However, an evaluation of the MOX fuel database indicated that there is
a strong correlation between :sup:`239`\ Pu and the other isotopes in
the vector that permits cross sections for the MOX fuel to be determined
to sufficient accuracy using only the :sup:`239`\ Pu concentration.

.. _5-1-3-2-1:

Input Description
^^^^^^^^^^^^^^^^^

ARP has a simple input scheme, a different line-by-line input expected
for each of the three problem types—uranium, MOX, or activation—with the
input required for each type shown in :numref:`table-uox-params`,
:numref:`table-mox-params`, and :numref:`table-act-params`.
Available input depends on what is available in the relevant arpdata.txt file
and the arplibs directory.

.. _table-uox-params:
.. table:: Input description for uranium fuels
  :widths: 8 22 25 45
  :align: center

  +-----------+---------------+------------------+----------------------------------------+
  | **Entry** | **Data type** | **Entry**        | **Comment**                            |
  |           |               |                  |                                        |
  | **#**     |               | **requirements** |                                        |
  +===========+===============+==================+========================================+
  | 1         | Data set name | Line 1           |  Enter a uranium CONFIGNAM             |
  |           |               | always           |  from the active arpdata.txt           |
  |           |               | required         |                                        |
  |           |               |                  |  (see :numref:`table-arpdata-uox`).    |
  +-----------+---------------+------------------+----------------------------------------+
  | 2         | Enrichment    | New line         |  Enter the wt %                        |
  |           |               | always           |  :sup:`235`\ U in toal U               |
  +-----------+---------------+------------------+----------------------------------------+
  | 3         | Number of     |    Always        |  Enter the number of                   |
  |           | cycles        |                  |  irradiation cycles                    |
  |           |               |                  |  :math:`N`.                            |
  +-----------+---------------+------------------+----------------------------------------+
  | 4         | Fuel          |    Always        |  Enter the irradiation time            |
  |           | irradiation   |                  |  for each cycle in days                |
  |           | period        |                  |  :math:`\Delta T_{i}`,                 |
  |           |               |                  |  for                                   |
  |           |               |                  |  :math:`i = 1,\ 2,\ldots,N`.           |
  +-----------+---------------+------------------+----------------------------------------+
  | 5         | Average power |    Always        | Enter the specific fission             |
  |           |               |                  | power (MW/MTHM) for each               |
  |           |               |                  | cycle :math:`P_{i}`,                   |
  |           |               |                  | for                                    |
  |           |               |                  | :math:`i = 1,\ 2,\ldots,N`.            |
  +-----------+---------------+------------------+----------------------------------------+
  | 6         | Data          |    Always        | Enter the nummber of cross             |
  |           | interpolations|                  | section sets to interpolate            |
  |           | per cycle     |                  | during each cycle                      |
  |           |               |                  | :math:`m_{i}`, for                     |
  |           |               |                  | :math:`i = 1,\ 2,\ldots,N`.            |
  +-----------+---------------+------------------+----------------------------------------+
  | 7         | Moderator     |    Always        | Enter the moderator density            |
  |           | density       |                  | (g/cm\ :sup:`3`).                      |
  |           |               |                  |                                        |
  |           |               |                  | Enter only one value                   |
  +-----------+---------------+------------------+----------------------------------------+
  | 8         | New library   | New line         | Enter the filename of the              |
  |           | name          |                  | new ORIGEN library created             |
  |           |               | always           | from interpolation.                    |
  +-----------+---------------+------------------+----------------------------------------+
  | 9         | Interpolation |    Optional      | Enter the interpolation algorithm      |
  |           | keyword       |                  | which will be used from                |
  |           |               |                  | :numref:`table-interp-opts`            |
  |           |               |                  |                                        |
  |           |               |                  | (**DEFAULT: spline**)                  |
  +-----------+---------------+------------------+----------------------------------------+

.. _table-mox-params:
.. table:: Input description for MOX fuels
  :widths: 8 22 25 45
  :align: center

  +-----------+----------------------+------------------+----------------------------------------+
  | **Entry** | **Data type**        | **Entry**        | **Comment**                            |
  |           |                      |                  |                                        |
  | **#**     |                      | **requirements** |                                        |
  +===========+======================+==================+========================================+
  | 1         | Data set name        | Line 1           | Enter a MOX CONFIGNAM                  |
  |           |                      |                  | from the active arpdata.txt            |
  |           | *(starts with MOX)*  | Always           |                                        |
  |           |                      | required         | (see :numref:`table-arpdata-mox`)      |
  +-----------+----------------------+------------------+----------------------------------------+
  | 2         | Plutonium content    | New line         | Enter the Pu content                   |
  |           |                      |                  | as wt % Pu in total                    |
  |           |                      | always           | heavy metal.                           |
  +-----------+----------------------+------------------+----------------------------------------+
  | 3         | :sup:`239`\ Pu       | Always           | Enter the :sup:`239`\ Pu               |
  |           | isotopic vector      |                  | isotopic concentration as              |
  |           |                      |                  | wt % :sup:`239`\ Pu in total           |
  |           |                      |                  | Pu.                                    |
  +-----------+----------------------+------------------+----------------------------------------+
  | 4         | Reserved parameter   | Always           | Enter a dummy value                    |
  |           | (not used)           |                  | (e.g., 1.0)                            |
  +-----------+----------------------+------------------+----------------------------------------+
  | 5         | Number of cycles     | Always           |  Enter the number of                   |
  |           |                      |                  |  irradiation cycles                    |
  |           |                      |                  |  :math:`N`.                            |
  +-----------+----------------------+------------------+----------------------------------------+
  | 6         | Fuel irradiation     | Always           | Enter the irradiation                  |
  |           | period (days)        |                  | time for each cycle                    |
  |           |                      |                  | days                                   |
  |           |                      |                  | :math:`\Delta T_{i}`,                  |
  |           |                      |                  | for                                    |
  |           |                      |                  | :math:`i = 1,\ 2,\ldots,N`.            |
  +-----------+----------------------+------------------+----------------------------------------+
  | 7         | Average power        | Always           | Enter the specific fission             |
  |           | (MW/MTHM)            |                  | power (MW/MTHM) for each               |
  |           |                      |                  | cycle, :math:`P_{i}`, for              |
  |           |                      |                  | :math:`i = 1,\ 2,\ldots,N`.            |
  +-----------+----------------------+------------------+----------------------------------------+
  | 8         | Data interpolations  | Always           | Enter the number of cross              |
  |           | per cycle            |                  | section sets to interpolate            |
  |           |                      |                  | during each cycle,                     |
  |           |                      |                  | :math:`m_{i}` for                      |
  |           |                      |                  | :math:`i = 1,\ 2,\ldots,N`.            |
  +-----------+----------------------+------------------+----------------------------------------+
  | 9         | Moderator            | Always           |  Enter the water moderator             |
  |           | density              |                  |  density (g/cm\ :sup:`3`).             |
  |           |                      |                  |                                        |
  |           |                      |                  |  Enter only one value.                 |
  +-----------+----------------------+------------------+----------------------------------------+
  | 10        | New library name     |  New line        | Enter the name of the new interpolated |
  |           |                      |  always          | library created by ARP.                |
  +-----------+----------------------+------------------+----------------------------------------+
  | 11        | Interpolation        |    Optional      | Enter the interpolation algorithm      |
  |           | keyword              |                  | which will be used from                |
  |           |                      |                  | :numref:`table-interp-opts`            |
  |           |                      |                  |                                        |
  |           |                      |                  | (**DEFAULT: spline**)                  |
  +-----------+----------------------+------------------+----------------------------------------+




.. _table-act-params:
.. table:: Input description for activaiton problems
  :widths: 8 22 25 45
  :align: center

  +-----------+---------------------+------------------+----------------------------------------+
  | **Entry** | **Data type**       | **Entry**        | **Comment**                            |
  | **no.**   |                     | **requirements** |                                        |
  +===========+=====================+==================+========================================+
  | 1         | Data set name       |    Line 1        | Enter an activation                    |
  |           |                     |    always        | CONFIGNAM from the active              |
  |           |                     |    required      | arpdata.txt                            |
  |           | *(starts with ACT)* |                  |                                        |
  |           |                     |                  | see :numref:`table-arpdata-act`        |
  +-----------+---------------------+------------------+----------------------------------------+
  | 2         | Dummy parameter     |    Always        | Enter 1.                               |
  +-----------+---------------------+------------------+----------------------------------------+
  | 3         | Number of cycles    |    Always        | Enter the number of                    |
  |           |                     |                  | irradiation cycles                     |
  |           |                     |                  | :math:`N`.                             |
  +-----------+---------------------+------------------+----------------------------------------+
  | 4         | Fuel irradiation    |    Always        | Enter the irradiation time for each    |
  |           | period              |                  | cyce time in days :math:`\Delta T_{i}`,|
  |           |                     |                  | :math:`i = 1,\ 2,\ldots,N`.            |
  +-----------+---------------------+------------------+----------------------------------------+
  | 5         | Average neutron     |    Always        | Enter the average flux level           |
  |           | flux                |                  | (n/cm\ :sup:`2`-s) for each cycle,     |
  |           |                     |                  | :math:`\Phi_{i}`, for                  |
  |           |                     |                  | :math:`i = 1,\ 2,\ldots,N`.            |
  +-----------+---------------------+------------------+----------------------------------------+
  | 6         | Data                |    Always        | Enter the number of cross section sets |
  |           | interpolations      |                  | to interpolate during each cycle,      |
  |           | per cycle           |                  | :math:`m_{i}`, for                     |
  |           |                     |                  | :math:`i = 1,\ 2,\ldots,N`.            |
  +-----------+---------------------+------------------+----------------------------------------+
  | 7         | Flux type (flag)    | Always           | Enter 1.                               |
  +-----------+---------------------+------------------+----------------------------------------+
  | 8         | New library name    |  New line        | Enter the name of the new interpolated |
  |           |                     |  always          | library created by ARP.                |
  +-----------+---------------------+------------------+----------------------------------------+
  | 9         | Interpolation       |    Optional      | Enter the interpolation algorithm      |
  |           | keyword             |                  | which will be used from                |
  |           |                     |                  | :numref:`table-interp-opts`            |
  |           |                     |                  |                                        |
  |           |                     |                  | (**DEFAULT: spline**)                  |
  +-----------+---------------------+------------------+----------------------------------------+

.. _5-1-3-2-2:

ARPDATA.TXT listing file
^^^^^^^^^^^^^^^^^^^^^^^^

In addition to the user input file, ARP also reads a file named
arpdata.txt when it runs. This file describes the parametrization of the
ORIGEN libraries. The file is required because the cross section
libraries contain no imbedded information on the reactor type, fuel
type, or irradiation conditions. Both the file arpdata.txt and the
directory of ORIGEN libraries named arplibs is searched for, first in
the working directory so that a user can override the default libraries,
and then to the SCALE data directory. An example arpdata.txt file is
shown in :numref:`fig-arpdata`

.. code-block:: none
  :caption: Examples of arpdata.txt entries.
  :name: fig-arpdata

   !ce14x14
   6 1 11
   1.5 2.0 3.0 4.0 5.0 6.0
   0.7332
   'ce14_e15.f33' 'ce14_e20.f33' 'ce14_e30.f33'
   'ce14_e40.f33' 'ce14_e50.f33' 'ce14_e60.f33'
   0. 1500. 4500. 7500. 10500. 13500.
   16500. 31500. 46500. 58500. 70500.


   !mox_bw15x15
   3 5 1 1 10
   4.0000 7.0000 10.0000
   50.0000 55.0000 60.0000 65.0000 70.0000
   1.0
   0.7135
   'mox_bw15_e40v50.f33' 'mox_bw15_e70v50.f33' 'mox_bw15_e10v50.f33'
   'mox_bw15_e40v55.f33' 'mox_bw15_e70v55.f33' 'mox_bw15_e10v55.f33'
   'mox_bw15_e40v60.f33' 'mox_bw15_e70v60.f33' 'mox_bw15_e10v60.f33'
   'mox_bw15_e40v65.f33' 'mox_bw15_e70v65.f33' 'mox_bw15_e10v65.f33'
   'mox_bw15_e40v70.f33' 'mox_bw15_e70v70.f33' 'mox_bw15_e10v70.f33'
   0.00 1040.00 3000.00 5000.00 7500.00


   !w17x17
   6 1 11
   1.5 2.0 3.0 4.0 5.0 6.0
   0.723
   'w17_e15.f33' 'w17_e20.f33' 'w17_e30.f33'
   'w17_e40.f33' 'w17_e50.f33' 'w17_e60.f33'
   0. 1500. 4500. 7500. 10500. 13500.
   16500. 31500. 46500. 58500. 70500.


As shown in :numref:`Example %s, <fig-arpdata>` the arpdata.txt is simply
a list of entries, each beginning with a "!CONFIGNAM," where CONFIGNAM is
the name to be used to reference the entire data set. Whether the entry is for a
uranium, MOX, or activation problem is dictated by the actual CONFIGNAM.
If it begins with MOX, it is a MOX entry, and if it begins with ACT, it
is an activation entry. Otherwise it is uranium. The ORIGEN libraries
listed must reside next to arpdata.txt, in a directory called arplibs.
Each type of entry is described fully in :numref:`table-arpdata-uox`,
:numref:`table-arpdata-mox`, and :numref:`table-arpdata-act` for uranium,
MOX, and activation, respectively.

.. _table-arpdata-uox:
.. table:: ARPDATA.TXT uranium-type entry
  :widths: 8 22 25 45
  :align: center

  +----------+---------------+------------------+--------------------------------+
  | **Line** | **Data name** | **Desccription** | **Comments**                   |
  | **no.**  |               |                  |                                |
  +==========+===============+==================+================================+
  | 1        | CONFIGNAM     | Data set name    | Must begin with "!" in column  |
  |          |               +------------------+ one, followed by the           |
  |          |               | (40-character    | alphanumeric name this data    |
  |          |               | maximum)         | will be referenced by.         |
  |          |               |                  +--------------------------------+
  |          |               |                  | May not begin with ACT or MOX  |
  +----------+---------------+------------------+--------------------------------+
  | 2        | N1            | Number of        | Entries pertain to the number  |
  |          |               | enrichments      | of parameterized cross section |
  |          +---------------+------------------+ data points for each variable  |
  |          | N2            | Number of water  | type.                          |
  |          |               | densities        |                                |
  |          +---------------+------------------+                                |
  |          | N3            | Number of        |                                |
  |          |               | burnup steps     |                                |
  +----------+---------------+------------------+--------------------------------+
  | 3        | ENR           | Enrichment       | N1 entries defining the        |
  |          |               | values (wt %     | discrete enrichment values for |
  |          |               | :sup:`235`\ U);  | each library                   |
  |          |               | values at which  |                                |
  |          |               | ARP libraries    |                                |
  |          |               | were generated   |                                |
  +----------+---------------+------------------+--------------------------------+
  | 4        | DENS          | Water density    | N2 entries defining the        |
  |          |               | values           | discrete moderator density     |
  |          |               | (g/cm\ :sup:`3`) | values for each library        |
  +----------+---------------+------------------+--------------------------------+
  | 5        | FILES         | Filenames of     | N1 × N2 entries                |
  |          |               | ORIGEN libraries |                                |
  |          |               | for this fuel    |                                |
  |          |               | assembly type    |                                |
  |          |               +------------------+--------------------------------+
  |          |               | (Enclose each    | Filenames are ordered first by |
  |          |               | filename in      | density values, then by        |
  |          |               | single quotes    | enrichment values.             |
  |          |               | with at least    |                                |
  |          |               | one space        |                                |
  |          |               | between each     |                                |
  |          |               | name.)           |                                |
  +----------+---------------+------------------+--------------------------------+
  | 6        | BURN          | Burnups          | N3 entries                     |
  |          |               | (MWd/MTU)        +--------------------------------+
  |          |               | corresponding    | Each set of burnup-dependent   |
  |          |               | to each position | cross sections is stored       |
  |          |               | on the ORIGEN    | withinn a single ORIGEN binary |
  |          |               | library          | library file (the first burnup |
  |          |               |                  | is usually zero).              |
  +----------+---------------+------------------+--------------------------------+
  | **NOTE:** Repeat all of the above entries for each fuel assembly             |
  | configuration type                                                           |
  +------------------------------------------------------------------------------+


.. _table-arpdata-mox:
.. table:: ARPDATA.TXT MOX-type entry
  :widths: 8 22 25 45
  :align: center

  +----------------+---------------+-----------------+----------------+
  | **Line no**    | **Data name** | **Description** | **Comments**   |
  +================+===============+=================+================+
  | 1              | CONFIGNAM     | Data set name   | Must begin     |
  |                |               +-----------------+ with "!" in    |
  |                |               | (40-character   | column one,    |
  |                |               | maximum)        | followed by    |
  |                |               |                 | the            |
  |                |               |                 | alphanumeric   |
  |                |               |                 | name by which  |
  |                |               |                 | this data set  |
  |                |               |                 | will be        |
  |                |               |                 | referenced.    |
  |                |               |                 +----------------+
  |                |               |                 | Must begin     |
  |                |               |                 | with MOX       |
  |                |               |                 | (e.g.,         |
  |                |               |                 | !mox_bw15x15). |
  +----------------+---------------+-----------------+----------------+
  | 2              | N1            | Number of Pu    | Entries        |
  |                |               | content values  | pertain to the |
  |                +---------------+-----------------+ number of      |
  |                | N2            | Number of       | separate cross |
  |                |               | :sup:`239`\ Pu  | section sets   |
  |                |               | values          | generated for  |
  |                +---------------+-----------------+ each           |
  |                | N3            | Not used        | parameter.     |
  |                |               | (enter 1)       |                |
  |                +---------------+-----------------+                |
  |                | N4            | Number of       |                |
  |                |               | water           |                |
  |                |               | densities       |                |
  |                +---------------+-----------------+                |
  |                | N5            | Number of       |                |
  |                |               | burnup steps    |                |
  +----------------+---------------+-----------------+----------------+
  | 3              | PU            | Pu content      | N1 entries     |
  |                |               | values          |                |
  |                |               | (wt % Pu in     |                |
  |                |               | heavy metal)    |                |
  +----------------+---------------+-----------------+----------------+
  | 4              | VECT          | :sup:`239`\ Pu  | N2 entries     |
  |                |               | vector values   |                |
  |                |               | (wt % :sup:`239`\ Pu/Pu) |       |
  +----------------+---------------+-----------------+----------------+
  | 5              | RESRV         | Not used        | N3 entries;    |
  |                |               | (enter 1)       | dummy entry    |
  |                |               |                 | required.      |
  +----------------+---------------+-----------------+----------------+
  | 6              | DENS          | Water density   | N4 entries     |
  |                |               | values          |                |
  |                |               | (g/cm\ :sup:`3`) |               |
  +----------------+---------------+-----------------+----------------+
  | 7              | FILE          | Filenames of    | N1 × N2 × N3 × |
  |                |               | ORIGEN          | N4 entries     |
  |                |               | libraries for   +----------------+
  |                |               | this fuel       | Increment FILE |
  |                |               | assembly type.  | names in the   |
  |                |               | Enclose each    | order of N1,   |
  |                |               | filename in     | then N2, then  |
  |                |               | single quotes   | N3, and then   |
  |                |               | with at least   | N4 values      |
  |                |               | one space       |                |
  |                |               | between each    |                |
  |                |               | name.           |                |
  +----------------+---------------+-----------------+----------------+
  | 8              | BURN          | Burnups         | N5 entries     |
  |                |               | (MWd/MTU)       +----------------+
  |                |               | corresponding   | (first burnup  |
  |                |               | to each         | is usually     |
  |                |               | position on     | zero)          |
  |                |               | the ORIGEN      |                |
  |                |               | library         |                |
  +----------------+---------------+-----------------+----------------+
  | **NOTE:** Repeat all of the above entries for each fuel assembly  |
  | configuration type                                                |
  +-------------------------------------------------------------------+

.. _table-arpdata-act:
.. table:: ARPDATA.TXT activation-type entry
  :widths: 8 22 25 45
  :align: center

  +----------------+---------------+-----------------+--------------------------+
  | **Line no.**   | **Data name** | **Description** | **Comments**             |
  +================+===============+=================+==========================+
  | 1              | CONFIGNAM     | Data set name   | Must begin in colummn    |
  |                |               +-----------------+ one followed by the      |
  |                |               | (40-character   | alphanumeric name by     |
  |                |               | maximum)        | which this data set will |
  |                |               |                 | referenced.              |
  |                |               |                 +--------------------------+
  |                |               |                 | Must begin with ACT      |
  |                |               |                 | (e.g., !actcntlrod).     |
  +----------------+---------------+-----------------+--------------------------+
  | 2              | N1            | Reserved        | The first two entries    |
  |                |               | (enter 1)       | pertain to the number of |
  |                +---------------+-----------------+ separate cross section   |
  |                | N2            | Not used        | sets generated for each  |
  |                |               | (enter 1)       | variable parameter.      |
  |                +---------------+-----------------+--------------------------+
  |                | N3            | Number of       | These are usually set to |
  |                |               | fluence values  | 1.                       |
  |                |               +-----------------+--------------------------+
  |                |               |                 | The variable N3          |
  |                |               |                 | corresponds to the       |
  |                |               |                 | number of                |
  |                |               |                 | fluence-dependent        |
  |                |               |                 | cross section sets       |
  |                |               |                 | available in the library.|
  +----------------+---------------+-----------------+--------------------------+
  | 3              | RESRV         | Not used        | Enter 1.                 |
  |                |               | (enter 1)       |                          |
  +----------------+---------------+-----------------+--------------------------+
  | 4              | FTYPE         | Neutron flux    | Enter 1.                 |
  |                |               | type (flag)     |                          |
  +----------------+---------------+-----------------+--------------------------+
  | 5              | FILES         | Filenames of    | Generally only one       |
  |                |               | ORIGEN          | one library name is      |
  |                |               | library.        | required.                |
  |                |               | Enclose         |                          |
  |                |               | filename in     |                          |
  |                |               | single quotes.  |                          |
  +----------------+---------------+-----------------+--------------------------+
  | 6              | FLUENCE       | Neutron         | N3 entries               |
  |                |               | fluence values  +--------------------------+
  |                |               | (n/cm\ :sup`2`) | **The fluence values**   |
  |                |               | at each of the  | **are reduced by the**   |
  |                |               | ORIGEN          | **factor**               |
  |                |               | libraries       | :math:`10^{-24}`         |
  |                |               |                 | **to avoid numerical**   |
  |                |               |                 | **problems during the**  |
  |                |               |                 | **interpolation**        |
  |                |               |                 +--------------------------+
  |                |               |                 | (First value is usually  |
  |                |               |                 | zero.)                   |
  +----------------+---------------+-----------------+--------------------------+
  | **NOTE:** Repeat all of the above entries for each fuel assembly            |
  | configuration type                                                          |
  +-----------------------------------------------------------------------------+

.. _5-1-3-3:

ORIGEN Module
~~~~~~~~~~~~~

. include:: <isonum.txt>

The ORIGEN module drives depletion, decay, and activation calculations
as described in :ref:`5-1-2-4`, including
the conversion of generated powers to fluxes described in
:ref:`5-1-2-3`, as well as alpha, beta, gamma, and neutron
source calculations described in :ref:`5-1-2-4`.

.. _5-1-3-3-1:

Key Features
^^^^^^^^^^^^

This section briefly highlights some key features in ORIGEN and describes how they are used.

.. _5-1-3-3-1-1:

Nuclide Specification and ORIGEN Sub-libraries
""""""""""""""""""""""""""""""""""""""""""""""

The nuclide identifiers in ORIGEN are more flexible than those in other
modules of SCALE and even within the ORIGEN family.
:numref:`table-origen-nuc-spec` shows the possible ways to
specify nuclides (and elements).

.. _table-origen-nuc-spec:
.. table:: Nuclide / element specification in ORIGEN
  :widths: 30 35 10 5 10
  :align: center

  +-------------------------------+----------------------+----------------+--------+-----------+
  | **Identifier Form**           | **Comments**         | **Examples**                        |
  |                               |                      +                                     +
  |                               |                      | *nuclide*       |rarr|   *input id* |
  +-------------------------------+----------------------+----------------+--------+-----------+
  | IZZZAAA                       | Standard numeric     | :sup:`235`\ U   |rarr|       92235  |
  |                               | identifier with one  +                                     +
  |    I – *isomeric state*       | optional digit of    | :sup:`235m`\ U  |rarr|    10992235  |
  |                               | isomeric state,      |                                     |
  |    ZZZ – *atomic nummber*     | three digits of      +                                     +
  |                               | atomic number, three | :sup:`135`\ Xe  |rarr|      54135   |
  |                               | digit of mass        +                                     |
  |    AAA – *mass number*        | number; elements     | :sup:`1`\ H     |rarr|       1001   |
  |                               | have mass number of  +                                     |
  |                               | 000.                 | :sup:`10`\ B    |rarr|       5010   |
  |                               |                      +                                     +
  |                               |                      | Fe              |rarr|      54000   |
  +-------------------------------+----------------------+---------------+---------+-----------+
  | EAm                           | Standard symbolic    | :sup:`235`\ U   |rarr|    u235      |
  |                               | identifier with      +                                     +
  |    E – *element symbol*       | element symbol       | :sup:`235m`\ U  |rarr|    u235m     |
  |                               | followed by mass     +                                     +
  |    A – *mass number*          | number, followed by  | :sup:`135`\ Xe  |rarr|    xe135     |
  |                               | optional metastable  +                                     +
  |    m – *metastable indicator* | indicator; can       | :sup:`1`\ H     |rarr|    h1        |
  |                               | include a dash       +                                     +
  |                               | between E and A      | :sup:`10`\ B    |rarr|    b10       |
  |                               | (E-Am); case         +                                     +
  |                               | insensitive.         | Fe              |rarr|    fe        |
  +-------------------------------+----------------------+---------------+---------+-----------+

One important aspect ORIGEN users must be aware of is that the ORIGEN
library (f33) being used dictates the set of nuclides available in a
calculation and that there may be more than one *version* of a nuclide
in a library. The duplicates arise in large part from the need to
analyze fission products separately. For example, a gadolinia-doped
uranium oxide fuel with burnup will have some :sup:`155`\ Gd from the
initial gadolinia loading and some :sup:`155`\ Gd generated as a fission
product. Although these fuels physically behave the same way, it is
sometimes important to be able to analyze them separately. These groups,
versions, or categories are referred to as sublibraries because in an
ORIGEN library, they appear almost like three separate, smaller ORIGEN
libraries. The three libraries are for

  1. naturally occurring, light nuclides, sometimes called "light
     elements" or "activation products,"

  2. actinides and their reaction and decay products, and

  3. fission products.

Called "sublibs" for short, they are identified by a number or
2-character specifier:

  1. light nuclides with "LT" or 1,

  2. actinides with "AC" or 2, and

  3. fission products with "FP" or 3.

The production of fission products from actinides (2/AC3/FP) is the only
type of transition in a typical ORIGEN library that spans sublibs. The
sublib is optional in a nuclide specification and is indicated in
parentheses after the identifier—IZZZAAA(S), EAm(S). If the sublib for a
nuclide/element is not provided, it is guessed in the following manner:

  1. If the nuclide is in fact an element, then it is placed in
     sublib=1/LT.

  2. If the atomic number Z\textlt 26, an *attempt* is made to place it in
     sublib=1/LT.

  3. Otherwise (Z\textgeq 26 or attempt fails), sublibs are searched in reverse
     order, from 3/FP, 2/AC, and then 1/LT.

The third rule, which is to search sublibs in reverse order, correctly
handles spent reactor fuel, a common and important scenario. The other
two conditions can be interpreted as exceptions. The first exception
correctly handles activation scenarios where it is most convenient to
specify the initial elemental constituents. The second exception handles
light nuclides that could not be real fission products, as fission
products have Z\textgeq 26 by definition. The byproducts :sup:`1`\ H,
:sup:`2`\ H, :sup:`3`\ H, :sup:`3`\ He, and :sup:`4`\ He actually exist
in all sublibs, but FP and AC byproducts have a reduced set of
transitions compared to the LT version, which has full decay and
activation chains. Thus when a user specifies one of the byproduct
nuclides as input, it is best to associate it to the LT version.

.. _5-1-3-3-1-2:

Physical Units in Calculations
""""""""""""""""""""""""""""""

A variety of units can be used in the input and specified for the output
of an ORIGEN calculation. The input allows for initial concentrations in

  1. grams,

  2. moles (or gram-atoms),

  3. number density in atoms/barn-cm, and

  4. curies.

Time may be expressed in seconds, minutes, hours, days, years, or a
user-defined unit. Irradiation may be expressed in terms of neutron flux
(n/cm\ :sup:`2`-s) or power (W). The allowed units for output include
those for input, as well as the following decay quantities:

  1. total decay heat power (W),

  2. gamma decay heat power (W),

  3. airborne toxicity (m\ :sup:`3`) required to dilute activities to the
     Radiation Concentration Guide (RCG) limit for air,

  4. ingestion toxicity (m\ :sup:`3`) required to dilute activities to the
     RCG limit for water, and

  5. alpha, beta, neutron, photon sources (particles/s or MeV/s).


:numref:`table-origen-units` summarizes the available units in
ORIGEN. During irradiation cases, the following can also be returned:

  1. absorption rates (absorptions/s),

  2. fission rates (fissions/s), and

  3. infinite neutron multiplication constant, k\ :sub:`∞`.

.. _table-origen-units:
.. table:: Availalble physical units in ORIGEN
  :widths: 28 45 9 9 9
  :align: center


  +-------------------+-----------------+-----------+----------------------------+
  | **Unit name**     | **Description** | **Input** | **Output**                 |
  |                   |                 |           +--------------+-------------+
  |                   |                 |           | **(irrad.)** | **(decay)** |
  +===================+=================+===========+==============+=============+
  | GRAMS             | Mass in grams   |     *     |      *       |     *       |
  +-------------------+-----------------+-----------+--------------+-------------+
  | MOLES or          | Number in moles |     *     |      *       |     *       |
  |                   | (or legcy       |           |              |             |
  | GRAM-ATOMS        | equivalent of   |           |              |             |
  |                   | gram-atoms)     |           |              |             |
  +-------------------+-----------------+-----------+--------------+-------------+
  | ATOMS-PER-BARN-CM | Density in      |     *     |      *       |     *       |
  |                   | atoms/barn-cm   |           |              |             |
  |                   | (10\ :sup:`-24` |           |              |             |
  |                   | cm/barn ×       |           |              |             |
  |                   | density in      |           |              |             |
  |                   | atoms/          |           |              |             |
  |                   | cm\ :sup:`3`);  |           |              |             |
  |                   | requires        |           |              |             |
  |                   | volume input    |           |              |             |
  +-------------------+-----------------+-----------+--------------+-------------+
  | CURIES            | Activity in     |     *     |      *       |      *      |
  |                   | curies          |           |              |             |
  +-------------------+-----------------+-----------+--------------+-------------+
  | BECQUERELS        | Activity in     |     *     |      *       |      *      |
  |                   | becquerels      |           |              |             |
  +-------------------+-----------------+-----------+--------------+-------------+
  | ATOMS_PPM         | Atom fractions  |           |      *       |      *      |
  |                   | x 10\ :sup:`6`  |           |              |             |
  +-------------------+-----------------+-----------+--------------+-------------+
  | WEIGHT_PPM        | Weight fractions|           |      *       |      *      |
  |                   | x 10\ :sup:`6`  |           |              |             |
  +-------------------+-----------------+-----------+--------------+-------------+
  | WATTS             | Total decay     |           |              |      *      |
  |                   | heat in watts   |           |              |             |
  +-------------------+-----------------+-----------+--------------+-------------+
  | G-WATTS           | Total decay heat|           |              |      *      |
  |                   | from photons in |           |              |             |
  |                   | watts           |           |              |             |
  +-------------------+-----------------+-----------+--------------+-------------+
  | M3_AIR            | Radiotoxicity   |           |              |      *      |
  |                   | m\ :sup:`3` for |           |              |             |
  |                   | for inhalation  |           |              |             |
  +-------------------+-----------------+-----------+--------------+-------------+
  | M3_WATER          | Radiotoxicity   |           |              |      *      |
  |                   | in m\ :sup:`3`  |           |              |             |
  |                   | for ingestion   |           |              |             |
  +-------------------+-----------------+-----------+--------------+-------------+

.. _5-1-3-3-1-3:

Saving Results
""""""""""""""

ORIGEN can save any results (isotopics and source spectra) in a special
ORIGEN binary concentrations file (f71). The file is a simple sequence
of solutions, and new results are simply appended on to the end of an
existing file. Note that no matter how initial isotopics are entered or
what units are asked for in the output file, the ORIGEN f71 contains
**moles** (gram-atoms) of each isotope and an optional **volume** to
permit unit conversions to number density (atoms/barn-cm). Isotopics for
an ORIGEN calculation can be initialized from any position on this file
in an ORIGEN calculation. The f71 can also be read by OPUS to perform
various post-processing tasks.

.. _5-1-3-3-2:

Input Description
^^^^^^^^^^^^^^^^^

ORIGEN uses the Scale Object Notation (SON) language for its input,
although it can also read FIDO-based input for backwards compatibility
with SCALE 6.1 :cite:`laboratory_scale_2011`. The basic structure of an ORIGEN input is shown in
:numref:`fig-origen-input-overview`.


.. code-block:: scale
  :caption: ORIGEN input file overview
  :name: fig-origen-input-overview

   'SCALE comment
   =origen

   % ORIGEN comment %

   bounds{ … }
   solver{ … }
   options{ … }

   case(A){
       time=[31 365] % days
       …
   }

   case(B){
      …
   }
   …
   % more cases?

   end


The ORIGEN input is hierarchical, containing four levels, where level 0
is the "root" level, allowed between "=origen" and "end." The complete
set of keywords is shown in :numref:`table-origen-commands`,
with arrays denoted with "=[]" and blocks with "{}". Referring to the
overview in :numref:`fig-origen-input-overview`, at the root level, there is a
"solver" block for changing solver options, a "bounds" block for entering the
energy  boundaries for various particle emissions, and an "options" block for
altering the miscellaneous global options. These blocks may only appear once.
The remainder of the input is a sequence of "case" blocks (in the above examples
there are two cases with identifiers "A" and "B"), which each case is executed
in order, with each case possibly depending on one or more of the previous cases.


.. _table-origen-commands:
.. table:: List of all available ORIGEN input commands
   :widths: auto
   :class: longtable
   :align: center

   +---------------+----------------------+-----------------------+------------------+
   | **Level 0**   | **Level 1**          | **Level 2**           | **Level 3**      |
   +===============+======================+=======================+==================+
   | **case{}**    | title                                                           |
   |               +----------------------+------------------------------------------+
   |               | time{}               | start                                    |
   |               |                      |                                          |
   |               |                      | t=[]                                     |
   |               |                      |                                          |
   |               |                      | units                                    |
   |               |                      |                                          |
   |               |                      | custom_name                              |
   |               |                      |                                          |
   |               |                      | custom_length                            |
   |               +----------------------+------------------------------------------+
   |               |                      | file                                     |
   |               | lib{}                |                                          |
   |               |                      | pos                                      |
   |               +----------------------+------------------------------------------+
   |               | flux=[]                                                         |
   |               +-----------------------------------------------------------------+
   |               | power=[]                                                        |
   |               +----------------------+------------------------------------------+
   |               | print{}              | cutoff_step                              |
   |               |                      |                                          |
   |               |                      | absfrac_step                             |
   |               |                      |                                          |
   |               |                      | absfrac_sublib                           |
   |               |                      |                                          |
   |               |                      | rel_cutoff                               |
   |               |                      |                                          |
   |               |                      | cutoffs                                  |
   |               |                      |                                          |
   |               |                      | fisrate                                  |
   |               |                      |                                          |
   |               |                      | kinf                                     |
   |               |                      +-----------------------+------------------+
   |               |                      | nuc{}                 | sublibs=[]       |
   |               |                      |                       |                  |
   |               |                      | ele{}                 | total            |
   |               |                      |                       |                  |
   |               |                      |                       | units=[]         |
   |               |                      +-----------------------+------------------+
   |               |                      | neutron{}             | summary          |
   |               |                      |                       |                  |
   |               |                      |                       | spectra          |
   |               |                      |                       |                  |
   |               |                      |                       | detailed         |
   |               |                      +-----------------------+------------------+
   |               |                      | gamma{}               | summary          |
   |               |                      |                       |                  |
   |               |                      |                       | spectra          |
   |               |                      |                       |                  |
   |               |                      |                       | principal_step   |
   |               |                      |                       |                  |
   |               |                      |                       | unbinned_warning |
   |               |                      |                       |                  |
   |               |                      |                       | principal_cutoff |
   |               |                      +-----------------------+------------------+
   |               |                      | alpha{}               | summary          |
   |               |                      |                       |                  |
   |               |                      |                       | spectra          |
   |               |                      +-----------------------+------------------+
   |               |                      | beta{}                | summary          |
   |               |                      |                       |                  |
   |               |                      |                       | spectra          |
   |               |                      |                       |                  |
   |               |                      |                       | principal_step   |
   |               |                      |                       |                  |
   |               |                      |                       | principal_cutoff |
   |               +----------------------+-----------------------+------------------+
   |               | mat{}                | iso=[]                                   |
   |               |                      |                                          |
   |               |                      | feed=[]                                  |
   |               |                      |                                          |
   |               |                      | units                                    |
   |               |                      |                                          |
   |               |                      | previous                                 |
   |               |                      |                                          |
   |               |                      | volume                                   |
   |               |                      |                                          |
   |               |                      | blend=[]                                 |
   |               |                      +-----------------------+------------------+
   |               |                      |                       | file             |
   |               |                      | load{}                |                  |
   |               |                      |                       | pos              |
   +---------------+----------------------+-----------------------+------------------+
   |               | save{}               | steps=[]                                 |
   |               |                      |                                          |
   |               |                      | file                                     |
   |               |                      |                                          |
   |               |                      | time_offset                              |
   |               |                      |                                          |
   |               |                      | time_units                               |
   |               +----------------------+------------------------------------------+
   |               | neutron{}            | alphan_medium                            |
   |               |                      |                                          |
   |               |                      | alphan_bins                              |
   |               |                      |                                          |
   |               |                      | alphan_cutoff                            |
   |               |                      |                                          |
   |               |                      | alphan_step                              |
   |               +----------------------+------------------------------------------+
   |               | gamma{}              | sublib                                   |
   |               |                      |                                          |
   |               |                      | adjust_for_missing                       |
   |               |                      |                                          |
   |               |                      | conserve_line_energy                     |
   |               |                      |                                          |
   |               |                      | split_near_boundary                      |
   |               |                      |                                          |
   |               |                      | continuum                                |
   |               |                      |                                          |
   |               |                      | immediate                                |
   |               |                      |                                          |
   |               |                      | brem_medium                              |
   |               |                      |                                          |
   |               |                      | spont                                    |
   |               +----------------------+------------------------------------------+
   |               | alpha{}                                                         |
   |               +----------------------+------------------------------------------+
   |               | beta{}               | sublib                                   |
   +---------------+----------------------+------------------------------------------+
   | **bounds{}**  | alpha=[]                                                        |
   |               |                                                                 +
   |               | beta=[]                                                         |
   |               |                                                                 +
   |               | gamma=[]                                                        |
   |               |                                                                 +
   |               | neutron=[]                                                      |
   +---------------+-----------------------------------------------------------------+
   | **solver{}**  | type                                                            |
   |               +----------------------+------------------------------------------+
   |               |                      | terms                                    |
   |               |                      |                                          |
   |               |                      | maxp                                     |
   |               |                      |                                          |
   |               |                      | abstol                                   |
   |               |                      |                                          |
   |               | opt{}                | reltol                                   |
   |               |                      |                                          |
   |               |                      | calc_type                                |
   |               |                      |                                          |
   |               |                      | order                                    |
   |               |                      |                                          |
   |               |                      | substeps                                 |
   +---------------+----------------------+------------------------------------------+
   | **options{}** | print_xs                                                        |
   |               |                                                                 |
   |               | digits                                                          |
   |               |                                                                 |
   |               | fixed_fission_energy                                            |
   +---------------+-----------------------------------------------------------------+


The percent sign (\%) is the comment character *inside the ORIGEN
sequence,* between "=origen" and "end." The % is a very flexible comment
that may be placed almost anywhere in the input and continues until the
end of the line. Outside the ORIGEN sequence, the SCALE comment
character of a single quote ' at the beginning of a line must be used.
Arrays in SON begin with "[" and end with "]" and support the following
special shortcuts inherited from FIDO. Note that the interpolation
shortcuts (I and L) *insert* values between two specified values so that
there will be N+2 values in the final expanded array section.


.. _table-origen-array-shortcuts:
.. table:: Array entry shortcuts
   :widths: 20 15 65

   +------------------------+------------------+------------------------+
   | **Shortcut**           | **Format**       | **Examples**           |
   |                        |                  |                        |
   |                        |                  | *shortcutexpansion*    |
   +========================+==================+========================+
   | Repeat (**R**)         | *N*\ **R**\ *X*  | 3r1e141e14 1e14 1e14   |
   |                        |                  |                        |
   |                        |                  | 6r3 3 3 3 3 3 3        |
   +------------------------+------------------+------------------------+
   | Linear interpolation   | *N*\ **I** *X Y* | 3i 5 1 5 4 3 2 1       |
   | (**I**)                |                  |                        |
   |                        |                  | 9i 0.0 1.0 0.0 0.1 0.2 |
   |                        |                  | 0.3 0.4 0.5 0.6 0.7    |
   |                        |                  | 0.8 0.9 1.0            |
   +------------------------+------------------+------------------------+
   | Log interpolation      | *N*\ **L** *X Y* | 3l 1 5                 |
   | (**L**)                |                  |                        |
   |                        |                  | 5l 1e-9 1e-3 1e-9 1e-8 |
   |                        |                  | 1e-7 1e-6 1e-5 1e-4    |
   |                        |                  | 1e-3                   |
   +------------------------+------------------+------------------------+

As an alternative to manually creating an ORIGEN input file via a text
editor, the user may use the SCALE graphical user interface (GUI)
Fulcrum to create ORIGEN input files. Advantages to using Fulcrum
include syntax highlighting, autocomplete, immediate feedback when input
is incorrect, and one-click running of calculations.

.. _5-1-3-3-2-1:

Calculation Case (case)
"""""""""""""""""""""""

A single ORIGEN sequence may contain an unlimited number of case blocks.
Each case block is processed in order and can represent either an
independent calculation or continuation of a previous case. The complete
contents of a single case block are shown in :numref:`table-origen-nuc-spec`.


.. code-block:: scale
  :caption: ORIGEN "case" overview
  :name: fig-origen-case-overview

   case(ID){
      title="my title"

       lib{ … }
       mat{ … }
       time{ … }
       flux{ … } % or power{ … }

       print{ … }
       save{ … }

       alpha{ … }
       beta{ … }
       gamma{ … }
       neutron{ … }
   }


The most important three components are the lib, mat, and
time/power/flux inputs:

  1. an ORIGEN library and the transition matrix data set on it to use
      (lib),

  2. initial amounts of nuclides (mat), and

  3. a power or flux history (time/power or time/flux).

The case identifier and case title string (shown as ID and title="my
title" in :numref:`fig-origen-case-overview`) are echoed in the output file
and can be a convenient way to differential cases. Both are optional, with the
ID defaulting to the case index, with "1" for the first case, "2" for
the second, etc. The "print" and "save" blocks represent two ways to
analyze the output from a calculation. The "print" block prints
tables directly to the output file, and the "save" block saves the
solution in a special ORIGEN binary concentration file (f71), e.g.,
for later post-processing. Finally, the "alpha," "beta," "gamma," and
"neutron" blocks control the emission source calculations for alpha,
beta, gamma, and neutron particles, respectively. The remaining
subsections will describe the input for each of these blocks.

Transition Matrix Specification (lib)
.....................................

The transition matrix to use in a case is controlled by the "lib" shown
in :numref:`fig-origen-lib-overview`.

.. code-block:: scale
  :caption: ORIGEN "lib" overview
  :name: fig-origen-lib-overview

   lib{
       file="origen.f33"  % ORIGEN library filename
       pos=1              % data set position on library
   }


A "lib" **must** be present in the first case with a defined ORIGEN
library file. The default position is "pos=1". The "lib" may be omitted
in subsequent cases, and if so, the previous case’s "lib" is used. The
position refers to the set of transition coefficients (transition matrix
**A**) to load. To load another position on the same library file, the
"lib" block with "pos=X" can be used to load position X. When ARP
generates an ORIGEN library, it will contain a set of transition
coefficients for each requested burnup. When COUPLE generates an ORIGEN
library, it will contain a single position. **For decay calculations,
file="end7dec" can be used to load a decay-only library.**

Material Specification (mat)
............................

The initial isotopics for a case a controlled by the "mat" shown in
:numref:`fig-origen-mat-overview`. Note that the material specification
has a few different variants, with only one allowed to specify the material
in a given case.

.. code-block:: scale
  :caption: ORIGEN "mat" block overview
  :name: fig-origen-mat-overview

   % from iso
   mat{
       iso=[ u235=1.0 u238=9.0 ] %id(sublib)=amount
       units=GRAMS               %units in iso array
   }

   % from iso with number density input
   mat{
       iso=[ u235=1e-2 u238=1e-1 ] %id(sublib)=amount
       units=ATOMS-PER-BARN-CM     %units in iso array
       volume=200                  %cm^3
   }

   % from position on f71 file
   mat{
       load{ file="origen.f71" pos=11 }
   }

   % from previous case (previous=LAST is default)
   mat{
       previous=4 %step index from previous case
   }


In the first variant in :numref:`fig-origen-mat-overview`, the isotopic
distribution "iso" is used with "units." The "iso" array contains a sequence
of "id=amount" pairs, where "id" is a nuclide identifier in the format
described in :ref:`5-1-3-3-1-1`, and the units of the amount are given
by the "units" keyword, one of the unit names listed in the third column of
:numref:`table-origen-units`. Default units are MOLES.

In the second variant, the number density (ATOMS-PER-BARN-CM) is
specified which requires an additional specification of the "volume" in
cm\ :sup:`3`. Internally, the number density will be converted to MOLES
using that volume. For any type of units specified internally for
calculations, isotopics are always converted to MOLES and then
reconverted to the output units required.

In the third variant, the isotopics are loaded from a specific position
on the f71 file. Note that the position index starts at one (not zero)
and because the f71 is always appended to, it may contain multiple
materials, cases, timelines, etc. In the fourth and final variant, the
isotopics are loaded from *end* of step 4 from the previous case
("previous=4"). The index zero (e.g., "previous=0") corresponds to the
initial isotopics of the previous case. The keyword "LAST" may be used
to load the isotopics from the end of the last step, "previous=LAST".
This is the default behavior, used when a "mat" block is not
present.

There are two additional special material specifications shown
in :numref:`fig-origen-feed-blend`: (1) with a feed rate term,
:math:`\overrightarrow{S}(t)` in :eq:`eq-origen-trm-terms`, or (2) the blend
array. The feed specified is in the units specified *per second* and constant
for the entire case. It is possible to perform a calculation with feed but with
zero initial isotopics by specifying "iso=0". Feed can be negative,
however, the calculation becomes undefined and will abort when the
number of atoms of any nuclide becomes negative.

The blend array allows a fraction of each result from the previous cases
to be loaded. The identifier is the case name, or the *index* of the
case if a case name is not provided and the fraction is the atom
fraction. The step index for the isotopics can be specified in
parentheses. For example, B(2)=0.9 indicates that 90\% of the case(B)
isotopics should be taken at the end of step 2. The default step index
is the final step for the case. **Only one blend is allowed in an ORIGEN
input (between "=origen" and "end").** Multiple blends currently
requires saving isotopics to an f71 file and reloading in a subsequent
calculation.


.. code-block:: scale
  :caption: ORIGEN "feed" and "blend" arrays
  :name: fig-origen-feed-blend

   % with feed array
   mat{
       % units for iso and feed
       units=GRAMS

       % material is natural sodium
       iso=[na=1.0e6]
       % with feed array, set initial isotopics of zero
       %iso=0

       % continuous feed of U-235 at 1 kg/day
       % converted to grams/second
       feed=[u235=0.01157]
   }

   % with blend array (only one allowed in an input)
   case(A){ … }
   case(B){ … }
   case{
       …
       mat{
           % case ID(step index)=fraction of atoms
           blend[ A=0.1 B(2)=0.9 ]
       }
   }

Operating History (power, flux, time)
.....................................

The operating history is specified using "time," "power," and "flux,"
with examples shown in :numref:`fig-origen-history-blocks`. For decay cases,
only the "time" array in units of days is required. For irradiation cases,
either "power" or "flux" may be provided. When flux is used, it is the
step-wise flux :math:`\Phi_{n}\ \left( \frac{n}{cm^{2}s} \right)`
appearing directly in the depletion equations of :eq:`eq-origen-trm-terms`.
When power is used, it is the total step-average power-- :math:`P_{n}\ (MW)`
--converted to step-wise average flux using :eq:`eq-origen-pc-flux`.
With irradiation cases using flux or power, the same number of entries must be
specified on the time and flux/power array. The start time corresponding to the
initial conditions is not included in the array of time values. Additionally,
the time specification allows time units (including a custom unit) and a start
time in which the block form of "time" must be used "time{…}."


.. code-block:: scale
   :caption: ORIGEN operating history blocks ("time," "flux," and "power").
   :name: fig-origen-history-blocks

   % simple decay case (two steps 0 unicode::U+2192 1 and 31 unicode::U+2192 65 days)
   time = [ 31 365 ]

   % flux irradiation (decay if flux=0)
   time = [ 31   365  396 ]
   flux = [ 2e14 1e14 0 ]

   % power irradiation (decay if power=0)
   time = [ 31 365 396 ]
   power= [ 50 45  0 ] %50 MW, 45 MW, then decay

   % changing units using time block
   time{
       t = [ 5 15 300 ]
       units = HOURS
       % available units:
       % SECONDS, MINUTES, HOURS, DAYS, YEARS, CUSTOM
   }

   % custom units
   time{
       t = [ 1 2 3 ]
       units = CUSTOM
       custom_name = "MONTH"
       custom_length = 2678400 %seconds per "MONTH"
   }

   % 10-step detailed power history
   time=[   5  10 20 100 300 400 405 500 800 1000]
   power=[ 20  41 43  42  37  33  16 14.5 28.5 26]


To illustrate some aspects of specifying a power history, refer to
:numref:`fig-origen-history-plot`, where the black line ("actual power") shows
a piecewise linear power history that is translated to a possible step-wise
constant power history shown by the red line ("step-wise constant power"), with
input shown in :numref:`fig-origen-history-blocks` labeled "10-step detailed
power history". The secondary (right) y-axis shows the step-wise flux,
calculated from the step-wise power via the predictor-corrector approach of
:eq:`eq-origen-pc-flux`. The dependence of the power-to-flux conversion on
the actual material composition is shown in the comparison of flux results
for an initial composition with 6% fissile :sup:`235`\ U (blue dotted line)
versus 2% fissile :sup:`235`\ U (purple dashed line). The flux at the beginning
of the irradiation is a factor of 3 higher with the 2% fissile case, due to
approximately a factor of 3 lower fissile content. With time, fissile
plutonium build-up closes the gap to a factor of 1.5.

.. _fig-origen-history-plot:
.. figure:: figs/ORIGEN/fig14.png

   Example of ORIGEN operating history and power-to-flux conversion.


.. code-block:: scale
   :caption: ORIGEN "start" time usage.
   :name: fig-origen-start-time

   % first case
   case{
       mat{ … }
       time=[ 1 10 25 50]
       flux=[ 4r1e14 ]
   }
   % continuation case (time zero is 50 days)
   case{
       time{
           units=YEARS
           %without start, times must continue > 50 days
           %t=[50/365.+0.1 50/365.+0.3 … ]
           %with start=0, times given assume start at zero
           start=0
           t=[0.1 0.3 0.9 2.7]
       }
   }


By default, subsequent cases that continue operations on a material,
continue the timeline of that material. Using "start=0" is convenient
when switching time unitsfrom irradiation in days to decay time in
years, for example. Otherwise, the final time must be converted to
years.

Printing Options (print)
........................

The "print" command is one of the most complex inputs, with options to
set printing cutoffs and control the concentrations returned, broken
down by nuclides and elements and emission sources for gamma, neutron,
alpha, and beta particles. Additionally, there are options to print
fission rates, absorption rates, and the ratio of fission rate to
absorption rate. Each case is allowed a print block.

.. centered:: Inventories by nuclide and element


The options for printing nuclides and elements are shown in
:numref:`fig-origen-print-blocks`.  The print block allows the "nuc" block
and "ele" block for printing nuclide and element results, respectively.


.. code-block:: scale
   :name: fig-origen-print-blocks
   :caption: ORIGEN nuclide and element “print” blocks

   % print each nuclide (total across all sublibs) in grams
   print{
       nuc{ total=yes units=GRAMS }
   }

   % print each element (total across all sublibs)
   % in moles, grams, and curies with cutoffs of 1%
   print{
       ele{ total=yes units=[MOLES GRAMS CURIES] }
       cutoffs[ ALL=1.0 ]
   }

   % print decay heat and mass (by element)
   % of fission products and actinides only
   print{
       ele{ sublibs=[AC FP] units=[GRAMS WATTS] }
   }

   % change cutoff to absolute curies by element,
   % in step of interest (7), but print GRAMS
   print{
       cutoff_step = 7 % default -1 for average
       rel_cutoff = no % default is yes for cutoff in percent
       % only print above 1e-3 curies
       cutoffs[ CURIES=1e-3 ]   % default is 1e-6 percent
       nuc{
        total=yes
        units=GRAMS
       }
   }


Inside the "nuc" or "ele" blocks, there are three possible entries:

  -  a "sublibs" array (a list from LT, AC, FP, ALL),

  -  a "total" (yes or no), and

  -  a "units" array (see column 1 of :numref:`table-origen-units` for
     possible units).

The "total" is whether to sum over all "sublibs," i.e., if Gd-155 occurs
in both LT and FP sublibs, then the total will be the sum of the two. It
is possible to have "sublibs=[LT AC FP] total=yes," which results in
four output tables, one for each of the sublibs and one for the total.
The specification of "sublibs=ALL" is the same as "sublibs=[LT AC FP]."

Three parameters set the cutoff for printing a nuclide or element:

  -  "cutoff_step" sets the index on which to base the cutoff (default -1
     means use an average over all steps),

  -  "rel_cutoff" determines whether to treat the cutoff as a percent of
     the total (default/yes) or an absolute amount (no), and

  -  the "cutoffs" array allows one to specify the cutoff for each unit in
     :numref:`table-origen-units` as a sequence of "unit=cutoff" pairs.

.. centered:: Radiological Emissions (alpha, beta, gamma, neutron)


The emission printing options are controlled by the "alpha," "beta,"
"gamma," and "neutron" emission blocks inside a "print" block (examples
shown in :numref:`fig-origen-rad-print-blocks`).


.. code-block:: scale
   :caption: ORIGEN emission “print” blocks.
   :name: fig-origen-rad-print-blocks

   print{
       % default neutron options
       neutron{
        summary=yes
        spectra=no
        detailed=no
       }

       % default gamma options
       gamma{
        summary=yes
        spectra=no
        principal_step=NONE  %step index to calculate
                             %(NONE to suppress)
        principal_cutoff=2   %principal emitter cutoff
                             %in percent
        unbinned_warning=no  %print warning
                             %when line not binned
       }

       % default alpha options
       alpha{
        summary=yes
        spectra=no
       }

       % default beta options
       beta{
        summary=yes
        spectra=no
        principal_step=NONE  %step index to calculate
                             %principal (NONE to suppress)
        principal_cutoff=2   %principal emitter cutoff
                             %in percent
       }
   } %end print

The "neutron" print options are

  -  "summary" (yes/no) controls the printing of a source strength
     summary,

  -  "spectra" (yes/no) controls the printing of the spectra (energy
     group-wise), and

  -  "detailed" (yes/no) controls the printing of extra details about the
     neutron calculation.

   The "gamma" print options are

  -  "summary" (yes/no) controls the printing of a source strength summary
     and

  -  "spectra" (yes/no) controls the printing of the spectra (energy
     group-wise).

The gamma print allows a special output of the principal emitters in
each energy group, controlled by setting the "principal_step" keyword to
a specific step index in the case, with the "principal_cutoff" keyword
used to set the minimum percent of the total a nuclide must have to be
considered a principal emitter. For the gamma print there is a warning
that can be enabled with "unbinned_warning=yes" if some gamma lines fall
outside the user group structure and thus are not included.

The "alpha" print options are

  -  "summary" (yes/no) controls the printing of a source strength summary
     and

  -  "spectra" (yes/no) controls the printing of the spectra (energy
     group-wise).

The "beta" print options are

  -  "summary" (yes/no) controls the printing of a source strength summary
     and

  -  "spectra" (yes/no) controls the printing of the spectra (energy
     group-wise).

The beta print also allows a special output of the principal emitters by
setting the "principal_step" keyword to a specific step index in the
case, with the "principal_cutoff" keyword used to set the minimum
percent of the total a nuclide must have to be considered a principal
emitter.

The special printing options are shown in :numref:`fig-origen-special-print`.

.. code-block:: scale
   :caption: ORIGEN special "print" options
   :name: fig-origen-special-print

   % defaults special printing options
   print{
       absfrac_sublib = ALL %print absorption fractions for
                            %a specific sublib (LT,AC,FP)
                            %or ALL sublibs (DEFAULT)

       absfrac_step = 7  %if absfrac active, step to print
                         % default is last step

       fisrate = NONE    %print fission rates (default NONE)
                         %absolute (ABS) or relative (REL)

       kinf = no         %print fission/absorption (yes/no)
   }

Saving Results (save)
.....................

Saving the results to an ORIGEN binary file (f71) is requested with the
"save" block, which specifies both the name of the file and the step
indices to save, as shown in :numref:`fig-origen-save-block`. The default
for the filename is "file=ft71f001" and default for the steps is the special
"steps=ALL" which saves all isotopics and spectra as a shortcut to having to
specify "steps=[0 1 2 3 … LAST]". The step index "0" corresponds to the
initial isotopics and the step index "LAST" may be used as a shortcut for
the last case index. There is a special rule for copying f71 files from
SCALE’s temporary/working directory. If the file name "ft71f001" exists
in the directory when SCALE finishes, it is copied to the user’s
"${OUTDIR}" as "${BASENAME}.f71", e.g. if my.inp produces "ft71f001" in
the temporary/working directory then it will be copied to the same
location as the main output file ("my.out") as "my.f71". Note that f71
files are always appended to by ORIGEN. To save with the defaults, the
shortcut "save=yes" is provided. The default is "save=no".

.. code-block:: scale
   :name: fig-origen-save-block
   :caption: ORIGEN "save" block.

   case{
       mat{ … }
       time=[ 1 10 100 1000 ] % 4 steps to 1000 days
       save{
             file="short.f71"   % file name
             steps=[0 2 4]      % save initial (0) and isotopics
                                    % end-of-step 2 (10 days)
                                    % end-of-step 4 (1000 days)
       }

       save{
             file="ft71f001"   % file name (DEFAULT)
             steps=ALL         % save ALL steps (DEFAULT)
       }
       save=yes              % equivalent to the above

       save{
             file="last.f71"   % file name
             steps=[LAST]      % save only last (LAST=4 here)
             time_offset=1000  % write time - time_offset
             time_units=DAYS   % units of time_offset
       }
   }


In order to change the time values written to the f71 file, use
"time_offset=T\ :sub:`0`\ " which will write the current cumulative time
minus T\ :sub:`0` to the file. The "time_offset" is convenient, for
example, when time *since discharge* is desired instead of the absolute,
cumulative time. The "time_units" entry specifies the units of the
"time_offset", with the same units available in the "time" block. The
default is "time_units=DAYS".

Decay Emission Calculations (alpha, beta, gamma, neutron)
.........................................................

A decay emission calculation is initiated with the appropriate block
inside the calculation "case." The group structure for any emission
spectra result is determined by the energy bounds provided as described
in :ref:`5-1-3-3-2-2`. Each type of emission calculation
is activated by the existence of a calculation block named "alpha", "beta",
"gamma", or "neutron" for those respective types of calculations.
Alternatively, to turn on an emission calculation with defaults, use
"alpha=yes", "beta=yes", "gamma=yes", or "neutron=yes" in a "case" block.

.. centered:: Neutron source calculation


The neutron calculation (:ref:`5-1-2-4-1`) is activated by the
"neutron" calculation block. All neutron calculation options are to control the
:math:`\left(\alpha,n\right)` calculation.

Three :math:`\left(\alpha,n\right)` options can be indicated with the
"alphan_medium": a UO\ :sub:`2` fuel matrix (alphan_medium=UO2), a borosilicate
glass matrix (alphan_medium=BOROSILICATE), and the problem-dependent matrix
defined by the user input compositions (alphan_medium=CASE). The numeric
options 0, 1, and 2 are also valid for the UO2, BOROSILICATE, and CASE
options, respectively. Note that the UO\ :sub:`2` and borosilicate glass
matrix options assume that the neutron source nuclides reside in these
respective matrices, *regardless of the actual composition of the
material in the problem.*

For oxide fuels, a significant neutron source can be produced from
:sup:`17`\ O :math:`\left(\alpha,n\right)` and :sup:`18`\ O
:math:`\left(\alpha,n\right)` reactions in the oxygen compounds of the fuel.
For this reason, the UO\ :sub:`2` matrix option (enabled by alphan_medium=UO2)
is provided with natural isotopic distribution of :sup:`17`\ O and :sup:`18`\ O.
This includes the impact of oxygen isotopes on the neutron source without having
to include oxygen in the initial composition.

Another common use case is fuel storage in a borosilicate glass matrix
(enabled by alphan_medium=BOROSILICATE), listed in
:numref:`table-origen-borosilicate-comp`.


.. _table-origen-borosilicate-comp:
.. table:: Elemental composition [#bsg-comps]_ used in the borosilicate glass option.
  :widths: 20 30 25 25

  +-----------------------+----------------+-----------------------+------------+
  | **Atomic**            | **Element**    | **Wt %**              |            |
  |                       |                |                       |            |
  | **number**            | **symbol**     |                       | **Atom %** |
  +-----------------------+----------------+-----------------------+------------+
  |  3                    | Li [#an]_      |      2.18             | 6.296      |
  +-----------------------+----------------+-----------------------+------------+
  |  5                    | B [#an]_       |      2.11             | 3.913      |
  +-----------------------+----------------+-----------------------+------------+
  |  8                    | O [#an]_       | 46.4                  | 58.138     |
  +-----------------------+----------------+-----------------------+------------+
  |  9                    | F [#an]_       | 0.061                 | 0.0644     |
  +-----------------------+----------------+-----------------------+------------+
  | 11                    | Na [#an]_      | 7.65                  | 6.671      |
  +-----------------------+----------------+-----------------------+------------+
  | 12                    | Mg [#an]_      | 0.49                  | 0.404      |
  +-----------------------+----------------+-----------------------+------------+
  | 13                    | Al [#an]_      | 2.18                  | 1.620      |
  +-----------------------+----------------+-----------------------+------------+
  | 14                    | Si [#an]_      | 25.4                  | 18.130     |
  +-----------------------+----------------+-----------------------+------------+
  | 17                    | Cl [#an]_      | 0.049                 | 0.0277     |
  +-----------------------+----------------+-----------------------+------------+
  | 20                    | Ca             | 1.08                  | 0.540      |
  +-----------------------+----------------+-----------------------+------------+
  | 25                    | Mn             | 1.83                  | 0.668      |
  +-----------------------+----------------+-----------------------+------------+
  | 26                    | Fe             | 8.61                  | 3.091      |
  +-----------------------+----------------+-----------------------+------------+
  | 28                    | Ni             | 0.70                  | 0.239      |
  +-----------------------+----------------+-----------------------+------------+
  | 40                    | Zr             | 0.88                  | 0.193      |
  +-----------------------+----------------+-----------------------+------------+
  | 82                    | Pb             | 0.049                 | 0.0047     |
  +-----------------------+----------------+-----------------------+------------+
  | Total                 |                | 99.669                | 100.000    |
  +-----------------------+----------------+-----------------------+------------+

.. [#bsg-comps] Borosilicate glass compositions.
.. [#an] Elements with :math:`\left(\alpha,n\right)` yields.

In the last most rigorous option, the :math:`\left(\alpha,n\right)` neutron
source and spectra are calculated using the source, target, and constituents
determined using the material compositions in the problem *at a particular
time,* dictated by "alphan_step" in the "neutron" print options. For spent
fuel neutron source calculations, there are a large number of potential
source, target, and constituent nuclides in the :math:`\left(\alpha,n\right)`
calculation and in order to remove low-importance nuclides from the calculation,
the "alphan_step" and "alphan_cutoff" parameters are used. Only those nuclides
with an :math:`\alpha`-decay activity exceeding the product of "alphan_cutoff"
times the total :math:`\alpha` activity are included as source nuclides in the
:math:`\left(\alpha,n\right)` neutron calculation. Additionally, only those
nuclides with a constituent or target atom fraction less than
"alphan_cutoff" are included unless the concentration is greater than 1 ppm,
in which case it will be retained regardless of the cutoff. The "blend" array
is particularly useful for creating a problem-dependent medium composed of
fuel and another material.

.. code-block:: scale
   :caption: ORIGEN "neutron" calculation block
   :name: fig-origen-neutron-block

   case{
       …
       neutron{
             alphan_medium=CASE %0/UO2 for UO2
                                    %1/BOROSILICATE
                                    %  for Borosilicate glass
                                    %2/CASE for case-specific (DEFAULT)
             alphan_bins=200    %use 200 bins for
                                    %alpha slowing down calculation
             alphan_cutoff=0.0  %cutoff for alpha,n calculation
             alphan_step=LAST   %step index in this case
       }
       %alternatively, to enable neutron calculation with defaults
       %neutron=yes
   }


.. centered:: Gamma source calculation


The gamma (photon) calculation described in :ref:`5-1-2-4-4`
is activated with the "gamma" block, as shown in
:numref:`fig-origen-gamma-block`. The gamma block includes a host of options
where the default should be appropriate in most cases.

  -  The "sublib" option (default "ALL") affects the sublibraries included
     in the gamma emission calculation. The "immediate" option (default
     "yes") includes immediate gamma and x-rays.

  -  The "spont" option (default "yes") includes photons emitted during
     spontaneous fission and :math:`\left(\alpha,n\right)`.

  -  The "continuum" option (default "yes") enables mapping of continuum
     data stored artificially as lines to a continuum across the
     user-defined energy bins.

The following options may need to be modified in some scenarios.

  -  The "brem_medium" option (default "UO2") includes the photons emitted
     by beta particles as they slow down in a medium (Bremsstrahlung) in
     the gamma calculation. A problem-dependent medium is not available
     for "brem." The only options are "NONE," "H2O" (for Bremsstrahlung in
     water) and "UO2" (for uranium dioxide).

  -  The "conserve_line_energy" option (default "no") modifies the
     intensity of each gamma line within a group to conserve energy
     according to *I\ g = I\ a E\ a/E\ g*, where *I\ a* is the original
     line intensity, *E\ a* the original line energy and *E\ g* is the
     group energy (simple midpoint energy). Note that this option modifies
     intensities and thus results in number of particles not being
     conserved.

  -  The "adjust_for_missing" option (default "no") accounts for the
     scenario where a nuclide has a known gamma decay mode with known
     recoverable energy release, but the spectral data do not exist in the
     available emission resource. If "adjust_for_missing=yes," the *entire
     spectrum* is scaled up to include the missing energy. If the missing
     energy is more than 1% of the total, a warning is printed.

  -  The "split_near_boundary" option (default "no") enables a splitting
     of a line when it appears very close to a bin boundary. If
     "split=yes" and a photon line is within 3% of an interior energy
     boundary, then the intensity is split equally between the adjacent
     groups.

.. code-block:: scale
   :caption: ORIGEN "gamma" calculation block
   :name: fig-origen-gamma-block

   case{
       …
       gamma{
            sublib=ALL      %LT, FP, or AC – single sublib
                            %ALL – all sub-libraries
            brem_medium=UO2 %assume Bremsstrahlung in UO2
            continuum=yes   %expand continuum data stored as
                            %lines into proper continuua
            immediate=yes   %load lines for immediate gamma/x-rays
            spont=yes       %include photons from
                            %spontaneous fission
                            %and alpha,n reactions

            conserve_line_energy=no %conserve line energy instead
                                    %of line intensity
            adjust_for_missing=no   %adjust photon intensity
                                    %for energy of missing spectra
            split_near_boundary=no  %lines within 3% of a
                                    %group boundary are split
                                    %into two bins
       }
       %alternatively, to enable gamma calculation with defaults
       %gamma=yes
   }

.. centered:: Alpha and beta source calculation


The alpha calculation (:ref:`5-1-2-4-2`) has no options
and the beta calculation (:ref:`5-1-2-4-2`) only has a
single option to choose the nuclide sublibraries included (see
:numref:`fig-origen-alpha-beta-blocks`). Note that the alpha and beta
calculations determine *sources* and do not include any slowing down physics
for charged particles.


.. code-block:: scale
   :caption: ORIGEN "alpha" and "beta" calculation blocks.
   :name: fig-origen-alpha-beta-blocks

   case{
       …
       alpha{
           %no options
       }
       %alternatively, to enable alpha calculation with defaults
       %alpha=yes

       beta{
          sublib=ALL  %LT, FP, or AC – single sublib
                      %ALL – all sub-libraries
       }
       %alternatively, to enable beta calculation with defaults
       %beta=yes
   }

Processing Options (processing)
...............................

The processing options are contained inside the "processing" block
(inside a "case") and have two ways to modify the isotopics vector: the
"removal" block and the "retained" array (see
::numref::`fig-origen-processing-block`). Both operate on *elements* instead
of nuclides.

  -  Each "removal" block specifies a list of elements and a rate of
     continuous removal in units *(1/s)*. This removal is an artificial
     increase of the decay constant, from :eq:`eq-origen-trm-terms`, and it can
     be used to model any continuous system of removal, such as filtration.
     Note that more than one removal block may be specified.

  -  The "retained" array specifies a list of elements and the mole/atom
     fraction to be retained at the start of this case. **Note that all
     unspecified elements become zero.**

.. code-block:: scale
   :caption: ORIGEN "processing" block
   :name: fig-origen-processing-block

   case{
       …
       processing{
           %rate is in 1/s
           removal{ rate=1e-2 ele=[H Xe Ar] }
           removal{ rate=1e-7 ele=[U Pu] }
           %id=frac
           retained=[ u=1.0 pu=0.5 ]
       }
   }

.. _5-1-3-3-2-2:

Bounds Block
""""""""""""

The "bounds" block appears outside all cases and is valid for the entire
input, dictating the energy bins (i.e., groups) for emission spectra and
source calculations (see :numref:`fig-origen-bounds-block`). The array
shortcuts—"L" for logarithmically spaced intervals and "I" for
linearly-spaced intervals—can be particularly useful for specifying the
bounds (see :numref:`table-origen-array-shortcuts`). The energy bounds are
in units *(eV)* and can be given in increasing or decreasing order with the
output convention of  decreasing order. Additionally, neutron and gamma energy
bounds can be read  from a standard SCALE cross section library file by
specifying the path to the file instead of the array bounds.


.. code-block:: scale
   :caption: ORIGEN "bounds" block.
   :name: fig-origen-bounds-block

   =origen
   bounds{
       neutron=[1e6 1e3 1] %2-group with 1MeV, 1keV, 1eV
       gamma=[100L 1.0e7 1.0e-5] %101 logarithmically spaced bins
       alpha=[1e6 2e7] %high-energy bin between 1 and 20 MeV
       beta=[22I 1 100] %23 linear bins between 1 and 100 eV
       %read neutron bounds from SCALE multi-group library file
       %neutron="scale.rev04.xn252v7.1"
   }
   case{ … }
   end

.. _5-1-3-3-2-3:

Solver Block
""""""""""""

The solver block controls high-level solver options, the most important
of which is the actual solver kernel used, either the default MATREX
(:ref:`5-1-2-2-1`, :numref:`fig-origen-solver-block-matrex`) or
CRAM (:ref:`5-1-2-2-2`, :numref:`fig-origen-solver-block-cram`).

.. code-block:: scale
   :caption: ORIGEN "solver" block for MATREX
   :name: fig-origen-solver-block-matrex

   =origen
   solver{
       type=MATREX    %(DEFAULT)
       opt{
           terms=21   %number of expansion terms (DEFAULT)
           maxp=100   %maximum number of short-lived precursors
                      % for a long-lived nuclide (DEFAULT)
           substeps=1 %number of time step divisions (DEFAULT)
       }
   }
   case{ … }
   end

.. code-block:: scale
   :caption: ORIGEN "solver" block for CRAM
   :name: fig-origen-solver-block-cram

   =origen
   solver{
       type=CRAM
       opt{
           order=16   %order of the method (DEFAULT)
           substeps=1 %number time step divisions (DEFAULT)
       }
   }
   case{ … }
   end


The MATREX kernel contains two parameters that are generally sufficient
with the default values. The minimum number of "terms" is
:math:`n_{terms} =21`, which overrides the heuristic in
:eq:`eq-origen-solver-nterms`. Experience indicates that high flux levels
(e.g., greater than 10\ :sup:`16` n/cm\ :sup:`2`-s) may require more terms.
The second parameter, "maxp," is generally sufficient, describing the amount
of storage available for the short-lived precursors of a long-lived isotope.

The CRAM kernel has a single parameter that impacts the numerical error:
the "order." Both the CRAM and MATREX solver include the "substeps"
parameter that adds substeps to each user-defined time step. Testing the
same input with a different number of substeps (e.g., "substeps=1,"
"substeps=2," "substeps=4") can be a simple way to check that the time
grid is sufficient.

.. _5-1-3-3-2-4:

Options Block
"""""""""""""

The "options" block contains miscellaneous global options that apply to
all cases, as shown in :numref:`fig-origen-options-block`. The "print_xs"
option enables output of the transition matrix **A** used in each case, the
"digits" option enables high-precision output when set to 6, and the
"fixed_fission_energy" allows 200 MeV per fission to be used everywhere
instead of the nuclide-dependent energy release being used by default.

.. code-block:: scale
   :name: fig-origen-options-block
   :caption: ORIGEN "options" block

   =origen
   options{
       print_xs=no             %print cross sections
       digits=4                %digits=6 is high-precision
       fixed_fission_energy=no %set to yes to use 200 MeV/fission
   }
   case{…}
   end

.. _5-1-3-4:

OPUS Module
~~~~~~~~~~~

.. |nbsp| unicode:: U+2713
   :trim:

The analysis of ORIGEN results often involves evaluating large amounts
of output data that may include time-dependent nuclide and element
inventories, radiological decay properties, and neutron, alpha, beta and
photon source spectra. Visualization of the output data from ORIGEN
often provides a means of rapidly evaluating the dominant nuclides in a
problem, identifying important trends in the results, and providing
insight into the problem that is not easily obtained otherwise. The OPUS
utility program has been developed to read and process ORIGEN binary
concentration results file (f71) into a format easily entered into
graphics-plotting packages.

.. _5-1-3-4-1:

Key Features
^^^^^^^^^^^^

The output of OPUS is a PLT file with extension ".plt" which can be
easily read by most graphics packages, including the SCALE GUI Fulcrum.
An example of the PLT file is shown in :numref:`fig5-1-28`.

.. _fig5-1-28:
.. figure:: figs/ORIGEN/fig28.png
  :align: center
  :width: 500

  Example of the OPUS PLT file.

The various types of data that can be returned by OPUS fall into two
separate classes, briefly described as (1) dominant or selected isotopes
or elements and (2) photon, alpha, beta and neutron source spectra.
These requested data may be extracted for either irradiation or decay
time periods of interest. One key feature of the program is that by
default, it will automatically extract the 40 most dominant nuclides or
elements in the problem, rank them using the output response and time
periods of interest as specified by the user, and give the total
response. The returned data may be selected, ranked, and plotted
according to the group (types) of nuclides in the problem. The groups
include the actinides, fission products, activation products, fission
products and actinides, or all nuclides in the problem. The totals are
printed for all nuclides in the specified group, and a subtotal is
generated for all nuclides in the printed list. The user may also
specify any other nuclide or element to be included in the output,
regardless of its importance to the problem. The nuclides may be ranked
using different output units of mass, density, atomic density, activity,
toxicity, decay heat, or isotopic fractions.

Default values are assigned to most input variables, allowing a
comprehensive visual analysis of returned data with relatively little
user input.

.. _5-1-3-4-2:

Input Description
^^^^^^^^^^^^^^^^^

OPUS input records are limited to a maximum of 80 columns. A single data
entry may be entered anywhere in a record but cannot be divided between
two records; however, array-data entries may be divided over many
records. A data entry (from left to right) is composed of a keyword, an
equal sign (=), and numeric or alphanumeric data. A data entry is
illustrated in the following example:

.. code-block:: scale

   title="PWR 33 GWD/MTU 3.3 wt % U-235"

The program identifies keywords either by using only the first four
characters in the keyword name or the full keyword name. In the example
above, "titl" may be used, omitting the "e."\* Alphanumeric data (as
titles or axis labels) must be enclosed in double quotes, with nuclide
or element symbols being the notable exception.

\*
   Unlike in the previous OPUS versions, it is not permitted to enter
   four characters followed by any alphanumeric characters: only full
   keyword names or four-letter short-hands are allowed.

Floating-point data may be entered in various forms; for example, the
value 12340.0 may be entered as 12340, 12340.0, 1.234+4, 1.234E+4,
1.234E4, or 1.234E04. Also, the value 0.012 may be entered as 12E-3,
12-3, 1.2-2, etc. Numeric data must be followed immediately by one or
more blanks.

Array data (alphanumeric floating-point and integer) for an array-type
parameter must always be terminated with an END that does not begin in
column one.

Input parameters in a single OPUS sequence input (i.e., between "=opus"
and "end") may be entered in any order. Usually each sequence input
produces a single plot file with the name "${OUTBASENAME}N.plt" where
${OUTBASENAME} is the base of the input file name, e.g., my.inp has the
base name "my," and "N" is an 18-digit integer that is incremented with
each opus plot.

The OPUS input uses keywords. Keywords, descriptions, and allowed
choices for each entry are listed in :numref:`table-opus-plot` for
plot setup options and :numref:`table-opus-response` for response
units and nuclide selection. Input keywords and their choices occupy the first
column. The next two columns indicate the type of plot in which the keyword
may be entered. The last column is a description of the input keyword.

.. _table-opus-plot:
.. table:: OPUS input for plot setup
  :class: longtable
  :widths: 28 16 10 46

  +----------------------------+------------------+-------------+------------------------------------------------+
  | **Input keywords**         | **Nuclide /**    | **Spectra** |                                                |
  |                            |                  |             |                                                |
  |                            | **element plot** | **plot**    | **Keyword description**                        |
  +============================+==================+=============+================================================+
  | **LIBR**\ ARY= ("")        |                  |             |  ORIGEN binary cross section library (.f33).   |
  |                            |                  |             |  Only required in order to perform reaction    |
  |                            | ✓                | ✓           |  rate calculations (see ABSO and FISS          |
  |                            |                  |             |  units below).                                 |
  +----------------------------+------------------+-------------+------------------------------------------------+
  | **DATA**\ = ("ft71f001")   | ✓                | ✓           |  ORIGEN concentrations file (.f71). If         |
  |                            |                  |             |  enetered, must be enclosed in double quotes.  |
  +----------------------------+------------------+-------------+------------------------------------------------+
  | **TITL**\ E= ("")          | ✓                | ✓           |  Title of plot. If entered, must be enclosed   |
  |                            |                  |             |  in double quotes.                             |
  +----------------------------+------------------+-------------+------------------------------------------------+
  | **TYPA**\ RAMS= (NUCLIDES) | |nbsp|           | |nbsp|      | The type of parameter to be plotted            |
  |                            |                  |             |                                                |
  |     **NUCL**\ IDES         | ✓                | NA          | Request data for the comparison of             |
  |                            |                  |             | individual nuclides                            |
  |                            |                  |             |                                                |
  |     **ELEM**\ ENTS         | ✓                | NA          | Request data for the comparison of             |
  |                            |                  |             | elements                                       |
  |                            |                  |             |                                                |
  |     **ASPE**\ CTRUM        | NA               | ✓           | Request for alpha spectrum                     |
  |                            |                  |             |                                                |
  |     **BSPE**\ CTRUM        | NA               | ✓           | Request for beta spectrum                      |
  |                            |                  |             |                                                |
  |     **GSPE**\ CTRUM        | NA               | ✓           | Request for photon spectrum                    |
  +----------------------------+------------------+-------------+------------------------------------------------+
  | **TYPA**\ RAMS=            | |nbsp|           | |nbsp|      |                                                |
  |                            |                  |             |                                                |
  |     **NSPE**\ CTRUM        | NA               | ✓           | Request for total neutron spectrum from        |
  |                            |                  |             | all sources:                                   |
  |                            |                  |             | - Spontaneous fission                          |
  |                            |                  |             | - :math:`\left(\alpha,n\right)` sources        |
  |                            |                  |             | - Delayed neutron sources                      |
  |                            |                  |             |                                                |
  |     **SFSP**\ EC           | NA               | ✓           | Request for neutron spectrum only              |
  |                            |                  |             | from spontaneous fission                       |
  |                            |                  |             |                                                |
  |     **ANSP**\ EC           | NA               | ✓           | Request for neutron spectrum only              |
  |                            |                  |             | from :math:`\left(\alpha,n\right)`             |
  |                            |                  |             | reactions                                      |
  |                            |                  |             |                                                |
  |     **DNSP**\ EC           | NA               | ✓           | Request for neutron spectrum only              |
  |                            |                  |             | from delayed neutrons                          |
  +----------------------------+------------------+-------------+------------------------------------------------+
  | **FACTOR**\ =              | ✓                | NA          | User-defined multiplicative factor for all     |
  |                            |                  |             | concentrations                                 |
  +----------------------------+------------------+-------------+------------------------------------------------+
  | **VOLUME**\ =              | ✓                | NA          | Material volume in cm :sup:`3`; required when  |
  |                            |                  |             | plotting in units of grams/cm :sup:`3` or      |
  |                            |                  |             | atoms/barn-cm                                  |
  +----------------------------+------------------+-------------+------------------------------------------------+
  | **XLAB**\ EL=              | ✓                | ✓           | X- and Y-axis labels. If this parameters is    |
  |                            |                  |             | not entered, a label is generated              |
  |                            |                  |             | automatically. If entered, it must be enclosed |
  | **YLAB**\ EL=              |                  |             | in double quotes                               |
  +----------------------------+------------------+-------------+------------------------------------------------+
  | **COLS**\ = (YES)          |                  |             | Print nuclide edits by colummn (one nuclide    |
  |                            |                  |             | per column)                                    |
  |     **YES**                | ✓                | NA          |                                                |
  |                            |                  |             |                                                |
  |     **NO**                 |                  |             |                                                |
  +----------------------------+------------------+-------------+------------------------------------------------+
  | **ROWS**\ = (YES)          |                  |             | Print nuclide edits by colummn (one nuclide    |
  |                            |                  |             | per row)                                       |
  |     **YES**                | ✓                | NA          |                                                |
  |                            |                  |             |                                                |
  |     **NO**                 |                  |             |                                                |
  +----------------------------+------------------+-------------+------------------------------------------------+
  | **TIME**\ = (DAYS)         | ✓                | NA          | Unit of time to be plotted                     |
  |                            |                  |             |                                                |
  |     **SECO**\ NDS          | ✓                | NA          | Time plotted in seconds                        |
  |                            |                  |             |                                                |
  |     **MINU**\ TES          | ✓                | NA          | Time plotted in minutes                        |
  |                            |                  |             |                                                |
  |     **HOUR**\ S            | ✓                | NA          | Time plotted in hours                          |
  |                            |                  |             |                                                |
  |     **YEAR**\ S            | ✓                | NA          | Time plotted in years                          |
  +----------------------------+------------------+-------------+------------------------------------------------+


.. _table-opus-response:
.. table:: OPUS input for response units and nuclide selection
  :class: longtable
  :widths: 25 16 16 43

  +--------------------+------------------+-------------+-----------------------------------------------+
  | **Input keywords** | **Nuclide /**    | **Spectra** | **Keyword description**                       |
  |                    |                  |             |                                               |
  |                    | **element plot** | **plot**    |                                               |
  +====================+==================+=============+===============================================+
  | **NRAN**\K=(40)    | ✓                | N/A         | Total number of nuclides or elements to be    |
  |                    |                  |             | returned for the plot. If user-selected       |
  |                    |                  |             | nuclides or elements are requested (see       |
  |                    |                  |             | SYMNUC), output will include these nuclides   |
  |                    |                  |             | plus any remaining ones with the highest      |
  |                    |                  |             | rankings for the quantity specified. The      |
  |                    |                  |             | total and subtotal are always printed.        |
  |                    |                  |             |                                               |
  |                    |                  |             | Default is not used if SYMNUC is entered.     |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **UNITS**\ =       | ✓                | N/A         | Requested data units                          |
  |                    |                  |             |                                               |
  |     (GATO)         |                  |             | Gram-atoms are default for nuclide /          |
  |                    |                  |             | element plots, and particles / MeV-sec are    |
  |     (INTENSITY)    |                  |             | default for spectrum plots                    |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **ABSO**\ RPTIONS  | ✓                | N/A         | Absorption / removal rate (using removal XS   |
  |                    |                  |             | on library)                                   |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **AIRM**\ \**3     | ✓                | N/A         | Radiotoxicity; cubic meters of air to dilute  |
  |                    |                  |             | to RCG\ :sub:`a`                              |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **APEL**\ EM       | ✓                | N/A         | Atom \% of element; isotopic atom percentages |
  |                    |                  |             | of all elements specified in SYMNUC           |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **ATOM**\ S / B-CM | ✓                | N/A         | Atoms/barn-cm; requires VOLUME entry          |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **BECQ**\ UERELS   | ✓                | N/A         | Radioactivity, Bq.                            |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **CAPT**\ URES     | ✓                | N/A         | Capture reaction rate (removal minus fission; |
  |                    |                  |             | not equivalent to radiative capture)          |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **CURI**\ ES       | ✓                | N/A         | Radioactivity, Ci                             |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **FISS**\ IONS     | ✓                | N/A         | Fission reaction rate (using XS on library).  |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **GAMW**\ ATTS     | ✓                | N/A         | Gamma-ray thermal power, watts                |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **GATO**\ MS       | ✓                | N/A         | Gram atoms, gram-atomic weights or moles      |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **GPER**\ CM**3    | ✓                | N/A         | Partial density, grams/cm\ :sup:`3`; requires |
  |                    |                  |             | VOLUME entry                                  |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **GRAM**\ S        | ✓                | N/A         | Mass, grams                                   |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **H2OM**\ \**3     | ✓                | N/A         | Radiotoxicity; cubic meters of water to       |
  |                    |                  |             | required to dilute to to RCG\ :sub:`w`        |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **KILO**\ GRAMS    | ✓                | N/A         | Mass, kilograms                               |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **WPEL**\ EM       | ✓                | N/A         | Weight \% of element; isotopic weight         |
  |                    |                  |             | percentages of all elements specified in      |
  |                    |                  |             | SYMNUC                                        |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **WATT**\ S        | ✓                | N/A         | Total thermal power, watts                    |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **PART**\ ICLES    | N/A              |  *          | Print spectra in units of particles/sec       |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **INTEN**\ NSITY   | N/A              |  *          | Print spectra in units of particles/MeV-sec   |
  |                    |                  |             | (normalized to energy bin width)              |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **ENER**\ GY       | N/A              |  *          | Print spectra in units of MeV/MeV-s           |
  |                    |                  |             | (normalized to energy bin width; multiplied   |
  |                    |                  |             | by mean bin energy)                           |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **LIBT**\ YPE=(ALL)| ✓                | N/A         | Seleccts sublibrary(ies) to include for       |
  |                    |                  |             | nuclide/element plots.                        |
  |                    |                  |             |                                               |
  |                    |                  |             | **Does not apply to  spectrum plots.**        |
  +--------------------+------------------+-------------+-----------------------------------------------+
  |      **LITE**      | ✓                | N/A         | Include only nuclides in the light-nuclide /  |
  |                    |                  |             | activation product sublibrary                 |
  +--------------------+------------------+-------------+-----------------------------------------------+
  |      **ACT**       | ✓                | N/A         | Include only nuclides in the actinide         |
  |                    |                  |             | sublibrary                                    |
  +--------------------+------------------+-------------+-----------------------------------------------+
  |      **FISS**      | ✓                | N/A         | Include only nuclides in the fission product  |
  |                    |                  |             | sublibrary                                    |
  +--------------------+------------------+-------------+-----------------------------------------------+
  |      **FISSACT**   | ✓                | N/A         | Include nuclides in both the fission product  |
  |                    |                  |             | and actinide sublibraries                     |
  +--------------------+------------------+-------------+-----------------------------------------------+
  |      **ALL**       | ✓                | N/A         | Include all nuclides across all sublibraries  |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **SYMN**\ UC=      | ✓                | N/A         | Symbolic notation of nuclides or elements     |
  |                    |                  |             | requested in the plot data. The list is an    |
  |                    |                  |             | array terminated with an END.                 |
  |                    |                  |             |                                               |
  |                    |                  |             | Nuclide entry is by chemical symbol and mass  |
  |                    |                  |             | number, separated by a dash "--". Metastable  |
  |                    |                  |             | states are indicated with an "m" immediately  |
  |                    |                  |             | following the mass number (e.g.,              |
  |                    |                  |             | :sup:`242m`\ Am). Element entry is by         |
  |                    |                  |             | chemical symbol only (e.g., Pu)               |
  |                    |                  |             |                                               |
  |                    |                  |             | For nulide entry, it is also allowed to use   |
  |                    |                  |             | element identifiers; in such cases, all       |
  |                    |                  |             | isotopes of the element found in the ORIGEN   |
  |                    |                  |             | library are used.                             |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **SORT**\ =        | ✓                | N/A         | Option to sort user-requested nuclides input  |
  |                    |                  |             | via the SYMNUC array by descending order of   |
  |                    |                  |             | importance. If SORT is not given or is        |
  |                    |                  |             | SORT=NO, the order of the nuclides in the     |
  |                    |                  |             | plot table is the same order as in the input. |
  |                    |                  |             |                                               |
  |                    |                  |             | Options that can be given to SORT are the     |
  |                    |                  |             | same as for UNITS. If SORT=YES, the same      |
  |                    |                  |             | units provided in the UNITS entry are used.   |
  +--------------------+------------------+-------------+-----------------------------------------------+
  | **RESP**\ ONSE=    | ✓                | N/A         | Optional, user-specified arbitrary response   |
  |                    |                  |             | conversion factor array. These factors are    |
  |                    |                  |             | applied to the individual nuclides after      |
  |                    |                  |             | conversion to quantities in the units         |
  |                    |                  |             | requested by UNITS.                           |
  |                    |                  |             |                                               |
  |                    |                  |             | Entries are in nuclide ID-response factor     |
  |                    |                  |             | pairs. Nuclide identifiers are entered as     |
  |                    |                  |             | legacy ORIGEN ZZAAAI 6-digit integer IDs,     |
  |                    |                  |             | where the isomeric state is the last digit.   |
  |                    |                  |             |                                               |
  |                    |                  |             | The array must be terminated with an END.     |
  +--------------------+------------------+-------------+-----------------------------------------------+


The default values are given in parentheses after the input keyword
definitions. Only the first four characters of any keyword (the letters
are in bold) plus the "=," are required; they can be used instead of the
full keyword name. However, unlike in previous versions of OPUS, the
only two options accepted are the full keyword name or its first four
letters. The keyword default value is listed in parentheses, and values
are provided for almost all numeric input and axis labels. For example,
the user has the option to enter axis labels using XLABEL= and YLABEL=
entries, or "built-in" axis labels based on the time units and the type
of data units can be used.

The remaining sections give more detail on the nuclide/element plots,
the spectra plots, and time range, and case selection to further filter
the results on an f71 file.

.. _5-1-3-4-2-1:

Nuclide/element plots
"""""""""""""""""""""

Various responses may be returned either by nuclide or by element, as a
function of time, for a specified time interval. By default, the top
nuclides/elements contributing to the response of interest over the time
range are returned. An explicit list of nuclides/elements can also be
entered, in which case these nuclides will always be included,
regardless of their ranking. Results for nuclides in specific
sublibraries may be filtered (e.g., to only see output of :sup:`155`\ Gd
the fission product (FP) sublib and not the light nuclide version [LT]
sublib. The default behavior is to sum over all sublibs.

Response totals are always generated for each plot. These totals
represent the sum over all nuclides or elements in the specified library
type. In addition, a subtotal is printed (both in the printout and the
plot file) that represents the sum over the printed nuclides or
elements. The subtotal can be very useful in identifying whether the
nuclides in the printed list include all of the dominant nuclides in the
problem.

OPUS allows the user to sort using any of the provided concentration
units. For each nuclide/element, approximate integral value over all
selected time steps is calculated in the selected units;
nuclides/elements are then ranked according to this value. The NRANK
cutoff is applied after the sort has been performed.

It is permitted to enter SORT=YES, which is equivalent to setting SORT=
to the same value as UNITS=.

If the SORT key is not entered, nuclides/elements are sorted according
to their position in the SYMNUC array.

.. _5-1-3-4-2-2:

Spectra plots
"""""""""""""

Alpha, beta, photon and neutron energy spectra calculated by ORIGEN may
also be stored on the f71 file, and plotted by OPUS. One difference in
the units of the spectra returned by OPUS and those printed by ORIGEN is
that the intensities are typically converted from units of photons/s
(stored on f71 file) to *particles/s-MeV* by dividing by the
energy-group width. This conversion produces intensities that are more
easily comparable across different energy groups and energy-group
structures. Energy-intensity spectra in units of *MeV/s-MeV* and
intensity spectra in units of *particles/s* may also be requested.

.. _5-1-3-4-2-3:

Selection of plotting data
""""""""""""""""""""""""""

OPUS provides four basic options for selecting a subset of the data on
an f71 file:

  1. a range of times with TMIN and TMAX (floating point numbers),

  2. a range of positions on the f71 file with MINPOSITION and MAXPOSITION
     (integers),

  3. a single CASE selection, and

  4. a list of positions in the NPOSITION list.

A full overview of keywords that can be entered for time point selection
is given in :numref:`table-opus-data`.

If no selection inputs are used, all available steps on the
concentration file are printed. Range bounds (CASE, TMIN, TMAX,
MINPOSITION, MAXPOSITION) are used as independent constraints, so any
combination of those can be supplied, in which case all of the specified
constraints are applied.

In case invalid positions are specified in the NPOSITION array, an error
is raised, and no valid output is produced; the same happens if no steps
fit into the specified selection.

The case number is useful for ORIGEN stacked cases. Furthermore, TRITON
stores the mixture number (with 0 for the sum of all depletion materials
and -1 for the sum of selected materials) as the case number, so this
option can be used to obtain a plot of the desired depletion mixture
without actually knowing the time step numbers=. When an ORIGEN f71 file
is accessed, a table of contents is printed in the output (.out) file.
This can be very useful for understanding what is contained on the f71
at each position.

.. _table-opus-data:
.. table:: OPUS input keywords for data set selection
  :widths: 25 15 60

  +--------------------+----------+------------------------------------+
  | Input keywords     | Type     | Keyword description                |
  +====================+==========+====================================+
  | **NPOS**\ ITION=   | Array    | List of all requested position     |
  |                    |          | numbers of data (on NUMUNIT), in   |
  |                    |          | ascending order. No other entries  |
  |                    |          | are required since NPOSITION is a  |
  |                    |          | unique data set identifier.        |
  |                    |          | Terminate with END.                |
  |                    |          |                                    |
  |                    |          | NPOSITIONS cannot be specified     |
  |                    |          | together with any of TMIN, TMAX,   |
  |                    |          | MINPOSITION or MAXPOSITION.        |
  |                    |          |                                    |
  |                    |          | If none of the position selectors  |
  |                    |          | is entered, all available          |
  |                    |          | positions on the data file will be |
  |                    |          | returned.                          |
  +--------------------+----------+------------------------------------+
  | **CASE**\ =        | Variable | Number of ORIGEN case (or, a       |
  |                    |          | mixture number for TRITON-produced |
  |                    |          | f71 files).                        |
  +--------------------+----------+------------------------------------+
  | **MINP**\ OSITION= | Variable | Minimum position number, used to   |
  |                    |          | request a range of positions       |
  +--------------------+----------+------------------------------------+
  | **MAXP**\ OSITION= | Variable | Maximum position number            |
  |                    |          |                                    |
  |                    |          | All positions between MINPOSITION  |
  |                    |          | and MAXPOSITION, inclusive, are    |
  |                    |          | requested.                         |
  |                    |          |                                    |
  |                    |          | MINPOSITION and/or MAXPOSITION     |
  |                    |          | cannot be specified together with  |
  |                    |          | NPOSITIONS, but they can be        |
  |                    |          | specified at the same time as TMIN |
  |                    |          | and/or TMAX. Up to all four        |
  |                    |          | conditions (TMIN, TMAX,            |
  |                    |          | MINPOSITION, MAXPOSITION) will be  |
  |                    |          | used to constraint the selected    |
  |                    |          | time points.                       |
  |                    |          |                                    |
  |                    |          | If none of the position selectors  |
  |                    |          | is entered, all available          |
  |                    |          | positions on the data file will be |
  |                    |          | returned.                          |
  +--------------------+----------+------------------------------------+
  | **TMAX**\ =        | Variable | Minimum and maximum time for       |
  |                    |          | selection of positions on the data |
  | **TMIN**\ =        | Variable | file. The units of TMAX and TMIN   |
  |                    |          | are the same as for TIME.          |
  |                    |          |                                    |
  |                    |          | TMIN and/or TMAX cannot be         |
  |                    |          | specified together with            |
  |                    |          | NPOSITIONS, but they can be        |
  |                    |          | specified at the same time as      |
  |                    |          | MINPOSITION and/or MAXPOSITION. Up |
  |                    |          | to all four conditions (TMIN,      |
  |                    |          | TMAX, MINPOSITION, MAXPOSITION)    |
  |                    |          | will be used to constraint the     |
  |                    |          | selected time points.              |
  |                    |          |                                    |
  |                    |          | If none of the position selectors  |
  |                    |          | is entered, all available          |
  |                    |          | positions on the data file will be |
  |                    |          | returned.                          |
  +--------------------+----------+------------------------------------+

.. _5-1-3-4-3:

Plot File Formats
^^^^^^^^^^^^^^^^^

The plot file produced by OPUS is a text file that contains plot
information, including the title, axis labels, plot type, and the
time-dependent data for inventory-type plots or energy-dependent data
for spectral-type plots. The plot file is a free-format reading, so the
column positions have no particular significance. However, the plot
files created by OPUS are aligned by column to facilitate reading of the
files by other graphics programs.

File header information


The format of the first five records of the plot file is common to all
plot types. They are:

**Record 1:** TITL - problem title (maximum 32 characters)

**Record 2:** XHEA - x-axis label (maximum 20 characters)

**Record 3:** YHEA. y-axis label (maximum 20 characters)

**Record 4:** Plot type - The type of plot is selected by the words
"nuclide," "element," "case," or "spec." The nuclide and element entries
have the same effect and produce time-dependent plots of individual
nuclides or elements in the specified units. The "case" entry is used to
identify case comparisons of total quantities or individual nuclides.
The "spec" entry identifies spectral-type plots.

The remaining records and formats depend on the plot type specified in
Record 4.

Nuclide and element plot types


**Record 5:** NPTONC, KTOT - the number of time points (x-axis) for the
plot data KTOT - the number of nuclides or elements in the plot;
includes the last record that contains the totals, if present

**Record 6:** TIMES(NPTONC) - NPTONC entries for the times associated
with each data point; units are in the units specified in Record 2
(XHEA)

**Record 7:** SYMBOL, (X(N,I), I=1, NPTONC) - symbol is the alphanumeric
symbol for the nuclide or element. No spaces are permitted in PlotOPUS.
This symbol entry is followed by NPTONC entries containing the plot data
for the nuclide or element SYMBOL with index N.

**Record 8:** Record 7 is repeated for all KTOT nuclides or elements.

**Record 7+KTOT:** Last record - contains the totals or other related
quantity for the plot. The record has the same format as Record 7.

Spectral plot types


**Record 5:** NPTONC, NGP - the number of entries that follow to
construct the spectral histogram, where NGP=(NG+1)*2 and NG is the
number of energy groups. The histogram is made using a series of
connecting lines, and therefore does not require any special histogram
plotting capability in the graphics code.

**Record 6:** EN, YY - Each record contains a pair of entries: EN is the
energy (MeV), and YY is the value for energy EN.

Repeat Record 6 NGP times.

Case comparison plot types


**Record 5:** NCAS - the negative value of the total number of cases in
the plot

**Record 6:** NPTONC - the number of time points (x-axis) for the plot
data for the case (non-user-entered data)

**Record 7:** INPOIN the number of time points (x-axis) for the plot
data for user-entered data

**Record 8:** XINP(INPOIN) - INPOIN entries for the times associated
with each data point of the user-entered data

**Record 9:** YINP(INPOIN) - INPOIN entries containing the plot data for
the user-entered data

**Record 10:** LEGEND - legend for the user-entered data case.

The remaining records contain the case comparison data for the
non-user-input data. Repeat records 7, 8, 9, and 10 for the case
comparison plots, NPTONC times (same as case comparisons with no
user-entered data).

.. _5-1-4:

Examples
--------

The main problems solvable by the ORIGEN family of codes are enumerated
below (with relevant components in parentheses).

  1. Decay (ORIGEN)

  2. Activation (COUPLE+ORIGEN)

  3. Fuel irradiation (ARP+ORIGEN or ORIGAMI)

  4. Emission spectra from decay (ORIGEN)

  5. Processing, including batch/continuous chemical removal, isotopic
     feed, and stream blending (ORIGEN)

  6. Unit conversions (OPUS)

Examples of the six variations above are contained in the following
sections, except for fuel irradiation problems with ORIGAMI, as
described in its own chapter.

.. _5-1-4-1:

Decay of :sup:`238`\ U
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: scale
   :caption: Decay of :sup:`238`\ U
   :name: fig-origen-u238-decay

   =origen
   case{
       % use ENDF/VII-based decay library
       lib{ file="end7dec" }

       % create a material with 1 gram U-238
       mat{
           units=GRAMS
           iso=[u238=1.0]
       }
       time=[20L 1.0 1e9] %default units are days

       % save all information to f71
       save=yes
   }
   end


:numref:`fig-origen-u238-decay` illustrates using the "end7dec" binary decay
library and decaying one gram of :sup:`238`\ U for 10\ :sup:`9` days using
the logarithmic array shortcut to put 20 logarithmically spaced values between
1.0 and 1e9 days.

.. _5-1-4-2:

:sup:`252`\ Cf neutron Emission Spectrum
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: scale
   :caption: :sup:`252`\ Cf neutron emission spectrum.
   :name: fig-origen-cf252-decay

   =origen

   bounds{
       neutron=[ 2.000000e+07 6.376300e+06 3.011900e+06 1.826800e+06
               1.422700e+06 9.071800e+05 4.076200e+05 1.110900e+05 1.503400e+04
               3.035400e+03 5.829500e+02 1.013000e+02 2.902300e+01 1.067700e+01
               3.059000e+00 1.855400e+00 1.300000e+00 1.125300e+00 1.000000e+00
               8.000000e-01 4.139900e-01 3.250000e-01 2.250000e-01 1.000000e-01
               5.000000e-02 3.000000e-02 1.000000e-02 1.000000e-05 ]
   }

   case{
       title="Cf-252 decay"

       lib{ file="end7dec" pos=1 }

       time{
          units=YEARS
          t=[ 0.01 0.03 0.1 0.3 1 3 10 ]
       }

       mat{
          units=CURIES
          iso=[cf252=1.0]
       }

       %perform neutron calculation with defaults
       neutron=yes

       print{
          neutron{
              summary=yes
              spectra=yes
              detailed=yes
          }
       }
   }
   end


:numref:`fig-origen-cf252-decay` illustrates decay of 1 Ci of :sup:`252`\ Cf for ten years
with calculation of the time- and energy-dependent neutron source. The
case uses the binary decay library "end7dec." The neutron energy group
structure is defined in the bounds block with array "neutron."

.. _5-1-4-3:

Simple Fuel Irradiation Plus Decay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:numref:`fig-origen-simple` illustrates the input for irradiation of a fuel
assembly for 200 days at 15 MW in case "irrad," followed by decay for 5 years
in the next case, "decay." The ORIGEN library (f33) was prepared by ARP to
have a single position with a burnup of 1500 MWd/MTU. The input material
has been specified to have 1 MTU total with an enrichment of 4.0% in
:sup:`235`\ U. Note that there are consistency requirements between ARP
and ORIGEN that cannot be checked by either module. Namely, the
enrichment specified in ARP should be equivalent to the effective
enrichment specified in the ORIGEN input, and the burnup-dependent cross
section data on the ORIGEN library should be for the *midpoint burnup of
the case*, which requires consistency between the operating history
(power and time) and the initial isotopics heavy metal loading. In
typical fuel depletion calculations, it is most convenient to specify a
metric ton (10\ :sup:`6` grams) of initial heavy metal, such that the
power in MW may be interpreted as MW/MTIHM. In the above example, the
power history does not need to be constant but when combined with the
time values should produce an average burnup of 1500 MWd/MTU in order
that the cross sections interpolated by ARP in position 1 are valid.


.. code-block:: scale
   :caption: Simple fuel irradiation plus decay.
   :name: fig-origen-simple

   =arp
   'library type
   w17x17
   'wt%
   4.0
   'number of cycles
   1
   'number of days per cycle
   200.0
   'cycle-average specific power (MW/MTU)
   15.0
   'number of interpolated cross section sets generated per cycle
   1
   'moderator density (g/cc)
   0.723
   'interpolated output ORIGEN library
   w17x17_100d.f33
   end
   =origen
   case(irrad){
       % use xs data at pos=1 corresponds to midpoint burnup (200 d * 15MW/MTU)/2
       lib {
            file="w17x17_100d.f33" pos=1
       }
       % 1 MT of enriched uranium
       mat {
           units=GRAMS
           iso=[u234=356 u235=40000 u236=184 u238=959460]
       }
       % power history (at least 4 steps for MATREX)
       time=[ 50 100 150 200 ] %default time in days
       power=[ 15 15 15 15 ] %power in MW
   }
   case(decay){
       time{
           units=YEARS
           start=0 %start time at 0 in this case for ease of input for t[]
           t=[0.1 0.3 0.9 1 2 3 4 5] %observe rule of threes
       }
       save{ file="discharge.f71" steps=[0 LAST] } %only save begin and end
   }
   end


It is important to note that with the MATREX solver, used by default,
the recommendation for irradiation and decay of spent fuel is to use no
fewer than four steps for the irradiation and begin the decay period
with a time step on the order of weeks or a month, increasing the
interval for each subsequent step by no more than a factor of three. In
many continuation cases, such as the decay case described here, it is
convenient to specify times starting from zero for the case with
"start=0" in the time block.

.. _5-1-4-4:

Three Cycles of Irradiation Plus Decay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:numref:`fig-origen-3cycle` is similar to the previous one, except there are
three sets of burnup-dependent transition cross sections (positions) generated
by ARP and used in ORIGEN, and there are three cases, one corresponding to
each cycle. Neutron and gamma sources are generated and saved to the f71
file for the final decay case. The maximum burnup achieved is 60 GWd/MTIHM.


.. code-block:: scale
   :caption: Three cycles of irradiation plus decay
   :name: fig-origen-3cycle

   =arp
   w17x17
   4.0
   3
   500 500 500
   40.0 40.0 40.0
   1 1 1
   0.723
   ft33f001
   end

   =origens
   bounds{ neutron="xn27g19v7.0"
           gamma=[1e+7 8e+6 6.5e+6 5e+6 4e+6 3e+6 2.5e+6 2e+6 1.66e+6 1.33e+6 1e+6
                  8e+5 6e+5 4e+5 3e+5 2e+5 1e+5 5e+4 1e+4]}
   case(c1){
       lib{ file="ft33f001" pos=1 }
       time=[8i 50 500]
       power=[10r40]
       mat{ iso=[u235=4e3 u238=960e3] }
   }
   case(c2){
       lib{ pos=2 }
       time=[8i 550 1000]
       power=[10r40]
   }
   case(c3){
       lib{ pos=3 }
       time=[8i 1050 1500]
       power=[10r40]
   }
   case(cool){
       time{ start=0 t=[20L 0.001 100] units=YEARS }
       save{ file="snf.f71" time_offset=1500 }
    gamma{ sublib=ALL brem_medium=UO2 }
    print{ neutron{ spectra=yes } }
    neutron{ alphan_medium=UO2 }
    }
    end

.. _5-1-4-5:

Load Isotopics from an f71 File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The "mat" block allows isotopics to be loaded from any position on an
existing f71 file, as seen in :numref:`fig-origen-load-mat`. A table of
contents is printed in the output file every time an f71 is read or written.
Inspection of this table can help identify the appropriate position on the
f71, as shown in :numref:`fig-origen-f71-toc`, extracted
from the output file.


.. code-block:: scale
   :caption: Load isotopics from an f71 file using the "mat" block and perform a follow-on decay.
   :name: fig-origen-load-mat

   'copy existing f71 file from input file directory to working directory
   =shell
   cp ${INPDIR}/discharge.f71 discharge2.f71
   end

   =origen
   case(restart){
       % decay only library
       lib {
           file="end7dec" pos=1
       }
       % must know correct position
       mat {
           load{ file="discharge2.f71" pos=2 }
       }
       % continue timeline from previous case ending at 5 years
       time{
           units=YEARS
           start=5
           t=[10 20 40 80 160]
       }
       % append to file
       save{
           file="discharge2.f71" steps=[1 2 3 4 5]
       }
   }
   end


.. code-block:: scale
   :caption: Table of contents printed when accessing the f71 file.
   :name: fig-origen-f71-toc

   ==================================================================================
   = Restart F71 File for case 'restart' (#1/1) =
   ----------------------------------------------------------------------------------
   Data taken from position: 2
   index time power flux fluence burnup libpos case step DCGNAB
       1 0.00000e+00 0.00000e+00 0.00000e+00 0.00000e+00 3.00000e+03 1 2 0 DC----
       2 1.57800e+08 0.00000e+00 0.00000e+00 0.00000e+00 3.00000e+03 1 2 8 DC----
   D - state definition present
   C - concentrations present
   G - gamma emission spectra present
   N - neutron emission spectra present
   A - alpha emission spectra present
   B - beta emission spectra present


The simple input in :numref:`fig-origen-load-rename` can be used to print
contents of an existing f71 file. The file is renamed so that it does
not have extension ".f71." This prevents the automatic copy back from the
working directory to the input file directory. Note that the same is true
with any ORIGEN libraries that have the extension ".f33." There is a rule
in place that *any* file in the working directory with extension ".f71" or
".f33" is copied back to the input file's directory. To prevent this from
occurring, the ".f71" or ".f33" extensions must not be used in the filename,
or unneeded files with a shell command at the end must be explicitly deleted.

.. code-block:: scale
   :caption: Isotopics from an f71 or f33 file.
   :name: fig-origen-load-rename

   'avoid .f71 extension to prevent automatic copy back
   =shell
   cp /path/to/unknown.f71 f71
   end

   =origen
   case(test){
       lib{ file="end7dec" pos=1 }
       mat{ load{ file="f71" pos=1 } }
       time=[1]
   }
   end

   'remove any *.f71 or *.f33 in the working directory to prevent automatic copy back
   '(not necessary in this example, but for reference)
   =shell
   rm -f *.f71
   rm –f *.f33
   end

.. _5-1-4-6:

Continuous Feed and Removal
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Both continuous feeding of nuclides into a system and chemical removal
of elements from a system are required to simulate molten fuel systems
such as the molten salt reactor (MSR). Simulation of removal can be used
to represent other physical processes such as purification systems
(i.e., removal of chemical species by filtration or ion-exchange columns) and
ventilated systems in which the removal can be represented using a rate
constant (1/s). :numref:`fig-origen-msr` applies to simulation of a molten
salt reactor system, and it uses both continuous feed of :sup:`232`\ Th and
simultaneous removal of fission products according to their removal process.
To actually simulate this system properly, an ORIGEN reactor library
appropriate for the MSR must be generated.

There are 11 groups of nuclides in this example, each with the same
removal constant. The groups, by element and removal rate in units of
(1/s), are

   -  Group 1: Ca to As (3.37 × 10\ :sup:`-9`);

   -  Group 2: Y, La, Ce, Pr, Nd, Pm, Sm, Gd (2.31 × 10\ :sup:`-7`);

   -  Group 3: Eu (2.31 × 10\ :sup:`-8` );

   -  Group 4: Se, Nb, Mo, Tc, Ru, Rh, Pd, Ag, Sb, Te (5 × 10\ :sup:`-2`);

   -  Group 5: Zr, Cd, In, Sn (5.79 × 10\ :sup:`-8`) ;

   -  Group 6: Kr, Xe (5 × 10\ :sup:`-2`);

   -  Group 7: Br, I (1.93 × 10\ :sup:`-7`);

   -  Group 8: Rb, Sr, Cs, Ba (3.37 × 10\ :sup:`-9`);

   -  Group 9: Th, Li, Be, F (3.37 × 10\ :sup:`-9`);

   -  Group 10: Pa (3.86 × 10\ :sup:`-6`); and

   -  Group 11: Np, Pu, Am, Cm, Bk, Cf (1.98 × 10\ :sup:`-9`).

A :sup:`232`\ Th feed rate of 2.0 × 10\ :sup:`-2` grams/s is used.

.. code-block:: scale
   :caption: Demonstration of continuous feed and removal within an ORIGEN irradiation case.
   :name: fig-origen-msr

   =origen
   case{
       title="Single fluid MSR depletion calculation"

       lib{
          file="msr.f33"
          pos=1
       }
       time{
           units=YEARS
           t=[ 8i 0.05 1.0 ]
       }

       power=[ 10r30 ] %30 MW

       %initial material
       mat{
          %FLiBe with pure Li7 and 1 MTIHM loading
          units=GRAMS
          iso =[f=1e7 li7=5e6 be=1e6 th232=9.5e5 u233=0.5e5]

          %continuous feed of th-232
          feed=[th232=2e-2] %g/s
       }

       %continuous removal by element using atomic numbers
       processing{ removal{rate=3.37e-9 ele=[12i 20 33]}
                   removal{rate=2.31e-7 ele=[39 57 58 59 60 61 62 64]}
                   removal{rate=5.79e-8 ele=[40 48 49 50]}
                   removal{rate=5e-2 ele=[36 54]}
                   removal{rate=1.93e-7 ele=[35 53]}
                   removal{rate=3.37e-9 ele=[37 38 55 56]}
                   removal{rate=3.37e-9 ele=[90 3 4 9]}
                   removal{rate=3.86e-6 ele=[91]}
                   removal{rate=1.98e-9 ele=[93 94 95 96 97 98]}
       }

       print{
            cutoffs=[ GRAMS=0.1 ] %do not show grams < 0.1% of total
            nuc{ units=[GRAMS] total=yes }
            kinf=yes   %print k-infinity summary
            absfrac_sublib=LT %absorption fractions for light nuclides in FLiBe
       }
   } %end case
   end

The absorption rates, fission rates, and k-infinity values are printed
during irradiation, which can be used to evaluate the influence of the
feed rates and removal constants on the time-dependent reactor
performance. For the MSR in particular, the ability to self-sustain can
be assessed from the "k-infinity" summary output, enabled by "kinf=yes"
in print block (as well as the absorption fractions in the light
nuclides in FLiBe), and enabled by "absfrac_sublib=LT" in the print
block (:numref:`fig-origen-msr-history`). This example uses pure Li-7, whereas
if natural Li is used, one will see a much larger fraction of absorptions in
Li-6 and much lower "k-infinity."


.. code-block:: scale
   :caption: Continuous feed and removal--history overview.
   :name: fig-origen-msr-history

   =============================================================================================
   = History overview for case '1' (#1/1)
   = Single fluid MSR depletion calculation
   ---------------------------------------------------------------------------------------------
      step          t0          t1          dt           t        flux     fluence       power      energy
       (-)         (y)         (y)         (s)         (s)   (n/cm2-s)     (n/cm2)        (MW)       (MWd)
         1      0.0000      0.0500  1.5780E+06  1.5780E+06  1.9782E+13  3.1217E+19  3.0000E+01  5.4792E+02
         2      0.0500      0.1556  3.3313E+06  4.9093E+06  2.0112E+13  9.8216E+19  3.0000E+01  1.7046E+03
         3      0.1556      0.2611  3.3313E+06  8.2407E+06  2.0575E+13  1.6676E+20  3.0000E+01  2.8613E+03
         4      0.2611      0.3667  3.3313E+06  1.1572E+07  2.1057E+13  2.3691E+20  3.0000E+01  4.0181E+03
         5      0.3667      0.4722  3.3313E+06  1.4903E+07  2.1557E+13  3.0872E+20  3.0000E+01  5.1748E+03
         6      0.4722      0.5778  3.3313E+06  1.8235E+07  2.2075E+13  3.8226E+20  3.0000E+01  6.3315E+03
         7      0.5778      0.6833  3.3313E+06  2.1566E+07  2.2613E+13  4.5759E+20  3.0000E+01  7.4882E+03
         8      0.6833      0.7889  3.3313E+06  2.4897E+07  2.3171E+13  5.3478E+20  3.0000E+01  8.6449E+03
         9      0.7889      0.8944  3.3313E+06  2.8229E+07  2.3750E+13  6.1390E+20  3.0000E+01  9.8016E+03
        10      0.8944      1.0000  3.3313E+06  3.1560E+07  2.4351E+13  6.9502E+20  3.0000E+01  1.0958E+04

                 step - step index within this case
                   t0 - time at beginning-of-step in input units
                   t1 - time at end-of-step in input units
                   dt - length of step in seconds
                    t - end-of-step cumulative time in seconds
                 flux - flux in neutrons/cm^2-sec (CALCULATED)
              fluence - cumulative end-of-step fluence in neutrons/cm^2 (CALCULATED)
                power - power in mega-watts (INPUT)
               energy - cumulative end-of-step energy released in mega-watt-days (INPUT)
   =============================================================================================


   =============================================================================================
   =   Overall neutron balance for case '1' (#1/1)
   =   Single fluid MSR depletion calculation
   ---------------------------------------------------------------------------------------------
                          0.0E+00y    5.0E-02y    1.6E-01y    2.6E-01y    3.7E-01y    4.7E-01y
   n-production           2.9579E+18  2.9272E+18  2.9110E+18  2.9123E+18  2.9138E+18  2.9154E+18
   n-absorption           2.6018E+18  2.6178E+18  2.6858E+18  2.7707E+18  2.8583E+18  2.9489E+18
   k-inf                  1.1369E+00  1.1182E+00  1.0838E+00  1.0511E+00  1.0194E+00  9.8864E-01
   =============================================================================================

   =============================================================================================
   =   Fraction of absorption rate for light elements for case '1' (#1/1)
   =   Single fluid MSR depletion calculation
   ---------------------------------------------------------------------------------------------
               0.0E+00y    5.0E-02y    1.6E-01y    2.6E-01y    3.7E-01y    4.7E-01y
   f-19        9.5276E-02  9.4189E-02  9.2293E-02  9.0506E-02  8.8782E-02  8.7113E-02
   be-9        9.4833E-02  9.3751E-02  9.1862E-02  9.0083E-02  8.8366E-02  8.6704E-02
   li-7        6.3293E-02  6.2572E-02  6.1312E-02  6.0125E-02  5.8980E-02  5.7871E-02
   li-6        0.0000E+00  5.6409E-04  1.7104E-03  2.8000E-03  3.8355E-03  4.8190E-03
   he-3        0.0000E+00  2.9340E-08  7.1009E-07  3.0708E-06  7.9374E-06  1.5939E-05
   o-16        0.0000E+00  4.3552E-08  1.3502E-07  2.2606E-07  3.1678E-07  4.0728E-07

   *{list continues}*

.. _5-1-4-7:

Calculate Fuel :math:`\left(\alpha,n \right)` Emissions in a Glass Matrix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Batch processing options are provided to separate various components of
the nuclide compositions into different streams and to recombine the
streams to form new compositions. This example applies to the
irradiation of typical commercial fuel and subsequent storage of
separated fission products and actinides from fuel in a glass matrix.
The matrix is important in determining the :math:`\left(alpha,n\right)` component of the
neutron source because the alpha particles interact with the light
element constituents in the matrix, with :math:`\left(alpha,n\right)` yields corresponding to
the medium containing the :math:`\alpha`-emitting nuclides. Therefore, an accurate
calculation of the neutron source in a glass matrix requires combining
the oxide fuel compositions after irradiation with the defined glass
matrix. The calculation could be performed by creating a case by
manually entering the calculated nuclide activities and the matrix
composition. However, this is only practical if the number of source
nuclides is small. This example applies batch processing and blending
options to generate the required compositions.

The blending option is used to combine two streams: one stream from
irradiated fuel, and the other stream defining the glass matrix
composition.

An irradiation case—-"irrad"-—is performed first to generate spent nuclear
fuel compositions. The next case "spent" decays the results for one
year. At the start of the decay, only selected elements are retained in
the stream by performing processing with the "retained" array. In this
example, all elements are removed except for Se (99.8%); Rb, Sr, Te, Cs,
Ba, Dy (77.8%); and U, Np, Pu, Am, Cm (1%).

The glass matrix compositions are then defined in the third case,
"glass."

The final case—"blend"—blends 10% of each the last step's isotopics from the
"spent" and "glass" cases. To test the dependence on the time when the blend
is performed, the blend can be changed to "blend=[spent(N)=0.1 glass=0.1 ],"
where *N* is the index of the step from which to take isotopics from the
spent case.

.. code-block:: scale
   :caption: Continuous feed and removal--blending option.
   :name: fig-origen-blending

   =arp
   w17x17
   3
   1
   360
   40
   1
   0.723
   fuellib
   end

   =origen
   bounds{
       neutron=[ 1.00E-05 1.00E-02 3.00E-02 5.00E-02 1.00E-01 2.25E-01
                 3.25E-01 4.14E-01 8.00E-01 1.00E+00 1.13E+00 1.30E+00
                 1.86E+00 3.06E+00 1.07E+01 2.90E+01 1.01E+02 5.83E+02
                 3.04E+03 1.50E+04 1.11E+05 4.08E+05 9.07E+05 1.42E+06
                 1.83E+06 3.01E+06 6.38E+06 2.00E+07 ]
   }
   case(irrad){
       title="Fuel Stream 1 Irradiation"
       lib{ file="fuellib" pos=1 }
       time=[ 8I 36 360 ]
       power=[ 10r40 ]
       mat{
           units=GRAMS
           iso=[u234=534 u235=60000 u236=276 u238=939190]
       }
   }
   case(spent){
       title="Fuel Stream 1 Decay"
       time{
           t=[ 0.1 0.3 1 3 10 30 100 300 360 ] start=0 %enter times from 0
       }
       processing {
           retained=[se=0.998 rb=0.778 sr=0.778 te=0.778 cs=0.778 ba=0.778
                     dy=0.998 u=0.010 np=0.010 pu=0.010 am=0.010 cm=0.010]
       }
   }
   case(glass){
       title="100 kg glass" time{ t=[ 1 ] start=0 }
       mat{
           units=GRAMS
           iso=[li=2.18e3 b=2.11e3 o=46.4e3 f=0.061e3 na=7.65e3 mg=0.49e3 al=2.18e3
                si=25.4e3 cl=0.049e3 ca=1.08e3 mn=1.83e3 fe=8.61e3 ni=0.70e3
                zr=0.88e3 pb=0.049e3 ]
       }
   }
   case(blend){
       title="final blended case"  time=[ 1.01 3 10 30 100 ] %continue previous
       mat{
           blend=[ spent=0.1 glass=0.1 ] %blend factors of 0.1 for each
       }
    neutron{ alphan_medium=CASE } %use this case's isotopics
    print{ ele{ total=yes units=[GRAMS] }
           neutron{ summary=yes spectra=yes detailed=yes }
    }
   }
   end

.. _5-1-4-8:

Create an ORIGEN Decay Library from a Decay Resource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following COUPLE input (:numref:`fig-couple-decay-lib`) is all that is
required to produce a binary decay library from the ORIGEN decay resource
file in the SCALE data directory, which is linked by default to unit number
27. This means that to create a new decay library based on another decay
resource, it could be copied to the working directory as "ft27f001." COUPLE,
when looking for unit 27, will first look for file "ft27f001." If it is not
found, then COUPLE will it look to the special file "origen_filenames" in the
SCALE data directory and find that unit 27 is associated with "decay,"
shorthand for the decay resource.


.. code-block:: scale
   :caption: Creation of an ORIGEN decay library from the decay resource
   :name: fig-couple-decay-lib

   =couple
   ORIGEN Decay Library Revision 3
   Prepared by Johnny B. Good on 2015-10-18

   1$$ a1 1 e
   1t
   3$$ a1 0 e
   3t
   done
   end

   'Save a copy of the ORIGEN library.
   =shell
   cp ft33f001 "${OUTDIR}/my_dk.f33"
   end

.. _5-1-4-9:

Create an ORIGEN Reaction Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:numref:`fig-couple-rxn-lib` creates an ORIGEN reaction library from an
AMPX library created using the SCALE csas1x sequence. After COUPLE
completes, the ORIGEN library created (on default unit 33 or file
"ft33f001") is copied to the input directory. There are two very
important factors to verify when using COUPLE in this capacity.

   1. The ``"0$$ a5 4"`` and ``"1$$ a13 6"`` entries are very important, as they
      dictate that the cross sections will be read from "ft04f001" for AMPX
      library zone 6, which in this case is mixture ID "6" (related input
      highlighted in red). There are some AMPX libraries which do not
      contain zones, e.g. "ft03f001" produced by some sequences,
      representing the system-average cross sections. In this case the
      default should be used for ``"1$$ a13"`` of "0" indicating that a
      specific zone ID is not desired. By accessing different zones with
      ``"1$$ a13"``, an ORIGEN library can be created for clad activation or
      boron depletion in water by choosing a different mixture.

   2. The group structure of the reaction resource (``"0$$ a3 75"``) should be
      the same as the AMPX library produced (for example, "v7-56" in the
      csas1x input [related input highlighted in blue]). This requires
      inspection of the "origen_filenames" file to verify that unit 75 is
      associated with a 56-group library.


.. code-block:: scale
   :caption: Creation of an ORIGEN reaction library using COUPLE.
   :name: fig-couple-rxn-lib

   =csas1x
   pwr pin cell self-shielded xs
   v7-56
   read comp
     u-235       6  0  4.366e-4 1000.  end u-235
     u-238       6  0  2.352e-2 1000.  end u-238
     pu-239      6  0  1.110e-4 1000.  end pu-239
     pu-240      6  0  2.655e-5 1000.  end pu-240
     pu-241      6  0  1.209e-5 1000.  end pu-241
     o-16        6  0  4.549e-2 1000.  end o-16
     pu-242      6  0  1.705e-6 1000.  end pu-242
     am-241      6  0  2.598e-7 1000.  end am-241
     o-16        7  0  1.00e-20 1000.  end o-16
     zr          8  0  4.252e-2  750.  end zr
     h-1         9  0  4.836e-2  550.  end h-1
     b-10        9  0  4.280e-6  550.  end b-10
     b-11        9  0  1.780e-5  550.  end b-11
     o-16        9  0  2.418e-2  550.  end o-16
     h-1        10  0  4.405e-2  550.  end h-1
     b-10       10  0  3.998e-6  550.  end b-10
     b-11       10  0  1.770e-5  550.  end b-11
     o-16       10  0  2.202e-2  550.  end o-16
   end comp
   read celldata
     multiregion cylindrical right_bdy=white end
     6 0.41212  7 0.41738  8 0.47572  9 0.71187 10 0.74429  end zone
     moredata  wgt=1 icon=region  end moredata
   end celldata
   end

   =couple
   ********************************************************************************
   *                weighting flux from xsdrn pwr pincell                         *

   0$$ a3 75 a5 4 a6 33 e
   1$$ 0 0 0 1 a13 6 a14 1 a16 8 a17 0 0 e t
   done
   end

   'Save a copy of the AMPX and ORIGEN library.
   =shell
   cp ft04f001 "${INPDIR}/my.ampx"
   cp ft33f001 "${INPDIR}/my_rx.f33"
   end

.. _5-1-4-10:

Create an ORIGEN Activation Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Activation calculations typically do not require self-shielding, so an
ORIGEN "activation" library is a means to refer to a library that is
using infinitely dilute cross sections from the reaction resource. An
ORIGEN activation library can be created very easily as long as the flux
spectrum is available in one of the reaction resource group structures.
In the example below, a 238-group structure is used with reaction
resource on unit 18 (0$$ a3 80). Additionally, this case requests
explicit fission yields only for :sup:`235`\ U, :sup:`238`\ U,
:sup:`239`\ Pu, and :sup:`241`\ Pu in the 7$$ array. Other nuclides with
fission cross sections will not generate fission products. In a library
meant only for activation of standard structural materials, the library
could be made much smaller by not including any fission yields without
any impact on the calculation as long as it did not include fissionable
isotopes. Since the reaction resource contains 238 neutron groups, the
user-defined weighting flux given in the 9*\* array has 238 entries (in
order of descending energy).


.. code-block:: scale
   :caption: Creation of an ORIGEN activation library using COUPLE.
   :name: fig-couple-act-lib

   =couple
   ********************************************************************************
   *                cross sections from 238-group JEFF-3.0/A                      *
   *              fission product yields for u and pu                             *
   *              238 group weighting spectrum                                    *

   0$$ a3 80 a6 33 e
   1$$ a15 4 a16 8 0 238 e t
   7$$ 922350 922380 942390 942410
   ' thermal flux spectrum (238group endf/b-vii)
   9**
   6.2943E-08 2.0143E-05 4.9336E-05 6.3102E-05 1.7274E-04 2.7527E-03
   8.2268E-03 3.4521E-02 1.0638E-01 5.8410E-02 2.2867E-01 1.9072E-01
   6.5706E-02 3.2923E-01 3.0830E-01 1.0042E-01 4.5056E-02 4.0200E-02
   7.1789E-02 5.5827E-02 1.1555E-01 1.0753E-01 1.1282E-01 2.6197E-02
   3.3311E-02 1.8825E-02 5.6907E-02 1.0139E-01 1.0842E-01 1.4185E-02
   1.1467E-01 4.6204E-02 4.0279E-02 9.2133E-02 5.6120E-02 5.8296E-02
   3.9839E-02 4.1426E-02 1.5809E-01 1.5434E-01 2.1608E-01 1.8633E-01
   9.3426E-02 1.4238E-01 8.7520E-02 1.8431E-02 4.5110E-02 1.3542E-02
   9.5876E-02 6.7192E-02 1.8068E-02 4.7728E-02 1.7297E-01 7.4721E-02
   1.4966E-01 9.9660E-02 1.1138E-01 5.7821E-02 9.6891E-02 1.3524E-01
   1.2843E-02 6.6610E-02 4.4455E-02 3.4587E-02 1.1515E-02 5.6625E-02
   4.1249E-02 8.9513E-03 7.0964E-02 4.9612E-02 8.2643E-02 4.7146E-03
   4.7913E-02 1.3398E-01 1.5071E-02 3.7742E-02 2.8784E-02 2.5570E-03
   1.5954E-02 7.2581E-03 8.5716E-02 4.9578E-03 6.7959E-03 1.2430E-02
   1.5134E-02 2.0495E-02 1.7871E-02 4.7094E-03 9.7362E-03 1.0202E-02
   1.2089E-02 7.0278E-03 1.1748E-02 6.1341E-03 1.8192E-02 4.8103E-03
   4.9266E-03 5.0479E-03 3.3129E-03 4.8823E-03 6.9562E-03 4.7749E-03
   6.5503E-03 5.9089E-03 6.0943E-03 2.2221E-03 4.9783E-03 4.6347E-03
   7.1654E-03 4.4272E-03 4.2751E-03 2.5593E-03 7.8861E-03 2.7036E-03
   6.9270E-03 1.4644E-02 1.5863E-02 1.7326E-02 1.1228E-02 7.8853E-03
   8.2418E-03 4.2658E-03 1.3431E-02 9.5486E-03 9.0541E-03 7.3772E-03
   7.1365E-03 9.7966E-03 1.2279E-02 5.1688E-03 2.0891E-02 1.3908E-02
   1.6944E-02 1.7905E-02 3.0182E-03 5.1578E-03 5.3283E-03 5.5130E-03
   5.7122E-03 1.4610E-02 1.0560E-02 6.9833E-03 2.3063E-02 9.2517E-03
   8.3577E-03 1.3698E-02 4.1645E-03 2.1272E-03 1.4553E-03 4.8014E-03
   5.0002E-03 5.2430E-03 5.4865E-03 5.7120E-03 5.3013E-03 4.7860E-03
   5.3835E-03 5.2580E-03 7.3491E-03 3.8938E-03 5.4116E-03 6.3655E-03
   6.6848E-03 7.0417E-03 7.4051E-03 4.2986E-03 4.4473E-03 4.6103E-03
   4.7587E-03 4.9334E-03 2.5427E-03 2.5963E-03 2.6593E-03 2.7116E-03
   1.0989E-03 1.1056E-03 1.1130E-03 1.1231E-03 1.1334E-03 1.1420E-03
   1.1510E-03 1.1629E-03 1.1753E-03 1.1857E-03 1.1965E-03 1.2106E-03
   1.2246E-03 1.2409E-03 1.2534E-03 3.1928E-03 3.2547E-03 3.3266E-03
   3.4127E-03 7.1615E-03 7.6347E-03 8.0398E-03 8.7135E-03 9.3187E-03
   4.9383E-03 5.2114E-03 1.1051E-02 1.2360E-02 1.3594E-02 1.5691E-02
   8.6578E-03 9.6049E-03 1.0326E-02 1.1808E-02 1.2995E-02 1.5499E-02
   1.8011E-02 2.2842E-02 2.9192E-02 3.8848E-02 5.4147E-02 7.8442E-02
   4.0085E-02 4.7411E-02 5.2900E-02 6.0463E-02 6.6447E-02 7.1355E-02
   7.2251E-02 3.2877E-02 8.8606E-02 9.2103E-03 7.2183E-03 2.1029E-03
   1.7575E-03 7.6841E-04 6.7619E-04 5.0434E-04 1.6279E-04 9.2721E-05
   9.6876E-05 7.4318E-05 6.2449E-05 1.3205E-06 e t
   done
   end
   'Save a copy of the ORIGEN library.
   =shell
   cp ft33f001 "${INPDIR}/my_act.f33"
   end


The following excerpts from the output file
(:numref:`fig-origen-avg-energy-fission`) show average energy of the neutrons
causing fission that are used for the fission yield interpolation, as well as
a partial listing of the one-group cross sections computed from the weighting
spectrum and folded into the ORIGEN binary library. In the one-group cross
section list, the units are barns and the lines labeled "tot-cap" correspond
to the total removal cross section.


.. code-block:: scale
   :caption: ORIGEN activation library: average energy per fission calculated.
   :name: fig-origen-avg-energy-fission

   * Average energy per fission calculated (eV) *
   922350 1.80316E+04
   922380 3.03510E+06
   942390 1.38073E+04
   942410 1.04235E+04

   …

   922350 fission    4.91087E+01
   922350 to 922320  3.86728E-12      mt=  37
   922350 to 922360  1.02705E+01      mt= 102
   922350 to 912350  3.92165E-07      mt= 103
   922350 to  10010  1.53793E-13      mt= 103  byproduct
   922350 to 902320  8.64582E-06      mt= 107
   922350 to  20040  7.47503E-11      mt= 107  byproduct
   922350 tot-cap    5.93828E+01
   922360 to 922350  1.99485E-03      mt=  16
   922360 to 922351  4.98709E-04      mt=  16
   922360 to 922340  3.15162E-05      mt=  17
   922360 fission    2.97265E-01
   922360 to 922370  7.10594E+00      mt= 102
   922360 to 912360  1.26031E-07      mt= 103
   922360 to  10010  1.58839E-14      mt= 103  byproduct
   922360 to 902330  4.63085E-08      mt= 107
   922360 to  20040  2.14447E-15      mt= 107  byproduct

.. _5-1-4-11:

Create an ORIGEN Library with User-Supplied Cross Sections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is possible to set the fission and removal cross sections directly
for a nuclide and for individual reaction transitions from nuclide to
nuclide if the daughter nuclide is known. The following example is the
same as the previous but with additional inputs for ``"1$$ a3 1,"`` ``15$$``,
``71$$``, ``72$$``, and ``73**`` arrays (highlighted in red).


.. code-block:: scale
   :caption: Creation of an ORIGEN library with user-supplied cross sections in COUPLE.
   :name: fig-couple-user-rxn-lib

   =couple
   ********************************************************************************
   *                cross sections from 238-group JEFF-3.0/A                      *
   *              fission product yields for u and pu                             *
   *              238 group weighting spectrum + user-defined xs                  *

   0$$ a3 80 a6 33 e
   1$$ a3 1 a15 4 a16 8 0 238 e t
   7$$ 922350 922380 942390 942410
   ' thermal flux spectrum (238group endf/b-vii)
   9**
   6.2943E-08 2.0143E-05 4.9336E-05 6.3102E-05 1.7274E-04 2.7527E-03
   8.2268E-03 3.4521E-02 1.0638E-01 5.8410E-02 2.2867E-01 1.9072E-01
   6.5706E-02 3.2923E-01 3.0830E-01 1.0042E-01 4.5056E-02 4.0200E-02
   7.1789E-02 5.5827E-02 1.1555E-01 1.0753E-01 1.1282E-01 2.6197E-02
   3.3311E-02 1.8825E-02 5.6907E-02 1.0139E-01 1.0842E-01 1.4185E-02
   1.1467E-01 4.6204E-02 4.0279E-02 9.2133E-02 5.6120E-02 5.8296E-02
   3.9839E-02 4.1426E-02 1.5809E-01 1.5434E-01 2.1608E-01 1.8633E-01
   9.3426E-02 1.4238E-01 8.7520E-02 1.8431E-02 4.5110E-02 1.3542E-02
   9.5876E-02 6.7192E-02 1.8068E-02 4.7728E-02 1.7297E-01 7.4721E-02
   1.4966E-01 9.9660E-02 1.1138E-01 5.7821E-02 9.6891E-02 1.3524E-01
   1.2843E-02 6.6610E-02 4.4455E-02 3.4587E-02 1.1515E-02 5.6625E-02
   4.1249E-02 8.9513E-03 7.0964E-02 4.9612E-02 8.2643E-02 4.7146E-03
   4.7913E-02 1.3398E-01 1.5071E-02 3.7742E-02 2.8784E-02 2.5570E-03
   1.5954E-02 7.2581E-03 8.5716E-02 4.9578E-03 6.7959E-03 1.2430E-02
   1.5134E-02 2.0495E-02 1.7871E-02 4.7094E-03 9.7362E-03 1.0202E-02
   1.2089E-02 7.0278E-03 1.1748E-02 6.1341E-03 1.8192E-02 4.8103E-03
   4.9266E-03 5.0479E-03 3.3129E-03 4.8823E-03 6.9562E-03 4.7749E-03
   6.5503E-03 5.9089E-03 6.0943E-03 2.2221E-03 4.9783E-03 4.6347E-03
   7.1654E-03 4.4272E-03 4.2751E-03 2.5593E-03 7.8861E-03 2.7036E-03
   6.9270E-03 1.4644E-02 1.5863E-02 1.7326E-02 1.1228E-02 7.8853E-03
   8.2418E-03 4.2658E-03 1.3431E-02 9.5486E-03 9.0541E-03 7.3772E-03
   7.1365E-03 9.7966E-03 1.2279E-02 5.1688E-03 2.0891E-02 1.3908E-02
   1.6944E-02 1.7905E-02 3.0182E-03 5.1578E-03 5.3283E-03 5.5130E-03
   5.7122E-03 1.4610E-02 1.0560E-02 6.9833E-03 2.3063E-02 9.2517E-03
   8.3577E-03 1.3698E-02 4.1645E-03 2.1272E-03 1.4553E-03 4.8014E-03
   5.0002E-03 5.2430E-03 5.4865E-03 5.7120E-03 5.3013E-03 4.7860E-03
   5.3835E-03 5.2580E-03 7.3491E-03 3.8938E-03 5.4116E-03 6.3655E-03
   6.6848E-03 7.0417E-03 7.4051E-03 4.2986E-03 4.4473E-03 4.6103E-03
   4.7587E-03 4.9334E-03 2.5427E-03 2.5963E-03 2.6593E-03 2.7116E-03
   1.0989E-03 1.1056E-03 1.1130E-03 1.1231E-03 1.1334E-03 1.1420E-03
   1.1510E-03 1.1629E-03 1.1753E-03 1.1857E-03 1.1965E-03 1.2106E-03
   1.2246E-03 1.2409E-03 1.2534E-03 3.1928E-03 3.2547E-03 3.3266E-03
   3.4127E-03 7.1615E-03 7.6347E-03 8.0398E-03 8.7135E-03 9.3187E-03
   4.9383E-03 5.2114E-03 1.1051E-02 1.2360E-02 1.3594E-02 1.5691E-02
   8.6578E-03 9.6049E-03 1.0326E-02 1.1808E-02 1.2995E-02 1.5499E-02
   1.8011E-02 2.2842E-02 2.9192E-02 3.8848E-02 5.4147E-02 7.8442E-02
   4.0085E-02 4.7411E-02 5.2900E-02 6.0463E-02 6.6447E-02 7.1355E-02
   7.2251E-02 3.2877E-02 8.8606E-02 9.2103E-03 7.2183E-03 2.1029E-03
   1.7575E-03 7.6841E-04 6.7619E-04 5.0434E-04 1.6279E-04 9.2721E-05
   9.6876E-05 7.4318E-05 6.2449E-05 1.3205E-06 e t
   15$$ 3 t
   71$$ 922380 -942390  952410
   72$$ 922380  942390  102
   73** 1.2     500.0   10.0
   done
   end

.. _5-1-4-12:

Printing library cross-section values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _5-1-4-12-1:

Print the Cross Section Values on an ORIGEN Library in COUPLE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cross sections can be printed when a library is generated in COUPLE by
setting the 1$ array entry 14, IEDOU = 1, as illustrated in
:numref:`fig-couple-print-lib`.

.. code-block:: scale
   :caption:  Printing cross section values on an ORIGEN library using COUPLE.
   :name: fig-couple-print-lib

   =shell
   cp ${INPDIR}/my_rx.f33 ft33f001
   end

   =couple
   edit reaction transition cross sections

   0$$ a4 33 e
   1$$ a5 1 a14 1 0 e t
   done
   end

.. _5-1-4-12-2:

Print the Cross Section Values on an ORIGEN Library in ORIGEN
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cross sections can also be printed when the library is used in ORIGEN by
setting "print_xs=yes" in the options block, shown as
:numref:`fig-origen-print-lib`.

.. code-block:: scale
   :caption: Printing cross section values on an ORIGEN library using ORIGEN.
   :name: fig-origen-print-lib

   =shell
   cp ${INPDIR}/my_rx.f33 ft33f001
   end

   =origen
   options{ print_xs=yes }
   case{
       lib{ file="ft33f001" pos=1 }
       time=[1] %dummy time
       mat{ iso=[u235=1] } %dummy iso
   }
   end

.. _5-1-4-13:

Ranking Contribution to Toxicity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The OPUS input in :numref:`fig-opus-rank-radtox` creates a plot of the
volume of various nuclides with the maximum permissible concentration (MPC)
in water using the "snf.f71" produced by the "Three cycle plus decay" example
(:numref:`fig-origen-3cycle`). Only positions 6–16 are plotted using
"minposition" and "maxposition." Three nuclides (:sup:`242`\ Cm,
:sup:`137m`\ Ba, and :sup:`99`\ Tc ) are forced to be included via the "symnuc"
list, with 17 more nuclides (for total "nrank=20") included according to their
average rank in terms of the MPC in water. The total number of nuclides
requested is 20. The x-axis label is set to "TIME (YEARS)," and the title is
"SPENT FUEL AT 60 GWD/MTHM."

.. code-block:: scale
   :caption: Using OPUS to produce a ranked contribution to radiotoxicity
   :name: fig-opus-rank-radtox

   =shell
     cp ${INPDIR}/snf.f71 f71
   end

   =opus
   data="f71"
   typarams=nucl
   units=h2om**3
   time=year
   libtype=fisact
   minposition=6  maxposition=16   nrank=20
   title="SPENT FUEL AT 60 GWD/MTIHM "
   xlabel="TIME (YEARS)"
   symnuc=cm-242 ba-137m tc-99 end
   end

.. _5-1-4-14:

Spectrum plots with OPUS
~~~~~~~~~~~~~~~~~~~~~~~~

.. _5-1-4-14-1:

Photon Spectrum Plot
^^^^^^^^^^^^^^^^^^^^

The OPUS input shown in :numref:`fig-opus-photon-spec` creates a plot of the
photon spectrum for all times between 1 and 5 years, using "tmin=1" and
"tmax=5" with "time=years."


.. code-block:: scale
   :caption: Plotting the photon spectrum using OPUS.
   :name: fig-opus-photon-spec

   =shell
   cp ${INPDIR}/snf.f71 f71
   end

   =opus
   data="f71"
   typarams=gspectrum
   units=intensity
   tmin=1 tmax=5 time=years
   end


:numref:`fig-opus-gamma-output` shows the output of the time-dependent
gamma spectrum extracted from the f71 file by OPUS.

.. code-block:: scale
   :caption: Photon spectrum plot from OPUS-- output of the time-dependent gamma spectrum.
   :name: fig-opus-gamma-output

	       1/(s.MeV) |        1.25y       2.15y       3.73y
   ----------------------+-------------------------------------
    1.00e+01 -- 8.00e+00 |   2.7961e+11  3.0661e+03  3.0661e+03
    8.00e+00 -- 6.50e+00 |   7.1201e+13  1.9436e+04  1.9436e+04
    6.50e+00 -- 5.00e+00 |   8.9725e+15  2.5300e+10  5.3041e+09
    5.00e+00 -- 4.00e+00 |   3.7075e+16  9.1643e+12  1.9001e+12
    4.00e+00 -- 3.00e+00 |   1.1734e+17  1.3562e+14  2.8824e+13
    3.00e+00 -- 2.50e+00 |   3.4321e+17  5.5945e+15  4.8216e+15
    2.50e+00 -- 2.00e+00 |   5.2847e+17  1.1338e+16  5.9433e+15
    2.00e+00 -- 1.66e+00 |   8.3528e+17  3.3015e+16  1.8382e+16
    1.66e+00 -- 1.33e+00 |   1.8060e+18  2.7233e+17  2.4658e+17
    1.33e+00 -- 1.00e+00 |   2.4156e+18  1.4238e+17  9.2264e+16
    1.00e+00 -- 8.00e-01 |   5.0662e+18  3.2193e+17  2.6845e+17
    8.00e-01 -- 6.00e-01 |   6.4083e+18  2.1010e+18  1.8903e+18
    6.00e-01 -- 4.00e-01 |   7.1803e+18  1.1822e+18  1.0301e+18
    4.00e-01 -- 3.00e-01 |   8.7297e+18  1.7856e+18  1.6414e+18
    3.00e-01 -- 2.00e-01 |   1.9481e+19  1.0658e+19  9.7018e+18
    2.00e-01 -- 1.00e-01 |   2.9105e+19  1.5198e+19  1.3996e+19
    1.00e-01 -- 5.00e-02 |   6.2160e+19  9.1756e+18  8.3611e+18
    5.00e-02 -- 1.00e-02 |   1.1219e+20  3.4628e+19  3.1458e+19

.. _5-1-4-14-2:

Neutron Spectrum Plot
^^^^^^^^^^^^^^^^^^^^^

The OPUS input in :numref:`fig-opus-total-neut-spec` creates a plot of the
total neutron spectrum at all times.

.. code-block:: scale
   :caption: Neutron spectrum plot using OPUS
   :name: fig-opus-total-neut-spec

   =opus
   data="f71"
   typarams=nspe
   units=intensity
   end

.. _5-1-4-15:

Isotopic Weight Percentages for Uranium and Plutonium During Decay
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The isotopic distributions in uranium and plutonium, in weight percent,
may be plotted with the OPUS input in :numref:`fig-opus-iso-wt-pct`.


.. code-block:: scale
   :caption: Isotopic weight percentages for uranium and plutonium during decay.
   :name: fig-opus-iso-wt-pct

   =opus
   data="f71"
   units=wpel
   libtype=act
   symnuc=u pu end
   end

.. _5-1-4-16:

User-Specified Response Function in OPUS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :numref:`fig-opus-user-response`, response conversion factor data are
entered in the RESPONSE= array as nuclide-response factor pairs, with the
nuclide id being the legacy nuclide ID (ZZAAAI), with ZZ two digits of
atomic number, AAA three digits of mass number, and I one digit of isomeric
state. For example, :sup:`235m`\ U would be given as 922351 and H-1 as 10010.
In this example, it is assumed that the response factors are activity based
(response/Bq of nuclide), so the units of Becquerels are requested using the
UNITS keyword. The user-supplied response conversion factors are applied to
the Becquerel units for all nuclides in the RESPONSE= array, and the results
for any nuclide for which no response factors are provided are zeroed.


.. code-block:: scale
   :caption: Example of a user-specified response function in OPUS.
   :name: fig-opus-user-response

   =opus
   data="f71"
   units=becq
   time=year
   typarams=nucl
   response=
    270600 1.92027E+00  962460 2.27711E-01  481151 1.64222E-01
    822100 5.19246E-12  962470 1.75728E-09  501230 3.81237E-02
    832101 9.43341E-09  962480 1.05672E+00  511240 1.53438E+02
    882260 1.51600E-05  962500 1.60583E+02  511250 1.81023E-04
    892270 1.67080E-05  982490 2.21420E-04  511260 5.13360E+00
    902280 2.06832E-02  982500 2.87199E+02  end
   end

.. bibliography:: bibs/ORIGEN.bib
