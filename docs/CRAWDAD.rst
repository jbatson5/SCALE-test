.. _7-7:

CRAWDAD: Module to Produce CENTRM-Formatted Continuous-Energy Nuclear Data Libraries
====================================================================================

*M. L. Williams, D. Wiarda, and S. W. D. Hart*

ACKNOWLEDGMENTS

The authors would like to acknowledge the important contributions to
CRAWDAD made by former ORNL staff N. M. Greene and D. F. Hollenbach.

.. _7-7-1:

Introduction
------------

SCALE uses the code CRAWDAD (Code to Read And Write DAta for Discretized
solution) to read nuclear data from the SCALE-6 continuous (CE) library
files, and write it to an output file in the particular format needed
for the discretized energy solution in CENTRM. Prior to SCALE-6, the CE
data used by the CENTRM and PMC modules were distributed directly in the
CENTRM library format. However beginning with SCALE-6, the same CE data
are used by both CENTRM/PMC and by the CE versions of the KENO and
Monaco Monte Carlo codes. CE nuclear data for each nuclide are stored in
individual files contained in the SCALE permanent data directory.
CRAWDAD reads the files for each material appearing in a problem and
combines all data into a single problem-dependent CENTRM library file
stored in the temporary directory for execution.

All SCALE-6 calculations that use modules CENTRM and PMC for
self-shielding multigroup (MG) cross sections must first execute the
CRAWDAD computational module. During execution of SCALE sequences, the
XSProc self-shielding module automatically executes CRAWDAD whenever the
CENTRM/PMC method is specified. CRAWDAD also can be run in stand-alone
mode to process and save a CENTRM-formatted library for subsequent
CENTRM/PMC calculations.

PMC allows the energy range of the CE data to be selected, as well as
which reactions are placed on the output CENTRM library. The output
CENTRM library always contains the following “standard” nuclear data
types for all materials: total (1); elastic (2); complete inelastic (4);
radiative capture (102); fission (18); total/prompt/delayed nubars (452,
455, 456); and (n,α) cross section for 10B and 7Li. In this list, the
number shown in parenthesis corresponds to the ENDF/B “mt numbers.”

CE data are obtained for arbitrary energies by linear interpolation of
discrete cross sections defined on a pointwise (PW) energy mesh. The PW
energy mesh for a given nuclide is sufficiently fine that error
introduced by linear interpolation between any two points is less than
0.1%. CRAWDAD also interpolates the CE data to the specific temperatures
needed for the problem. The default temperature interpolation method
uses square-root of temperature below 1200 Kelvin and a finite
difference procedure above this temperature :cite:`hart_creation_2016`.

.. _7-7-2:

CRAWDAD Input Data
------------------

For standalone CRAWDAD execution, the user prepares the FIDO input deck
as described below. However during a SCALE sequence computation, the
XSProc module always executes CRAWDAD for CENTRM/PMC self-shielding
calculations, and defines appropriate CRAWDAD parameter values based on
specified CENTRM and PMC options. This is the recommended mode of
operation. Some XSProc default values for CRAWDAD can be changed using
keywords in the CENTRM DATA block; e.g., see parameters *mtout=* and
*kernel=* in :ref:`7-4-4`. Several options available for stand-alone
execution cannot be controlled by keywords in the sequence runs, as
these are set automatically

.. this reference needs to be checked.

.. highlight:: none

::

  CRAWDAD STANDALONE INPUT

  **************     DATA BLOCK 1

  0$$   LOGICAL UNIT ASSIGNMENTS [4 entries.  Default values given in parentheses]

  Entry Number	Variable Name	Description	Default Value
  1	lcen	logical unit number of output CENTRM library	(81)
  2	n17	logical unit for scratch	(17)
  3	n18	logical unit for scratch	(18)
  4	n19	logical unit for reading CE-KENO libraries	(88)

  1$$   INTEGER PARAMETERS  [10 entries ]

  1	num_nucs	number of PW nuclides to process	(1)
  2	idtap	identifier placed on header of output CENTRM library	(66666)
  3	iprt	print out option  (1)
  		-1  no print out AT ALL
  		0  hardly any print
  		1  normal print
  		2  debug print
  4	obsolete feature
  5	iterp   	temperature interpolation method for PW cross sections (0)
  		0  square-root-T interpolation for T<1200 K and finite difference for T>1200 K
  		1  square-root-T interpolation for all temperatures
  		2  finite difference interpolation for all temperatures
  6	libth   	create CENTRM thermal kernel library for bound moderators (1)
  		0  no
  		1  yes  (output kernel file is named lib_cen_kern)
  7–10	N/A	extra integer parameters (not used)	(0)


  1**   REAL PARAMETERS  [10 entries]

  1	teps	tolerance on temperature differences  (5.0)
  	( temperatures within +/- "teps" are assumed equal)
  2	tole	not implemented
  3–10	N/A	extra real parameters (not used)	(0.0)

  T       terminate data block 1

::

  **************     DATA BLOCK 2
  *****	Repeat data block(s) 2 and 3, stacked "num_nucs" times to create a new
   	CENTRM library containing specified temperatures and reaction types

  2$$  NUCLIDE INFORMATION [5 entries]

  Entry Number	Variable Name	Description	Default Value

  1	za	zaid for this nuclide in PW XS library
  2	lver	version number of evaluated nuclear data (e.g, 7 for ENDF/B-VII)
  3	mod	desired mod number of evaluated nuclear  (-1)
  		-1 => use latest mod
  4	inum	desired number of temperatures for this nuclide (0)
  		0 - put all available temperatures on output CENTRM library
  		n - include data at the "n" temperatures in 4** array
  5	mtout	MTS to be included on output CENTRM PW library (2)
  		0 - output PW data for all available MTs
  		1 - output PW data only for default standard MTs:
  		1, 2, 4, 102, 18, 452, 455, 456 for all materials; and  107 for 10B and 7Li
  		2 - output standard MTs, plus inelastic levels and (n,2n)
  		3 - standard MTs plus those listed in 5$$ array
  		-3 - out all MTs EXCEPT those listed in 5$$
  6	kmod	mod number for ENDF thermal scattering law data (-1)
  		≥ 0 – use cross section data with this thermal mod number
  		-1 – use cross section data with latest thermal mod and kernel (if available)
  		-2 – do not include bound kernel data (i.e., free-gas scattering will be used in CENTRM)
  7	lsrc	Source of nuclear data  (0 only allowed at present)
  		0/1/2/3/4 => ENDF/JEF/JENDL/BROND/CENDL

  3** ENERGY LIMITS [2 entries]

  1	pemin	minimum energy for PW data	(0.0001 eV)
  2	pemax	maximum energy for PW data	(20 MeV)

  T  terminate data block 2

::

  **************     DATA BLOCK 3
  *****	Only enter if inum >0, or mtout= +/- 3 )

  4**   DESIRED TEMPERATURES for this nuclide  [inum entries]
  5$$   MT VALUES (if mtout = +/-3)   [always end with an "E"]

  T    terminate data block 3

  Optional  72 character title for the CENTRM library

.. _7-7-3:

CRAWDAD Sample Input
--------------------

:numref:`list7-7-1` shows an example input file for standalone execution of
CRAWDAD. The CRAWDAD output for this case is shown in :numref:`list7-7-2`. In
more typical cases where CRAWDAD is executed automatically by the XSProc
module as part of a SCALE sequence calculation, no CRAWDAD input is
needed, but similar CRAWDAD output will be printed.

.. code-block:: scale
  :name: list7-7-1
  :caption: CRAWDAD input generated by CSAS1 sample.

  =crawdad
  0$$   81   17   18    77         e
  1$$   5    66666  0   0   2   1  e
  1**   5.00E+00                   e
   t
  2$$  8016  7   3   2   2   -1   0
    3**   1.00-03   1.30+04         2t
    4**   6.00+02   9.00+02         3t
  2$$  13027  7   1   1   2  -1   0
    3**   1.00E-03   1.30E+04       2t
    4**   6.50E+02                  3t
  2$$  92235  7   7   1   2   -1   0
    3**   1.00E-03   1.30E+04       2t
    4**   9.00E+02                  3t
  2$$  92238  7   5   1   2   -1   0
    3**   1.00E-03   1.30E+04       2t
    4**   9.00E+02                  3t
  2$$  1001   7   5   1   2    0   0
    3**   1.00E-03   1.30E+04       2t
    4**   6.00E+02                  3t
  end
  ‚ move the generated PW CENTRM library to execution directory
  =shell
    mv ft81f001 $RTNDIR
  end shell
  ‘ ……………………………………………………………………

.. code-block:: scale
  :name: list7-7-2
  :caption: Sample output edit from CRAWDAD.

  A new centrm library has been written on unit number:   81
    The number of input nuclides was:                        5
    Number of Nuclides on output PW library:                 5
    Directory containing input PW library files:    /scale/scale6.dev/data/cekenolib_7.0


                    Description of Output CENTRM Library

   Entry    ZA   Data Src  Vers No.  Mod No.  MT-Optn  Thermal ID    XS temperatures
   -----  -----  --------  --------  -------  -------  ----------    ---------------
     1     8016    endf       7         3        2             0        600.00
                                                                        900.00
     2    13027    endf       7         1        2             0        650.00
     3    92235    endf       7         7        2             0        900.00
     4    92238    endf       7         5        2             0        900.00
     5     1001    endf       7         5        2       7000001        600.00



     Nuclides in Problem-Dependent Thermal Kernel Library

               Library Identifier:     901
                Number of kernels:       1
      Maximum Order of Scattering:       6
   Maximum Number of Temperatures:       9

   Library Directory
   Nuclide     Identifier  Sigfree  File
   ----------  ----------  -------  -------------------------------------------
   h(h2o)         7000001    20.48  endf_b/vers7/1-0

   ===============================================================================
   logical 18 (problem dependent centrm thermal kernel library)
   dataset name: /usr/tmp/xmw.9890/lib_cen_kernel
         volume:
   ===============================================================================

   CRAWDAD has terminated normally











.. bibliography:: bibs/CRAWDAD.bib
