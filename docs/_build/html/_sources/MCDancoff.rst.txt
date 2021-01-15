.. _7-8:

MCDancoff Data Guide
====================

*L. M. Petrie, B. T. Rearden*

ABSTRACT

The MCDancoff program is used to calculate Dancoff factors in
complicated, three-dimensional (3-D) geometries using Monte Carlo
integrations. The geometries are standard SCALE geometry descriptions,
with the current restriction that Dancoff factors can only be calculated
for regions bounded by cuboids, spheres, or cylinders. Multiple Dancoff
factors can be calculated with one input file.

ACKNOWLEDGMENT

This work was sponsored in part by Atomic Energy of Canada, Ltd. The
contribution of S. J. Poarch in preparing this document is gratefully
acknowledged.

.. _7-8-1:

Introduction
------------

MCDancoff (Monte Carlo Dancoff) is a program that calculates Dancoff
factors for complicated, three-dimensional geometries. Its input is a
slight modification of a CSAS6 input file which uses the standard SCALE
geometry as detailed for KENO-VI. The modifications to the input involve
different input in the START data block describing which Dancoff factors
are to be calculated. The calculation involves starting histories
isotropically on the surface of the region for which the Dancoff factor
is to be calculated and following the path of each history until it has
encountered all the elements of the material in the region, or until it
has exited the system. A one group cross-section library is used to
determine the total cross sections of the mixtures in the problem.

A current restriction of MCDancoff is that it can only calculate Dancoff
factors for regions bounded by cylinders, spheres, or cuboids. Other
simple bodies could be added in the future, but a general bounding
surface would be impractical.

The Dancoff factors are used in SCALE to correctly self-shield
multigroup cross sections for a given problem; either as input to BONAMI
or to determine an equivalent cell for CENTRM. This is most typically
accomplished through the MORE DATA and CENTRM DATA blocks.

The Dancoff factors are actually calculated by a modified version of the
KENO-VI code called KENO_Dancoff. All printed output from these
calculations is suppressed by default. If there is a need to see this
output (for example, to find an error message), it can be turned on by
setting an environment variable **print_dancoff=yes**.

.. _7-8-2:

Input data description
----------------------

MCDancoff input data is the same as CSAS6 input data with the following
exceptions. A special one group cross-section library will be used. It
can be specified as **xn01** in the input but will be set to this if
anything else is entered for the library. Because MCDancoff is running a
fixed source problem, and the Dancoff factor doesn’t need to be
calculated with the same accuracy as an eigenvalue, there are useful
changes that can be made to the parameters in the PARAMETER data block.
:ref:`7-8-3` discusses this in more detail. Finally, the START data
block is used to define which Dancoff factors will be calculated. This
data block is defined below.

**READ START** Begins the data block

1. **dancoff**

begins defining a new Dancoff factor. Always start
relative to the global unit in the geometry.

2. **array**

step into an array contained in the current unit – followed
by **karray**, **nbx**, **nby**, **nbz** where **karray** is the
region containing the array in the current unit, **nbx** is the x
position in the array of the next unit, **nby** is the y position
in the array of the next unit, and **nbz** is the z position in
the array of the next unit.

3. **hole**

step into a hole contained in the current unit – followed by
**nhole**, the hole number relative to the current unit.

4. **unit**

final unit in the nesting chain – followed by **nn**, the
unit number

5. **region**

region to calculate the Dancoff factor for – followed by
**k**, the relative geometry word in unit **nn** defining the
outer bound of the region.

6. **nst**

if input, must be 0 (defaults to 0).

Repeat 2 and 3 to get from the global unit to the final unit **nn**.

Repeat 1–5 for each Dancoff factor to be calculated.

**END START** Ends the data block


.. _7-8-3:

Calculation and use of 3D Dancoff factors
-----------------------------------------

1. The 3-D Dancoff factors are computed with KENO-VI geometry. If
   beginning with CSAS5 model, use C5TOC6 to convert to CSAS6.

2. Change sequence name from CSAS6 to MCDancoff and change cross-section
   library to **xn01**.

3. Input appropriate parameter data.

..

   Since the Dancoff calculation is fixed source integration, there is
   no need to skip generations, and **nsk** should be set to 0. Since
   small changes to the Dancoff have very minor effects on the cross
   sections, fewer histories are probably needed for calculating the
   Dancoff than for calculating *k\ eff*. Thirty thousand histories
   divided as 100 generations of 300 histories per generation has
   produced Dancoff factors with deviations of less than 1 percent. It
   may be advantageous to turn off plots at this point. Since the same
   parameters can be entered more than once, with the final entry being
   the one used, adding a separate record with these values immediately
   before the **end parameter** keywords would override the original
   KENO-VI parameters.

   Example:


.. highlight:: scale

..


::

     read param
              .........
       nsk=0 npg=300 gen=100 nub=no fdn=no flx=yes plt=no
     end param


4. Identify the region for which Dancoff factors are desired in START
   data.

..

   The start type needs to be set to **0** for the Dancoff calculation
   (this is the default). All KENO-VI START data should be removed or
   commented out by placing an apostrophe in column 1. Each region for
   which a Dancoff calculation is desired then starts with the keyword
   **dancoff**. This is followed by data that specify the relationship
   of the global unit to the specific geometry description of the
   region. If the region is nested inside an array, then the keyword,
   **array**, is specified, followed by four integers. The first integer
   is the indices of the media record specifying the array relative to
   the current unit. The next 3 integers are the X, Y, and Z indexes of
   the position of the next unit in the array. If the region is nested
   in a hole, then the keyword, **hole**, is specified, followed by the
   relative count of the correct hole in the unit. The preceding data
   are repeated (in the correct nesting order starting with the global
   unit) until reaching the unit where the region is located. Then the
   keyword, **unit**, followed by the unit number is given, followed by
   the keyword, **region**, followed by the relative index of the
   geometry keyword describing the desired region with respect to that
   unit. Currently, only cylinders, spheres, and cuboids are programmed
   for calculating Dancoff factors.

   Examples:

   ::

     read start
       nst=0
       dancoff    hole 1    unit=1  reg=1
     end start

     read start
        dancoff  array  1 1 1 1  array  1 17 17 2  unit 10  region 1
     end start


5. Execute MCDANCOFF *filename.*\ input file like any other SCALE input
   file.


6. Examine *filename*.dancoff file, which will contain Dancoff factors
   for each nuclide in the specified region

::

  index        nuclide        dancoff      deviation
                     1          92234    3.36340E-01    1.81134E-03
                     2          92235    3.36340E-01    1.81134E-03
                     3          92236    3.36340E-01    1.81134E-03
                     4          92238    3.36340E-01    1.81134E-03
                     5           8016    1.00000E+00    0.00000E+00

7.	Once all desired Dancoff factors are obtained, return to original model and
    enter CENTRM DATA for each cell with dan2pitch(mix) specified.

::

  read celldata
    latticecell triangpitch fuelr=0.633  1 gapr=0.637 0 cladr=0.675 10 hpitch=0.867  14 end
  centrm data
    dan2pitch(1)=0.336
  end centrm

8. If executing TSUNAMI-3D, additional steps are necessary because
   TSUNAMI‑3D does not treat the dan2pitch input parameter.

..

   Return to the original TSUNAMI-3D input file and replace the sequence
   name to “CSAS-MG PARM=CHECK” and delete all data after the unit cell
   data to quickly obtain revised pitch values. (Note: CSAS will not
   modify cell dimensions to more than 20 cm, so a revised moderator
   density may need to be entered to obtain the desired Dancoff factor.)
   Search for the word “\ *desired”* in output file to find new pitch
   values for each cell.

   ::

     unit cell  =    1
       original pitch                = 1.7340E+00
       Dancoff for orig pitch        = 2.9728E-01
       desired Dancoff               = 3.3600E-01

     pitch to produce desired Dancoff= 1.6845E+00

9. Enter revised pitch and revised moderator density (for cell
   calculation only, not for geometry model) in TSUNAMI model.

.. _7-8-4:

Example Case
------------

The following is a contrived case to illustrate an input file using both
holes, arrays, and multiple sets of Dancoff factors (although both
factors apply to the same pin, so only one set can be used). The case
represents two fuel assemblies in a cylindrical tank, each assembly
having a poisoned central pin, and four water holes. The Dancoff factors
are calculated for each central pin. The input file is listed in
:numref:`list7-8-1`.

.. code-block:: scale
  :name: list7-8-1
  :caption: Example input file (continued below).

  =mcdancoff
  sample case demonstrating calculating Dancoff factors
  xn01
  read composition
    uo2     1  den=10.38  1  294  92234 .0303  92235 4.7378  92236 .1364  92238 95.0955  end uo2
    zirc4   2             1  294  end zirc4
    h2o     3             1  294  end h2o
    uo2     4  den=10.08  1  294  92234 .0303  92235 4.7378  92236 .1364  92238 95.0955  end uo2
    gd      4  den= 0.3   1  294  end gd
  end composition
  read param
    nsk=0 gen=100 npg=300
  end param
  read geometry
    unit 1
      com=!fuel pin!
      cylinder   10  0.395  40.0  -40.0
      cylinder   20  0.410  40.0  -40.0
      cylinder   30  0.470  40.0  -40.0
      cuboid     40  4p0.65  2p40.0
      media      1  1  10
      media      0  1  20 -10
      media      2  1  30 -20
      media      3  1  40 -30
      boundary   40
    unit 2
      com=!water hole!
      cuboid     40  4p0.65  2p40.0
      media      3  1  40
      boundary   40
    unit 3
      com=!unit containing a 2x2 array of fuel pins!
      cuboid     10  4p1.30  2p40.0
      array      1  10  place 1 1 1 -0.65 -0.65 0.0
      boundary   10
    unit 4
      com=!unit containing a 1x2 array of fuel pins!
      cuboid     10  2p0.65  2p1.30  2p40.0
      array      2  10  place 1 1 1 0.0 -0.65 0.0
      boundary   10
    unit 5
      com=!unit containing a 2x1 array of fuel pins!
      cuboid     10  2p1.30  2p0.65  2p40.0
      array      3  10  place 1 1 1 -0.65 0.0 0.0
      boundary   10
    unit 6
      com=!unit containing a 5x5 array of fuel pins!
      cuboid     10  4p3.25  2p40.0
      array      4  10  place 2 2 1 0.0 0.0 0.0
      boundary   10
    unit 7
      com=!unit containing a 5x5 array of fuel pins - water hole in the middle!
      cuboid     10  4p3.25  2p40.0
      array      5  10  place 2 2 1 0.0 0.0 0.0
      boundary   10


::

  unit 8
    com=!unit containing a 5x5 array of fuel pins - poisoned pin in the middle!
    cuboid     10  4p3.25  2p40.0
    array      6  10  place 2 2 1 0.0 0.0 0.0
    boundary   10
  unit 9
    com=!poisoned fuel pin!
    cylinder   10  0.395  40.0  -40.0
    cylinder   20  0.410  40.0  -40.0
    cylinder   30  0.470  40.0  -40.0
    cuboid     40  4p0.65  2p40.0
    media      4  1  10
    media      0  1  20 -10
    media      2  1  30 -20
    media      3  1  40 -30
    boundary   40
  unit 10
    com=!unit containing a 15x15 fuel assembly!
    cuboid     10  4p9.75  2p40.0
    array      7  10  place  2 2 1 0.0 0.0 0.0
    boundary   10
  global
  unit 11
    com=!global unit with 2 fuel assemblies!
    cylinder   10  25.0  60.0  -60.0
    hole       10  origin x=-10.0
    hole       10  origin x= 10.0
    media      3  1  10
    boundary   10
  end geometry
  read array
  ara=1 typ=square nux=2 nuy=2 nuz=1  fill f1 end fill
  ara=2 typ=square nux=1 nuy=2 nuz=1  fill f1 end fill
  ara=3 typ=square nux=2 nuy=1 nuz=1  fill f1 end fill
  ara=4 typ=square nux=3 nuy=3 nuz=1  fill 3 4 3 5 1 5 3 4 3 end fill
  ara=5 typ=square nux=3 nuy=3 nuz=1  fill 3 4 3 5 2 5 3 4 3 end fill
  ara=6 typ=square nux=3 nuy=3 nuz=1  fill 3 4 3 5 9 5 3 4 3 end fill
  ara=7 typ=square nux=3 nuy=3 nuz=1  fill 7 6 7 6 8 6 7 6 7 end fill
  end array
  read start
  ' first Dancoff - calculate for the poisoned fuel pin in unit 9 for the x=-10 assembly
  dancoff
  ' hole 1 is unit 10 at x=-10
    hole 1
  ' array in first region of unit 10 is array 7 - 2 2 1 position is unit 8
    array 1 2 2 1
  ' array in first region of unit 8 is array 6 - 2 2 1 position is unit 9
    array 1 2 2 1
  '  cylinder labeled 10 in unit 9 is the first region
    unit 9   region 1
  ' second Dancoff - calculate for the poisoned fuel pin in unit 9 for the x=+10 assembly
  dancoff
  ' hole 2 is unit 10 at x=+10
    hole 2
  ' array in first region of unit 10 is array 7 - 2 2 1 position is unit 8
    array 1 2 2 1
  ' array in first region of unit 8 is array 6 - 2 2 1 position is unit 9
    array 1 2 2 1
  '  cylinder labeled 10 in unit 9 is the first region
    unit 9   region 1
  end start
  end data
  end


This input file creates two files of Dancoff factors.  The first such file is listed in :numref:`list7-8-2`.

.. code-block:: scale
  :name: list7-8-2
  :caption: Output file of Dancoff factors.

  Unit 9 at global x -1.00000E+01  y  0.00000E+00  z  0.00000E+00
            index        nuclide        dancoff      deviation
                1          92234    2.20873E-01    1.03436E-03
                2          92235    2.20873E-01    1.03436E-03
                3          92236    2.20873E-01    1.03436E-03
                4          92238    2.20873E-01    1.03436E-03
                5           8016    9.64748E-01    4.28121E-04
                6          64000    2.82254E-10    3.61320E-11

The second file is statistically the same, as it solved for the mirror image Dancoff factor.
