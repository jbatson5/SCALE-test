*k*\ :sub:`eff`.. _STARBUCS:

STARBUCS: A Scale Control Module for Automated Criticality Safety Analyses Using Burnup Credit
==============================================================================================

*G. Radulescu and I. C. Gauld*

STARBUCS is an analysis sequence in SCALE for automating criticality
safety and burnup loading curve analyses of spent fuel systems employing
burnup credit. STARBUCS requires only the fresh fuel composition, an
irradiation history, and the KENO model for a spent fuel configuration
to be provided in an input file. It automatically performs all necessary
calculations to determine spent fuel compositions, self-shielded cross
sections, and the *k*\ :sub:`eff` of the spent fuel configuration. In addition,
for burnup loading curve analyses, STARBUCS performs iterative
calculations to search for initial fuel enrichments that result in an
upper subcritical limit. STARBUCS allows the user to simulate axial- and
horizontal-burnup gradients in a spent fuel assembly, select the
specific actinides and/or fission products that are to be included in
the criticality analysis, and apply isotopic correction factors to the
predicted spent fuel nuclide inventory to account for calculational bias
and uncertainties. A depletion analysis calculation for each of the
burnup-dependent regions of a spent fuel assembly, or any other system
containing spent nuclear fuel, is performed using the ORIGEN-ARP
sequence of SCALE. For criticality safety calculations employing
multigroup cross section data, the spent fuel compositions are used to
generate resonance self-shielded cross sections for each region of the
problem. The region dependent nuclide concentrations and cross sections
are applied in a three-dimensional criticality safety calculation using
the KENO code. Both KENO V.a and KENO-VI criticality codes are supported
for single criticality safety calculations using burnup credit, but only
KENO V.a can be used in criticality calculations for burnup loading
curve analyses. Although STARBUCS was developed specifically to address
the burnup-credit analysis needs for spent fuel transport and storage
applications, it provides sufficient flexibility to allow criticality
safety assessments involving many different potential configurations of
UO\ :sub:`2` spent nuclear fuel.

Introduction
------------

The U.S. Nuclear Regulatory Commission (NRC) issued Revision 3 of the
Interim Staff Guidance 8 (ISG-8) (:cite:`us_nuclear_regulatory_commission_burnup_2012`) on burnup credit in
September, 2012. ISG-8 provides guidance on the application of
burnup-credit in criticality safety analyses for pressurized-water
reactor (PWR) spent fuel in transportation and storage casks. Burnup
credit is the concept of taking credit for the reduction in reactivity
in spent fuel due to burnup. The reduction in reactivity that occurs
with fuel burnup is due to the change in concentration (net reduction)
of fissile nuclides and the production of actinide and fission-product
neutron absorbers. In contrast to criticality safety analyses that
employ a fresh-fuel assumption (i.e., conservatively assuming
unirradiated fuel compositions), credit for burnup requires the
prediction of both fissile material and absorber nuclide concentrations
in spent nuclear fuel (SNF) and consideration of many burnup-related
phenomena, in addition to the criticality issues.

Consideration of the depletion aspects in the criticality assessment of
SNF places an increasing reliance on computational tools and methods,
and significantly increases the overall complexity of the criticality
safety analysis. The use of spent fuel nuclide concentrations in the
criticality evaluation also necessitates consideration of many
additional sources of uncertainty associated with fuel depletion. ISG-8
highlights, for example, the need for applicants employing burnup credit
in criticality safety assessments to address the axial and horizontal
variation of the burnup within a spent fuel assembly, uncertainties and
bias in the nuclide predictions, and the additional reactivity margin
available from fission products and actinides not credited in the
licensing basis.

To assist in performing and reviewing criticality safety assessments of
transport and storage casks that apply burnup credit, a new control
sequence called STARBUCS (**St**\ andardized **A**\ nalysis of
**R**\ eactivity for **Bu**\ rnup **C**\ redit using **S**\ CALE) was
developed in SCALE 5. STARBUCS automates the generation of
spatially-varying nuclide compositions in a spent fuel assembly, and
applies the assembly compositions in a three-dimensional (3-D)
Monte Carlo analysis of the system. STARBUCS automatically prepares
input files for each of the modules in the sequence, executes the
modules through the SCALE driver, and performs all flow control, module
interface, and data management functions. The STARBUCS sequence uses
well-established code modules currently available in SCALE. STARBUCS
also performs iterations over a range of initial fuel enrichments to
determine the initial enrichments below which UO\ :sub:`2` commercial
spent fuel may be loaded in a transport/storage cask for specified
burnup values. With this capability, STARBUCS assists in generating
burnup loading curves for criticality safety analyses of spent fuel in
transport and storage casks.

The STARBUCS sequence automates the depletion calculations using the
ORIGEN-ARP methodology to perform a series of cross section preparation
and depletion calculations to generate a comprehensive set of spent fuel
isotopic inventories for each spatially-varying burnup region of an
assembly. The spent fuel nuclide concentrations are subsequently input
to either CSAS5 or CSAS6 to and perform a criticality calculation of the
system using the KENO V.a or KENO-VI code, respectively, to determine
the neutron multiplication factor (*k*\ :sub:`eff`) for the system. Only
minimal input is required by the user to perform a typical burnup-credit
analysis. The user can specify the assembly-average irradiation history,
the axial density variation of the reactor moderator, the axial- and
horizontal-burnup profile, and the nuclides that are to be applied in
the criticality safety analysis. Nuclide correction factors may also be
applied to the predicted concentrations to account for known bias and/or
uncertainty in the predicted SNF compositions.

Methodology
-----------

The STARBUCS control module is a burnup-credit sequence designed to
perform 3-D Monte Carlo criticality safety calculations that include the
effects of spatially-varying burnup in SNF configurations. STARBUCS
offers two options: either perform a single criticality safety
calculation with burnup credit or perform iterative calculations for
burnup loading curve analyses of commercial UO\ :sub:`2` spent fuels.
The sequence contains a set of instructions designed to automatically
process input data, execute code modules currently available in SCALE
for depletion, resonance cross section, and criticality calculations. In
addition, for burnup loading curve analyses, STARBUCS checks whether
*k*\ :sub:`eff` converges to a user-provided upper subcritical limit, adjusts
the initial fuel enrichment using the least squares method, and repeats
the sequence until either convergence is achieved or determine that no
solution can be found. The overall program structures and flow for a
single criticality calculation and for burnup loading curve calculations
are illustrated in :numref:`fig2-3-1` and :numref:`fig2-3-2`, respectively.

The sequence uses well-established code modules currently available in
the SCALE code system. These modules include ARP and ORIGEN to perform
the depletion analysis phase of the calculations. ORIGEN-ARP is a
sequence within the SCALE system that serves as a faster alternative to
the TRITON depletion sequence of SCALE to perform point-irradiation
calculations with the ORIGEN code using problem-dependent cross
sections. ARP uses an algorithm that enables the generation of cross
section libraries for the ORIGEN code by interpolation over pregenerated
cross section libraries. The ORIGEN code performs isotopic generation
and depletion calculations to obtain the spent fuel nuclide
compositions. For criticality safety calculations using multigroup cross
section data, problem dependent cross sections are processed with the
resonance self-shielding capabilities of XSProc using the
region-dependent compositions from the depletion analyses. Finally, the
region dependent nuclide concentrations and cross sections are applied
in a 3-D criticality calculation for the system using either KENO V.a or
KENO-VI to calculate the *k*\ :sub:`eff` value.

The ORIGEN-ARP depletion analysis methodology represents a significant
increase in computational speed as compared to equivalent calculations
performed using the SCALE depletion analysis sequences that use
two-dimensional transport methods, with virtually no sacrifice in
accuracy. ARP uses an algorithm that enables the generation of cross
sections for the ORIGEN code by interpolating on cross sections
available in pre-generated data libraries. For uranium-based fuels the
interpolation parameters available are initial fuel enrichment, burnup
and, optionally, moderator density. STARBUCS creates input files for ARP
and ORIGEN for each burnup-dependent region of an assembly and
calculates the spent fuel nuclide concentrations for the region using a
user-specified assembly irradiation history, cooling time, and burnup
profiles. The ORIGEN libraries must be available in advance of a
STARBUCS burnup-credit calculation. These libraries may be created using
TRITON. The libraries include the effects of assembly design and
operating conditions on the neutron cross sections used in the burnup
analysis. Several ORIGEN libraries are distributed in the SCALE code
system and can be applied in a STARBUCS analysis. Alternatively, a user
may create a specific ORIGEN library for other assembly types or
operating conditions not available in the default libraries. The
generation of ORIGEN reactor libraries is discussed in the ORIGEN
Reactor Libraries chapter.

The depletion phase of the analysis is performed using ARP and ORIGEN to
calculate the compositions of each discrete fuel region (axial or
horizontal). After a single ORIGEN-ARP depletion calculation is
completed, control is passed back to the STARBUCS module which reads the
spent fuel nuclide inventories generated by ORIGEN, saves them, prepares
the ARP and ORIGEN input files for the next burnup region, and executes
the codes in sequence. This cycle continues until the fuel compositions
for all axial and horizontal regions have been calculated and saved,
completing the depletion phase of the analysis. The depletion
calculations for each axial and radial zone are performed using an
initial fuel basis of 1 MTHM (10:sup:`6` g heavy metal).

After all depletion calculations are completed, STARBUCS reads the spent
fuel nuclide inventories for all regions and prepares input for the
criticality calculation. The concentrations of all nuclides in the
ORIGEN depletion analysis are converted from gram-atom units (per MTU)
to units of atoms/b-cm applied in the criticality calculation. The
criticality calculation is performed using the capabilities in the CSAS5
or CSAS6 control module of SCALE. Specifically, STARBUCS prepares input
for the CSAS5 module when criticality calculations are to be performed
using KENO V.a, and for the CSAS6 sequence when using KENO-VI. Note that
only the criticality safety sequence CSAS5 of SCALE can be used for
burnup loading curve calculations.

For burnup loading curve iterative calculations, STARBUCS employs the
search algorithm described in CSAS5 section on *Optimum
(Minimum/Maximum) Search* to determine initial fuel enrichments that
satisfy a convergence criterion for the k\ :sub:`eff` of the spent fuel
configuration. If convergence is not achieved in a search pass, the
initial fuel enrichment is automatically adjusted. This sequence repeats
until either k\ *eff* converges to an upper subcritical limit or until
the algorithm determines that a solution is not possible. The procedure
is repeated for each requested burnup value. The maximum allowable
iterations, upper subcritical limit, tolerance for convergence, and a
range of initial fuel enrichments can be set by the user. The lower and
upper enrichment bounds as well as the burnup values for spent fuel
regions must be contained within the range of enrichment and burnup
values used to generate the applicable ORIGEN library. The control
module prepares a STARBUCS input file for each search pass requesting a
single criticality calculation using the calculated spent fuel
compositions. In this input file, the burnup history data block and/or
the fuel mixture compositions are updated based on the outcome of the
search sequence. The pre-burnup compositions for the two minor uranium
isotopes, :sup:`234`\ U and :sup:`236`\ U, are updated in the STARBUCS
input file for a new pass only if they were included in the initial
input file prepared by the user. Their updated weight percentages are
based on the assumption that the mass ratios
:sup:`234`\ U/\ :sup:`235`\ U and :sup:`236`\ U/\ :sup:`235`\ U do not
change with fuel enrichment.

.. _fig2-3-1:
.. figure:: figs/STARBUCS/fig1.png
  :align: center
  :width: 600

  Modules and flow of STARBUCS sequence for criticality calculations.

.. _fig2-3-2:
.. figure:: figs/STARBUCS/fig2.png
  :align: center
  :width: 600

  Modules and flow of STARBUCS sequence for burnup loading curve calculations.

.. _cap-and-lim:

Capabilities and Limitations
----------------------------

STARBUCS is designed to facilitate criticality safety analyses employing
burnup credit by automating and linking the depletion and criticality
calculations. The STARBUCS sequence has been designed to readily allow
analysts and reviewers to assess the subcritical margins associated with
many of the important phenomena that need to be evaluated in the context
of the current regulatory guidance on burnup credit. However, STARBUCS
is sufficiently general to allow virtually any configuration involving
irradiated nuclear material to be analyzed. Limitations and some of the
key capabilities of the STARBUCS sequence are described below.

1. STARBUCS limitations include the use of a single UO\ :sub:`2` fuel
   type and, for analyses employing multigroup cross section data, the
   use of geometry configurations consisting of spent fuel rod arrays.
   However, the type of spent fuel configurations that can be analyzed
   is entirely general. STARBUCS can be used to perform criticality
   safety assessments of individual fuel assemblies, a spent fuel cask,
   a spent fuel storage pool, or any nuclear system containing
   UO\ :sub:`2` irradiated nuclear fuel.

2. Only the criticality safety sequence CSAS5 of SCALE can be used for
   burnup loading curve calculations; therefore KENO V.a geometry
   description must be available in a STARBUCS input file for burnup
   loading curve calculations.

3. Burnup calculations can incorporate any desired operating history.
   The user may enter the specific power, cycle lengths, cycle down
   time, post-irradiation cooling time, etc. The axial-water-moderator
   density variation may also be specified in the depletion analysis,
   provided the ORIGEN cross section library contains such data.

4. The effects of assembly design, soluble boron concentrations,
   burnable poison exposure, reactor operating conditions, etc., are
   accounted for in the ORIGEN cross section libraries used in the
   ORIGEN depletion calculations. Libraries for several fuel assembly
   designs are distributed with SCALE. These libraries can also be
   readily created for any reactor and fuel assembly design that can be
   represented in the depletion analysis sequences of the SCALE system.

5. The user can select the specific actinide and/or fission product
   nuclides to be included in the criticality safety analysis. The user
   also has the option to perform a criticality calculation employing
   all nuclides for which cross section data exist.

6. Isotopic correction factors may be input to adjust the calculated
   nuclide inventories to account for known bias and/or uncertainties
   associated with the depletion calculations.

Minimal user input is required to perform many types of analyses.
Default values are supplied for many of the input parameter keywords.
The user may select from built-in burnup-dependent 18-axial-zone
profiles taken from :cite:`lancaster_actinide-only_1998`, or the user may input an arbitrary
user-defined burnup distribution with up to 100-axial zones and up to
7-horizontal zones. The depletion analysis calculations for each zone
are performed for all nuclides (the ORIGEN data libraries contain cross
section and decay data for more than 1000 unique actinides, fission
products, and structural activation products). The specific nuclides to
be considered in the *k*\ :sub:`eff` analysis may be input by the user. If no
nuclide set is explicitly selected, then all nuclides that have cross
section data in the ORIGEN library are automatically applied in the
criticality analysis, resulting in a “full” burnup-credit criticality
assessment. A capability to adjust the calculated isotopic inventories
using correction factors that can account for biases and/or
uncertainties in the calculated isotopic concentrations is also
provided.

An appropriate ORIGEN cross section library for UO\ :sub:`2` fuel must
be available for the depletion analysis using STARBUCS. The user may use
the libraries distributed with SCALE (e.g., ge7×7-0, ge8×8-4, ce14×14,
w15×15, w17×17_ofa) or the user may generate their own problem-specific
libraries using the TRITON depletion analysis sequence available in
SCALE. A complete list of ORIGEN libraries distributed with SCALE and
methods for generating ORIGEN libraries are both described in the ORIGEN
Reactor Libraries chapter. The range of initial fuel enrichment and
requested burnup values to be used in the STARBUCS calculations must be
contained within the range of the enrichments and burnups used to
generate the applicable ORIGEN library.

The user is required to provide a complete KENO V.a model of the spent
fuel configuration for burnup loading curve calculations and a complete
KENO V.a or KENO-VI model of the spent fuel configuration for single
criticality calculations using burnup credit. The initial material
composition information is defined in a standard composition data block.
The fuel material is automatically depleted in the sequence for each of
the burnup-dependent regions or zones in the problem. The nuclide
concentrations after irradiation and decay are automatically applied to
the KENO criticality analysis. The mixture numbers for each of the fuel
regions are identified by unique mixture numbers assigned automatically
by STARBUCS based on the axial and horizontal regions in the problem
(see :numref:`fig2-3-3`). The user is required to specify the geometry/extent
of the axial and horizontal zones in the KENO model and apply the
appropriate mixture numbers for the desired configuration based on the
mixture identifying scheme. STARBUCS performs no checking of the
criticality model to verify that all mixtures in the problem have been
used or that the order of the mixture numbers in the KENO model
corresponds to the corresponding order of the input burnup profile. This
provides the user a great deal of flexibility in setting up problems.
However, it also requires that the user accurately prepare the input
files to ensure that the spent fuel zone mixtures are assigned to the
correct KENO V.a or KENO-VI geometry regions. For instance, the user
could (intentionally) reverse the order of the axial-material
identifiers in the KENO model to simulate inverted fuel, or zone
mixtures could be omitted to simulate a problem using only a subset of
the available fuel zones that were simulated in the depletion analysis.

.. _fig2-3-3:
.. figure:: figs/STARBUCS/fig3.png
  :align: center
  :width: 600

  Fuel and material mixture numbering convention used in STARBUCS.

.. _fig2-3-4:
.. figure:: figs/STARBUCS/fig4.png
  :align: center
  :width: 600

  Example of mixture numbering scheme used in STARBUCS.

There are several conventions that must be followed when using STARBUCS.
In general, these relate to the specification of materials and mixture
numbering of the cross section mixing table.

1. The maximum number of horizontal zones is restricted to seven if
   there is no gap or second moderator mixture, six if a gap or second
   moderator mixture is defined, and five if both a gap and a second
   moderator are defined. The number of axial-fuel zones is limited such
   that the product of horizontal zones ∗ axial zones is less than or
   equal to 100. These limits constrain the maximum mixture number used
   for burned fuel in the KENO criticality calculation to less than 1000
   and assign unique mixture numbers to clad, moderator, and gap
   mixtures for lattice cell descriptions. The convention used to number
   the depleted fuel zones is to start at mixture 101 and increment by 1
   for each axial-burnup region. Thus, for a case with 10 axial-burnup
   regions, the fuel mixtures used in the criticality analysis would
   range from 101 to 110. For a similar case having two horizontal zones
   in addition to the axial zones, the mixture numbers would also
   include mixtures 201 to 210.

2. Mixture numbers for the clad, gap (if applicable), and moderator may
   also be used directly in the KENO model. Additional unique mixture
   numbers are required by the code for the lattice cell descriptions
   for each separate fuel zone (except for mixture 0 for void). These
   additional mixtures are assigned automatically by the code and are
   shown in :numref:`fig2-3-3` for a lattice cell consisting of fuel, gap,
   clad, and moderator. The additional mixture numbers may also be used
   directly in the KENO model. Mixture number allocation is illustrated
   in :numref:`fig2-3-4` for an example case where the number of different
   horizontal zones is four and the maximum number of axial zones is
   limited to 25.

3. All structural materials in the problem must have mixture numbers
   different from the numbers automatically generated by the code (see
   :numref:`fig2-3-4` for an example of available mixture numbers). For the
   example shown in :numref:`fig2-3-4`, mixtures 5–100, 126–200, 226–300,
   326–400, 501, 601, 701, 426–500, and 801–2147 are not allocated by
   STARBUCS and may be defined by the user in the composition data block
   and used in the geometry model. If the constraints in paragraph 1 are
   followed, mixture numbers less than 100 that were not used for fuel,
   gap, clad, moderator and mixture numbers from 1001 to 2147 are always
   available for structural materials. Note that STARBUCS does not
   provide a warning or stop program execution if a mixture number
   assigned to a structural material has also been generated internally
   by the computer code. The mixture numbers for structural materials
   are not changed and are thus applied in the KENO model in a
   one-to-one correspondence with the standard composition mixture as
   done for typical CSAS calculations. Therefore, the use of a mixture
   number for structural materials that is identical to one of the
   mixture numbers automatically generated by the code results in the
   combination of both materials in the composition for the mixture
   number.

4. Not all SCALE standard composition alphanumeric names (see the
   Standard Composition Library chapter) are currently recognized by
   STARBUCS. The use of special materials (e.g., C-GRAPHITE, NIINCONEL,
   H-POLY), particularly as fuel materials, that have nuclide
   identifiers that are not readily translated to ORIGEN ZA numbers
   should be avoided since these materials cannot be depleted.

5. A single STARBUCS calculation is limited to a single initial fuel
   type (composition, enrichment, assembly design, etc.). Configurations
   involving multiple fuel types may be solved by running a separate
   STARBUCS case for each type, saving the corresponding CSAS cases
   generated by STARBUCS that contain the irradiated fuel nuclide
   compositions, and manually merging the cases in such a way that all
   required fuel types are represented in the final case.


Input Description
-----------------


STARBUCS input is divided into different data blocks containing related
types of information. The standard composition data block used to define
initial (fresh) fuel composition and all other materials in the
criticality analysis problem, is read and processed by the material and
cross section processing module of SCALE (XSProc) and conforms to the
standard input conventions (see
Chapter \ 7 (SECTIONREFERENCE)
In addition to the standard composition data, three more input data
blocks are required by STARBUCS. The data blocks are entered in the form

.. highlight:: scale

::

  READ XXXX    input data   END XXXX

where **XXXX** is the data block keyword for the type of data being
entered. The types of data blocks that are entered include general
control parameter information, irradiation history and decay data or
search parameter data, and the KENO V.a or KENO-VI input specifications.
The valid block keywords for a single criticality safety calculation
using burnup credit and for burnup loading curve calculations are listed
in :numref:`tab2-3-1` and :numref:`tab2-3-2`, respectively. A minimum of four
characters is required for most keywords. The exception is the
criticality model input data block READ KENOVA or READ KENOVI in which
case the code must check additional character positions to determine the
CSAS control sequence to be executed. The keywords can be up to twelve
characters long, the first four of which must be input exactly as listed
in the table. Entering the words **READ XXXX** followed by one or more
blanks activates the data block input. All input data pertinent to block
**XXXX** are then entered. Entering **END XXXX** followed by two or more
blanks terminates data block **XXXX**.

.. _tab2-3-1:
.. table:: Valid data block keywords for a single criticality safety calculation using burnup credit
  :align: center

  +---------------------+---------------------+
  | **Data block type** | **Block keyword**   |
  +---------------------+---------------------+
  | Control parameters  | CONTROL             |
  +---------------------+---------------------+
  | Burnup history      | HISTORY or BURNDATA |
  +---------------------+---------------------+
  | KENO V.a input      | KENOVA or KENO5     |
  +---------------------+---------------------+
  | KENO-VI input       | KENOVI or KENO6     |
  +---------------------+---------------------+

.. _tab2-3-2:
.. table:: Valid data block keywords for burnup loading curve calculations.
  :align: center

  +---------------------+-------------------+
  | **Data block type** | **Block keyword** |
  +---------------------+-------------------+
  | Control parameters  | CONTROL           |
  +---------------------+-------------------+
  | Search parameters   | SEARCH            |
  +---------------------+-------------------+
  | KENO V.a input      | KENOVA or KENO5   |
  +---------------------+-------------------+

All input within a data block is entered using keywords and is free
format. Keyword entries may be of variable or array type. Variable
keyword entries include the keyword plus the “=”, followed by the value.
Array keywords are usually followed by a series of entries, each
separated by a blank or comma, and must always be terminated with an END
that does not begin in column one. In some instances a single value may
be input as an array entry; however, the word END is still always
required. Within a given input data block the keyword entries may be in
any order.

A single data entry may be entered anywhere on a line but cannot be
divided between two lines; however, array data entries may be divided
over many lines. The code identifies data keywords using only the first
four (maximum) characters in the keyword name. Beyond the first four
characters, the user may enter any alphanumeric or special character
acceptable in FORTRAN, including single blanks, before the “=”
character. Floating-point data may be entered in various forms; for
example, the value 12340.0 may be entered as: 12340, 12340.0, 1.234+4,
1.234E+4, 1.234E4, or 1.234E+04. Also, the value 0.012 may be entered as
12E−3, 12−3, 1.2−2, etc. Numeric data must be followed immediately by
one or more blanks or a comma.

Overview of input structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~

An overview of the input to the STARBUCS sequence is given in
:numref:`tab2-3-3`. This table provides an outline of the input data block
structure. The input data in positions 1 to 5 (see :numref:`tab2-3-3`) are read
and processed by the material and cross section processing module of
SCALE (XSProc). These are the first data read by the code and must be in
the order indicated. Data positions 6, 7 or 8, and 9 are read directly
by STARBUCS and may be entered in any order.

.. _tab2-3-3:
.. table:: Outline of input data for the STARBUCS sequence
  :align: center

  +-----------------+-----------------+-----------------+-----------------+
  | **Data**        | **Type of       | **Data entry**  | **Comments**    |
  |                 | data**          |                 |                 |
  | **position**    |                 |                 |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |                 | Sequence name   | =STARBUCS       | Start in column |
  |                 |                 |                 | one             |
  +-----------------+-----------------+-----------------+-----------------+
  | 1               | TITLE           | Enter a title   | 80 characters   |
  +-----------------+-----------------+-----------------+-----------------+
  | 2               | Standard SCALE  | Library name    | The currently   |
  |                 | pointwise or    |                 | available       |
  |                 | multigroup      |                 | standard SCALE  |
  |                 | cross section   |                 | cross section   |
  |                 | library name or |                 | libraries are   |
  |                 |                 |                 | listed in the   |
  |                 | the name of a   |                 | SCALE Cross     |
  |                 | user-supplied   |                 | Section         |
  |                 | multigroup      |                 | Libraries       |
  |                 | cross section   |                 | chapter, table  |
  |                 | library         |                 | *Standard SCALE |
  |                 |                 |                 | Cross-Section   |
  |                 |                 |                 | Libraries*.     |
  |                 |                 |                 |                 |
  |                 |                 |                 | STARBUCS allows |
  |                 |                 |                 | a non-standard  |
  |                 |                 |                 | SCALE           |
  |                 |                 |                 | multigroup      |
  |                 |                 |                 | cross section   |
  |                 |                 |                 | library to be   |
  |                 |                 |                 | used in a       |
  |                 |                 |                 | criticality     |
  |                 |                 |                 | calculation.    |
  +-----------------+-----------------+-----------------+-----------------+
  | 3               | Standard        | Enter the       | Begins this     |
  |                 | Composition     | appropriate     | data block with |
  |                 | specification   | data            | READ COMP and   |
  |                 | data            |                 | terminate with  |
  |                 |                 |                 | END COMP. See   |
  |                 |                 |                 | Standard        |
  |                 |                 |                 | Composition     |
  |                 |                 |                 | section for     |
  |                 |                 |                 | details.        |
  +-----------------+-----------------+-----------------+-----------------+
  | 4               | Type of         | LATTICECELL     | Begins this     |
  |                 | calculation     |                 | data block with |
  |                 |                 |                 | READ CELL and   |
  |                 |                 |                 | terminates with |
  |                 |                 |                 | END CELL. Only  |
  |                 |                 |                 | regular unit    |
  |                 |                 |                 | cells may be    |
  |                 |                 |                 | used. See       |
  |                 |                 |                 | XSProc section  |
  |                 |                 |                 | for details.    |
  +-----------------+-----------------+-----------------+-----------------+
  | 5               | Unit cell       | Enter the       | Each dimension  |
  |                 | geometry        | appropriate     | may be entered  |
  |                 | specification\  | data            | as a diameter.  |
  |                 | :sup:`a`        |                 | See XSProc      |
  |                 |                 |                 | section for     |
  |                 |                 |                 | LATTICECELL.    |
  +-----------------+-----------------+-----------------+-----------------+
  | 6               | Control         | Enter the       | Begins this     |
  |                 | parameter data  | desired data    | data block with |
  |                 |                 |                 | READ CONT and   |
  |                 |                 |                 | terminate with  |
  |                 |                 |                 | END CONT.       |
  |                 |                 |                 | See Conntrol pa\|
  |                 |                 |                 | rameter data sec|
  +-----------------+-----------------+-----------------+-----------------+
  | 7\ :sup:`b`     | Burnup history  | Enter the       | Begins this     |
  |                 | specification   | desired data    | data block with |
  |                 |                 | for each cycle  | READ HISTORY    |
  |                 |                 |                 | (or BURNDATA)   |
  |                 |                 |                 | and terminate   |
  |                 |                 |                 | with            |
  |                 |                 |                 | END HISTORY (or |
  |                 |                 |                 | BURNDATA).      |
  |                 |                 |                 | See Burnup hist/|
  |                 |                 |                 | ory data sec.   |
  +-----------------+-----------------+-----------------+-----------------+
  | 8\ :sup:`b`     | Search          | Enter the       | Begins this     |
  |                 | parameter data  | desired data    | data block with |
  |                 |                 |                 | READ SEARCH and |
  |                 |                 |                 | terminate with  |
  |                 |                 |                 | END SEARCH.     |
  |                 |                 |                 | See Search para/|
  |                 |                 |                 | meter data sec. |
  +-----------------+-----------------+-----------------+-----------------+
  | 9               | KENO data       | Enter KENO      | Begins this     |
  |                 |                 | criticality     | data block with |
  |                 |                 | model           | READ KENOVA (or |
  |                 |                 |                 | KENO5) and      |
  |                 |                 |                 | terminate with  |
  |                 |                 |                 | END KENOVA (or  |
  |                 |                 |                 | KENO5).         |
  |                 |                 |                 |                 |
  |                 |                 |                 | For KENO-VI use |
  |                 |                 |                 | block keyword   |
  |                 |                 |                 | KENOVI (or      |
  |                 |                 |                 | KENO6) in place |
  |                 |                 |                 | of KENOVA       |
  |                 |                 |                 | (or KENO5). See |
  |                 |                 |                 | Keno Input Data.|
  +-----------------+-----------------+-----------------+-----------------+
  |                 | Terminate input | END             | Must begin in   |
  |                 |                 |                 | column 1.       |
  +-----------------+-----------------+-----------------+-----------------+
  | :sup:`a` \Input |                 |                 |                 |
  | data required o\|                 |                 |                 |
  | nly for critica\|                 |                 |                 |
  | lity calculatio\|                 |                 |                 |
  | ns employing    |                 |                 |                 |
  | multigroup      |                 |                 |                 |
  | cross section   |                 |                 |                 |
  | libraries. Only |                 |                 |                 |
  | one unit cell   |                 |                 |                 |
  | may be defined  |                 |                 |                 |
  | in the cell     |                 |                 |                 |
  | data block for  |                 |                 |                 |
  | STARBUCS.       |                 |                 |                 |
  |                 |                 |                 |                 |
  | :sup:`b` Either |                 |                 |                 |
  | burnup history  |                 |                 |                 |
  | specification   |                 |                 |                 |
  | or search       |                 |                 |                 |
  | parameter data  |                 |                 |                 |
  | may be defined  |                 |                 |                 |
  | in a STARBUCS   |                 |                 |                 |
  | input.          |                 |                 |                 |
  +-----------------+-----------------+-----------------+-----------------+

Sequence specification card
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The STARBUCS analytical sequence is initiated with “=STARBUCS” beginning
in column 1 of the input. This instructs the SCALE driver module to
execute the STARBUCS sequence. The input data are then entered in
free-format. The input is terminated with the word “END” starting in
column 1. An “END” is a special data item, which may be used to delimit
an input data block, end an array of input items, and terminate the
input for the case. In the context of input data blocks, the “END” has a
name or label associated with it. An “END” used to terminate an array of
entries must not begin in column 1 as this instructs the SCALE driver to
terminate input to the sequence.

Optional sequence parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To check the input data, run STARBUCS and specify PARM=CHECK or PARM=CHK
after the analytical sequence specification as shown below.

::

  =STARBUCS PARM=CHK

Other optional input for the PARM field to control multigroup resonance
self-shielding calculations are described in the XSProc section of this
manual.

XSProc
~~~~~~

The XSProc is used to read and process the standard composition
specification data that define the initial compositions of the fuel and
all structural materials in the problem, into mixing tables and unit
cell geometry information that are used by STARBUCS. All composition
data required for the problem are entered as standard composition
entries. A detailed description of this portion of the input can be
found in the section on XSProc (Chapter 7 (SECTIONREFERENCE)). Only one UO\ :sub:`2` fuel
type is permitted in STARBUCS. Therefore, a single fuel mixture defining
the fresh fuel composition and, for criticality safety calculations
employing multigroup cross sections, the geometry description of a
single fuel lattice cell are required in a STARBUCS input file. Only the
regular unit cells SQUAREPITCH, TRIANGPITCH, SPHSQUAREP, SPHTRIANGP, and
SYMMSLACELL may be specified for the LATTICECELL entry. Outside
diameters of the fuel, gap, and clad mixtures (i.e., not the radii) are
required.

Control parameter data
~~~~~~~~~~~~~~~~~~~~~~

The control parameter data block allows the user to specify control
parameters and array data related to many of the burnup-credit analysis
parameters to be used in the problem. All input is by keyword entry. All
keywords are three-character identifiers that must be followed
immediately by an equals sign (“=”). The keywords may be in any order
within a data block. Input to the parameter data block is initiated with
the data block keywords **READ CONTROL** (only first four characters of
block name are required). The data block is terminated by the keywords
**END CONTROL**.

The types of control parameter data that may be input are summarized in
Table 2.3.4. The individual keyword entries are described below.

1.  ARP= NAME OF THE ORIGEN LIBRARY TO BE USED. A character string with
    the name of the ORIGEN library to be used in the depletion
    calculation. This is a required entry. The library must be defined
    in the SCALE text file ARPDATA.TXT that contains the cross section
    library names and interpolation data used by ARP. A description of
    an ARP input and the location of the ORIGEN cross section libraries
    are provided in *ARP Input Description* located in the ORIGEN ARP
    Module chapter. STARBUCS calculations are limited to UO\ :sub:`2`
    spent fuels.

2.  NAX= NUMBER OF AXIAL ZONES. This is the number of axial-burnup
    subdivisions. For a user-input profile the value of NAX is
    determined automatically by the code, and the NAX keyword is
    optional, provided the AXP= array has been entered. The maximum
    value of NAX must be chosen such that due product of NAX \* NHZ is
    less than or equal to 100 (i.e., NAX:sub:`max` is 100, 50, 33, 25,
    20, 16, or 14 when the number of horizontal zones is 1, 2, 3, 4, 5,
    6, or 7, respectively). By default, the profile is automatically
    normalized to unity by the code unless NPR=no. Built-in
    burnup-dependent 18‑axial-zone profiles may be selected with an
    entry of –18. These built-in profiles and the burnup range over
    which they are applied, are listed in :numref:`tab2-3-5`. These profiles
    have been proposed elsewhere (Ref. 2) as bounding axial profiles and
    are included as options for convenience only. The default value of
    NAX is –18 (use built-in profiles).

3.  NHZ= NUMBER OF HORIZONTAL ZONES. This is the number of
    horizontal-burnup subdivisions in the assembly. An optional entry if
    no horizontal profile is requested. The maximum value is seven
    zones. The exact limit is determined by the number of mixtures
    defined in the lattice cell description. If a gap and second
    moderator type are used the number of horizontal zones is limited to
    five.

4.  NUC= BURNUP-CREDIT NUCLIDES used in the criticality calculation. A
    list of actinides and/or fission products that are to be included in
    the KENO criticality safety calculation. This is an array entry
    keyword and is delimited by the keyword END. The nuclides are
    entered using their standard composition alphanumeric names, as
    listed in the Standard Composition Library chapter of the SCALE
    manual. Isotopic correction factors may be entered, optionally,
    immediately following the nuclide name. The isotopic correction
    factors will be multiplied times the spent fuel nuclide
    concentrations to account for isotopic composition bias.
    The concentration of any nuclide that does not have a correction
    factor is not adjusted. To select all available actinide and fission
    product nuclides (with cross section data and atom densities greater
    than 1.0E−29) for the criticality calculation, the user may select
    NUC= ALL, without an END terminator. This is the only situation
    where an array entry does not require an END. Note that the set of
    nuclides tracked by ORIGEN in any decay or irradiation calculation,
    documented in the ORIGEN Reaction Resource Contents chapter, is much
    larger than the set of nuclides with available cross sections for
    neutron transport calculations, documented in the SCALE Cross
    Section Libraries chapter. Only nuclides with available cross
    sections for neutron transport calculations are included in the
    irradiated fuel compositions for criticality calculations.

5.  FLE= FUEL LIGHT ELEMENT NUCLIDES. A user-provided list of light
    element nuclides that are to be included in the irradiated fuel
    compositions for a CSAS5 or a CSAS6 calculation. This is an array
    entry keyword and is delimited by the keyword END. The nuclides are
    entered using their standard composition alphanumeric names, as
    listed in Standard Composition Library chapter of the SCALE manual.
    To select all available light element nuclides (with cross section
    data and atom densities greater than 1.0E−29) for the criticality
    calculation, the user may specify FLE= ALL, without an END
    terminator. This is the only situation where an array entry does not
    require an END. The use of the keyword FLE is not required if only
    o-16 is to be included in the composition of irradiated uranium
    oxide fuel pellets. For these material mixtures, o-16 will be
    automatically included in irradiated fuel compositions due to its
    significant concentration. Isotopic correction factors are not
    allowed for light element nuclides. Note that the set of nuclides
    tracked by ORIGEN in any decay or irradiation calculation,
    documented in the ORIGEN Reaction Resource Contents chapter, is much
    larger than the set of nuclides with available cross sections for
    neutron transport calculations, documented in the SCALE Cross
    Section Libraries chapter. Only nuclides with available cross
    sections for neutron transport calculations are included in the
    irradiated fuel compositions for criticality calculations.

6.  AXP= AXIAL-BURNUP PROFILE. The user-supplied axial-burnup profile of
    the assembly to be used in the analysis. This entry is required
    unless use of the built-in burnup-dependent axial profiles shown in
    :numref:`tab2-3-5` is requested (NAX= −18). If NAX is set to anything other
    than −18, the AXP array must contain NAX entries. Otherwise, the
    value of NAX is determined automatically by the code. By default
    (NPR=yes), the profile is automatically normalized by the code; this
    may be disabled by setting NPR=no. If the burnup profile is
    normalized, it is implicitly assumed that the height/volume of each
    axial region is uniform when determining the average fuel burnup
    (i.e., the burnup of each axial region is equally weighted). **The
    user is cautioned that if fuel region subdivisions of unequal volume
    are used, normalization should not be applied and the user must
    ensure a correct correspondence between the axial-profile input and
    the axial regions specified in the criticality calculation. AXP** is
    an array entry and must be delimited by an END that must not start
    in the first column.

7.  HZP= HORIZONTAL-BURNUP PROFILE. An optional array entry used to
    specify a burnup gradient across assemblies. The elements of the
    array are the ratios of the burnups of horizontal subdivisions in
    the assembly to average assembly burnup (entry for the POWER=
    keyword described in :ref:`burnup-history-data`). If NHZ is input, the HZP array
    must contain NHZ entries delimited by an END that must not start in
    the first column. Otherwise, the value of NHZ is determined
    automatically by the code. The profile will be normalized if NPR=yes
    (default). Sample problem 5 illustrates use of this option.

8.  FIX= FIXED ASSEMBLY POWER OPTION. Option to select a constant
    specific power level for the depletion analysis for all axial and
    horizontal zones of the assembly. For FIX=yes, the depletion
    analysis for all zones is performed using the specific power input
    in the power history data block for the POWER= keyword. The
    irradiation time is adjusted to achieve the desired burnup. The
    default of FIX=no applies a variable power for all zones and a
    constant irradiation time as defined by the BURN= keyword.

9.  NPR= NORMALIZE PROFILE. Option to control whether the user input
    axial- and horizontal-burnup profiles will be normalized. The input
    profiles are automatically normalized using NPR=yes (default). If
    fuel region subdivisions of unequal volume are used, NPR=NO should
    be specified.

10. MOD= AXIAL MODERATOR DENSITY. This is an array entry keyword and is
    delimited by the keyword END. The array dimension is equal to the
    number of axial zones (NAX entry) and the array values are provided
    in the same order as the AXP array elements. This input array is
    required only if the applicable ORIGEN library contains variable
    moderator density cross sections.

11. BUG= DEBUG PRINT OPTION. BUG=yes will print program debugging
    variables and arrays in STARBUCS. The default is BUG=no.

.. _tab2-3-4:
.. table:: Table of control parameter data.
  :align: center

  +-----------------+-----------------+-----------------+-----------------+
  | **Keyword**     | **Data**        | **Default**     | **Comments**    |
  |                 |                 |                 |                 |
  | **name**        | **type**        | **value**       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | READ CONTROL    |                 | Initiate        |                 |
  |                 |                 | reading the     |                 |
  |                 |                 | control         |                 |
  |                 |                 | parameter block |                 |
  |                 |                 | of data         |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | ARP=            | Character       | None            | Name of the     |
  |                 |                 |                 | ORIGEN library  |
  |                 |                 |                 | to be used.     |
  |                 |                 |                 | Required.       |
  |                 |                 |                 | Library must be |
  |                 |                 |                 | defined in      |
  |                 |                 |                 | SCALE text file |
  |                 |                 |                 | ARPDATA.TXT.    |
  +-----------------+-----------------+-----------------+-----------------+
  | NAX=            | Integer         | −18             | Number of       |
  |                 |                 |                 | axial-burnup    |
  |                 |                 |                 | subdivisions in |
  |                 |                 |                 | fuel assembly.  |
  |                 |                 |                 | The value of    |
  |                 |                 |                 | NAX is          |
  |                 |                 |                 | determined      |
  |                 |                 |                 | automatically   |
  |                 |                 |                 | if an axial     |
  |                 |                 |                 | profile is      |
  |                 |                 |                 | input using     |
  |                 |                 |                 | AXP= entries.   |
  |                 |                 |                 | The maximum     |
  |                 |                 |                 | value of NAX is |
  |                 |                 |                 | 100. Default    |
  |                 |                 |                 | value (−18)     |
  |                 |                 |                 | applies a       |
  |                 |                 |                 | built-in        |
  |                 |                 |                 | 18‑axial-region |
  |                 |                 |                 | -burnup         |
  |                 |                 |                 | profile.        |
  +-----------------+-----------------+-----------------+-----------------+
  | NHZ=            | Integer         | 1               | Number of       |
  |                 |                 |                 | horizontal-burn |
  |                 |                 |                 | up              |
  |                 |                 |                 | subdivisions.   |
  |                 |                 |                 | Maximum value   |
  |                 |                 |                 | of              |
  |                 |                 |                 | 5–7 zones (see  |
  |                 |                 |                 | Sect. 2.3.4.5). |
  |                 |                 |                 | No entry is     |
  |                 |                 |                 | required if     |
  |                 |                 |                 | horizontal      |
  |                 |                 |                 | profile is not  |
  |                 |                 |                 | used.           |
  +-----------------+-----------------+-----------------+-----------------+
  | NUC=            | Character and   | None            | List of         |
  |                 | real mixed      |                 | burnup-credit   |
  |                 | array\ :sup:`a` |                 | nuclides, and   |
  |                 |                 |                 | optionally the  |
  |                 |                 |                 | corresponding   |
  |                 |                 |                 | isotopic        |
  |                 |                 |                 | correction      |
  |                 |                 |                 | factors, to be  |
  |                 |                 |                 | included in the |
  |                 |                 |                 | criticality     |
  |                 |                 |                 | calculation.\   |
  |                 |                 |                 | :sup:`b`        |
  |                 |                 |                 | Array entry     |
  |                 |                 |                 | generally       |
  |                 |                 |                 | delimited by    |
  |                 |                 |                 | END, unless ALL |
  |                 |                 |                 | is selected.    |
  |                 |                 |                 | Nuclides are    |
  |                 |                 |                 | input using     |
  |                 |                 |                 | their standard  |
  |                 |                 |                 | composition     |
  |                 |                 |                 | alphanumeric    |
  |                 |                 |                 | identifiers.    |
  +-----------------+-----------------+-----------------+-----------------+
  | FLE=            | Character       | o-16            | List of light   |
  |                 | array\ :sup:`a` |                 | element         |
  |                 |                 |                 | nuclides to be  |
  |                 |                 |                 | included in the |
  |                 |                 |                 | criticality     |
  |                 |                 |                 | calculation.\   |
  |                 |                 |                 | :sup:`b`        |
  |                 |                 |                 | Array entry     |
  |                 |                 |                 | generally       |
  |                 |                 |                 | delimited by    |
  |                 |                 |                 | END, unless ALL |
  |                 |                 |                 | is selected.    |
  |                 |                 |                 | Nuclides are    |
  |                 |                 |                 | input using     |
  |                 |                 |                 | their standard  |
  |                 |                 |                 | composition     |
  |                 |                 |                 | alphanumeric    |
  |                 |                 |                 | identifiers.    |
  +-----------------+-----------------+-----------------+-----------------+
  | AXP=            | Real array\     | See NAX         | Axial-burnup-pr |
  |                 | :sup:`a`        |                 | ofile           |
  |                 |                 |                 | array. Required |
  |                 |                 |                 | if NAX > 0. NAX |
  |                 |                 |                 | entries that    |
  |                 |                 |                 | define the      |
  |                 |                 |                 | axial-burnup    |
  |                 |                 |                 | shape. The      |
  |                 |                 |                 | profile is      |
  |                 |                 |                 | automatically   |
  |                 |                 |                 | normalized if   |
  |                 |                 |                 | NPR=YES         |
  |                 |                 |                 | (default).      |
  |                 |                 |                 | Delimited by    |
  |                 |                 |                 | END.            |
  +-----------------+-----------------+-----------------+-----------------+
  | HZP=            | Real array\     | None            | Horizontal-burn |
  |                 | :sup:`a`        |                 | up-profile      |
  |                 |                 |                 | array. Required |
  |                 |                 |                 | if NHZ > 1.     |
  |                 |                 |                 | Array containin |
  |                 |                 |                 | g               |
  |                 |                 |                 | NHZ entries     |
  |                 |                 |                 | that define the |
  |                 |                 |                 | horizontal,     |
  |                 |                 |                 | or radial,      |
  |                 |                 |                 | burnup profile  |
  |                 |                 |                 | for the         |
  |                 |                 |                 | analysis. Array |
  |                 |                 |                 | is              |
  |                 |                 |                 | automatically   |
  |                 |                 |                 | normalized by   |
  |                 |                 |                 | the code.       |
  |                 |                 |                 | Delimited by    |
  |                 |                 |                 | END.            |
  +-----------------+-----------------+-----------------+-----------------+
  | MOD=            | Real array\     | None            | Axial-moderator |
  |                 | :sup:`a`        |                 | density,        |
  |                 |                 |                 | applied in the  |
  |                 |                 |                 | fuel depletion  |
  |                 |                 |                 | analysis.       |
  |                 |                 |                 | Note that MOD=  |
  |                 |                 |                 | is required     |
  |                 |                 |                 | only if the     |
  |                 |                 |                 | ORIGEN library  |
  |                 |                 |                 | contains        |
  |                 |                 |                 | variable        |
  |                 |                 |                 | moderator       |
  |                 |                 |                 | density cross   |
  |                 |                 |                 | sections.       |
  |                 |                 |                 | NAX entries     |
  |                 |                 |                 | ordered as AXP= |
  |                 |                 |                 | array.          |
  |                 |                 |                 | Delimited by    |
  |                 |                 |                 | END. Moderator  |
  |                 |                 |                 | density default |
  |                 |                 |                 | values are not  |
  |                 |                 |                 | available in    |
  |                 |                 |                 | STARBUCS for    |
  |                 |                 |                 | variable        |
  |                 |                 |                 | moderator       |
  |                 |                 |                 | density cross   |
  |                 |                 |                 | sections.       |
  +-----------------+-----------------+-----------------+-----------------+
  | FIX=            | Character       | No              | Option to       |
  |                 |                 |                 | select a        |
  |                 |                 |                 | constant        |
  |                 |                 |                 | specific power  |
  |                 |                 |                 | level for all   |
  |                 |                 |                 | axial and       |
  |                 |                 |                 | horizontal      |
  |                 |                 |                 | zones of the    |
  |                 |                 |                 | assembly using  |
  |                 |                 |                 | FIX=yes.        |
  +-----------------+-----------------+-----------------+-----------------+
  | NPR=            | Character       | Yes             | Option to       |
  |                 |                 |                 | normalize       |
  |                 |                 |                 | user-input      |
  |                 |                 |                 | axial- and      |
  |                 |                 |                 | horizontal-burn |
  |                 |                 |                 | up              |
  |                 |                 |                 | profiles.       |
  |                 |                 |                 | Default is to   |
  |                 |                 |                 | automatically   |
  |                 |                 |                 | normalize       |
  |                 |                 |                 | profiles.       |
  +-----------------+-----------------+-----------------+-----------------+
  | BUG=            | Character       | No              | Optional debug  |
  |                 |                 |                 | printout with   |
  |                 |                 |                 | BUG=yes.        |
  +-----------------+-----------------+-----------------+-----------------+
  | END CONTROL     |                 | End of the      |                 |
  |                 |                 | control         |                 |
  |                 |                 | parameter block |                 |
  |                 |                 | of data         |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |:sup:`a` Termina\|                 |                 |                 |
  | te array data   |                 |                 |                 |
  | entries with    |                 |                 |                 |
  | end. Do not     |                 |                 |                 |
  | place this end  |                 |                 |                 |
  | in column 1.    |                 |                 |                 |
  |                 |                 |                 |                 |
  |:sup:`b` Note th\|                 |                 |                 |
  | at the set of   |                 |                 |                 |
  | nuclides        |                 |                 |                 |
  | tracked by      |                 |                 |                 |
  | ORIGEN in any   |                 |                 |                 |
  | decay or        |                 |                 |                 |
  | irradiation     |                 |                 |                 |
  | calculation,    |                 |                 |                 |
  | documented in   |                 |                 |                 |
  | the ORIGEN      |                 |                 |                 |
  | Reaction        |                 |                 |                 |
  | Resource        |                 |                 |                 |
  | Contents        |                 |                 |                 |
  | chapter, is     |                 |                 |                 |
  | much larger     |                 |                 |                 |
  | than the set of |                 |                 |                 |
  | nuclides with   |                 |                 |                 |
  | available cross |                 |                 |                 |
  | sections for    |                 |                 |                 |
  | neutron         |                 |                 |                 |
  | transport       |                 |                 |                 |
  | calculations,   |                 |                 |                 |
  | documented in   |                 |                 |                 |
  | the SCALE Cross |                 |                 |                 |
  | Section         |                 |                 |                 |
  | Libraries       |                 |                 |                 |
  | chapter. Only   |                 |                 |                 |
  | nuclides with   |                 |                 |                 |
  | available cross |                 |                 |                 |
  | sections for    |                 |                 |                 |
  | neutron         |                 |                 |                 |
  | transport       |                 |                 |                 |
  | calculations    |                 |                 |                 |
  | are included in |                 |                 |                 |
  | the irradiated  |                 |                 |                 |
  | fuel            |                 |                 |                 |
  | compositions    |                 |                 |                 |
  | for criticality |                 |                 |                 |
  | calculations.   |                 |                 |                 |
  +-----------------+-----------------+-----------------+-----------------+

.. _tab2-3-5:
.. table:: Built-in burnup-dependent axial profiles, NAX= 18 from :cite:`lancaster_actinide-only_1998`)
  :align: center

  +-------------+-------------+-------------+-------------+-------------+
  | **Axial**   | **Fraction  | **Burnup    | **18 ≤      | **Burnup    |
  |             | of**        | < 18 GWd/MT | Burnup      | ≥ 30 GWd/MT |
  | **zone      |             | U**         | < 30 GWd/MT | U**         |
  | no.**       | **core      |             | U**         |             |
  |             | height**    |             |             |             |
  +-------------+-------------+-------------+-------------+-------------+
  |             |             | **1**       | **2**       | **3**       |
  +-------------+-------------+-------------+-------------+-------------+
  | 1           | 0.0278      | 0.649       | 0.668       | 0.652       |
  +-------------+-------------+-------------+-------------+-------------+
  | 2           | 0.0833      | 1.044       | 1.034       | 0.967       |
  +-------------+-------------+-------------+-------------+-------------+
  | 3           | 0.1389      | 1.208       | 1.150       | 1.074       |
  +-------------+-------------+-------------+-------------+-------------+
  | 4           | 0.1944      | 1.215       | 1.094       | 1.103       |
  +-------------+-------------+-------------+-------------+-------------+
  | 5           | 0.2500      | 1.214       | 1.053       | 1.108       |
  +-------------+-------------+-------------+-------------+-------------+
  | 6           | 0.3056      | 1.208       | 1.048       | 1.106       |
  +-------------+-------------+-------------+-------------+-------------+
  | 7           | 0.3611      | 1.197       | 1.064       | 1.102       |
  +-------------+-------------+-------------+-------------+-------------+
  | 8           | 0.4167      | 1.189       | 1.095       | 1.097       |
  +-------------+-------------+-------------+-------------+-------------+
  | 9           | 0.4722      | 1.188       | 1.121       | 1.094       |
  +-------------+-------------+-------------+-------------+-------------+
  | 10          | 0.5278      | 1.192       | 1.135       | 1.094       |
  +-------------+-------------+-------------+-------------+-------------+
  | 11          | 0.5833      | 1.195       | 1.140       | 1.095       |
  +-------------+-------------+-------------+-------------+-------------+
  | 12          | 0.6389      | 1.190       | 1.138       | 1.096       |
  +-------------+-------------+-------------+-------------+-------------+
  | 13          | 0.6944      | 1.156       | 1.130       | 1.095       |
  +-------------+-------------+-------------+-------------+-------------+
  | 14          | 0.7500      | 1.022       | 1.106       | 1.086       |
  +-------------+-------------+-------------+-------------+-------------+
  | 15          | 0.8056      | 0.756       | 1.049       | 1.059       |
  +-------------+-------------+-------------+-------------+-------------+
  | 16          | 0.8611      | 0.614       | 0.933       | 0.971       |
  +-------------+-------------+-------------+-------------+-------------+
  | 17          | 0.9167      | 0.481       | 0.669       | 0.738       |
  +-------------+-------------+-------------+-------------+-------------+
  | 18          | 0.9722      | 0.284       | 0.373       | 0.462       |
  +-------------+-------------+-------------+-------------+-------------+

.. _burnup-history-data:

Burnup history data
~~~~~~~~~~~~~~~~~~~

The burnup history data block defines the irradiation history for the
assembly. These data are entered by keyword. The keywords are summarized
in :numref:`tab2-3-6`. Only the first four characters of the keywords are
required (i.e., any characters after the first four characters are
optional). A minimum of two entries are required for each cycle, (1) the
average assembly power (POWER=) and (2) the irradiation time (BURN=).
The decay time (DOWN=), if any, at the end of the cycle, and the number
of cross section libraries (NLIB=) are optional. The word END is
required to delimit the entries for each cycle. The entries within a
given cycle may be in any order.

The burnup history data block reading is initiated with the keywords
READ HISTORY (or BURNDATA) and terminated by END HISTORY (or BURNDATA).

POWER= The average specific power of the assembly for this cycle.
The units of the specific power are in MW/MTU (W/g) of initial uranium.
The axial and horizontal profiles are multiplied by the specific power
to achieve the desired spatially-dependent burnup profiles for the
assembly when FIX=NO (default). If FIX=YES, the specific power input
using this keyword is assumed to be uniform over all fuel regions (axial
and horizontal) and the code will adjust the irradiation time to obtain
the desired burnup for each region.

BURN= THE IRRADIATION TIME FOR THIS CYCLE. The cycle irradiation time in
days.

DOWN= CYCLE DOWN TIME. An optional entry to specify the down time, in
days, at the end of an irradiation cycle. The down time is simulated as
an irradiation time step of effectively zero power after the irradiation
cycle. The down time for the last cycle is simulated as a separate
ORIGEN decay case with nine equally-spaced time steps. If a negative
down time is input, the time steps are spaced logarithmically.

NLIB= LIBRARIES PER CYCLE. An optional entry to request multiple cross
section libraries during a depletion cycle. If requested, the code
automatically subdivides the cycle in NLIB segments of uniform duration
and generates a separate library for the depletion analysis for each
segment using ARP. Generating multiple libraries provides a more
accurate representation of the time-dependent cross section variation
during the burnup analysis. Each segment of the cycle is assumed to have
the same specific power, and no down time is assumed between each
segment of the cycle.

END The word END is required to terminate the input for each cycle.

Repeat the above entries for each cycle to define the complete assembly
power history.

.. _tab2-3-6:
.. table:: Table of power history data.
  :align: center

  +-----------------+-----------------+-----------------+-----------------+
  | **Keyword**     | **Data**        | **Default**     | **Comments**    |
  |                 |                 |                 |                 |
  | **name**        | **type**        | **value**       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | READ HISTORY    |                 |                 | Start of burnup |
  | (or BURNDATA)\  |                 |                 | history data    |
  | :sup:`a`        |                 |                 | block           |
  +-----------------+-----------------+-----------------+-----------------+
  | POWER=          | Real variable   | None            | Average         |
  |                 |                 |                 | assembly power  |
  |                 |                 |                 | for this cycle  |
  |                 |                 |                 | (MW/MTU)        |
  +-----------------+-----------------+-----------------+-----------------+
  | BURN=           | Real variable   | None            | Cycle           |
  |                 |                 |                 | irradiation     |
  |                 |                 |                 | time (days)     |
  +-----------------+-----------------+-----------------+-----------------+
  | DOWN=           | Real variable   | 0               | End-of-cycle    |
  |                 |                 |                 | decay time      |
  |                 |                 |                 | (days).         |
  |                 |                 |                 | Optional. A     |
  |                 |                 |                 | negative down   |
  |                 |                 |                 | time may be     |
  |                 |                 |                 | used to select  |
  |                 |                 |                 | logarithmic     |
  |                 |                 |                 | decay time      |
  |                 |                 |                 | intervals for   |
  |                 |                 |                 | the last decay  |
  |                 |                 |                 | case.           |
  +-----------------+-----------------+-----------------+-----------------+
  | NLIB/CYCLE=     | Integer         | 1               | Number of       |
  |                 | variable        |                 | libraries to be |
  |                 |                 |                 | applied in this |
  |                 |                 |                 | cycle.          |
  |                 |                 |                 | Optional.       |
  |                 |                 |                 | If multiple     |
  |                 |                 |                 | libraries are   |
  |                 |                 |                 | requested for   |
  |                 |                 |                 | this cycle, the |
  |                 |                 |                 | cycle is        |
  |                 |                 |                 | subdivided into |
  |                 |                 |                 | equal time      |
  |                 |                 |                 | segments, and   |
  |                 |                 |                 | an updated      |
  |                 |                 |                 | library is      |
  |                 |                 |                 | generated for   |
  |                 |                 |                 | each segment.   |
  |                 |                 |                 | No down time is |
  |                 |                 |                 | simulated       |
  |                 |                 |                 | between         |
  |                 |                 |                 | segments.       |
  +-----------------+-----------------+-----------------+-----------------+
  | END             |                 |                 | Required.       |
  |                 |                 |                 | Defines the end |
  |                 |                 |                 | of the data for |
  |                 |                 |                 | the current     |
  |                 |                 |                 | cycle. Repeat   |
  |                 |                 |                 | the above       |
  |                 |                 |                 | entries for     |
  |                 |                 |                 | each cycle in   |
  |                 |                 |                 | the irradiation |
  |                 |                 |                 | history. An     |
  |                 |                 |                 | END, not to     |
  |                 |                 |                 | begin in        |
  |                 |                 |                 | column 1, must  |
  |                 |                 |                 | terminate each  |
  |                 |                 |                 | cycle           |
  |                 |                 |                 | definition.     |
  +-----------------+-----------------+-----------------+-----------------+
  | END HISTORY (or |                 |                 | End block       |
  | BURNDATA)\ *a*  |                 |                 |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | :sup:`a` Only   |                 |                 |                 |
  | the first four  |                 |                 |                 |
  | characters are  |                 |                 |                 |
  | required, i.e., |                 |                 |                 |
  | HIST (or BURN). |                 |                 |                 |
  +-----------------+-----------------+-----------------+-----------------+

Search parameter data
~~~~~~~~~~~~~~~~~~~~~

The search parameter data block defines input data for burnup loading
curve analyses for commercial UO\ :sub:`2` spent fuels. Burnup history
input data are not allowed in an input file that supplies search
parameters. A burnup history data block is generated in STARBUCS for
subsequent iterative calculations using the initial user-supplied search
parameter data. STARBUCS sample problem *starbucs1.input* contains a
search data block to request burnup loading curve analyses for spent
fuel at various burnups. The search data block reading is initiated with
the keywords READ SEARCH and terminated by END SEARCH. The keywords are
summarized in :numref:`tab2-3-7`. These keywords may be in any order.

USL= THE UPPER SUBCRITICAL LIMIT FOR BURNUP LOADING.

EPS= TOLERANCE ON CONVERGENCE. The convergence criterion used in the
search for initial fuel enrichment so that user-specified *k*\ :sub:`eff` value
is within USL ± EPS. The tolerance value must be greater that the
standard deviation of the calculated k\ :sub:`eff` for the solution to
converge.

ITMAX= MAXIMUM ITERATIONS ALLOWED FOR EACH ENRICHMENT SEARCH. The search
for initial fuel enrichment stops when the number of iterations exceeds
this parameter and a warning message is provided to the user.

ECL= LOWER ENRICHMENT CONSTRAINT. The unit for this parameter is wt%
:sup:`235`\ U. The lower enrichment constraint must be within the
enrichment interval used in the ORIGEN library specified in READ CONTROL
data block.

ECH= UPPER ENRICHMENT CONSTRAINT. The unit for this parameter is wt%
:sup:`235`\ U. The upper enrichment constraint must be within the
enrichment interval used in the ORIGEN library specified in READ CONTROL
data block.

BU= ARRAY OF REQUESTED BURNUP VALUES (GWd/MTU). The word END is required
to terminate this array. The user inputs a series of discharge burnup
values for which the initial fuel enrichments that result in a desired
*k*\ :sub:`eff` value (USL ± EPS) are to be determined.

AVGBU= AVERAGE BURNUP PER CYCLE (GWd/MTU). An optional entry used to
determine the number of irradiation cycles as the ratio of a burnup
value in the BU array to AVGBU.

POWER= The average specific power of the assembly. The units of the
specific power are in MW/MTU (W/g) of initial uranium. This entry has
the same function as the entry for POWER= keyword in the HISTORY data
block (see :ref:`burnup-history-data`). It is also used to determine cycle
irradiation time as the ratio of a burnup value in the BU array to
average assembly power.

FDT= FRACTIONAL DOWNTIME. An optional entry used to determine down time
between irradiation cycles (the entry for DOWN= keyword in the HISTORY
data block) if fuel irradiation requires two or more cycles. For
example, for a cycle with 365 days of irradiation followed by a 30-day
downtime, FDT = 30 / 395 = 0.07595. STARBUCS uses the user-provided FDT
to compute cycle downtime as the irradiation time per cycle multiplied
by FDT and divided by (1-FDT).

DEC= DECAY TIME AFTER IRRADIATION. An optional entry to specify the
decay time, in days, after fuel discharge. A negative value may be used
to select logarithmic decay time intervals.

NLIB= NUMBER OF LIBRARIES PER CYCLE. An optional entry to request
multiple cross section libraries during a depletion cycle. Generating
multiple libraries provides a more accurate representation of the
time-dependent cross section variation during the burnup analysis. Each
segment of the cycle is assumed to have the same specific power.

FFE= FRESH FUEL ENRICHMENT. The purpose of this option is to help in
reducing the total number of iterations needed to achieve convergence.
There are two options implemented in STARBUCS for the fresh fuel
enrichment value to be used in the first inner iterations over fuel
enrichment, FFE=SEARCH (default) and FFE=INPUT. With the default option
(FFE=SEARCH), the lower enrichment bound and the starting fresh fuel
enrichment at the beginning of a search are adjusted based on the
results of the previous outer iteration over burnup. The procedure
includes the following steps. First, the user requested burnup values
are sorted in ascending order so that STARBUCS outer iterations over
burnup proceed from the lowest to the highest burnup value. Then, the
initial fresh fuel for the lowest burnup is changed to the mid-value of
the enrichment interval, (ECL+ECU)/2, and the search for the fresh fuel
enrichment corresponding to the lowest burnup is initiated and
completed. Suppose that a solution for this burnup step exists. This
solution becomes the lower enrichment constraint (ECL) in the search
passes for the next burnup value and the initial fresh fuel enrichment
is chosen as the middle point of the enrichment interval. The procedure
is applied for the entire set of the requested burnups. The average
number of iterations for each burnup step with this option is
approximately 4. The alternate option (FFE=INPUT) starts a search for
fuel enrichment with the user supplied fresh fuel enrichment.

.. _tab2-3-7:
.. table:: Table of search data.
  :align: center

  +-----------------+-----------------+-----------------+-----------------+
  | **Keyword**     | **Data**        | **Default**     | **Comments**    |
  |                 |                 |                 |                 |
  | **Name**        | **type**        | **value**       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | READ SEARCH\    |                 |                 | Initiate        |
  | :sup:`a`        |                 |                 | reading the     |
  |                 |                 |                 | search block of |
  |                 |                 |                 | data.           |
  |                 |                 |                 |                 |
  |                 |                 |                 |                 |
  |                 |                 |                 |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | USL=            | Real            | 1.0             | Upper           |
  |                 |                 |                 | subcritical     |
  |                 |                 |                 | limit.          |
  +-----------------+-----------------+-----------------+-----------------+
  | EPS=            | Real            | 0.005           | Tolerance on    |
  |                 |                 |                 | convergence.    |
  +-----------------+-----------------+-----------------+-----------------+
  | ITMAX=          | Integer         | 10              | Iteration       |
  |                 |                 |                 | limit.          |
  +-----------------+-----------------+-----------------+-----------------+
  | ECL=            | Real            | 1.5             | Lower initial   |
  |                 |                 |                 | fuel enrichment |
  |                 |                 |                 | constraint      |
  |                 |                 |                 | (U-235 wt%).    |
  +-----------------+-----------------+-----------------+-----------------+
  | ECH=            | Real            | 5.0             | Upper initial   |
  |                 |                 |                 | fuel enrichment |
  |                 |                 |                 | constraint      |
  |                 |                 |                 | (U-235 wt%).    |
  +-----------------+-----------------+-----------------+-----------------+
  | BU              | Real\ :sup:`b`  | None            | Array entry of  |
  |                 |                 |                 | requested       |
  |                 |                 |                 | burnup values   |
  |                 |                 |                 | (GWd/MTU).\     |
  |                 |                 |                 | :sup:`c`        |
  +-----------------+-----------------+-----------------+-----------------+
  | AVGBU=          | Real            | 20.0            | Average burnup  |
  |                 |                 |                 | per cycle.      |
  +-----------------+-----------------+-----------------+-----------------+
  | POWER=          | Real            | 25.0            | Average         |
  |                 |                 |                 | specific power  |
  |                 |                 |                 | (W/g).          |
  +-----------------+-----------------+-----------------+-----------------+
  | FDT=            | Real            | 0.2             | Fractional      |
  |                 |                 |                 | downtime.       |
  +-----------------+-----------------+-----------------+-----------------+
  | DEC=            | Real            | 1825.0          | Decay time      |
  |                 |                 |                 | (days).         |
  +-----------------+-----------------+-----------------+-----------------+
  | NLIB=           | Integer         | 2               | Libraries per   |
  |                 |                 |                 | cycle.          |
  +-----------------+-----------------+-----------------+-----------------+
  | FFE=            | Character       | SEARCH          | Fresh fuel      |
  |                 |                 |                 | option.         |
  |                 |                 |                 | FFE=INPUT       |
  |                 |                 |                 | starts the      |
  |                 |                 |                 | outer           |
  |                 |                 |                 | iterations over |
  |                 |                 |                 | the burnup      |
  |                 |                 |                 | values with     |
  |                 |                 |                 | user supplied   |
  |                 |                 |                 | fresh fuel      |
  |                 |                 |                 | composition.    |
  |                 |                 |                 | FFE=SEARCH      |
  |                 |                 |                 | helps in        |
  |                 |                 |                 | reducing the    |
  |                 |                 |                 | number of       |
  |                 |                 |                 | search passes   |
  |                 |                 |                 | (approximately  |
  |                 |                 |                 | 4 in average).  |
  +-----------------+-----------------+-----------------+-----------------+
  |                 |                 |                 |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |   END SEARCH    |                 | End of the      |                 |
  |                 |                 | search data     |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | :sup:`a` \Only  |                 |                 |                 |
  | the first four  |                 |                 |                 |
  | characters are  |                 |                 |                 |
  | required.       |                 |                 |                 |
  |                 |                 |                 |                 |
  | :sup:`b` Termin\|                 |                 |                 |
  | ate array data  |                 |                 |                 |
  | entries with    |                 |                 |                 |
  | end. Do not     |                 |                 |                 |
  | place this end  |                 |                 |                 |
  | in column 1.    |                 |                 |                 |
  |                 |                 |                 |                 |
  | :sup:`c` There  |                 |                 |                 |
  | are no restrain\|                 |                 |                 |
  | ts on the maxim\|                 |                 |                 |
  | um number of the|                 |                 |                 |
  | burnup values   |                 |                 |                 |
  | requested in    |                 |                 |                 |
  | burnup loading  |                 |                 |                 |
  | curve           |                 |                 |                 |
  | calculations. A |                 |                 |                 |
  | user may        |                 |                 |                 |
  | consider        |                 |                 |                 |
  | computer time   |                 |                 |                 |
  | and resources   |                 |                 |                 |
  | in assessing    |                 |                 |                 |
  | the maximum     |                 |                 |                 |
  | number of       |                 |                 |                 |
  | burnup values   |                 |                 |                 |
  | in this array.  |                 |                 |                 |
  +-----------------+-----------------+-----------------+-----------------+

KENO input data
~~~~~~~~~~~~~~~

The KENO input for the problem is specified in the KENO data block.
Input to the data block is initiated with the data block keywords **READ
KENO or READ KENOVA** and is terminated by the keywords **END** **KENO**
or **END** **KENOVA** for criticality calculations using **KENO V.a**.
Input to the data block is initiated with the data block keywords **READ
KENOVI or READ KENO6** and is terminated by the keywords **END**
**KENOVI** or **END** **KENO6** for criticality calculations using
**KENO VI**. STARBUCS performs no error checking of the KENO input. The
data within the data block delimiters is copied, without change, to the
CSAS input file and executed. The user is therefore advised to ensure
that the KENO input is free of errors by first running the case within
CSAS5 or CSAS6 before applying the input in STARBUCS.

The input requirements for KENO V.a and KENO-VI are not described in
this section, but are described in detail in the KENO chapter of this
manual. This section describes only the input requirements as related to
the execution of KENO within STARBUCS and the conventions used for
module compatibility.

The mixture numbers for each of the non-fuel materials applied to the
material regions of the KENO model are defined as the mixture numbers
(MX) specified in the standard composition input. STARBUCS automatically
defines the *MIXTURE ID* for each of the fuel regions according to the
axial and/or horizontal zones defined by the NAX and NHZ entries in the
burnup-profile arrays. The first axial-zone mixture is assigned MX=101,
and is incremented by one for each additional axial zone. Therefore, in
a problem that defines 18 axial zones, spent fuel mixtures will be
generated with identifiers that range from 101 to 118. The
correspondence of these mixtures to the assembly locations is determined
by the ordering of the AXP= input array that defines the axial-burnup
profile for the assembly. If the AXP= array orders the burnup profile
from the bottom of the assembly to the top of the assembly, the
resulting MX=101 will correspond to the bottom axial-zone segment, and
MX=118 would correspond to the top axial zone. If multiple horizontal
zones are defined, then the numbering sequence of the second horizontal
zone will start at MX=201 and, in the example given here, would range up
to MX=218. Refer to :ref:`cap-and-lim` for limitations in the mixture-numbering
scheme. The mixture-numbering scheme is illustrated in :numref:`fig2-3-3`.

Sample problems
---------------

A series of example problems are presented to illustrate the application
of STARBUCS to burnup-credit criticality safety and burnup loading curve
analyses. Sample problem 1 is a simple pin-cell problem for burnup
loading curve iterative calculations. The fuel pin contains a single
axial-burnup zone (i.e., uniform-axial burnup). It is useful to
illustrate the main features of the system and demonstrate functionality
of the system modules within SCALE. Problem 2 illustrates the same
problem with 18-axial burnup-dependent zones. Problem 3 extends the
pin-cell model to an array of spent fuel assemblies residing in a
water-filled pool. The models apply 18-axial-burnup-dependent zones.
Problem 4 is a generic cask model, and this problem exercises more of
the burnup credit options available in STARBUCS. Problem 5 illustrates
the use of the horizontal-burnup option for a simple 4 × 4 array of
spent fuel assemblies residing in water. Sample problem 6 uses KENO-VI
to model a hexagonal VVER‑440 fuel assembly.

Sample problem 1
~~~~~~~~~~~~~~~~

Sample problem 1, listed in :numref:`list2-3-1`, defines a simple infinite
UO\ :sub:`2` pin-cell model with uniform-axial burnup for burnup loading
curve calculations. The initial fuel enrichment is 2.0 wt %. The control
parameter data block specifies that the standard Westinghouse (W)
17 × 17 ORIGEN library is to be used for the depletion analysis. The
burnup-credit criticality calculation uses a subset of the major
actinides as defined in the NUC= array. The sample problem contains a
“\ *read search*\ ” data block, which provides an upper limit for
subcriticality, *usl*, a tolerance value for the search algorithm,
*eps*, the lower and upper enrichment bounds, *ecl* and e\ *ch*,
respectively, the maximum number of iterations for each burnup value
requested, *imaxl*, average specific power in W/g, *power*, decay time
after irradiation in days, *dec*, number of libraries per cycle, *nlib*,
average burnup per cycle in GWd/MTU, *avgbu*, fractional downtime,
*fdt*, and a set of burnup values, *bu* array.

Sample problem 2
~~~~~~~~~~~~~~~~

Sample problem 2, listed in :numref:`list2-3-2`, illustrates a simple pin-cell
model using 18-axial-burnup-dependent zones. In this example, the
built-in axial profiles for three burnup ranges are applied using the
NAX= −18 option (see profiles in :numref:`tab2-3-5`). STARBUCS determines the
average assembly burnup from the power history data input, and
automatically selects the appropriate profile based on the discharge
assembly burnup. The axial-profile data were developed for a predefined
axial-zoning structure (i.e., fraction of the assembly height). It is
important that the KENO V.a geometry model therefore also reflect this
axial-zone structure. That is, the height of each axial zone in the
criticality model must conform to the axial zones for the profile
applied in the analysis. In this example, the total pin height is
365.7 cm (144 in.), which is subdivided into 18 equal-height segments of
20.32 cm each.

The burnup-dependent cross sections generated for the criticality
analysis have material identifiers ranging from 101 (bottom) to
118 (top). There is no constraint on how the fuel materials can be
applied in the KENO V.a model. For example, the order of the material
numbers could easily be reversed, which would effectively invert the
profile and could be used to simulate an assembly loaded upside down. It
is also not necessary to use all of the materials in the problem. For
instance, all fuel regions in the KENO V.a model could be assigned the
same fuel mixture number to represent a flat axial profile having a
burnup value equal to that of the particular mixture used. The average
assembly burnup would also be equal to that of the particular mixture
used, and not that defined by the power history data block.

.. code-block:: scale
  :name: list2-3-1
  :caption: STARBUCS input listing for sample problem 1

      =starbucs
     PWR 17x17 Fuel Assembly - uniform axial burnup rods
    v7-238
    read comp
    ' UO2 Fuel 2.0 wt% u-235
     uo2    1 den=10.96 0.95 293.0 92235 2.0 92238 98.0 end
    'Zircalloy
     zirc4  2  1  end
    'Water
     h2o    3  1  end
    'Gap
     n 4 den=0.00125 1 end
    end comp
    read celldata
     latticecell squarepitch  pitch=1.259 3 fueld=0.805 1 cladd=0.95 2 gapd=0.822 4 end
    end celldata
    ' Enter burnup credit control parameters
    read control
     arp=w17x17
     axp= 1 end
     nuc= u-234 u-235 u-236 u-238 pu-238 pu-239 pu-240
          pu-241 pu-242 am-241 am-242m am-243 np-237 end
     fle=all
    end control
    read search
      usl=0.96
      eps=0.002
      ecl=1.51
      ech=4.99
      itmax=10
      power=60.0
      dec=1826.25
      nlib=2
      avgbu=20
      fdt=0.2
      ffe=input
      bu= 10 50 70  end
    end search
    read kenova
    ' infinite pin cell lattice
    '
    '**************************************
    '* materials
    '* 101 = uo2, uniform axial region
    '* 2 = Zircaloy
    '* 3 = Water
    '* 4 = Gap
    '**************************************
    read param tme=10000 gen=510 nsk=10 npg=1000 end param
    read geom
    '           Fuel Pin
    global unit 1
     cylinder   101  1   0.4025  50.0  -50.0
     cylinder   4    1   0.4110  50.0  -50.0
     cylinder   2    1   0.4750  50.0  -50.0
     cuboid     3    1 4p0.6295  50.0  -50.0
    '
    end geom
    read bounds  all=reflect  end bounds
    end data
    end kenova
    end

.. code-block:: scale
  :name: list2-3-2
  :caption: STARBUCS input listing for sample problem 2

  =starbucs
   PWR 17x17 Fuel Assembly - 18-zone axial burnup profile
  v7-238
  read comp
  ' UO2 Fuel 2.0 wt% u-235
   uo2    1 den=10.96 0.95 293.0 92235 2.0 92238 98.0 end
  'Zircalloy
   zirc4  2  1  end
  'Water
   h2o    3  1  end
  'Gap
   n 4 den=0.00125 1 end
  end comp
  read celldata
   latticecell squarepitch  pitch=1.259 3 fueld=0.805 1 cladd=0.95 2 gapd=0.822 4 end
  end celldata
  ' Enter burnup credit control parameters
  read control
  arp=w17x17  nax=-18
  nuc= u-234 u-235 u-236 u-238 pu-238 pu-240
      pu-241 pu-242 am-241 am-242m am-243 np-237 end
  fle=o-16 h-1 end
  end control
  read hist
    power=35.001 burn=100 nlib=1 end
    power=28.5   burn=230 down=100 nlib=2 end
    power=24.001 burn=300 nlib=2 down=1826 end
  end hist
  read kenova
  '**************************************
  '* materials
  '* 101-118 = uo2, 18-axial zone model
  '* 2 = Zircaloy
  '* 3 = Water
  '* 4 = Gap
  '**************************************
  read param  tme=10000 gen=510 nsk=10 npg=1000 end param
  read geom
  '           Fuel Pin
  global unit 1
   cylinder   101  1  0.4025 -162.53  -182.85
   cylinder   102  1  0.4025 -142.22  -182.85
   cylinder   103  1  0.4025 -121.90  -182.85
   cylinder   104  1  0.4025 -101.58  -182.85
   cylinder   105  1  0.4025  -81.27  -182.85
   cylinder   106  1  0.4025  -60.95  -182.85
   cylinder   107  1  0.4025  -40.63  -182.85
   cylinder   108  1  0.4025  -20.32  -182.85
   cylinder   109  1  0.4025    0.00  -182.85
   cylinder   110  1  0.4025   20.32  -182.85
   cylinder   111  1  0.4025   40.63  -182.85
   cylinder   112  1  0.4025   60.95  -182.85
   cylinder   113  1  0.4025   81.27  -182.85
   cylinder   114  1  0.4025  101.58  -182.85
   cylinder   115  1  0.4025  121.90  -182.85
   cylinder   116  1  0.4025  142.22  -182.85
   cylinder   117  1  0.4025  162.53  -182.85
   cylinder   118  1  0.4025  182.85  -182.85
   cylinder   4    1  0.4110  182.85  -182.85
   cylinder   2    1  0.4750  182.85  -182.85
   cuboid     3    1 4p0.6295 182.85  -182.85
  '
  end geom
  read bounds  all=reflect  end bounds
  end data
  end kenova
  end

Sample problem 3
~~~~~~~~~~~~~~~~

Sample problem 3, listed in :numref:`list2-3-3`, performs a burnup-credit
criticality safety calculation using the SCALE 238-group ENDF/B-VII
cross section library (V7-238) for an array of Combustion Engineering
(CE) 14 × 14 spent fuel assemblies in water. A subset of burnup-credit
actinides and fission products are included in the criticality
calculation. A user-supplied 18-axial-region-burnup profile of the
assemblies is input. This profile was obtained from the
axial-burnup-profile database :cite:`cacciapouti_axial_2000` for Maine Yankee assembly N863. Note
that the axial profile will be normalized automatically by the code
using NPR=yes (default). The normalization is performed such that the
average value of the profile values is unity (i.e., the sum of the
profile values is equal to the number of axial zones). The 3.3 wt %
enriched UO\ :sub:`2` fuel is assumed to achieve a discharge burnup of
37,626 MWd/MTU in three cycles of approximately 12.5 GWd/MTU per cycle
and a downtime per cycle of 80 days, followed by a cooling time of
5 years after discharge (1826 days). An average assembly power level of
32 MW/MTU is used for the depletion calculation. Two libraries per cycle
are requested during the depletion. Note that by increasing the number
of libraries generated per cycle, the cross sections used in the burnup
analysis are updated more frequently to reflect the changes that occur
with burnup. The nominal CE 14 × 14 assembly design specifications were
obtained from :cite:`dehart_extension_1996`. The assembly pitch in the criticality
calculations is 22.78 cm. A cross section view of the assembly geometry,
a 2 × 8 array of water reflected assemblies, is illustrated in
:numref:`fig2-3-5`.

.. code-block:: scale
  :name: list2-3-3
  :caption: STARBUCS input listing for sample problem

    =starbucs
  CE 14x14 assembly 2 x 8 array
  V7-238
  read comp
  ' UO2 Fuel 3.3 wt% u235
  uo2  1 den=10.045 1 273 92234 0.0294 92235 3.3 92236 0.0152 92238 96.6554 end
  'Zircalloy
   zirc4 2  1  end
  'Water
   h2o    3  1  end
  end comp
  read celldata
   latticecell squarepitch  pitch=1.473 3 fueld=0.968 1
                            cladd=1.118 2  gapd=0.985 0  end
  end celldata
  read control
  arp=ce14x14 nax=18
  axp=
    0.67053 0.93322 1.02433 1.05329 1.06026 1.06185
    1.06215 1.06249 1.06312 1.06408 1.06541 1.06702
    1.06836 1.06760 1.05918 1.02515 0.92262 0.66935 end
  nuc=
    u-234  u-235  u-236  u-238  pu-238 pu-239 pu-240
    pu-241 pu-242 am-241 np-237
    mo-95  tc-99  ru-101 rh-103 ag-109 cs-133 nd-143
    nd-145 sm-147 sm-149 sm-150 sm-151 eu-151 sm-152
    eu-153 gd-155 end
  end control
  read hist
    power=32.00  burn=391.937 nlib=2 down=80  end
    power=32.00  burn=391.937 nlib=2 down=80  end
    power=32.00  burn=391.937 nlib=2 down=1826 end
  end hist
  read keno
  '
  '******************************************
  '* materials
  '* 101 = uo2, lower axial region (0.67053)
  '* 118 = uo2, upper axial region (0.66935)
  '* 2 = Zircaloy
  '* 3 = Water
  '******************************************
  read param
   tme=10000 gen=510 nsk=10 npg=1000
  end param
  read geom
  '  Fuel Pin
  unit           1
   cylinder   101  1  0.484 -162.53  -182.85
   cylinder   102  1  0.484 -142.22  -182.85
   cylinder   103  1  0.484 -121.90  -182.85
   cylinder   104  1  0.484 -101.58  -182.85
   cylinder   105  1  0.484  -81.27  -182.85
   cylinder   106  1  0.484  -60.95  -182.85
   cylinder   107  1  0.484  -40.63  -182.85
   cylinder   108  1  0.484  -20.32  -182.85
   cylinder   109  1  0.484    0.00  -182.85
   cylinder   110  1  0.484   20.32  -182.85
   cylinder   111  1  0.484   40.63  -182.85
   cylinder   112  1  0.484   60.95  -182.85
   cylinder   113  1  0.484   81.27  -182.85
   cylinder   114  1  0.484  101.58  -182.85
   cylinder   115  1  0.484  121.90  -182.85
   cylinder   116  1  0.484  142.22  -182.85
   cylinder   117  1  0.484  162.53  -182.85
   cylinder   118  1  0.484  182.85  -182.85
   cylinder   0    1  0.4925 182.85  -182.85
   cylinder   2    1  0.559  182.85  -182.85
   cuboid     3    1 4p0.7365 182.85  -182.85
  '
  '  2 x 2 Array of Fuel Pins
  unit           2
   array 1 3*0
  '
  '  Large Water Hole
  unit           3
   cylinder   3    1  1.3140  182.85  -182.85
   cylinder   2    1  1.4160  182.85  -182.85
   cuboid     3    1 4p1.473  182.85  -182.85
  '
  '  Assembly Unit
  unit           4
   array      2 -10.311 -10.3124 -182.85
   cuboid     3    1 4p11.390  182.85  -182.85
  '
  '  Assembly Array (2x8)
  global
  unit           5
   array      3  3*0
   reflector  3  1 6r30.0  1
  end geom
  read array
  ara=1  nux=2  nuy=2  nuz=1 fill
    1 1
    1 1  end fill
  ara=2  nux=7  nuy=7  nuz=1 fill
    2 2 2 2 2 2 2
    2 3 2 2 2 3 2
    2 2 2 2 2 2 2
    2 2 2 3 2 2 2
    2 2 2 2 2 2 2
    2 3 2 2 2 3 2
    2 2 2 2 2 2 2  end fill
  ara=3  nux=2  nuy=8  nuz=1 fill
    16r4  end fill
  end array
  read bounds  all=void  end bounds
  end data
  end keno
  end

.. _fig2-3-5:
.. figure:: figs/STARBUCS/fig5.png
  :align: center
  :width: 500

  Plot of the CE 14 × 14 assembly array geometry in sample problem 3.

Sample problem 4
~~~~~~~~~~~~~~~~

Sample problem 4, listed in :numref:`list2-3-4`, illustrates the application of
STARBUCS for a criticality safety analysis of a burnup-credit cask. The
cask geometry in this example is based on a 32-assembly generic
burnup-credit cask model and is illustrated in :numref:`fig2-3-6`.

The assemblies are assumed to be W 17 × 17 OFA assemblies with an
initial enrichment of 4.98 wt %. The standard composition description
for this problem includes the fuel assembly and all cask structural
material definitions. The analysis applies built-in 18-axial-zone
profiles, and actinide-only burnup credit (i.e., only a subset of
actinides and no fission products). The assembly is irradiated to an
average burnup of about 50 GWd/MTU. The axial-burnup profile is
automatically selected by the code based on the average assembly burnup.
Isotopic correction factors are applied to the calculated actinide
inventories. The correction factors were obtained from Ref. 4. An
axial-moderator density is also applied. Note that actual entries in the
MOD= array are not realistic for a PWR and are only intended to
illustrate the use of this feature. Since the ORIGEN library applied in
this calculation does not have variable moderator density, the values in
the MOD= array have no effect on the calculation. The criticality
evaluation of the cask is performed following a cooling time of
1826 days (5 years).

.. _fig2-3-6:
.. figure:: figs/STARBUCS/fig6.png
  :align: center
  :width: 500

  Cutaway view of the generic 32-assembly burnup-credit cask showing the cask bottom half with a quarter of the model removed.

.. code-block:: scale
  :name: list2-3-4
  :caption: STARBUCS input listing for sample problem 4

  =starbucs
   PWR 18-axial zone W17x17 assembly, GBC-32 assembly cask model
  v7-238
  read comp
  ' UO2 Fuel Rod 4.98 wt % u235
   uo2    1 den=10.96 0.95 293.0 92235 4.98 92238 95.02 end
  'Zircalloy
   zirc2  2  1  end
  'Water
   h2o    3  1  end
  'Stainless Steel
   ss304  4  1  end
  ' BORAL Center - B-10 loading of 0.0225 g/cm3
   b-10   5  0  6.5795E-03   293.0  end
   b-11   5  0  2.7260E-02   293.0  end
   c      5  0  8.4547E-03   293.0  end
   al     5  0  4.1795E-02   293.0  end
  'Stainless Steel
   ss304  6  1  end
  ' aluminum
   al     7  0  0.0602       293.0  end
  end comp
  read celldata
   latticecell squarepitch  pitch=1.2598 3 fueld=0.7844 1 cladd=0.9144 2 gapd=0.8001 0 end
  end celldata
  read control
   arp=w17x17_ofa nax=-18
   nuc= u-234 0.635
        u-235 1.085
        u-236 0.910
        u-238 0.992
       pu-238 0.856
       pu-239 1.076
       pu-240 0.945
       pu-241 1.087
       pu-242 0.848
       am-241 0.609
       am-243 0.804
       np-237 0.697 end
  mod= 0.720 0.709 0.699 0.688 0.678 0.667 0.657
       0.646 0.635 0.625 0.614 0.604 0.593 0.583
       0.572 0.562 0.551 0.540 end
  end control
  read hist
   power=32.89 burn=100 end
   power=32.89 burn=200 end
   power=32.89 burn=900 nlib=3 end
   power=32.89 burn=320 down=-1826 end
  end hist

  read kenova
  '**************************************
  '* Assembly Type: Westinghouse 17x17 OFA/V5
  '* Materials
  '* 101 - 118 = uo2, axial regions 1 through 18
  '* 2 = Zircaloy
  '* 3 = Water
  '* 4 = Stainless Steel
  '* 5 = Boral
  '* 6 = Stainless Steel
  '* 7 = Al

  '**************************************
  read param tme=10000 gen=510 nsk=10 npg=1000 end param

  read geom
  unit 1
  com='Fuel Pin'
   cylinder   101  1  0.3922 -162.53  -182.85
   cylinder   102  1  0.3922 -142.22  -182.85
   cylinder   103  1  0.3922 -121.90  -182.85
   cylinder   104  1  0.3922 -101.58  -182.85
   cylinder   105  1  0.3922  -81.27  -182.85
   cylinder   106  1  0.3922  -60.95  -182.85
   cylinder   107  1  0.3922  -40.63  -182.85
   cylinder   108  1  0.3922  -20.32  -182.85
   cylinder   109  1  0.3922    0.00  -182.85
   cylinder   110  1  0.3922   20.32  -182.85
   cylinder   111  1  0.3922   40.63  -182.85
   cylinder   112  1  0.3922   60.95  -182.85
   cylinder   113  1  0.3922   81.27  -182.85
   cylinder   114  1  0.3922  101.58  -182.85
   cylinder   115  1  0.3922  121.90  -182.85
   cylinder   116  1  0.3922  142.22  -182.85
   cylinder   117  1  0.3922  162.53  -182.85
   cylinder   118  1  0.3922  182.85  -182.85
   cylinder   0    1  0.40005  182.85  -182.85
   cylinder   2    1  0.4572  182.85  -182.85
   cuboid     3    1  2p0.6299  2p0.6299  182.88  -182.88

  unit 2
  com='Guide Thimble/Instrument Tube'
   cylinder 3 1 0.56135  365.76  0
   cylinder 2 1 0.602    365.76  0
   cuboid   3 1  0.6299  -0.6299  0.6299  -0.6299  365.76  0

  unit 4
  com='Top Half Horizontal Boral Panel'
  cuboid          7  1  9.5250   -9.5250     0.02540   0.0       365.76   0.
  cuboid          5  1  9.5250   -9.5250     0.12827   0.0       365.76   0.
  cuboid          3  1  11.75   -11.75       0.12827   0         365.76   0

  unit 5
  com='Right-Hand Side Half Vertical Boral Panel'
  cuboid          7  1  0.02540   0.0       9.5250   -9.5250     365.76   0.
  cuboid          5  1  0.128270  0.0       9.5250   -9.5250     365.76   0.
  cuboid          3  1  0.12827    0       11.75    -11.75       365.76   0

  unit 6
  com='Bottom Half Horizontal Boral Panel'
  cuboid          7  1  9.5250   -9.5250     0.0     -0.0254      365.76   0.
  cuboid          5  1  9.5250   -9.5250     0.0     -0.12827     365.76   0.
  cuboid          3  1  11.75   -11.75       0.0     -0.12827     365.76   0

  unit 7
  com='Left-Hand Side Half Vertical Boral Panel'
  cuboid          7  1   0.0     -0.0254     9.5250   -9.5250     365.76   0.
  cuboid          5  1   0.0     -0.12827    9.5250   -9.5250     365.76   0.
  cuboid          3  1   0.0     -0.12827   11.75    -11.75       365.76   0

  unit 8
  com='Empty Corner (Water)'
  cuboid          3  1   0.12827   0       0.12827      0         365.76  0

  unit 10
  com='Top Boral/Basket Plate with water added to fit array dimensions'
  cuboid          5  1   9.525    -9.525     -0.7754  -0.87827    365.76  0
  cuboid          7  1   9.525    -9.525     -0.75    -0.87827    365.76  0
  cuboid          3  1  11.7500  -11.75      -0.75    -0.87827    365.76  0.
  cuboid          4  1  11.7500  -11.75       0.0     -0.87827    365.76  0.
  cuboid          3  1  11.87827 -11.87827    0.12827 -0.87827    365.76  0

  unit 11
  com='Bottom Boral/Basket Plate with water added to fit array dimensions'
  cuboid          5  1   9.525    -9.525     0.87827   0.7754     365.76  0
  cuboid          7  1   9.525    -9.525     0.87827   0.75       365.76  0
  cuboid          3  1  11.7500  -11.75      0.87827   0.75       365.76  0.
  cuboid          4  1  11.7500  -11.75      0.87827   0.0        365.76  0.
  cuboid          3  1  11.87827 -11.87827   0.87827  -0.12827    365.76  0

  unit 12
  com='Left-Hand Side Boral/Basket Plate with water added to fit array dimensions'
  cuboid          5  1   0.87827   0.7754     9.525    -9.525     365.76  0
  cuboid          7  1   0.87827   0.75       9.525    -9.525     365.76  0
  cuboid          3  1   0.87827   0.75      11.75    -11.75      365.76  0.
  cuboid          4  1   0.87827   0.0       11.75    -11.75      365.76  0.
  cuboid          3  1   0.87827  -0.12827   11.87827 -11.87827   365.76  0.

  unit 13
  com='Right-Hand Side Boral/Basket Plate with water added to fit array dimensions'
  cuboid          5  1  -0.7754   -0.87827     9.525    -9.525    365.76  0
  cuboid          7  1  -0.75     -0.87827     9.525    -9.525    365.76  0
  cuboid          3  1  -0.75     -0.87827    11.75    -11.75     365.76  0.
  cuboid          4  1   0.0      -0.87827    11.75    -11.75     365.76  0.
  cuboid          3  1   0.12827  -0.87827    11.87827 -11.87827  365.76  0

  unit 20
  com='Top Boral/Basket Plate'
  cuboid          5  1   9.525    -9.525     -0.7754  -0.87827    365.76  0
  cuboid          7  1   9.525    -9.525     -0.75    -0.87827    365.76  0
  cuboid          3  1  11.7500  -11.75      -0.75    -0.87827    365.76  0.
  cuboid          4  1  11.7500  -11.75       0.0     -0.87827    365.76  0.

  unit 21
  com='Bottom Boral/Basket Plate'
  cuboid          5  1   9.525    -9.525     0.87827   0.7754     365.76  0
  cuboid          7  1   9.525    -9.525     0.87827   0.75       365.76  0
  cuboid          3  1  11.7500  -11.75      0.87827   0.75       365.76  0.
  cuboid          4  1  11.7500  -11.75      0.87827   0.0        365.76  0.

  unit 22
  com='Left-Hand Side Boral/Basket Plate'
  cuboid          5  1   0.87827   0.7754     9.525    -9.525     365.76  0
  cuboid          7  1   0.87827   0.75       9.525    -9.525     365.76  0
  cuboid          3  1   0.87827   0.75      10.9999  -10.9999    365.76  0.
  cuboid          4  1   0.87827   0.0       10.9999  -10.9999    365.76  0.

  unit 23
  com='Right-Hand Side Boral/Basket Plate'
  cuboid          5  1  -0.7754   -0.87827     9.525    -9.525    365.76  0
  cuboid          7  1  -0.75     -0.87827     9.525    -9.525    365.76  0
  cuboid          3  1  -0.75     -0.87827    10.9999  -10.9999   365.76  0.
  cuboid          4  1   0.0      -0.87827    10.9999  -10.9999   365.76  0.


  unit 100
  com='17x17 Fuel Assembly in Basket'
   array 1 -10.7083  -10.7083  0
   cuboid 3 1  11  -11  11  -11  365.76  0
   cuboid 0 1  11  -11  11  -11  365.76  0
   cuboid 4 1  11.75  -11.75  11.75  -11.75  365.76  0

  unit 101
  com='17x17 Fuel Assembly in Basket with Half Boral Panels'
    array 2 0  0  0

  unit 112
  com='Top Row of Fuel Assemblies'
    array 12  -47.51308  -12.38154   0
  unit 113
  com='Left Row of Fuel Assemblies'
    array 13  -12.38154   -47.51308  0

  unit 114
  com='Bottom Row of Fuel Assemblies'
    array 14  -47.51308  -12.38154   0

  unit 115
  com='Right Row of Fuel Assemblies'
    array 15  -12.38154  -47.51308   0

  global unit 200
  com='Cask with 32 Fuel Assemblies'
    array 3  -47.51308   -47.51308   0
    cylinder 3 1 87.5  395.76  -30
    hole 112   0       59.89463  0
    hole 114   0      -59.89463  0
    hole 113 -59.89463  0        0
    hole 115  59.89463  0        0
    hole  20  59.39136   48.39136 0
    hole  20 -59.39136   48.39136 0
    hole  21  59.39136  -48.39136 0
    hole  21 -59.39136  -48.39136 0
    hole  22 -48.39136   59.39136 0
    hole  22 -48.39136  -59.39136 0
    hole  23  48.39136   59.39136 0
    hole  23  48.39136  -59.39136 0
    cylinder 6 1 107.5  425.76  -60
    cuboid 0 1  108  -108  108  -108  425.76  -60
  end geom

  read array
  ara=1 nux=17 nuy=17 nuz=1
  fill 39*1 2 2*1 2 2*1 2 8*1 2 9*1 2 22*1 2 2*1 2 2*1 2 2*1 2 2*1 2 38*1 2 2*1 2
   2*1 2 2*1 2 2*1 2 38*1 2 2*1 2 2*1 2 2*1 2 2*1 2 22*1 2 9*1 2 8*1 2 2*1 2 2*1
   2 39*1
  end fill
  ara=2 nux=3 nuy=3 nuz=1
  fill 8  4  8
       5 100 7
       8  6  8
  end fill
  ara=3 nux=4 nuy=4 nuz=1
  fill f101 end fill
  ara=12 nux=4 nuy=2 nuz=1
  fill 101 101 101 101
        10  10  10  10
  end fill
  ara=13 nux=2 nuy=4 nuz=1
  fill 12 101
       12 101
       12 101
       12 101
  end fill
  ara=14 nux=4 nuy=2 nuz=1
  fill  11  11  11  11
       101 101 101 101
  end fill
  ara=15 nux=2 nuy=4 nuz=1
  fill 101 13
       101 13
       101 13
       101 13
  end fill
  end array
  read plot
   ttl='2-d cross section of gbc-32 cask'
   xul=-90  yul=90  zul=100
   xlr=90  ylr=-90  zlr=100
   nax=800
   uax=1 vdn=-1 end
  end plot
  read bounds  xyf=mirror   end bounds
  end data
  end kenova
  end

Sample problem 5
~~~~~~~~~~~~~~~~

Sample problem 5, listed in :numref:`list2-3-5`, uses the CE 14 × 14 assembly
design from problem 3, and performs a burnup-credit calculation using
the horizontal burnup-profile option. The assembly configuration is
taken to be a simple 2 × 2 assembly array with water reflection. This
problem is only designed to illustrate the basic features of the
horizontal profile option. In this example, it is assumed that there is
a burnup gradient across the assemblies, such that half the fuel pins
have a burnup exceeding the average assembly burnup by 10% and half the
pins have a burnup of 10% less than the average, with the two burnup
regions separated by the assembly diagonal. The input card required to
simulate the two horizontal burnup regions in an assembly is

::

  hzp= 0.9 1.1 end

STARBUCS applies these factors to calculate compositions for each of the
horizontally-varying burnup regions in each zone of the problem. It is
important to note that the option inherently assumes that there is an
equal volume/mass of fuel in each of the horizontal (or axial) zones
since the code weights all regions equally when determining the average
assembly burnup. To illustrate this, consider modeling an assembly with
**only one quadrant** having a burnup that is 10% higher than the other
three quadrants. The user would enter data for each of the four
horizontal assembly quadrants or zones, e.g.,

::

  hzp= 0.9766 0.9766 0.9766 1.0700 end

such that the average of the HZP array entries is unity. This ensures
that the average assembly burnup will be that specified in the power
history data block. Note that this array is automatically normalized if
NPR=yes (default). However, the user could substantially reduce the
computational time involved by specifying only two fuel regions, e.g.,

::

  hzp= 0.9766 1.0700 end

and turning off the normalization option (e.g., NPR=no). The
normalization option must be turned off to prevent the profile from
being altered (since the sum is not equal to 2). This allows the user to
account for the fact that, in this scenario, there are three quadrants
having a lower burnup (and consequently three times the mass) and just
one quadrant having an elevated burnup compared to the average. However,
it is the responsibility of the user to ensure that the profiles and the
KENO V.a problem description produce the desired average burnup.

In this sample problem the four assemblies are aligned so the lower
burnup regions of the assemblies are adjacent to one another to maximize
the system reactivity. The assembly geometry showing the different
burnup regions of the assemblies is illustrated in :numref:`fig2-3-7`. The
criticality calculation is performed using the SCALE ENDF/B-VII
continuous cross section library (CE_V7).

Following the STARBUCS calculation, the KENO V.a geometry model could be
readily altered to simulate other assembly configurations (e.g., shuffle
the fuel assembly locations). The CSAS5 case could subsequently be
executed as a standalone case since all of the material compositions
have already been created during the initial STARBUCS run. This
facilitates the rapid evaluation of different fuel configurations
without the need to regenerate the material compositions using STARBUCS.

.. code-block:: scale
  :name: list2-3-5
  :caption: STARBUCS input listing for sample problem 5

  =starbucs
  CE 14x14 assembly 4x4 array - horizontal burnup gradient
  ce_v7
  read comp
  ' UO2 Fuel Rod 3.038 wt %
  uo2  1 den=10.045  1  273
     92234 0.027 92235 3.038 92236 0.014 92238 96.921   end
  'Zircalloy
  arbmzirc 6.44 4 0 0 1 40000 97.91 26000 0.5 50116 0.86 50120 0.73 2 1 620  end
  'Water
   h2o    3  1  end
  end comp
  read celldata
   latticecell squarepitch  pitch=1.473 3 fueld=0.968 1 cladd=1.118 2  gapd=0.985 0  end
   end
  end celldata
  read control
  arp=ce14x14
  nax=18
  axp=
    0.67053 0.93322 1.02433 1.05329 1.06026 1.06185
    1.06215 1.06249 1.06312 1.06408 1.06541 1.06702
    1.06836 1.06760 1.05918 1.02515 0.92262 0.66935 end
  nhz= 2
  hzp= 0.9 1.1  end
  nuc=
    u-234  u-235  u-236  u-238  pu-238 pu-239 pu-240
    pu-241 pu-242 am-241 am-242m am-243 np-237 end
  end control
  read hist
    power=28.00  burn=520.833 nlib=2 down=80  end
    power=28.00  burn=520.833 nlib=2 down=80  end
    power=28.00  burn=520.833 nlib=2 down=-1865 end
  end hist
  read kenova
  '*************************************************************
  '* materials
  '* 101 = uo2, lower axial region, low burnup region
  '* 118 = uo2, upper axial region, low burnup region
  '* 201 = uo2, lower axial region, high burnup region
  '* 218 = uo2, upper axial region, high burnup region
  '* 2 = Zircaloy
  '* 3 = Water
  '*************************************************************
  read param
  tme=10000 gen=510 nsk=10 npg=1000
  end parm
  read geom
  '  Fuel Pin, Low Burnup Region
  unit           1
   cylinder   101  1  0.484 -162.53  -182.85
   cylinder   102  1  0.484 -142.22  -182.85
   cylinder   103  1  0.484 -121.90  -182.85
   cylinder   104  1  0.484 -101.58  -182.85
   cylinder   105  1  0.484  -81.27  -182.85
   cylinder   106  1  0.484  -60.95  -182.85
   cylinder   107  1  0.484  -40.63  -182.85
   cylinder   108  1  0.484  -20.32  -182.85
   cylinder   109  1  0.484    0.00  -182.85
   cylinder   110  1  0.484   20.32  -182.85
   cylinder   111  1  0.484   40.63  -182.85
   cylinder   112  1  0.484   60.95  -182.85
   cylinder   113  1  0.484   81.27  -182.85
   cylinder   114  1  0.484  101.58  -182.85
   cylinder   115  1  0.484  121.90  -182.85
   cylinder   116  1  0.484  142.22  -182.85
   cylinder   117  1  0.484  162.53  -182.85
   cylinder   118  1  0.484  182.85  -182.85
   cylinder   0    1  0.4925 182.85  -182.85
   cylinder   2    1  0.559  182.85  -182.85
   cuboid     3    1 4p0.7365 182.85  -182.85
  '
  '  Fuel Pin, High Burnup Region
  unit           2
   cylinder   201  1  0.484 -162.53  -182.85
   cylinder   202  1  0.484 -142.22  -182.85
   cylinder   203  1  0.484 -121.90  -182.85
   cylinder   204  1  0.484 -101.58  -182.85
   cylinder   205  1  0.484  -81.27  -182.85
   cylinder   206  1  0.484  -60.95  -182.85
   cylinder   207  1  0.484  -40.63  -182.85
   cylinder   208  1  0.484  -20.32  -182.85
   cylinder   209  1  0.484    0.00  -182.85
   cylinder   210  1  0.484   20.32  -182.85
   cylinder   211  1  0.484   40.63  -182.85
   cylinder   212  1  0.484   60.95  -182.85
   cylinder   213  1  0.484   81.27  -182.85
   cylinder   214  1  0.484  101.58  -182.85
   cylinder   215  1  0.484  121.90  -182.85
   cylinder   216  1  0.484  142.22  -182.85
   cylinder   217  1  0.484  162.53  -182.85
   cylinder   218  1  0.484  182.85  -182.85
   cylinder   0    1  0.4925 182.85  -182.85
   cylinder   2    1  0.559  182.85  -182.85
   cuboid     3    1 4p0.7365 182.85  -182.85
  '
  '  2 x 2 Array of Lower Burnup Fuel Pins
  unit           3
   array 1 3*0
  '
  '  2 x 2 Array of Higher Burnup Fuel Pins
  unit           4
   array 2 3*0
  '
  '  Large Water Hole
  unit           5
   cylinder   3    1  1.3140  182.85  -182.85
   cylinder   2    1  1.4160  182.85  -182.85
   cuboid     3    1 4p1.473  182.85  -182.85
  '
  '  Assembly 1 Unit
  unit           6
   array      3 -10.311 -10.311 -182.85
   cuboid     3    1 4p11.390  182.85  -182.85
  '
  '  Assembly 2 Unit
  unit           7
   array      4 -10.311 -10.311 -182.85
   cuboid     3    1 4p11.390  182.85  -182.85
  '
  '  Assembly 3 Unit
  unit           8
   array      5 -10.311 -10.311 -182.85
   cuboid     3    1 4p11.390  182.85  -182.85
  '
  '  Assembly 4 Unit
  unit           9
   array      6 -10.311 -10.311 -182.85
   cuboid     3    1 4p11.390  182.85  -182.85
  '
  '  Assembly Array (2 x 2)
  global
  unit           10
   array      7  3*0
   reflector  3  1 6r30.0  1
  end geom
  read array
  ara=1  nux=2  nuy=2  nuz=1 fill
    1 1
    1 1  end fill
  ara=2  nux=2  nuy=2  nuz=1 fill
    2 2
    2 2  end fill
  ara=3  nux=7  nuy=7  nuz=1 fill
    3 3 3 3 3 3 3
    3 5 3 3 3 5 4
    3 3 3 3 4 4 4
    3 3 3 5 4 4 4
    3 3 3 4 4 4 4
    3 5 4 4 4 5 4
    4 4 4 4 4 4 4  end fill
  ara=4  nux=7  nuy=7  nuz=1 fill
    3 3 3 3 3 3 3
    4 5 3 3 3 5 3
    4 4 4 3 3 3 3
    4 4 4 5 3 3 3
    4 4 4 4 3 3 3
    4 5 4 4 4 5 3
    4 4 4 4 4 4 4  end fill
  ara=5  nux=7  nuy=7  nuz=1 fill
    4 4 4 4 4 4 3
    4 5 4 4 4 5 3
    4 4 4 4 4 3 3
    4 4 4 5 3 3 3
    4 4 3 3 3 3 3
    4 5 3 3 3 5 3
    4 3 3 3 3 3 3  end fill
  ara=6  nux=7  nuy=7  nuz=1 fill
    3 4 4 4 4 4 4
    3 5 4 4 4 5 4
    3 3 4 4 4 4 4
    3 3 3 5 4 4 4
    3 3 3 3 3 4 4
    3 5 3 3 3 5 4
    3 3 3 3 3 3 4  end   fill
  '
  ara=7  nux=2  nuy=2  nuz=1 fill
    8 9
    7 6  end fill
  end array
  read bounds  all=void  end bounds
  end data
  end kenova
  end

.. _fig2-3-7:
.. figure:: figs/STARBUCS/fig7.png
  :align: center
  :width: 600

  Plot of the 2 x 2 array of CE 14  14 assemblies with burnup gradient.

Sample problem 6
~~~~~~~~~~~~~~~~

The last sample problem uses KENO-VI to model a hexagonal VVER-440 fuel
assembly. In this example the axial burnup profile is simulated using
five axial regions of non-uniform volume (height). In this case the
profile input in the AXP= array is not normalized by the code (i.e.,
NPR=NO). The criticality calculation is performed using actinide credit
only. The input file is listed in :numref:`list2-3-6` and is the geometry is
illustrated in :numref:`fig2-3-8`.

.. code-block:: scale
  :name: list2-3-6
  :caption: STARBUCS input listing for sample problem 6

  =starbucs
  VVER assembly array
  V7-238
  read comp
  'UO2 Fuel
   uo2     1 den=8.7922 1.0 293 92235 3.3  92238 96.7 end
  'Cladding
    zr  2 den=6.4073 1.0  293  end
  'Moderator
   h2o   3 den=0.71533 0.9994 293 end
   boron   3 den=0.71533 0.0006 293 end
  end comp
  '
  read celldata
   latticecell triangpitch pitch=1.22 3 fueld=0.772 1 cladd=0.91 2 end
  end celldata
  '
  read control
   arp=vver440(3.6)  npr=no
   axp= 0.652 0.967 1.084 0.738 0.462 end
   nuc= u-234 u-235 u-236 u-238 pu-238 pu-239 pu-240
        pu-241 pu-242 am-241 am-243 np-237 end
  end control
  read hist
    power=35.00  burn=1428.6 down=1826 nlib=4 end
  end hist
  read keno6
  read param gen=110 npg=1000 nsk=10 end param
  read geom
  unit  2
  com='Vacant(water filled) hex'
   hexprism 10 0.610 257.0 0.0
   media 3 1 10
   boundary 10
  unit   4
  com='UO2 Fuel Rod'
   cylinder 11 0.386  14.28 0.0
   cylinder 12 0.386  28.56 0.0
   cylinder 13 0.386 228.44 0.0
   cylinder 14 0.386 242.72 0.0
   cylinder 15 0.386 257.00 0.0
   cylinder 20 0.455 257.00  0.0
   hexprism 30 0.610  257.00  0.0
   media 101 1 11
   media 102 1 12 -11
   media 103 1 13 -12
   media 104 1 14 -13
   media 105 1 15 -14
   media 2   1 20 -15
   media 3   1 30 -20
   boundary 30
  unit  5
  com='UO2 Fuel assembly'
   hexprism 10 11.800 257.0 0.0  rotate a1=-30
   array 1 10 place 12 12 1 3*0.0
   boundary 10
  global unit 1
  com='UO2 assembly'
   cuboid 10  4p15.0  257.0 0.0
  hole 5 rotate a1=30
   media 3  1 10
   boundary 10
  end geom
  read array
   com='Assembly hexagonal rod array'
   ara=1 typ=hexagonal nux=23 nuy=23 nuz=1
  fill
  2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
  2 2 2 2 2 2 2 2 2 2 2 4 4 4 4 4 4 4 4 4 4 4 2
  2 2 2 2 2 2 2 2 2 2 4 4 4 4 4 4 4 4 4 4 4 4 2
  2 2 2 2 2 2 2 2 2 4 4 4 4 4 4 4 4 4 4 4 4 4 2
  2 2 2 2 2 2 2 2 4 4 4 4 4 4 4 4 4 4 4 4 4 4 2
  2 2 2 2 2 2 2 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 2
  2 2 2 2 2 2 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 2
  2 2 2 2 2 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 2
  2 2 2 2 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 2
  2 2 2 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 2
  2 2 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 2
  2 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 2
  2 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 2 2
  2 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 2 2 2
  2 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 2 2 2 2
  2 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 2 2 2 2 2
  2 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 2 2 2 2 2 2
  2 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 2 2 2 2 2 2 2
  2 4 4 4 4 4 4 4 4 4 4 4 4 4 4 2 2 2 2 2 2 2 2
  2 4 4 4 4 4 4 4 4 4 4 4 4 4 2 2 2 2 2 2 2 2 2
  2 4 4 4 4 4 4 4 4 4 4 4 4 2 2 2 2 2 2 2 2 2 2
  2 4 4 4 4 4 4 4 4 4 4 4 2 2 2 2 2 2 2 2 2 2 2
  2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
  end fill
  end array
  read bounds  xyf=reflect zfc=water end bounds
  end data
  end keno6
  end

.. _fig2-3-8:
.. figure:: figs/STARBUCS/fig8.png
  :align: center
  :width: 500

  Cutaway 3-D view of the hexagonal VVER assembly model with water hidden.






.. bibliography:: bibs/STARBUCS.bib
