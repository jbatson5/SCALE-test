.. _7-1b:

XSProc Standard Composition Examples
====================================

.. _7-1b-1:

Infinite homogeneous medium unit cell data
------------------------------------------

EXAMPLE 1. A single mixture 1.

   Consider a single cylindrical configuration of mixture 1, composed of
   10% enriched UO\ :sub:`2` having a radius of 35 cm and a height of
   20 cm. This fuel region is sufficient large to model as an infinite
   medium. Mixture 100 may be used in subsequent multigroup neutron
   transport calculations.

.. highlight:: scale

::

  INFHOMMEDIUM  1  CELLMIX=10  END

XSDRNPM will calculate the eigenvalue of an infinite mass of 10%
enriched UO\ :sub:`2`.

.. _7-1b-2:

LATTICECELL unit cell data
--------------------------

Examples of “regular” **LATTICECELL** unit cells are given in
Examples 1–5, and examples of “annular” **LATTICECELL** unit cells are
given in Examples 6–10 below.

EXAMPLE 1. SQUAREPITCH (infinitely long cylindrical pins in a square-pitched array).

   Consider a large array of UO\ :sub:`2` fuel pins having a fuel O.D.
   of 0.79 cm, a 0.015-cm gap, and a 0.06-cm-thick aluminum clad. The
   array is a square-pitched array with a center-to-center spacing of
   1.60 cm and is completely flooded with water. In the standard
   composition data, UO\ :sub:`2` is defined to be mixture 1, the
   aluminum clad is defined to be mixture 2, and the water moderator is
   defined to be mixture 3.

::

  LATTICECELL  SQUAREPITCH PITCH=1.60 3 FUELD=0.79 1 CLADD=0.94 2 GAPD=0.82 0 END

EXAMPLE 2. TRIANGPITCH (infinitely long cylinders in a triangular-pitched array).

   Consider an array of UO\ :sub:`2` pins with a diameter of 0.635 m.
   The outside diameter of the clad is 0.78 cm. There is no gap between
   the fuel and clad. The array is a triangular-pitched array with a
   center-to-center spacing of 5.0 cm and is flooded with water. In the
   standard composition data, the UO\ :sub:`2` is defined to be
   mixture 1, the aluminum is defined to be mixture 2, and the water
   moderator is defined to be mixture 3.

::

  LATTICECELL  TRIANGPITCH PITCH=5.0  3  FUELD=.635  1  CLAD=.78  2  END

EXAMPLE 3. SPHSQUAREP (spheres in a square-pitched array).

   Consider a large array of U\ :sub:`3`\ O\ :sub:`8` spheres having a
   fuel O.D. of 18.6 cm, with an aluminum clad that is 0.18 cm thick.
   The array is a triangular-pitched array with a center-to-center
   spacing of 19.0 cm and is unmoderated. In the standard composition
   data, the aluminum is defined to be mixture 1 and the
   U\ :sub:`3`\ O\ :sub:`8` is defined to be mixture 2. There is no
   moderator material, so 0 will be used to represent a void. Also, have
   XSDRNPM make a cell weighted material 20 from this unit cell.

::

  LATTICECELL SPHSQUAREP PITCH=19.0 0 FUELD=18.6 2 CLADD=18.96 1 CELLMIX=20 END

EXAMPLE 4. SPHTRIANGP (spheres in a triangular-pitched array).

   Consider a large array of U\ :sub:`3`\ O\ :sub:`8` spheres having a
   fuel O.D. of 18.6 cm, with an aluminum clad that is 0.18 cm thick.
   The array is a triangular-pitched array with a center-to-center
   spacing of 19.0 cm and is flooded with water. In the standard
   composition data, the aluminum is defined to be mixture 1, the
   U\ :sub:`3`\ O\ :sub:`8` is defined to be mixture 2, and the water
   moderator is defined to be mixture 3.

::

  LATTICECELL  SPHTRIANGP  PITCH=19.0  3  FUELD=18.6  2 CLADD=18.96  1  END

EXAMPLE 5. SYMMSLABCELL (slabs repeated in a symmetric fashion).

   Consider a system of alternating slabs of U\ :sub:`3`\ O\ :sub:`8`
   and low-density water. Each U\ :sub:`3`\ O\ :sub:`8` region is
   1.27 cm thick, and each water region is 15.0 cm thick. In the
   standard composition data, the U\ :sub:`3`\ O\ :sub:`8` is defined to
   be mixture 1, and the low-density water is defined to be mixture 2.

::

  LATTICECELL  SYMMSLABCELL PITCH=16.27  2 FUELD=1.27  1  END

EXAMPLE 5a. SYMMSLABCELL (slabs repeated in a symmetric fashion).

   Consider a system of alternating slabs of U\ :sub:`3`\ O\ :sub:`8`
   and low-density water. Each U\ :sub:`3`\ O\ :sub:`8` region is
   1.27 cm thick, and each water region is 15.0 cm thick. The
   U\ :sub:`3`\ O\ :sub:`8` regions have a 0.01-cm gap and 0.24-cm-thick
   aluminum clad on each face. In the standard composition data, the
   U\ :sub:`3`\ O\ :sub:`8` is defined to be mixture 1, the aluminum is
   defined to be mixture 2, and the low-density water is defined to be
   mixture 3. Also, have XSDRNPM make a cell-weighted material 100 from
   this unit cell.

::

  LATTICECELL  SYMMSLABCELL  PITCH=16.77  3  FUELD=1.27  1
  CLADD=1.77  2  GAPD=1.29  0  CELLMIX=100  END


EXAMPLE 6. ASQUAREPITCH (infinitely long annular cylindrical rods in a square-pitched array).

   Consider an array of uranium metal pipes having an inside diameter of
   5.0 cm and an outer diameter of 6.75 cm. A gap of 0.025 cm and a clad
   of 0.25 cm exist on both the inner and outer surfaces of the fuel.
   The fuel rods are arranged in a square-pitched array.
   The center-to-center spacing is 8.0 cm. The array is completely
   flooded with water. In the standard composition data, the uranium
   metal is defined to be mixture 1, the outer clad is mixture 2, the
   inner clad is mixture 7, the inner moderator is Plexiglas and is
   mixture 3, the gap is a void, and the external moderator is water,
   defined to be mixture 4.

::

  LATTICECELL  ASQUAREPITCH  PITCH=8.0  4  FUELD=6.75  1  GAPD=6.8  0
  CLADD=7.3  2  IMODD=4.45  3  ICLADD=4.95 7  IGAPD=5.0  0  END

EXAMPLE 6a. ASQUAREPITCH (infinitely long annular cylindrical rods in a square-pitched array).

   Consider an array of uranium metal pipes having an inside diameter of
   5.0 cm and an outer diameter of 6.75 cm arranged in a square-pitched
   array. The center-to-center spacing is 8.0 cm. The array is
   completely flooded with water. In the standard composition data, the
   uranium metal is defined to be mixture 1, the water moderator is
   defined to be mixture 2, and the inside water moderator is defined as
   mixture 3.

::

  LATTICECELL  ASQUAREPITCH  PITCH=8.0  2  FUELD=6.75  1  IMODD=5.0  3  END

.. note:: This problem defines two water mixtures. If mixture 2 were
  entered twice, i.e., for both the inner and outer moderator, an error
  message would be printed and the calculation terminated.

EXAMPLE 7. ATRIANGPITCH (infinitely long annular cylindrical rods in a triangular-pitched array).

   Consider an array of uranium metal pipes having an inside diameter of
   8.0 cm and a wall thickness of 0.75 cm arranged in a square-pitched
   array. The center-to-center spacing is 9.75 cm. The array is
   completely flooded with water. A Plexiglas rod fills the center of
   the uranium pipe. In the standard compositions data, the uranium
   metal is defined to be mixture 1, the Plexiglas is defined to be
   mixture 2, and the external water moderator is mixture 3.

::

  LATTICECELL  ATRIANGPITCH  PITCH=9.75  3  FUELD=9.5  1  IMODD=8.0  2  END

EXAMPLE 8. ASPHSQUAREP (spherical annuli in a square-pitched array).

   Consider a large array of hollow U\ :sub:`3`\ O\ :sub:`8` spheres
   having a fuel I.D. of 8.0 cm and O.D. of 18.6 cm. The centers of the
   spheres are empty. The external moderator is water. The spheres are
   stacked in a square-pitched array with a center-to-center spacing of
   19.0 cm. In the standard composition data, the
   U\ :sub:`3`\ O\ :sub:`8` is defined to be mixture 1, and the water is
   defined to be mixture 2. The centers of the spheres are defined to be
   void, mixture 0.

::

  LATTICECELL  ASPHSQUAREP  HPITCH=9.5  2  FUELR=9.3  1  IMODR=4.0  0  END

EXAMPLE 9. ASPHTRIANGP (spheres in a triangular-pitched array).

   Consider a large array of hollow U\ :sub:`3`\ O\ :sub:`8` spheres
   having a fuel I.D. of 8.0 cm and a fuel O.D. of 18.6 cm. A
   0.18-cm-thick aluminum clad exists outside the fuel. The interior of
   each sphere is void. The array is a triangular-pitched array with a
   center-to-center spacing of 19.0 cm and is flooded with water. In the
   standard composition data, the aluminum is defined to be mixture 1,
   the U\ :sub:`3`\ O\ :sub:`8` is defined to be mixture 2, and the
   water moderator is defined to be mixture 3. The void in the center of
   each sphere is entered as mixture 0.

::

  LATTICECELL ASPHTRIANGP HPITCH=9.5  3 FUELR=9.3  2 IMODR=4.0  0 CLADR=9.48  1 END

EXAMPLE 10. ASYMSLABCELL (repeated slabs having different moderator conditions on the left and right boundaries).

   Consider an array of U\ :sub:`3`\ O\ :sub:`8` slabs with an inner
   moderator region composed of full-density water with a half thickness
   of 8.0 cm, and a low-density water outer moderator with a 16 cm half
   thickness of 16 cm half thickness. Each U\ :sub:`3`\ O\ :sub:`8` slab
   is 10.54 cm thick. In the standard composition data, the
   U\ :sub:`3`\ O\ :sub:`8` is defined to be mixture 1, the full density
   water is defined to be mixture 2, and the low-density water is
   mixture 3. Also, have XSDRNPM create a cell weighted mixture 100 from
   this unit cell.

::

  LATTICECELL ASYMSLABCELL CELLMIX=100 IMODR=8.0 2 FUELR=18.54 1  HPITCH=34.54 3 END

EXAMPLE 10a. ASYMSLABCELL (repeated slabs having different moderator conditions on the left and right boundaries).

   Consider an array of U\ :sub:`3`\ O\ :sub:`8` fuel plates with an
   inner moderator region of full-density water with a half-thickness of
   8.0 cm, and with a 16 cm thick low-density outer moderator. Each fuel
   plate includes a 10.54 cm thick U\ :sub:`3`\ O\ :sub:`8` slab with a
   0.01 cm gap and 0.24-cm-thick aluminum clad on each face. In the
   standard composition data, the U\ :sub:`3`\ O\ :sub:`8` is defined to
   be mixture 1, the full density water is defined to be mixture 2, and
   the low-density water is mixture 3, the inner aluminum is mixture 4,
   the outer aluminum clad is mixture 5, and both gaps are voids.

::


  LATTICECELL ASYMSLABCELL IMODR=8.0 2 ICLADR=8.24 5 IGAPR=8.25 0 FUELR=18.79 1
  GAPR 18.80 0 CLADR 19.04 4 HPITCH=27.04 3 END

.. _7-1b-3:

MULTIREGION unit cell data
--------------------------

Examples of **MULTIREGION** unit cells follow:

EXAMPLE 1. SLAB.

   Consider a 5-cm-thick slab of fuel (mixture 1) with 0.5 cm of
   aluminum (mixture 3) and 15 cm of water (mixture 2) on each face. The
   unit cell data for this problem could be entered as follows:

::

  MULTIREGION  SLAB  LEFT_BDY=REFLECTED  RIGHT_BDY=VACUUM  ORIGIN=0  END
  1  2.5  3  3.0  2  18.0  END ZONE

EXAMPLE 2. CYLINDRICAL.

   Consider a large array of fuel pins. Each pin is UO\ :sub:`2`
   (mixture 1) with a radius of 0.465 cm, a 0.009-cm gap (mixture 0),
   and a Zircaloy clad (mixture 9) 0.062 cm thick, centered in a water
   (mixture 8) region surrounded by a flooded support structure
   represented by homogenized water and Zircaloy (mixture 10). The outer
   radius of the water-Zircaloy region is 0.844 cm and it is 0.037 cm
   thick. This problem cannot be described as a **LATTICECELL** problem
   because the **LATTICECELL** configuration is limited to
   fuel-gap-clad-cell boundary and this problem is
   fuel-gap-clad-moderator-outer region. When **MULTIREGION** is used,
   lattice effects are accounted for by specifying a **WHITE**,
   **PERIODIC**, or **REFLECTED** right boundary condition, as long as
   the CENTRM/PMC self-shielding method is used. **MULTIREGION** cells
   should not be used for arrays if BONAMI-only method is specified


::

  MULTIREGION  CYLINDRICAL RIGHT_BDY=WHITE  END
  1  0.465  0  0.474  9  0.536  8  0.807  10  0.844  END ZONE

EXAMPLE 3. SPHERICAL.

   Describe a bare sphere of uranium metal 8.72 cm in radius. The
   uranium metal is defined to be mixture 1. Also, have XSDRNPM create a
   cell weighted mixture 100 and calculate and eigenvalue. The unit cell
   data for this problem could be entered as follows:

::

  MULTIREGION  SPHERICAL  CELLMIX=100  END   1  8.72    END ZONE

EXAMPLE 4. BUCKLEDSLAB.

   Consider a plate of fuel 4 cm thick, reflected by 3 cm of water on
   both faces. The plate is 32 cm tall and 16 cm deep. The fuel is
   mixture 1 and the water is mixture 2. Also, have XSDRNPM create a
   cell weighted mixture 100 and calculate and eigenvalue.

::

  MULTIREGION  BUCKLEDSLAB  CELLMIX=100  LEFT_BDY=REFLECTED  RIGHT_BDY=VACUUM
  DY=32 DZ=16.0  END  1  2.0  2  5.0  END ZONE

EXAMPLE 5. BUCKLEDCYL.

   Consider a solution of uranyl nitrate contained in a cylindrical
   stainless-steel container reflected by 33 cm of water. The inside
   dimensions of the steel container are 7.62 cm in radius and 130.0 cm
   tall. The steel is 0.15 cm thick. The uranyl nitrate is defined to be
   mixture 1, the steel is defined to be mixture 2, and the water is
   defined to be mixture 3.

::

  MULTIREGION  BUCKLEDCYL  DY=130  END
  1  7.62  2  7.77  3  40.77  END ZONE

.. _7-1b-4:

DOUBLEHET unit cell data
------------------------

Unit cell data are always required for **DOUBLEHET** calculations. As
many unit cells as needed may be defined in the problem. If
**CELLMIX**\ =\ *mx* is entered after the fuel element (macro cell)
description, XSProc calls XSDRNPM to calculate the eigenvalue of the
cell and to create a homogenized cell-weighted cross section having the
characteristics of the doubly-heterogeneous cell configuration.

EXAMPLE 1: A doubly-heterogeneous spherical fuel element with 15,000 UO\ :sub:`2` particles in a graphite matrix.

   Grain fuel radius is 0.025 cm. Grain contains one coating layer that
   is 0.009-cm-thick. Pebbles are in a triangular pitch on a
   6.4-cm-pitch. Fuel pebble fuel zone is 2.5‑cm in radius and contains
   a 0.5-cm-thick graphite clad that contains small amounts of
   :sup:`10`\ B. Pebbles are surrounded by :sup:`4`\ He. Assume the
   composition block is below:

::

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

The cell data for the **DOUBLEHET** cell follows:

::

  DOUBLEHET FUELMIX=10 END
   GFR=0.025  1 COATT=0.009 2 MATRIX=6 NUMPAR=15000 END GRAIN
  PEBBLE SPHTRIANGP RIGHT_BDY=WHITE HPITCH=3.2 8 FUELR=2.5 CLADR=3.0 7  END

In this case we designated the homogenized mixture as mixture 10. If we
have a KENO V.a or KENO-VI input section, we would use mixture 10 in
that section. Note that the keyword “\ **FUELR**\ =” is followed by the
fuel dimension only, i.e., no mixture number. That is because the fuel
mixture number is specified with “\ **FUELMIX**\ =” and therefore need
not be repeated.

EXAMPLE 2: Same as Example 1, except volume fraction of the grain type is known and is 0.037732.

::

  DOUBLEHET  RIGHT_BDY=WHITE FUELMIX=10 END
   GFR=0.025  1 COATT=0.009 2 MATRIX=6 VF=0.037732 END GRAIN
  PEBBLE SPHTRIANGP RIGHT_BDY=WHITE HPITCH=3.2 8 FUELR=2.5 CLADR=3.0 7  END

EXAMPLE 3: Same as Example 1, except halfpitch of the grain type is known and is 0.10137 cm.

::

  DOUBLEHET FUELMIX=10 END
   GFR=0.025  1 COATT=0.009 2 HPITCH=0.10137 MATRIX=6 END GRAIN
  PEBBLE SPHTRIANGP RIGHT_BDY=WHITE HPITCH=3.2 8 FUELR=2.5 CLADR=3.0 7  END

EXAMPLE 4: A doubly-heterogeneous spherical fuel element with 10,000 UO2 particles
and 5,000 PuO2 particles in a graphite matrix.

  Grain fuel radii for UO\ :sub:`2` and PuO\ :sub:`2` particles are
  0.025 cm and 0.012 cm, respectively. UO\ :sub:`2` grains contain one
  coating layer that is 0.009‑cm-thick. PuO\ :sub:`2` grains contain one
  coating layer that is 0.0095-cm-thick. Pebbles are in a triangular pitch
  on a 6.4-cm-pitch. Fuel pebble fuel zone is 2.5-cm in radius and
  contains a 0.5-cm-thick graphite clad that contains small amounts of
  :sup:`10`\ B. Pebbles are surrounded by :sup:`4`\ He. Assume the
  composition block is given below:

::

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

The cell data for the **DOUBLEHET** cell follows:

::

  DOUBLEHET FUELMIX=10 END
   GFR=0.025  1 COATT=0.009 2 MATRIX=6 NUMPAR=10000 END GRAIN
   GFR=0.012 11 COATT=0.0095 12 MATRIX=16 NUMPAR=5000 END GRAIN
  PEBBLE SPHTRIANGP RIGHT_BDY=WHITE HPITCH=3.2 8 FUELR=2.5 CLADR=3.0 7 END

Since number of particles is entered, the total volume fraction and the pitch can be calculated by the code.

EXAMPLE 5: Same as Example 4 above except the volume fractions of UO\ :sub:`2`
and PuO\ :sub:`2` grains are 0.02511 and 0.00318, respectively.

::

  DOUBLEHET  RIGHT_BDY=WHITE FUELMIX=10 END
   GFR=0.025  1 COATT=0.009 2 MATRIX=6 VF=0.02511 END GRAIN
   GFR=0.012 11 COATT=0.0095 12 MATRIX=16 VF=0.00318 END GRAIN
  PEBBLE SPHTRIANGP RIGHT_BDY=WHITE HPITCH=3.2 8 FUELR=2.5 CLADR=3.0 7 END

EXAMPLE 6: Same as Example 4 above except pitch is also known.

   UO\ :sub:`2` grains have a pitch of 0.25 cm. PuO\ :sub:`2` grains
   have a pitch of 0.20 cm.

::

  DOUBLEHET FUELMIX=10 END
   GFR=0.025  1 COATT=0.009 2
   MATRIX=6 NUMPAR=10000 PITCH=0.25 END GRAIN
   GFR=0.012  11 COATT=0.0095 12
   MATRIX=16 NUMPAR=5000 PITCH=0.20 END GRAIN
  PEBBLE SPHTRIANGP RIGHT_BDY=WHITE HPITCH=3.2 8 FUELR=2.5 CLADR=3.0 7 END

Since number of particles is sufficient to perform the homogenization,
it is used. However, instead of calculating the pitch for the 1-D cell
calculation for each grain type, the user input pitch is used. Hence,
the calculated *k*\ :sub:`eff` of Example 6 will be different from those of
Examples 4 and 5.

**EXAMPLE 7: Same as Example 6 except the doubly-heterogeneous cell will
be cell-weighted.**

   The final cell-weighted mixture number is 17.

::


  DOUBLEHET FUELMIX=10 END
   GFR=0.025  1 COATT=0.009 2
   NUMPAR=10000 PITCH=0.25 MATRIX=6 END GRAIN
   GFR=0.012  11 COATT=0.0095 12
   NUMPAR=5000 PITCH=0.20 MATRIX=16 END GRAIN
  PEBBLE SPHTRIANGP RIGHT_BDY=WHITE HPITCH=3.2 8 FUELR=2.5 CLADR=3.0 7 CELLMIX=17 END

EXAMPLE 8: A doubly-heterogeneous spherical fuel element with 15,000 UO\ :sub:`2` particles in a graphite matrix.

   Grain fuel radius is 0.012 cm. Grain contains four coating layers
   that are 0.0095, 0.004, 0.0035, and 0.004-cm-thick. Pebbles are in a
   square pitch on a 6.0‑cm-pitch. Fuel pebble fuel zone is 2.5-cm in
   radius and contains a 0.5-cm-thick graphite clad that contains small
   amounts of :sup:`10`\ B. Pebbles are surrounded by :sup:`4`\ He.
   Assume the composition block is given below:

::


  ' UO2 FUEL KERNEL
  U-235  1 0 1.92585E-3 293.6 END
  O      1 0 4.64272E-2 293.6 END
  ' FIRST COATING
  C      2 0 5.26449E-2 293.6 END
  ' INNER PYRO CARBON
  C      3 0 9.52621E-2 293.6 END
  ' SILICON CARBIDE
  C      4 0 4.77240E-2 293.6 END
  SI     4 0 4.77240E-2 293.6 END
  ' OUTER PYRO CARBON
  C      5 0 9.52621E-2 293.6 END
  ' GRAPHITE MATRIX
  GRAPHITE 6 0 8.77414E-2 293.6 END
  ' CARBON PEBBLE OUTER COATING
  C      7 0 8.77414E-2 293.6 END
  B-10   7 0 9.64977E-9 293.6 END
  HE-4   8 0 2.65156E-5 293.6 END

The cell data for the **DOUBLEHET** cell follows:

::

  DOUBLEHET FUELMIX=10 END
   GFR=0.012  1 COATT=0.0095 2 COATT=0.004 3 COATT=0.0035 4 COATT=0.004 5 MATRIX=6 NUMPAR=15000 VF=0.0245 END GRAIN
  PEBBLE SPHSQUAREP RIGHT_BDY=WHITE HPITCH=3.0 8 FUELR=2.5 CLADR=3.0 7 END

Note that the grains are overspecified and the numbers are inconsistent.
A **VF** value of 0.0245 results in a total number of particles of
10652.32 which is considerably less than 15,000. In this case, the code
will issue a warning to this effect and will use **VF** value in the
calculations (i.e., ignore **NUMPAR**\ =15000 entry).

EXAMPLE 9: Similar to Example 8 except radii for grain regions are entered.

::

  DOUBLEHET FUELMIX=10 END
   GFR=0.012  1 COATR=0.0215 2 COATR=0.0255 3 COATR=0.029 4 COATR=0.033 5 MATRIX=6 NUMPAR=15000 VF=0.0245 END GRAIN
  PEBBLE SPHSQUAREP RIGHT_BDY=WHITE HPITCH=3.0 8 FUELR=2.5 CLADR=3.0 7 END

EXAMPLE 10: A doubly-heterogeneous spherical fuel element with two UO\ :sub:`2` grain types.

   First grain type has a fuel radius of 0.025 cm. Second grain type
   fuel radius is 0.004 cm. First grain type has one coating that is
   0.009-cm-thick. Second grain type has two coatings each
   0.004-cm-thick. Each grain type has a volume fraction of 0.45.
   Pebbles are in a triangular pitch on a 7.0-cm-pitch. Fuel pebble fuel
   zone is 2.5-cm in radius and contains a 0.5-cm-thick graphite clad
   that contains small amounts of :sup:`10`\ B and :sup:`11`\ B. Pebbles
   are surrounded by :sup:`4`\ He. Assume the composition block is given
   below:

::

  ' FUEL KERNEL
  U-238  1 0 2.12877E-2 END
  U-235  1 0 1.92585E-3 END
  O      1 0 4.64272E-2 END
  B-10   1 0 1.14694E-7 END
  B-11   1 0 4.64570E-7 END
  ' FIRST COATING
  C      2 0 5.26449E-2 END
  ' INNER PYRO CARBON
  C      3 0 9.52621E-2 END
  ' SILICON CARBIDE
  C      4 0 4.77240E-2 END
  SI     4 0 4.77240E-2 END
  ' FUEL KERNEL
  U-238  5 0 2.12877E-2 END
  U-235  5 0 1.92585E-3 END
  O      5 0 4.64272E-2 END
  B-10   5 0 1.14694E-7 END
  B-11   5 0 4.64570E-7 END
  ' GRAPHITE MATRIX
  C      6 0 8.77414E-2 END
  B-10   6 0 9.64977E-9 END
  B-11   6 0 3.90864E-8 END
  ' CARBON PEBBLE OUTER COATING
  C      7 0 8.77414E-2 END
  B-10   7 0 9.64977E-9 END
  B-11   7 0 3.90864E-8 END
  ' HELIUM
  HE     8 0.000164 END
  ' GRAPHITE MATRIX
  C      9 0 8.77414E-2 END
  B-10   9 0 9.64977E-9 END
  B-11   9 0 3.90864E-8 END

The cell data for the **DOUBLEHET** cell follows:

::

  DOUBLEHET FUELMIX=10 END
   GFR=0.025  1 COATR=0.034 2  MATRIX=6 VF=0.45 END GRAIN
   COATT=0.004 3 GFR=0.4 5 COATT=0.004 4 MATRIX=9  VF=0.45    END GRAIN
  PEBBLE SPHTRIANGP RIGHT_BDY=WHITE HPITCH=3.5 8 FUELD=5.0
    CLADD=6.0 7 END

EXAMPLE 11: A doubly-heterogeneous hexagonal block type fuel element
with UO\ :sub:`2` grains in a cylindrical fuel region.

   Grain fuel radius is 0.025 cm. Grain coating is 0.009-cm-thick.
   Grains have a volume fraction of 0.45. Hexagonal rods are in a 7-cm
   triangular pitch. Fuel rod fuel zone is 2.5-cm in radius, 10-cm-high
   and contains a 0.5-cm-thick graphite clad that contains small amounts
   of :sup:`10`\ B. Assume the composition block is below:

::

  ' FUEL KERNEL
  U-238  1 0 2.12877E-2 END
  U-235  1 0 1.92585E-3 END
  O      1 0 4.64272E-2 END
  B-10   1 0 1.14694E-7 END
  ' FIRST COATING
  C      2 0 5.26449E-2 END
  ' GRAPHITE MATRIX
  C      6 0 8.77414E-2 END
  B-10   6 0 9.64977E-9 END
  ' CARBON PEBBLE OUTER COATING
  C      7 0 8.77414E-2 END
  B-10   7 0 9.64977E-9 END
  ' IRON CLADDING
  FE     8 END

The cell data for the **DOUBLEHET** cell follows:

::

  DOUBLEHET FUELMIX=10 END
   GFR=0.025  1 COATR=0.034 2  MATRIX=6 VF=0.45 END GRAIN
  ROD TRIANGP RIGHT_BDY=WHITE HPITCH=3.5 7 FUELD=5.0
    FUELH=10 END

EXAMPLE 12: This is the same as Example 11 except the fuel elements (cylindrical rods) have 0.05‑cm-thick iron cladding.

The cell data for the **DOUBLEHET** cell follows:

::

  DOUBLEHET FUELMIX=10 END
   GFR=0.025  1 COATR=0.034 2  MATRIX=6 VF=0.45 END GRAIN
  ROD TRIANGP RIGHT_BDY=WHITE HPITCH=3.5 7 FUELR=2.5
    CLADD=5.1 8 FUELH=10 END

.. _7-1b-5:

Optional parameter data
-----------------------

The optional parameter data provide a means of providing additional
information or alternative data to the cross-section processing codes.
There are two types of optional parameter data. The first type of data
is used by XSDRNPM and BONAMI for cross-section processing and
cell-weighting cross sections. This type of data is initiated using the
keywords **MORE DATA** and ends with the keywords **END MORE**. This
input is described in :ref:`7-1-3-8`. The second type of optional
parameter data is used by CENTRM and PMC for cross-section processing.
This type of data is initiated using the keywords **CENTRM DATA** and
ends with the keywords **END CENTRM**. This input is described in
:ref:`7-1-3-9`. It is possible to input both types of data for a unit
cell. The optional parameter data specified apply only to the unit cell
that immediately precedes it.


MORE DATA examples

Consider a problem in which it is desirable to increase the number of
inner iterations in XSDRNPM to 30 and to tighten the overall convergence
criteria to a value of 0.000075. This could be accomplished by entering
the data as follows:

::

  MORE DATA   IIM=30  EPS=0.000075  END

The order of the data entry is not important, and it can be continued
across several lines. However, a keyword and its value cannot be
separated across lines. The terminator for the optional parameter data,
END, must not begin in column 1 unless you assign a name to it. An
alternative method of entering the above data is given below.

::

  MORE DATA
    IIM=30  EPS=0.000075
  END MORE

or,

::

  MORE DATA  IIM=30  EPS=0.000075  END MORE DATA

.. _7-1b-6:

CENTRM DATA examples
--------------------

Consider a problem in which it is desirable to increase the upper energy
of the CENTRM CE transport calculation from the default of 20000 eV to a
value 50000 eV, and to extend the default lower energy from 0.001 eV to
0.0001. This is accomplished by entering the data as follows:

::

  CENTRM DATA  DEMAX=50000  DEMIN=0.0001 END CENTRM

As with the **MORE DATA** block, an alternative method of entering the
above data is given below.

::

  CENTRMDATA
    DEMAX=50000  DEMIN=0.0001
  END CENTRMDATA

**CENTRM and PMC** computation options can also be controlled with
**CENTRM DATA.** A complete description of the CENTRM/PMC computational
methods and options can be found the corresponding sections of the SCALE
manual. The following example specifies that:

(a) discrete-level inelastic scattering will be used in CENTRM and
processed in PMC [nmf6];

(b) the CENTRM 1D discrete S\ :sub:`N` transport solver will be used in
the upper MG energy range [nfst] and the CE energy range [npxs], while
the infinitie medium model will be used for the thermal energy range
[nthr];

(c) a P3 scattering order [isct] will be used in the transport
calculations;

(d) PMC will perform “consistent PN” corrections on Legendre moments of
the 2D elastic matrices [n2d]; (e) additional output information will be
provided by CENTRM [ixprt] and by PMC [nprt].

::

  CENTRM DATA  NMF6=0 NFST=0 NTHR=2 ISCT=3
         N2D=-2 IXPRT=1  NPRT=1    END CENTRM DATA
