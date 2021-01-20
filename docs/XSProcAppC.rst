.. _7-1c:

Examples of Complete XSProc Input Data
======================================

.. _7-1c-1:

Infinite homogeneous medium input data
--------------------------------------

Examples of XSProc input data for infinite homogeneous media problems
are given below. In these cases the cross section library name “fine_n”
indicates that the latest recommended fine-group SCALE library will used
in the calculations.

EXAMPLE 1. Default cell definition.


   Consider a cylindrical billet of 20 wt % enriched UO\ :sub:`2`,
   having a density of 10.85 g/cm\ :sup:`3` that is 26 cm in diameter
   and 26 cm tall.

The average mean-free path in the uranium dioxide is on the order of
2.5 cm. Because only a small fraction of the billet is within a
mean-free path of the surface, the material can be treated as an
infinite homogeneous medium; therefore the CELL DATA block can be
omitted. The XSProc data follows:

.. highlight:: scale

::

  20%  ENRICHED  UO2  BILLET
  fine_n
  READ COMP
  UO2  1  0.99  293  92235  20  92238  80  END
  END  COMP

The volume fraction used for the UO\ :sub:`2`, 0.99, is calculated by
dividing the actual density by the theoretical density obtained from the
*Isotopes in standard composition library* table in the STDCMP chapter,
(10.85/10.96). Since the enrichment was specified as 20%, it is assumed
that the remainder is :sup:`238`\ U.

An alternative input data description follows:

::

  20% ENRICHED UO2 BILLET
  fine_n
  READ COMP
  UO2 1 DEN=10.85  1  293  92235  20  92238  80  END
  END COMP

EXAMPLE 2. Specify the cell definition.


   Consider a 5-liter Plexiglas bottle with an inner radius of 9.525 cm
   and inner height of 17.78 cm that is filled with highly enriched
   uranyl nitrate solution at 415 g/L and 0.39 mg of excess nitrate per
   gram of solution. The uranium isotopic content of the nitrate
   solution is 92.6 wt % :sup:`235`\ U, 5.9 wt % :sup:`238`\ U, 1.0 wt %
   :sup:`234`\ U, and 0.5 wt % :sup:`236`\ U. Solution density will be
   calculated from the given data.

The size of the nitrate solution is on the order of 16 to 20 cm in
diameter and height. The average mean-free path in the nitrate solution
is on the order of 0.5 cm. Therefore, infinite homogeneous medium is an
appropriate choice for this problem. By default BONAMI is used for
self-shielding the infinite medium of Plexiglas, while CENTRM is used to
shield the infinite medium fissile solution.

::

  SET UP 5 LITER URANYL NITRATE SOLUTION IN A PLEXIGLAS CONTAINER
  fine_n
  READ COMP
  PLEXIGLAS   1  END
  SOLUTION   MIX=2   RHO[UO2(NO3)2]=415
             92235   92.6   92238   5.9   92236   0.5
  END SOLUTION
  END  COMP
  READ CELLDATA
  INFHOMMEDIUM  2  END
  END CELLDATA

.. _7-1c-2:

LATTICECELL input data
----------------------

Examples of XSProc input data for **LATTICECELL** problems are given
below.

EXAMPLE 1. SQUAREPITCH ARRAY.


   Consider an infinite planar array (infinite in X and Y and one layer
   in Z) of 20 wt % enriched U metal rods with a 1-cm pitch. Each fuel
   rod is bare uranium metal, 0.75 cm OD × 30.0 cm long. The rods are
   submerged in water.

Because the diameter of the fuel rod, 0.75 cm, is only slightly larger
than the average mean-free path in the uranium metal, approximately 0.5,
and because the configuration is a regular array, **LATTICECELL** is the
appropriate choice for proper cross-section processing. The *parm* field
is not provided, so the default CENTRM/PMC self-shielding method is
used. XSProc data follows:

::

  INFINITE  PLANAR  ARRAY  OF  20%  U  METAL  RODS
  fine_n
  READ COMP
  URANIUM  1  1  293  92235  20  92238  80  END
  H2O      2  END
  END  COMP
  READ CELLDATA
  LATTICECELL  SQUAREPITCH   PITCH=1.0  2  FUELD=0.75  1  END
  END CELLDATA

Since the MORE DATA and CENTRM DATA blocks were omitted, default options
will be used in the self-shielding calculations. The default CENTRM/PMC
computation options for a square pitch lattice cell are the
method-of-characteristics (MoC) method with P0 scatter in CENTRM
calculations.

EXAMPLE 2. SQUAREPITCH PWR LATTICE.


   Consider an infinite, uniform planar array (infinite in X and Y and
   one layer in Z) of PWR-like fuel pins of 2.35% enriched UO\ :sub:`2`
   clad with zirconium. The density of the UO\ :sub:`2` is
   9.21 g/cm\ :sup:`3`. The fuel in each pin is 0.823 cm in diameter,
   the clad is 0.9627 cm in diameter, and the length of each pin is
   366 cm. The fuel pins are separated by 0.3124 cm of water in the
   horizontal plane.

**LATTICECELL** is the appropriate choice for cross-section processing.
Assume that all defaults are appropriate; thus the CENTRM/PMC
methodology is used, and the MORE DATA and CELL DATA blocks are not
entered. The input cross section library named “broad_n” indicates that
the recommended broad group SCALE library will be used. In this case
CENTRM uses the 2D MoC transport solver. The XSProc data follows:

::

  PWR-LIKE FUEL BUNDLE; uniform infinite array model.
  broad_n
  READ COMP
  UO2   1  .84  293.  92235  2.35  92238  97.65  END
  ZR    2  1  END
  H2O   3  1  END
  END  COMP
  READ CELLDATA
  LATTICECELL  SQUAREPITCH  PITCH=1.2751  3  FUELD=0.823  1  CLADD=0.9627  2  END
  END CELLDATA

EXAMPLE 3. SQUAREPITCH PWR LATTICE, with non-uniform Dancoff.


This example is a single PWR assembly of fuel pins of the type described
above, contained in a water pool. The interior pins in the assembly can
be self-shielded using the same uniform, infinite lattice model in
previous example. However self-shielding of the outer boundary-edge pins
will be modified to account for being adjacent to a water reflector,
rather than surrounded on all sides by similar pins. This requires that
the MCDancoff module be executed previously to obtain non-uniform
Dancoff factors for the edge pins. The average edge-pin value of 0.61 is
used to represent Dancoff factors of all boundary pins. The default
CENTRM MoC transport solver is used for both cells, but the original
pitch of 1.2751 cm for the second cell (i.e., boundary pin) is modified
to a new pitch corresponding to a Dancoff value of 0.61.

::

  PWR-LIKE FUEL BUNDLE, with boundary-pin corrections
  broad_n
  READ COMP
  ' mixtures for interior pins
  UO2   1  .84  293.  92235  2.35  92238  97.65  END
  ZR    2  1  END
  H2O   3  1  END
  ' mixtures for boundary pins
  UO2   4  .84  293.  92235  2.35  92238  97.65  END
  ZR    5  1  END
  H2O   6  1  END
  END  COMP
  READ CELLDATA
  LATTICECELL  SQUAREPITCH PITCH=1.2751 3 FUELD=0.823 1 CLADD=0.9627 2  END
  LATTICECELL  SQUAREPITCH PITCH=1.2751 6 FUELD=0.823 4 CLADD=0.9627 5  END
    CENTRM DATA  DAN2PITCH=0.61    END CENTRM
  END CELLDATA

EXAMPLE 6. SPHTRIANGP ARRAY.


   Consider an infinite array of spherical pellets of 2.67% enriched
   UO\ :sub:`2` with a density of 10.3 g/cm\ :sup:`3` and a diameter of
   1.0724 cm arranged in a “triangular” pitch, flooded with borated
   water at 4350 ppm. The boron is natural boron; the borated water is
   created by adding boric acid, H\ :sub:`3`\ BO\ :sub:`3`, and has a
   density of 1.0078 g/cm\ :sup:`3`. The temperature is 15ºC and the
   pitch is 1.1440 cm. The standard composition data for the borated
   water are given in Example 2 of :ref:`7-1a-9`.

Because the diameter of the fuel pellet, 1.0724 cm, is smaller than the
average mean-free path in the UO\ :sub:`2`, approximately 1.5 cm, and
because the configuration is a regular array, **LATTICECELL** is the
appropriate choice for proper cross-section processing.

The density fraction for the UO\ :sub:`2` is the ratio of actual to
theoretical density (10.3/10.96 = 0.9398). Assume that the U is all
:sup:`235`\ U and :sup:`238`\ U. See :ref:`7-1a-9` for how to define
borated water.

The XSProc data follows:

::

  SPHERICAL  PELLETS  IN  BORATED  WATER
  fine_n
  READ COMP
  UO2   1  .9398  288  92235  2.67  92238  97.33  END
  ATOMH3BO3  2  0.025066  3  5000  1  1001  3  8016  3
         1.0  288  END
  H2O   2  0.984507  288  END
  END  COMP
  READ CELLDATA
  LATTICECELL  SPHTRIANGP  PITCH=1.1440  2  FUELD=1.0724  1  END
  END CELLDATA

.. _7-1c-3:

MULTIREGION input data
----------------------

Examples of XSProc input data for **MULTIREGION** problems are given
below.

EXAMPLE 1. SPHERICAL.


   Consider a small highly enriched uranium sphere supported by a
   Plexiglas collar in a tank of water. The uranium metal sphere has a
   diameter of 13.1075 cm, is 97.67% enriched, and has a density of
   18.794 g/cm\ :sup:`3`. The cylindrical Plexiglas collar has a
   4.1275-cm-radius central hole, extends to a radius of 12.7 cm and is
   2.54 cm thick. The water filled tank is 60 cm in diameter.

The density fraction of the uranium metal is the ratio of actual to
theoretical density, where the theoretical density is obtained from the
*Isotopes in standard composition library* table in section 7.2.1. Thus,
the density multiplier is 18.794/19.05 = 0.9866. The abundance of
uranium is not stated beyond 97.67% enriched, so it is reasonable to
assume the remainder is :sup:`238`\ U. The Plexiglas collar is not
significantly different from water and does not surround the fuel, so it
can be ignored. If it is ignored, the problem becomes a 1-D geometry
that can be defined using the **MULTIREGION** type of calculation, and
the eigenvalue of the system can be obtained without additional data by
executing CSAS1. However, the Plexiglas has been included in this data
so it can be passed to a code such as KENO V.a which can describe the
geometry rigorously. The XSProc data follow:

::

  SMALL  WATER  REFLECTED  SPHERE  ON  PLEXIGLAS  COLLAR
  fine_n
  READ COMP
  URANIUM    1  .9866  293.  92235  97.67  92238  2.33  END
  PLEXIGLAS  2  END
  H2O        3  END
  END  COMP
  READ CELLDATA
  MULTIREGION SPHERICAL RIGHT_BDY=VACUUM END 1 6.55375 3 30.0 END ZONE
  END CELLDATA

EXAMPLE 2. BUCKLEDSLAB.


   This example features a 93.2% enriched uranyl-fluoride solution
   inside a rectangular Plexiglas container immersed in water. The
   fissile solution contains 578.7 g of UO\ :sub:`2`\ F\ :sub:`2` per
   liter and has no excess acid. The critical thickness of the fuel is
   5.384 cm. The finite height of the fuel slab is 147.32 cm, and the
   depth is 71.58 cm. The Plexiglas container is 1.905 cm thick and is
   reflected by 20.32 cm of water.

The half thickness of the fuel (2.692) will be used with a reflected
left boundary and a vacuum right boundary (default). The XSProc data
follow:

::

  CRITICAL SLAB EXPERIMENT USING URANYL-FLUORIDE SOLUTION
  fine_n
  READ COMP
  SOLUTION  MIX=1  RHO[UO2F2]=578.7
            92235  93.2  92238  6.8  TEMP=300
  END SOLUTION
  PLEXIGLAS  2  END
  H2O        3  END
  END  COMP
  READ CELLDATA
  MULTIREGION  BUCKLEDSLAB  LEFT_BDY=REFLECTED
  DY=71.58 DZ=147.32  END  1  2.692  2  4.597  3  24.917  END ZONE
  END CELLDATA

.. _7-1c-4:

DOUBLEHET input data
--------------------

EXAMPLE 1: A doubly-heterogeneous spherical fuel element with 15,000 UO\ :sub:`2` particles in a graphite matrix.


   Grain fuel radius is 0.025 cm. Grain contains one coating layer that
   is 0.009-cm-thick. Pebbles are in a triangular pitch on a
   6.4-cm-pitch. Fuel pebble fuel zone is 2.5‑cm in radius and contains
   a 0.5-cm-thick graphite clad that contains small amounts of
   :sup:`10`\ B. Pebbles are surrounded by :sup:`4`\ He. In this case we
   designated the homogenized mixture as mixture 10. If we have a
   KENO V.a or KENO-VI input section, we would use mixture 10 in that
   section. Note that the keyword “FUELR=” is followed by the fuel
   dimension only, i.e., no mixture number. That is because the fuel
   mixture number is specified with “FUELMIX=” and therefore need not be
   repeated.

::

  INFINITE ARRAY OF UO2-FUELLED PEBBLES
  fine_n
  READ COMP
  ' UO2 FUEL KERNEL
  U-235  1 0 1.92585E-3 293.6 END
  O      1 0 4.64272E-2 293.6 END
  ' FIRST COATING
  C      2 0 5.26449E-2 293.6 END
  ' GRAPHITE MATRIX
  C      6 0 8.77414E-2 293.6 END
  ' CARBON PEBBLE OUTER COATING
  C      7 0 8.77414E-2 293.6 END
  B-10   7 0 9.64977E-9 293.6 END
  HE-4   8 0 2.65156E-5 293.6 END
  END COMP
  READ CELLDATA
  DOUBLEHET  RIGHT_BDY=WHITE FUELMIX=10 END
   GFR=0.025  1 COATT=0.009 2 MATRIX=6 NUMPAR=15000 END GRAIN
  PEBBLE SPHTRIANGP RIGHT_BDY=WHITE HPITCH=3.2 8 FUELR=2.5 CLADR=3.0 7  END
  END CELLDATA

EXAMPLE 2: A doubly-heterogeneous spherical fuel element with 10,000 UO\ :sub:`2` particles and 5,000 PuO\ :sub:`2` particles in a graphite matrix.


   Grain fuel radii for UO\ :sub:`2` and PuO\ :sub:`2` particles are
   0.025 cm and 0.012 cm, respectively. UO\ :sub:`2` grains contain one
   coating layer that is 0.009‑cm-thick. PuO\ :sub:`2` grains contain
   one coating layer that is 0.0095-cm-thick. Pebbles are in a
   triangular pitch on a 6.4-cm-pitch. Fuel pebble fuel zone is 2.5-cm
   in radius and contains a 0.5-cm-thick graphite clad that contains
   small amounts of :sup:`10`\ B. Pebbles are surrounded by
   :sup:`4`\ He. Since number of particles is entered, the total volume
   fraction and the pitch can be calculated by the code.

::

  INFINITE ARRAY OF UO2- AND PUO2-FUELLED PEBBLES
  fine_n
  READ COMP
  ' UO2 FUEL KERNEL
  U-235  1 0 1.92585E-3 293.6 END
  O      1 0 4.64272E-2 293.6 END
  ' FIRST COATING
  C      2 0 5.26449E-2 293.6 END
  ' GRAPHITE MATRIX
  C      6 0 8.77414E-2 293.6 END
  ' CARBON PEBBLE OUTER COATING
  C      7 0 8.77414E-2 293.6 END
  B-10   7 0 9.64977E-9 293.6 END
  HE-4   8 0 2.65156E-5 293.6 END
  ' PUO2 FUEL KERNEL
  PU-239  11 0 1.24470E-02 293.6 END
  O       11 0 4.60983E-02 293.6 END
  ' FIRST COATING
  C      12 0 5.26449E-2 293.6 END
  ' GRAPHITE MATRIX
  C      16 0 8.77414E-2 293.6 END
  END COMP
  READ CELLDATA
  DOUBLEHET  RIGHT_BDY=WHITE FUELMIX=10 END
   GFR=0.025  1 COATT=0.009 2 MATRIX=6 NUMPAR=10000 END GRAIN
   GFR=0.012 11 COATT=0.0095 12 MATRIX=16 NUMPAR=5000 END GRAIN
  PEBBLE SPHTRIANGP RIGHT_BDY=WHITE HPITCH=3.2 8 FUELR=2.5 CLADR=3.0 7 END
  END CELLDATA

EXAMPLE 3: A doubly-heterogeneous slab fuel element with flibe salt coolant


   Grain fuel radii for UO\ :sub:`2` particles are 0.025 cm. The
   UO\ :sub:`2` grains contain four coating layers with thicknesses of
   0.01, 0.0035, 0.003, and 0.004 cm, respectively. The fuel grains are
   embedded in a carbon matrix material to form the fuel compact. The
   x-dimension of fuel plate consists of a 0.5 cm (half-thickness) fuel
   compact region, a carbon clad with outer dimension of 1.27, followed
   by the flibe coolant with an outer reflected dimension of 1.62 cm.
   The width (y-dimension) of the slab plate is 22.5 cm and the height
   (z-dimension) is 500 cm. The y and z dimensions are only used to
   define volumes for the fuel plate.

::

  slab doublehet sample problem: double-het for slab
  v7.1-252n
  read comp
  ' fuel kernel
  u-238  1 0 2.12877e-2 293.6 end
  u-235  1 0 1.92585e-3 293.6 end
  o      1 0 4.64272e-2 293.6 end
  b-10   1 0 1.14694e-7 293.6 end
  b-11   1 0 4.64570e-7 293.6 end
  ' first coating
  c      2 0 5.26449e-2 293.6 end
  ' inner pyro carbon
  c      3 0 9.52621e-2 293.6 end
  ' silicon carbide
  c      4 0 4.77240e-2 293.6 end
  si     4 0 4.77240e-2 293.6 end
  ' outer pyro carbon
  c      5 0 9.52621e-2 293.6 end
  ' graphite matrix
  c      6 0 8.77414e-2 293.6 end
  b-10   6 0 9.64977e-9 293.6 end
  b-11   6 0 3.90864e-8 293.6 end
  ' carbon slab outer coating
  c      7 0 8.77414e-2 293.6 end
  b-10   7 0 9.64977e-9 293.6 end
  b-11   7 0 3.90864e-8 293.6 end
  Li-6         8    0   1.38344E-06   948.15  end
  Li-7         8    0   2.37205E-02   948.15  end
  Be           8    0   1.18609E-02   948.15  end
  F            8    0   4.74437E-02   948.15  end
  end comp
  read celldata
    doublehet  fuelmix=10 end
      gfr=0.02135   1
      coatt=0.01    2
      coatt=0.0035  3
      coatt=0.003   4
      coatt=0.004   5
      vf=0.4
      matrix=6
      end grain
    slab symmslabcell
      hpitch=1.62   8
      cladr=1.27    7
      fuelr=0.5
      fuelh=500
      fuelw=22.500
    end
    centrm data ixprt=1 isn=8 end centrm
  end celldata



EXAMPLE 4: A doubly-heterogeneous triangular-pitch fuel element with 1,302 UO\ :sub:`2` particles in a graphite matrix with the DAN2PITCH option for grain.


    Grain fuel radius for UO2 particles are 0.02125 cm.  The UO2 grains contain four
    coating layers with radii of 0.03125, 0.03525, 0.03875, and 0.04275 cm,
    respectively.  The fuel grains are embedded in a carbon matrix material to form
    the fuel compact.    Fuel compact is in a triangular pitch on a 1.8796-cm-pitch.
    Fuel zone is 0.6225-cm in radius and there is a 0.0125 cm gap between fuel and
    graphite moderator. Since number of particles is entered, the total volume
    fraction and the pitch can be calculated by the code. Dancoff factor of 0.6552
    is inputted for a grain to consider neutron leakage effect.

::

  DH_dan2pitch_nonuniform
  v7.1-252
  read composition
   u-235       1 0 3.6676E-03   600.0   end
   u-238       1 0 1.9742E-02   600.0   end
   o-16        1 0 3.5114E-02   600.0   end
   c           1 0 1.1705E-02   600.0   end
   c           2 0 5.2646E-02   600.0   end
   c           3 0 9.5263E-02   600.0   end
   si-28       4 0 4.4159E-02   600.0   end
   si-29       4 0 2.2433E-03   600.0   end
   si-30       4 0 1.4805E-03   600.0   end
   c           4 0 4.7883E-02   600.0   end
   c           5 0 9.5263E-02   600.0   end
   c-graphite  6 0 7.2701E-02   600.0   end
   he          7 0 2.4006E-05   600.0   end
   c-graphite  8 0 9.2756E-02   600.0   end
  end composition

  read celldata
   doublehet  fuelmix=9 end
    gfr=0.02125   1
    coatr=0.03125 2
    coatr=0.03525 3
    coatr=0.03875 4
    coatr=0.04275 5
    numpar=1302
    matrix=6  end grain
   centrm data alump=0.0 dan2pitch=0.6562 end centrm
   rod triangpitch
    fuelr=0.6225
    gapr=0.635 7
    hpitch=0.9398 8
    fuelh=1.000
    right_bdy=white left_bdy=reflected end
   centrm data iup=12 isn=16  alump=0.0  end centrm
  end celldata


.. _7-1c-5:

Two methods of specifying a fissile solution
--------------------------------------------

The standard composition specification data offer flexibility in the
choice of input data. This section illustrates two methods of specifying
the same fissile solution.

Create a mixture 3 that is aqueous uranyl nitrate solution:

   UO\ :sub:`2`\ (NO\ :sub:`3`)\ :sub:`2`, solution density = 1.555 g
   cm\ :sup:`3`/

   0.2669 g U/g-soln., 0.415 g U/ cm\ :sup:`3`; excess nitrate =
   0.39 mg/g-soln

   Uranium isotopic content: 92.6 wt % U-235 5.9 wt % U-238

   1.0 wt % U-234 and 0.5 wt % U-236

The SCALE atomic weights used in this problem are listed as follows:

   H 1.0078

   O 15.999

   N 14.0067

   U-234 234.041

   U-235 235.0439

   U-236 236.0456

   U-238 238.0508

Two methods of describing the uranyl nitrate solution will be demonstrated.
Method 1 is more rigorous, and method 2 is easier and as accurate.

.. centered:: METHOD 1:


This method involves breaking the solution into its component parts
[(HNO\ :sub:`3`, UO\ :sub:`2`\ (NO\ :sub:`3`)\ :sub:`2`, and
H\ :sub:`2`\ O)] and entering the basic standard composition
specifications for each.

1. Calculate the density of the HNO\ :sub:`3` 0.39 × 10\ :sup:`−3` g
   NO\ :sub:`3`/g soln × [(62.997 g HNO\ :sub:`3`/mole
   HNO\ :sub:`3`)/(61.990 g NO\ :sub:`3`/mole NO\ :sub:`3`)] × 1.555 g
   soln/ cm\ :sup:`3`\ soln = 6.16 × 10\ :sup:`−4` g HNO\ :sub:`3`/cc
   soln.

2. Calculate the density fraction of HNO\ :sub:`3` (actual
   density/theoretical density). In the Standard Composition Library the
   theoretical density of HNO\ :sub:`3` is 1.0. 6.16 × 10\ :sup:`−4`/1.0
   = 6.16 × 10\ :sup:`−4`.

3. Calculate the molecular weight of the uranium

..

   The number of atoms in a mole of uranium is the sum of the number of
   atoms of each isotope in the mole of uranium.

   Let AU = the average molecular weight of uranium, g U/mole U

   GU = the density of uranium in g/cm\ :sup:`3`.

   Then the number of atoms in a mol of uranium =

   (6.023 × 10\ :sup:`+23` \* 10\ :sup:`−24` \* GU)/AU

   or 0.6023 \* GU/AU.

   The weight fraction of each isotope is the weight % \* 100.

   Therefore, F235 = 0.926, the weight fraction of U-235 in the U

   F238 = 0.059, the weight fraction of U-238 in the U

   F236 = 0.005, the weight fraction of U-236 in the U

   F234 = 0.010, the weight fraction of U-234 in the U

   A235 = 235.0442, the molecular weight of U-235

   A238 = 238.0510, the molecular weight of U-238

   A236 = 236.0458, the molecular weight of U-236

   A234 = 234.0406, the molecular weight of U-234.

   Then the number of atoms of isotopes in a mol of uranium =

   6.023 × 10\ :sup:`+23` \* 10\ :sup:`−24` \* ( (GU*F235/A235) +
   (GU*F238/A238) +

   GU*F236/A236) + (GU*F234/A234) )

   or

   0.6023*GU \* ( 0.926/235.0442 + 0.059/238.0510 +

   0.005/236.0458 + 0.010/234.0406 ).

   Because the number of atoms of uranium equals the sum of the atoms of
   isotopes,

   0.6023 \* GU/AU = 0.6023 \* GU \*( 0.926/235.0442 + 0.059/238.0510 +

   0.005/236.0458 + 0.010/234.0406 )

   1/AU = 0.926/235.0442 + 0.059/238.0510 + 0.005/236.0458 +
   0.010/234.0406

   AU = 235.2144.

4. Calculate the molecular weight of the
   UO\ :sub:`2`\ (NO\ :sub:`3`)\ :sub:`2`.

..

   235.2144 + (8 × 15.9954) + (2 × 14.0033) = 391.184 g
   UO\ :sub:`2`\ (NO\ :sub:`3`)\ :sub:`2`/mole

5. Calculate the density of UO\ :sub:`2`\ (NO\ :sub:`3`)\ :sub:`2`

..

   0.415 g U/cc × [(391.184 g
   UO\ :sub:`2`\ (NO\ :sub:`3`)\ :sub:`2`/mol)/(235.2144 g U/mole)] =

   0.69018 g UO\ :sub:`2`\ (NO\ :sub:`3`)\ :sub:`2`/ cm\ :sup:`3`.soln.

Calculate the density fraction (actual density/theoretical density) of
UO\ :sub:`2`\ (NO\ :sub:`3`)\ :sub:`2`.

   [In the Standard Composition Library the theoretical density of
   UO\ :sub:`2`\ (NO\ :sub:`3`)\ :sub:`2` is given as
   2.2030 g/cm\ :sup:`3`.]

   The density fraction is 0.69018/2.2030 = 0.31329.

6. Calculate the amount of water in the solution

..

   1.555 g soln/ cm\ :sup:`3`. soln − 6.16 × 10\ :sup:`−4` g
   HNO\ :sub:`3`/cm\ :sup:`3` soln − 0.69018 g
   UO\ :sub:`2`\ (NO\ :sub:`3`)\ :sub:`2`\ LL/ cm\ :sup:`3`. soln =
   0.8642 g H\ :sub:`2`\ O/cc soln.

7. Calculate the density fraction (actual density/theoretical density)
   of water.

::

  HNO3       3   6.16-4   293  END
  UO2(NO3)2  3  .31329  293  92235  92.6  92238  5.9  92234  1.0
                     92236   0.5  END
  H2O        3    .86575  293  END

.. centered:: METHOD 2:

This method utilizes the solution option available in the standard
composition specification data. Because the density is specified in the
input data, this method should yield correct number densities that
should agree with method 1 except for calculational round-off.

1. Calculate the fuel density

..

   0.415 g U/cc is 415 g U/L.

2. The molecular weight of nitrate NO\ :sub:`3` is 61.9895.

3. Calculate the molarity of the solution.

..

   0.39 mg nitrate/g soln × 1000 cm\ :sup:`3`\ soln/L soln × 1 g/1000 mg
   × 1.555 g soln/ cm\ :sup:`3`\ soln = 0.60645 g excess nitrate/L soln.

   A 1-molar solution is 1 mole of acid/L of solution:

   (For nitric acid 1 molar is 1 normal because there is only one atom
   of hydrogen per molecule of acid in HNO\ :sub:`3`.)

   (0.60645 g nitrate/L soln)/(61.9895 g NO\ :sub:`3`/mole NO\ :sub:`3`)
   = 9.783 × 10\ :sup:`−3` mole nitrate/L is identical to mole of
   acid/L, which is identical to molarity.

4. The density fraction of the solution is 1.0. Do not try to use the
   density of the solution divided by the theoretical density of
   UO\ :sub:`2`\ (NO\ :sub:`3`)\ :sub:`2` from the Standard Composition
   Library for your density multiplier. The
   UO\ :sub:`2`\ (NO\ :sub:`3`)\ :sub:`2` listed there is the solid, not
   the solution.

..

   The solution specification data follow:

::

  SOLUTION 	MIX=1	RHO[UO2(NO3)2] = 415	92235	92.6	92238	5.9
  			92234	 1.0	92236	0.5
  		MOLAR [HNO3] = 9.783-3
  		TEMP = 293	DENSITY = 1.555	END SOLUTION

.. centered:: Comparison of number densities from the two methods

The number densities of methods 1 and 2 should agree within the limits
of the input data. The density multipliers in method 1 are 5 digits and
the density multipliers in method 2 are 4 digits. Therefore, the number
densities calculated by the two methods should agree to 4 or 5 digits.

+----------------+--------------+--------------+
|                | Method 1     | Method 2     |
+----------------+--------------+--------------+
| Nuclide number | Atom density | Atom density |
+----------------+--------------+--------------+
| 92235          | 9.84603E−04  | 9.84603E−04  |
+----------------+--------------+--------------+
| 92238          | 6.19415E−05  | 6.19415E−05  |
+----------------+--------------+--------------+
| 92234          | 1.06784E−05  | 1.06784E−05  |
+----------------+--------------+--------------+
| 92236          | 5.29387E−06  | 5.29387E−06  |
+----------------+--------------+--------------+
| 07014          | 2.13092E−03  | 2.13092E−03  |
+----------------+--------------+--------------+
| 08016          | 3.74135E−02  | 3.7410E−02   |
+----------------+--------------+--------------+
| 01001          | 5.77973E−02  | 5.77983E−02  |
+----------------+--------------+--------------+

.. _7-1c-6:

Multiple unit cells in a single problem
---------------------------------------

Consider a problem that involves three different UO\ :sub:`2` fuel
assemblies: a 1.98%-enriched assembly, a 2.64%-enriched assembly, and a
2.96%-enriched assembly. All fuel rods are UO\ :sub:`2` at
10.138 g/cm\ :sup:`3` and are 0.94 cm in diameter. The Zircaloy-4 clad
has an inside radius of 0.4875 cm and an outside radius of 0.545 cm. The
rod pitch is 1.44 cm. Each fuel assembly is a 15 × 15 array of fuel pins
with water holes, instrumentation holes, and burnable poison rods. For
cross-section processing, the presence of the water holes,
instrumentation holes, and burnable poison rods in the assemblies are
ignored.

The following XSProc input use the CENTRM/PMC method for self-shielding
three latticecells with different fuel enrichments. The remaining
mixture (SS-304), not specified in a unit cell, is processed as an
infinite homogeneous medium using the BONAMI method. Each mixture can
appear only in a single zone of one unit cell. For square pitch
latticecells the default CENTRM transport solver is MoC with P0 scatter;
however in this input, the solver for the 3\ :sup:`rd` cell is modified
through CENTRM DATA to use the two-region approximation for the CE
calculation [npxs=5], and discrete S\ :sub:`N` transport calculation
with P1 anisotropic scatteringfor the MG solutions in the fast and
thermal energy ranges [nfst=0, nthr=0].

::

  DEMONSTRATION PROBLEM WITH MULTIPLE RESONANCE CORRECTIONS REQUIRED
  broad_n
  READ COMP
  UO2        1  .925    300  92235  1.98  92238  98.02  END
  UO2        2  .925    300  92235  2.64  92238  97.36  END
  UO2        3  .925    300  92235  2.96  92238  97.04  END
  ZIRC4      4  1.0     300  END
  H2O        5  1.0     300  END
  ZIRC4      6  1.0     300  END
  H2O        7  1.0     300  END
  ZIRC4      8  1.0     300  END
  H2O        9  1.0     300  END
  SS304     10  1.0     300  END
  END  COMP
  READ CELLDATA
  LATTICECELL SQUAREPITCH PITCH=1.44 5 FUELD=0.94  1 CLADD=1.09  4 GAPD=0.975  0 END
  LATTICECELL SQUAREPITCH PITCH=1.44 7 FUELD=0.94  2 CLADD=1.09  6 GAPD=0.975  0 END
  LATTICECELL SQUAREPITCH PITCH=1.44 9 FUELD=0.94  3 CLADD=1.09  8 GAPD=0.975  0 END
  CENTRM DATA  npxs=5 nthr=0 nfst=0 isct=1    END CENTRM DATA
  END CELLDATA

.. _7-1c-7:

Multiple fissile mixtures in a single unit cell
-----------------------------------------------

The following problem involves large units having the bulk of their
fissile material more than one mean-free path away from the surface of
the unit. The interaction between the units that occurs in the resonance
range is a very small fraction of the total interaction because an
overwhelming percentage of the interaction occurs deep within each unit.
Therefore, the resonance range interaction between the units can be
ignored, and the default infinite homogeneous medium cross-section
processing in the resonance range can be considered adequate for this
particular application.

Consider a problem that consists of four 20.96-kg 93.2%-enriched uranium
metal cylinders, density 18.76 g/cm\ :sup:`3`, and four 5-liters
Plexiglas bottles filled with highly enriched uranyl nitrate solution at
415 g/L, a specific gravity of 1.555, and 0.39 mg of excess nitrate per
gram of solution. The isotopic content of the uranium metal is 93.2 wt %
:sup:`235`\ U, 5.6 wt % :sup:`238`\ U, 1.0 wt % :sup:`234`\ U, and
0.2 wt % :sup:`236`\ U. The uranium isotopic content of the nitrate
solution is 92.6 wt % :sup:`235`\ U, 5.9 wt % :sup:`238`\ U, 1.0 wt %
:sup:`234`\ U and 0.5 wt % :sup:`236`\ U. The size of the metal
cylinders is between 10 and 12 cm in diameter and height, and the size
of the nitrate solution is on the order of 16 and 20 cm in diameter and
height. The average mean-free path in the uranium metal is on the order
of 1.5 cm, and the average mean free path in the nitrate solution is on
the order of 0.5 cm. Therefore, infinite homogeneous medium is an
appropriate choice for this problem and the use of CENTRM/PMC is valid.

See Examples 1–4 of  :ref:`7-1a-2` for data input details for the
Plexiglas and uranium metal. See Example 1 of :ref:`7-1a-5` for data
input details for the uranyl nitrate solution. The XSProc data for this
problem follow:

::

  SET  UP  4 AQUEOUS  4  METAL
  fine_n
  READ COMP
  URANIUM  1  0.985  293  92235  93.2  92238  5.6  92234  1.0  92236  0.2  END
  SOLUTION 2  RHO[UO2(NO3)2]=415  92235 92.6 92238 5.9 92234 1.0 92236 0.5
              MOLAR[HNO3]=9.783-3  DENSITY=1.555  TEMPERATURE=293  END SOLUTION
  PLEXIGLAS 3  END
  END COMP

Consider the same materials above except rearrange them so that a 10 cm
diameter uranium metal sphere sits inside a 50 cm diameter spherical
tank of uranyl nitrate solution having a 1-cm thick Plexiglas wall. This
problem can be modeled in SCALE but only CENTRM/PMC will treat the
resonance processing correctly. This problem is modeled below.

::

  SET  UP  4 AQUEOUS  4  METAL
  fine_n
  READ COMP
  URANIUM   1  0.985  293   92235  93.2  92238  5.6  92234  1.0  92236  0.2  END
  SOLUTION  2  RHO[UO2(NO3)2]=415  92235 92.6 92238 5.9 92234 1.0 92236 0.5
               MOLAR[HNO3]=9.783-3  DENSITY=1.555  TEMPERATURE=293  END SOLUTION
  PLEXIGLAS  3  END
  END  COMP
  READ CELLDATA
  MULTIREGION SPHERICAL END 1 5.0 2 25.0 3 26.0 END ZONE
  END CELLDATA

.. _7-1c-8:

Cell weighting an infinite homogeneous problem
----------------------------------------------

Cell weighting an infinite homogeneous medium has no effect on the
cross sections because there is only one zone and one set of
cross sections. However, a cell-weighted mixture number can still be
supplied using the keyword **CELLMIX**\ = followed by an unique mixture
number. This cell-weighted mixture number can be used in subsequent
codes and will produce results similar to the cross sections of the
original mixture.

EXAMPLE 1

This problem would probably be run with CSAS1 to provide the k-infinity
of 20%-enriched UO\ :sub:`2`.

::

  20%  ENRICHED  UO2  BILLET
  fine_n
  READ COMP
  UO2  1  0.99  293  92235  20  92238  80  END
  END COMP
  READ CELLDATA
  INFHOMMEDIUM  1  CELLMIX=100  END
  END CELLDATA

.. _7-1c-9:

Cell weighting a LATTICECELL problem
------------------------------------

Cell weighting used with a **LATTICECELL** problem creates cell-weighted
homogeneous cross sections that represent the characteristics of the
heterogeneous unit cell. This cell-weighted mixture can then be used in
a subsequent code for the overall volume where the cells are located
without having to mock up the actual 3-D heterogeneous array of cells.
This cell-weighted homogeneous mixture is designated by the user with
the keyword **CELLMIX**\ = immediately followed by an unused mixture
number. This needs to follow immediately after the cell description.
Note that the mixtures used in the unit cell data cannot be used in a
subsequent code because they have been flux weighted to create the user
specified mixture. Therefore, if a mixture used in the unit cell
description is also to be used in a subsequent code, another mixture
must be created that is identical except for the mixture number. Every
mixture that is to be used in a subsequent code except zero (i.e., void)
must be defined in the standard composition data.

A byproduct of the cell-weighting calculation is the eigenvalue
(k-effective) of an infinite array of the cell described as the unit
cell.

EXAMPLE 1

Consider a cylindrical stainless steel tank filled with spherical
pellets of 2.67%-enriched UO\ :sub:`2` arranged in a close-packed
“triangular” pitch, flooded with borated water at 4350 ppm. The
cylindrical stainless tank is sitting in a larger tank filled with
borated water at 4350 ppm.

The data for the UO\ :sub:`2` and borated water were developed in detail
in Example 3 of :ref:`7-1c-2`. The stainless steel must be defined, and
mixture 3 was chosen because mixture 1 was the UO\ :sub:`2` and
mixture 2 was the borated water. Because the borated water will be used
as a reflector for the stainless steel tank and has been used in the
unit cell data, it must be repeated with a different mixture number (in
this case, as mixture 4).

In the subsequent calculation, user specified cell mixture 100 will be
used to represent the UO\ :sub:`2` pellets in the borated water,
mixture 3 will represent the stainless steel tank, and mixture 4 will
represent the borated water reflector around the stainless-steel tank.

The XSProc data for creating the cell-weighted cross sections on
mixture 100 follow:

::

  SPHERICAL  PELLETS  IN  BORATED  WATER
  fine_n
  READ COMP
  UO2        1  .9398  293.  92235  2.67  92238  97.33  END
  ATOMH3BO3  2  0.025066  3  5000  1  1001  3  8016  3  1.0  293  END
  H2O        2  0.984507  293  END
  SS304      3  1.0  293  END
  ATOMH3BO3  4  0.025066  3  5000  1  1001  3  8016  3  1.0  293  END
  H2O        4  0.984507  293  END
  END  COMP
  READ CELLDATA
  LATTICECELL  SPHTRIANGP   PITCH  1.0724  2  FUELD  1.0724  1  CELLMIX=100  END
  END CELLDATA

.. _7-1c-10:

Cell weighting a MULTIREGION problem
------------------------------------

A **MULTIREGION** problem is cell weighted primarily to obtain a
cell-weighted homogeneous cross section that represents the
characteristics of the heterogeneous unit cell. The eigenvalue obtained
for a **MULTIREGION** problem with cylindrical or spherical geometry
having a white boundary condition specified on the right boundary
approximates an infinite array of the cells. A vacuum boundary condition
would represent a single cell. A slab with reflected boundary conditions
for both boundaries represents an infinite array of slab cells. The
cell-weighted cross sections for spherical or cylindrical geometries
with a white right boundary condition do not use a Dancoff correction
and thus may not be accurate for representing a large array of the
specified units.


EXAMPLE 1


Consider a small, highly enriched uranium sphere supported by a
Plexiglas collar in a tank of water. The uranium metal sphere has a
diameter of 13.1075 cm, is 97.67% enriched, and has a density of
18.794 g/cm\ :sup:`3`. The cylindrical Plexiglas collar has a 4.1275-cm
radius central hole, extends to a radius of 12.7 cm and is 2.54 cm
thick. The water-filled tank is 60 cm in diameter.

The Plexiglas collar is not significantly different from water and does
not surround the fuel, so it will be ignored. Because this makes the
problem a 1-D geometry, it can be defined using the **MULTIREGION** type
of calculation and the eigenvalue of the system can be obtained without
additional data by executing CSAS1 with CENTRM/PMC, if PARM=CENTRM is
specified on the command line. The abundance of uranium is not stated
beyond 97.67% enriched, so assume the remainder is :sup:`238`\ U. The
XSProc data follow:

::

  =CSAS5
  SMALL  WATER  REFLECTED  SPHERE  ON  PLEXIGLAS  COLLAR
  fine_n
  READ COMP
  URANIUM    1  DEN=18.794  1  293.  92235  97.67  92238  2.33  END
  H2O        2  END
  END  COMP
  READ CELLDATA
  MULTI SPHERICAL CELLMIX=100  END   1  6.5537  2  30.0  END ZONE
  END CELLDATA
  •
  •
  •
  KENO DATA THAT USES MIX=100 FOR A HOMOGENEOUS SPHERE OF 30-CM RADIUS GOES HERE.
  •
  •
  END
