.. _7-2:

Standard Composition Library
============================

*L. M. Petrie, R. A. Lefebvre, and D. Wiarda*

ABSTRACT

The SCALE Standard Composition Library provides a flexible and
convenient means of generating models that include many types of
materials. Users may specify materials as individual nuclides; elements
with tabulated natural abundances; compounds, alloys, mixtures, and
fissile solutions commonly encountered in engineering practice.

ACKNOWLEDGMENTS

This work was originally funded by the U.S. Nuclear Regulatory
Commission through the Office of Nuclear Material Safety and Safeguards
and the Office of Nuclear Regulatory Research. Continuing support is
provided by the U.S. Department of Energy Nuclear Criticality Safety
Program.

.. _7-2-1:

Introduction
------------

The Standard Composition Library has been included within the SCALE
system to provide the user with a simple and straightforward method of
specifying the material mixtures for a given problem. The library
consists of over 700 mixtures and isotopes commonly used within
criticality safety, shielding, and reactor physics models. This library
is tabulated in :ref:`7-2-2` with the various features of each
composition. Additionally, a number of standard fissile solutions
available for use are tabulated in :ref:`7-2-3`.

The Standard Composition Library is created using the COMPOZ module, and
can be updated by users as desired.

.. _7-2-2:

The Standard Composition Library
--------------------------------

The Standard Composition Library describes the various isotopes,
elements (both symbols and full name), and compounds/alloys that can be
used to define the material mixtures for a given problem. Typically, the
alphanumeric description of one or more of these materials will be used
to define a material mixture.

When formulating a mixture, it is often necessary to know the density
(g/cm\ :sup:`3`) of the various constituent materials. For convenience,
the reference values given in the library have been listed in
:numref:`tab7-2-2` through :numref:`tab7-2-5`. Note that the given reference values
represent the actual theoretical density, except in the case of isotopes
and some individual nuclides where a default value of 1.0 g/cm\ :sup:`3`
is used. The actual theoretical densities are fixed values at naturally
occurring or nominal conditions. These default densities should not be
used for materials containing enriched isotopes, especially light
elements with isotopes that are strong absorbers such as boron,
B\ :sub:`4`\ C, or lithium. When densities are recalculated by other
codes such as KENO, the recalculated densities may differ slightly from
those given in the Standard Composition Library depending on the
cross-section library specified in the calculation.  Note that the
recalculated mixture densities are presented for information purposes
and are not used in the calculations.

Note that not all nuclides in the Standard Composition Library are
available on each cross-section library, and user are encourage to
review the code output for warning messages regarding composition data.
Refer to the cross section library chapter for listings of available
nuclides in each cross-section library.

Multiple sets of iron, nickel, and chromium nuclides are available in
the Standard Composition Library. These sets correspond to different
weighting functions used in generating the multigroup cross sections.
One special weighting function corresponds to 1/[E σ\ :sub:`t`\ (E)],
where σ\ :sub:`t`\ (E) is the total cross section of the referenced
nuclide or alloy. Entries have been added to the isotopic distribution
table so that standard weighted isotopes will be requested if the
desired nuclide is not on the specified library.

The nuclide identifying numbers (IDs) are listed in –. Typically, the ID
is 1000*Z + A, where Z and A are the charge and mass numbers for the
nuclide (e.g., 1001 for :sup:`1`\ H and 8016 for :sup:`16`\ O).
Exceptions to this rule include metastable nuclides, nuclides with bound
thermal scattering data, and nuclides whose cross sections have a
special weighting. Also, elements with isotopic mixtures (typically
natural abundance) have IDs of Z* 1000.

If a nuclide identifier is listed in :numref:`tab7-2-1`, it can be accessed
and used in a user‑specified material (a.k.a., arbitrary material).
User-specified materials require the user to provide all the information
normally found in the Standard Composition Library. Refer to the XSProc
manual for details on how to input user-specified materials.

Several materials contain multiple isotopes of a single element. For
these materials, the user is free to specify the isotopic distribution
as discussed in the XSProc chapter. Alternatively, the user may elect
not to enter this data, thereby telling the code to assume the default
values shown in the tables. In describing a user-specified material, a
multiple isotope ID of Z * 1000 can be used to denote the elements of
:numref:`tab7-2-2`. Note that even if the natural abundances from :numref:`tab7-2-2`
are accessed through elemental specification, not all nuclides are
necessarily present on each cross-section library. Refer to the Cross
Section Library chapter for listings of available nuclides in each
cross-section library.

Atomic masses for the isotopes were taken from “The Ame2003 atomic mass
evaluation (II)” by G. Audi et al. :cite:`audi_ame2003_2003`. The atom percents of the
isotopic distribution table were taken from “Isotopic Compositions of
the Elements, 2001” by J. K. Bö̈hlke :cite:`bohlke_isotopic_2005`. Densities were taken from
several sources, including the CRC Handbook of Chemistry and
Physics :cite:`weast_crc_2001`. Gases and explicit isotopes were changed to all have a
theoretical density of 1.0 g/cm\ :sup:`3`.

To more fully document the composition of each compound and/or document
the assumptions used in producing the associated cross-section data, a
brief description is given in the tables where needed.

.. _tab7-2-1:
.. list-table:: Isotopes in standard composition library.
  :align: center

  * - .. image:: figs/stdcmp/tab1-1.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-2.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-3.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-4.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-5.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-6.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-7.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-8.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-9.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-10.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-11.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-12.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-13.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-14.svg
        :width: 300


.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-15.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-16.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-17.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-18.svg
        :width: 300


.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-19.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-20.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-21.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-22.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-23.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-24.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-25.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-26.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-27.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-28.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-29.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-30.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-31.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-32.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-33.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-34.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-35.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-36.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-37.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-38.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-39.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-40.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-41.svg
        :width: 300


.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-42.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-43.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-44.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-45.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-46.svg
        :width: 300


.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-47.svg
        :width: 300


.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-48.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-49.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-50.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-51.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-52.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-53.svg
        :width: 300


.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-54.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-55.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-56.svg
        :width: 300


.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-57.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-58.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-59.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-60.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-61.svg
        :width: 300

.. list-table:: Isotopes in standard composition library (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab1-62.svg
        :width: 300

.. _tab7-2-2:
.. list-table:: Elements and their natural abundances.
  :align: center

  * - .. image:: figs/stdcmp/tab2-1.svg
        :width: 500

.. list-table:: Elements and their natural abundances (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab2-2.svg
        :width: 500

.. list-table:: Elements and their natural abundances (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab2-3.svg
        :width: 500

.. list-table:: Elements and their natural abundances (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab2-4.svg
        :width: 500

.. list-table:: Elements and their natural abundances (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab2-5.svg
        :width: 500

.. list-table:: Elements and their natural abundances (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab2-6.svg
        :width: 500

.. _tab7-2-3:
.. list-table:: Elements and special nuclide symbols.
  :align: center

  * - .. image:: figs/stdcmp/tab3.svg
        :width: 500

.. _tab7-2-4:
.. list-table:: Compounds.
  :align: center

  * - .. image:: figs/stdcmp/tab4-1.svg
        :width: 500

.. list-table:: Compounds (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab4-2.svg
        :width: 500

.. list-table:: Compounds (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab4-3.svg
        :width: 500


.. _tab7-2-5:
.. list-table:: Alloys and mixtures.
  :align: center

  * - .. image:: figs/stdcmp/tab5-1.svg
        :width: 500

.. list-table:: Alloys and mixtures (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab5-2.svg
        :width: 500

.. list-table:: Alloys and mixtures (continued).
  :align: center

  * - .. image:: figs/stdcmp/tab5-3.svg
        :width: 500

.. _7-2-3:

Table of Fissile Solutions
--------------------------

The Standard Composition Library ( through ) describes the various
compounds, alloys, elements, and isotopes one may use in defining the
material mixtures for a given problem. In addition to the various
materials listed there, one is also free to use any of the fissile
solutions listed in :numref:`tab7-2-6`. Indeed, the user is encouraged to treat
the solutions listed in :numref:`tab7-2-6` as he would any other standard
composition. Using empirical fits to experimental data, the code will
then automatically calculate the density of the solution, or the user
can explicitly specify the density. The code then calculates the volume
fraction corresponding to the heavy metal, acid, and water components of
the solution. A fissile solution starts with the keyword, SOLUTION,
after which one or two salts and the corresponding acid may be
specified. Input specifications for fissile solutions can be found in
:ref:`7-1`.

.. _tab7-2-6:
.. table:: Available fissile solution components.
  :align: center

  +---------------------------------------+-----------------+
  | **Name of**                           | **Nuclides in** |
  | **component**                         | **component**   |
  +=======================================+=================+
  | Nitrate solutions                     |                 |
  +---------------------------------------+-----------------+
  | UO\ :sub:`2`\ (NO\ :sub:`3`)\ :sub:`2`| 92000 7000 8000 |
  +---------------------------------------+-----------------+
  | Pu(NO\ :sub:`3`)\ :sub:`4`            | 94000 7000 8000 |
  +---------------------------------------+-----------------+
  | Th(NO\ :sub:`3`)\ :sub:`4`            | 90000 7000 8000 |
  +---------------------------------------+-----------------+
  | HNO\ :sub:`3` ACID                    | 1000 7000 8000  |
  +---------------------------------------+-----------------+
  | Fluoride solutions                    |                 |
  +---------------------------------------+-----------------+
  | UO\ :sub:`2`\ F\ :sub:`2`             | 92000 8000 9000 |
  +---------------------------------------+-----------------+
  | PuF\ :sub:`4`                         | 94000 9000      |
  +---------------------------------------+-----------------+
  | ThF\ :sub:`4`                         | 90000 9000      |
  +---------------------------------------+-----------------+
  | HFACID                                | 1000 9000       |
  +---------------------------------------+-----------------+




.. bibliography:: bibs/stdcmp.bib
