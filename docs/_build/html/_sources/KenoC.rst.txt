.. _8-1C:

Keno Appendix C: Sample problems
================================

This section contains sample problems to demonstrate some of the options
available in KENO in stand-alone mode. Because stand-alone KENO has no
means to read standard composition information and process for use, the
problem-dependent cross section library must be prepared before
executing KENO in the multigroup mode. The **MIXTURE** data block (See
:ref:`9-1-2-1`) is used to provide the mixing table. In the continuous
energy mode, the cross sections are directly used and therefore no
problem-dependent library is needed. The mixing table is required in the
continuous energy mode as well. If KENO is executed as part of CSAS5 or
CSAS6 sequence, generation of the problem-dependent library (for the
multigroup mode) and the mixing table is automatically performed by the
sequence.

A total of 33 KENO V.a different case inputs and 27 KENO-VI inputs are
provided as multigroup mode KENO sample problems in a single input file
“kenova.input” and “kenovi.input” for KENO V.a and KENO-VI,
respectively. This input file contains an initial CSAS-MG input to
create the problem-dependent cross section library to be used in the
sample problems in the input file. Although KENO does not run stacked
cases, when KENO is run as part of SCALE, the driver allows KENO to be
executed each time it encounters an “=KENO5” or “=KENOVA”, respectively
“=KENO6” or “=KENOVI.” The “.input” file contains all 33/27 problems one
after the other. A similar input file “cekenova.input”, respectively
“cekenovi.input” is also provided for continuous energy mode of
calculations. The changes required to create the continuous energy mode
input file from the multigroup mode input file are simple. The
continuous energy mode file does not have (or need) the CSAS-MG input at
the beginning. In addition, all “lib=4” entries in the PARAMETER data
block are changed to “cep=ce_v7_endf” to indicate the mode of
calculation is continuous energy and the continuous energy cross section
directory file is “ce_v7_endf” indicating ENDF/B-VII-based cross
sections. The mixing table entry SCT is not applicable in the continuous
energy mode, so it has been deleted from the continuous energy input
file. Finally, the nuclide IDs in the mixing table are modified to
remove the mixture number prefix because the continuous energy mode
cross section file for a nuclide or isotope is the same regardless of
where that nuclide is used.

The same 33/27 problems are also executed as individual cases with
filenames “k5smp??.input”, respectively “k6smp??.input”, where ?? stands
for sample problem number (01 through 33 or 27). Since each one of these
sample problems needs a problem-dependent cross section library
(multigroup mode only) and a mixing table, these problems have been
converted to run as CSAS5/6 problems. Similar input files are also
provided to be run in the continuous energy mode and the files are named
“cek5smp??.input”, respectively “cek6smp??.input”, where ?? again stands
for sample problem number (01 through 33 or 27). The change required to
create the continuous energy mode inputs from the multigroup mode inputs
is very simple: the cross-section library name is changed from “v7-238”
to “ce_v7”.

In the following section the input for each case is listed assuming the
multigroup mode of calculation in KENO. The KENO input is also listed in
the file corresponding “.input” file. The CSAS-MG input file for these
cases is in the next section.

.. _8-1c-1:

CSAS-MG data
------------

The multigroup mode KENO sample problems use nuclide IDs that are
consistent with the SCALE CSAS5/6 nuclide ID naming convention. Nuclides
are identified by the ZA number plus 1000000 times the mixture number.
CSAS-MG can be used to create a problem-dependent working format
cross-section library suitable for use with the sample problems. CSAS-MG
can (1) be run alone with problem-dependent working library on logical
Unit 4 saved for later use with the KENO sample problems, or (2) be
placed in front of the KENO sample problems.

The CSAS-MG SCALE control module calculates the necessary resonance data
required to create the problem-dependent AMPX working format library
using SCALE standard composition input.

The multigroup mode KENO sample problem input data are independent of
energy group structure. To use a different energy group structure,
simply supply the desired master cross-section library name in the
CSAS-MG or CSAS5/6 data. See XSProc, Standard Composition and CSAS5/6
chapters for additional information and examples. See the XSLib chapter
for information about the master format cross-section libraries that are
available in SCALE.

Data for CSAS-MG are provided to create a problem-dependent AMPX working
format cross-section library suitable for use with the multigroup mode
KENO sample problems. These data include all of the mixtures used in the
KENO sample problems and will create an AMPX working format
cross-section library with nuclide IDs matching those in the KENO sample
problem mixing tables. This cross-section library is problem-specific
and is not appropriate for use with other problems.

The CSAS-MG input data to produce an AMPX working format cross-section
library for the multigroup mode KENO V.a sample problems are given
below.

.. highlight:: scale

::

  =CSAS-MG
  csasn to prepare 238 group working format xsec lib for kenova smp prbs
  v7-238
  READ COMP
  ' uranium metal for smp prbs 1,2,3,4,5,6,7,8,9,10,11,12,19,22,23,24,25,26,27,28
    uranium  1 den=18.76 1 300 92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
  ' uranyl nitrate solution for smp prbs 12,18,19   spg=1.555
    solution  mix=2  rho[uo2(no3)2]=415 92235 92.6 92238 5.9 92234 1.0  92236 0.5
              molar[hno3]=9.783-3  temp=300 density=?   end solution
  ' uranium metal for smp prbs 13,14
    uranium  3 den=18.69 1 300  92235 93.2 92238 5.6 92234 1.0 92236 0.2 end
  ' uranium metal for smp prb 15
    uranium  4 den=18.794 1 300 92235 97.67 92238 1.03
                               92234 1.09  92236 0.21 end
  ' uranyl fluoride solution for smp prb 16
    solution  mix=5  rho[uo2f2]=578.7 92235 93.2 92238 6.8 temp=300 end solution
  ' borated uranyl fluoride solution for smp prb 16
    solution  mix=6  rho[uo2f2]=578.7 92235 93.2 92238 6.8 temp=300 end solution
    boron          6 den=.0266 end
  ' uranyl fluoride solution for smp prb 17
    solution  mix=7  rho[uo2f2]=133  92235 93.0  92238 7.0  temp=300 end solution
  ' uranyl fluoride solution for smp prb 20
    solution  mix=8  rho[uo2f2]=576.87 92235 93.2 92238 6.8 temp=300 end solution
  ' uranyl fluoride solution for smp prb 21     spg= 1.56
    solution  mix=9  rho[uo2f2]=494 92235 4.89 92238 95.09 92234 0.02
              temp=300  end solution
  ' paraffin for smp prbs 3,4,18
    paraffin 10 end
  ' plexiglas for smp prbs 12,15,18,19
    plexiglas 11 end
  ' water for smp prbs 15
    h2o 12 end
  ' pyrex glass for smp prb 16
    pyrex 13 end
  ' aluminum for smp prb 20,21
    al 14 end
  ' low density water for smp prb 18
    h2o 15 1-9 end
  ' uranium metal for smp prbs 29 - 32
    uranium  16 den=18.747 1 300  92235 93.21 92238 5.7697 92234 0.9844
                                  92236  0.0359 end
  ' uranium metal for water moderated portion of smp prb 33
    uranium  17 den=19.0 1 300  92235 1.95 92238 98.042 92234 0.002 92236 0.006  end
  ' internal (2nd) moderator water for smp prb 33
    h2o      18 end
  ' external moderator water and reflector for smp prb 33
    h2o      19 end
  ' uranium metal for bare portion of smp prb 33
    uranium  20 den=19.0 1 300  92235 1.95 92238 98.042 92234 0.002 92236 0.006  end
  END COMP
  READ CELLDATA
  'latticecell data for samp prb 33
    latticecell atriangpitch  pitch=20.828 19 fueld=18.288 17 imodd=6.604 18 end
    latticecell atriangpitch  pitch=20.828  0 fueld=18.288 20 imodd=6.604  0 end
  END CELLDATA
  END

.. _8-1c-2:

KENO V.a sample problem data
----------------------------

A brief problem description and the associated input data are included
for each multigroup mode KENO sample problem. Different options may be
easily activated by making changes in the data. These problems are set
up using an AMPX working format library which was created by a CSAS-MG
case just prior to the KENO V.a cases. The nuclide identifiers for this
library are consistent with the SCALE identifiers created by CSAS-MG.
Input data to create this library are given in :ref:`8-1c-1`. The unit
number is defined by the parameter LIB= in the parameter data.

.. _8-1c-2-1:

Sample Problem 1   2C8 BARE
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a simple 2 × 2 × 2 array of uranium metal cylinders as described
in the article “Critical Three-Dimensional Arrays of U(93.2)-Metal
Cylinders,” :cite:`thomas_critical_1973` by J. T. Thomas. This critical experiment is designated
in Table II of that article as cylinder index 11 and reflector index 1.
:numref:`fig8-1c-1` shows the critical experiment.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 1  case 2c8 bare
  READ PARAMETERS
    flx=yes fdn=yes far=yes gas=no lib=4
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1
      1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05 1092238 2.65767e-03
  END MIXT
  READ GEOMETRY
    unit 1
      cylinder 1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.87 -6.87 6.87 -6.87 6.505 -6.505
  END GEOMETRY
  READ ARRAY
    nux=2 nuy=2 nuz=2
  END ARRAY
  END DATA
  END

KENO-VI

::

  =KENOVI
  kenovi  sample problem 1  case 2c8 bare
  READ PARAMETERS
    flx=yes fdn=yes far=yes gas=no lib=4
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1 1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05
          1092238 2.65767e-03
  END MIXT
  READ GEOMETRY
    unit 1
      com='single 2c8 unit centered'
      cylinder 10  5.748 5.3825 -5.3825
      cuboid   20  4p6.87 2p6.505
      media  1 1 10      vol=8938.968624
      media  0 1 20 -10  vol=10710.044784
      boundary 20
    global unit 2
      cuboid 10  4p13.74 2p13.01
      com='2x2x2  2c8 array'
      array 1 +10 place 1 1 1 2r-6.87 -6.505
      boundary  10
  END GEOMETRY
  READ ARRAY
    ara=1 nux=2 nuy=2 nuz=2  fill f1  end fill
  END ARRAY
  END DATA
  END

.. _fig8-1c-1:
.. figure:: figs/KenoC/fig1.png
  :align: center
  :width: 400

  Critical 2C8 bare assembly.

.. _8-1c-2-2:

Sample Problem 2  CASE 2C8 BARE WITH 8 UNIT TYPES MATRIX CALCULATION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem is the same as sample problem 1 except it is set up as a
mixed unit problem with each unit of the array defined as a different
unit type. Matrix k-effectives will be calculated for this problem by
both unit type and array position. The print flags are set to print all
matrix data.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 2  2c8 bare with 8 unit types matrix calculation
  READ PARAM
    lib=4  flx=yes fdn=yes
    mku=yes fmu=yes mkp=yes fmp=yes
  END PARAM
  READ GEOMETRY
    unit 1
      cylinder  1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.87 -6.87 6.87 -6.87 6.505 -6.505
    unit 2
      cylinder  1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.87 -6.87 6.87 -6.87 6.505 -6.505
    unit 3
      cylinder  1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.87 -6.87 6.87 -6.87 6.505 -6.505
    unit 4
      cylinder  1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.87 -6.87 6.87 -6.87 6.505 -6.505
    unit  5
      cylinder  1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.87 -6.87 6.87 -6.87 6.505 -6.505
    unit 6
      cylinder  1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.87 -6.87 6.87 -6.87 6.505 -6.505
    unit 7
      cylinder  1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.87 -6.87 6.87 -6.87 6.505 -6.505
    unit 8
      cylinder  1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.87 -6.87 6.87 -6.87 6.505 -6.505
  END GEOM
  READ MIXT
    sct=2
    mix=1
      1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05 1092238 2.65767e-03
  END MIXT
  READ ARRAY
    nux=2 nuy=2 nuz=2  loop
      10*1
      3*2 7*1
      3 1 1 1 2 2 1 1 1 1
      4 2 2 1 2 2 1 1 1 1
      5 6*1 2 2 1
      6 2 2 1 1 1 1 2 2 1
      7  1 1 1 2 2 1 2 2 1
      8 2 2 1 2 2 1 2 2 1    end loop
  END ARRAY
  END DATA
  END

KENO-VI

::

  =KENOVI
  kenovi sample problem 2  case 2c8 bare with 8 unit types matrix cal
  READ PARAM
    lib=4 flx=yes fdn=yes mku=yes cku=yes fmu=yes mkp=yes ckp=yes fmp=yes
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1 1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05
          1092238 2.65767e-03
  END MIXT
  READ GEOMETRY
    unit 1
      cylinder 10 5.748 5.3825 -5.3825
      cuboid   20 4p6.87 2p6.505
      media  1 1 10     vol=1117.371078
      media  0 1 20 -10 vol=1338.755598
      boundary   20
    unit 2
      cylinder 10  5.748 5.3825 -5.3825
      cuboid   20  4p6.87 2p6.505
      media  1 1 10     vol=1117.371078
      media  0 1 20 -10 vol=1338.755598
      boundary   20
    unit 3
      cylinder 10  5.748 5.3825 -5.3825
      cuboid   20  4p6.87 2p6.505
      media  1 1 10     vol=1117.371078
      media  0 1 20 -10 vol=1338.755598
      boundary  20
    unit 4
      cylinder 10  5.748 5.3825 -5.3825
      cuboid   20  4p6.87 2p6.505
      media  1 1 10     vol=1117.371078
      media  0 1 20 -10 vol=1338.755598
      boundary 20
    unit 5
      cylinder 10  5.748 5.3825 -5.3825
      cuboid   20  4p6.87 2p6.505
      media  1 1 10     vol=1117.371078
      media  0 1 20 -10 vol=1338.755598
      boundary  20
    unit 6
      cylinder 10  5.748 5.3825 -5.3825
      cuboid   20 4p6.87 2p6.505
      media  1 1 10     vol=1117.371078
      media  0 1 20 -10 vol=1338.755598
      boundary  20
    unit 7
      cylinder 10  5.748 5.3825 -5.3825
      cuboid   20 4p6.87 2p6.505
      media  1 1 10     vol=1117.371078
      media  0 1 20 -10 vol=1338.755598
      boundary 20
    unit 8
      cylinder 10  5.748 5.3825 -5.3825
      cuboid   20 4p6.87 2p6.505
      media  1 1 10     vol=1117.371078
      media  0 1 20 -10 vol=1338.755598
      boundary  20
    global unit 9
      cuboid  10 4p13.74 2p13.01
      com='2x2x2  2c8 array'
      array 1 +10 place 1 1 1 2r-6.87 -6.505
      boundary  10
  END GEOMETRY
  READ ARRAY
   ara=1 nux=2 nuy=2 nuz=2  gbl=1
   loop  10*1
         3*2 7*1
         3 1 1 1 2 2 1 1 1 1
         4 2 2 1 2 2 1 1 1 1
         5 6*1 2 2 1
         6 2 2 1 1 1 1 2 2 1
         7  1 1 1 2 2 1 2 2 1
         8 2 2 1 2 2 1 2 2 1 end loop
  END ARRAY
  END DATA
  END

.. _8-1c-2-3:

Sample Problem 3  2C8  15.24-CM PARAFFIN REFL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A 2 × 2 × 2 array of uranium metal cylinders is reflected by 6 in. of
paraffin on all faces (:numref:`fig8-1c-1`). This critical
experiment\ :sup:`1` is designated as cylinder index 11 and reflector
index 5 in Table II of Ref. 1. :numref:`fig8-1c-2` shows half of the critical
experiment, which consisted of the half shown and the mirror image of
it. These two assemblies were moved together to achieve criticality. The
top reflector is missing in :numref:`fig8-1c-2`, but was present when
criticality was achieved.

.. _fig8-1c-2:
.. figure:: figs/KenoC/fig2.png
  :align: center
  :width: 500

  Half of the paraffin reflected 2C8 assembly before the top reflector was added.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 3  2c8  15.24 cm paraffin refl
  READ PARAM
    lib=4  flx=yes fdn=yes pwt=yes
  END PARAM
  READ ARRAY
    nux=2 nuy=2 nuz=2
  END ARRAY
  READ MIXT
    mix=1
      1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05 1092238 2.65767e-03
    mix=2
      10006000 3.84193e-02 10001901 7.99120e-02
    sct=2
  END MIXT
  READ GEOM
    unit 1
      cylinder  1 1 5.748 5.3825 -5.3825
      cuboid  0 1 11.74 -11.74 11.74 -11.74 11.375 -11.375
    global unit 2
      array   1 -23.48 -23.48 -22.75
      cuboid  2 2 26.48 -26.48 26.48 -26.48 25.75 -25.75
      cuboid  2 3 29.48 -29.48 29.48 -29.48 28.75 -28.75
      cuboid  2 4 32.48 -32.48 32.48 -32.48 31.75 -31.75
      cuboid  2 5 35.48 -35.48 35.48 -35.48 34.75 -34.75
      cuboid  2 6 38.72 -38.72 38.72 -38.72 37.99 -37.99
  END GEOM
  READ BIAS
    id=400 2 6
  END BIAS
  END DATA
  END

  KENO-VI

  =KENOVI
  keno-vi sample problem 3  2c8  15.24 cm paraffin refl
  READ PARAM
    lib=4 flx=yes fdn=yes pwt=yes
  END PARAM
  READ MIXT
    sct=2
    mix=1 1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05
          1092238 2.65767e-03
    mix=2 10006000 3.84193e-02 10001901 7.99120e-02
  END MIXT
  READ GEOMETRY
    unit 1
      com='single 2c8 unit centered'
      cylinder 10  5.748 5.3825 -5.3825
      cuboid   20  4p11.74 2p11.375
      media  1 1 10      vol=8938.968624
      media  0 1 20 -10  vol=10710.044784
      boundary  20
    global unit 2
      com='2x2x2  2c8 array with reflector'
      cuboid 10 4p23.48 2p22.75
      cuboid 20   26.48 -26.48 26.48 -26.48 25.75 -25.75
      cuboid 30   29.48 -29.48 29.48 -29.48 28.75 -28.75
      cuboid 40   32.48 -32.48 32.48 -32.48 31.75 -31.75
      cuboid 50   35.48 -35.48 35.48 -35.48 34.75 -34.75
      cuboid 60   38.72 -38.72 38.72 -38.72 37.99 -37.99
      array 1 +10 place 1 1 1 2r-11.74 -11.375
      media  2 2 -10 +20  vol=4.41067E+04
      media  2 3 -20 +30  vol=5.54410E+04
      media  2 4 -30 +40  vol=6.80712E+04
      media  2 5 -40 +50  vol=8.19974E+04
      media  2 6 60 -50   vol=1.05694E+05
      boundary  60
  END GEOMETRY
  READ BIAS
    id=400 2 6
  END BIAS
  READ ARRAY
    ara=1 nux=2 nuy=2 nuz=2 fill f1 end fill
  END ARRAY
  END DATA
  END

.. _8-1c-2-4:

Sample Problem 4  2C8  15.24-CM PARAFFIN REFL AUTOMATIC REFL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem is the same as sample problem 3 except it is set up using more reflector regions.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 4  2c8 15.24 cm paraffin refl automatic refl
  READ PARAM
    pwt=yes lib=4  flx=yes fdn=yes
  END PARAM
  READ GEOMETRY
    unit 1
      cylinder  1 1 5.748 5.3825 -5.3825
      cuboid  0 1 11.74 -11.74 11.74 -11.74 11.375 -11.375
    global unit 2
      array      1 -23.48 -23.48 -22.75
      reflector  2 2 6*3.0 5
      reflector  2 7 6*.24 1
  END GEOM
  READ MIXT
    sct=2
    mix=1
      1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05 1092238 2.65767e-03
    mix=2
      10006000 3.84193e-02 10001901 7.99120e-02
  END MIXT
  READ ARRA
    nux=2 nuy=2 nuz=2
  END ARRAY
  READ BIAS
    id=400 2 7
  END BIAS
  END DATA
  END

KENO-VI

::

  =KENOVI
  keno-vi sample problem 4  2c8  15.24 cm paraffin refl
  READ PARAM
    lib=4 flx=yes fdn=yes pwt=yes
  END PARAM
  READ MIXT
    sct=2
    mix=1 1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05
          1092238 2.65767e-03
    mix=2 10006000 3.84193e-02 10001901 7.99120e-02
  END MIXT
  READ GEOMETRY
    unit 1
      com='single 2c8 unit centered'
      cylinder 10  5.748 5.3825 -5.3825
      cuboid   20  4p11.74 2p11.375
      media  1 1 10
      media  0 1 20 -10
      boundary  20
    global unit 2
      com='2x2x2  2c8 array with reflector'
      cuboid 10 4p23.48 2p22.75
      cuboid 20   26.48 -26.48 26.48 -26.48 25.75 -25.75
      cuboid 30   29.48 -29.48 29.48 -29.48 28.75 -28.75
      cuboid 40   32.48 -32.48 32.48 -32.48 31.75 -31.75
      cuboid 50   35.48 -35.48 35.48 -35.48 34.75 -34.75
      cuboid 60   38.48 -38.48 38.48 -38.48 37.75 -37.75
      cuboid 70   38.72 -38.72 38.72 -38.72 37.99 -37.99
      array 1 +10 place 1 1 1 2r-11.74 -11.375
      media  2 2 -10 +20
      media  2 3 -20 +30
      media  2 4 -30 +40
      media  2 5 -40 +50
      media  2 6  60 -50
      media  2 7  70 -60
      boundary 70
  END GEOMETRY
  READ VOLUME
     type=trace
  END VOLUME
  READ BIAS
    id=400 2 7
  END BIAS
  READ ARRAY
    ara=1 nux=2 nuy=2 nuz=2 fill f1 end fill
  END ARRAY
  END DATA
  END

.. _8-1c-2-5:

Sample Problem 5  2C8  12-INCH PARAFFIN ALBEDO REFLECTOR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem is the same as samples problems 3 and 4 except the
reflector is represented by a 12‑in. paraffin albedo. Note the decrease
in execution time when using an albedo reflector instead of doing actual
tracking. Note also that k-effective is somewhat higher for this system,
probably due to the small edge size of the system :cite:`whitesides_use_1969`.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 5  2c8 12 inch paraffin albedo reflector
  READ PARA
    flx=yes far=yes gas=no fdn=yes lib=4
  END PARA
  READ ARRAY
    nux=2 nuy=2 nuz=2
  END ARRAY
  READ MIXT
    mix=1
      1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05 1092238 2.65767e-03
    sct=2
  END MIXT
  READ BOUNDS
    all=paraffin
  END BOUNDS
  READ GEOM
    unit 1
      cylinder  1 1 5.748 5.3825 -5.3825
      cuboid  0 1 11.74 -11.74 11.74 -11.74 11.375 -11.375
  END GEOM
  END DATA
  END

KENO-VI

::

  =KENOVI
  kenovi sample problem 5  2c8 12 inch paraffin albedo reflector
  READ PARA
    flx=yes far=yes gas=no fdn=yes lib=4
  END PARA
  READ MIXT
    sct=2
    mix=1 1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05
          1092238 2.65767e-03
  END MIXT
  READ BOUNDS
    all=paraffin
  END BOUNDS
  READ GEOMETRY
    unit 1
      com='single 2c8 unit centered'
      cylinder 10  5.748 5.3825 -5.3825
      cuboid   20 4p11.74 2p11.375
      media  1 1 10
      media  0 1 20 -10
      boundary  20
    global unit 2
      cuboid 10  4p23.48 2p22.75
      com='2x2x2  2c8 array'
      array 1 +10 place 1 1 1 2r-11.74 -11.375
      boundary 10
  END GEOMETRY
  READ ARRAY
    ara=1 nux=2 nuy=2 nuz=2  fill f1 end fill
  END ARRAY
  READ VOLUME
    type=random
  END VOLUME
  END DATA
  END

.. _8-1c-2-6:

Sample Problem 6  ONE 2C8 UNIT (SINGLE UNIT)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of the 2C units\ :sup:`1` is described and run as a single-unit
problem, and its k-effective is calculated.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 6  one 2c8 unit (single unit)
  READ PARA
    lib=4  flx=yes fdn=yes far=yes gas=no
  END PARA
  READ MIXT
    sct=2
    mix=1
      1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05 1092238 2.65767e-03
  END MIXT
  READ GEOMETRY
    unit 1
      cylinder  1 1 5.748 5.3825 -5.3825
  END GEOMETRY
  END DATA
  END

KENO-VI

::

  =KENOVI
  kenovi sample problem 6  one 2c8 unit (single unit)
  READ PARA
    lib=4 flx=yes fdn=yes far=yes gas=no
  END PARA
  READ MIXT
    sct=2
    mix=1 1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05
          1092238 2.65767e-03
  END MIXT
  READ GEOMETRY
    global unit 1
      com='single 2c8 unit centered'
      cylinder 10  5.748 5.3825 -5.3825
      media  1 1 10  vol=1117.3710776
      boundary  10
  END GEOMETRY
  END DATA
  END

.. _8-1c-2-7:

Sample Problem 7  BARE 2C8 USING SPECULAR REFLECTION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One of the 2C units\ :sup:`1` is described and the 2 × 2 × 2 array is
simulated by using specular reflection on the positive X, Y, and Z faces
of the unit. This is a simulation of sample problem 1.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 7  bare 2c8 using specular reflection
  READ PARA
    lib=4  flx=yes fdn=yes far=yes gas=no
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1
      1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05 1092238 2.65767e-03
  END MIXT
  READ GEOM
    unit 1
      cylinder  1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.87 -6.87 6.87 -6.87 6.505 -6.505
  END GEOM
  READ BOUNDS
    +fc=specular
  END BOUNDS
  END DATA
  END

KENO-VI

::

  =KENOVI
  keno-vi  sample problem 7  bare 2c8 using specular reflection
  READ PARA
    flx=yes fdn=yes far=yes gas=no lib=4
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1 1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05
          1092238 2.65767e-03
  END MIXT
  READ GEOMETRY
    global unit 1
      com='single 2c8 unit centered'
      cylinder 10  5.748 5.3825 -5.3825
      cuboid   20  4p6.87 2p6.505
      media  1 1 10      vol=1117.371078
      media  0 1 20 -10  vol=1338.755598
      boundary  20
  END GEOMETRY
  READ BOUNDS
    +fc=specular
  END BOUNDS
  END DATA
  END

.. _8-1c-2-8:

Sample Problem 8  INFINITELY LONG CYLINDER FROM 2C8 UNIT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The fuel and cylinder radius from sample problem 1 is used. The length
of the cylinder is arbitrarily chosen to be 20 cm, and the unit is
specularly reflected on the top and bottom to create an infinitely long
cylinder.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 8  infinitely long cylinder from 2c8 unit
  READ PARAM
    lib=4
  END PARAM
  READ MIXT
    sct=2
    mix=1
      1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05 1092238 2.65767e-03
  END MIXT
  READ GEOMETRY
    unit 1
      cylinder  1 1 5.748 10.0 -10.0
      cuboid  0 1 6.87 -6.87 6.87 -6.87 10.0 -10.0
  END GEOMETRY
  READ BOUNDS
    zfc=mirror
  END BOUNDS
  END DATA
  END

KENO-VI

::

  =KENOVI
  keno-vi  sample problem 8 infinitely long cylinder from 2c8 unit
  READ PARAMETERS
    lib=4
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1 1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05
          1092238 2.65767e-03
  END MIXTURES
  READ GEOMETRY
    global unit 1
      com='single 2c8 unit centered'
      cylinder 10  5.748 2p10.0
      cuboid   20  4p6.87 2p10.0
      media  1 1 10
      media  0 1 20 -10
      boundary  20
  END GEOMETRY
  READ BOUNDS
    zfc=mirror
  END BOUNDS
  READ VOLUME
    type=trace  iface=zface
  END VOLUME
  END DATA
  END

.. _8-1c-2-9:

Sample Problem 9  INFINITE ARRAY OF 2C8 UNITS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 9  infinite array of 2c8 units
  READ PARAM
    lib=4  gen=103
  END PARAM
  READ MIXT
    sct=2
    mix=1
      1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05 1092238 2.65767e-03
  END MIXT
  READ BOUN
    all=mir
  END BOUN
  READ GEOM
    unit 1
      cylinder  1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.87 -6.87 6.87 -6.87 6.505 -6.505
  END GEOM
  END DATA
  END

KENO-VI

::

  =KENOVI
  keno-vi  sample problem 9  infinite array of 2c8 units
  READ PARAMETERS
    lib=4
  END PARAMETERS
  READ MIXTURES
    sct=2
    mix=1 1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05
          1092238 2.65767e-03
  END MIXT
  READ GEOMETRY
    global unit 1
      com='single 2c8 unit centered'
      cylinder 10  5.748 5.3825 -5.3825
      cuboid   20  4p6.87 2p6.505
      media  1 1 10      vol=1117.371078
      media  0 1 20 -10  vol=1338.755598
      boundary  20
  END GEOMETRY
  READ BOUNDS
    all=mirror
  END BOUNDS
  END DATA
  END

.. _8-1c-2-10:

Sample Problem 10  2C8 BARE  WRITE RESTART
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The geometry description from sample problem 1 is used, and the cuboid
is specularly reflected on all faces to create an infinite array of 2C8
units having an edge-to-edge spacing of 2.244 cm in the X and
Y directions and 2.245 cm in the Z direction.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 10  case 2c8 bare  write restart
  READ PARAMETERS
    flx=yes fdn=yes far=yes gas=no lib=4  res=5 wrs=94
    app=yes
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1
      1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05 1092238 2.65767e-03
  END MIXT
  READ GEOMETRY
    unit 1
      cylinder 1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.87 -6.87 6.87 -6.87 6.505 -6.505
  END GEOMETRY
  READ ARRAY
    nux=2 nuy=2 nuz=2
  END ARRAY
  END DATA
  END

KENO-VI

::

  =KENOVI
  sample problem 10  case 2c8 bare  write restart
  READ PARAMETERS
    flx=yes fdn=yes far=yes gas=no lib=4 res=5 wrs=94 app=yes
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1 1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05
          1092238 2.65767e-03
  END MIXTURES
  READ GEOMETRY
    unit 1
      com='single 2c8 unit centered'
      cylinder 10  5.748 5.3825 -5.3825
      cuboid   20  4p6.87 2p6.505
      media  1 1 10      vol=8938.968624
      media  0 1 20 -10  vol=10710.044784
      boundary  20
    global unit 2
      cuboid 10  4p13.74 2p13.01
      com='2x2x2  2c8 array'
      array 1 +10 place 1 1 1 2r-6.87 -6.505
      boundary  10
  END GEOMETRY
  READ ARRAY
    ara=1 nux=2 nuy=2 nuz=2  fill f1  end fill
  END ARRAY
  END DATA
  END

.. _8-1c-2-11:

Sample Problem 11  2C8 BARE  READ RESTART DATA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem is a restart of sample problem 10. The problem is restarted
from the tenth set of restart data that was written by sample problem 10
(i.e., it restarts with the fifty-first generation).

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 11  2c8 bare  read restart data
  READ PARAM
    beg=51  rst=94 res=0
  END PARAM
  END DATA
  END

KENO-VI

::

  =KENOVI
  sample problem 11  2c8 bare  read restart data
  READ PARAM
    beg=51 rst=94 res=0
  END PARAM
  END DATA
  END

.. _8-1c-2-12:

Sample Problem 12  4 AQUEOUS 4 METAL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem is a critical experiment consisting of a
composite array\ :sup:`1` of four highly enriched uranium metal
cylinders and four cylindrical Plexiglas containers filled with uranyl
nitrate solution. The metal units in this experiment are designated in
Table II of Ref. 1 as cylinder index 11 and reflector index 1. A
photograph of the experiment is given in :numref:`fig8-1c-3`.

.. _fig8-1c-3:
.. figure:: figs/KenoC/fig3.png
  :align: center
  :width: 500

  Critical assembly of 4 solution units and 4 metal units.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 12 4 aqueous 4 metal mixed units
  READ PARAM
    lib=4 fdn=yes nub=yes smu=yes mkp=yes
    mku=yes fmp=yes fmu=yes
  END PARAM
  READ MIXT
    sct=2
    mix=1
      1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05 1092238 2.65767e-03
    mix=2
      2001001 5.77931e-02   2007014 2.13092e-03   2008016 3.74114e-02
      2092234 1.06784e-05   2092235 9.84602e-04   2092236 5.29386e-06
      2092238 6.19414e-05
    mix=3
     11001001 5.67873e-02  11006000 3.54921e-02  11008016 1.41968e-02
  END MIXT
  READ GEOM
    unit 1
      cylinder  2 1 9.525 8.89 -8.89
      cylinder  3 1 10.16 9.525 -9.525
      cuboid  0 1 10.875 -10.875 10.875 -10.875 10.24 -10.24
    unit  2
      cylinder  1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.59 -15.16 6.59 -15.16 6.225 -14.255
    unit  3
      cylinder  1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.59 -15.16 15.16 -6.59 6.225 -14.255
    unit  4
      cylinder  1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.59 -15.16 6.59 -15.16 14.255 -6.225
    unit  5
      cylinder  1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.59 -15.16 15.16 -6.59 14.255 -6.225
  END GEOM
  READ ARRAY
    gbl=1 ara=1 nux=2 nuy=2 nuz=2  loop
      1 3r2 1 2 1 1 2 1
      2 9r1
      3 3r1 2 2 1 3r1
      4 6r1 2 2 1
      5 3r1 2 2 1 2 2 1  end loop
  END ARRAY
  END DATA
  END

KENO-VI

::

  =KENOVI
  sample problem 12 4 aqueous 4 metal mixed units
  READ PARAM
    lib=4  flx=yes fdn=yes nub=yes smu=yes mku=yes fmp=yes fmu=yes
  END PARAM
  READ MIXT
    sct=2
    mix=1  1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05
           1092238 2.65767e-03
    mix=2  2001001 5.77931e-02   2007014 2.13092e-03   2008016 3.74114e-02
           2092234 1.06784e-05   2092235 9.84602e-04   2092236 5.29386e-06
           2092238 6.19414e-05
    mix=3 11001001 5.67873e-02  11006000 3.54921e-02  11008016 1.41968e-02
  END MIXT
  READ GEOM
    unit 1
      cylinder 10  9.525 8.89 -8.89
      cylinder 20  10.16 9.525 -9.525
      cuboid   30  10.875 -10.875 10.875 -10.875 10.24 -10.24
      media 2 1 10      vol=20270.8327
      media 3 1 -10 20  vol=4440.27764
      media 0 1 30 -20  vol=14042.16966
      boundary  30
    unit      2
      cylinder 10  5.748 5.3825 -5.3825
      cuboid   20  6.59 -15.16 6.59 -15.16 6.225 -14.255
      media 1 1 10      vol=1117.371078
      media 0 1 20 -10  vol=8570.948922
      boundary  20
    unit      3
      cylinder 10  5.748 5.3825 -5.3825
      cuboid   20  6.59 -15.16 15.16 -6.59 6.225 -14.255
      media 1 1 10      vol=1117.371078
      media 0 1 20 -10  vol=8570.948922
      boundary  20
    unit      4
      cylinder 10  5.748 5.3825 -5.3825
      cuboid   20  6.59 -15.16 6.59 -15.16 14.255 -6.225
      media 1 1 10      vol=1117.371078
      media 0 1 20 -10  vol=8570.948922
      boundary  20
    unit      5
      cylinder 10  5.748 5.3825 -5.3825
      cuboid   20  6.59 -15.16 15.16 -6.59 14.255 -6.225
      media 1 1 10      vol=1117.371078
      media 0 1 20 -10  vol=8570.948922
      boundary  20
    global
    unit  6
      cuboid 10  43.5 0.0 43.5 0.0 40.96 0.0
      array 1 +10 place 1 1 1 15.16 15.16 14.255
      boundary  10
  END GEOM
  READ ARRAY
    gbl=1 ara=1 nux=2 nuy=2 nuz=2  loop
    1 3r2 1 2 1 1 2 1
    2 9r1
    3 3r1 2 2 1 3r1
    4 6r1 2 2 1
    5 3r1 2 2 1 2 2 1  end loop
  END ARRAY
  END DATA
  END

.. _8-1c-2-13:

Sample Problem 13  TWO CUBOIDS IN A CYLINDRICAL ANNULUS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This critical experiment :cite:`irving_monte_1964` consists of two assemblies of 93.2%
:sup:`235`\ U-enriched uranium metal (ρ = 18.69 g/cc) stacked
vertically. The bottom assembly contains a uranium metal cuboid offset
to the left within a uranium metal cylindrical annulus. The top assembly
contains a uranium metal cuboid offset to the right within a uranium
metal cylindrical annulus. The cuboid extends above the annulus. A
drawing of the two sections and the total assembly is given in
:numref:`fig8-1c-4`.

.. _fig8-1c-4:
.. figure:: figs/KenoC/fig4.png
  :align: center
  :width: 500

  Drawing of two cuboids in an annulus critical assembly.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 13  two cuboids in a cylindrical annulus
  READ PARAM
     lib=4
  END PARAM
  READ GEOM
    unit 1
      cuboid  1 1 6.35 -6.35 6.35 -6.35 7.62 0.0
      cylinder  0 1 13.97 7.62 0.0 orig -6.0934 0.0
      cylinder  1 1 19.05 7.62 0.0 orig -6.0934 0.0
      cuboid  0 1 12.9566 -25.1434 19.05 -19.05 7.62 0.0
    unit 2
      cuboid  1 1 6.35 -6.35 6.35 -6.35 8.56 0.0
      cylinder  0 1 13.97 8.56 0.0 origin 6.0934 0.0
      cylinder  1 1 19.05 8.56 0.0 origin 6.0934 0.0
      cuboid  0 1 25.1434 -12.9566 19.05 -19.05 8.56 0.0
    unit 3
      cuboid  1 1 6.35 -6.35 6.35 -6.35 2.616 0.0
      cuboid  0 1 25.1434 -12.9566 19.05 -19.05 2.616 0.0
  END GEOM
  READ MIXT
    sct=2
    mix=1
      3092234 4.80916e-04  3092235 4.46300e-02  3092236 9.53661e-05 3092238 2.64776e-03
  END MIXT
  READ ARRAY
    gbl=1 nux=1 nuy=1 nuz=3  fill 1 2 3 t
  END ARRAY
  END DATA
  END

KENO-VI

::

  =KENOVI
  sample problem 13  two cuboids in a cylindrical annulus
  READ PARAM
    lib=4
  END PARAM
  READ MIXT
    sct=2
    mix=1  3092234 4.80916e-04  3092235 4.46300e-02  3092236 9.53661e-05
           3092238 2.64776e-03
  END MIXT
  READ GEOM
    unit 1
      cuboid    10 6.35 -6.35 6.35 -6.35 7.62 0.0
      cylinder  20 13.97 7.62 0.0 orig x=-6.0934
      cylinder  30 19.05 7.62 0.0 orig x=-6.0934
      cuboid    40 12.9566 -25.1434 19.05 -19.05 7.62 0.0
      media  1 1 10     vol=1229.0298
      media  0 1 20 -10 vol=3442.914497898
      media  1 1 30 -20 vol=4015.555429598
      media  0 1 40 -30 vol=2373.768472504
      boundary  40
    unit 2
      cuboid   10 6.35 -6.35 6.35 -6.35 8.56 0.0
      cylinder 20  13.97 8.56 0.0 origin x=6.0934
      cylinder 30  19.05 8.56 0.0 origin x=6.0934
      cuboid   40 25.1434 -12.9566 19.05 -19.05 8.56 0.0
      media  1 1 10     vol=1380.6424
      media  0 1 20 -10 vol=3867.630984515
      media  1 1 30 -20 vol=4510.912661071
      media  0 1 40 -30 vol=2666.595554414
      boundary  40
    unit 3
      cuboid 10  6.35 -6.35 6.35 -6.35 2.616 0.0
      cuboid 20 25.1434 -12.9566 19.05 -19.05 2.616 0.0
      media  1 1 10     vol=421.93464
      media  0 1 20 -10 vol=3375.47712
      boundary  20
    global unit 4
      cuboid  10 12.9566 -25.1434 2p19.05 18.796 0.
      array 1 10 place 1 1 1 3r0.
      boundary  10
  END GEOM
  READ ARRAY
    ara=1 nux=1 nuy=1 nuz=3  fill 1 2 3 end fill
  END ARRAY
  END DATA
  END

.. _8-1c-2-14:

Sample Problem 14  U METAL CYLINDER IN AN ANNULUS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This critical experiment\ :sup:`3` consists of a 93.2
:sup:`235`\ U-enriched uranium metal cylinder within a cylindrical
annulus of the same material as shown in :numref:`fig8-1c-5`. The uranium
metal specification is identical to that used in sample problem 13.

.. _fig8-1c-5:
.. figure:: figs/KenoC/fig5.png
  :align: center
  :width: 500

  Drawing of the cylinder in an annulus critical assembly.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 14  u metal cylinder in an annulus
  READ PARAM
    lib=4
  END PARAM
  READ MIXT
    sct=2
    mix=1
      3092234 4.80916e-04  3092235 4.46300e-02  3092236 9.53661e-05 3092238 2.64776e-03
  END MIXT
  READ GEOM
    global unit 1
      cylinder  1 1 8.89 10.109 0.0 orig 5.0799 0.0
      cylinder  0 1 13.97 10.109 0.0
      cylinder  1 1 19.05 10.109 0.0
  END GEOM
  END DATA
  END

KENO-VI

::

  =KENOVI
  sample problem 14  u metal cylinder in an annulus
  READ PARAM
    lib=4
  END PARAM
  READ MIXT
    SCT=2
    mix=1  3092234 4.80916e-04  3092235 4.46300e-02  3092236 9.53661e-05
           3092238 2.64776e-03
  END MIXT
  READ GEOM
    global unit 1
      cylinder 10  8.89 10.109 0.0 orig x=5.08
      cylinder 20  13.97 10.109 0.0
      cylinder 30  19.05 10.109 0.0
      media  1 1 10          vol=2509.929894
      media  0 1 20 -10      vol=3688.060252
      media  1 1 30 -20 -10  vol=5327.198142
      boundary  30
  END GEOM
  END DATA
  END

.. _8-1c-2-15:

Sample Problem 15  SMALL WATER REFLECTED SPHERE ON PLEXIGLAS COLLAR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This critical experiment :cite:`byers_critical_1977` is a small highly enriched uranium sphere
supported by a Plexiglas doughnut in a tank of water. The sphere extends
down through the hole of the doughnut. However, the KENO geometry
package cannot rigorously describe a doughnut (torus) with either KENO
V.a or KENO-VI. Therefore, the KENO mockup of this problem describes the
doughnut as an annular cylindrical plate and the sphere is supported by
it. Both are contained in a cylindrical tank of water. A drawing of the
experiment is given in :numref:`fig8-1c-6`. This drawing shows the sphere
above the cylindrical collar for the sake of clarity. The sphere is
actually supported by the collar and extends into the opening in its
center. The actual experiment utilized a torus or doughnut instead of a
cylindrical collar.

.. _fig8-1c-6:
.. figure:: figs/KenoC/fig6.png
  :align: center
  :width: 400

  Drawing of a critical assembly consisting of a uranium sphere on a Plexiglas collar with a cylindrical water reflector.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 15  small water reflected sphere on plexiglas collar
  READ PARAM
    lib=4  flx=yes fdn=yes
  END PARAM
  READ MIXT
    sct=2
    mix=1
       4092234 5.27115e-04  4092235 4.70308e-02  4092236 1.00692e-04 4092238 4.89708e-04
    mix=2
      11001001 5.67873e-02  11006000 3.54921e-02  11008016 1.41968e-02
    mix=3
      12001001 6.67554e-02
    mix=3
      12008016 3.33757e-02
  END MIXT
  READ GEOM
    unit 1
      hemisphe-z 1 1 6.5537 chord -5.09066
      cylinder  3 1 4.1275 -5.09066 -7.63065
      cylinder  2 1 12.7   -5.09066 -7.63065
      cuboid  3 1 4p12.7 -5.09066 -7.63065
    unit 2
      hemisphe+z 1 1 6.5537 chord 5.09066
      cuboid  3 1 4p12.7 6.5537 -5.09066
    global unit 3
      array     1 -12.7 -12.7 -7.092175
      cylinder  3 1 17.97 2p7.0922
      replicate 3 2 3*3.0 5
  END GEOM
  READ BIAS
    id=500 2 6
  END BIAS
  READ ARRAY
    nux=1 nuy=1 nuz=2  fill 1 2 end fill
  END ARRAY
  READ PLOT
    scr=yes lpi=10
    ttl='x-z slice through the center of the sphere'
    xul=-20.0 zul=10.0 yul=0.0  xlr=20.0 ylr=0.0 zlr=-10.0
    uax=1.0 wdn=-1.0 nax=400
  END PLOT
  END DATA
  END

KENO-VI

::

  =KENOVI
  sample problem 15  small water reflected sphere on plexiglas collar
  READ PARAM
    lib=4 flx=yes fdn=yes plt=yes
  END PARAM
  READ MIXT
    sct=2
    mix=1  4092234 5.27115e-04   4092235 4.70308e-02   4092236 1.00692e-04
           4092238 4.89708e-04
    mix=2 11001001 5.67873e-02  11006000 3.54921e-02  11008016 1.41968e-02
    mix=3 12001001 6.67515e-02
    mix=3 12008016 3.33757e-02
  END MIXT
  READ GEOM
    global unit 1
      sphere   10  6.5537
      cylinder 20  4.1275 -5.09066 -7.63065
      cylinder 30  12.7   -5.09066 -7.63065
      cylinder 40  21.5537 21.5537 -21.5537
      media  1 1 10  vol=1179.093598091
      media  3 1 20 -10  vol=95.1516
      media  2 1 30 -20 -10  vol=1151.089182028
      media  3 1 40 -30 -20 -10  vol=60488.221616778
      boundary  40
  END GEOM
  READ PLOT
    scr=yes  lpi=10
    ttl='x-z slice through the center of the sphere'
    xul=-20.0 zul=10.0 yul=0.0  xlr=20.0 ylr=0.0 zlr=-10.0
    uax=1.0 wdn=-1.0 nax=400
  END PLOT
  END DATA
  END

.. _8-1c-2-16:

Sample Problem 16 UO2F2 INFINITE SLAB K-INFINITY
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem solves for the k-infinity of an infinite number of slabs of
uranyl fluoride solution contained in Pyrex glass and separated by
borated uranyl fluoride solution. The uranyl fluoride slab is 4.958 cm
thick, 93.2% enriched, and has a density of 578.7 g U/l. The Pyrex glass
is 1.27 cm thick and is present on both faces of the uranyl fluoride
solution. A total of 27.46 cm of borated solution separates the Pyrex
glass of adjacent slabs of solution. 1.482 × 10\ :sup:`–27` atoms of
boron per milliliter are present in the borated solution.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 16 uo2f2 infinite slab k-infinity
  READ PARAMETERS
    lib=4  amx=yes xap=no
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1
      5009019 2.96287e-03  5001001 6.08125e-02  5008016 3.33691e-02  5092235 1.38188e-03  5092238 9.95505e-05
    mix=2
     13011023 2.39503e-03 13013027 4.97720e-04 13014028 1.66260E-02 13014029 8.41845E-04 13014030 5.58826E-04 13005010 9.14627e-04 13005011 3.68149e-03 13008016 4.49174e-02  mix=3
      6009019 2.96287e-03  6001001 6.08125e-02  6008016 3.33691e-02  6092235 1.38188e-03  6092238 9.95505e-05  6005010 2.94862e-04  6005011 1.18686e-03
  END MIXT
  READ GEOMETRY
    global unit 1
      cuboid 1 1 2.479 -2.479 100 -100 100 -100
      cuboid 2 1 3.749 -3.749 100 -100 100 -100
      cuboid 3 1 17.479 -17.479 100 -100 100 -100
  END GEOM
  READ BOUNDS
    all=mirror
  END BOUNDS
  END DATA
  END

KENO-VI

::

  =KENOVI
  sample problem 16 uo2f2 infinite slab k-infinity
  READ PARAMETERS
    lib=4 amx=yes xap=no
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1  5009019 2.96287e-03  5001001 6.08125e-02  5008016 3.33691e-02
           5092235 1.38188e-03  5092238 9.95505e-05
    mix=2 13011023 2.39503e-03 13013027 4.97720e-04 13014028 1.66260E-02
          13014029  8.41845E-04 13014030 5.58826E-04
          13005010 9.14627e-04 13005011 3.68149e-03 13008016 4.49174e-02
    mix=3  6009019 2.96287e-03  6001001 6.08125e-02  6008016 3.33691e-02
           6092235 1.38188e-03  6092238 9.95505e-05
           6005010 2.94862e-04  6005011 1.18686e-03
  END MIXT
  READ GEOMETRY
    global unit 1
      cuboid 10  2.479 -2.479 100.0 -100.0 100.0 -100.0
      cuboid 20  3.749 -3.749 100.0 -100.0 100.0 -100.0
      cuboid 30  17.479 -17.479 100.0 -100.0 100.0 -100.0
      media 1 1 10
      media 2 1 20 -10
      media 3 1 30 -20 -10
      boundary  30
  END GEOM
  READ BOUNDS
    all=mirror
  END BOUNDS
  READ VOLUME
    type=trace  iface=xface
  END VOLUME
  END DATA
  END

.. _8-1c-2-17:

Sample Problem 17 93% UO2F2 SOLUTION SPHERE ADJOINT CALCULATION
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A single 93% enriched uranyl fluoride sphere is run as an adjoint
calculation. The result for the forward and adjoint k-effectives should
be the same within statistical error when the problem is run both ways.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 17 93% uo2f2 solution sphere  adjoint calculation
  READ PARAMETERS
    lib=4  npg=10000 nbk=10500 adj=yes amx=yes xap=no
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1
      7001001 6.55892e-02 7008016 3.34755e-02 7009019 6.80925e-04 7092235 3.16910e-04 7092238 2.35522e-05
  END MIXT
  READ GEOMETRY
    global unit 1
      sphere 1 1 16.0
  END GEOM
  END DATA
  END

KENO-VI

::

  =KENOVI
  sample problem 17 93% uo2f2 solution sphere  adjoint calculation
  READ PARAMETERS
    lib=4 amx=yes pwt=yes xap=no adj=yes npg=10000 nbk=10500
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1  7001001 6.55892e-02  7008016 3.34755e-02  7009019 6.80925e-04
           7092235 3.16910e-04  7092238 2.35522e-05
  END MIXT
  READ GEOMETRY
    global unit 1
      sphere 10 16.0
      media 1 1 10  vol=17157.284678
      boundary  10
  END GEOM
  END DATA
  END

.. _8-1c-2-18:

Sample Problem 18 1F27 DEMONSTRATION OF OPTIONS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A reflected cubic array of 27 cylinders of aqueous uranyl nitrate in
Plexiglas bottles :cite:`thomas_critical_1964`. The walls of the bottles were 0.64-cm thick, and
each bottle was filled with 5 liters of 92.6% enriched solution at a
concentration of 415 g/L, a specific gravity of 1.555 and 0.39 mg excess
nitrate/g soln (From experimental facility documents.  Not reported in ORNL/TM-719.)
The 3 × 3 × 3 array was surrounded by a 6-in.
paraffin reflector. Most of the print options available in KENO are
exercised in this problem. A perspective of this critical experiment is
shown in :numref:`fig8-1c-7`. A photograph of one of the experiments utilized
27 of the Plexiglas bottles is shown in :numref:`fig8-1c-8`. Sample
problem 18 has 15.24 cm of paraffin on all six faces rather than the
2.54-cm Plexiglas shown on five faces.

.. _fig8-1c-7:
.. figure:: figs/KenoC/fig7.png
  :align: center
  :width: 500

  Perspective of critical 1F27 experiment.

.. _fig8-1c-8:
.. figure:: figs/KenoC/fig8.png
  :align: center
  :width: 500

  View of a 27-unit array with 2.54-cm. thick Plexiglas reflector on five sides and a 15.24-cm. thick paraffin base.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 18   1f27 demonstration of options problem
  READ PARA   gen=103 npg=500 fdn=yes nub=yes lib=4
    mku=yes fmu=yes mkh=yes fmh=yes mka=yes fma=yes rnd=f12c09ed2195
    pwt=yes far=yes flx=yes amx=yes pax=yes pgm=yes
  END PARA
  READ MIXT
    sct=2
    mix=1
       2001001 5.77931e-02   2007014 2.13092e-03   2008016 3.74114e-02
       2092234 1.06784e-05   2092235 9.84602e-04   2092236 5.29386e-06
       2092238 6.19414e-05
    mix=2
      11001001 5.67873e-02  11006000 3.54921e-02  11008016 1.41968e-02
    mix=3
      10006000 3.84193e-02  10001901 7.99120e-02
    mix=4
      15008016 3.33757e-11  15001001 6.67515e-11
   END MIXT
  READ BOUNDS
    -zb= h2o
  END BOUNDS
  READ GEOM
    unit 1
      cylinder 1 1 9.52 8.7804 -8.7804
      cylinder 0 1 9.52 8.9896 -8.7804
      cylinder 2 1 10.16 9.6296 -9.4204
      cuboid 4 1 18.45 -18.45 18.45 -18.45 17.8946 -17.6854
    unit 2
      array 1 3*0.0
    unit 3
      array 2 3*0.0
    unit 4
      array 3 3*0.0
    unit 5
      array 4 3*0.0
    global
    unit 6
      cuboid 4 1 55.3501 -55.3501 55.3501 -55.3501 53.3701 -53.3701
       hole 2 -55.35   -18.45   -17.79
       hole 3 -55.35   -18.45   -53.3701
       hole 4  18.4501 -18.45   -53.3701
       hole 5 -55.3501 -55.3501 -53.3701
      replicate 3 2 6*3 5
      replicate 3 7 6*0.24 1
  END GEOM
  READ BIAS
    id=400 2 7
  END BIAS
  READ ARRAY
    ara=1 nux=2 nuy=2 nuz=2 fill f1 end fill
    ara=2 nux=2 nuy=2 nuz=1 fill f1 end fill
    ara=3 nux=1 nuy=2 nuz=3 fill f1 end fill
    ara=4 nux=3 nuy=1 nuz=3 fill f1 end fill
  END ARRAY
  READ START
    nst=6 tfx=0.0 tfy=0.0 tfz=0.0
    lnu=500 ps6=yes
  END START
  READ PLOT
    scr=yes  plt=yes lpi=10
    ttl=?  1f27 xy plot at z=0.0 ?
    xul=-71.0 yul= 71.0 zul=0.0
    xlr= 71.0 ylr=-71.0 zlr=0.0
    uax=1     vdn=-1    nax=400
    run=yes
    end plt1
    ttl=?unit map 1f27 xy plot at z=0.0?
    pic=unit
  END PLOT
  END DATA
  END

KENO-VI

::

  =KENOVI
  sample problem 18   1f27  critical experiment
  READ PARA
    gen=103 npg=500 fdn=yes nub=yes lib=4 plt=yes
    mku=yes cku=yes fmu=yes fmh=yes mka=yes cka=yes fma=yes pwt=yes
    far=yes flx=yes amx=yes pax=yes pgm=yes rnd=f12c09ed2195
  END PARA
  READ MIXT
    sct=2
    mix=1  2001001 5.77931e-02   2007014 2.13092e-03   2008016 3.74114e-02
           2092234 1.06784e-05   2092235 9.84602e-04   2092236 5.29386e-06
           2092238 6.19414e-05
    mix=2 11001001 5.67873e-02  11006000 3.54921e-02  11008016 1.41968e-02
    mix=3 10006000 3.84193e-02  10001901 7.99120e-02
    mix=4 15008016 3.33757e-11  15001001 6.67515e-11
  END MIXT
  READ BOUNDS
    -zb=h2o
  END BOUNDS
  READ GEOM
    unit 1
      cylinder 10  9.52 8.7804 -8.7804
      cylinder 20  9.52 8.9896 -8.7804
      cylinder 30  10.16 9.6296 -9.4204
      cuboid   40  18.45 -18.45 18.45 -18.45 17.8946 -17.6854
      media 1 1 10
      media 0 1 -10 20
      media 2 1 -10 -20 30
      media 0 1 40 -20 -30
      boundary  40
    unit 2
      cuboid 10  18.45 -55.35  55.35 -18.45  53.37 -17.79
      cuboid 20  18.45 -55.35  55.35 -18.45 -17.79 -53.37
      cuboid 30  55.35  18.45  55.35 -18.45  53.37 -53.37
      cuboid 40  55.35 -55.35 -18.45 -55.35  53.37 -53.37
      cuboid 50  55.35 -55.35  55.35 -55.35  53.37 -53.37
      array  1 10 place 1 1 1 -36.90 0.0 -0.1046
      array  2 20 -10 place 1 1 1 -36.90 0.0 -35.6846
      array  3 30 -20 -10 place 1 1 1 36.90 0.0 -35.6846
      array  4 40 -30 -20 -10 place 1 1 1 -36.90 -36.90 -35.6846
      media 0 1 50 -40 -30 -20 -10
      boundary  50
    global unit 3
      cuboid 10  55.35 -55.35 55.35 -55.35 53.37 -53.37
      cuboid 20  58.35 -58.35 58.35 -58.35 56.37 -56.37
      cuboid 30  61.35 -61.35 61.35 -61.35 59.37 -59.37
      cuboid 40  64.35 -64.35 64.35 -64.35 62.37 -62.37
      cuboid 50  67.35 -67.35 67.35 -67.35 65.37 -65.37
      cuboid 60  70.59 -70.59 70.59 -70.59 68.61 -68.61
      array 5 10 place 1 1 1 3*0.0
      media 3 2 -10 20
      media 3 3 -20 30
      media 3 4 -30 40
      media 3 5 -40 50
      media 3 6 60 -50
      boundary  60
   END GEOM
  READ BIAS
    id=400 2 6
  END BIAS
  READ VOLUME
    type=random
  END VOLUME
  READ ARRAY
    ara=1 nux=2 nuy=2 nuz=2 fill f1 end fill
    ara=2 nux=2 nuy=2 nuz=1 fill f1 end fill
    ara=3 nux=1 nuy=2 nuz=3 fill f1 end fill
    ara=4 nux=3 nuy=1 nuz=3 fill f1 end fill
    gbl=5 ara=5 nux=1 nuy=1 nuz=1 fill f2 end fill
  END ARRAY
  READ PLOT
    scr=yes lpi=10
    ttl='  1f27 xy plot at z=0.0 '
    xul=-71.0 yul=71.0 zul=0.0 xlr=71.0 ylr=-71.0 zlr=0.0
    uax=1 vdn=-1 nax=400 end plt0
    ttl='unit map 1f27 xy plot at z=0.0'
    pic=unit
  END PLOT
  END DATA
  END

.. _8-1c-2-19:

Sample Problem 19 4 AQUEOUS 4 METAL ARRAY OF ARRAYS (SAMP PROB 12)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This critical experiment was described previously as SAMPLE PROBLEM 12.
The input data given below utilize the array of arrays option. See
:numref:`fig8-1c-3`.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 19 4 aqueous 4 metal array of arrays (samp prob 12)
  READ PARAM
    lib=4  flx=yes fdn=yes nub=yes smu=yes mkp=yes
    mku=yes fmp=yes fmu=yes
  END PARAM
  READ MIXT
    mix=1
      1092234 4.82717e-04  1092235 4.47971e-02  1092236 9.57233e-05  1092238 2.65767e-03
    mix=2
      2001001 5.77931e-02   2007014 2.13092e-03   2008016 3.74114e-02
      2092234 1.06784e-05   2092235 9.84602e-04   2092236 5.29386e-06
      2092238 6.19414e-05
    mix=3
     11001001 5.67873e-02  11006000 3.54921e-02  11008016 1.41968e-02
    sct=2
  END MIXT
  READ GEOM
    unit 1
      com='uranyl nitrate solution in a plexiglas container'
      cylinder  2 1 9.525 2p8.89
      cylinder  3 1 10.16 2p9.525
      cuboid  0 1 4p10.875 2p10.24
    unit 2
      com='uranium metal cylinder'
      cylinder  1 1 5.748 2p5.3825
      cuboid  0 1 4p6.59 2p6.225
    unit 3
      com='1x2x2 array of solution units'
      array 1 3*0.0
    unit 4
      com='1x2x2 array of metal units padded to match solution array'
      array 2 3*0.0
      replicate 0 1 2*0.0 2*8.57 2*8.03 1
  END GEOM
  READ ARRAY
    ara=1 nux=1 nuy=2 nuz=2 fill f1 end fill
    ara=2 nux=1 nuy=2 nuz=2 fill f2 end fill
    gbl=3 ara=3 nux=2 nuy=1 nuz=1
      com='composite array of solution and metal units'
      fill 4 3 end fill
  END ARRAY
  END DATA
  END

KENO-VI

::

  =KENOVI
  sample problem 19 4 aqueous 4 metal array of arrays (samp prob 12)
  READ PARAM
    lib=4 flx=yes fdn=yes nub=yes smu=yes mkp=yes mku=yes fmp=yes fmu=yes
  END PARAM
  READ MIXT
    sct=2
    mix=1  1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05
           1092238 2.65767e-03
    mix=2  2001001 5.77931e-02   2007014 2.13092e-03   2008016 3.74114e-02
           2092234 1.06784e-05   2092235 9.84602e-04   2092236 5.29386e-06
           2092238 6.19414e-05
    mix=3 11001001 5.67873e-02  11006000 3.54921e-02  11008016 1.41968e-02
  END MIXT
  READ GEOMETRY
    unit 1
      com='uranyl nitrate solution in a plexiglas container'
      cylinder 10   9.525 2p8.89
      cylinder 20   10.16 2p9.525
      cuboid   30  4p10.875 2p10.24
      media 2 1 10      vol=20270.83270
      media 3 1 -10 20  vol=4440.27764
      media 0 1 30 -20  vol=14042.16966
      boundary  30
    unit 2
      com='uranium metal cylinder'
      cylinder 10  5.748 2p5.3825
      cuboid   20 4p6.59 2p6.225
      media 1 1 10      vol=4469.48431
      media 0 1 20 -10  vol=4181.39321
      boundary  20
    unit 3
      com='1x2x2 array of solution units'
      cuboid 10  21.75 0.0 43.5 0.0 40.96 0.0
      array 1 +10 place 1 1 1 10.875 10.875 10.240
      boundary  10
    unit 4
      com='1x2x2 array of metal units padded to match solution array'
      cuboid 10  13.18 0.0 26.36 0.0 24.9 0.0
      cuboid 20  13.18 0.0 34.93 -8.57 32.93 -8.03
      array 2 +10 place 1 1 1 6.59 6.59 6.225
      media 0 1 20 -10  vol=14830.750188
      boundary  20
    global unit 5
      com='global unit of arrays 1 and 2'
      cuboid 10 34.93 0.0 43.5 0.0 40.96 0.0
      array 3 +10 place 1 1 1 0 8.57 8.03
      boundary  10
  END GEOM
  READ ARRAY
    ara=1 nux=1 nuy=2 nuz=2 fill f1 end fill
    ara=2 nux=1 nuy=2 nuz=2 fill f2 end fill
    gbl=3 ara=3 nux=2 nuy=1 nuz=1
    com='composite array of solution and metal units'
    fill 4 3 end fill
  END ARRAY
  END DATA
  END

.. _8-1c-2-20:

Sample Problem 20 TRIANGULAR PITCHED ARRAY
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem is a critical experiment14 consisting of seven cylinders in
a triangular-pitched unreflected array. The central cylinder has six
cylinders arranged around it. The surface-to-surface separation between
the units is 0.15 in. Each unit consists of a 60-mil-thick aluminum can
with an 8-in. inside diameter, filled with a solution of 93.2% enriched
uranyl fluoride with a H/235U atomic ratio of 44.3 and a density of
576.87 g U/L. The apparatus for conducting this experiment is shown in
:numref:`fig8-1c-9`.

.. _fig8-1c-9:
.. figure:: figs/KenoC/fig9.png
  :align: center
  :width: 500

  Typical arrangement for critical experiments with interacting
  arrays of aluminum cylinders containing enriched :sup:`235`\ U
  solutions.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 20 triangular pitched array
  READ PARAM
    lib=4
  END PARAM
  READ MIXT
    sct=2
    mix=1
      8092235 1.37751e-03 8092238 9.92357e-05 8008016 3.33717e-02 8009019 2.95350e-03  8001001 6.08364e-02
    mix=2
     14013027 6.03067e-02
  END MIXT
  READ GEOM
    unit 1
      cylinder   1 1 10.16 18.288 0
      cylinder   2 1 10.312 18.288 -.152
    unit 2
      cuboid     0 1 4p50 50 -.152
      hole       1 3r0
      hole       1 21.006 2r0
      hole       1 -21.006 2r0
      hole       1 10.503 18.192 0
      hole       1 -10.503 18.192 0
      hole       1 10.503 -18.192 0
      hole       1 -10.503 -18.192 0
  END GEOM
  READ ARRAY
    gbl=1 nux=1 nuy=1 nuz=1 fill 2 end fill
  END ARRAY
  READ PLOT
    ttl='hex array' pic=mix lpi=10 scr=yes
    xul=0   yul=100 zul=10
    xlr=100 ylr=0   zlr=10
    uax=1   vdn=-1  nax=400
  END PLOT
  END DATA
  END

KENO-VI

::

  =KENOVI
  sample problem 20  triangular pitched array 7 pins in a circle
  READ PARAMETERS
    lib=4
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1  8092235 1.37751e-03  8092238 9.92357e-05  8008016 3.33717e-02
           8009019 2.95350e-03  8001001 6.08364e-02
    mix=2 14013027 6.03067e-02
  END MIXT
  READ GEOMETRY
    unit 1
      com='single cell fuel can in hexprism'
      cylinder 10  10.16  18.288  0.0
      cylinder 20  10.312 18.288 -0.152
      hexprism 30  10.503 18.288 -0.152
      media  1 1 10      vol=41514.66537
      media  2 1 20 -10  vol=1606.91193
      media 0 1 30 -20   vol=6204.469507
      boundary  30
    unit 2
      com='empty cell'
      hexprism 10  10.503 18.288 -0.152
      media  0 1 10  vol=8155.956715
      boundary  10
    global unit 3
      cylinder 10  31.500 18.288 -0.152
      com='7 cylinders in a circle with cylindrical boundary'
      array  1 10 place 3 3 1 3*0.0
      boundary  10
  END GEOMETRY
  READ ARRAY
    ara=1 typ=triangular nux=5 nuy=5 nuz=1
    fill 7*2 2*1 2*2 3*1 2*2 2*1 7*2 end fill
  END ARRAY
  END DATA
  END

.. _8-1c-2-21:

Sample Problem 21 PARTIALLY FILLED SPHERE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This critical experiment consisted of a partially filled,
unreflected spherical container. This aluminum container had an inside
diameter of 27.244 in. and a wall thickness of 1/16 in. It is referred
to in the report as the 27.3-in.-diameter vessel. The sphere was 98%
filled with uranyl fluoride at an enrichment of 4.89% with an
H/\ :sup:`235`\ U atomic ratio of 1099. The height of the solution in
the sphere was 64.6 cm above the bottom of the sphere. A schematic
diagram of the apparatus used in the experiment is given in
:numref:`fig8-1c-10`. The steel tank was ignored.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 21  partially filled sphere
  READ PARAM
    lib=4
  END PARAM
  READ GEOM
    global unit 1
      hemisphe-z  1 1 34.6   chord 30.
      sphere      0 1 34.6
      sphere      2 1 34.759
  END GEOM
  READ MIXT
    sct=2
    mix=1
      9001001 6.19770e-02  9008016 3.34895e-02  9009019 2.50098e-03
      9092234 2.54224e-07  9092235 6.18924e-05  9092238 1.18835e-03
    mix=2
     14013027 6.03067e-02
  END MIXT
  END DATA
  END

KENO-VI

::

  =KENOVI
  sample problem 21  partially filled sphere
  READ PARAM
    lib=4
  END PARAM
  READ MIXT
    sct=2
    mix=1  9001001 6.19770e-02  9008016 3.34895e-02  9009019 2.50098e-03
           9092234 2.54224e-07  9092235 6.18924e-05  9092238 1.18835e-03
    mix=2 14013027 6.03067e-02
  END MIXT
  READ GEOM
    global unit 1
      sphere 10 34.6  chord -z=30.0
      sphere 20 34.6
      sphere 30 34.759
      media 1 1 10  vol=171309.
      media 0 1 20 -10  vol=2198.14
      media 2 1 30 -20 -10  vol=2403.00
      boundary  30
  END GEOM
  END DATA
  END

.. _fig8-1c-10:
.. figure:: figs/KenoC/fig10.png
  :align: center
  :width: 500

  Schematic of bare partially filled sphere experiment inside a 9.5-ft-diameter, 9-ft-high steel tank.

.. _8-1c-2-22:

Sample Problem 22 CASE 2C8 BARE WITH 3 NESTED HOLES, EACH IS EQUAL VOLUME
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The physical representation of this sample problem is the critical
experiment described in sample problem 1. It is a simple 2 × 2 × 2 array
of 93.2% wt enriched uranium metal cylinders. This sample problem
defines a uranium cylinder in a void spacing cuboid using nested holes.
Eight of these units are stacked together in a 2 × 2 × 2 array.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 22   case 2c8 bare with 3 nested, equal volume holes
  READ PARAMETERS
    flx=yes fdn=yes far=yes gas=no lib=4
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1
      1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05 1092238 2.65767e-03
  END MIXT
  READ GEOMETRY

    unit 1
      cylinder 1 1 3.621 2p3.3907

    unit 2
      cylinder 1 1 4.5622 2p4.2721
      hole 1 3*0.0

    unit 3
      cylinder 1 1 5.2224 2p4.8903
      hole 2 3*0.0

    unit 4
      cylinder 1 1 5.748 5.3825 -5.3825
      hole 3 3*0.0
      cuboid  0 1 6.87 -6.87 6.87 -6.87 6.505 -6.505

  END GEOMETRY
  READ ARRAY
    nux=2 nuy=2 nuz=2 fill f4 end fill
  END ARRAY
  END DATA
  END

KENO-VI

::

  =KENOVI
  sample problem 22  case 2c8 bare with 3 nested, equal volume holes
  READ PARAMETERS
    flx=yes fdn=yes far=yes gas=no lib=4 mkh=yes ckh=yes fmh=yes
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1 1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05
          1092238 2.65767e-03
  END MIXT
  READ GEOMETRY
    unit 1
      cylinder 10 3.621 2p3.3907
      media 1 1 10  vol=279.335597542
      boundary  10
    unit 2
      cylinder 20 4.5622 2p4.2721
      hole 1
      media 1 1 20  vol=279.353142545
      boundary 20
    unit 3
      cylinder 20 5.2224 2p4.8903
      hole 2
      media 1 1 20  vol=279.333676489
      boundary  20
    unit 4
      cylinder 20  5.748 2p5.3825
      cuboid   30 6.87 -6.87 6.87 -6.87 6.505 -6.505
      hole 3
      media 1 1 20  vol=279.34866089
      media 0 1 30 -20  vol=1338.755598534
      boundary  30
    global unit 5
      cuboid 10 20.61 -6.87 20.61 -6.87 19.515 -6.505
      array 1 10 place 1 1 1 3*0.0
      boundary  10
  END GEOMETRY
  READ ARRAY
    ara=1 nux=2 nuy=2 nuz=2 fill f4 end fill
  END ARRAY
  END DATA
  END

.. _8-1c-2-23:

Sample Problem 23 CASE 2C8 BARE AS STACKED CYLINDERS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The physical representation of this sample problem is the critical
experiment described in sample problem 1. This sample problem describes
each of the eight units in the critical 2 × 2 × 2 array using
Z hemicylinders (in KENO V.a) or hemicylinders with different chord
sizes and directions (in KENO‑VI).

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 23  case 2c8 bare as mixed zhemicylinders
  READ PARAMETERS
    fdn=yes lib=4
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1
      1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05 1092238 2.65767e-03
  END MIXT
  READ GEOMETRY
    unit 1
      com='-x half of unit 3'
      zhemicyl-x 1 1 5.748 5.3825 -5.3825
      cuboid  0 1 0.0  -6.87 6.87 -6.87 6.505 -6.505
    unit 2
      com='+x half of unit 3'
      zhemicyl+x 1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.87  0.0  6.87 -6.87 6.505 -6.505
    unit 3
      com='cylinder composed of equal halves (zhemicylinders with x radii)'
      array 1 3*0.0
    unit 4
      com='-x portion (more than half) of unit 6'
      zhemicyl-x 1 1 5.748 5.3825 -5.3825 chord 3.0
      cuboid  0 1 3.0  -6.87 6.87 -6.87 6.505 -6.505
    unit 5
      com='+x portion (less than half) of unit 6'
      zhemicyl+x 1 1 5.748 5.3825 -5.3825 chord -3.0
      cuboid  0 1 6.87  3.0  6.87 -6.87 6.505 -6.505
    unit 6
      com='cylinder composed of unequal halves (zhemicylinders with x radii)'
      array 2 3*0.0
    unit 7
      com='cylinder of a single zhemicylinder in the -x direction'
      zhemicyl-x 1 1 5.748 5.3825 -5.3825 chord 5.748
      cuboid  0 1 6.87 -6.87 6.87 -6.87 6.505 -6.505
    unit 8
      com='cylinder of a single zhemicylinder in the +x direction'
      zhemicyl+x 1 1 5.748 5.3825 -5.3825 chord 5.748
      cuboid  0 1 6.87 -6.87 6.87 -6.87 6.505 -6.505
    unit 9
      com='-y half of unit 11'
      zhemicyl-y 1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.87 -6.87 0.0  -6.87 6.505 -6.505
    unit 10
      com='+y half of unit 11'
      zhemicyl+y 1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.87 -6.87 6.87  0.0  6.505 -6.505
    unit 11
      com='cylinder composed of equal halves (zhemicylinders with z radii)'
      array 3 3*0.0
    unit 12
      com='-y portion (more than half) of unit 14'
      zhemicyl-y 1 1 5.748 5.3825 -5.3825 chord 3.0
      cuboid  0 1 6.87 -6.87 3.0  -6.87 6.505 -6.505
    unit 13
      com='+y portion (less than half) of unit 14'
      zhemicyl+y 1 1 5.748 5.3825 -5.3825 chord -3.0
      cuboid  0 1 6.87 -6.87 6.87  3.0  6.505 -6.505
    unit 14
      com='cylinder composed of unequal halves (zhemicylinders with z radii)'
      array 4 3*0.0
    unit 15
      com='cylinder of a single zhemicylinder in the -y direction'
      zhemicyl-y 1 1 5.748 5.3825 -5.3825 chord 5.748
      cuboid  0 1 6.87 -6.87 6.87 -6.87 6.505 -6.505
    unit 16
      com='cylinder of a single zhemicylinder in the +y'
      zhemicyl+y 1 1 5.748 5.3825 -5.3825 chord 5.748
      cuboid  0 1 6.87 -6.87 6.87 -6.87 6.505 -6.505
  END GEOMETRY
  READ ARRAY
    com='array 1 defines unit 3 (zhemicylinders with x radii)'
    ara=1 nux=2 nuy=1 nuz=1 fill 1 2 end fill
    com='array 2 defines unit 6 (zhemicylinders with x radii)'
    ara=2 nux=2 nuy=1 nuz=1 fill 4 5 end fill
    com='array 3 defines unit 11 (zhemicylinders with y radii)'
    ara=3 nux=1 nuy=2 nuz=1 fill 9 10 end fill
    com='array 4 defines unit 14 (zhemicylinders with y radii)'
    ara=4 nux=1 nuy=2 nuz=1 fill 12 13 end fill
    com='array 5 defines the total 2c8 problem'
    gbl=5 ara=5 nux=2 nuy=2 nuz=2 fill 3 7 6 8 11 15 14 16 end fill
  END ARRAY
  END DATA
  END

KENO-VI

::

  =KENOVI
  sample problem 23  case 2c8 bare as mixed unrotated zcylinders
  READ PARAMETERS
    fdn=yes lib=4
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1 1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05
          1092238 2.65767e-03
  END MIXT
  READ GEOMETRY
    unit 1
      com='-x half of unit 3'
      cylinder 10 5.748 5.3825 -5.3825 chord -x=0.0
      cuboid   20 0.0 -6.87 6.87 -6.87 6.505 -6.505
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 2
      com='+x half of unit 3'
      cylinder 10 5.748 5.3825 -5.3825 chord +x=0.0
      cuboid   20 6.87 0.0 6.87 -6.87 6.505 -6.505
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 3
      com='cylinder composed of equal halves (zhemicylinders with x radii)'
      cuboid 10 6.87 -6.87 6.87 -6.87 6.505 -6.505
      array 1 10 place 1 1 1 0.0 0.0 0.0
      boundary  10
    unit 4
      com='-x portion (more than half) of unit 6'
      cylinder 10 5.748 5.3825 -5.3825 chord -x=3.0
      cuboid   20 3.0 -6.87 6.87 -6.87 6.505 -6.505
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 5
      com='+x portion (less than half) of unit 6'
      cylinder 10 5.748 5.3825 -5.3825 chord +x=3.0
      cuboid   20 6.87 3.0 6.87 -6.87 6.505 -6.505
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 6
      com='cylinder composed of unequal halves (zhemicylinders with x radii)'
      cuboid 10 6.87 -6.87 6.87 -6.87 6.505 -6.505
      array 2 10 place 1 1 1 3*0.0
      boundary  10
    unit 7
      com='cylinder of a single zhemicylinder in the -x direction'
      cylinder 10 5.748 5.3825 -5.3825 chord -x=5.748
      cuboid   20 6.87 -6.87 6.87 -6.87 6.505 -6.505
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 8
      com='cylinder of a single zhemicylinder in the +x direction'
      cylinder 10 5.748 5.3825 -5.3825 chord +x=-5.748
      cuboid   20 6.87 -6.87 6.87 -6.87 6.505 -6.505
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 9
      com='-y half of unit 11'
      cylinder 10 5.748 5.3825 -5.3825 chord -y=0.0
      cuboid   20 6.87 -6.87 0.0 -6.87 6.505 -6.505
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 10
      com='+y half of unit 11'
      cylinder 10 5.748 5.3825 -5.3825 chord +y=0.0
      cuboid   20 6.87 -6.87 6.87 0.0 6.505 -6.505
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 11
      com='cylinder composed of equal halves (zhemicylinders with y radii)'
      cuboid 10 6.87 -6.87 6.87 -6.87 6.505 -6.505
      array 3 10 place 1 1 1 0.0 0.0 0.0
      boundary  10
    unit 12
      com='-y portion (more than half) of unit 14'
      cylinder 10 5.748 5.3825 -5.3825 chord -y=3.0
      cuboid   20 6.87 -6.87 3.0 -6.87 6.505 -6.505
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 13
      com='+y portion (less than half) of unit 14'
      cylinder 10 5.748 5.3825 -5.3825 chord +y=3.0
      cuboid   20 6.87 -6.87 6.87 3.0 6.505 -6.505
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 14
      com='cylinder composed of unequal halves (zhemicylinders with y radii)'
      cuboid 10 6.87 -6.87 6.87 -6.87 6.505 -6.505
      array 4 10 place 1 1 1 3*0.0
      boundary  10
    unit 15
      com='cylinder of a single zhemicylinder in the -y direction'
      cylinder 10 5.748 5.3825 -5.3825 chord -y=5.748
      cuboid   20 6.87 -6.87 6.87 -6.87 6.505 -6.505
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 16
      com='cylinder of a single zhemicylinder in the +y direction'
      cylinder 10 5.748 5.3825 -5.3825 chord +y=-5.748
      cuboid   20 6.87 -6.87 6.87 -6.87 6.505 -6.505
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    global unit 17
      cuboid 10 13.74 -13.74 13.74 -13.74 13.010 -13.010
      array 5 10 place 1 1 1 -6.87 -6.87 -6.505
      boundary  10
  END GEOMETRY
  READ ARRAY
    com='array 1 defines unit 3 (zhemicylinders with x radii)'
    ara=1 nux=2 nuy=1 nuz=1 fill 1 2 end fill
    com='array 2 defines unit 6 (zhemicylinders with x radii)'
    ara=2 nux=2 nuy=1 nuz=1 fill 4 5 end fill
    com='array 3 defines unit 11 (zhemicylinders with y radii)'
    ara=3 nux=1 nuy=2 nuz=1 fill 9 10 end fill
    com='array 4 defines unit 14 (zhemicylinders with y radii)'
    ara=4 nuz=1 nuy=2 nuz=1 fill 12 13 end fill
    com='array 5 defines the total 2c8 problem'
    gbl=5 ara=5 nux=2 nuy=2 nuz=2 fill 3 7 6 8 11 15 14 16 end fill
  END ARRAY
  END DATA
  END

.. _8-1c-2-24:

Sample Problem 24 CASE 2C8 BARE AS STACKED ROTATED CYLINDERS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The physical representation of this sample problem is the critical
experiment described in sample problem 1. This sample problem describes
each of the eight units in the critical 2 × 2 × 2 array using
hemicylinders whose axes are in the x direction. In KENO V.a this is
realized using xhemicylinders, while in KENO-VI the hemycylinders with
different chord sizes are rotated in the X-direction.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 24  case 2c8 bare as mixed xhemicylinders
  READ PARAMETERS
    fdn=yes lib=4
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1
      1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05 1092238 2.65767e-03
  END MIXT
  READ GEOMETRY
    unit 1
      com='-y half of unit 3'
      xhemicyl-y 1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.505 -6.505 0.0 -6.87 6.87 -6.87
    unit 2
      com='+y half of unit 3'
      xhemicyl+y 1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.505 -6.505 6.87 0.0  6.87 -6.87
    unit 3
      com='cylinder composed of equal halves (xhemicylinders with y radii)'
      array 1 3*0.0
    unit 4
      com='-y portion (more than half) of unit 6'
      xhemicyl-y 1 1 5.748 5.3825 -5.3825 chord 3.0
      cuboid  0 1 6.505 -6.505 3.0 -6.87 6.87 -6.87
    unit 5
      com='+y portion (less than half) of unit 6'
      xhemicyl+y 1 1 5.748 5.3825 -5.3825 chord -3.0
      cuboid  0 1 6.505 -6.505 6.87 3.0  6.87 -6.87
    unit 6
      com='cylinder composed of unequal halves (xhemicylinders with y radii)'
      array 2 3*0.0
    unit 7
      com='cylinder of a single xhemicylinder in the -y direction'
      xhemicyl-y 1 1 5.748 5.3825 -5.3825 chord 5.748
      cuboid  0 1 6.505 -6.505 6.87 -6.87 6.87 -6.87
    unit 8
      com='cylinder of a single xhemicylinder in the +y direction'
      xhemicyl+y 1 1 5.748 5.3825 -5.3825 chord 5.748
      cuboid  0 1 6.505 -6.505 6.87 -6.87 6.87 -6.87
    unit 9
      com='-z half of unit 11'
      xhemicyl-z 1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.505 -6.505 6.87 -6.87 0.0 -6.87
    unit 10
      com='+z half of unit 11'
      xhemicyl+z 1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.505 -6.505 6.87 -6.87 6.87 0.0
    unit 11
      com='cylinder composed of equal halves (xhemicylinders with z radii)'
      array 3 3*0.0
    unit 12
      com='-z portion (more than half) of unit 14'
      xhemicyl-z 1 1 5.748 5.3825 -5.3825 chord 3.0
      cuboid  0 1 6.505 -6.505 6.87 -6.87 3.0 -6.87
    unit 13
      com='+z portion (less than half) of unit 14'
      xhemicyl+z 1 1 5.748 5.3825 -5.3825 chord -3.0
      cuboid  0 1 6.505 -6.505 6.87 -6.87 6.87 3.0
    unit 14
      com='cylinder composed of unequal halves (xhemicylinders with z radii)'
      array 4 3*0.0
    unit 15
      com='cylinder of a single xhemicylinder in the -z direction'
      xhemicyl-z 1 1 5.748 5.3825 -5.3825 chord 5.748
      cuboid  0 1 6.505 -6.505 6.87 -6.87 6.87 -6.87
    unit 16
      com='cylinder of a single xhemicylinder in the +z direction'
      xhemicyl+z 1 1 5.748 5.3825 -5.3825 chord 5.748
      cuboid  0 1 6.505 -6.505 6.87 -6.87 6.87 -6.87
  END GEOMETRY
  READ ARRAY
    com='array 1 defines unit 3 (xhemicylinders with y radii)'
    ara=1 nux=1 nuy=2 nuz=1 fill 1 2 end fill
    com='array 2 defines unit 6 (xhemicylinders with y radii)'
    ara=2 nux=1 nuy=2 nuz=1 fill 4 5 end fill
    com='array 3 defines unit 11 (xhemicylinders with z radii)'
    ara=3 nux=1 nuy=1 nuz=2 fill 9 10 end fill
    com='array 4 defines unit 14 (xhemicylinders with z radii)'
    ara=4 nux=1 nuy=1 nuz=2 fill 12 13 end fill
    com='array 5 defines the total 2c8 problem'
    gbl=5 ara=5 nux=2 nuy=2 nuz=2 fill 3 7 6 8 11 15 14 16 end fill
  END ARRAY
  END DATA
  END

KENO-VI

::

  =KENOVI
  sample problem 24  case 2c8 bare as mixed x-rotated cylinders
  READ PARAMETERS
    rnd=4c6a61962572 fdn=yes lib=4
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1 1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05
          1092238 2.65767e-03
  END MIXT
  READ GEOMETRY
    unit 1
      com='-y half of unit 3'
      cylinder 10 5.748 5.3825 -5.3825 chord -x=0.0 rotate a1=90 a2=90
      cuboid   20 6.505 -6.505 0.0 -6.87 6.87 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 2
      com='+y half of unit 3'
      cylinder 10 5.748 5.3825 -5.3825 chord +x=0.0 rotate a1=90 a2=90
      cuboid   20 6.505 -6.505 6.87 0.0 6.87 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 3
      com='cylinder composed of equal halves (xhemicylinders with y radii)'
      cuboid 10 6.505 -6.505 6.87 -6.87 6.87 -6.87
      array 1 10 place 1 1 1 0.0 0.0 0.0
      boundary  10
    unit 4
      com='-y portion (more than half) of unit 6'
      cylinder 10 5.748 5.3825 -5.3825 chord -x=3.0 rotate a1=90 a2=90
      cuboid   20 6.505 -6.505 3.0 -6.87 6.87 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 5
      com='+y portion (less than half) of unit 6'
      cylinder 10 5.748 5.3825 -5.3825 chord +x=3.0 rotate a1=90 a2=90
      cuboid   20 6.505 -6.505 6.87 3.0 6.87 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 6
      com='cylinder composed of unequal halves (xhemicylinders with y radii)'
      cuboid 10 6.505 -6.505 6.87 -6.87 6.87 -6.87
      array 2 10 place 1 1 1 3*0.0
      boundary  10
    unit 7
      com='cylinder of a single xhemicylinder in the -y direction'
      cylinder 10 5.748 5.3825 -5.3825 chord -x=5.748 rotate a1=90 a2=90
      cuboid   20 6.505 -6.505 6.87 -6.87 6.87 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 8
      com='cylinder of a single xhemicylinder in the +y direction'
      cylinder 10 5.748 5.3825 -5.3825 chord +x=-5.748 rotate a1=90 a2=90
      cuboid   20 6.505 -6.505 6.87 -6.87 6.87 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 9
      com='-z half of unit 11'
      cylinder 10 5.748 5.3825 -5.3825 chord -y=0.0 rotate a1=90 a2=90
      cuboid   20 6.505 -6.505 6.87 -6.87 0.0 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 10
      com='+z half of unit 11'
      cylinder 10 5.748 5.3825 -5.3825 chord +y=0.0 rotate a1=90 a2=90
      cuboid   20 6.505 -6.505 6.87 -6.87 6.87 0.0
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 11
      com='cylinder composed of equal halves (xhemicylinders with z radii)'
      cuboid 10 6.505 -6.505 6.87 -6.87 6.87 -6.87
      array 3 10 place 1 1 1 0.0 0.0 0.0
      boundary  10
    unit 12
      com='-z portion (more than half) of unit 14'
      cylinder 10 5.748 5.3825 -5.3825 chord -y=3.0 rotate a1=90 a2=90
      cuboid   20 6.505 -6.505 6.87 -6.87 3.0 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 13
      com='+z portion (less than half) of unit 14'
      cylinder 10 5.748 5.3825 -5.3825 chord +y=3.0 rotate a1=90 a2=90
      cuboid   20 6.505 -6.505 6.87 -6.87 6.87 3.0
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 14
      com='cylinder composed of unequal halves (xhemicylinders with z radii)'
      cuboid 10 6.505 -6.505 6.87 -6.87 6.87 -6.87
      array 4 10 place 1 1 1 3*0.0
      boundary  10
    unit 15
      com='cylinder of a single xhemicylinder in the -z direction'
      cylinder 10 5.748 5.3825 -5.3825 chord -y=5.748 rotate a1=90 a2=90
      cuboid   20 6.505 -6.505 6.87 -6.87 6.87 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 16
      com='cylinder of a single xhemicylinder in the +z direction'
      cylinder 10 5.748 5.3825 -5.3825 chord +y=-5.748 rotate a1=90 a2=90
      cuboid   20 6.505 -6.505 6.87 -6.87 6.87 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    global unit 17
      cuboid 10 13.01 -13.01 13.74 -13.74 13.74 -13.74
      array 5 10 place 1 1 1 -6.505 -6.87 -6.87
      boundary  10
  END GEOMETRY
  READ ARRAY
    com='array 1 defines unit 3 (xhemicylinders with y radii)'
    ara=1 nux=1 nuy=2 nuz=1 fill 1 2 end fill
    com='array 2 defines unit 6 (xhemicylinders with y radii)'
    ara=2 nux=1 nuy=2 nuz=1 fill 4 5 end fill
    com='array 3 defines unit 11 (xhemicylinders with z radii)'
    ara=3 nux=1 nuy=1 nuz=2 fill 9 10 end fill
    com='array 4 defines unit 14 (xhemicylinders with z radii)'
    ara=4 nux=1 nuy=1 nuz=2 fill 12 13 end fill
    com='array 5 defines the total 2c8 problem'
    ara=5 nux=2 nuy=2 nuz=2 fill 3 7 6 8 11 15 14 16 end fill
  END ARRAY
  END DATA
  END

.. _8-1c-2-25:

Sample Problem 25 CASE 2C8 BARE AS MIXED YHEMICYLINDERS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The physical representation of this sample problem is the critical
experiment described in sample problem 1. This sample problem describes
each of the eight units in the critical 2 × 2 × 2 array using
hemicylinders whose axes are in the y direction. This is realized in
KENO V.a by using yhemicylinders, while in KENO-VI it is realized using
hemicylinders with different chord sizes and directions whose long axes
are rotated in the Y-direction.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 25  case 2c8 bare as mixed yhemicylinders
  READ PARAMETERS
     fdn=yes lib=4
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1
      1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05 1092238 2.65767e-03
  END MIXT
  READ GEOMETRY
    unit 1
      com='-x half of unit 3'
      yhemicyl-x 1 1 5.748 5.3825 -5.3825
      cuboid  0 1 0.0  -6.87 6.505 -6.505 6.87 -6.87
    unit 2
      com='+x half of unit 3'
      yhemicyl+x 1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.87  0.0  6.505 -6.505 6.87 -6.87
    unit 3
      com='cylinder composed of equal halves (yhemicylinders with x radii)'
      array 1 3*0.0
    unit 4
      com='-x portion (more than half) of unit 6'
      yhemicyl-x 1 1 5.748 5.3825 -5.3825 chord 3.0
      cuboid  0 1 3.0  -6.87 6.505 -6.505 6.87 -6.87
    unit 5
      com='+x portion (less than half) of unit 6'
      yhemicyl+x 1 1 5.748 5.3825 -5.3825 chord -3.0
      cuboid  0 1 6.87  3.0  6.505 -6.505 6.87 -6.87
    unit 6
      com='cylinder composed of unequal halves (yhemicylinders with x radii)'
      array 2 3*0.0
    unit 7
      com='cylinder of a single yhemicylinder in the -x direction'
      yhemicyl-x 1 1 5.748 5.3825 -5.3825 chord 5.748
      cuboid  0 1 6.87 -6.87 6.505 -6.505 6.87 -6.87
    unit 8
      com='cylinder of a single yhemicylinder in the +x direction'
      yhemicyl+x 1 1 5.748 5.3825 -5.3825 chord 5.748
      cuboid  0 1 6.87 -6.87 6.505 -6.505 6.87 -6.87
    unit 9
      com='-z half of unit 11'
      yhemicyl-z 1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.87 -6.87 6.505 -6.505 0.0 -6.87
    unit 10
      com='+z half of unit 11'
      yhemicyl+z 1 1 5.748 5.3825 -5.3825
      cuboid  0 1 6.87 -6.87 6.505 -6.505 6.87 0.0
    unit 11
      com='cylinder composed of equal halves (yhemicylinders with z radii)'
      array 3 3*0.0
    unit 12
      com='-z portion (more than half) of unit 14'
      yhemicyl-z 1 1 5.748 5.3825 -5.3825 chord 3.0
      cuboid  0 1 6.87 -6.87 6.505 -6.505 3.0 -6.87
    unit 13
      com='+z portion (less than half) of unit 14'
      yhemicyl+z 1 1 5.748 5.3825 -5.3825 chord -3.0
      cuboid  0 1 6.87 -6.87 6.505 -6.505 6.87 3.0
    unit 14
      com='cylinder composed of unequal halves (yhemicylinders with z radii)'
      array 4 3*0.0
    unit 15
      com='cylinder of a single  yhemicylinder in the -z direction'
      yhemicyl-z 1 1 5.748 5.3825 -5.3825 chord 5.748
      cuboid  0 1 6.87 -6.87 6.505 -6.505 6.87 -6.87
    unit 16
      com='cylinder of a single yhemicylinder in the +z direction'
      yhemicyl+z 1 1 5.748 5.3825 -5.3825 chord 5.748
      cuboid  0 1 6.87 -6.87 6.505 -6.505 6.87 -6.87
  END GEOMETRY
  READ ARRAY
    com='array 1 defines unit 3 (yhemicylinders with x radii)'
    ara=1 nux=2 nuy=1 nuz=1 fill 1 2 end fill
    com='array 2 defines unit 6 (yhemicylinders with x radii)'
    ara=2 nux=2 nuy=1 nuz=1 fill 4 5 end fill
    com='array 3 defines unit 11 (yhemicylinders with z radii)'
    ara=3 nux=1 nuy=1 nuz=2 fill 9 10 end fill
    com='array 4 defines unit 14 (zhemicylinders with z radii)'
    ara=4 nux=1 nuy=1 nuz=2 fill 12 13 end fill
    com='array 5 defines the total 2c8 problem'
    gbl=5 ara=5 nux=2 nuy=2 nuz=2 fill 3 7 6 8 11 15 14 16 end fill
  END ARRAY
  END DATA
  END

KENO-VI

::

  =KENOVI
  sample problem 25  case 2c8 bare as mixed y-rotated cylinders
  READ PARAMETERS
    fdn=yes lib=4
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1 1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05
          1092238 2.65767e-03
  END MIXT
  READ GEOMETRY
    unit 1
      com='-x half of unit 3'
      cylinder 10 5.748 5.3825 -5.3825 chord -y=0.0 rotate a1=180 a2=90 a3=90
      cuboid   20 0.0 -6.87 6.505 -6.505 6.87 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 2
      com='+x half of unit 3'
      cylinder 10 5.748 5.3825 -5.3825 chord +y=0.0 rotate a1=180 a2=90 a3=90
      cuboid   20 6.87 0.0 6.505 -6.505 6.87 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 3
      com='cylinder composed of equal halves (yhemicylinders with x radii)'
      cuboid 10 6.87 -6.87 6.505 -6.505 6.87 -6.87
      array 1 10 place 1 1 1 0.0 0.0 0.0
      boundary  10
    unit 4
      com='-x portion (more than half) of unit 6'
      cylinder 10 5.748 5.3825 -5.3825 chord -y=3.0 rotate a1=180 a2=90 a3=90
      cuboid   20 3.0 -6.87 6.505 -6.505 6.87 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 5
      com='+x portion (less than half) of unit 6'
      cylinder 10 5.748 5.3825 -5.3825 chord +y=3.0 rotate a1=180 a2=90 a3=90
      cuboid   20 6.87 3.0 6.505 -6.505 6.87 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 6
      com='cylinder composed of unequal halves (yhemicylinders with x radii)'
      cuboid 10 6.87 -6.87 6.505 -6.505 6.87 -6.87
      array 2 10 place 1 1 1 3*0.0
      boundary  10
    unit 7
      com='cylinder of a single yhemicylinder in the -x direction'
      cylinder 10 5.748 5.3825 -5.3825 chord -y=5.748 rotate a1=180 a2=90 a3=90
      cuboid   20 6.87 -6.87 6.505 -6.505 6.87 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 8
      com='cylinder of a single yhemicylinder in the +x direction'
      cylinder 10 5.748 5.3825 -5.3825 chord +y=-5.748 rotate a1=180 a2=90 a3=90
      cuboid   20 6.87 -6.87 6.505 -6.505 6.87 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 9
      com='-z half of unit 11'
      cylinder 10 5.748 5.3825 -5.3825 chord -x=0.0 rotate a1=180 a2=90 a3=90
      cuboid   20 6.87 -6.87 6.505 -6.505 0.0 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 10
      com='+z half of unit 11'
      cylinder 10 5.748 5.3825 -5.3825 chord +x=0.0 rotate a1=180 a2=90 a3=90
      cuboid   20 6.87 -6.87 6.505 -6.505 6.87 0.0
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 11
      com='cylinder composed of equal halves (yhemicylinders with z radii)'
      cuboid 10 6.87 -6.87 6.505 -6.505 6.87 -6.87
      array 3 10 place 1 1 1 0.0 0.0 0.0
      boundary  10
    unit 12
      com='-z portion (more than half) of unit 14'
      cylinder 10 5.748 5.3825 -5.3825 chord -x=3.0 rotate a1=180 a2=90 a3=90
      cuboid   20 6.87 -6.87 6.505 -6.505 3.0 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 13
      com='+z portion (less than half) of unit 14'
      cylinder 10 5.748 5.3825 -5.3825 chord +x=3.0 rotate a1=180 a2=90 a3=90
      cuboid   20 6.87 -6.87 6.505 -6.505 6.87 3.0
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 14
      com='cylinder composed of unequal halves (yhemicylinders with z radii)'
      cuboid 10 6.87 -6.87 6.505 -6.505 6.87 -6.87
      array 4 10 place 1 1 1 3*0.0
      boundary  10
    unit 15
      com='cylinder of a single yhemicylinder in the -z direction'
      cylinder 10 5.748 5.3825 -5.3825 chord -x=5.748 rotate a1=180 a2=90 a3=90
      cuboid   20 6.87 -6.87 6.505 -6.505 6.87 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    unit 16
      com='cylinder of a single yhemicylinder in the +z direction'
      cylinder 10 5.748 5.3825 -5.3825 chord +x=-5.748 rotate a1=180 a2=90 a3=90
      cuboid   20 6.87 -6.87 6.505 -6.505 6.87 -6.87
      media 1 1 10     vol=2234.742156
      media 0 1 20 -10 vol=2677.511196
      boundary  20
    global unit 17
      cuboid 10 13.74 -13.74 13.01 -13.01 13.74 -13.74
      array 5 10 place 1 1 1 -6.87 -6.505 -6.87
      boundary  10
  END GEOMETRY
  READ ARRAY
    com='array 1 defines unit 3 (yhemicylinders with z radii)'
    ara=1 nux=2 nuy=1 nuz=1 fill 1 2 end fill
    com='array 2 defines unit 6 (yhemicylinders with z radii)'
    ara=2 nux=2 nuy=1 nuz=1 fill 4 5 end fill
    com='array 3 defines unit 11 (yhemicylinders with x radii)'
    ara=3 nux=1 nuy=1 nuz=2 fill 9 10 end fill
    com='array 4 defines unit 14 (yhemicylinders with x radii)'
    ara=4 nux=1 nuy=1 nuz=2 fill 12 13 end fill
    com='array 5 defines the total 2c8 problem'
    gbl=5 ara=5 nux=2 nuy=2 nuz=2 fill 3 7 6 8 11 15 14 16 end fill
  END ARRAY
  READ VOLUME
    type=random
  END VOLUME
  END DATA
  END

.. _8-1c-2-26:

Sample Problem 26 (KENO V.a ONLY) CASE 2C8 BARE AS MIXED ZHEMICYLINDERS WITH ORIGINS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The physical representation of this sample problem is the critical
experiment described in sample problem 1. This sample problem describes
each of the eight units in the critical 2 × 2 × 2 array using
zhemicylinders with origins.

KENO V.a

::

  =KENOVA
  sample problem 26  case 2c8 bare as mixed zhemicylinders with origins
  READ PARAMETERS
    fdn=yes lib=4  run=yes
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1
      1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05 1092238 2.65767e-03
  END MIXT
  READ GEOMETRY
    unit 1
      com='-x half of first cylinder'
      zhemicyl-x 1 1 5.748 5.3825 -5.3825 origin 6.87 0.0
      cuboid  0 1 6.87 0.0 6.87 -6.87 6.505 -6.505
    unit 2
      com='+x half of first cylinder'
      zhemicyl+x 1 1 5.748 5.3825 -5.3825 origin 6.87 0.0
      cuboid  0 1 13.74 6.87 6.87 -6.87 6.505 -6.505
    unit 3
      com='1st cylinder composed of equal portions (z hemicylinders with x radii)'
      array 1 3*0.0
    unit 4
      com='-x portion (more than half) of second cylinder'
      zhemicyl-x 1 1 5.748 5.3825 -5.3825 chord 3.0 origin 6.87 0.0
      cuboid  0 1 9.87 0.0 6.87 -6.87 6.505 -6.505
    unit 5
      com='+x portion (less than half) of second cylinder'
      zhemicyl+x 1 1 5.748 5.3825 -5.3825 chord -3.0 origin 6.87 0.0
      cuboid  0 1 13.74 9.87 6.87 -6.87 6.505 -6.505
    unit 6
      com='2nd cylinder composed of unequal portions (z hemicylinders with x radii)'
      array 2 3*0.0
    unit 7
      com='3rd cylinder: described as a zhemicylinder in the -x direction'
      zhemicyl-x 1 1 5.748 5.3825 -5.3825 chord 5.748 origin 6.87 0.0
      cuboid  0 1 13.74 0.0 6.87 -6.87 6.505 -6.505
    unit 8
      com='4th cylinder: described as a zhemicylinder in the +x direction'
      zhemicyl+x 1 1 5.748 5.3825 -5.3825 chord 5.748 origin 6.87 0.0
      cuboid  0 1 13.74 0.0 6.87 -6.87 6.505 -6.505
    unit 9
      com='-y half of fifth cylinder'
      zhemicyl-y 1 1 5.748 5.3825 -5.3825 origin 0.0 6.87
      cuboid  0 1 6.87 -6.87 6.87 0.0 6.505 -6.505
    unit 10
      com='+y half of fifth cylinder'
      zhemicyl+y 1 1 5.748 5.3825 -5.3825 origin 0.0 6.87
      cuboid  0 1 6.87 -6.87 13.74 6.87  6.505 -6.505
    unit 11
      com='5th cylinder composed of equal portions (zhemicylinders with y radii)'
      array 3 3*0.0
    unit 12
      com='-y portion (more than half) of sixth cylinder'
      zhemicyl-y 1 1 5.748 5.3825 -5.3825 chord 3.0 origin 0.0 6.87
      cuboid  0 1 6.87 -6.87 9.87  0.0 6.505 -6.505
    unit 13
      com='+y portion (less than half) of sixth cylinder'
      zhemicyl+y 1 1 5.748 5.3825 -5.3825 chord -3.0 origin 0.0 6.87
      cuboid  0 1 6.87 -6.87 13.74  9.87  6.505 -6.505
    unit 14
      com='6th cylinder composed of unequal portions (zhemicylinders with y radii)'
      array 4 3*0.0
    unit 15
      com='7th cylinder: described as a zhemicylinder in the -y direction'
      zhemicyl-y 1 1 5.748 5.3825 -5.3825 chord 5.748 origin 0.0 6.87
      cuboid  0 1 6.87 -6.87 13.74 0.0 6.505 -6.505
    unit 16
      com='8th cylinder: described as a zhemicylinder in the +y direction'
      zhemicyl+y 1 1 5.748 5.3825 -5.3825 chord 5.748 origin 0.0 6.87
      cuboid  0 1 6.87 -6.87 13.74 0.0 6.505 -6.505
    global unit 17
      com='complete 2c8 bare configuration'
      array 5 3*0.0
  END GEOMETRY
  READ ARRAY
    com='array 1: 1st cylinder (unit 3) equal x portions of zhemicylinders'
    ara=1 nux=2 nuy=1 nuz=1 fill 1 2 end fill
    com='array 2: 2nd cylinder (unit 6) unequal x portions of zhemicylinders'
    ara=2 nux=2 nuy=1 nuz=1 fill 4 5 end fill
    com='array 3: 5th cylinder (unit 11) equal y portions of zhemicylinders'
    ara=3 nux=1 nuy=2 nuz=1 fill 9 10 end fill
    com='array 4: 6th cylinder (unit 14) unequal y portions of zhemicylinders'
    ara=4 nux=1 nuy=2 nuz=1 fill 12 13 end fill
    com='array 5 defines the total 2c8 problem'
    ara=5 nux=2 nuy=2 nuz=2 fill 3 7 6 8 11 15 14 16 end fill
  END ARRAY
  END DATA
  END

.. _8-1c-2-27:

Sample Problem 27 (KENO V.a oONLY) CASE 2C8 BARE AS MIXED XHEMICYLINDERS WITH ORIGINS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The physical representation of this sample problem is the critical
experiment described in sample problem 1. This sample problem describes
each of the eight units in the critical 2 × 2 × 2 array using
hemicylinders whose axes are in the x direction. Origins are specified
for each hemicylinder.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 27  case 2c8 bare as mixed xhemicylinders with origins
  READ PARAMETERS
    fdn=yes lib=4  run=yes
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1
      1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05 1092238 2.65767e-03
  END MIXT
  READ GEOMETRY
    unit 1
      com='-y half of first cylinder'
      xhemicyl-y 1 1 5.748 5.3825 -5.3825 origin 6.87 0.0
      cuboid  0 1 6.505 -6.505 6.87 0.0 6.87 -6.87
    unit 2
      com='+y half of first cylinder'
      xhemicyl+y 1 1 5.748 5.3825 -5.3825 origin 6.87 0.0
      cuboid  0 1 6.505 -6.505 13.74 6.87 6.87 -6.87
    unit 3
      com='1st cylinder composed of equal portions (xhemicylinders with y radii)'
      array 1 3*0.0
    unit 4
      com='-y portion (more than half) of second cylinder'
      xhemicyl-y 1 1 5.748 5.3825 -5.3825 chord 3.0 origin 6.87 0.0
      cuboid  0 1 6.505 -6.505 9.87 0.0 6.87 -6.87
    unit 5
      com='+y portion (less than half) of second cylinder'
      xhemicyl+y 1 1 5.748 5.3825 -5.3825 chord -3.0 origin 6.87 0.0
      cuboid  0 1 6.505 -6.505 13.74 9.87  6.87 -6.87
    unit 6
      com='2nd cylinder composed of unequal portions (xhemicylinders with y radii)'
      array 2 3*0.0
    unit 7
      com='3rd cylinder: described as a xhemicylinder in the -y direction'
      xhemicyl-y 1 1 5.748 5.3825 -5.3825 chord 5.748 origin 6.87 0.0
      cuboid  0 1 6.505 -6.505 13.74 0.0 6.87 -6.87
    unit 8
      com='4th cylinder: described as a xhemicylinder in the +y direction'
      xhemicyl+y 1 1 5.748 5.3825 -5.3825 chord 5.748 origin 6.87 0.0
      cuboid  0 1 6.505 -6.505 13.74 0.0 6.87 -6.87
    unit 9
      com='-z half of fifth cylinder'
      xhemicyl-z 1 1 5.748 5.3825 -5.3825 origin 0.0 6.87
      cuboid  0 1 6.505 -6.505 6.87 -6.87 6.87 0.0
    unit 10
      com='+z half of fifth cylinder'
      xhemicyl+z 1 1 5.748 5.3825 -5.3825 origin 0.0 6.87
      cuboid  0 1 6.505 -6.505 6.87 -6.87 13.74 6.87
    unit 11
      com='5th cylinder composed of equal portions (xhemicylinders with z radii)'
      array 3 3*0.0
    unit 12
      com='-z portion (more than half) of sixth cylinder'
      xhemicyl-z 1 1 5.748 5.3825 -5.3825 chord 3.0 origin 0.0 6.87
      cuboid  0 1 6.505 -6.505 6.87 -6.87 9.87 0.0
    unit 13
      com='+z portion (less than half) of sixth cylinder'
      xhemicyl+z 1 1 5.748 5.3825 -5.3825 chord -3.0 origin 0.0 6.87
      cuboid  0 1 6.505 -6.505 6.87 -6.87 13.74 9.87
    unit 14
      com='6th cylinder composed of unequal portions (xhemicylinders with z radii)'
      array 4 3*0.0
    unit 15
      com='7th cylinder: described as a xhemicylinder in the -z direction'
      xhemicyl-z 1 1 5.748 5.3825 -5.3825 chord 5.748 origin 0.0 6.87
      cuboid  0 1 6.505 -6.505 6.87 -6.87 13.74 0.0
    unit 16
      com='8th cylinder: de3scribed as a xhemicylinder in the +z direction'
      xhemicyl+z 1 1 5.748 5.3825 -5.3825 chord 5.748 origin 0.0 6.87
      cuboid  0 1 6.505 -6.505 6.87 -6.87 13.74 0.0
    global unit 17
      com='complete 2c8 bare configuration'
      array 5 3*0.0
  END GEOMETRY
  READ ARRAY
    com='array 1: 1st cylinder (unit 3) equal y portions of xhemicylinders'
    ara=1 nux=1 nuy=2 nuz=1 fill 1 2 end fill
    com='array 2: 2nd cylinder (unit 6) unequal y portions of xhemicylinders'
    ara=2 nux=1 nuy=2 nuz=1 fill 4 5 end fill
    com='array 3: 5th cylinder (unit 11) equal z portions of xhemicylinders'
    ara=3 nux=1 nuy=1 nuz=2 fill 9 10 end fill
    com='array 4: 6th cylinder (unit 14) unequal z portions of xhemicylinders'
    ara=4 nux=1 nuy=1 nuz=2 fill 12 13 end fill
    com='array 5 defines the total 2c8 problem'
    gbl=5 ara=5 nux=2 nuy=2 nuz=2 fill 3 7 6 8 11 15 14 16 end fill
  END ARRAY
  END DATA
  END

.. _8-1c-2-28:

Sample Problem 28 (KENO V.a oONLY) CASE 2C8 BARE AS MIXED YHEMICYLINDERS WITH ORIGINS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The physical representation of this sample problem is the critical
experiment described in sample problem 1. This sample problem describes
each of the eight units in the critical 2 × 2 × 2 array using
hemicylinders whose axes are in the y direction. Origins are specified
for each hemicylinder.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 28  case 2c8 bare as mixed yhemicylinders with origins
  READ PARAMETERS
    fdn=yes lib=4  run=yes
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1
      1092234 4.82717e-04 1092235 4.47971e-02 1092236 9.57233e-05 1092238 2.65767e-03
  END MIXT
  READ GEOMETRY
    unit 1
      com='-x half of first cylinder'
      yhemicyl-x 1 1 5.748 5.3825 -5.3825 origin 6.87 0.0
      cuboid  0 1 6.87 0.0 6.505 -6.505 6.87 -6.87
    unit 2
      com='+x half of unit 3'
      yhemicyl+x 1 1 5.748 5.3825 -5.3825 origin 6.87 0.0
      cuboid  0 1 13.74 6.87  6.505 -6.505 6.87 -6.87
    unit 3
      com='1st cylinder composed of equal portions (yhemicylinders with x radii)'
      array 1 3*0.0
    unit 4
      com='-x portion (more than half) of second cylinder'
      yhemicyl-x 1 1 5.748 5.3825 -5.3825 chord 3.0 origin 6.87 0.0
      cuboid  0 1 9.87 0.0 6.505 -6.505 6.87 -6.87
    unit 5
      com='+x portion (less than half) of second cylinder'
      yhemicyl+x 1 1 5.748 5.3825 -5.3825 chord -3.0 origin 6.87 0.0
      cuboid  0 1 13.74 9.87 6.505 -6.505 6.87 -6.87
    unit 6
      com='2nd cylinder composed of unequal portions (yhemicylinders with x radii)'
      array 2 3*0.0
    unit 7
      com='3rd cylinder: described as a single yhemicylinder in the -x direction'
      yhemicyl-x 1 1 5.748 5.3825 -5.3825 chord 5.748 origin 6.87 0.0
      cuboid  0 1 13.74 0.0 6.505 -6.505 6.87 -6.87
    unit 8
      com='4th cylinder: described as a single yhemicylinder in the +x direction'
      yhemicyl+x 1 1 5.748 5.3825 -5.3825 chord 5.748 origin 6.87 0.0
      cuboid  0 1 13.74 0.0 6.505 -6.505 6.87 -6.87
    unit 9
      com='-z half of fifth cylinder'
      yhemicyl-z 1 1 5.748 5.3825 -5.3825 origin 0.0 6.87
      cuboid  0 1 6.87 -6.87 6.505 -6.505 6.87 0.0
    unit 10
      com='+z half of sixth cylinder'
      yhemicyl+z 1 1 5.748 5.3825 -5.3825 origin 0.0 6.87
      cuboid  0 1 6.87 -6.87 6.505 -6.505 13.74 6.87
    unit 11
      com='5th cylinder composed of equal portions (yhemicylinders with z radii)'
      array 3 3*0.0
    unit 12
      com='-z portion (more than half) of sixth cylinder'
      yhemicyl-z 1 1 5.748 5.3825 -5.3825 chord 3.0 origin 0.0 6.87
      cuboid  0 1 6.87 -6.87 6.505 -6.505 9.87 0.0
    unit 13
      com='+z portion (less than half) of sixth cylinder'
      yhemicyl+z 1 1 5.748 5.3825 -5.3825 chord -3.0 origin 0.0 6.87
      cuboid  0 1 6.87 -6.87 6.505 -6.505 13.74 9.87
    unit 14
      com='6th cylinder composed of unequal portions (yhemicylinders with z radii)'
      array 4 3*0.0
    unit 15
      com='7th cylinder: described as a yhemicylinder in the -z direction'
      yhemicyl-z 1 1 5.748 5.3825 -5.3825 chord 5.748 origin 0.0 6.87
      cuboid  0 1 6.87 -6.87 6.505 -6.505 13.74 0.0
    unit 16
      com='8th cylinder: described as a yhemicylinder in the +z direction'
      yhemicyl+z 1 1 5.748 5.3825 -5.3825 chord 5.748 origin 0.0 6.87
      cuboid  0 1 6.87 -6.87 6.505 -6.505 13.74 0.0
    global unit 17
      com='complete 2c8 bare configuration'
      array 5 3*0.0
  END GEOMETRY
  READ ARRAY
    com='array 1: 1st cylinder (unit 3) equal x portions of yhemicylinders'
    ara=1 nux=2 nuy=1 nuz=1 fill 1 2 end fill
    com='array 2: 2nd cylinder (unit 6) unequal x portions of yhemicylinders'
    ara=2 nux=2 nuy=1 nuz=1 fill 4 5 end fill
    com='array 3: 5th cyllinder (unit 11) equal z portions of yhemicylinders'
    ara=3 nux=1 nuy=1 nuz=2 fill 9 10 end fill
    com='array 4: 6th cylinder (unit 14) unequal z portions of yhemicylinders'
    ara=4 nux=1 nuy=1 nuz=2 fill 12 13 end fill
    com='array 5 defines the total 2c8 problem'
    gbl=5 ara=5 nux=2 nuy=2 nuz=2 fill 3 7 6 8 11 15 14 16 end fill
  END ARRAY
  END DATA
  END

.. _8-1c-2-29:

Sample Problem 29  BARE CRITICAL SPHERE 3.4420-IN. RADIUS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem is a critical experiment :cite:`mihalczo_measurements_1993` consisting of a critical
Oralloy sphere. The density of the Oralloy is 18.747 g/cc, and the
isotopic enrichment (wt %) is 93.21% :sup:`235`\ U, 5.7697%
:sup:`238`\ U, 0.9844% :sup:`234`\ U, and 0.0359% :sup:`236`\ U. The
critical radius was 8.74268 cm. A photograph of the experiment is given
in :numref:`fig8-1c-11`. The support structure was ignored in the input data.

.. _fig8-1c-11:
.. figure:: figs/KenoC/fig11.png
  :align: center
  :width: 500

  Critical Oralloy sphere.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 29  bare critical sphere   3.4420" radius
  READ PARAMETERS
      fdn=yes lib=4
  END PARAMETERS
  READ MIXT
    sct=2
    mix=16
     16092235 4.47709e-02 16092238 2.73631e-03 16092234 4.74858e-04 16092236 1.71704e-05
  END MIXT
  READ GEOMETRY
    global unit 1
      sphere   16 1 8.74268
  END GEOMETRY
  READ PLOT
    scr=yes lpi=10
    ttl='x-y slice at z=0.0'
    xul=-9 yul= 9 zul=0.0
    xlr= 9 ylr=-9 zlr=0.0
    uax=1  vdn=-1 nax=400 nch=' *'
  END PLOT
  END DATA
  END

KENO-VI

::

  =KENOVI
  sample problem 26  bare critical sphere   3.4420" radius
  READ PARAMETERS
    fdn=yes lib=4
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1   16092235   4.47709e-02
            16092238   2.73631e-03
            16092234   4.74858e-04
            16092236   1.71704e-05
  END MIXT
  READ GEOMETRY
    global unit 1
      sphere   10  8.74268
      media  1 1 10  vol=2799.1254126
      boundary 10
  END GEOMETRY
  END DATA
  END

.. _8-1c-2-30:

Sample Problem 30 (KENO V.a ONLY) BARE CRITICAL SPHERE Z HEMISPHERE MODEL 3.4420-IN. RADIUS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The physical representation of this sample problem is the critical
experiment described in sample problem 29. This sample problem describes
the sphere as two Z hemispheres, each with a chord and origin specified.
One of the hemispheres is placed using the hole geometry option.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 30   bare critical sphere    z hemisphere model 3.4420" radius
  READ PARAMETERS
      fdn=yes lib=4
  END PARAMETERS
  READ MIXT
    sct=2
    mix=16
     16092235 4.47709e-02 16092238 2.73631e-03 16092234 4.74858e-04 16092236 1.71704e-05
  END MIXT
  READ GEOMETRY
     unit 1
       hemisphe+z   16 1 8.74268  chord +3.0 origin 8.9 8.9 8.9
     global unit 2
       hemisphe-z   16 1 8.74268  chord -3.0 origin 8.9 8.9 8.9
       cuboid       0 1 17.8 0.0 17.8 0.0 17.8 0.0
       hole 1 3*0.0
  END GEOMETRY
  READ PLOT
    scr=yes lpi=10
    ttl='y-z slice at x=8.9   mixture map'
    xul=8.9 yul=-0.5 zul=18.5
    xlr=8.9 ylr=18.5 zlr=-0.5
    vax=1   wdn=-1   nax=400   end plt1
    ttl='y-z slice at x=8.9   unit map'
    pic=box                    end plt2
  END PLOT
  END DATA
  END

.. _8-1c-2-31:

Sample Problem 31 (KENO V.a ONLY) BARE CRITICAL SPHERE X HEMISPHERE MODEL 3.4420-IN. RADIUS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The physical representation of this sample problem is the critical
experiment described in sample problem 29. This sample problem describes
the sphere as two X hemispheres, each with a chord and origin specified.
One of the hemispheres is placed using the hole geometry option.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 31   bare critical sphere    x hemisphere model 3.4420" radius
  READ PARAMETERS
      fdn=yes lib=4
  END PARAMETERS
  READ MIXT
    sct=2
    mix=16
     16092235 4.47709e-02 16092238 2.73631e-03 16092234 4.74858e-04 16092236 1.71704e-05
  END MIXT
  READ GEOMETRY
     unit 1
       hemisphe-x   16 1 8.74268  chord +3.0
     global unit 2
       hemisphe+x   16 1 8.74268  chord -3.0 origin 8.9 8.9 8.9
       cuboid       0 1 17.8 0.0 17.8 0.0 17.8 0.0
       hole 1 3*8.9
  END GEOMETRY
  READ PLOT
    scr=yes lpi=10
    ttl='x-y slice at z=8.9     mixture map'
    xul=-0.5 yul=18.5 zul=8.9
    xlr=18.5 ylr=-0.5 zlr=8.9
    uax=1   vdn=-1    nax=400  end plt1
    ttl='y-z slice at x=8.9   unit map'
    pic=box                    end plt2
  END PLOT
  END DATA
  END

.. _8-1c-2-32:

Sample Problem 32 (KENO V.a ONLY) BARE CRITICAL SPHERE Y HEMISPHERE MODEL 3.4420-IN. RADIUS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The physical representation of this sample problem is the critical
experiment described in sample problem 29. This sample problem describes
the sphere as two Y hemispheres, each with a chord and origin specified.
One of the hemispheres is placed using the hole geometry option.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 32   bare critical sphere    y hemisphere model 3.4420" radius
  READ PARAMETERS
      fdn=yes lib=4
  END PARAMETERS
  READ MIXT
    sct=2
    mix=16
     16092235 4.47709e-02 16092238 2.73631e-03 16092234 4.74858e-04 16092236 1.71704e-05
  END MIXT
  READ GEOMETRY
    unit 1
      hemisphe-y   16 1 8.74268  chord +3.0 origin 8.9 9.9 10.9
    global unit 2
      hemisphe+y   16 1 8.74268  chord -3.0 origin 8.9 8.9 8.9
      cuboid       0 1 17.8 0.0 17.8 0.0 17.8 0.0
      hole 1 0.0 -1.0 -2.0
  END GEOMETRY
  READ PLOT
    scr=yes lpi=10
    ttl='x-y slice at z=8.9     mixture map'
    xul=-0.5 yul=18.5 zul=8.9
    xlr=18.5 ylr=-0.5 zlr=8.9
    uax=1    vdn=-1   nax=400  end plt1
    ttl='y-z slice at x=8.9   unit map'
    pic=box                    end plt2
  END PLOT
  END DATA
  END

.. _8-1c-2-33:

Sample Problem 33  CRITICAL TRIANGULAR PITCHED ARRAY OF ANNULAR RODS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This sample problem represents a critical
experiment :cite:`johnson_critical_1966` that consists of a partially flooded
array of 19 low enriched uranium metal cylindrical annuli billets
arranged in a triangular pitched array. The density of the uranium metal
was 19.0 g/cc, and the isotopic enrichment in weight percent was 1.95%
:sup:`235`\ U, 98.02% :sup:`238`\ U, 0.006% :sup:`236`\ U, and 0.002%
:sup:`234`\ U. The cylindrical annuli had an inside diameter of
6.604 cm, an outside diameter of 18.288 cm, and were placed with a pitch
of 20.828 cm. Each billet was 101.6 cm long. The array was positioned in
a very large tank. This configuration was critical when the tank was
filled to a height of 47.7 cm on a scale whose zero point was 0.6 cm
below the bottom of the billets. The bottom of the billets was 21.6 cm
above the bottom of the tank. The tank and all support structures have
been ignored in this model. The model utilizes only 15.24 cm of water
reflector on all sides of the array. :numref:`fig8-1c-12` and :numref:`fig8-1c-13`
provide a representation of the model. A photograph of a single annular
billet is shown in :numref:`fig8-1c-14`.

.. centered:: Input Data

KENO V.a

::

  =KENOVA
  sample problem 33   critical triangular pitched array of annular rods
  READ PARAMETERS  fdn=yes nub=yes lib=4
  END PARAMETERS
  READ MIXT
    sct=2
    mix=17
      17092235   9.49270e-04 17092238   4.71245e-02 17092234   9.77785e-07 17092236   2.90844e-06
    mix=18
      18008016   3.33757e-02 18001001   6.67515e-02
    mix=19
      19001001   6.67515e-02 19008016   3.33757e-02
    mix=20
      20092235   9.49270e-04 20092238   4.71245e-02 20092234   9.77785e-07 20092236   2.90844e-06
  END MIXT
  READ GEOM
    unit 1
      zhemicyl-x 18 1 3.302 47.7 0.6
      zhemicyl-x 17 1 9.144 47.7 0.6
    unit 2
      zhemicyl-y 18 1 3.302 47.7 0.6
      zhemicyl-y 17 1 9.144 47.7 0.6
    unit 3
      zhemicyl+x 18 1 3.302 47.7 0.6
      zhemicyl+x 17 1 9.144 47.7 0.6
    unit 4
      zhemicyl+y 18 1 3.302 47.7 0.6  origin 0.0 -18.03758
      zhemicyl+y 17 1 9.144 47.7 0.6  origin 0.0 -18.03758
      cuboid     19 1 2p10.414 2p18.03758 47.7 0.6
      hole      1       10.414    0.0      0.0
      hole      2        0.0     18.03758  0.0
      hole      3      -10.414    0.0      0.0
    unit 5
      cuboid     19 1 2p10.414 10.414 0.0 47.7 0.6
    unit 6
      zhemicyl-y 18 1 3.302 47.7 0.6
      zhemicyl-y 17 1 9.144 47.7 0.6
      cuboid     19 1 2p10.414 0.0 -10.414 47.7 0.6
    unit 7
      zhemicyl-y 18 1 3.302 47.7 0.6 origin 0.0 18.03758
      zhemicyl-y 17 1 9.144 47.7 0.6 origin 0.0 18.03758
      cuboid     19 1 2p10.414 2p18.03758 47.7 0.6
      hole     3      -10.414 0.0 0.0
    unit 8
      zhemicyl+y 18 1 3.302 47.7 0.6 origin 0.0 -18.03758
      zhemicyl+y 17 1 9.144 47.7 0.6 origin 0.0 -18.03758
      cuboid     19 1 2p10.414 2p18.03758 47.7 0.6
      hole     3      -10.414 0.0 0.0
    unit 9
      zhemicyl+y 18 1 3.302 47.7 0.6
      zhemicyl+y 17 1 9.144 47.7 0.6
      cuboid     19 1 2p10.414 10.414 0.0 47.7 0.6
    unit 10
      zhemicyl+y 18 1 3.302 47.7 0.6  origin 0.0 -18.03758
      zhemicyl+y 17 1 9.144 47.7 0.6  origin 0.0 -18.03758
      cuboid     19 1 2p10.414 2p18.03758 47.7 0.6
      hole     1       10.414 0.0 0.0
    unit 11
      zhemicyl-y 18 1 3.302 47.7 0.6  origin 0.0 18.03758
      zhemicyl-y 17 1 9.144 47.7 0.6  origin 0.0 18.03758
      cuboid     19 1 2p10.414 2p18.03758 47.7 0.6
      hole     1       10.414 0.0 0.0
    unit 21
      zhemicyl-x  0 1 3.302 102.2 47.7
      zhemicyl-x 20 1 9.144 102.2 47.7
    unit 22
      zhemicyl-y  0 1 3.302 102.2 47.7
      zhemicyl-y 20 1 9.144 102.2 47.7
    unit 23
      zhemicyl+x  0 1 3.302 102.2 47.7
      zhemicyl+x 20 1 9.144 102.2 47.7
    unit 24
      zhemicyl+y  0 1 3.302 102.2 47.7  origin 0.0 -18.03758
      zhemicyl+y 20 1 9.144 102.2 47.7  origin 0.0 -18.03758
      cuboid      0 1 2p10.414 2p18.03758 102.2 47.7
      hole      21      10.414    0.0      0.0
      hole      22       0.0     18.03758  0.0
      hole      23     -10.414    0.0      0.0
    unit 25
      cuboid      0 1 2p10.414 10.414 0.0 102.2 47.7
    unit 26
      zhemicyl-y  0 1 3.302 102.2 47.7
      zhemicyl-y 20 1 9.144 102.2 47.7
      cuboid      0 1 2p10.414 0.0 -10.414 102.2 47.7
    unit 27
      zhemicyl-y  0 1 3.302 102.2 47.7  origin 0.0 18.03758
      zhemicyl-y 20 1 9.144 102.2 47.7  origin 0.0 18.03758
      cuboid      0 1 2p10.414 2p18.03758 102.2 47.7
      hole     23      -10.414 0.0 0.0
    unit 28
      zhemicyl+y  0 1 3.302 102.2 47.7  origin 0.0 -18.03758
      zhemicyl+y 20 1 9.144 102.2 47.7  origin 0.0 -18.03758
      cuboid      0 1 2p10.414 2p18.03758 102.2 47.7
      hole     23      -10.414 0.0 0.0
    unit 29
      zhemicyl+y  0 1 3.302 102.2 47.7
      zhemicyl+y 20 1 9.144 102.2 47.7
      cuboid      0 1 2p10.414 10.414 0.0 102.2 47.7
    unit 30
      zhemicyl+y  0 1 3.302 102.2 47.7  origin 0.0 -18.03758
      zhemicyl+y 20 1 9.144 102.2 47.7  origin 0.0 -18.03758
      cuboid      0 1 2p10.414 2p18.03758 102.2 47.7
      hole     21       10.414 0.0 0.0
    unit 31
      zhemicyl-y  0 1 3.302 102.2 47.7  origin 0.0 18.03758
      zhemicyl-y 20 1 9.144 102.2 47.7  origin 0.0 18.03758
      cuboid      0 1 2p10.414 2p18.03758 102.2 47.7
      hole     21       10.414 0.0 0.0
    unit 32
      com='flooded portion of array with 15.24 cm of water in x and y'
      array 1 2*0.0 0.6
      replicate 19 1 4r15.24 0.0 0.6 1
      replicate 19 2 5r0.0 3.0 7
    unit 33
      com='unflooded upper portion of array'
      array 2 3*0.0
      replicate 0 1 4r15.24 2*0.0 1
    global
    unit 34
      array 3 -67.31 -61.72916 -21.0
  END GEOM
  READ BIAS
    id=500 2 8
  END BIAS
  READ ARRAY
     ara=1 nux=5 nuy=4 nuz=1  fill  5 3r 6  5   11 3r 4  7    10 3r 4  8      5 3r 9  5  end fill
     ara=2 nux=5 nuy=4 nuz=1  fill 25 3r26 25   31 3r24 27    30 3r24 28     25 3r29 25  end fill
     ara=3 nux=1 nuy=1 nuz=2  fill 32 33 end fill
  END ARRAY
  READ START
    nst=1   xsm=-52 xsp=52   ysm=-47 ysp=47   zsm=0.6 zsp=47.7
  END START
  READ PLOT
    scr=yes lpi=10
    clr=17 255 0 0
        18 128 255 255
        19 0 0 255
        20 255 0 128
    end color
    ttl='x-y plot of pins at z=45.0'
      xul=-52.0 yul= 47.0 zul=45.0
      xlr= 52.0 ylr=-47.0 zlr=45.0
      uax=  1.0 vdn=-1.0  nax=400
    end plt1
    ttl='x-z plot of pins at y=0.0'
      xul=-52.0 yul=0.0 zul=102.7
      xlr= 52.0 ylr=0.0 zlr=-3.0
      uax=  1.0 wdn=-1.0 nax=400
    end plt2
    ttl='x-z plot at y=0.0'
      xul=-68.0 yul=0.0 zul=102.7
      xlr= 70.0 ylr=0.0 zlr=-25.0
      uax=  1.0 wdn=-1.0 nax=400
    end plt3
  END PLOT
  END DATA
  END

KENO-VI

::

  =KENOVI
  sample problem 27   critical triangular pitched array of annular rods
  READ PARAMETERS
    fdn=yes nub=yes lib=4
  END PARAMETERS
  READ MIXT
    sct=2
    mix=1   17092235   9.49270e-04
            17092238   4.71245e-02
            17092234   9.77785e-07
            17092236   2.90844e-06
    mix=2   18008016   3.33757e-02
            18001001   6.67515e-02
    mix=3   19001001   6.67515e-02
            19008016   3.33757e-02
    mix=4   20092235   9.49270e-04
            20092238   4.71245e-02
            20092234   9.77785e-07
            20092236   2.90844e-06
    mix=5   18008016   3.33757e-02
            18001001   6.67515e-02
  END MIXT
  READ GEOM
    unit 1
      cylinder 10  3.302 102.2 0.6
      cylinder 20  9.144 102.2 0.6
      plane    30  zpl=1.0 con=-47.7
      hexprism 40 10.414 102.2 0.0
      media  2 1 10 -30
      media  1 1 20 -10 -30
      media  3 1 40 -20 -30
      media  0 1 10  30
      media  4 1 20 -10  30
      media  0 1 40 -20  30
      boundary 40
    unit 2
      plane    10  zpl=1.0 con=-47.7
      hexprism 20 10.414 102.2 0.0
      media  3 1 -10  20
      media  0 1  10  20
      boundary 20
    global unit 3
      cylinder 10  52.42 102.2 0.0
      plane    20  zpl=1.0 con=-47.7
      cylinder 30  82.9  102.2 -21.0
      array  1 10 place 4 4 1 3*0.0
      media  0 1 30  20 -10
      media  5 1 30 -20 -10
      boundary 30
  END GEOM
  READ ARRAY
    ara=1 nux=7 nuy=7 nuz=1 typ=tri fill
    2 2 2 2 2 2 2
     2 2 2 1 1 1 2
      2 2 1 1 1 1 2
       2 1 1 1 1 1 2
        2 1 1 1 1 2 2
         2 1 1 1 2 2 2
          2 2 2 2 2 2 2   end fill
  END ARRAY
  READ VOLUME
    type=random
  END VOLUME
  READ PLOT
    scr=yes lpi=10
    clr=1 255 0 0
        2 128 255 255
        3 0 0 255
        4 255 0 128
        5 200 200 200
    end color
    ttl='x-z plot of pins at y=0.0'
      xul=-68.0 yul= 0.0 zul=102.7
      xlr= 70.0 ylr= 0.0 zlr=-25.0
      uax=  1.0 wdn=-1.0
      nax=800
    end plt0
    ttl='x-y plot of pins and water at z=45.0'
      xul=-68.0 yul= 68.0 zul=45.0
      xlr= 68.0 ylr=-68.0 zlr=45.0
      uax=  1.0 vdn= -1.0
      nax=800
    end plt1
  END PLOT
  END DATA
  END

.. _fig8-1c-12:
.. figure:: figs/KenoC/fig12.png
  :align: center
  :width: 500

  Horizontal slice through a critical triangular pitched array of partially flooded 1.95% enriched uranium metal annular billets.

.. _fig8-1c-13:
.. figure:: figs/KenoC/fig13.png
  :align: center
  :width: 500

  Vertical slice through the center of a critical triangular-pitched array of partially flooded 1.9% enriched uranium metal annular billets.

.. _fig8-1c-14:
.. figure:: figs/KenoC/fig14.png
  :align: center
  :width: 500

  1.95% Enriched uranium metal annular billet used in critical experiments

.. bibliography:: bibs/KenoC.bib
