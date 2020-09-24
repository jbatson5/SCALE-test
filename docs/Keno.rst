.. _Keno:

Keno: A Monte Carlo Criticality Program
=======================================

*L. M. Petrie, K. B. Bekar, C. Celik, D. F. Hollenbach*,\ :sup:`1` *C. M.*
*Perfetti, S. Goluoglu,*\ :sup:`1` *N. F. Landers,*\ :sup:`1` *M. E. Dunn, B.*
*T. Rearden*

KENO is a three-dimensional (3D) Monte Carlo criticality transport
program developed and maintained for use as part of the SCALE Code
System. It can be used as part of a sequence or as a standalone program.
There are two versions of the code currently supported in SCALE.
KENO V.a is the older of the two. KENO-VI contains all current KENO V.a
features plus a more flexible geometry package known as the SCALE
Generalized Geometry Package. The geometry package in KENO-VI is capable
of modeling any volume that can be constructed using quadratic
equations. In addition, such features as geometry intersections, body
rotations, hexagonal and dodecahedral arrays, and array boundaries have
been included to make the code more flexible.

The simpler geometry features supported by KENO V.a allow for
significantly shorter execution times than KENO-VI, while the additional
geometry features supported in KENO-VI make the code appropriate for
cases where geometry modeling is not possible with KENO V.a. In
particular, KENO-VI allows intersections, body truncations with planes,
and a much wider variety of geometrical bodies. KENO-VI also has the
ability to rotate bodies so that volumes no longer must be positioned
parallel to a major axis. Hexagonal arrays are available in KENO-VI and
dohecahedral arrays enable the code to model pebble bed reactors and
other systems composed of close packed spheres. The use of array
boundaries makes it possible to fill a non-cuboidal volume with an
array, specifying the boundary where a particle leaves and enters the
array.

Except for geometry capabilities, the two versions of KENO share most of
the computational capabilities and the input flexibility specific to
most SCALE modules. They can both operate in multigroup or continuous
energy mode, run as standalone codes, or integrated in computational
sequences such as CSAS, TSUNAMI-3D, or TRITON. Both versions of the code
are continually updated and are written in FORTRAN 90.

Computational capabilities shared by the two versions of KENO include
the determination of k‑effective, neutron lifetime, generation time,
energy-dependent leakages, energy- and region-dependent absorptions,
fissions, the system mean-free-path, the region-dependent
mean-free-path, average neutron energy, flux densities, fission
densities, reaction rate tallies, mesh tallies, source convergence
diagnostics, problem-dependent continuous energy temperature treatments,
parallel calculations, restart capabilities, and many more.

:sup:`1`\ Formerly with Oak Ridge National Laboratory

ACKNOWLEDGMENTS

Many individuals have contributed significantly to the development of
KENO. Special recognition is given to G. E. Whitesides, former Director
of the Computing Applications Division, who was responsible for the
concept and development of the original KENO code. He has also
contributed significantly to some of the techniques used in both KENO
versions. The late J. T. Thomas offered many ideas that have been
implemented in the code. R. M. Westfall, retired from ORNL, provided
early consultation, encouragement, and benchmarks for validating the
code. The special abilities of J. R. Knight, retired from ORNL,
contributed substantially to debugging early versions of the code. S. W.
D. Hart was instrumental in implementing continuous energy temperature
treatments. W. J. Marshall has provided substantial validation and
quality assurance reviews. Appreciation is expressed to C. V. Parks and
S. M. Bowman for their support of KENO and the KENO3D visualization
tool. The late P. B. Fox provided many of the figures in this document.
D. Ilas, B. J. Marshall, and D. E. Mueller consolidated the previous
KENO V.a and KENO-VI manuals into this present form. The efforts of
L. F. Norris (retired), W. C. Carter (retired), S. J. Poarch, D. J.
Weaver (retired), S. Y. Walker and R. B. Raney in preparing this
document are gratefully acknowledged.

The authors thank the U. S. Nuclear Regulatory Commission and the DOE
Nuclear Criticality Safety Program for sponsorship of the continuous
energy, source convergence diagnostics, and grid geometry features in
the current version.

Introduction to KENO
--------------------

KENO, a functional module in the SCALE system, is a Monte Carlo
criticality program used to calculate :math:`k_{eff}`, fluxes, reaction rates,
and other data for three-dimensional (3-D) systems. Special features
include multigroup or continuous energy mode, simplified data input, the
ability to specify origins for spherical and cylindrical geometry
regions, a P\ :sub:`n` scattering treatment, and restart capability.

The KENO data input features flexibility in the order of input. The only
restrictions are that the sequence identifier, title, and cross section
library must be entered first. A large portion of the data has been
assigned default values found to be adequate for many
problems. This feature enables the user to run a problem with a minimum
of input data.

In addition to the features listed above, KENO-VI uses the SCALE
Generalized Geometry Package (SGGP), which contains a much larger set of
geometrical bodies, including cuboids, cylinders, spheres, cones,
dodecahedrons, elliptical cylinders, ellipsoids, hoppers,
parallelepipeds, planes, rhomboids, and wedges. The code’s flexibility
is increased by allowing: intersecting geometry regions; hexagonal,
dodecahedral, and cuboidal arrays; bodies and holes rotated to any angle
and translated to any position; and a specified array boundary that
contains only that portion of the array located inside the boundary.
Users should be aware that the added geometry features in KENO‑VI can
result in significantly longer run times than KENO V.a. A KENO-VI
problem that can be modeled in KENO V.a will typically run about four
times as long with KENO-VI as it does with KENO V.a. Therefore KENO-VI
is not a replacement for KENO V.a, but rather an additional version for
more complex geometries that could not be modeled previously.

Blocks of input data are entered in the form

**READ XXXX** *input_data* **END XXXX,**

where **XXXX** is the keyword for the type of data being entered. The
types of data entered include parameters, geometry region data, array
definition data, biasing or weighting data, albedo boundary conditions,
starting distribution information, the cross section mixing table, extra
one-dimensional (1-D) (reaction rate) cross section IDs for special
applications, energy group boundaries for tallying in the continuous
energy mode, a mesh grid for collecting flux moments, and printer plot
information.

A block of data can be omitted unless it is needed or desired for the
problem. Within the blocks of data, most of the input is activated by
using keywords to override default values.

The treatment of the energy variable can be either multigroup or
continuous. Changing the calculation mode from multigroup to continuous
energy or vice versa is established by simply changing the cross section
library used. All available calculated entities in the multigroup mode
can also be calculated in the continuous energy mode. If the calculated
entity is energy or group dependent, it is automatically tallied into
the appropriate group structure in the continuous energy mode.

The KENO V.a geometry input consists of spheres, hemispheres, cylinders,
hemicylinders, and cuboids. Although the origin of the cylinders,
hemicylinders, spheres, and hemispheres is zero by default, they may be
specified to any value that will allow the geometry to fit in the
problem. This feature allows the use of nonconcentric cylindrical and
spherical shapes and provides a great deal of freedom in positioning
them. Another feature that expands the generality of the code is the
ability to place the cut surface of the hemicylinders and hemispheres at
any distance between the radius and the origin.

An additional convenience is the availability of an alternative method
for specifying the array definition unit-location data. This method uses
FIDO-like options for filling the array.

As mentioned above, KENO-VI uses the SGGP, which contains a much more
flexible geometry package than the one in KENO V.a. In KENO-VI, geometry
regions are constructed and processed as sets of quadratic equations. A
set of geometric shapes (including all of those used in KENO V.a plus
others) is available in KENO-VI, as well as the ability to build more
complex geometric shapes using sets of quadratic equations. Unlike
KENO V.a, KENO-VI allows intersections between geometry regions within a
unit, and it provides the ability to specify an array boundary that
intersects the array.

The most flexible KENO V.a geometry features are the
“\ **ARRAY**-of-**ARRAY**\ s” and “\ **HOLE**\ s” capabilities. The
**ARRAY**-of-**ARRAY**\ s option allows the construction of **ARRAY**\ s
from other **ARRAY**\ s. The depth of nesting is limited only by
computer space restrictions. This option greatly simplifies the setup
for **ARRAY**\ s involving different **UNIT**\ s at different spacings.
The **HOLE** option allows a **UNIT** or an **ARRAY** to be placed at
any desired location within a geometry region. The emplaced **UNIT** or
**ARRAY** cannot intersect any geometry region and must be wholly
contained within a region. As many **HOLE**\ s as will snugly fit
without intersecting can be placed in a region. This option is
especially useful for describing shipping casks and reflectors that have
gaps or other geometrical features. Any number of **HOLE**\ s can be
described in a problem, and **HOLE**\ s can be nested to any depth.

The primary difference between the KENO V.a and KENO-VI geometry input
is the methodology used to represent the geometry/material regions in a
unit. KENO-VI uses two geometry records (cards) to describe a region.
The first record, called the GEOMETRY record, contains the geometry
(**shape**) keyword, region boundary definitions, and any geometry
modification data. Using geometry modification data, regions can be
rotated and translated to any angle and position within a unit. The
second record, the **CONTENT** record, contains the **MEDIA** keyword;
the material, **HOLE**, or **ARRAY** ID number; the bias ID number; and
the region definition vector. KENO-VI requires that a **GLOBAL UNIT** be
specified in all problems, including single unit problems.

In addition to the *cuboidal* **ARRAY**\ s available in KENO V.a,
*hexagonal* **ARRAY**\ s and *dodecahedral* **ARRAY**\ s can be directly
constructed in KENO-VI. Also, the ability to specify an **ARRAY**
boundary that intersects the **ARRAY** makes it possible to construct a
lattice in a cylinder using one **ARRAY** in KENO-VI instead of multiple
**ARRAY**\ s and **HOLE**\ s as would be required in KENO V.a.

Anisotropic scattering is treated by using discrete scattering angles.
The angles and associated probabilities are generated in a manner that
preserves the moments of the angular scattering distribution for the
selected group-to-group transfer. These moments can be derived from the
coefficients of a P\ :sub:`n` Legendre polynomial expansion. All moments
through the 2n − 1 moment are preserved for n discrete scattering
angles. A one-to-one correspondence exists such that n Legendre
coefficients yield n moments. The cases of zero and one scattering angle
are treated in a special manner. Even when the user specifies multiple
scattering angles, KENO can recognize that the distribution is
isotropic, and therefore KENO selects from a continuous isotropic
distribution. If the user specifies one scattering angle, the code
selects the scattering angle from a linear function if it is positive
between -1 and +1, and otherwise it performs semicontinuous scattering
by picking scattering angle cosines uniformly over some range between –1
and +1. The probability is zero over the rest of the range.

The KENO restart option is easy to activate. Certain changes can be made
when a problem is restarted, including using a different random sequence
or turning off certain print options such as fluxes or the fissions and
absorptions by region.

KENO can also compute angular fluxes and flux moments in multigroup
calculations, which are required to compute scattering terms for
generation of sensitivity coefficients with the SAMS module or the
TSUNAMI-3D control module. Fluxes can also be accumulated in a Cartesian
mesh that is superimposed over the user-defined geometry in an automated
manner.

KENO can perform Monte Carlo transport calculations concurrently on a
number of computational nodes. By introducing a simple master-slave
approach via MPI, KENO runs different random walks concurrently on the
replicated geometry within the same generation. Fission source and other
tallied quantities are gathered at the end of each generation by the
master process and are then processed either for final edits or
subsequent generations. Code parallel performance is strongly dependent
on the size of the problem simulated and the size of the tallied
quantities.

KENO Data Guide
---------------

KENO may be run stand alone or as part of a SCALE criticality safety or
sensitivity and uncertainty analysis sequence. If KENO is run stand
alone in the multigroup mode, cross section data can be used from an
AMPX [2]_ working format library or from a Monte Carlo format cross
section library. If KENO uses an AMPX working format library, a mixing
table data block must be entered. If a Monte Carlo format library is
used, a mixing table data block is not entered, and the mixtures
specified in the KENO geometry description must be consistent with the
mixtures created on the Monte Carlo format library file.

If KENO is run stand alone in the continuous energy mode, a mixing table
data block must be provided unless the restart option is used.

If KENO is run as part of a SCALE criticality safety or sensitivity and
uncertainty analysis sequence, the mixtures are defined in the CSAS or
TSUNAMI-3D input, and a mixing table data block cannot be entered in
KENO. Furthermore, the mixture numbers used in the KENO geometry
description must correspond to those defined in the composition data
block of the CSAS or TSUNAMI-3D input. To use a cell-weighted mixture in
KENO, the keyword “\ **CELLMIX**\ =,” followed by a unique mixture
number, must be specified in the unit cell data of the CSAS or
TSUNAMI‑3D sequence. Unit cell data are applicable only in the
multigroup mode. The mixture number used in the KENO input is the unique
mixture number immediately following the keyword “\ **CELLMIX**\ =.” A
cell‑weighted mixture is available only in SCALE sequences that use
XSDRN to perform a cell-weighting calculation using a multigroup cross
section library. :numref:`tab8-1-1` through :numref:`tab8-1-14` summarize the KENO
input data blocks. These input data blocks are discussed in detail in
the following sections.

In order to run KENO parallel (standalone execution), the user must
provide a name with the “%” prefix in the input file (=%kenovi). Control
modules like CSAS, TRITON, and TSUNAMI-3D automatically initiate
parallel KENO execution if the user provides the required arguments
while running this code.

.. list-table:: Summary of parameter data.
  :name: tab8-1-1
  :align: center

  * - .. image:: figs/Keno/tab1.svg

.. list-table:: Summary of array data.
  :name: tab8-1-2
  :align: center

  * - .. image:: figs/Keno/tab2.svg

.. list-table:: Summary of biasing data.
  :name: tab8-1-3
  :align: center

  * - .. image:: figs/Keno/tab3.svg

.. list-table:: Summary of boundary condition data.
  :name: tab8-1-4
  :align: center

  * - .. image:: figs/Keno/tab4.svg

.. list-table:: Summary of boundary condition data specific to KENO-VI.
  :name: tab8-1-5
  :align: center

  * - .. image:: figs/keno/tab5.svg

.. list-table:: Summary of geometry data in KENO V.a.
  :name: tab8-1-6
  :align: center

  * - .. image:: figs/Keno/tab6.svg
  * - .. image:: figs/Keno/tab6cont.svg

.. list-table:: Summary of geometry data in KENO-VI.
  :name: tab8-1-7
  :align: center

  * - .. image:: figs/Keno/tab7.svg

.. list-table:: Summary of mixing table data.
  :name: tab8-1-8
  :align: center

  * - .. image:: figs/Keno/tab8.svg

.. list-table:: Summary of plot data.
  :name: tab8-1-9
  :align: center

  * - .. image:: figs/Keno/tab9.svg

.. list-table:: Summary of starting data.
  :name: tab8-1-10
  :align: center

  * - .. image:: figs/Keno/tab10.svg

.. list-table:: Summary of volume data (KENO-VI).
  :name: tab8-1-11
  :align: center

  * - .. image:: figs/Keno/tab11.svg

.. list-table:: Summary of grid geometry data.
  :name: tab8-1-12
  :align: center

  * - .. image:: figs/Keno/tab12.svg

.. _tab8-1-13:
.. table:: Summary of energy group boundary data.
  :align: center

  +-----------------------------------+-----------------------------------+
  | ENERGY                            | Format: READ ENERGY energy group  |
  |                                   | boundaries END ENERGY             |
  |                                   |                                   |
  |                                   | Enter upper energy boundary for   |
  |                                   | each group in eV. The last entry  |
  |                                   | is the lower energy boundary of   |
  |                                   | the last group. For N groups,     |
  |                                   | there are N+1 entries. Entries    |
  |                                   | must be in descending order and   |
  |                                   | in units of eV.                   |
  +-----------------------------------+-----------------------------------+

.. list-table:: Summary of reaction data.
  :name: tab8-1-14
  :align: center

  * - .. image:: figs/Keno/tab14.svg


Keno input outline
~~~~~~~~~~~~~~~~~~

The data input for KENO is outlined below. Default data for KENO have
been found to be adequate for many problems. These values should be
carefully considered when entering data.

Blocks of input data are entered in the form:

**READ XXXX** *input_data* **END XXXX**

where **XXXX** is the keyword for the type of data being entered. The
keywords that can be used are listed in Table 8.1.15. A minimum of four
characters is required for a keyword, and some keyword names may be as
long as twelve characters (**READ PARAMETER**, **READ GEOMETRY**, etc.).
Keyword inputs are not case sensitive. Data input is activated by
entering the words **READ XXXX** followed by one or more blanks. All
input data pertinent to **XXXX** are then entered. Data for **XXXX** are
terminated by entering **END XXXX** followed by two or more blanks. Note
that multiple **READ GRID** blocks are used if multiple grid definitions
are needed.

.. _tab8-1-15
.. table:: Types of input data.
  :align: center

  +-----------------------------------+-----------------------------------+
  | Type of data                      | First four characters             |
  +-----------------------------------+-----------------------------------+
  | Parameters                        | PARA or PARM                      |
  +-----------------------------------+-----------------------------------+
  | Geometry                          | GEOM                              |
  +-----------------------------------+-----------------------------------+
  | Biasing                           | BIAS                              |
  +-----------------------------------+-----------------------------------+
  | Boundary conditions               | BOUN or BNDS                      |
  +-----------------------------------+-----------------------------------+
  | Start                             | STAR or STRT                      |
  +-----------------------------------+-----------------------------------+
  | Energy                            | ENER                              |
  +-----------------------------------+-----------------------------------+
  | Array (unit orientation)          | ARRA                              |
  +-----------------------------------+-----------------------------------+
  | Extra 1-D cross sections          | X1DS                              |
  +-----------------------------------+-----------------------------------+
  | Cross section mixing table\       | MIXT or MIX                       |
  | :sup:`a`                          |                                   |
  +-----------------------------------+-----------------------------------+
  | Plot\ :sup:`a`                    | PLOT or PLT or PICT               |
  +-----------------------------------+-----------------------------------+
  | Volumes                           | VOLU                              |
  +-----------------------------------+-----------------------------------+
  | Grid geometry                     | GRID                              |
  +-----------------------------------+-----------------------------------+
  | Reactions                         | REAC                              |
  +-----------------------------------+-----------------------------------+
  | :sup:`a` MIX and PLT must include |                                   |
  | a trailing blank, which is        |                                   |
  | considered part of the keyword.   |                                   |
  +-----------------------------------+-----------------------------------+

Three data records **must** be entered for every problem: first the
SCALE sequence identifier, then the problem title, and then the **END
DATA** to terminate the problem.

(1) KENO is typically run using one of the SCALE CSAS or TSUNAMI
sequences, but it may also be run stand alone using KENO V.a or KENO-VI.
The sequence identifier is specified using one line similar to:

=kenovi

This line may also include additional runtime directives that are
described throughout the SCALE manual. For example:

=kenova parm=check

The following guidance generally assumes the user is running KENO stand
alone. If KENO is to be run using of the other sequences (e.g., CSAS5),
see the appropriate manual section for additional guidance.

(2) **problem title**

   Enter a problem title (limit 80 characters, including blanks; extra
   characters will be discarded). A title **must be entered**.
   See Sect. 8.1.2.3.

(3) **READ PARA** *parameter_data* **END PARA**

   Enter parameter input as needed to describe a problem. If parameter
   data are desired in standalone KENO calculations (i.e., non-CSAS),
   they must immediately follow the problem title. Default values are
   assigned to all parameters. A problem **can** be run without entering
   any parameter data if the default values are acceptable.

   Parameter data must begin with the words **READ PARA**, **READ
   PARM**, or **READ PARAMETER.** Parameter data may be entered in any
   order. If a parameter is entered more than once, the last value is
   used. The words **END PARA** or **END PARM**, or **END PARAMETER**
   terminate the parameter data. See Sect. 8.1.2.3.

(n:sub:`1`)...( n\ :sub:`13`) The following data may be entered in any
order. Data not needed to describe the problem may be omitted.

(n:sub:`1`) **READ GEOM** *all_geometry_region_data* **END GEOM**

Geometry region data must be entered for every problem that is not a
restart problem. Geometry data must begin with the words **READ GEOM**
or **READ GEOMETRY**. The words **END GEOM** or **END GEOMETRY**
terminate the geometry region data. See Sect. 8.1.2.4.

(n:sub:`2`) **READ ARRA** *array_definition_data* **END ARRA**

   Enter array definition data as needed to describe the problem. Array
   definition data define the array size and position units (defined in
   the geometry data) in a 3-D lattice that represents the physical
   problem being analyzed. Array data must begin with the words **READ
   ARRA** or **READ ARRAY** and must terminate with the words **END
   ARRA** or **END ARRAY**. See Sect. 8.1.2.5.

(n:sub:`4`) **READ BOUN** *albedo_boundary_conditions* **END BOUN**

   Enter albedo boundary conditions as needed to describe the problem.
   Albedo data must begin with the words **READ BOUN, READ BNDS**,
   **READ BOUND**, or **READ BOUNDS,** and it must terminate with the
   words **END BOUN**, **ENDS BNDS**, **END BOUND**, or **END BOUNDS**.
   See Sect. 8.1.2.6.

(n:sub:`3`) **READ BIAS** *biasing_information* **END BIAS**

   The *biasing_information* is used to define the weight given to a
   neutron surviving Russian roulette. Biasing data must begin with the
   words **READ BIAS**. The words **END BIAS** terminate the biasing
   data. See Sect. 8.1.2.7.

(n:sub:`5`) **READ STAR** *starting_distribution_information* **END
STAR**

   Enter starting information data for starting the initial source
   neutrons only if a uniform starting distribution is undesirable.
   Start data must begin with the words **READ STAR, READ STRT** or
   **READ START**, and it must terminate with the words **END STAR**,
   **END STRT** or **END START**. See Sect. 8.1.2.8.

(n:sub:`6`) **READ ENER** *energy_group_boundaries* **END ENER**

   Enter upper energy boundaries for each neutron energy group to be
   used for tallying in the continuous energy mode. Energy bin data
   begin with the words **READ ENER** or **READ ENERGY** and terminate
   with the words **END ENER** or **END ENERGY**. The last entry is the
   lower energy boundary of the last group. The values must be in
   descending order. This block is only applicable to continuous energy
   KENO calculations. See Sect. 8.1.2.12.

(n:sub:`7`) **READ MIXT** *cross_section_mixing_table* **END MIXT**

   Enter a mixing table to define all the mixtures to be used in the
   problem. The mixing table must begin with the words **READ MIXT** or
   **READ MIX** and must end with the words **END MIXT** or **END MIX**.
   Do not enter mixing table data if KENO is being executed as a part of
   a SCALE sequence. See Sect. 8.1.2.10.

(n:sub:`8`) **READ X1DS** *extra_1-D_cross_section_IDs* **END X1DS**

   Enter the IDs of any extra 1-D cross sections to be used in the
   problem. These must be available on the mixture cross section
   library. Extra 1-D cross section data must begin with the words
   **READ X1DS** and terminate with the words **END X1DS**. See
   Sect. 8.1.2.9.

(n:sub:`9`) **READ PLOT** *plot_data* **END PLOT**

   Enter the data needed to provide a 2-D character or color plot of a
   slice through a specified portion of the 3-D geometrical
   representation of the problem. Plot data must begin with the words
   **READ PLOT**, **READ PLT**, or **READ PICT** and terminate with the
   words **END PLOT**, **END PLT**, or **END PICT**. See Sect. 8.1.2.11.

(n:sub:`10`) **READ VOLU** *volume_data* **END VOLU**

   Enter the data needed to specify the volumes of the geometry data.
   Volume data must begin with the words **READ VOLU** or **READ
   VOLUME** and end with the words **END VOLU** or **END VOLUME**. See
   Sect.Volume data.

(n:sub:`11`) **READ GRID** *mesh_grid_data* **END GRID**

   Enter the data needed to specify a simple Cartesian grid over either
   the entire problem or part of the problem geometry for tallying
   fluxes, moments, fission sources, etc. Grid data may be entered using
   the keywords **READ GRID**, **READ GRIDGEOM**, or **READ
   GRIDGEOMETRY**, and they are terminated with either **END GRID**,
   **END GRIDGEOM**, or **END GRIDGEOMETRY**. Multiple grids may be
   defined by repeating the **READ GRID** block several times,
   specifying a different mesh grid identification number for each so
   defined grid. See Sect. Grid geometry data for further information.

(n:sub:`12`) **READ REAC** *reaction_data* **END REAC**

   Enter the data needed to specify filters for the reaction tally
   calculations. Reaction data must begin with the words **READ REAC**
   and terminate with **END REAC**. This block is only applicable to
   calculations in the continuous energy mode. See Sect.8.1.2.15.

(n:sub:`13`) **END DATA must be entered**

   Terminate the data for the problem.

Procedure for data input
~~~~~~~~~~~~~~~~~~~~~~~~

For a standalone KENO problem, the first data records **must** be the
sequence identifier (e.g., =kenovi or =kenova) and the title. The next
block of data **must** be the parameters if they are to be entered. A
problem can be run without entering the parameters, which causes KENO to
use default values for input parameters. The remaining blocks of data
can be entered in any order.

   **BOLD TYPE** specifies keywords. A keyword is used to identify the
   data that follow it. When a keyword is used, it must be entered
   exactly as shown in the data guide. All keywords except those ending
   with an equal sign must be followed by at least one blank.

   *small_italics* correlate data with a program variable name. The
   actual values are entered in place of the program variable name and
   are terminated by a blank or a comma.

   *CAPITAL ITALICS* identify general data items. General data items are
   general classes of data including

   (1) geometry data such as *UNIT INITIALIZATION* and *UNIT NUMBER
   DEFINITION, GEOMETRY REGION DESCRIPTION, GEOMETRY WORD, MIXTURE
   NUMBER, BIAS ID,* and *REGION DIMENSIONS*,

   (2) albedo data such as *FACE CODES* and *ALBEDO NAMES*,

(3) weighting data such as *BIAS ID NUMBERS*, etc.

   Square brackets The square brackets, [ and ], are used to show that
   an entry is optional.

   Broken line The broken line, \|, is used as a logical “or” symbol to
   show that the entries to its left and right are alternatives that
   cannot be used simultaneously.

Title and parameter data
~~~~~~~~~~~~~~~~~~~~~~~~

A *title*, a character string, must be entered at the top of the input
file. The syntax is:

*title* a string of characters with a length of up to 80 characters,
including blanks.

The **PARAMETER** block may contain parameter initializations for those
parameters that need to be changed from their default value. The syntax
for the **PARAMETER** block is:

**READ** **PARA**\ [**METER**] *p\ 1 … p\ N* **END**
**PARA**\ [**METER**]

or

**READ** **PARM** *p\ 1 … p\ N* **END** **PARM**

*p\ 1 … p\ N* are *N* (*N* greater than or equal to zero) keyworded
parameters that together make up the *PARAMETER DATA*

The commonly changed parameters are **TME**\ *,* **GEN**\ *,* **NSK**,
and **NPG**. Seldom changed parameters are **NBK**\ *,* **NFB**\ *,*
**XNB**\ *,* **XFB**\ *,* **WTH**\ *,* **WTL**\ *,* **TBA**\ *,*
**BUG**\ *,* **TRK**\ *,* and **LNG**.

The *PARAMETER DATA*, *p\ 1 … p\ N*, consists of one or more of the
parameters described below.

Floating point parameters

  **RND** = *rndnum* input hexadecimal random number, a default value is
  provided.

  **TME** = *tmax* execution time (in minutes) for the problem, default =
  0.0 (no limit).

  **TBA** = *tbtch* time allotted for each generation (in minutes),
  default = 10 minutes. If *tbtch* is exceeded in any generation, the
  problem is assumed to be looping. Execution is terminated, and final
  edits are performed. The problem can loop indefinitely on a computer if
  the system-dependent routine to interrupt the problem (PULL) is not
  functional. **TBA=** is also used to set the amount of time available
  for generating the initial starting points.

  **SIG** = *tsigma* if entered and > 0.0, this is the standard deviation
  at which the problem will terminate, default = 0.0, which means do not
  check sigma.

  **WTA** = *dwtav* the default average weight given a neutron that
  survives Russian roulette, *dwtav* default = 0.5.

  **WTH** = *wthigh* the default value of *wthigh* is 3.0 and should be
  changed only if the user has a valid reason to do so. The weight at
  which splitting occurs is defined to be *wthigh x wtavg*, where *wtavg*
  is the weight given to a neutron that survives Russian roulette.

  **WTL** = *wtlow* Russian roulette is played when the weight of a
  neutron is less than *wtlow x wtavg*. The *wtlow* default =
  1.0/\ *wthigh*.

  .. note:: The default values of *wthigh* and *wtlow* have been determined to minimize the deviation per unit running time for many problems.
