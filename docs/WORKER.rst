.. _11-2:

WORKER: SCALE System Module for Creating and Modifying Working-Format Libraries
===============================================================================

L. M. Petrie

ABSTRACT

WORKER is a standalone utility module used to convert AMPX
master-formatted or working-formatted multigroup cross section libraries
into a single working library for SCALE transport calculations performed
by XSDRNPM, KENO V.a and KENO‑VI, and other modules. Beginning with
SCALE 6.2, WORKER is no longer used for calculations performed with
SCALE sequences because this function has been absorbed into the XSProc
module. This document gives instructions on how to use the WORKER
program as a standalone module.


ACKNOWLEDGMENTS

Several former ORNL staff made valuable contributions to the WORKER
development. The authors acknowledge the contributions of former ORNL
staff members S. Goluoglu, N. M. Greene, and D. F. Hollenbach.

.. _11-2-1:

Introduction
------------

Historically the AMPX nuclear data processing system [1]_ has defined
two formats for the multigroup (MG) libraries used in SCALE. The
“master” formatted library contains more general information than
normally required for radiation transport calculations. A master library
includes such information as 2D transfer arrays for all inelastic
levels, temperature-dependent thermal-scattering kernels, and Bondarenko
self-shielding data. A “working” formatted library contains only the
subset of these data needed for radiation transport calculations. A
working library contains only a single, combined 2D transfer array
[i.e., sum of elastic, all discrete inelastic levels, (n,2n), etc.], and
the temperature-dependent data normally have been interpolated to the
appropriate temperatures. In SCALE 6.2, more general formats for nuclear
data libraries are supported, and the MG libraries distributed with
SCALE are no longer restricted by the inflexible Master library format.
However the WORKER module is retained in SCALE 6.2 for manipulation of
legacy formatted libraries.

WORKER is a standalone program that reads input nuclear data library
files and produces a single working library file that can be read by
transport modules such as XSDRNPM, KENO‑VI, NEWT, CENTRM, and Monaco.
Prior to SCALE 6.2, the distributed MG libraries were stored in master
format, and WORKER was executed during every MG sequence to read the
master library file and write an output working library file
subsequently read by the transport codes run by the sequence. In modern
versions of AMPX and SCALE (e.g., SCALE 6.2 and later), the differences
in the master and working formats are superfluous, and the functions of
WORKER are now performed in memory by the XSProc module. Nevertheless,
WORKER may still be useful for manipulation of external library files
and for standalone execution of SCALE modules such as CENTRM and
XSDRNPM.

.. _11-2-2:

AMPX Library Format Conversion
------------------------------

The primary function of WORKER is to convert data from an initial AMPX
MG library file, with any format supported by SCALE, into the AMPX
working library format. The nuclear data files distributed with SCALE
provide MG data that are truly problem-independent and that can be
tailored at runtime for a particular application. These library files
must carry data at a sufficient level of detail to allow satisfying many
of the less-common but very powerful analyses such as cross section
sensitivity studies and coupled neutron-gamma transport calculations.
The nuclear data libraries include shielding factors used by the
Bondarenko self-shielding method. Temperature dependence of the
shielding factors and the thermal scattering kernel data is allowed. Any
number of scattering processes [e.g., elastic, discrete-level inelastic,
continuum inelastic, (n,2n), etc.] can be included to any degree of
anisotropic representation. In short, there is too much detail to
require transport codes to process this library.

WORKER processes and combines the data mentioned above into a form ready
for use by MG particle transport programs. The final output is an AMPX
working library file containing two types of data: group-averaged 1D
cross sections for an arbitrary number of processes for neutrons and/or
gamma rays, and total 2D transfer matrices (i.e., summed over the
scattering types) for neutrons and/or gamma rays. In some cases, the
transfer matrices on the master library are temperature-dependent.
WORKER performs linear interpolation to the temperature specified for
the nuclide, but it does not extrapolate outside the range of the data.
WORKER also has the option of producing an AMPX master library of the
selected nuclides interpolated to the specified temperature(s). For
resonance nuclides, the elastic scattering matrix is scaled uniformly to
make the matrix consistent with the self-shielded 1D values. The
P\ :sub:`ℓ`\ (ℓ > 0) matrices are scaled by the amount required for the
P\ :sub:`0` matrix. For processes involving multiple-exit neutrons
[e.g., (n,2n), (n,3n), etc.], WORKER multiplies by the appropriate
multiplicity before adding to the total transfer matrix. In the case of
coupled neutron-gamma libraries, gamma yields are sometimes expressed in
“yield” units, thereby requiring a multiplication by a cross section
before their introduction into the total transfer matrix. (This scheme
allows one to produce self-shielded gamma production cross sections.)

.. _11-2-3:

WORKER Input Specifications
---------------------------

The following is a description of WORKER input requirements and
input-output device requirements.

.. _11-2-3-1:

Input parameters
~~~~~~~~~~~~~~~~

WORKER uses FIDO-type input. The number of items to be input in an array
is shown in brackets, and default values are given in parentheses. If N1
and/or N7 are negative, a *direct access* master file will be assumed on
that unit. Note that direct access master files may use up to five
different units. The initial values of N1 or N7 will be used to
determine the starting unit number for the first file, and the unit
number will be incremented by 1 for each additional file.

Data block 1

-1$$ Option [1]

  1. NFISFOT – No Fission Photon Option (0)

    0 – add fission photons to the transfer array

    1 – do not add fission photons to the transfer array

0$ Logical Assignments [6]. This array is input only if a user needs to
modify default values.

  1. N1 – Input Master Cross section Library (1)

  2. N2 – Input Working Cross section Library (2)

  3. N4 – Output Working Cross section Library produced by WORKER (4)

  4. N5 – Scratch (18)

  5. N6 – Scratch (19)

  6. N7 – Output Temperature Interpolated Master Library (0)

1$ Integer Parameters [8]

  1. NUCM – Number of nuclides to be read from the input library, N1. (0)

  2. NUCW – Number of nuclides to be read from the input working library, N2. (0)

  3. IPRT – Output print option trigger. (2)

      -2 – no cross section edits

      -1 – edit reaction cross sections

      >-1 – edit reaction cross sections and transfer arrays through order
      IPRT

  4. IMST – Flag to copy entire Master Library. (0) (0 / >0 = only listed nuclides/all nuclides)

  5. IWRK – Flag to copy entire Working Library. (0) (0 / >0 = only listed nuclides/all nuclides)

  6. N1A – Sequence number of the filename for unit N1. (1)

  7. N2A – Sequence number of the filename for unit N2. (1)

  8. N4A – Sequence number of the filename for unit N4. (1)

**Data block 2**

WORKER can combine data from multiple input libraries to make the merged
output working library on logical Unit N4. This output working library
contains either the entire library specified or only those nuclides
selected on the specified library. If IMST is set greater than ZERO, the
entire input library is copied to the output working library. If IWRK is
set greater than ZERO, the entire input working library is copied to the
output working library. If there is no data in the ``4$$`` or ``5$$`` arrays,
the nuclide ID numbers listed in the ``2$$`` and ``3$$`` arrays remain
unchanged. For selected master libraries, nuclides are by default
selected at 300 K unless data is provided in the 6** array.

2$$

ID numbers from the input library on N1 of nuclides to be placed on
the output working library. If this array is not present and N1 is
specified or if IMST > 0, then all nuclides on N1 will be copied to the
output working library.

3$$

ID numbers from the input library on N2 of nuclides to be placed on
the output working Library. If this array is not present and N2 is
specified or if IWRK > 0, then all nuclides on N2 will be copied to the
output working library.

4$$

New ID numbers for nuclides from the input master library on N1 to
be placed on the output working Library. If this array is not present
and N1 is specified, then all nuclides on N1 that are to be copied to
the output working library will retain their original ID numbers. These
correspond on a one-to-one basis with the ID numbers entered in the
2$$ array.

5$$

New ID numbers for nuclides from the input library on N2 to be
placed on the output working library. If this array is not present and
N2 is specified, then all nuclides on N2 that are to be copied to the
output working library will retain their original ID numbers. These
correspond on a one-to-one basis with the ID numbers entered in the
$$ array.

6*\*

Thermal-Scattering kernel temperatures (K) for nuclides selected.
Scattering kernels are sometimes provided at several temperatures for a
nuclide on a master library. To get data at the specified input
temperature, WORKER will interpolate between temperature data. For
temperatures above the maximum or below the minimum temperature, WORKER
will not extrapolate but instead will use the maximum or minimum
temperature data. This array has no effect for sets of data with zero or
one thermal kernel.

7$$

MT number of the incoherent thermal-scattering kernel. These allow
selecting a thermal-scattering kernel with an MT (identifying) number
other than the default (1007).

8$$

Mixture numbers associated with the ID numbers in the 2$$ array.

9$$

Mixture numbers associated with the ID numbers in the 3$$ array.

  T – Terminate Block 2.

.. _11-2-3-2:

Abbreviated input description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Users who become familiar with the values required by WORKER will become
dissatisfied with having to use a detailed input description. The
description that follows is intended to serve as a “skeleton” guide for
these users:

Data Block 1

-1$$ Option (1)

  1.    NFISFOT     –     Fission     photon    flag

0$$ Logical Assignments (6)

  1. NT1 – Input library (1)

  2. NT2 – Working In (2)

  3. NT4 – Working Out (4)

  4. NT5 – Scratch (18)

  5. NT6 – Scratch (19)

  6. NT7 – Master Out (0)



1$ Integer Parameters [5]

  1. NMT – number from master

  2. NWT – number from working

  3. IPRT – cross section print option

  4. IMST – flag to copy entire master library

  5. IWRK – flag to copy entire working library

  6. N1A – flag to append integer to master library file

  7. N2A – flag to append integer to working library file

  8. N4A – flag to append integer to output library file

T Terminate Block 1.


Data Block 2

2$$ Identifiers of nuclides on input library (NUCM)

3$$ Identifiers of nuclides on working library (NUCW)

4$$ New identifiers for nuclides from input Library (NUCM)

5$$ New Identifiers for nuclides from working Library (NUCW)

6*\* Thermal Kernel Temperatures (NUCM)

7$$ MTs for incoherent thermal scattering matrices

8$$ Mixture numbers associated with identifiers in the ``2$$`` (NUCM)

9$$ Mixture numbers associated with identifiers in the ``3$$`` (NUCW)

T Terminate Block 2

.. _11-2-3-3:

Input/output assignments
~~~~~~~~~~~~~~~~~~~~~~~~

WORKER typically requires the following input-output devices during an
execution.

+----------------+--+----------------------------------------------+
| Logical Number |  | Purpose                                      |
+----------------+--+----------------------------------------------+
| NT1 (1)        |  | Input Cross section Library                  |
+----------------+--+----------------------------------------------+
| NT2 (2)        |  | Previously Prepared Working/Weighted Library |
+----------------+--+----------------------------------------------+
| NT4 (4)        |  | New Working Library                          |
+----------------+--+----------------------------------------------+
| NT5 (18)       |  | Scratch Unit                                 |
+----------------+--+----------------------------------------------+
| NT6 (19)       |  | Scratch Unit                                 |
+----------------+--+----------------------------------------------+
| NT7 (0)        |  | Temperature Interpolated Master Library      |
+----------------+--+----------------------------------------------+
| 5              |  | Record Input (when run outside of SCALE)     |
+----------------+--+----------------------------------------------+
| 6              |  | Printed Output                               |
+----------------+--+----------------------------------------------+

.. _11-2-4:

Sample Problem
--------------

A sample problem includes two calls to WORKER to represent different
capabilities. The input assumes there is a master library available on
Unit 84 that contains at least the following five nuclides—1001, 8016,
13027, 92235, and 92238—and a working library that contains the same
nuclides on Unit 70.

.. _11-2-4-1:

Sample problem input
~~~~~~~~~~~~~~~~~~~~

:numref:`list11-2-1` shows the input for the sample problem. The first call to
WORKER copies five nuclides from the master library on Unit 84 to the
working library on Unit 75. The ``0$$`` array specifies reading a master
library on Unit 84 and writing a working library on Unit 75. The
``1$$`` array specifies selecting five nuclides that are read from the
master library. The ``2$$`` array lists the five nuclides requested from the
master library: hydrogen (1001), oxygen (8016), aluminum (13027),
:sup:`235`\ U (92235), and :sup:`238`\ U (92238). The ``4$$`` array
specifies the new nuclide ID numbers. In this problem, the ``4$$`` array is
not needed since the ID numbers do not change. The 6** array specifies
selecting the thermal scattering kernel at 300 K for any nuclide having
multiple-scattering kernels.

The second call to WORKER combines a master and working library. The
``0$$`` array specifies reading a master library on Unit 70 and a working
library on Unit 75 and writing a new working library on Unit 79.
The ``1$$`` array specifies selecting five nuclides that are read from the
master library and five nuclides that are read from the working library.
The ``2$$`` array lists the five nuclides requested from the master library:
hydrogen (1001), oxygen (8016), aluminum (13027), :sup:`235`\ U (92235),
and :sup:`238`\ U (92238). The ``4$$`` array specifies the new nuclide ID
numbers for the master library nuclides. The ``3$$`` array lists the five
nuclides requested from the working library: hydrogen (1001), oxygen
(8016), aluminum (13027), :sup:`235`\ U (92235), and :sup:`238`\ U
(92238). The ``5$$`` array specifies the new nuclide ID numbers for the
working library nuclides. The 6** array specifies selecting the thermal
scattering kernel at 600 K for any nuclide from the MASTER library
having multiple-scattering kernels.

.. _list11-2-1:
.. code-block:: scale
  :caption: Sample problem input.

    =WORKER
      0$$ 84  0  75  E
      1$$  5  0  -2  -1  -1   E   T
      2$$ 1001 8016 13027 92238 92235  E
      4$$ 1001 8016 13027 92238 92235  E
      6** 300  300  300   300   300    E   T
    END

    =WORKER
      0$$ 70  75  79  E
      1$$  5  5  -2  -1  -1   E   T
      2$$ 1001 8016 13027 92238 92235  E
      3$$ 1001 8016 13027 92238 92235  E
      4$$ 3001001 3008016 2013027 1092238 1092235  E
      5$$ 6001001 6008016 5013027 4092238 4092235  E
      6** 600  600  600   600   600    E   T
    END


Reference
~~~~~~~~~

.. [1]
   D. Wiarda, M. L. Williams, C. Celik, and M. E. Dunn, “AMPX: A
   Modern Cross Section Processing System For Generating Nuclear Data
   Libraries,” *Proceedings of International Conference on Nuclear
   Criticality Safety,* Charlotte, N.C., Sept. 13–17, 2015.
