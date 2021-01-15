.. _5B:

ORIGEN Utility Programs
=======================

.. sectionauthor:: I. C. Gauld, S. M. Bowman, and W. A. Wieselquist

There are three utility programs that may be of interest to ORIGEN
users: PRISM, ARPLIB, and XSECLIST. The traditional use of the PRISM
module has been to produce the set of TRITON input files necessary to
compile an ORIGEN reactor library, e.g. with varied enrichment and
moderator density. For the most part, this capability has been replaced
by the SLIG capability described in Appendix 5.A. The ARPLIB utility’s
main purpose is to remove burnup points from existing ORIGEN libraries,
e.g. to reduce the size on disk. The final utility, XSECLIST, provides a
simple way to print the burnup-dependent cross sections contained in the
ORIGEN library.

.. _5B-1:

PRISM
-----

PRISM is a utility that reads a single input template file containing
generic parameter flags and replaces them with specific values
designated by the user to generate any number of files containing
desired combinations of specific parameter values. PRISM provides a
procedure to convert a generic input file for a particular fuel assembly
design into a large number of input files containing combinations of
specific fuel enrichment and moderator densities and/or other parameters
for generating basic cross-section libraries. The program was designed
in a general manner so PRISM can be used to generate multiple files from
any generic file.

The input description for PRISM is presented in Table 5.B.1. The input
format is free form. The user input includes the name of the template
file to be read; the pattern for the name of the output files to be
generated, using the generic parameter flags; the number of generic
parameter flags; the number of files to be generated; each generic
parameter flag and the specific values to be substituted in each output
file.

The template file contains generic parameter flags. PRISM creates copies
of the template file and substitutes specific values for the generic
flags. **Note that the character length of each specific value must be
the same as that of the associated generic flag.**

An example using PRISM to generate input files for six fuel enrichments
is presented in :numref:`ex-origen-prism` and :numref:`ex-origen-prism-out`.
In this example a TRITON input file for a Westinghouse 17 × 17 fuel assembly
(:numref:`ex-origen-prism-out`) is processed by PRISM using the input file for
PRISM listed in :numref:`ex-origen-prism`. The case generates 6 specific input
files from the template file.


.. table:: PRISM input description
   :name: tab-origen-prism
   :widths: 10 20 35 35
   :align: center


   +----------------+----------------+-----------------+----------------+
   | **Line No.**   | **Parameter**  | **Description** | **Comments**   |
   +----------------+----------------+-----------------+----------------+
   | 1              | TEMPLATE       | Template file   | 80 characters  |
   |                |                | name            | maximum        |
   +----------------+----------------+-----------------+----------------+
   | 2              | OUT_TEMPLATE   | Pattern for     | 80 characters  |
   |                |                | output file     | maximum        |
   |                |                | names           |                |
   |                |                |                 | Must contain   |
   |                |                |                 | enough generic |
   |                |                |                 | parameter      |
   |                |                |                 | names to       |
   |                |                |                 | create unique  |
   |                |                |                 | filename for   |
   |                |                |                 | each output    |
   |                |                |                 | file           |
   +----------------+----------------+-----------------+----------------+
   | 3              | NUMPARMS       | Number of       |                |
   |                |                | generic         |                |
   |                |                | parameter       |                |
   |                |                | types           |                |
   +----------------+----------------+-----------------+----------------+
   |                | NUMFILES       | Number of       |                |
   |                |                | output files    |                |
   |                |                | to be           |                |
   |                |                | generated       |                |
   +----------------+----------------+-----------------+----------------+
   |                | **NOTE:** Repeat the following data for each      |
   |                | generic parameter type (i.e. a total of NUMPARMS  |
   |                | times).                                           |
   +----------------+----------------+-----------------+----------------+
   | 4              | PARAM_NAME     | Generic         | 80 characters  |
   |                |                | parameter name  | maximum        |
   |                |                | as it appears   |                |
   |                |                | in template     |                |
   |                |                | file            |                |
   +----------------+----------------+-----------------+----------------+
   | 5 [#f1]_       | PARAMETERS     | Specific        | NUMFILES       |
   |                |                | values of       | entries        |
   |                |                | generic         | required.      |
   |                |                | parameter for   | Length of      |
   |                |                | each output     | value must be  |
   |                |                | file            | same as length |
   |                |                |                 | of PARAM_NAME  |
   +----------------+----------------+-----------------+----------------+

.. [#f1] May be continued on subsequent lines as needed.

.. code-block:: none
   :name: ex-origen-prism
   :caption: PRISM input example to generate TRITON input files.

   =shell
     cp $RTNDIR/w17x17_template.input .
   end
   =prism
     w17x17_template.input
     w17_u235.inp
     5 6
     u234wt%
     0.01200 0.01639 0.02543 0.03473 0.04423 0.05389
     u235
     1.50 2.00 3.00 4.00 5.00 6.00
     u236wt%
     0.00690 0.00920 0.01380 0.01840 0.02300 0.02760
     u238wt%
     98.4811 97.9744 96.9608 95.9469 94.9328 93.9185
     namelibrary
     w17_e15.lib
     w17_e20.lib
     w17_e30.lib
     w17_e40.lib
     w17_e50.lib
     w17_e60.lib
   end
   =shell
     cp w17*.inp $RTNDIR
   end

.. code-block:: none
   :name: ex-origen-prism-out
   :caption: Generic TRITON input template for PRISM.

   =t-depl parm=nitawl
      PWR Westinghouse 17x17, 1/4 assembly model
      44groupndf5
      ' ----------------------------------------------------------------
      ' template to generate libraries for ORIGEN-S
      ' parameters are: u235 - wt% U-235
      ' u234wt% - wt% U-234
      ' u236wt% - wt% U-236
      ' u238wt% - wt% U-238
      ' namelibrary - name of ORIGEN library created
      ' ----------------------------------------------------------------
      ' Mixture data
      ' ----------------------------------------------------------------
      read comp
      ' fuel
      uo2 1 den=10.412 1 900 92234 u234wt%
      92235 u235
      92236 u236wt%
      92238 u238wt% end
      '
      ' clad
      zirc4 2 1 622 end
      ' water moderator with 630 ppm B
      h2o 3 den=0.723 1 575.5 end
      Figure .. Generic TRITON input template for PRISM.
      arbmb 0.723 1 1 0 0 5000 100 3 630e-06 575.5 end
      ' gap
      n 4 den=0.00125 1 622 end
      ' guide tube
      zirc4 5 1 575.5 end
      '
      end comp
      ' ----------------------------------------------------------------
      ' Cell data
      ' ----------------------------------------------------------------
      read celldata
      latticecell squarepitch pitch=1.259 3
      fueld=0.805 1
      gapd=0.822 4
      cladd=0.95 2
      end
      end celldata
      ' ----------------------------------------------------------------
      ' Depletion data
      ' ----------------------------------------------------------------
      read depletion
      1
      end depletion
      ' ----------------------------------------------------------------
      ' Burn data
      ' ----------------------------------------------------------------
      read burndata
      power=40.0 burn=1e-15 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      power=40.0 burn=75 down=0 end
      end burndata
      ' ----------------------------------------------------------------
      ' NEWT model data
      ' ----------------------------------------------------------------
      read model
      Westinghouse 17x17
      read parm
      cmfd=yes xycmfd=4
      run=yes echo=yes drawit=no
      end parm
      read materials
      1 1 ! fuel ! end
      2 1 ! clad ! end
      3 2 ! water ! end
      4 0 ! gap ! end
      5 1 ! guide tube ! end
      Figure 5.B.2. Generic TRITON input template for PRISM. (continued)
      end materials
      read geom
      unit 1
      com='regular fuel rod'
      cylinder 10 .4025
      cylinder 20 .411
      cylinder 30 .475
      cuboid 40 4p0.6295
      media 1 1 10
      media 4 1 20 -10
      media 2 1 30 -20
      media 3 1 40 -30
      boundary 40 4 4
      unit 5
      com='guide tube'
      cylinder 10 .57175
      cylinder 20 .6121
      cuboid 40 4p0.6295
      media 3 1 10
      media 5 1 20 -10
      media 3 1 40 -20
      boundary 40 4 4
      unit 11
      com='right half of fuel rod'
      cylinder 10 .4025 chord +x=0
      cylinder 20 .411 chord +x=0
      cylinder 30 .475 chord +x=0
      cuboid 40 0.6295 0.0 2p0.6295
      media 1 1 10
      media 4 1 20 -10
      media 2 1 30 -20
      media 3 1 40 -30
      boundary 40 2 4
      unit 12
      com='top half of fuel rod'
      cylinder 10 .4025 chord +y=0
      cylinder 20 .411 chord +y=0
      cylinder 30 .475 chord +y=0
      cuboid 40 2p0.6295 0.6295 0.0
      media 1 1 10
      media 4 1 20 -10
      media 2 1 30 -20
      media 3 1 40 -30
      boundary 40 4 2
      unit 51
      com='right half of guide tube'
      cylinder 10 .5715 chord +x=0
      cylinder 20 .6121 chord +x=0
      cuboid 40 0.6295 0.0 2p0.6295
      media 3 1 10
      media 5 1 20 -10
      media 3 1 40 -20
      boundary 40 2 4
      unit 52
      com='top half of guide tube'
      cylinder 10 .5715 chord +y=0
      cylinder 20 .6121 chord +y=0
      cuboid 40 2p0.6295 0.6295 0.0
      media 3 1 10
      media 5 1 20 -10
      media 3 1 40 -20
      boundary 40 4 2
      unit 53
      com='1/4 instrument tube'
      cylinder 10 .5715 chord +x=0 chord +y=0
      cylinder 20 .6121 chord +x=0 chord +y=0
      cuboid 40 0.6295 0.0 0.6295 0.0
      media 3 1 10
      media 5 1 20 -10
      media 3 1 40 -20
      boundary 40 2 2
      global unit 10
      cuboid 10 10.7015 0.0 10.7015 0.0
      array 1 10 place 1 1 0 0
      media 3 1 10
      boundary 10 34 34
      end geom
      read array
      ara=1 nux=9 nuy=9 typ=cuboidal
      fill
      53 12 12 52 12 12 52 12 12
      11 1 1 1 1 1 1 1 1
      11 1 1 1 1 1 1 1 1
      51 1 1 5 1 1 5 1 1
      11 1 1 1 1 1 1 1 1
      11 1 1 1 1 5 1 1 1
      51 1 1 5 1 1 1 1 1
      11 1 1 1 1 1 1 1 1
      11 1 1 1 1 1 1 1 1
      end fill
      end array
      read bounds
      all=refl
      end bounds
      end model
      end
      =shell
        cp ft33f001.cmbined $RTNDIR/namelibrary
      end

.. _5B-2:

ARPLIB
------

ARPLIB is a utility program designed to read a burnup-dependent binary
ORIGEN-ARP cross-section library and copy the cross-section data from
only the desired burnup positions to create a new ORIGEN-ARP
cross-section library.

The input for ARPLIB is described in :numref:`tab-origen-arplib`. A new
library (OUTLIB) is created by listing the positions from one or more existing
libraries to copy to the new library.

An example of the input to ARPLIB is given in :numref:`ex-origen-arplib`,
showing how to use ARPLIB to reduce the number of cross sections sets on a
library by creating a new library with only certain positions retained from the
old library.


.. table:: ARPLIB input description
   :name: tab-origen-arplib
   :widths: 15 40 35
   :align: center

   +---------------+-------------------------+-------------------------+
   | **Parameter** | **Description**         | **Comments**            |
   +---------------+-------------------------+-------------------------+
   | OUTLIB        | Filename of output      | This library should not |
   |               | library to create       | already exist           |
   +---------------+-------------------------+-------------------------+
   | NLIB          | Number of input         |                         |
   |               | libraries to read       |                         |
   +---------------+-------------------------+-------------------------+
   |               | **For each input library, i up to NLIB**          |
   +---------------+-------------------------+-------------------------+
   | LIBNAME[i]    | Filename of input       |                         |
   |               | library to read         |                         |
   +---------------+-------------------------+-------------------------+
   | NPOS[i]       | Number of positions to  | >0                      |
   |               | read from this i-th     |                         |
   |               | library                 |                         |
   +---------------+-------------------------+-------------------------+
   | p1 p2 …       | The list of position    | NPOS[i] position        |
   |               | indices from this i-th  | indices are read from a |
   |               | library to put on the   | single line (all        |
   |               | output library          | position indices are    |
   |               |                         | >0)                     |
   +---------------+-------------------------+-------------------------+

.. code-block:: none
   :caption: ARPLIB example input to reduce size of ORIGEN cross-section libraries.
   :name: ex-origen-arplib

   'get an ORIGEN library files for testing
   =shell
     cp "${DATA}/arplibs/w17_e30.f33" 1_f33
   end
   'create a new library (ft33f001) with every-other burnup points
   =arplib
     ft33f001
     1
     1_f33
     8
     1 3 5 7 9 11 13 15
    end

.. _5B-3:

XSECLIST
--------

The XSECLIST program is intended to provide an interpreted listing of
any ORIGEN-ARP cross-section library. This utility program allows users
to list the absorption and/or fission cross sections of any or all
nuclides in the library as a function of burnup. The absorption
cross sections are given for light elements, actinides, and fission
products. Some of the light-element isotopes in the library may appear
also as fission products; therefore, some isotopes may be listed twice.
Fission cross sections may be listed for any or all actinides for which
nonzero values of the cross sections exist. ORIGEN-S cross sections are
typically normalized to thermal flux, rather than the total flux.

The nuclide ID numbers used in the library listings have the form
IZ*10000+IA*10+IS, where

   IZ = the atomic number;

   IA = the atomic weight;

   IS = 0, for ground state;

   IS = 1, for metastable state.

The XSECLIST input is described in :numref:`tab-origen-xseclist`. The input is
free format. The user specifies the library filename, the total number of
burnup positions in the library, and the burnup values (GWd/MTU) corresponding
to each burnup position. The user then indicates whether the cross-section
data listings are for absorption, fission, or both; and whether the listings
are for all nuclides or only certain specified ones.

An example input file for XSECLIST is shown in :numref:`ex-origen-xseclist`.
This example contains two cases: The first case lists both absorption and
fission cross sections for :sup:`240`\ Pu in the ORIGEN-ARP 5 wt %
enriched PWR 14 × 14 basic cross-section library. The output listing for
this case is displayed in :numref:`ex-origen-xseclist-pu240`. These are
microscopic cross sections listed in units of barns. The second case lists the
fission cross sections for all nuclides in the ORIGEN‑ARP 1.5 wt % enriched PWR
14 × 14 basic cross-section library. The output from this case is not
presented here because of its size.


.. table:: XSECLIST input description
   :name: tab-origen-xseclist
   :widths: 10 20 35 35

   +----------------+----------------+-----------------+------------------+
   | **Line No.**   | **Parameter**  | **Description** | **Comments**     |
   +----------------+----------------+-----------------+------------------+
   | 1              | FILENAME       | Library         | 30-character     |
   |                |                | filename        | maximum          |
   +----------------+----------------+-----------------+------------------+
   | 2              | NL             | Number of       |                  |
   |                |                | burnup          |                  |
   |                |                | positions in    |                  |
   |                |                | library         |                  |
   +----------------+----------------+-----------------+------------------+
   | 3\ [#f2]_      | BURN           | Burnup          | NL entries       |
   |                |                | (GWd/MTU) of    | required         |
   |                |                | each burnup     |                  |
   |                |                | position in     |                  |
   |                |                | library         |                  |
   +----------------+----------------+-----------------+------------------+
   | 4              | CHARD          | Cross-section   | a = absorption   |
   |                |                | data to be      |                  |
   |                |                | printed         | f = fission      |
   |                |                |                 |                  |
   |                |                |                 | b = both         |
   +----------------+----------------+-----------------+------------------+
   | 5              | CHARL          | List entire     | y = yes          |
   |                |                | library (all    |                  |
   |                |                | nuclides)       | n = no           |
   +----------------+----------------+-----------------+------------------+
   |                | **NOTE: The following optional data are entered**   |
   |                | **only if CHARL = n.**                              |
   +----------------+----------------+-----------------+------------------+
   | 6              | MT             | Number of       |                  |
   |                |                | nuclides for    |                  |
   |                |                | which           |                  |
   |                |                | cross-section   |                  |
   |                |                | listings are    |                  |
   |                |                | desired         |                  |
   +----------------+----------------+-----------------+------------------+
   | 7\ [#f2]_      | MTRD           | Nuclide         | MT entries       |
   |                |                | IDs [#f3]_      | required         |
   +----------------+----------------+-----------------+------------------+

.. [#f2] May be continued on subsequent lines as needed.

.. [#f3] Nuclide ID = Atomic No. \* 10000 + Atomic wt \* 10 + IS,
       where IS = 0 for ground state and 1 for metastable state.


.. code-block:: none
   :caption: XSECTLIB input example
   :name: ex-origen-xseclist

   =xseclist
   ce14_e50.arplib
   10
   0.0 1.5 4.5 7.5 10.5 13.5 16.5 31.5
   46.5 58.5
   b
   n
   1
   942400
   end
   =xseclist
   ce14_e15.arplib
   10
   0.0 1.5 4.5 7.5 10.5 13.5 16.5 31.5
   46.5 58.5
   f
   y
   end


.. code-block:: none
   :caption: XSECLIST listing of :sup:`240`\ Pu data.
   :name: ex-origen-xseclist-pu240

   \*****\* absorption cross sections \*****\*
   ----------- light elements -----------
   ------- end of light elements --------
   ------------- actinides --------------
   material= 942400 (pu240 )
   burnup xsec
   0.00000E+00 1.65356E+03
   1.50000E+00 1.69928E+03
   4.50000E+00 1.60593E+03
   7.50000E+00 1.47163E+03
   1.05000E+01 1.34200E+03
   1.35000E+01 1.22895E+03
   1.65000E+01 1.13326E+03
   3.15000E+01 8.27437E+02
   4.65000E+01 6.82870E+02
   5.85000E+01 6.15974E+02
   --------- end of actinides -----------
   --------- fission products ----------
   ------ end of fission products -------
   \****\* end of absorption cross sections \***\*
   \*****\* fission cross sections \*****\*
   material= 942400 (pu240 )
   burnup xsec
   0.00000E+00 4.51353E+00
   1.50000E+00 4.71392E+00
   4.50000E+00 4.82682E+00
   7.50000E+00 4.89713E+00
   1.05000E+01 4.93990E+00
   1.35000E+01 4.96174E+00
   1.65000E+01 4.96700E+00
   3.15000E+01 4.82935E+00
   4.65000E+01 4.56642E+00
   5.85000E+01 4.34749E+00
   \****\* end of fission cross sections \****\*

.. raw:: latex

  \clearpage
