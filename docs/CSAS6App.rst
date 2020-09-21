.. _CSAS6App:

Additional Example Applications of CSAS6
========================================

Several example uses of CSAS6 are shown in this section for a variety of applications.

.. _run-KENO-CSAS6:

Run KENO-VI using CSAS6
-----------------------

CSAS6 creates a microscopic working format library and a mixing table
that is passed to KENO-VI. The library is created using
CENTRM/PMC/WORKER to process the cross section data in the resolved
resonance regions of the isotopes contained in the library. CSAS6 then
executes KENO-VI, which calculates *k*\ :sub:`eff` for the problem. The
following examples are for using the multigroup mode of calculation for
KENO-VI. Using the continuous energy mode can be accomplished by simply
changing the library name to one of the continuous energy libraries.

EXAMPLE 1. CSAS6 – Determine the *k*\ :sub:`eff` of a system.

Consider a problem consisting of eight uranium metal cylinders that are
93.2% wt enriched, having a density of 18.76 g/cm\ :sup:`3`. The
cylinders are arranged in a 2 × 2 × 2 array. Each has a radius of
5.748 cm and a height of 10.765 cm. The center-to-center spacing in the
horizontal (X-Y) plane is 13.74 cm and the vertical center-to-center
spacing is 13.01 cm. Because the cross section processing will be done
assuming an infinite homogeneous medium and no cell mixtures are used,
there is no unit cell data. The input data for this problem follow.

.. highlight:: scale

::

  =CSAS6
  SET UP 2C8 IN CSAS6
  V7-238
  READ COMP
  URANIUM  1 DEN=18.76 1 293  92235 93.2 92238 5.6 92234 1.0 92236 0.2 END
  END COMP
  READ PARAMETERS  FLX=YES FDN=YES FAR=YES  END PARAMETERS
  READ GEOMETRY
  UNIT 1
  CYLINDER 10  5.748 5.3825 -5.3825
  CUBOID   20  6.87 -6.87 6.87 -6.87 6.505 -6.505
  MEDIA 1 1 10
  MEDIA 0 1 20 -10
  BOUNDARY 20
  GLOBAL UNIT 2
  CUBOID 10 4P13.74   2P13.010
  ARRAY  1  10  PLACE 1 1 1 -6.87 -6.87 -6.505
  BOUNDARY 10
  END GEOMETRY
  READ ARRAY
  GBL=1 ARA=1 NUX=2 NUY=2 NUZ=2  FILL  F1 END FILL
  END ARRAY
  END DATA
  END

EXAMPLE 2. CSAS6 – Determine the *k*\ :sub:`eff` of an array of fuel pellets in
a UO\ :sub:`2`\ F\ :sub:`2` solution.

Consider a 60 cm inside diameter cylindrical tank filled with
5.0%-enriched UO\ :sub:`2` fuel rods and 5.0%‑enriched
UO\ :sub:`2`\ F\ :sub:`2` solution at 295 gm/liter. A 51 × 51 × 1 array
of fuel rods is centered on the bottom of the tank. The fuel rods are
366 cm long, 0.45 cm in radius, clad with 0.01-cm-thick Al, and at a
pitch of 1.5 cm. The fuel rods sit on the bottom of the container and
the container and solution rise 5.0 cm above the top of the rods. The
container is 10 cm thick in the side and bottom and open at the top.
Determine the *k*\ :sub:`eff` of the system. Input data for this problem
follow.

::

  =CSAS6
  UO2 pins in a UO2F2 solution
  V7-238
  READ COMP
  UO2       1 0.95 300 92235 5.0 92238 95.0 END
  AL        2 1.0  300 END
  SOLNUO2F2 3 295 0.0 1.0 300 92235 5.0 92238 95.0 END
  AL        4 1.0  300 END
  SOLNUO2F2 5 295 0.0 1.0 300 92235 5.0 92238 95.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SQUAREPITCH PITCH=1.50 3 FUELD=0.9  1 CLADD=0.94 2 END
  END CELLDATA
  READ GEOM
  UNIT  1
  COM='FUEL PIN'
  CYLINDER 10  0.45  2P183.0
  CYLINDER 20  0.47 2P183.1
  CUBOID     30  4P0.75 2P183.1
  MEDIA 1 1 10
  MEDIA 2 1 20 -10
  MEDIA 3 1 30 -20 -10
  BOUNDARY 30
  GLOBAL UNIT  2
  COM='FUEL PINS AND SOLUTION IN TANK'
  CUBOID    10  4p38.25  2P183.1
  CYLINDER  20  60.0  188.1 -183.1
  CYLINDER  30  70.0  188.1 -193.1
  ARRAY  1  10  PLACE 26 26 1 3*0.0
  MEDIA  5  1  20 -10
  MEDIA  4  1  30 -20
  BOUNDARY  30
  END GEOM
  READ ARRAY
  ARA=1 NUX=51 NUY=51 NUZ=1 FILL F1 END FILL
  END ARRAY
  END DATA
  END

Run KENO-VI containing cell-weighted mixtures
---------------------------------------------

CSAS6 creates a microscopic working format library and a mixing table
that is passed to KENO-VI. The microscopic cross sections of the
nuclides used in the unit cell geometry description are cell‑weighted by
specifying CELLMIX= followed by a unique mixture number. This mixture
number utilizes the cell-weighted cross sections that represent the
heterogeneous system. CSAS6 executes KENO-VI and calculates *k*\ :sub:`eff` for
the problem.

EXAMPLE 1. CSAS6 – Calculate the *k*\ :sub:`eff` of an array of fuel assemblies
using cell-weighted cross sections.

Consider the 4 × 4 × 1 array of fuel assemblies in a square aluminum
cask described in Sect. 2.2.A.1.1, Example 2. Calculate the *k*\ :sub:`eff` of
the system by using the cell-weighted mixture 200 to represent the fuel
pins in the fuel assembly. Note that mixtures 1, 2, and 3, representing
UO\ :sub:`2`, zirconium, and water, respectively, are used in the unit
cell description. Cell-weighting is applied to the microscopic
cross sections that are used in the cell, making them incorrect for use
elsewhere. Because water is used both inside the cell and between the
fuel assemblies, an additional mixture, mixture 6, has been added to
represent the water between the fuel assemblies. The input data for this
problem follow.

::

  =CSAS6
  SQUARE FUEL CASK EXAMPLE USING HOMOGENEOUS MOCKUP
  V7-238
  READ COMP
  UO2  1 DEN=9.21 1.0 293. 92235 2.35 92238 97.65 END
  ZR   2 1 END
  H2O  3 1 END
  B4C  4 0.367 END
  AL   4 0.636 END
  AL   5 1 END
  H2O  6 1 END
  END COMP
  READ CELLDATA
  LATTICECELL SQUAREPITCH PITCH=1.3 3 FUELD=0.8 1 CLADD=0.94 2 CELLMIX=200 END
  END CELLDATA
  READ PARAM  FAR=YES GEN=253 END PARAM
  READ GEOM
  UNIT  2
  COM='FUEL ASSEMBLY'
  CUBOID  10 4P11.05  2P183.07
  CUBOID  20 4P11.70  2P183.72
  CUBOID  30 4P12.20  2P184.22
  MEDIA  200  1  10
  MEDIA  4  1  20  -10
  MEDIA  6  1  30  -20  -10
  BOUNDARY  30
  GLOBAL  UNIT 3
  COM='FUEL CASK CONTAINING 4X4 ARRAY OF ASSEMBLIES'
  CUBOID  10  4P48.8  2P184.22
  CUBOID  20  4P58.8  2P194.22
  ARRAY  1 10  PLACE 1 1 1 -36.6 -36.6 0.0
  MEDIA  5  1  20 -10
  BOUNDARY  20
  END GEOM
  READ ARRAY
  ARA=1 NUX=4 NUY=4 NUZ=1 FILL F2 END FILL
  END ARRAY
  END DATA
  END

EXAMPLE 2. CSAS6 – Determine the *k*\ :sub:`eff` of an array of fuel pellets in
a UO\ :sub:`2`\ F\ :sub:`2` solution using cell‑weighted cross sections.

This is the same problem as described in :ref:`run-KENO-CSAS6` Example 2.
However, the rods and solutions have been replaced with a cell-weighted
mixture 50. Determine the *k*\ :sub:`eff` of the container. Input data for this
problem follow.

::

  =CSAS6
  UO2 pins in a UO2F2 solution, cell-weighted mixture
  V7-238
  READ COMP
  UO2       1 0.95 300 92235 5.0 92238 95.0 END
  AL        2 1.0  300 END
  SOLNUO2F2 3 295 0.0 1.0 300 92235 5.0 92238 95.0 END
  AL        4 1.0  300 END
  SOLNUO2F2 5 295 0.0 1.0 300 92235 5.0 92238 95.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SQUAREPITCH PITCH=1.50 3 FUELD=0.9 1 CLADD=0.94 2 CELLMIX=50 END
  END CELLDATA
  READ GEOM
  GLOBAL UNIT  2
  COM='FUEL PINS AND SOLUTION IN TANK'
  CUBOID    10  4p38.25  2P183.1
  CYLINDER  20  60.0  188.1 -183.1
  CYLINDER  30  70.0  188.1 -193.1
  MEDIA 50  1  10
  MEDIA  5  1  20 -10
  MEDIA  4  1  30 -20
  BOUNDARY  30
  END GEOM
  END DATA
  END

Run KENO-VI containing multiple unit cells
------------------------------------------

CSAS6 can create a microscopic working format library and a mixing table
that contains more than one unit cell. Each unit cell is explicitly
defined in the CELLDATA section of the standard composition data.
Materials may appear in only one unit cell. All materials in the
standard composition that are not contained in a unit cell are processed
assuming infinite homogeneous media. CSAS6 passes the created working
library to KENO-VI which calculates *k*\ :sub:`eff` for the problem.

EXAMPLE 1. CSAS6 – Calculate the *k*\ :sub:`eff` of a system using two unit
cell descriptions.

Consider an infinite XY-array composed of two types of fuel assemblies
in a checkerboard pattern moderated by water. Each assembly consists of
a 17 × 17 × 1 array of zirconium-clad, enriched UO\ :sub:`2` fuel pins
in a square pitched array. In one array the uranium is 3.5%-enriched and
in the other array the uranium is 2.9%-enriched. The UO\ :sub:`2` has a
density of 9.21 g/cm\ :sup:`3`. The pin diameter is 0.8 cm and is 366 cm
long. The clad is 0.07 cm thick, and the pitch is 1.3 cm. Each fuel
bundle is contained in a 0.65-cm-thick Boral sheath. The bundles are
separated by an edge-to-edge spacing of 1.0 cm. The water and zirconium
is input in the standard composition data once for every unit cell in
which it appears because a material may appear in only one unit cell.
Determine the *k*\ :sub:`eff` of the infinite array. Note that periodic
boundary conditions are required to obtain an infinite checkerboard
array. Input data for this problem follow.

::

  =CSAS6
  2 SQUARE FUEL ASSEMBLIES EXAMPLE IN AN INFINITE LATTICE OF ASSEMBLIES
  V7-238
  READ COMP
  UO2  1  DEN=9.21 1.0 293. 92235 3.5 92238 96.5 END
  ZR   2  1 END
  H2O  3  1 END
  UO2  4  DEN=9.21 1.0 293. 92235 2.9 92238 97.1 END
  ZR   5  1 END
  H2O  6  1 END
  B4C  7  0.367 END
  AL   7  0.636 END
  END COMP
  READ CELLDATA
  LATTICECELL SQUAREPITCH PITCH=1.3 3 FUELD=0.8 1 CLADD=0.94 2 END
  LATTICECELL SQUAREPITCH PITCH=1.3 6 FUELD=0.8 4 CLADD=0.94 5 END
  END CELLDATA
  READ PARAM FAR=YES GEN=253 END PARAM
  READ GEOM
  UNIT  1
  COM='3.5 W% FUEL PIN'
  CYLINDER 10  0.4  2P183.0
  CYLINDER 20  0.47 2P183.07
  CUBOID   30  4P0.65 2P183.07
  MEDIA 1 1 10
  MEDIA 2 1 20 -10
  MEDIA 3 1 30 -20 -10
  BOUNDARY 30
  UNIT  2
  COM='3.5 W% FUEL ASSEMBLY'
  CUBOID  10  4P11.05  2P183.07
  CUBOID  20  4P11.7   2P183.72
  CUBOID  30  4P12.2   2P184.22
  ARRAY  1 10  PLACE 9 9 1 3*0.0
  MEDIA  7  1  20 -10
  MEDIA  3  1  20 -20 -20
  BOUNDARY  30
  UNIT  3
  COM='2.9 W% FUEL PIN'
  CYLINDER 10  0.4  2P183.0
  CYLINDER 20  0.47 2P183.07
  CUBOID   30  4P0.65 2P183.07
  MEDIA 4 1 10
  MEDIA 5 1 20 -10
  MEDIA 6 1 30 -20 -10
  BOUNDARY 30
  UNIT   4
  COM='2.9 W% FUEL ASSEMBLY'
  CUBOID  10  4P11.05  2P183.07
  CUBOID  20  4P11.7   2P183.72
  CUBOID  30  4P12.2   2P184.22
  ARRAY  2 10  PLACE 9 9 1 3*0.0
  MEDIA  7  1  20 -10
  MEDIA  6  1  20 -20 -20
  BOUNDARY  30
  GLOBAL  UNIT 5
  COM='FUEL CASK CONTAINING 4X4 ARRAY OF ASSEMBLIES'
  CUBOID   10  4P24.4  2P184.22
  ARRAY  3 10  PLACE  1 1 1 -12.2  -12.2  0.0
  BOUNDARY 10
  END GEOM
  READ ARRAY
  ARA=1 NUX=17 NUY=17 NUZ=1 FILL F1 END FILL
  ARA=2 NUX=17 NUY=17 NUZ=1 FILL F3 END FILL
  GBL=3 ARA=3 NUX=2 NUY=2 NUZ=1 FILL 2 4 4 2 END FILL
  END ARRAY
  READ BOUNDS XYF=PERIODIC END BOUNDS
  END DATA
  END

EXAMPLE 2. CSAS6 – Calculate the *k*\ :sub:`eff` of a system using two unit
cell descriptions and cell-weighted mixtures.

Consider a problem in which a stainless steel cylinder with an inner
diameter of 56 cm and an inside height of 91 cm is filled with pellets
of UO\ :sub:`2` in borated water. The steel is 0.125 cm thick. The
spherical 2.57%-enriched UO\ :sub:`2` pellets have a diameter of 1.07 cm
and are arranged in a triangular pitch array with a pitch of 1.13 cm.
The spherical 2.96%-enriched UO\ :sub:`2` pellets have a diameter of
1.07 cm and are arranged in a triangular pitch array with a pitch of
1.12 cm. The cylindrical tank is filled half full of the 2.96% pellets
in borated water, and the remainder is filled with the 2.57%-enriched
pellets in borated water.

Mixture 100 is the cell-weighted mixture containing the 2.57%-enriched
uranium pellets and mixture 200 is the cell-weighted mixture containing
the 2.96%-enriched uranium pellets. Determine the *k*\ :sub:`eff` of this
system. Input data for this problem follow.

::


  =CSAS6
  2.57% AND 2.96% ENR UO2 PELLETS IN 3500 PPM BORATED WATER
  V7-238
  READ COMP
  UO2    1 0.925  283 92235 2.57 92238 97.43 END
  H2O    2 1.0 283 END
  ATOMBACID 2 2.0017-2 3 5000 1 1001 3 8016 3 1.0 283 END
  UO2    3 0.925  283 92235 2.96 92238 97.04 END
  H2O    4 1.0 283 END
  ATOMBACID 4 2.0017-2 3 5000 1 1001 3 8016 3 1.0 283 END
  SS304 5 1.0 283 END
  END COMP
  READ CELLDATA
  LATTICECELL CELLMIX=100 SPHTRIANGP PITCH=1.13 2 FUELD=1.07 1 END
  LATTICECELL CELLMIX=200 SPHTRIANGP PITCH=1.13 4 FUELD=1.07 3 END
  END CELLDATA
  READ PARAM  FLX=YES   END PARAM
  READ GEOM
  GLOBAL UNIT 1
  CYLINDER 10 38.0 45.5 0.0
  CYLINDER 20 38.0 91.0 0.0
  CYLINDER 30 38.125 91.0 -0.125
  MEDIA 100 1 10
  MEDIA 200 1 20 -10
  MEDIA   5 1 30 -20
  BOUNDARY 30
  END GEOM
  END DATA
  END
