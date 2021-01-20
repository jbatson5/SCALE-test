.. _11-4:

ICE: Module to Mix Multigroup Cross Sections
============================================

*N. M. Greene,*\ :sup:`\*` *L. M. Petrie, S. K. Fraley*\ :sup:`\*` [1]_

ABSTRACT

ICE is a legacy SCALE utility program that reads microscopic cross
sections from an AMPX working library and uses input mixture number
densities to produce macroscopic cross sections, which are written to an
output file in the AMPX working library format. User input is entered
with the FIDO procedures.

.. _11-4-1:

Introduction
------------

ICE (**I**\ ntermixed **C**\ ross Sections **E**\ ffortlessly) is a
legacy SCALE utility program that reads microscopic cross sections from
an AMPX working library and uses input mixture number densities to
produce macroscopic cross sections, which are written to an AMPX working
library output file. The code was originally developed to allow
efficient cross section mixing with minimum user effort and with reduced
core storage requirements. The SCALE version of ICE is the latest in a
series [2]_ of versions of the program.

In previous versions of SCALE several sequences employed the ICE module
as a component in the self-shielding procedure; however in modern
sequences the functionality of ICE has been replaced by new routines in
the XSProc module. The ICE module is retained in the modern version of
SCALE mainly for use as a standalone executable module to compute
macroscopic cross sections and to provide backward compatibility with
legacy inputs.

.. _11-4-2:

Cross Section Mixing Expressions
--------------------------------

The mixing operations in ICE use the simple expressions presented below.

.. _11-4-2-1:

Cross-section mixing for AMPX libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the options that produce AMPX working libraries, the mixing of
cross sections involves a very simple summing of constituent values
times a number density for the constituent, that is, Σ, a macroscopic
value, is determined by

.. math::

  \Sigma=\sum_{j} N_{j} \sigma_{j}


where the j are the individual nuclides in the mixture whose number
density and microscopic cross sections are N\ :sub:`j` and σ\ :sub:`j`,
respectively.

The only exceptions to the above rule are for fissionable mixtures where
the number of neutrons per fission, υ\ :sub:`g`, or a fission spectrum,
χ\ :sub:`g`, is required:

.. math::

  v_{\mathrm{g}}=\frac{\sum_{j} N_{j} v_{g j} \sigma_{g j}}{\sum_{j} N_{j} \sigma_{f g j}}

χ\ :sub:`g` is defined as the fraction of the fission neutrons produced
by the mixture which fall in group g. By definition,

.. math::

  \sum_{\mathrm{g}} \chi_{\mathrm{g}}=1.0

ICE uses the following scheme to determine χ. First, terms F\ :sub:`g`
are determined by

.. math::
  :label: eq11-4-1

  \mathrm{F}_{\mathrm{g}}=\sum_{\mathrm{j}} \mathrm{N}_{\mathrm{j}} \chi_{\mathrm{g}, \mathrm{j}} \sum_{\mathrm{g}^{\prime}} \overline{\mathrm{v} \sigma}_{\mathrm{fg}^{\prime}, \mathrm{j}} \hat{\phi}_{\mathrm{g}^{\prime}} ,


where :math:`\text { VO } \mathrm{fg}, \mathrm{j}` is the average of the product of υ times σ\ :sub:`f` for the
nuclide, χ\ :sub:`g,j` is the nuclide fission spectrum, and :math:`\hat{\phi}_{\mathrm{g}}` is an
estimate for the integrated flux in group g´. Once the F\ :sub:`g` are
determined, χ\ :sub:`g` is determined by normalizing the sum of
F\ :sub:`g` to unity.

In many AMPX libraries, the integrals of the spectrum used to determine
the multigroup values are carried on the library for each nuclide. ICE
uses this nuclide-dependent spectrum to determine χ\ :sub:`g`. This
option should be exercised with caution, however, for no attempt is made
to ensure that the individual spectra are consistently normalized.

.. _11-4-3:

Input Instructions
------------------

The input to ICE uses the FIDO schemes described in the FIDO chapter. In
the descriptions, the number of entries expected in an array is given in
square brackets.

\*******************************************************************************\*

Card A (20A4)

Title card

Data Block 1

–1$ Direct-Access Specifications [4]

  1. NB8 No longer used.

  2. NL8 No longer used.

  3. NB9 No longer used.

  4. NL9 No longer used.

0$ Logical Unit Specifications for Various Cross-Section Libraries [5]

  1. INTAPE Input AMPX working library unit; default 4.

  2. IOT1 Output AMPX working library unit; default 3.

  3. IOT2 No longer used.

  4. IOT3 No longer used.

  5. IOT4 No longer used.

1$ Problem Size and Major Options [7]

  1. MIX Number of cross-section mixtures to be made.

  2. NMIX Number of mixing operations (elements times density operations) to be performed.

  3. IFLAG(1) Set greater than ten if AMPX working library output desired

  4. IFLAG(2) No longer used..

  5. IFLAG(3) No longer used..

  6. IFLAG(4) No longer used.

  7. KOPT No longer used.

T - Terminate Block 1

Data Block 2

2$ [NMIX]

1. (KM(I),I=1,NMIX) Mixture numbers in the mixture specification table –
values range from 1 to MIX.

3$ [NMIX]

1. (KE(I),I=1,NMIX) Element identifiers for the mixture specification
table.

4\* [NMIX]

1. (RHO(I),I=1,NMIX) Atom densities for the mixture specification table.

5$ [MIX]

1. (NCOEF(I),I=1,MIX) Number of Legendre coefficients, including
P\ :sub:`o`, to be mixed for each mixture.

6\* [NG+4]

No longer used.

12$ [NMIX]

\`1.(NUCMX(I),I=1,NMIX) Element mixture identifiers for the mixture
specification table.

7$ No longer used.

T - Terminate Data Block 2

Data Block 3

8$ [MIX] Required only if IFLAG(1) > 0

1. (MID(I),I=1,MIX) Mixture ID numbers for AMPX working library;
default (MID(I)=I,I=1,MIX)

9$ [N] No longer used.

.

.

10 No longer used.

11 No longer used.

T - Terminate Data Block 3

.. _11-4-4:

Sample Problem
--------------

A simple case has been selected to demonstrate the use of ICE. In this
case, it is desired to produce mixture cross sections for UO\ :sub:`2`
and H\ :sub:`2`\ O using basic data from ENDF version 7 238 group SCALE
library. Information pertinent to the basic data is given in the
following table:

+---------------+--+------------+--+---------------------+
| Nuclide       |  | Identifier |  | Order of Scattering |
+===============+==+============+==+=====================+
| :sup:`235`\ U |  | 92235      |  | 5                   |
+---------------+--+------------+--+---------------------+
| :sup:`238`\ U |  | 92238      |  | 5                   |
+---------------+--+------------+--+---------------------+
| O             |  | 8016       |  | 5                   |
+---------------+--+------------+--+---------------------+
| H             |  | 1001       |  | 5                   |
+---------------+--+------------+--+---------------------+

The atom densities to be used are:

UO\ :sub:`2`

   N(\ :sup:`235`\ U) = 0.01 atoms/(barn-cm)

   N(\ :sup:`238`\ U) = 0.04 atoms/(barn-cm)

   N(O) = 0.08 atoms/(barn-cm)

Water

   N(H) = 0.06 atoms/(barn-cm)

   N(O) = 0.03 atoms/(barn-cm)

In the sample case, we have elected to make an AMPX working library on
logical 61,

We have selected further to identify UO\ :sub:`2` with a 111 on the AMPX
working library.

CSAS-MG PARM=CHECK is run to set up the master library, then WORKER is
run to produce a working library for ICE.

A listing of the input follows:

.. highlight:: scale

::

  =csas-mg   parm=(check)
  cross sections for ice sample problem
  v7-238
  read composition
    atom   1 1 4  1001 1  8016 1  92235 1  92238 1  end atom
  end composition
  end
  =ice
  sample ice problem
  0$$  4 61 62 63 64
  1$$ 2 5 13 13 13 13 2  1t
  2$$ 3r1 2r2
  3$$ 92235 92238 8016 1001 8016
  4** 0.01  0.04  0.08 0.06 0.03
  5$$ 1 2
  12$$  f1
   2t
  8$$ 111 222  9$$ 1 2 3  11$$ 100 1111 2222  3t
  End



Reference
~~~~~~~~~

.. [1]
   :sup:`∗` Formerly with Oak Ridge National Laboratory.

.. [2]
   S. K. Fraley, *User’s Guide for ICE,* ORNL/CSD/TM-9, Union Carbide
   Corporation (Nuclear Division), Oak Ridge National Laboratory, July
   1976.
