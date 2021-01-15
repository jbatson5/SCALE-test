.. _7-6:

CHOPS: Module to Compute Pointwise Disadvantage Factors and Produce a Cell-Homogenized CENTRM Library
=====================================================================================================

*M. L. Williams and L. M. Petrie*

.. _7-6-1:

Introduction
------------

CHOPS (**C**\ ompute **HO**\ mogenized **P**\ ointwise **S**\ tuff)
computes pointwise (PW) disadvantage factors from the PW zone fluxes on
a CENTRM output file, and then multiples the disadvantage factors by
continuous-energy (CE) cross section data in a CENTRM library to
generate a new cell-homogenized CENTRM CE library. The PW disadvantage
factor for zone “Z”, as a function of energy E, is calculated from the
expression,

.. math::
  :label: eq7-6-1

  D_{Z}(E)=\frac{\Phi_{Z}(E)}{\Phi_{C}(E)}

where :math:`\Phi_{Z}(E)` is the CENTRM PW flux spectrum averaged over the volume
of zone Z in the cell, and :math:`\Phi_{C}(E)` is the PW flux averaged over the
entire cell volume. The cell-homogenized CE cross section for a nuclide
“j” is equal to

.. math::
  :label: eq7-6-2

  \sigma_{C}^{(j)}(E)=\sum_{Z} F_{Z}^{(j)} D_{Z}(E) \sigma_{Z}^{(j)}(E)

where :math:`F_{Z}^{(j)}` is the fraction of all nuclide–j atoms contained in zone
Z, and :math:`\sigma_{Z}^{(j)}(E)` is the CE cross section for nuclide-j at the
temperature of zone Z. When multiplied by the cell-homogenized number
density of nuclide-j and by the cell-average flux, the cross section
expression in :eq:`eq7-6-1` gives the correct average reaction rate at
energy E.

.. equation in here says 8.5.1

CHOPS is used in the automated double heterogeneity sequence in SCALE,
in which a low-level heterogeneity, such as microspheres in a granular
fuel element, are smeared into a homogenized absorber region appearing
in the second level heterogeneity, such as fuel pellet or pebble
appearing in a lattice. The disadvantage factors provide for flux
weighting of the PW XS data so that the spatial self-shielding is
treated correctly in the homogenized geometry. A second CENTRM PW
transport calculation is performed with the cell-averaged PW library
output by CHOPS in order to account for the additional self-shielding of
the absorber pellets/pebbles in the lattice. CHOPS is called
automatically by the XSProc module for double-heterogeneous unit cells,
or it can run as a standalone code.

.. _7-6-2:

CHOPS Input Data
----------------

**DATA BLOCK 1**

**0$$ LOGICAL UNIT ASSIGNMENTS** (10 entries. Default values given in
parentheses)

1. lold -- logical unit number of input CENTRM XS library (1)

2. lnew -- logical unit number of output CENTRM homogenized XS library
(2)

3. lflx -- logical unit number of input CENTRM PW flux library (3)

4. ldis -- logical unit number for edit of PW disadvantage factors (0)

5. n15 -- logical unit number for scratch (15)

6. n16 -- logical unit number for scratch (16)

7. n17 -- logical unit number for scratch (17)

8. n18 -- logical unit number for scratch (18)

9. n19 -- logical unit number for scratch (19)

10. nsq -- sequence number used in filename on unit “lnew” (1)

[Example: if *lnew=11* and *nsq=3*: output filename of homogenized
library\ *= ft11f003]*


**1$$ INTEGER PARAMETERS** (5 entries )

1. idtap -- identifier for the new library (55555)

[for macro library, the value of *idtap* is made negative]

2. nprt -- output print option: 0 = > min print; 1 = > normal; 2 = > max
print (0)

3. iden -- if=0 = > define homogenized XS id = id on CENTRM flux file
(0)

if>0 = > define homogenized XS id to be, (*iden*\ \*10\ :sup:`6` + ZA)

4. macr -- type of XS output: 0 = > microscopic ; 1 = > macroscopic (0)

5. icorr -- not used (0)


**2*\* REAL PARAMETERS** (3 entries )

1. tole -- tolerance used to thin pointwise cross-sections (0.0025)

( 0.0 means no thinning is done )

2. cleth -- maximum lethargy between thinned pointwise cross-sections

points that allow a point to be discarded (0.25)

3. vfrac -- multiplier applied to all output XS’s [eg, grain fraction]
(1.0)

T [ TERMINATE DATA BLOCK 1 ]

.. _7-6-3:

CHOPS I/O units
---------------

:numref:`tab7-6-1` shows default logical unit numbers used by CHOPS. These
values may be changed in the 0$$ array of input.

.. _tab7-6-1:
.. table:: Default I/O unit assignments for CHOPS.
  :align: center

  +-------------+-------------------------------------------+
  | Unit number | Description                               |
  +-------------+-------------------------------------------+
  | 1           | Input CENTRM CE data library              |
  |             |                                           |
  | 2           | Output homogenized CENTRM CE data library |
  |             |                                           |
  | 3           | Input pointwise CENTRM flux file          |
  |             |                                           |
  | 15          | Scratch file                              |
  |             |                                           |
  | 16          | Scratch file                              |
  |             |                                           |
  | 17          | Scratch file                              |
  |             |                                           |
  | 18          | Scratch file                              |
  |             |                                           |
  | 19          | Scratch file                              |
  +-------------+-------------------------------------------+

.. _7-6-4:

CHOPS Sample Input
------------------

The sample case in :numref:`list7-6-1` first executes a CENTRM unit cell
geometry calculation using the CSAS-MG sequence, which by default
generates the PW flux file on unit 15, as well as the CE nuclear data
library on unit 81 for input to CHOPS. The standalone CHOPS code then
computes a cell-homogenized CE library for the unit cell. The new
homogenized CENTRM CE library is output on unit 91with filename:
*ft91f001*

.. code-block:: scale
  :caption: CHOPS sample input.
  :name: list7-6-1

    =CSAS-MG      parm=centrm
   test case for CHOPS
  v7-252n
  READ COMP
  ' Fuel pellet
  o          1 0 4.59675e-2 900.0 end
  u-235   1 0 4.88385e-4 900.0 end
  u-238   1 0 2.24804e-2 900.0 end
  ' Clad
  zr         2 0 4.99789e-2 600.0 end
  ' Coolant
  h          3 0 4.76619e-2 600.0 end
  o          3 0 2.38310e-2 600.0 end
  END COMP
  READ CELLDATA
     latticecell squarepitch pitch=1.6  3
       fueld=1.262 1 cladd=1.350 2   end
  END CELLDATA
  END
  =CHOPS
  0$$  81 91 15 93 92  e
  1$$  a2 1 e
  2**  a3 1.0 e
   t
  END
