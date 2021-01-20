.. _11-3:

COMPOZ Data Guide 
=================

*J. R. Knight* [1]_ *and L. M. Petrie* 

ABSTRACT

The COMPOZ program used to create the Standard Composition Library is
described. Of particular importance is documentation of the COMPOZ input
data file structure. Knowledge of the file structure allows users to
edit the data file and subsequently create their own site-specific
composition library.


ACKNOWLEDGMENT

This work was originally funded by the Office of Nuclear Material Safety
and Safeguards of the U.S. Nuclear Regulatory Commission.

.. _11-3-1:

Introduction
------------

COMPOZ is the program that creates (writes) the SCALE Standard
Composition Library. Data are input in free form. A text data file
containing the input to COMPOZ (and the Standard Composition Library) is
available with the SCALE system. Execution of COMPOZ using this data
file creates the Standard Composition Library currently available with
the SCALE package. This section provides documentation of the data file
structure. Knowledge of the data file structure allows users to edit the
data file and subsequently create their own site-specific or
user-specific composition library.

COMPOZ is intended to create or make *permanent* *changes* to and/or to
print the composition library and should not be used for any other
purpose. To avoid confusion with the Standard Composition Library
provided with SCALE, it is strongly recommended that only *new* keywords
and compositions be used in any site-specific or user-specific library.

.. _11-3-2:

Input Data Description
----------------------

COMPOZ input data are entered in free form. All data must be followed by
at least one blank. The COMPOZ input data file contains *five* data
records or blocks:

1. COMPOZ mode flag selects whether a new standard composition library
   will be created, or an old standard composition library will be
   listed. Only if a new library is being created are the following data
   records entered. A new library is created with a filename of
   “xfile089”. If an old library is being dumped as an ASCII file, it
   will be named “_sclN…N” where N…N is an 18 digit sequence number that
   is incremented starting from 0 for each library dumped in the same
   directory.

2. The header record contains the library identification, a set of
   parameters describing the size of the library, and library title with
   80 characters per line.

3. The standard composition table contains the name, theoretical
   density, number of elements, and other information about each
   standard composition. Individual nuclides, mixtures, and compounds
   are all included in the table.

4. The nuclide information table contains the nuclide identification
   number, atomic mass, and resonance energy cross sections.

5. The isotopic distribution table contains the nuclide identification
   number and the atom percent of each isotope used in specifying the
   default enrichment.

.. note:: For executing COMPOZ via SCALE, an =COMPOZ is required in the
  first eight columns of a record preceding the mode flag, and an END is
  required in the first three columns of a record inserted after the last
  data record. If debug output is desired, then use =COMPOZ PRINTDEBUG to
  execute compoz.

.. _11-3-2-1:

COMPOZ mode selector
~~~~~~~~~~~~~~~~~~~~

1. LGEN =

  0 – create a new library and list it

  1 – list an existing library

  >1 – list an existing library and write an ASCII input file.

If LGEN is 0, then input the following data to create a new standard
composition library.

.. _11-3-2-2:

Library heading information
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. IDT – library identification number

2. TITLE – 1 line of 80 characters used to identify the library

.. _11-3-2-3:

Standard composition table
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. SCID – Composition name, maximum of 12 characters.

2. ROTH – Theoretical density, gm/cm\ :sup:`3`.

3. ICP –

  0 for a mixture,

  1 for a compound.

4. NCZA – Element or nuclide ID

5. ATPM – Weight percent if ICP = 0. Number of atoms per molecule if ICP = 1.

6. END – Keyword END to terminate this standard composition.

For each composition, items 4 and 5 are repeated until all components of
the composition are described. Items 1 through 6 are entered in a
similar fashion for all compositions. After all the standard
compositions are read, terminate the table with an END [label], where
[label] represents an optional label.

.. _11-3-2-4:

Nuclide information table
~~~~~~~~~~~~~~~~~~~~~~~~~

1. NZA – Nuclide ID. This should be the mass number + 1000 \* the atomic
number.

2. AM – Atomic mass, C-12 scale.

3. SIGS – Resonance energy scattering cross section, barns.

4. SIGT – Resonance energy total cross section, barns.

5. NU*SIGF – Resonance energy nu*sigf cross section, barns.

The resonance energy cross sections are averaged over the appropriate
energy range for the nuclide. Items 1–5 are repeated for all nuclides.
After all nuclides are entered, terminate the nuclide table with an END
[label].

.. _11-3-2-5:

Isotopic distribution table
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. NZN – 1000 \* atomic number of variable isotope elements.

2. ISZA – Isotope ID.

3. ABWP – Default abundance, atom percent.

4. END – Keyword END to terminate this isotopic specification.

The default abundance is generally the naturally occurring abundance.
For each element, items 2 and 3 are repeated until 100% total abundance
is described, making a set for this element. The next element is
described in the same fashion in the next set, etc. After all isotopic
distributions are entered, terminate the isotopic distribution table
with an END [label].

.. _11-3-3:

Sample Problem
--------------

The following sample problem first lists the SCALE standard composition
library, then creates a new, short standard composition library, then
lists and outputs an ASCII copy of this new library, and finally copies
this new copy back to the output directory.

.. code:: scale
  :class: long

    =compoz
  '  print the current standard composition library
      1
  end
  =compoz
  '  create a new standard composition library
      0
  '  library identification number
    101
  '  library title
  scale-X standard composition library
  '  standard composition table
  '  all nuclide IDs here must be in the nuclide table
      h               1.0000    0        1001 100.0000 end
      o               1.0000    0        8016 100.0000 end
      u              19.0500    0       92000 100.0000 end
      h2o             0.9982    1        1001    2
                                         8016    1 end
      uo2            10.9600    1       92000    1
                                         8016    2 end
  '  end of standard composition table
     end stdcmp
  '  nuclide table
  '    ID       AWR     SigmaS      SigmaT      nuSigmaF
     1001   1.00783    20.38087    20.38782     0.00000
     1002   2.01410     3.39486     3.39487     0.00000
     8016  15.99491     3.88696     3.88696     0.00000
     8017  16.99913     3.74000     3.74501     0.00000
     8018  17.99916     3.79000     3.79000     0.00000
    92233 233.03964    12.46693    37.62292   100.78482
    92234 234.04095    12.18716    16.09542     2.66969
    92235 235.04393    11.90249    35.22383    90.23152
    92236 236.04556    12.27302    14.93351     1.33334
    92237 237.04874    14.24581    24.68619     1.93695
    92238 238.05080    12.32636    14.62708     0.65970
  '  end of nuclide table
     end nuclides
  '  isotope distribution table
  '  all nuclide IDs here must be in the nuclide table
     1000   1001  99.9885
            1002   0.0115 end
     8000   8016  99.7570
            8017   0.0380
            8018   0.2050 end
    92000  92234   0.0054
           92235   0.7204
           92238  99.2742 end
  '  end of isotope distribution table
      end isotopes
  '  end of compoz input
  end
  =compoz
  '  print and create an ASCII copy of the current standard composition library
  '  (created in the previous step)
    2
  end
  =shell
   # copy the ASCII copy back to the output directory
    copy_file _scl000000000000000000 ${OUTBASE}.stdcmplib
  end

.. [1]
   Formerly with Oak Ridge National Laboratory.
