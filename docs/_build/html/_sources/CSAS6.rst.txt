.. _CSAS6:

CSAS6:  Control Module for Enhanced Criticality Safety Analysis with KENO-VI
============================================================================

*L. M. Petrie, K. B. Bekar, D. F. Hollenbach,*\ :sup:`1` *S. Goluoglu*\ :sup:`1`


The **C**\ riticality **S**\ afety **A**\ nalysis **S**\ equence with
KENO-VI (CSAS6) provides reliable and efficient means of performing
*k\ eff* calculations for systems that are routinely encountered in
engineering practice. In the multigroup calculation mode, CSAS6 uses
XSProc to process the cross sections for temperature corrections and
problem-dependent resonance self-shielding and calculates the *k\ eff*
of three-dimensional (3-D) system models. If the continuous energy
calculation mode is selected no resonance processing is needed and the
continuous energy cross sections are used directly in KENO-VI, with
temperature corrections provided as the cross sections are loaded. The
geometric modeling capabilities available in KENO-VI coupled with the
automated cross-section processing within the control sequences allow
complex, 3-D systems to be easily analyzed.

:sup:`1`\ Formerly with Oak Ridge National Laboratory

ACKNOWLEDGMENTS

The CSAS6 Criticality Safety Analysis Sequence is based on the CSAS
control module, and the KENO‑VI functional module, described in their
respective chapters. G. E. Whitesides is acknowledged for his
contributions through early versions of KENO. Appreciation is expressed
to C. V. Parks and S. M. Bowman for their guidance in developing CSAS6.


Introduction
------------

Criticality Safety Analysis Sequence with KENO-VI (CSAS6) provides
reliable and efficient means of performing *k\ eff* calculations for
systems that are routinely encountered in engineering practice,
especially in the calculation of *k\ eff* of three-dimensional (3-D)
system models. CSAS6 implements XSProc to process material input and
provide a temperature and resonance-corrected cross-section library
based on the physical characteristics of the problem being analyzed. If
a continuous energy cross-section library is specified, no resonance
processing is needed and the continuous energy cross sections are used
directly in KENO-VI, with temperature corrections provided as the cross
sections are loaded.

Sequence Capabilities
---------------------

CSAS6 is designed to prepare a resonance-corrected cross-section library
for subsequent use in KENO‑VI. In order to minimize human error, the
SCALE data handling is automated as much as possible. CSAS6 and many
other SCALE sequences apply a standardized procedure to provide
appropriate number densities and cross sections for the calculation.
XSProc is responsible for reading the standard composition data and
other engineering-type specifications, including volume fraction or
percent theoretical density, temperature, and isotopic distribution as
well as the unit cell data. XSProc then generates number densities and
related information, prepares geometry data for resonance self-shielding
and flux-weighting cell calculations, if needed, and (if needed)
provides problem-dependent multigroup cross-section processing. CSAS6
invokes a KENO-VI Data Processor to read and check the KENO-VI data.
When the data checking has been completed, the control sequence executes
XSProc to prepare a resonance-corrected microscopic cross-section
library in the AMPX working library format if a multigroup library has
been selected.

For each unit cell specified as being cell-weighted, XSProc performs the
necessary calculations and produces a cell-weighted microscopic
cross-section library. KENO-VI may be executed to calculate the *k\ eff*
or neutron multiplication factor using the cross-section library that
was prepared by the control sequence.

Multigroup CSAS6 limitations
----------------------------

The CSAS6 control module was developed to use simple input data and
prepare problem-dependent cross sections for use in calculating the
effective neutron multiplication factor of a 3-D system using KENO-VI
and possibly XSDRNPM. An attempt was made to make the system as general
as possible within the constraints of the standardized methods chosen to
be used in SCALE. Standardized methods of data input were adopted to
allow easy data entry and for quality assurance purposes. Some of the
limitations of the CSAS6 sequence are a result of using preprocessed
multigroup cross sections. Inherent limitations in CSAS6 are as follows:

   1. Two-dimensional (2-D) effects such as fuel rods in assemblies
   where some positions are filled with control rod guide tubes,
   burnable poison rods and/or fuel rods of different enrichments. The
   cross sections are processed as if the rods are in an infinite
   lattice of rods. If the user inputs a Dancoff factor for the cell
   (such as one computed by MCDancoff), XSProc can produce an infinite
   lattice cell, which reproduces that Dancoff. This can mitigate some
   two dimensional lattice effects.

It is strongly recommended that the user perform CSAS6 calculations of
benchmark experiments similar to the problem of interest to demonstrate
the validity of the cross-section data and processing for that type of
problem.

Continuous energy CSAS6 limitations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When continuous energy KENO calculations are desired, none of the
resonance processing modules are applicable or needed. Moreover, the MG
limitations noted in the previous section are eliminated. The continuous
energy cross sections are directly used in KENO. An existing multigroup
input file can easily be converted to a continuous energy input file by
simply specifying the continuous energy library. In this case, all cell
data is ignored. However, the following limitations exist:

1. If CELLMIX is defined in the cell data, the problem will not run in
   the continuous energy mode. CELLMIX implies new mixture cross
   sections are generated using XSDRNPM-calculated cell fluxes and
   therefore is not applicable in the continuous energy mode.

2. Only VACUUM, MIRROR, PERIODIC, and WHITE boundary conditions are
   allowed. Other albedos, e.g., WATER, CARBON, POLY, etc. are for
   multigroup only.

3. Problems with DOUBLEHET cell data are not allowed as they inherently
   utilize CELLMIX feature.

Input Data Guide
----------------

The input data for CSAS6 are composed of two broad categories of data.
The first is XSProc, including Standard Composition Specification Data
and Unit Cell Geometry Specification. This first category specifies the
cross-section library and defines the composition of each mixture and
optionally the unit cell geometry that may be used to process the
cross sections. The second category of data, the KENO-VI input data, is
used to specify the geometric and boundary conditions that represent the
physical 3-D configuration of the problem. Both data blocks are
necessary for CSAS6.

All data are entered in free form, allowing alphanumeric data,
floating-point data, and integer data to be entered in an unstructured
manner. Up to 252 columns of data entry per line are allowed. Data can
usually start or end in any column with a few exceptions. As an example,
the word END beginning in column 1 and followed by two blank spaces or a
new line will end the problem and any data following will be ignored.
Each data entry must be followed by one or more blanks to terminate the
data entry. For numeric data, either a comma or a blank can be used to
terminate each data entry. Integers may be entered for floating values.
For example, 10 will be interpreted as 10.0. Imbedded blanks are not
allowed within a data entry unless an E precedes a single blank as in an
unsigned exponent in a floating-point number. For example, 1.0E 4 would
be correctly interpreted as 1.0 × 10\ :sup:`4`.

The word “END” is a special data item. An “END” may have a name or label
associated with it. The name or label associated with an “END” is
separated from the “END” by a single blank and is a maximum of
12 characters long. *At least two blanks or a new line MUST follow every
labeled and unlabeled “END.” It is the user’s responsibility to ensure
compliance with this restriction. Failure to observe this restriction
can result in the use of incorrect or incomplete data without the
benefit of warning or error messages.*

Multiple entries of the same data value can be achieved by specifying
the number of times the data value is to be entered, followed by either
R, \*, or $, followed by the data value to be repeated. Imbedded blanks
are not allowed between the number of repeats and the repeat flag. For
example, 5R12, 5*12, 5$12, or 5R 12, etc., will enter five successive
12s in the input data. Multiple zeros can be specified as nZ where n is
the number of zeroes to be entered.

The purpose of this section is to define the input data in discrete
subsections relating to a particular type of data. Tables of the input
data are included in each subsection, and the entries are described in
more detail in the appropriate sections.

Resonance-corrected cross sections are generated using the appropriate
boundary conditions for the unit cell description (i.e., void for the
outer surface of a single unit, white for the outer surface of an
infinite array of cylinders, spheres, or planes). As many unit cells as
needed may be specified in a problem. A unit cell is cell‑weighted by
using the keyword CELLMIX= followed by a unique user specified mixture
number in the unit cell data.

To check the input data without actually processing the cross sections,
the words “PARM=CHECK” or “PARM=CHK” should be entered, as shown below.

  =CSAS6    PARM=CHK

or

  #CSAS6    PARM=CHK

This will cause the input data for CSAS6 to be checked and appropriate
error messages to be printed. If plots are specified in the data, they
will be printed. This feature allows the user to debug and verify the
input data while using a minimum amount of computer time.

XSProc data
~~~~~~~~~~~

The XSProc reads the standard composition specification data and the
unit cell geometry specifications. It then produces the mixing table and
unit cell information necessary for processing the cross sections if
needed. The XSProc section of this manual provides a detailed
description of the input data and processing options.

KENO-VI data
~~~~~~~~~~~~

:numref:`tab2-2-1` contains the outline for the KENO-VI input. The KENO-VI
input is divided into 13 data blocks. A brief outline of commonly used
data blocks is shown in :numref:`tab2-2-1`. Note that parameter data must
precede all other KENO data blocks. Information on all KENO-VI input is
provided in the KENO chapter of this document and will not be repeated
here.

.. _tab2-2-1:
.. table:: Outline of KENO data

  +-----------------+-----------------+-----------------+-----------------+
  | **Type of       |    **Starting   | **Comments**    | **Termination   |
  | data**          |    flag**       |                 | flag**          |
  +-----------------+-----------------+-----------------+-----------------+
  |    Parameters\* | READ PARAMETER  |    Enter        | END PARAMETER   |
  |                 |                 |    desired      |                 |
  |                 |                 |    parameter    |                 |
  |                 |                 |    data         |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |    Geometry     | READ GEOMETRY   |    Enter        | END GEOMETRY    |
  |                 |                 |    desired      |                 |
  |                 |                 |    geometry     |                 |
  |                 |                 |    data         |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |    Array data   | READ ARRAY      |    Enter        | END ARRAY       |
  |                 |                 |    desired      |                 |
  |                 |                 |    array data   |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |    Boundary     | READ BOUNDS     |    Enter        | END BOUNDS      |
  |    conditions   |                 |    desired      |                 |
  |                 |                 |    boundary     |                 |
  |                 |                 |    conditions   |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |    Energy group | READ ENERGY     |    Enter        | END ENERGY      |
  |    boundaries   |                 |    desired      |                 |
  |                 |                 |    neutron      |                 |
  |                 |                 |    energy group |                 |
  |                 |                 |    boundaries   |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |    Start data   | READ START      |    Enter        | END START       |
  |    or initial   |                 |    desired      |                 |
  |    source       |                 |    start data   |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |    Plot data    | READ PLOT       |    Enter        | END PLOT        |
  |                 |                 |    desired plot |                 |
  |                 |                 |    data         |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |    Grid         | READ GRID       |    Enter        | END GRID        |
  |    geometry     |                 |    desired mesh |                 |
  |    data         |                 |    data         |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |    Reaction     | READ REACTION   |    Enter desire | END REACTION    |
  |                 |                 |    reaction     |                 |
  |                 |                 |    tallies (CE  |                 |
  |                 |                 |    mode only)   |                 |
  +-----------------+-----------------+-----------------+-----------------+
  |    KENO-VI data | END DATA        |    | Enter to   |                 |
  |    terminus     |                 |      signal the |                 |
  |                 |                 |      end of all |                 |
  |                 |                 |    | KENO-VI    |                 |
  |                 |                 |      data       |                 |
  +-----------------+-----------------+-----------------+-----------------+
  | \*Must precede  |                 |                 |                 |
  | all other data  |                 |                 |                 |
  | blocks in this  |                 |                 |                 |
  | table.          |                 |                 |                 |
  +-----------------+-----------------+-----------------+-----------------+

Sample Problems
---------------

This section contains sample problems to demonstrate some of the options
available in CSAS6. A brief problem description and the associated input
data for multigroup mode of calculation are included for each problem.
The same sample problems may be executed in the continuous energy mode
by changing the library name to an continuous-energy library. See
Appendix A (SECTIONREFERENCE) for additional examples.

Sample Problem 1: Aluminum 30 Degree Pipe Angle Intersection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The purpose of this problem is to calculate the k-effective of a system
composed of intersecting aluminum pipes, in the shape of a Y, filled
with a 5% enriched UO\ :sub:`2`\ F\ :sub:`2` solution. The
UO\ :sub:`2`\ F\ :sub:`2` solution at 299°K contains 907.0 gm/l of
uranium, no excess acid, and has a specific gravity of
2.0289 gm/cm\ :sup:`3`. The assembly is composed of a 212.1 cm long
vertical pipe and a second pipe that intersects the vertical pipe
76.7 cm from the outside bottom at an angle of 29.26 degrees with the
upper vertical pipe. Both pipes have 13.95 cm inner diameters and
14.11 cm outer diameters. The vertical pipe is open on the top and
1.3 cm thick on the bottom. The Y-leg pipe, in the YZ-plane, is
126.04 cm in length with the sealed end 0.64 cm thick. The assembly is
filled with solution to a height 129.5 cm above the outside bottom of
the vertical pipe. From the point where the pipes intersect the assembly
is surrounded by water 37.0 cm in the ±X directions, 100 cm in the
+Y direction, –37 cm in the –Y direction, to the top of the assembly in
the +Z direction, and –99.6 cm in the –Z direction.

.. _fig2-2-1:
.. figure:: figs/CSAS6/fig1.png
  :align: center
  :width: 400

  Critical assembly of UO\ :sub:`2`\ F\ :sub:`2` solution in a 30°-Y aluminum pipe.

.. highlight:: scale

::

  =csas6
  sample problem 1  Y-30, 5%uo2f2, 907.0g/l, 128.2, soln. ht.
  v7-238
  read comp
    solution
      mix=1
      rho[uo2f2]=907.0 92235 5.0 92238 95.0
      density=?
      temperature=299.0
    end solution
    al        2 1.0 end
    h2o       3 1.0 end
  end comp
  read parameters
    flx=yes fdn=yes far=yes pgm=yes plt=yes
  end parameters
  read start
    nst=6 tfx=0.0 tfy=0.0 tfz=0.0 lnu=1000
  end start
  read geometry
    global
    unit 1
      com='30 deg y'
      cylinder 10  13.95  135.4 -75.4
      cylinder 20  14.11  135.4 -76.7
      cylinder 30  13.95  125.4   0.0   rotate a2=-29.26
      cylinder 40  14.11  126.04  0.0   rotate a2=-29.26
      cuboid   50  2p37.0 100. -37.0 52.8 -75.4
      cuboid   60  2p37.0 100. -37.0 135.4 -99.6
      media  1  1 10  50
      media  2  1 20 -10 -30
      media  1  1 30  50 -10
      media  2  1 40 -30 -20
      media  0  1 10 -50
      media  0  1 30 -50 -10
      media  3  1 60 -20 -40 -10
      boundary  60
  end geometry
  read volume
      type=random  batches=1000
  end volume
  read plot
    scr=yes  lpi=10
    ttl='y-z slice at x=0.0  through centerline of both pipes'
    xul=0.0  yul=-39.0  zul=137.0
    xlr=0.0  ylr=105.0  zlr=-105.0
    vax=1    wdn=-1
    nax=400  end plt0
    ttl='x-y slice at z=26.0  slightly above point of separation'
    xul=-40.0 yul=105.0  zul=26.0
    xlr=+40.0 ylr=-40.0  zlr=26.0
    uax=1     vdn=-1
    nax=400 end plt1
    ttl='x-y slice at z=75.0  well above point of separation'
    xul=-40.0 yul=105.0  zul=75.0
    xlr=+40.0 ylr=-40.0  zlr=75.0
    uax=1     vdn=-1
    nax=400 end plt2
  end plot
  end data
  end

Sample Problem 2: Plexiglas Cross
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The purpose of this problem is to calculate the k-effective of a system
composed of intersecting Plexiglas pipes, in the shape of a cross,
filled with a 5% enriched UO\ :sub:`2`\ F\ :sub:`2` solution. The room
temperature UO\ :sub:`2`\ F\ :sub:`2` solution contains 896.1 gm/l of
uranium, no excess acid, and has a specific gravity of
2.015 gm/cm\ :sup:`3`. The pipes have a 13.335 cm inner diameter and
16.19 cm outer diameter. The vertical pipe is open on the top and
3.17 cm thick on the bottom. The horizontal pipe ends are 3.17 thick.
The vertical pipe is 210.19 cm in length and filled with solution to a
height of 117.2 cm. The two horizontal legs, positioned in the XZ‑plane,
intersect the vertical pipe 91.44 cm from the outside bottom at an
89 degree angle with the upper section of the pipe. Each horizontal is
91.44 cm in length and filled with the above specified
UO\ :sub:`2`\ F\ :sub:`2` solution. A water reflector surrounding the
solution filled pipes extends out from the point where the pipes
intersect 111.76 cm in the ±X directions, 20.64 cm in the ±Y directions,
29.03 cm in the +Z direction, and –118.428 cm in the –Z direction.

.. _fig2-2-2:
.. figure:: figs/CSAS6/fig2.png
  :align: center
  :width: 400

  Critical assembly of UO\ :sub:`2`\ F\ :sub:`2` solution in a Plexiglas cross.

::

  =csas6
  sample problem 2  89-cross, 5% uo2f2 soln, plexiglass pipes, h2o refl.
  v7-238
  read comp
    solution
      mix=1
      rho[uo2f2]=896.1 92235 5.0 92238 95.0
      density=?
      temperature=298.0
    end solution
    plexiglass 3 1.0 end
    h2o        2 1.0 end
  end comp
  read param
    plt=yes
  end param
  read geom
    global unit 1
      cylinder  10  13.335 28.93 -88.27
      cylinder  20  13.335 121.92 -88.27
      cylinder  30  16.19 121.92 -91.44
      cylinder  40  13.335 88.27 0.0 rotate a1=90. a2=89.
      cylinder  50  16.19  91.44 0.0 rotate a1=90. a2=89.
      cylinder  60  13.335 88.27 0.0 rotate a1=-90. a2=89.
      cylinder  70  16.19  91.44 0.0 rotate a1=-90. a2=89.
      cuboid    80  2p111.74 2p20.64 29.03 -118.428
      cuboid    90  2p111.74 2p40.64 121.92 -118.428
      media 1 1 10
      media 0 1 20 -10
      media 3 1 30 -10 -20 -50 -70
      media 1 1 40 -10 -20
      media 3 1 50 -40 -10 -20
      media 1 1 60 -10 -20
      media 3 1 70 -60 -10 -20 -50
      media 2 1 80 -10 -20 -30 -40 -50 -60 -70
      media 0 1 90 -20 -30 -80
      boundary  90
  end geom
  read volume
     type=trace
  end volume
  read start
    nst=6  tfx=0. tfy=0. tfz=0. lnu=1000
  end start
  read plot
    scr=yes  lpi=10
    ttl=' x-z slice at y=0.0 '
    xul=-113. yul=0. zul=  48.
    xlr= 113. ylr=0. zlr=-120.
    uax=1.0   wdn=-1.0
    nax=400  end plt0
    ttl=' y-z slce at x=0.0 '
    xul=0.    yul=-42. zul= 122.
    xlr=0.    ylr= 42. zlr=-120.
    vax=1.0   wdn=-1.0
    nax=400  end plt1
    ttl=' x-y slice at z=0.0 '
    xul=-113.0 yul= 42. zul=0.
    xlr= 113.0 ylr=-42. zlr=0.
    uax=1.0    vdn=-1.0
    nax=400  end plt2
  end plot
  end data
  end

Sample Problem 3: Sphere
~~~~~~~~~~~~~~~~~~~~~~~~

This problem models an assembly consisting of a 93.2% enriched bare
uranium sphere, 8.741 cm in radius, having a density of
18.76 gm/cm\ :sup:`3`. Problem 3 models the assembly as a single bare
sphere. The second problem models the assembly as a hemisphere with
mirror reflection on the flat surface. The next three problems model the
sphere using chords. This set of four problems is designed to illustrate
the use of multiple chords in a problem.

::

  =csas6
  sample problem 3  bare 93.2% enriched uranium sphere
  v7-238
  read comp
    uranium  1 den=18.76 1 293 92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
  end comp
  read geometry
    global unit 1
      sphere 10  8.741
      cuboid   20  6p8.741
      media  1 1 10      vol=2797.5121
      media  0 1 20 -10  vol=2545.3424
      boundary 20
  end geometry
  end data
  end

Sample Problem 4: Sphere Models Using Chords and Mirror Albedos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem models an assembly consisting of a 93.2% enriched bare
uranium sphere, 8.741 cm in radius, having a density of
18.76 gm/cm\ :sup:`3`. The problem models the assembly as a hemisphere
with mirror reflection on the flat surface.

::

  =csas6
  sample problem 4  bare 93.2% U sphere, hemisphere w/ mirror albedo
  v7-238
  read comp
    uranium  1 den=18.76 1 293 92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
  end comp
  read geometry
    global unit 1
      sphere 10  8.741  chord +x=0.0
      cuboid   20  8.741 0.0  8.741 -8.741 8.741 -8.741
      media  1 1 10      vol=2797.5121
      media  0 1 20 -10  vol=2545.3424
      boundary 20
  end geometry
  read bounds
    -xb=mirror
  end bounds
  end data
  end

Sample Problem 5: Sphere Models Using Chords and Mirror Albedos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem models an assembly consisting of a 93.2% enriched bare
uranium sphere, 8.741 cm in radius, having a density of
18.76 gm/cm\ :sup:`3`. The problem models the assembly as a quarter
sphere with mirror reflection on the two flat surfaces.

::

  =csas6
  sample problem 5  bare 93.2% U sphere, quarter sphere w/ mirror albedo
  v7-238
  read comp
    uranium  1 den=18.76 1 293 92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
  end comp
  read geometry
    global unit 1
      sphere 10  8.741  chord +x=0.0  chord  +y=0.0
      cuboid   20  8.741 0.0 8.741 0.0 8.741 -8.741
      media  1 1 10      vol=2797.5121
      media  0 1 20 -10  vol=2545.3424
      boundary 20
  end geometry
  read bounds
    -xy=mirror
  end bounds
  end data
  end

Sample Problem 6: Sphere Models Using Chords and Mirror Albedos (Eighth Sphere)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem models an assembly consisting of a 93.2% enriched bare
uranium sphere, 8.741 cm in radius, having a density of
18.76 gm/cm\ :sup:`3`. The problem models the assembly as an eighth
sphere with mirror reflection on the three flat surfaces.

::

  =csas6
  sample problem 6  bare 93.2% U sphere, eighth sphere w/ mirror albedo
  v7-238
  read comp
    uranium  1 den=18.76 1 293 92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
  end comp
  read geometry
    global unit 1
      sphere 10  8.741  chord +x=0.0  chord  +y=0.0  chord +z=0.0
      cuboid   20  8.741 0.0 8.741 0.0 8.741 0.0
      media  1 1 10      vol=2797.5121
      media  0 1 20 -10  vol=2545.3424
      boundary 20
  end geometry
  read bounds
    -fc=mirror
  end bounds
  end data
  end

Sample Problem 7: Grotesque without the Diaphragm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The purpose of this problem is to calculate the *k*\ :sub:`eff` of a system
composed of eight enriched uranium units placed on a diaphragm, with an
irregularly shaped centerpiece positioned in the center hole of the
diaphragm :cite:`mihalczo_brief_1999` The assembly and centerpiece are shown in :numref:`fig2-2-3`,
which is Fig. 4 from Ref. 1. The eight units consist of an approximate
parallelepiped with an irregular top, a parallelepiped, and
six cylinders of various sizes. The centerpiece, which penetrates the
hole in the diaphragm, consists of a cylinder topped by a parallelepiped
topped by a hemisphere. The diaphragm is not modeled in this example.

.. _fig2-2-3:
.. figure:: figs/CSAS6/fig3.png
  :align: center
  :width: 400

  Grotesque experimental setup.

::

  =csas6
  sample problem 7  keno-vi grotesque w/o diaphragm, ornl/csd/tm-220
  v7-238
  read comp
    uranium   1 den=18.76 1 293 92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
    uranium   2 den=18.76 1 293 92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
    uranium   3 den=18.76 1 293 92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
    uranium   4 den=18.76 1 293 92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
    uranium   5 den=18.76 1 293 92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
    uranium   6 den=18.76 1 293 92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
    uranium   7 den=18.76 1 293 92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
    uranium   8 den=18.76 1 293 92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
    uranium   9 den=18.76 1 293 92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
    uranium  10 den=18.76 1 293 92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
    uranium  11 den=18.76 1 293 92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
    uranium  12 den=18.76 1 293 92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
    uranium  13 den=18.76 1 293 92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
    uranium  14 den=18.76 1 293 92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
  end comp
  read param
    pgm=yes plt=yes
  end param
  read geom
    global unit 1
  '*** one through three is item 1 in drawing 84-10649 ornl/csd/tm-220 ***
  'one    top piece of item 1
    cuboid 10  2p6.3515 1.2685 -3.8115 13.377 13.058 origin y=-17.464 z=0.15 rotate a2=-1.35
  'two    middle piece of item 1
    cuboid 20  2p6.3515 6.3515 -3.8115 13.058 11.155 origin y=-17.464 z=0.15 rotate a2=-1.35
  'three  bottom piece of item 1
    cuboid 30  4p6.3515 11.155 0. origin y=-17.464 z=0.15 rotate a2=-1.35
  '*** four is item 2 in drawing 84-10649 ornl/csd/tm-220 ***
    cylinder 40 4.555 12.918 0.        origin x=-12.176 y=-9.343 z=0.111 rotate a1=-52.5 a2=-1.400
  '*** five is item 3 in drawing 84-10649 ornl/csd/tm-220 ***
    cylinder 50 5.761 13.475 0.        origin x=-16.333 y=1.681 z=0.174 rotate a1=83.5 a2=+1.173
  '*** six is item 4 in drawing 84-10649 ornl/csd/tm-220 ***
    cylinder 60 4.5525 12.969 0.    origin x=-9.539 y=11.168 z=0.156 rotate a1=40.5 a2=+1.970
  '*** seven and eight are item 5 in drawing 84-10649 ornl/csd/tm-220 ***
  'seven
    cuboid  70  2p3.81 8.13 -4.573 8.91 0. origin y=15.698 z=0.290 rotate a2=+2.58
  'eight
    cylinder 80 4.573 13.229 8.91   origin y=15.698 z=0.290 rotate a2=+2.58
  '*** nine is item 6 in drawing 84-10649 ornl/csd/tm-220 ***
    cylinder 90 4.5545 12.974 0.    origin x=9.854 y=10.964 z=0.134 rotate a1=-42.0 a2=+1.680
  '*** ten is item 7 in drawing 84-10649 ornl/csd/tm-220 ***
    cylinder 100 5.7495 13.475 0.    origin x=16.388 y=1.434 z=0.140 rotate a1=-86.0 a2=+1.400
  '*** eleven is item 8 in drawing 84-10649 ornl/csd/tm-220 ***
    cylinder 110 4.5565 12.954 0.    origin x=12.029 y=-9.398 z=0.087 rotate a1=38.0 a2=-1.100
  '*12 through 14 is the centerpiece in drawing 84-10649 ornl/csd/tm-220
  'twelve
    cylinder 120 5.757 2.690 0.      origin x=-0.593 y=-0.593 z=-1.753
  'thirteen
    cuboid 130 4p6.35 5.718 0.       origin z=0.937
  'fourteen
    sphere    140 6.082 chord +z=0.   origin x=-0.268 y=0.268 z=6.655
  '*** fifteen is the system boundary ***
  'fifteen
    cuboid   150 4p25.0 15.0 -2.0
    media  1 1 +10       vol=20.58546556
    media  2 1 +20 -10   vol=245.678420867
    media  3 1 +30 -20   vol=1800.040061395
    media  4 1 +40       vol=842.019046637
    media  5 1 +50       vol=1404.99376489
    media  6 1 +60       vol=844.415646269
    media  7 1 +70       vol=862.4600226
    media  8 1 +80 -70   vol=283.749744681
    media  9 1 +90       vol=845.483582679
    media 10 1 +100      vol=1399.390119093
    media 11 1 +110      vol=844.921798001
    media 12 1 +120 -130 vol=280.088070346
    media 13 1 +130      vol=922.25622
    media 14 1 +140 -130 vol=471.191948666
    media 0 1 150 -10 -20 -30 -40 -50 -60 -70 -80 -90 -100
              -110 -120 -130 -140  vol=31432.726088316
    boundary 150
  end geom
  read plot
    scr=yes  lpi=10
             clr= 1 255   0   0
                  2   0   0 205
                  3   0 229 238
                  4   0 238   0
                  5 205 205   0
                  6 255 121 121
                  7 145  44 238
                  8 150 150 150
                  9 240 200 220
                 10   0 191 255
                 11 224 255 255
                 12   0 128  64
                 13 255 202 149
                 14 255   0 128
              end color
    ttl='grotesque x-y slice at z=0.5'
    xul=-25.5 yul= 25.5 zul=0.5
    xlr= 25.5 ylr=-25.5 zlr=.5
    uax=1     vdn=-1  nax=800 end
    ttl='grotesque x-y slice at z=2.0'
    xul=-25.5 yul= 25.5 zul=2
    xlr= 25.5 ylr=-25.5 zlr=2 end
    ttl='grotesque x-y slice at z=9.5'
    xul=-25.5 yul= 25.5 zul=9.5
    xlr= 25.5 ylr=-25.5 zlr=9.5 end
    ttl='grotesque y-z slice at x=-0.593'
    xul=-.593 yul=-25.5 zul=15.5
    xlr=-.593 ylr= 25.5 zlr=-3.5
    uax=0     vax=1
    vdn=0     wdn=-1 nax=800  end
    ttl='grotesque x-z slice at y=0.0'
    xul=-25.5 yul=0.0  zul=15.5
    xlr= 25.5 ylr=0.0  zlr=-3.5
    uax=1     vax=0    wax=0
    udn=0     vdn=0    wdn=-1 nax=800  end
    ttl='grotesque x-z slice at y=12.125'
    xul=-25.5 yul=12.125  zul=15.5
    xlr= 25.5 ylr=12.125  zlr=-3.5
    uax=1     vax=0       wax=0
    udn=0     vdn=0       wdn=-1 nax=800  end
    ttl='grotesque x-z slice at y=-12.000'
    xul=-25.5 yul=-12.000  zul=15.5
    xlr= 25.5 ylr=-12.000  zlr=-3.5
    uax=1     vax=0        wax=0
    udn=0     vdn=0        wdn=-1 nax=800  end
  end plot
  end data
  end

Sample Problem 8 Infinite Array of MOX and UO2 Assemblies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The purpose of this problem is to calculate the *k\ eff* of a system
composed of an infinite array of MOX assemblies interspersed between
UO\ :sub:`2` assemblies. Both assembly types contain 331 pins in a
hexagonal lattice with a pin pitch of 1.275 cm and an assembly pitch
of 23.60 cm as shown in
:numref:`fig2-2-4`. The moderator is borated water at 306°C having a density
of 0.71533 gm/cc and composed of 99.94 wt % H\ :sub:`2`\ O and
0.06 wt % natural boron. Each fuel rod is 355 cm in length, has a
radius of 0.3860 cm, 0.722-cm-thick Zr cladding with no gap, and is at
a temperature of 754°C.

The UO\ :sub:`2` fuel consists of 4.4 wt % :sup:`235`\ U and 95.6 wt %
:sup:`238`\ U at a density of 8.7922 gm/cc. The UO\ :sub:`2` fuel also
contains 9.4581E–9 atoms/b-cm of :sup:`135`\ Xe and 7.3667E–8 atoms/b-cm
of :sup:`149`\ Sm.

The MOX fuel consists of 96.38 wt % UO\ :sub:`2` and
3.62 wt % PuO\ :sub:`2` at a density of 8.8182 gm/cc. The UO\ :sub:`2`
fuel is composed of 2.0 wt % \ :sup:`235`\ U and
98.0 wt % \ :sup:`238`\ U. The PuO\ :sub:`2` fuel is composed of
93.0 wt % :sup:`239`\ Pu, 6.0 wt % \ :sup:`240`\ Pu- and
1.0 wt % \ :sup:`241`\ Pu. The MOX fuel also contains 9.4581E–9
atoms/b-cm of :sup:`135`\ Xe and 7.3667E–8 atoms/b-cm of :sup:`149`\ Sm.

These two assemblies are placed so they represent an infinite array in
the X and Y dimensions as shown in :numref:`fig2-2-5`. There is 20 cm of water
above and below fuel assemblies. This problem uses CENTRM/PMC as the
resolved resonance processor cross section. Since an infinite array
cannot be explicitly modeled, a section of the array is modeled and the
X and Y sides have mirror reflection.

::

  =csas6        parm=(centrm)
  sample problem 8 - VVER inf. array - MOX & UO2 Assemblies
  v7-238
  read comp
  '  UO2 Fuel
      uo2     1 den=8.7922 1.0 1027 92235 4.4  92238 95.6 end
      xe-135  1 0 9.4581E-09 1027 end
      sm-149  1 0 7.3667E-08 1027 end
  '  MOX Fuel
      uo2     2 den=8.8182 0.9638 1027  92235  2.0 92238 98.0 end
      puo2    2 den=8.8182 0.0362 1027  94239 93.0 94240  6.0 94241  1.0 end
      xe-135  2 0 9.4581E-09 1027 end
      sm-149  2 0 7.3667E-08 1027 end
  '  Cladding for UO2 fuel
      zr      3 den=6.4073 1.0  579  end
  '  Moderator for UO2 fuel
      h2o     4 den=0.71533 0.9994 579 end
      boron   4 den=0.71533 0.0006 579 end
  '  Cladding for MOX fuel
      zr      5 den=6.4073 1.0  579  end
  '  Moderator for MOX fuel
      h2o     6 den=0.71533 0.9994 579 end
      boron   6 den=0.71533 0.0006 579 end
  '  Moderator for vacant units
      h2o     7 den=0.71533 0.9994 579 end
      boron   7 den=0.71533 0.0006 579 end
  end comp
  read celldata
    latticecell triangpitch pitch=1.2750 4 fueld=0.7720 1 cladd=0.9164 3 end
    latticecell triangpitch pitch=1.2750 6 fueld=0.7720 2 cladd=0.9164 5 end
  '  more data  dab=500  end more
  end celldata
  read param
    gen=203  npg=1000
  end param
  read bounds
    all=mirror zfc=void
  end bounds
  read geom
    unit   1
     com='UO2 Fuel Rod'
     cylinder 10 0.3860 355.0 0.0
     cylinder 20 0.4582 355.0 0.0
     hexprism 30 0.6375 355.0 0.0
     media 1 1 10
     media 3 1 20 -10
     media 4 1 30 -20
     boundary 30
    unit  2
     com='Vacant(water filled) hex'
     hexprism 10 0.6375 355.0 0.0
     media 7 1 10
     boundary 10
    unit  3
     com='Vacant(water filled) hex'
     hexprism 10 0.6375 355.0 0.0
     media 7 1 10
     boundary 10
    unit   4
     com='MOX Fuel Rod'
     cylinder 10 0.3860 355.0 0.0
     cylinder 20 0.4582 355.0 0.0
     hexprism 30 0.6375 355.0 0.0
     media 2 1 10
     media 5 1 20 -10
     media 6 1 30 -20
     boundary 30
    global unit 5
     rhexprism 10 11.800 355.0 0.0
     rhexprism 20 11.800 355.0 0.0 origin y=23.6
     rhexprism 30 11.800 355.0 0.0 origin x=20.4382 y=11.8
     rhexprism 40 11.800 355.0 0.0 origin x=20.4382 y=35.4
     cuboid   50 20.4382 0.0 35.4 0.0 375.0 -20.0
     array 1  10 -20 -30 -40 place 12 12 1  0.0       0.0  0.0
     array 2  20 -10 -30 -40 place 12 12 1  0.0      23.6  0.0
     array 2  30 -10 -20 -40 place 12 12 1  20.4382  11.8  0.0
     array 1  40 -10 -20 -30 place 12 12 1  20.4382  35.4  0.0
     media 4 1 50 -10 -20 -30 -40
     boundary 50
  end geom
  read array
    ara=1 typ=shexagonal nux=23 nuy=23 nuz=1
      fill
     3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
      3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 3 3 3 3 3 3
     3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 3 3 3 3 3
      3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3 3 3 3
     3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3 3 3
      3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3 3 3
     3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3 3
      3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3 3
     3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3
      3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3
     3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3
      3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3
     3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3
      3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3
     3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3
      3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3 3
     3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3 3
      3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3 3 3
     3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3 3 3
      3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3 3 3 3
     3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 4 3 3 3 3 3
      3 3 3 3 3 3 4 4 4 4 4 4 4 4 4 4 4 3 3 3 3 3 3
     3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
      end fill
    ara=2 typ=shexagonal nux=23 nuy=23 nuz=1
      fill
     2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
      2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2
     2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2
      2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2
     2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2
      2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2
     2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2
      2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2
     2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2
      2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2
     2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2
      2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2
     2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2
      2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2
     2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2
      2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2
     2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2
      2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2
     2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2
      2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2
     2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2
      2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2
     2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
      end fill
  end array
  read plot
    lpi=10 scr=yes
    ttl='VVER assembly x-y x-section'
    xul=-0.1  yul=35.5  zul=10
    xlr=20.6  ylr=-0.1  zlr=10
    uax=1     vdn=-1.0
    nax=640   pic=mat   end plt1
  end plot
  read volume
      type=random  batches=1000
  end volume
  end data
  end

.. _fig2-2-4:
.. figure:: figs/CSAS6/fig4.png
  :align: center
  :width: 400

  MOX or UO\ :sub:`2` hexagonal assembly.

.. _fig2-2-5:
.. figure:: figs/CSAS6/fig5.png
  :align: center
  :width: 400

  Infinite array of MOX assemblies interspersed between UO\ :sub:`2` assemblies.

Warning and Error Messages
--------------------------

CSAS6 contains two types of warning and error messages. The first type
of message is from XSProc is common to many of the SCALE analytical
sequences. The second type of message is from the CSAS6 subroutines and
is identified by CS- followed by a number. These messages are listed in
numerical order below. For additional information concerning a
message, simply look up the number in this section.

Warning messages appear when a possible error is encountered. It is the
responsibility of the user to verify whether the data are correct when a
warning message is encountered. The functional modules activated by
CSAS6 and related sequences will be executed even though a warning
message has been generated.

When an error is recognized, an error message is written and an error
flag is set so the functional modules will not be activated. The code
stops immediately if the error is too severe to allow continuation of
input. However, it will continue to read and check the data if it is
able. When the data reading is completed, execution is terminated if an
error flag was set when the data were being processed. If the error flag
has not been set, execution continues. When error messages are printed,
the user should focus on the first error message, because subsequent
messages may have been caused by the error that generated the first
message.

The following messages originate in the part of CSAS6 that reads,
checks, and prepares data for KENO‑VI. The same set of error messages
are also used for CSAS5 that reads, checks, and prepares data for
KENO V.a and MODIFY. CSAS6 is not capable of performing searches at this
time. An error message referring to a SEARCH routine, from a CSAS6
problem, indicates a code error.

CS-16 \***WARNING**\* READ FLAG NOT FOUND. ASSUME KENO V PARAMETER DATA FOLLOWS.
  This message from subroutine CPARAM indicates that the word READ is not
  the first word of KENO-VI data following the Material Information
  Processor input data. If parameter data is to be entered, the code
  expects the words READ PARAMETERS to precede the parameter input data.
  If the word READ is not the first word, the code assumes the data are
  parameter input data.

CS-21 A UNIT NUMBER WAS ENTERED FOR THE CROSS-SECTION LIBRARY. (LIB= IN PARAMETER DATA.) THE DEFAULT VALUE SHOULD BE USED IN ORDER TO UTILIZE THE CROSS SECTIONS GENERATED BY CSAS. MAKE CERTAIN THE CORRECT CROSS-SECTION LIBRARY IS BEING USED.
  This message is from subroutine CPARAM. It indicates that a value has
  been entered for the cross-section library in the KENO-VI parameter
  data. The cross-section library created by the analytical sequence
  should be used. MAKE CERTAIN THAT THE CORRECT CROSS SECTIONS ARE BEING
  USED.

CS-55 \**\* ERRORS WERE ENCOUNTERED IN PROCESSING THE CSAS-KENO6 DATA. EXECUTION IS IMPOSSIBLE. \**\*
  This message from subroutine SASSY is printed if errors were found in
  the KENO-VI input data for CSAS. If a search is being made, data reading
  will continue until all the data have been entered or a fatal error
  terminates the data reading. When the data reading and checking have
  been completed, the problem will terminate without executing. Check the
  printout to locate the errors responsible for this message.

CS-62 \**\* ERROR \**\* MIXTURE \_____\_ IN THE GEOMETRY WAS NOT CREATED IN THE STANDARD COMPOSITIONS SPECIFICATION DATA.
  This message from subroutine MIXCHK indicates that a mixture specified
  in the KENO-VI geometry was not created in the standard composition
  data.

CS-68 \**\* ERROR \**\* AN INPUT DATA ERROR HAS BEEN ENCOUNTERED IN THE DATA ENTERED FOR THIS PROBLEM.
  This message from the main program, CSAS6, is printed if the subroutine
  library routine LRDERR returns a value of “TRUE,” indicating that a
  reading error has been encountered in the “KENO PARAMETER” data. The
  appropriate data type is printed in the message. Locate the unnumbered
  message stating “****\* ERROR IN INPUT. CARD IMAGE PRINTED ON NEXT LINE
  \*****.” Correct the data and resubmit the problem.

CS-69 \***ERROR**\* MIXTURE \_____\_ IS AN INAPPROPRIATE MIXTURE NUMBER FOR USE IN THE KENO GEOMETRY DATA BECAUSE IT IS A COMPONENT OF THE CELL-WEIGHTED MIXTURE CREATED BY XSDRNPM.
  This message from subroutine CMXCHK indicates that a mixture that is a
  component of a cell-weighted mixture has been used in the KENO-VI
  geometry data.

CS-82 \**\* AN ERROR WAS ENCOUNTERED IN ONE OF THE FUNCTIONAL MODULES.
  This message from CSAS6 indicates that an error was encountered during
  execution of one of the functional modules such as CRAWDAD, BONAMI,
  CENTRM, PMC, XSDRNPM, or KENO-VI. Check the printout to locate and
  correct the error.

CS-99 THIS PROBLEM WILL NOT BE RUN BECAUSE PARM=CHECK WAS ENTERED IN THE ANALYTICAL SEQUENCE SPECIFICATION.
  This message from subroutine CSAS indicates that the problem data were
  read and checked and no errors were found. To execute the problem,
  remove the PARM=CHECK or PARM=CHK from the analytical sequence indicator
  data entry.

CS-100 THIS PROBLEM WILL NOT BE RUN BECAUSE ERRORS WERE ENCOUNTERED IN THE INPUT DATA.
  This message from subroutine CSAS is self-explanatory. Examine the
  printout to locate the error or errors in the input data. Correct them
  and resubmit the problem.

.. bibliography:: bibs/CSAS6.bib
