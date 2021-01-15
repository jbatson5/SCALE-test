.. _5-2:

Origen Data Resources
=====================

*I. C. Gauld, D. Wiarda, M. Pigni, W. Wieslequist*

ABSTRACT

.. |nbsp| unicode:: 0xA0
   :trim:

ORIGEN data resources include nuclear decay data, multigroup neutron
reaction cross sections, neutron-induced fission product yields, and
decay emission data for photons, neutrons, alpha particles and beta
particles. The nuclear decay data are based primarily on ENDF/B-VII.1
evaluations. The multigroup nuclear reaction cross section libraries now
include evaluations from the JEFF‑3.0/A neutron activation file
containing data for 774 target nuclides, more than
12,000 neutron-induced reactions, and more than 20 different reaction
types below 20 MeV, provided in various energy group structures.
Energy-dependent ENDF/B-VII.0-based fission product yields are available
for 30 fissionable actinides. Gamma-ray and x-ray emission data
libraries are based on ENDF/B-VII.1. The photon libraries contain
discrete photon line energy and intensity data for decay gamma and
x-rays emission for 1,132 radionuclides, prompt and delayed continuum
spectra for spontaneous fission, :math:`\left( \alpha,n \right)` reactions in oxide fuel,
and bremsstrahlung from decay beta (electron and positron) particles slowing
down in either a UO\ :sub:`2` fuel or water matrix. Methods and data
libraries used to calculate the neutron yields and energy spectra for
spontaneous fission, :math:`\left( \alpha,n \right)` reactions, and delayed neutron
emission are adopted from the SOURCES4C code. Capabilities to calculate
the beta and alpha particle emission source and spectra have also been added.

ACKNOWLEDGMENTS

Development and testing of ORIGEN data resources, libraries, and methods
have been sponsored by many organizations including the US Nuclear
Regulatory Commission (NRC), the US Department of Energy (DOE), and
nuclear power and research institutions.

VERSION INFORMATION

Following is a description of the data resources available for use with
ORIGEN in different SCALE versions. Methodologies and algorithms used in
applying the data are described in the ORIGEN chapter.

.. centered:: Version 6.2 (2016)

*Data lead(s):* I. C. Gauld, D. Wiarda, M. Pigni, and W. Wieselquist

Nuclear data in ORIGEN are unchanged from SCALE 6.1.3 except for the
modification of independent fission yields for thermal fission of
:sup:`235`\ U and :sup:`241`\ Pu and fast fission of :sup:`238`\ U to
provide greater compatibility between the direct and cumulative fission
yields when using the updated decay data from ENDF/B-VII.1.
Additionally, ORIGEN no longer has its own independent source of nuclide
mass and abundance data and now relies on the SCALE Standard Composition
library so that there is consistency in this data across SCALE. D.
Mueller and W. Wieselquist are acknowledged for testing of the new yield
data. W. Wieselquist and S. Hart are acknowledged for the revision of
this chapter.

.. centered:: Version 6.1.3 (2011)

*Data lead(s):* I. C. Gauld and D. Wiarda

SCALE 6.1 represented a complete revision and update of the nuclear data
available in ORIGEN. The following is a summary from the SCALE 6.1
manual.

   The ORIGEN data libraries include nuclear decay data, neutron
   reaction cross sections, neutron induced fission product yields,
   delayed gamma-ray emission data, and neutron emission data. The
   nuclear decay data libraries have been updated based on ENDF/B-VII
   evaluations and expanded to include 903 activation products and
   structural materials, 174 actinides, and 1149 fission products. The
   cross section libraries have been revised using evaluations from the
   JEFF-3.0/A neutron activation file, containing data for 774 target
   nuclides, more than 12,000 neutron-induced reactions, and more than
   20 different reaction types below 20 MeV. The JEFF-3.0/A activation
   file is processed into several multigroup cross section libraries,
   from 44 groups to 238 groups, that can be used to determine the
   neutron reaction transition rates in ORIGEN. Energy-dependent
   ENDF/B-VII fission product yields are provided for 30 fissionable
   actinides. Photon yield data libraries have been updated based on the
   most recent ENSDF nuclear structure evaluations processed using the
   NuDat program. The photon libraries contain discrete photon line
   energy and intensity data for decay gamma and x-rays emission for 982
   radionuclides, prompt and equilibrium continuum fission product
   spectra from spontaneous fission, :math:`\left( \alpha,n \right)` reactions in oxide fuel, and
   bremsstrahlung from decay beta (negatron and positron) particles
   slowing down in either UO\ :sub:`2` fuel or water matrix. Methods and data
   libraries used to calculate the neutron yields and energy spectra for
   spontaneous fission, :math:`\left( \alpha,n \right)` reactions in any matrix, and delayed
   neutron emission are adopted from the SOURCES code. The libraries
   used by ORIGEN can be coupled directly with detailed and
   problem-dependent physics calculations to obtain self-shielded
   problem-dependent cross sections based on the most recent evaluations
   of ENDF/B-VII. In addition, the library formats allow multiple sets
   of cross section data to be stored on a library to represent the
   changes in cross sections during irradiation.

.. _5-2-1:

Introduction
------------

ORIGEN data resources include nuclear decay data, multigroup neutron
reaction cross sections, neutron-induced fission product yields, and
decay emission data for photons, neutrons, alpha particles and beta
particles. The available resources are summarized in
:numref:`tab-origen-resources` and described in greater detail in the
subsequent sections. The "Unit" column shows the corresponding unit number
for use with FIDO input systems (e.g. with COUPLE).


.. table:: Available resources in ORIGEN
   :name: tab-origen-resources
   :align: center
   :class: longtable

   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | **Description**                | **Alias** | **Unit** | **Category** | **Location in SCALE data directory**      |
   +================================+===========+==========+==============+===========================================+
   | ENDF/B-VII.1 decay data        | decay     | 27       | Decay        | origen_data/origen.rev03.decay.data       |
   |                                |           |          |              |                                           |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | ENDF/B-VII.0-based             | yields    | 17       | Yield        | origen_data/origen.rev05.yields.data      |
   | fission yield data             |           |          |              |                                           |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | JEFF-3.0/A – 44g               | n44       | 79       | Reaction     | origen.rev03.jeff44g                      |
   |                                |           |          |              | ev03.jeff44g                              |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | JEFF-3.0/A – 47g               | n47       | 22       | Reaction     | origen.rev003.jeff47g                     |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | JEFF-3.0/A – 49g               | n49       | 77       | Reaction     | origen.rev03.jeff49g                      |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | JEFF-3.0/A – 56g               | n56       | 75       | Reaction     | origen.rev01.jeff56g                      |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | JEFF-3.0/A – 200g              | n200      | 78       | Reaction     | origen.rev03.jeff200g                     |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | JEFF-3.0/A – 238g              | n238      | 80       | Reaction     | origen.rev03.jeff238g                     |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | JEFF-3.0/A – 252g              | n252      | 74       | Reaction     | origen.rev01.jeff252g                     |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | JEFF-3.0/A – 999g              | n999      | 76       | Reaction     | origen.rev01.jeff999g                     |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | Energy per fission and capture |           |          | Energy       | n/a                                       |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | Master photon (x-ray and       |           |          | Emission     | origen_data/origen.rev04.mpkkxgam.data    |
   | gamma) emission data           |           |          |              |                                           |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | Spontaneous fission and        |           |          | Emission     | origen_data/origen.rev00.mpsfangm.data    |
   | :math:`\left(\alpha,n \right)` |           |          |              |                                           |
   | reaction gamma rays            |           |          |              |                                           |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | Bremsstrahlung from beta       |           |          | Emission     | origen_data/origen.rev00.mpbrh2om.data    |
   | particles slowing down in      |           |          |              |                                           |
   | water                          |           |          |              |                                           |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | Bremsstrahlung from positrons  |           |          | Emission     | origen_data/origen.rev00.mpbrh2op.data    |
   | slowing down in water          |           |          |              |                                           |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | Bremsstrahlung from beta       |           |          | Emission     | origen_data/origen.rev00.mpbruo2m.data    |
   | particles slowing down in      |           |          |              | igen_data/or                              |
   | UO\ :sub:`2`                   |           |          |              |                                           |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | Bremsstrahlung from positrons  |           |          | Emission     | origen_data/origen.rev00.mpbruo2p.data    |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | Neutron source emission and    |           |          | Emission     | origen_data/origen.rev01.alphdec.data     |
   | alpha decay data               |           |          |              | rigen_data/o                              |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | Alpha particle stopping cross  |           |          | Emission     | origen_data/origen.rev00.stcoeff.data     |
   | section expansion coeffcients  |           |          |              |                                           |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | Target                         |           |          | Emission     | origen_data/origen.rev00.alphyld.data     |
   | :math:`\left( \alpha,n\right)` |           |          |              |                                           |
   | product excited level          |           |          |              |                                           |
   | branching data                 |           |          |              |                                           |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | Target                         |           |          | Emission     | origen_data/origen.rev00.alphaxs.data     |
   | :math:`\left(\alpha,n \right)` |           |          |              |                                           |
   | cross section data             |           |          |              |                                           |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+
   | Beta source emission data      |           |          | Emission     | origen_data/origen.rev00.ensdf95beta.data |
   +--------------------------------+-----------+----------+--------------+-------------------------------------------+

.. _5-2-2:

Decay Resource
--------------

The nuclear data stored on the decay resource is based on ENDF/B-VII.1
evaluations :cite:`ENDF-VII.1`, including half-lives, decay modes and branching
fractions, and recoverable energy per disintegration. Decay modes
include beta (:math:`\beta^-`), positron (:math:`\beta^+`) and electron capture (EC),
isomeric transition (IT), alpha (:math:`\alpha`), spontaneous fission (SF), delayed
neutron (:math:`\beta^-\,n`) emission, neutron emission (n), double beta decay
:math:`\left( \beta^- \beta^- \right)`, and decay by beta and alpha emission (:math:`\beta^- \alpha`).
The decay resource also includes radiotoxicity factors based on the radioactivity concentration
guides (RCGs) for air and water as defined in Part 10, Title 20, of the
Code of Federal Regulations (10CFR20) :cite:`10CFR20`. RCGs specify the maximum
permissible concentrations of an isotope in soluble and insoluble forms
for both ingestion and inhalation and for occupational and unrestricted
exposure. The radiotoxicity is calculated as the dilution volume of a
nuclide for cases of direct ingestion or inhalation. The values are
defined to be the smaller (i.e., more toxic) of the values for soluble
and insoluble forms of the isotope. The maximum permissible RCGs for air
and water are the public exposure limits for adult ingestion and
inhalation dose coefficients of ICRP Publication 72 :cite:`ICRP72`. External
exposure dose coefficients for noble gases were obtained from the
Environmental Protection Agency (EPA) Federal Guidance Report 12 :cite:`EPA1993`.
Recoverable energy includes the delayed energy from all electron-related
radiations (e.g., :math:`\beta^-`, :math:`\beta^+`, Auger electrons), all gamma rays, x-rays,
annihilation radiations, and the average energy of all heavy charged
particles and delayed neutrons. The average alpha energy includes the
energy of the recoil nucleus. A part of the recoverable energy per decay
not included in the ENDF/B-VII.1 values is the additional contribution
from spontaneous fission. This energy was calculated as the product of
the spontaneous fission branching fraction and recoverable energy per
fission using a value of 200 MeV per fission and then added to the
ENDF/B-VII.1 recoverable Q energy. A value of 12.56 MeV gamma energy per
fission was used in computing the fraction of recoverable spontaneous
fission energy from gamma rays. External Bremsstrahlung radiation is
**not** included in the Q-value since the Bremsstrahlung spectrum
depends on electron interactions with the medium that contains the decay
nuclide. The energy from capture gamma rays accompanying :math:`\left( \alpha,n \right)` reactions
is not included either since it also depends on the medium.

Appendix A describes the decay resource file format. It is important to
note that the decay resource not only defines fundamental decay data,
but also the complete ORIGEN nuclide set, including the "duplicates" of
nuclides across sublibraries. For example, a version of :sup:`155`\ Gd
is contained in both the light nuclide/activation product and fission
product sublibraries. Appendix D includes the full list of the nuclides
on the ORIGEN decay library "end7dec" created by COUPLE based on the
current decay resource, including duplicates. Appendix E contains a list
of the fundamental decay data only, without duplicates. To consider a
different set of nuclides in an ORIGEN calculation, the current process
is to alter the decay resource and then regenerate the "end7dec" decay
library with COUPLE. By default, all subsequent libraries created from
COUPLE using problem-dependent reaction transitions are based on the
"end7dec" decay library and will therefore include the modified nuclide
set.

.. _5-2-3:

Neutron Reaction Resource
-------------------------

The neutron cross sections defining the nuclear reaction transmutation
rates use a comprehensive collection of nuclear data evaluations
compiled from the JEFF-3.0/A neutron activation files :cite:`JEFFDOC-982`.
The JEFF-3.0/A files contain continuous energy neutron data for 774 target
nuclei, including ground and metastable excited states, and
12,617 neutron-induced reactions below 20 MeV. The JEFF-3.0/A cross
section data are developed directly from the European Activation File
(EAF‑2003) :cite:`FUS-486` formatted as standard ENDF-6 format data. JEFF-3.0/A
cross sections are stored using File 3, multiplicities on File 10, and
isomeric branching to different metastable levels using File 9.
The evaluations include many reactions that may be important for
modeling fast fission and other high-energy systems. Neutron reactions
are available for 23 reaction types, including
:math:`\left(n,n' \right)`, :math:`\left(n,2n \right)`,
:math:`\left(n,3n \right)`, :math:`\left(n,f \right)`,
:math:`\left(n,n' \alpha \right)`, :math:`\left(n,2n\alpha\right)`,
:math:`\left(n,3n\alpha \right)`, :math:`\left(n,n'p \right)`,
:math:`\left(n,n2\alpha \right)`, :math:`\left(n,n'd \right)`,
:math:`\left(n,n't \right)`, :math:`\left(n,n'{}^3 He \right)`,
:math:`\left(n,4n \right)`, :math:`\left(n,2np \right)`,
:math:`\left(n,\gamma \right)`,  :math:`\left(n,p \right)`,
:math:`\left(n,d \right)`, :math:`\left(n,t \right)`,
:math:`\left(n,{}^3\ He \right)`, :math:`\left(n,\alpha \right)`,
:math:`\left(n,2\alpha \right)`, :math:`\left(n,2p \right)`,
and :math:`\left(n,p\alpha \right)`.

The JEFF-3.0/A evaluations also include extensive compilations of
energy-dependent branching fractions that define neutron reaction
transitions to ground and metastable energy states. Energy-dependent
branching is fully implemented in the ORIGEN cross section libraries.
Implementation of the JEFF-3.0/A cross sections as ORIGEN multigroup
data was accomplished by processing and collapsing the JEFF-3.0/A
pointwise cross sections into a standard multigroup AMPX format using
ENDF data-processing modules of the AMPX :cite:`DuGr2002` cross section
processing code system. The collapse is performed using a thermal
Maxwellian–1/E–fission–1/E weighting spectrum (see
:numref:`fig-origen-collapse-flux`) to provide infinite dilution multigroup
cross sections.

.. _fig-origen-collapse-flux:
.. figure:: figs/ORIGENdata/fig1.png
  :align: center

  Pointwise flux spectrum used to generate collapsed cross section libraries.


Neutron reactions with transitions to multiple states of the daughter
product are represented using separate cross sections to the ground and
metastable states. A special reaction identifier (MT') is defined for
this implementation of metastable transitions as

.. math::
   \text{MT}' = \text{MT}*10000 + 100*\text{LP} + \text{LT}
   :label: eq-MT-special

where MT is the reaction identifier, LP is the product metastable state,
and LT is the target metastable state. Using the
:sup:`187`\ W(n,3n)\ :sup:`185`\ W cross section (MT=17) as an example,
the reaction identifier 170000 defines the partial cross section to the
ground state of :sup:`185`\ W, and 170100 defines the cross section to
metastable :sup:`185m`\ W.

Cross section data from the JEFF-3.0/A neutron activation file are first
converted to point-wise cross section data, are Doppler broadened to
900K, and then they are collapsed to different group structures. The
following group strucures are available in SCALE:

   *  238-group neutron (thermal applications),
   *  252-group neutron (thermal applications),
   *  56-group neutron (thermal applications),
   *  200-group neutron (fast applications and shielding),
   *  47-group neutron (applications using the BUGLE shielding transport
      library),
   *  49-group neutron (collapsed version of 238 groups),
   *  44-group neutron (collapsed version of 238 groups), and
   *  999-group neutron (multipurpose).

Several minor modifications were made to the JEFF-3.0/A data:

   *  The :sup:`239`\ Np radiative neutron capture cross section was
      replaced with data from ENDF/B-VII.0. Neutron capture using
      JEFF-3.0/A cross sections was significantly larger than ENDF/B-VII.0
      due to differences in the resonance cross section region. Although
      experimental resonance parameters are not available for
      :sup:`239`\ Np, comparisons of :sup:`240`\ Pu production during
      irradiation :cite:`Gump1954` obtained using the two evaluations showed that
      better agreement with the experiment was obtained using the
      ENDF/B-VII.0 evaluation.

   *  The :math:`{}^{241} Am (n,\gamma)` branching fraction to the :sup:`242`\ Am
      ground and metastable states was replaced by the evaluation from
      ENDF/B-VII.0 to yield better agreement with the results of
      destructive radiochemical assay measurements of irradiated fuels. The
      branching fraction of :sup:`241`\ Am to :sup:`242m`\ Am for thermal
      neutron capture changed from 8.2% in JEFF-3.0/A to 10.0% in
      ENDF/B-VII.0.

The cross section library header record information and a complete list
of nuclides in JEFF-3.0/A libraries developed for ORIGEN are provided in
Appendix E.

Because JEFF-3.0/A-based libraries are formatted as standard AMPX
working libraries, they can be accessed and/or manipulated using
standard AMPX utility modules in SCALE. For example, multigroup cross
sections may be listed using the PALEALE module. Additionally, the data
may be visualized using the Fulcrum user interface. Cross section plots
of the 238-group JEFF‑3.0/A library are illustrated in
:numref:`fig-origen-jeff-w187` for :math:`(n,\gamma)`, :math:`(n,\alpha)`,
(n,2n), and (n,3n) cross sections to the ground and metastable states.

Before the cross sections in ORIGEN can be used, they must be collapsed
with a user-defined multigroup flux to a one-group cross section and
added to the ORIGEN binary library (see the COUPLE input description).

.. _fig-origen-jeff-w187:
.. figure:: figs/ORIGENdata/fig2.png
  :align: center

  238-group JEFF-3.0/A cross sections for :sup:187:\ W.

.. _5-2-4:

Fission Yield Resource
----------------------

The fission-yield resource contains the energy-dependent direct yields
of each fission product for 30 fissionable actinides, including
:sup:`227,228,232`\ Th, :sup:`231`\ Pa, :sup:`232--238`\ U,
:sup:`238-242`\ Pu, :sup:`241,242m,243`\ Am, :sup:`237,238`\ Np,
:sup:`242-246,248`\ Cm, :sup:`249,252`\ Cf, and :sup:`254`\ Es.
Independent (direct) fission product yields are stored as atom percent
per fission, and except for :sup:`235`\ U(thermal), :sup:`238`\ U(fast),
and :sup:`241`\ Pu(thermal), they are obtained from ENDF/B‑VII.0 :cite:`ENDF-VII.0`
File 8 and MT=454.

Revised independent fission product yields for :sup:`235`\ U(thermal),
:sup:`238`\ U(fast), and :sup:`241`\ Pu(thermal) were adopted to address
inconsistencies between the direct and cumulative fission yields in
ENDF/B-VII.0 caused by the use of updated nuclear decay schemes in the
decay sublibrary :cite:`PiFrGa2015,FrWePi2015`. Namely, recent changes in the
decay data, particularly the delayed neutron branching fractions, result
in calculated fission product concentrations that do not agree with the
cumulative fission yields in the ENDF/B-VII.0 library. These issues were
particularly evident for the three cited isotopes because their
fissioning systems result in a preferential formation of fragments that
are sensitive to the changes in the decay data. For example, a study on
:sup:`239`\ Pu(thermal) showed negligible differences between cumulative
yields calculated (using the recent decay data sublibrary) and the
cumulative yields in ENDF/B-VII.0. Energy-dependent product yields are
available for thermal, fast, and high-energy incident neutron energies.
For fast fission, the value of the energy of incident neutron was
modified from the value of 500 keV tabulated in ENDF/B-VII.0 to more
accurately represent the relationship between the energy distribution of
the neutrons causing fission and the and the fission neutron spectrum
energy. For this implementation of the yield data, the effective
incident neutron energy for fast fission was adjusted from 500 keV to
2.0 MeV to better reflect the average fission energy of most nuclides.
The neutron energies for thermal fission (0.0253 eV) and high energy
fission (14 MeV) are unchanged.

The fission product yields also include cumulative ternary yields from
the JEF-2.2 fission yield library :cite:`JEF-2.2` for :sup:`3`\ H and
:sup:`4`\ He. The nuclide :sup:`3`\ He was also added to the fission
product library since it is a decay product of tritium.

Note that inclusion of fission yields for each actinide in an ORIGEN
library can be controlled by the user through COUPLE. Actinides not
assigned with explicit yields do not produce fission products during
fission.

.. table:: Fissionable isotopes having explicit fission yields
   :name: tab-origen-fiss-isotopes
   :align: center
   :class: longtable

   +----------------------+-------------------------------------------+
   | **Nuclide**          | **Neutron-induced fission energies**      |
   |                      | [#fiss-energy]_                           |
   +======================+======================+======+=============+
   | :sup:`227`\ Th       | Thermal              |      |             |
   +----------------------+----------------------+------+-------------+
   | :sup:`229`\ Th       | Thermal              |      |             |
   +----------------------+----------------------+------+-------------+
   | :sup:`232`\ Th       |                      | Fast | High energy |
   +----------------------+----------------------+------+-------------+
   | :sup:`231`\ Pa       |                      | Fast |             |
   +----------------------+----------------------+------+-------------+
   | :sup:`232`\ U        | Thermal              |      |             |
   +----------------------+----------------------+------+-------------+
   | :sup:`233`\ U        | Thermal              |      |             |
   +----------------------+----------------------+------+-------------+
   | :sup:`234`\ U        |                      | Fast | High energy |
   +----------------------+----------------------+------+-------------+
   | :sup:`235`\ U        | Thermal              | Fast | High energy |
   +----------------------+----------------------+------+-------------+
   | :sup:`236`\ U        |                      | Fast | High energy |
   +----------------------+----------------------+------+-------------+
   | :sup:`237`\ U        |                      | Fast |             |
   +----------------------+----------------------+------+-------------+
   | :sup:`238`\ U        |                      | Fast | High energy |
   +----------------------+----------------------+------+-------------+
   | :sup:`237`\ Np       | Thermal              | Fast | High energy |
   +----------------------+----------------------+------+-------------+
   | :sup:`238`\ Np       |                      | Fast |             |
   +----------------------+----------------------+------+-------------+
   | :sup:`238`\ Pu       |                      | Fast |             |
   +----------------------+----------------------+------+-------------+
   | :sup:`239`\ Pu       | Thermal              | Fast | High energy |
   +----------------------+----------------------+------+-------------+
   | :sup:`240`\ Pu       | Thermal              | Fast | High energy |
   +----------------------+----------------------+------+-------------+
   | :sup:`241`\ Pu       | Thermal              | Fast |             |
   +----------------------+----------------------+------+-------------+
   | :sup:`242`\ Pu       | Thermal              | Fast | High energy |
   +----------------------+----------------------+------+-------------+
   | :sup:`241`\ Am       | Thermal              | Fast | High energy |
   +----------------------+----------------------+------+-------------+
   | :sup:`242\ m`\ Am    | Thermal              |      |             |
   +----------------------+----------------------+------+-------------+
   | :sup:`243`\ Am       |                      | Fast |             |
   +----------------------+----------------------+------+-------------+
   | :sup:`242`\ Cm       |                      | Fast |             |
   +----------------------+----------------------+------+-------------+
   | :sup:`243`\ Cm       | Thermal              | Fast |             |
   +----------------------+----------------------+------+-------------+
   | :sup:`244`\ Cm       |                      | Fast |             |
   +----------------------+----------------------+------+-------------+
   | :sup:`245`\ Cm       | Thermal              |      |             |
   +----------------------+----------------------+------+-------------+
   | :sup:`246`\ Cm       |                      | Fast |             |
   +----------------------+----------------------+------+-------------+
   | :sup:`248`\ Cm       |                      | Fast |             |
   +----------------------+----------------------+------+-------------+
   | :sup:`249`\ Cf       | Thermal              |      |             |
   +----------------------+----------------------+------+-------------+
   | :sup:`251`\ Cf       | Thermal              |      |             |
   +----------------------+----------------------+------+-------------+
   | :sup:`254`\ Es       | Thermal              |      |             |
   +----------------------+----------------------+------+-------------+

.. [#fiss-energy] Neutron energy causing fission

.. _5-2-5:

Energy Resource
===============

The energy resource is a set of data defined internally to ORIGEN to
compute the total power during irradiation if the flux is known, or the
total flux if the power is known. The data include the energy
contributed by fission and capture. The recoverable energy values taken
primarily from ENDF/B evaluations are listed in
:numref:`tab-origen-recoverable-en-fc` and :numref:`tab-origen-recoverable-en-cap`.
The recoverable energy for fission and neutron capture for nuclides not listed in
the tables are assumed to be 200 MeV and 5.0 MeV, respectively.

.. table:: Recoverable energy (MeV) values for actinides
   :name: tab-origen-recoverable-en-fc
   :align: center

   =============== =========== ===========
   **Nuclide**     **Fission** **Capture**
   :sup:`230`\ Th  190.00      5.010
   :sup:`232`\ Th  189.21      4.786
   :sup:`233`\ Th  190.00      6.080
   :sup:`231`\ Pa  190.00      5.660
   :sup:`233`\ Pa  189.10      5.197
   :sup:`232`\ U   200.00      5.930
   :sup:`233`\ U   191.29      6.841
   :sup:`234`\ U   190.30      5.297
   :sup:`235`\ U   194.02      6.545
   :sup:`236`\ U   192.80      5.124
   :sup:`238`\ U   198.12      4.804
   :sup:`237`\ Np  195.10      5.490
   :sup:`239`\ Np  200.00      4.970
   :sup:`238`\ Pu  197.80      5.550
   :sup:`239`\ Pu  200.05      6.533
   :sup:`240`\ Pu  199.79      5.241
   :sup:`241`\ Pu  202.22      6.301
   :sup:`242`\ Pu  200.62      5.071
   :sup:`243`\ Pu  200.00      6.020
   :sup:`241`\ Am  202.30      5.529
   :sup:`242m`\ Am 202.29      6.426
   :sup:`243`\ Am  202.10      5.363
   :sup:`244`\ Cm  200.00      6.451
   :sup:`245`\ Cm  200.00      6.110
   =============== =========== ===========


.. table:: Recoverable energy (MeV) values for activation and fission products
   :name: tab-origen-recoverable-en-cap
   :align: center

   =============== ===========
   **Nuclide**     **Capture**
   :sup:`1`\ H     2.225
   :sup:`10`\ B    2.790
   :sup:`16`\ O    4.143
   :sup:`56`\ Fe   7.600
   :sup:`58`\ Ni   9.020
   :sup:`90`\ Zr   7.203
   :sup:`91`\ Zr   8.635
   :sup:`92`\ Zr   6.758
   :sup:`96`\ Zr   5.571
   :sup:`95`\ Mo   9.154
   :sup:`95`\ Tc   7.710
   :sup:`101`\ Ru  9.216
   :sup:`103`\ Rh  6.999
   :sup:`105`\ Rh  7.094
   :sup:`109`\ Ag  6.825
   :sup:`131`\ Xe  8.936
   :sup:`135`\ Xe  7.880
   :sup:`133`\ Cs  6.704
   :sup:`134`\ Cs  6.550
   :sup:`143`\ Nd  7.817
   :sup:`145`\ Nd  7.565
   :sup:`147`\ Pm  5.900
   :sup:`148`\ Pm  7.266
   :sup:`148m`\ Pm 7.266
   :sup:`147`\ Sm  8.140
   :sup:`149`\ Sm  7.982
   :sup:`150`\ Sm  5.596
   :sup:`151`\ Sm  8.258
   :sup:`152`\ Sm  5.867
   :sup:`153`\ Eu  6.444
   :sup:`154`\ Eu  8.167
   :sup:`155`\ Eu  6.490
   =============== ===========

.. _5-2-6:

Emission Resources
------------------

The two main groups for emission resources are the photon (gamma)
resource, which includes beta particle emission data, and the neutron
resource, which includes alpha emission data.

.. _5-2-6-1:

Gamma Emission
~~~~~~~~~~~~~~

The resources for gamma emission are stored as separate files (see
:numref:`tab-origen-photon-files`) containing the photon data associated with
different modes of decay or photon production. The photon data sets include decay
gamma and x-ray line-energy data, gamma rays accompanying spontaneous fission,
gamma rays accompanying :math:`\left( \alpha,n \right)` reactions in oxide fuels, and
Bremsstrahlung spectra from decay electrons/positrons slowing down in
UO\ :sub:`2` and water. The photon energy spectra can be generated in
any energy group structure for all activation products, actinides, and
fission product nuclides with photon yield data.

.. table:: Photon data files
   :name: tab-origen-photon-files
   :align: center

   ==============   ==================================================================
    **File name**   **Description**
   ==============   ==================================================================
    MPDKXGAM        x-ray and gamma emissions line data
    MPSFANGM        spontaneous fission and :math:`\left( \alpha,n \right)` reactions
    MPBRH2OM        bremsstrahlung from beta particles slowing down in water
    MPBRH2OP        bremsstrahlung from positrons slowing down in water
    MPBRUO2M        bremsstrahlung from beta particles slowing down in UO\ :sub:`2`
    MPBRUO2P        bremsstrahlung from positrons slowing down in UO\ :sub:`2`
   ==============   ==================================================================


All photon data sets are constructed with the same format (see Appendix
C). The majority of the photon emissions are discrete energy lines.
Photon continuum data, used to represent Bremstrahlung and some other
gamma-ray emission spectra, are stored at discrete energies and
approximately expanded to a continuum, as needed.
Gamma and x-ray yields are directly from ENDF/B-VII.1 decay files
containing spectral data for decay transitions of 1,132 nuclides. A
separate file contains emission spectra for gamma rays accompanying
spontaneous fission and for gamma rays accompanying :math:`\left( \alpha, n \right)`
reactions in oxide fuels :cite:`CrHaGr1979`. The spontaneous fission spectra
combine prompt and equilibrium fission product gamma-ray components. The prompt
spectrum is similar to that of :sup:`235`\ U, and the delayed fission product gamma
intensity at equilibrium is about 0.75 of that from the prompt fission
gamma rays. Based on measured prompt fission gamma spectra from
:sup:`235`\ U, spontaneous fission spectra are computed from the
following approximation:

.. math::
  N\left(E \right) \cong
  \begin{cases}
    11.5 & 0.1 \leq\ E \leq 0.6\ MeV \\
    35.4 e^{-1.78 E} & 0.6 \leq E < 1.5\ MeV \\
    12.6 e^{-1.09 E} & 1.5 \leq E \leq 10.5\ MeV \\
    0 & \text{otherwise.}
  \end{cases}
  :label: eq-origen-sfn-spec


where

   N(E) = number of photons per unit energy per fission (photons/MeV per
   fission) at energy E, where E is the photon energy (MeV).


For medical and industrial spontaneous fission source applications, a
more accurate simulation of the source may be desirable. Work has been
performed on :sup:`252`\ Cf source modeling to explicity represent the
fission product generation from fission and the delayed gamma emission.
In this application, the equilibrium spontaneous fission gamma spectrum
was replaced with an evaluation of the :sup:`252`\ Cf prompt gamma
spectrum, and the delayed fission product gamma rays was modeled
explicitly in ORIGEN by generating the time-dependent fission products
using :sup:`252`\ Cf spontaneous fission product yields from
ENDF/B-VII.0 :cite:`FoGaWa2011`. This was performed by adding decay transitions
to the ORIGEN library from the actinides to the fission products.
The spectrum of gamma rays accompanying :math:`\left( \alpha,n \right)`
reactions is based on reaction data for alpha interactions on :sup:`18`\ O
and from studies for :sup:`238`\ PuO\ :sub:`2` systems. The spectrum is
computed from the approximation:

.. math::
  :label: eq5-2-2

  N\left( E \right) \cong 2.13 \cdot 10^{-8}\ e^{- 1.38E}

where

   N(E) = number of photons per unit energy per alpha decay (photons/MeV
   per disintegration) at energy E (MeV).

The photon yields in this data set are continuum spectra represented by
discrete lines with an energy width of 500 keV and range from 250 keV to
10.25 MeV.

Two photon data sets contain bremsstrahlung spectra from decay electrons
and positrons slowing down in a UO\ :sub:`2` fuel matrix. The yields are
in the form of continuum spectra represented in the data sets as
discrete lines using up to 70 quasi-logarithmic spaced energy points
over the energy range between 0 and 13.5 MeV. Two libraries contain
bremsstrahlung spectra from decay electrons and positrons slowing down
in water. Bremsstrahlung spectra were calculated using a computer
program developed by Dillman *et al.* :cite:`DiSnFo1973` using beta spectra
derived from **Evaluated Nuclear Structure Data Files (**\ ENSDF) decay data
with a computer program written by Gove and Martin :cite:`GoMa1971`.

.. _5-2-6-2:

Neutron Emission
~~~~~~~~~~~~~~~~

There are four neutron emission resources used by ORIGEN to calculate
the neutron intensities and spectra: (1) neutron decay data, (2) an
\alpha-particle stopping power, (3) a target :math:`\left( \alpha,n \right)`
cross section, and (4) a target :math:`\left( \alpha,n \right)` product level
branching. All of the neutron data are stored in a text format with names and
descriptions given in :numref:`tab-origen-neutron-libs`. The neutron decay data
contain basic decay information for decay processes that lead to direct and
indirect emission of neutrons, including spontaneous fission branching
fractions, alpha decay branching fractions, delayed neutron branching fractions,
alpha-particle decay energies, Watt fission spectrum parameters, and delayed
neutron spectra. The stopping cross sections, :math:`\left( \alpha,n \right)`
target cross sections, and product-level branching data are used in calculating
the neutron yield and spectra from :math:`\left( \alpha,n \right)` reactions.

The neutron data were obtained directly from the updated SOURCES-4B code
package. The sources of the neutron data are described by Shores :cite:`Shores2000`.
An update was made to correct an error in the :sup:`250`\ Cf spontaneous fission
neutron branching fraction in the neutron source decay data distributed with the
SOURCES code. The :sup:`250`\ Cf branching fraction was incorrectly assigned the
value from :sup:`252`\ Cf of :math:`3.092 \cdot 10^{-2}`. A corrected value of
:math:`7.700 \cdot 10^{-4}` from ENDF/B‑VII.1 is used.

.. table:: Neutron source data libraries
   :name: tab-origen-neutron-libs
   :align: center

   ============= ====================================================================
   **File name** **Description**
   ALPHDEC          Neutron source decay data
   STCOEFF          Stopping cross section expansion coefficients
   ALPHYLD          Target :math:`\left( \alpha,n \right)` product level branching
   ALPHAXS          Target :math:`\left( \alpha,n \right)` cross section
   ============= ====================================================================

The neutron source decay contains spontaneous fission data for the
49 actinides listed in :numref:`origen-nucl-sfn`. These data include the
spontaneous fission branching fraction, the number of neutrons per fission
(:math:`nu`), and the watt spectrum parameters for spontaneous fission. The
spontaneous fission neutron energy spectrum is approximated using spectral
parameters A and B, such that

.. math::
    N\left( E \right) \cong \text{C\ }e^{ - \frac{E}{A}}\sinh \sqrt{\text{BE}}
    :label: eq-watt-spec


where *E* is the neutron energy and *C* is a normalization constant.


.. table:: Nuclides with spontaneous fission data and spectral parameters
   :name: origen-nucl-sfn
   :align: center

   ================  ================  ================  ================  ================
    :sup:`230`\ Th   :sup:`239`\ U     :sup:`240`\ Pu    :sup:`244`\ Am    :sup:`250`\ Cm
    :sup:`232`\ Th   :sup:`236`\ Np    :sup:`241`\ Pu    :sup:`244m`\ Am   :sup:`249`\ Bk
    :sup:`231`\ Pa   :sup:`236m`\ Np   :sup:`242`\ Pu    :sup:`240`\ Cm    :sup:`248`\ Cf
    :sup:`232`\ U    :sup:`237`\ Np    :sup:`243`\ Pu    :sup:`241`\ Cm    :sup:`250`\ Cf
    :sup:`233`\ U    :sup:`238`\ Np    :sup:`244`\ Pu    :sup:`242`\ Cm    :sup:`252`\ Cf
    :sup:`234`\ U    :sup:`239`\ Np    :sup:`240`\ Am    :sup:`243`\ Cm    :sup:`254`\ Cf
    :sup:`235`\ U    :sup:`236`\ Pu    :sup:`241`\ Am    :sup:`244`\ Cm    :sup:`253`\ Es
    :sup:`236`\ U    :sup:`237`\ Pu    :sup:`242`\ Am    :sup:`245`\ Cm    :sup:`254m`\ Es
    :sup:`237`\ U    :sup:`238`\ Pu    :sup:`242m`\ Am   :sup:`246`\ Cm    :sup:`255`\ Es
    :sup:`238`\ U    :sup:`239`\ Pu    :sup:`243`\ Am    :sup:`248`\ Cm
   ================  ================  ================  ================  ================


Delayed neutron branching fractions and neutron spectra for 105 fission
products are listed in :numref:`tab-origen-nucl-dn`. The delayed neutron
spectra are tabulated in discrete 10 keV bins from 50 keV to about 2 MeV.


.. table:: Nuclides with delayed neutron emission spectral data
   :name: tab-origen-nucl-dn
   :align: center

   ==============   ==============   ===============   ===============   ===============
    :sup:`79`\ Zn   :sup:`89`\ Br    :sup:`97`\ Y      :sup:`128`\ In    :sup:`41`\ I
    :sup:`79`\ Ga   :sup:`90`\ Br    :sup:`97m`\ Y     :sup:`129`\ In    :sup:`42`\ I
    :sup:`80`\ Ga   :sup:`91`\ Br    :sup:`98`\ Y      :sup:`129m`\ In   :sup:`43`\ I
    :sup:`81`\ Ga   :sup:`92`\ Br    :sup:`98m`\ Y     :sup:`130`\ In    :sup:`141`\ Xe
    :sup:`82`\ Ga   :sup:`93`\ Br    :sup:`99`\ Y      :sup:`131`\ In    :sup:`142`\ Xe
    :sup:`83`\ Ga   :sup:`92`\ Kr    :sup:`100`\ Y     :sup:`132`\ In    :sup:`143`\ Xe
    :sup:`83`\ Ge   :sup:`93`\ Kr    :sup:`104`\ Zr    :sup:`133`\ Sn    :sup:`144`\ Xe
    :sup:`84`\ Ge   :sup:`94`\ Kr    :sup:`105`\ Zr    :sup:`134`\ Sn    :sup:`141`\ Cs
    :sup:`85`\ Ge   :sup:`95`\ Kr    :sup:`103`\ Nb    :sup:`135`\ Sn    :sup:`142`\ Cs
    :sup:`86`\ Ge   :sup:`92`\ Rb    :sup:`104`\ Nb    :sup:`134m`\ Sb   :sup:`143`\ Cs
    :sup:`84`\ As   :sup:`93`\ Rb    :sup:`105`\ Nb    :sup:`135`\ Sb    :sup:`144`\ Cs
    :sup:`85`\ As   :sup:`94`\ Rb    :sup:`106`\ Nb    :sup:`136`\ Sb    :sup:`145`\ Cs
    :sup:`86`\ As   :sup:`95`\ Rb    :sup:`109`\ Mo    :sup:`137`\ Sb    :sup:`146`\ Cs
    :sup:`87`\ As   :sup:`96`\ Rb    :sup:`110`\ Mo    :sup:`136`\ Te    :sup:`147`\ Cs
    :sup:`87`\ Se   :sup:`97`\ Rb    :sup:`109`\ Tc    :sup:`137`\ Te    :sup:`147`\ Ba
    :sup:`88`\ Se   :sup:`98`\ Rb    :sup:`110`\ Tc    :sup:`138`\ Te    :sup:`148`\ Ba
    :sup:`89`\ Se   :sup:`99`\ Rb    :sup:`122`\ Ag    :sup:`139`\ Te    :sup:`149`\ Ba
    :sup:`90`\ Se   :sup:`97`\ Sr    :sup:`123`\ Ag    :sup:`137`\ I     :sup:`150`\ Ba
    :sup:`91`\ Se   :sup:`98`\ Sr    :sup:`128`\ Cd    :sup:`138`\ I     :sup:`147`\ La
    :sup:`87`\ Br   :sup:`99`\ Sr    :sup:`127`\ In    :sup:`139`\ I     :sup:`149`\ La
    :sup:`88`\ Br   :sup:`100`\ Sr   :sup:`127m`\ In   :sup:`140`\ I     :sup:`150`\ La
   ==============   ==============   ===============   ===============   ===============


Neutron yields from \alpha-particle interaction are available for 19 :math:`\left( \alpha,n \right)`
target nuclides: :sup:`7`\ Li, :sup:`9`\ Be, :sup:`10`\ B, :sup:`11`\ B,
:sup:`13`\ C, :sup:`14`\ N, :sup:`17`\ O, :sup:`18`\ O, :sup:`19`\ F,
:sup:`21`\ Ne, :sup:`22`\ Ne, :sup:`23`\ Na, :sup:`25`\ Mg,
:sup:`26`\ Mg, :sup:`27`\ Al, :sup:`29`\ Si, :sup:`30`\ Si,
:sup:`31`\ P, and :sup:`37`\ Cl. The neutron decay data contain discrete
alpha-particle energies and branching fractions for 89 actinides and
7 fission products listed in :numref:`tab-origen-nucl-alpha`. The sources of
the level branching fraction data and the :math:`\left( \alpha,n \right)`
cross section data are listed in :numref:`tab-origen-an-cxs`. The stopping
cross sections  and :math:`\left( \alpha,n \right)` target cross section
and product level branching libraries are used in calculating the neutron yield
and spectra from Ziegler :cite:`Zieg1977` for all elements with Z < 93, and
from Wilson :cite:`WPS1983` for all elements \geq 93.


.. table:: Nuclides with :math:`\alpha`-particle emission data for neutron yield calculations
   :name: tab-origen-nucl-alpha
   :align: center

   ================ ================ ================ ================= =================
    :sup:`142`\ Ce   :sup:`216`\ Po   :sup:`226`\ Ac   :sup:`237`\ Np    :sup:`245`\ Cm
    :sup:`144`\ Nd   :sup:`218`\ Po   :sup:`227`\ Ac   :sup:`235`\ Pu    :sup:`246`\ Cm
    :sup:`146`\ Sm   :sup:`215`\ At   :sup:`226`\ Th   :sup:`236`\ Pu    :sup:`247`\ Cm
    :sup:`147`\ Sm   :sup:`217`\ At   :sup:`227`\ Th   :sup:`237`\ Pu    :sup:`248`\ Cm
    :sup:`148`\ Sm   :sup:`218`\ At   :sup:`228`\ Th   :sup:`238`\ Pu    :sup:`249`\ Bk
    :sup:`149`\ Sm   :sup:`219`\ At   :sup:`229`\ Th   :sup:`239`\ Pu    :sup:`248`\ Cf
    :sup:`152`\ Gd   :sup:`217`\ Rn   :sup:`230`\ Th   :sup:`240`\ Pu    :sup:`249`\ Cf
    :sup:`210`\ Pb   :sup:`218`\ Rn   :sup:`232`\ Th   :sup:`241`\ Pu    :sup:`250`\ Cf
    :sup:`210`\ Bi   :sup:`219`\ Rn   :sup:`230`\ Pa   :sup:`242`\ Pu    :sup:`251`\ Cf
    :sup:`211`\ Bi   :sup:`220`\ Rn   :sup:`231`\ Pa   :sup:`244`\ Pu    :sup:`252`\ Cf
    :sup:`212`\ Bi   :sup:`222`\ Rn   :sup:`230`\ U    :sup:`240`\ Am    :sup:`253`\ Cf
    :sup:`213`\ Bi   :sup:`221`\ Fr   :sup:`231`\ U    :sup:`241`\ Am    :sup:`254`\ Cf
    :sup:`214`\ Bi   :sup:`222`\ Fr   :sup:`232`\ U    :sup:`242m`\ Am   :sup:`253`\ Es
    :sup:`210`\ Po   :sup:`223`\ Fr   :sup:`233`\ U    :sup:`243`\ Am    :sup:`254`\ Es
    :sup:`211`\ Po   :sup:`222`\ Ra   :sup:`234`\ U    :sup:`240`\ Cm    :sup:`254m`\ Es
    :sup:`212`\ Po   :sup:`223`\ Ra   :sup:`235`\ U    :sup:`241`\ Cm    :sup:`255`\ Es
    :sup:`213`\ Po   :sup:`224`\ Ra   :sup:`236`\ U    :sup:`242`\ Cm    :sup:`254`\ Fm
    :sup:`214`\ Po   :sup:`226`\ Ra   :sup:`238`\ U    :sup:`243`\ Cm    :sup:`255`\ Fm
    :sup:`215`\ Po   :sup:`225`\ Ac   :sup:`235`\ Np   :sup:`244`\ Cm    :sup:`256`\ Fm
    |nbsp|           |nbsp|           |nbsp|           |nbsp|            :sup:`257`\ Fm
   ================ ================ ================ ================= =================


.. table:: Target :math:`(\alpha,n)` cross section and branching level isotopes and sources
   :name: tab-origen-an-cxs
   :align: center
   :class: longtable

   +------------------+----------+--------------------------+------------------------+
   | **Isotope**      | **ZAID** | **Level branching**      | **Cross section data** |
   |                  |          | **fraction source data** |                        |
   +==================+==========+==========================+========================+
   | :sup:`7`\ Li     | 30070    | GNASH                    | Gibbons and Macklin    |
   |                  |          |                          | :cite:`GiMa1959`       |
   +------------------+----------+--------------------------+------------------------+
   | :sup:`9`\ Be     | 40090    | Geiger and Van der       | Geiger and Van der     |
   |                  |          | Zwain :cite:`GeZw1975`   | Zwain :cite:`GeZw1975` |
   +------------------+----------+--------------------------+------------------------+
   | :sup:`10`\ B     | 50010    | GNASH                    | Bair *et al.*          |
   |                  |          |                          | :cite:`BaCa1979`       |
   +------------------+----------+--------------------------+------------------------+
   | :sup:`11`\ B     | 50110    | GNASH                    | Bair *et al.*          |
   |                  |          |                          | :cite:`BaCa1979`       |
   +------------------+----------+--------------------------+------------------------+
   | :sup:`13`\ C     | 60130    | GNASH\ *a*               | Bair and Haas          |
   |                  |          |                          | :cite:`BaHa1973`       |
   +------------------+----------+--------------------------+------------------------+
   | :sup:`14`\ N     | 70140    | N/A                      | GNASH                  |
   +------------------+----------+--------------------------+------------------------+
   | :sup:`17`\ O     | 80170    | Lessor and Schenter      | Perry and Wilson       |
   |                  |          | :cite:`LeSc1971`         | :cite:`PeWi1981`       |
   +------------------+----------+--------------------------+------------------------+
   | :sup:`18`\ O     | 80180    | Lesser and Schenter      | Perry and Wilson       |
   |                  |          | :cite:`LeSc1971`         | :cite:`PeWi1981`       |
   +------------------+----------+--------------------------+------------------------+
   | :sup:`19`\ F     | 90190    | Lesser and Schenter      | Balakrishnan *et al.*  |
   |                  |          | :cite:`LeSc1971`         | :cite:`BaKaMe1978`     |
   +------------------+----------+--------------------------+------------------------+
   | :sup:`21`\ Ne    | 100210   | N/A                      | GNASH                  |
   +------------------+----------+--------------------------+------------------------+
   | :sup:`22`\ Ne    | 100220   | N/A                      | GNASH                  |
   +------------------+----------+--------------------------+------------------------+
   | :sup:`23`\ Na    | 110230   | GNASH                    | GNASH\ *a*             |
   +------------------+----------+--------------------------+------------------------+
   | :sup:`25`\ Mg    | 120250   | GNASH                    | GNASH                  |
   +------------------+----------+--------------------------+------------------------+
   | :sup:`26`\ Mg    | 120260   | GNASH                    | GNASH                  |
   +------------------+----------+--------------------------+------------------------+
   | :sup:`27`\ Al    | 130270   | GNASH                    | GNASH\ *a*             |
   +------------------+----------+--------------------------+------------------------+
   | :sup:`29`\ Si    | 140290   | GNASH                    | GNASH\ *a*             |
   +------------------+----------+--------------------------+------------------------+
   | :sup:`30`\ Si    | 140300   | GNASH                    | GNASH\ *a*             |
   +------------------+----------+--------------------------+------------------------+
   | :sup:`31`\ P     | 150310   | GNASH                    | GNASH                  |
   +------------------+----------+--------------------------+------------------------+
   | :sup:`37`\ Cl    | 170370   | GNASH                    | Woosley et. al.        |
   |                  |          |                          | :cite:`WoFoHoZi1975`   |
   +------------------+----------+--------------------------+------------------------+

.. [#gnash] GNASH-calculated data and measured data are available for these
            nuclides in the library. By default, the GNASH values are
            used. To use the measured data, the user must reverse the
            order of th GNASH and measured data in the library since the code
            uses the first set encountered in the library (GNASH set).

.. _5-2-6-3:

Beta Emission
~~~~~~~~~~~~~

Beta emission rates and energy spectra are calculated using an
analytic expression for the kinetic energy of the emitted
:math:`\beta^-` particles :cite:`GoMa1971`:

  .. math::
     N\left( Z,W \right) = \frac{g^{2}}{{2\pi}^{3}}
     F\left( Z,W \right) \rho W \left( W_{0}- W \right)^{2}S_{n}\left( W \right) dW

where

   :math:`Z =` atomic number of the daugher nucleus

   :math:`g =` weak interaction coupling constant

   :math:`W =` kinetic energy of beta particle (in :math:`m_{e}c^{2}` units)

   :math:`F\left( Z,W \right) =` Fermi function

   :math:`W_{0} =` endpoint beta energy

   :math:`\rho = \sqrt{W^{2} - 1}` = electron momentum

   :math:`S_{n}\left( W \right) =` spectral shape factor based on transition type

   :math:`n =` classification of the transition type


**Internal conversion electron emission is not considered.**

The calculation requires nuclear data on the fraction of the beta
transition to each exicited state of the daughter nucleus, the maximum
endpoint energy of the transition (W\ 0), and a classification of the
beta transition (n) defined by the spin and parity change of the
transition which defines the spectral shape factor. The transition
classification uses n\ =0 for allowed and forbidden non-unique
transitions, n\ =1 for first forbidden unique transitions, n\ =2 for
second forbidden unique transitions, and n\ =3 for third forbidden
unique transitions. These data are not stored in the decay data resource
but are included in a separate beta decay resource used only for the
beta calculation.

The beta decay data are stored in the formatted file
origen.rev00.ensdf95beta.data. The data are derived from ENSDF as
compiled in 1995. The file includes beta decay information for 715 beta
decay nuclides and has 8486 beta transition branches.

.. _5-2-6-4:

Alpha Emission
--------------

Calculation of the alpha emission intensity and spectrum requires
detailed information that is not available on the decay resource. The
calculation requires the alpha particle energy and branching fraction
for each transition branch. Unlike the beta spectrum, the alpha
particles are emitted with discrete energies, and the source spectrum
may be generated by straightforward binning into the user-defined group
structure. Alpha particle emission data are also used in the
:math:`\left( \alpha,n \right)` neutron source calculation.
Therefore, the alpha emission spectra are calculated using the same
alpha decay library in the neutron emission resource: ``origen.rev01.alphdec.data``.

.. _tab5-2-9:
.. list-table:: Nuclides with :math:`\alpha`-particle emission data for neutron yield calculations.
  :align: center

  * - .. image:: figs/ORIGENdata/tab9.svg
        :width: 800

.. _tab5-2-10:
.. list-table:: Target (:math:`\alpha`,n) cross section and branching level isotopes and sources.
  :align: center

  * - .. image:: figs/ORIGENdata/tab10.svg
        :width: 800

.. _5-2a:

Decay Resource Format
=====================

The decay resource is a simple text format file that can be processed by
COUPLE to create a binary decay-only library that can be used directly
by ORIGEN. In general, this is not necessary, as the decay resource
distributed with SCALE has already been processed with COUPLE to produce
the end7dec ORIGEN decay-only binary library file. Modifying the decay
data or the set of nuclides ORIGEN tracks requires modification of the
decay resource file. The format is described in
:numref:`tab-origen-decay-resource`. Note that as of the SCALE 6.2 release,
ORIGEN now uses the SCALE Standard Composition resource for abundance data
and the "ABUND" field shown below is ignored by COUPLE when reading the decay
resource.

.. table:: Definitions of data in the decay resource
   :name: tab-origen-decay-resource
   :align: center

   +---------------+-----------------------------------------------------+
   | **Data name** | **Definition**                                      |
   +---------------+-----------------------------------------------------+
   | LIB           | Nuclide sublib (used by COUPLE)                     |
   +---------------+-----------------------------------------------------+
   | NUC1          | Nuclide identifier                                  |
   +---------------+-----------------------------------------------------+
   | IU            | Units for the half life value                       |
   |               | (see numref:`tab-origen-hl-units`)                  |
   +---------------+-----------------------------------------------------+
   | HALFL         | Value of the half life in IU units                  |
   +---------------+-----------------------------------------------------+
   | FB1           | Beta decay transition leading to a daughter in the  |
   |               | metastable state                                    |
   +---------------+-----------------------------------------------------+
   | FP            | Positron emission decay fraction or orbital         |
   |               | electron capture to the ground state                |
   +---------------+-----------------------------------------------------+
   | FP1           | Positron emission decay fraction or orbital         |
   |               | electron capture to a metastable state              |
   +---------------+-----------------------------------------------------+
   | FA            | Alpha particle emission decay fraction              |
   +---------------+-----------------------------------------------------+
   | FT            | Isomeric transition decay fraction                  |
   +---------------+-----------------------------------------------------+
   | LIB1          | Nuclide type in the library                         |
   +---------------+-----------------------------------------------------+
   | FSF           | Spontaneous fission decay fraction                  |
   +---------------+-----------------------------------------------------+
   | FBN           | Delayed neutron decay (beta particle and a neutron) |
   |               | fraction                                            |
   +---------------+-----------------------------------------------------+
   | Q             | Recoverable energy per decay (MeV)                  |
   +---------------+-----------------------------------------------------+
   | ABUND         | Natural atom isotopic abundance in percent          |
   |               | (**no longer used**)                                |
   +---------------+-----------------------------------------------------+
   | AMPC          | Maximum permissible concentration in air            |
   +---------------+-----------------------------------------------------+
   | WMPC          | Maximum permissible concentration in water          |
   +---------------+-----------------------------------------------------+
   | LIB1          | Nuclide type in the library (used by COUPLE)        |
   +---------------+-----------------------------------------------------+
   | FG            | Fraction of recoverable decay energy Q associated   |
   |               | with gamma rays                                     |
   +---------------+-----------------------------------------------------+
   | FB            | Beta decay transition leading to a daughter in the  |
   |               | ground state                                        |
   +---------------+-----------------------------------------------------+
   | FBB           | Double beta decay fraction                          |
   +---------------+-----------------------------------------------------+
   | FN            | Neutron decay fraction                              |
   +---------------+-----------------------------------------------------+
   | FBA           | Beta decay plus an alpha particle emission decay    |
   |               | fraction                                            |
   +---------------+-----------------------------------------------------+

The variable ``LIB`` (and ``LIB1``)defines the nuclide sublibrary
(1/2/3=activation product/actinide/fission product). Variable ``LIB1`` is
included for formatting purposes only.

The nuclide identifier is read in variable ``NUC1`` and is subsequently
stored in array ``NUCL``. The nuclide identifier is given by

.. math::
   \text{NUCL} = \text{Z} * 10000 + \text{A} * 10 + \text{I}
   :label: eq-origen-nuc-id


where Z is the atomic number, A is the atomic mass number, and I is the
isomeric state, where :math:`I=0` designates a ground state, and :math:`I=1`
is the first metastable state.

The variable ``HALFL`` is the physical half-life in units designated by the
variable IU, as shown in :numref:`tab-origen-hl-units`. The definitions of 11
variables representing the different decay mode branching fractions are given in
:numref:`tab-origen-decay-resource`. The decay branching fractions are used in
constructing the transition matrix.


.. table:: Units of half-life indicated by the variable IU
   :name: tab-origen-hl-units
   :align: center

   ====== ======================
   **IU** **Units of half-life**
   1      seconds
   2      minutes
   3      hours
   4      days
   5      years
   6      stable
   7      10\ :sup:`3` years
   8      10\ :sup:`6` years
   9      10\ :sup:`9` years
   ====== ======================

The variable Q is the total amount of recoverable energy (MeV) per
disintegration released by radioactive decay used for decay heat
calculations. It does not include the energy of neutrinos emitted during
beta decay transitions. The variable FG is the fraction of recoverable
energy per disintegration that comes from gamma rays and x-rays.
The value of Q is obtained directly from ENDF/B-VII.1 as the sum of the
average beta, gamma, and alpha decay energy values. The quantity
includes the energy from all electron- related radiations such as :math:`\beta^-`,
:math:`\beta^+`, Auger electrons, etc., all gamma rays, x-rays, and annihilation
radiations, and the average energy of all heavy charged particles and
delayed neutrons. The contribution from alpha decay energy includes the
energy of the recoil nucleus. A part of the recoverable energy per decay
not included in the ENDF/B-VII.1 values is the additional contribution
from spontaneous fission. This energy was calculated as the product of
the spontaneous fission branching fraction and recoverable energy per
fission using a value of 200 MeV per fission and added to the
ENDF/B-VII.1 recoverable Q energy. A value of 12.56 MeV gamma energy per
fission was used in computing the fraction of recoverable spontaneous
fission energy from gamma rays.

External bremsstrahlung radiation is **not** included in the values of
FG since the bremsstrahlung spectrum depends on electron interactions
with the medium that contains the decay nuclide. The energy from capture
gamma rays accompanying :math:`\left( \alpha,n \right)` reactions is also not included since it
also depends on the medium. The variable ABUND is the atom percent
abundance of naturally occurring isotopes.

An example of the decay resource content for selected fission products is
presented as :numref:`ex-dec-res-fp`.

.. literalinclude:: figs/ORIGENdata/dec-fp.txt
  :caption: Example of the ENDF/B-VII.1 decay data resource entries for selected fission products.
  :name: ex-dec-res-fp
  :language: none

.. _5-2b:

Fission Yield Resource Format
=============================

The independent fission product yields are stored as a formatted text
file. The header record for each set of fission product yields includes
the fissionable nuclide ID and an unused entry (0.0), followed by the
number of incident neutron energies included for this nuclide. The
fission yields for each energy are preceeded by a single record
containing the incident neutron energy (eV), an unused entry (0.0), an
index for the incident energy, the number of data entries per fission
product, the total number of entries for each incident energy, and the
number of fission products. The fission product yields for each
fissionable nuclide and incident neutron energy are then listed as pairs
of entries for the fission product nuclide ID and the independent
(direct) fission yield as atom percent per fission. An example of the
format is shown below in :numref:`ex-origen-fy-th227` for :sup:`227`\ Th.

The number and order of the fission product yields must be the same for
all fissionable nuclides and must correspond to the fission products in
the nuclear decay data. The fission product yields for each fissionable
nuclide, excluding the yields for the terniary fission products
:sup:`3`\ H, :sup:`3`\ He, and :sup:`4`\ He, sum to 200.

The fissionable nuclides and the tabulated incident neutron energies for
which yields are available are listed in :numref:`tab-origen-fiss-isotopes`.


.. literalinclude:: figs/ORIGENdata/fy-th227.txt
   :caption: Fission yield format example showing a portion of :sup:`227`\ Th.
   :name: ex-origen-fy-th227
   :language: none

.. _5-2c:

Gamma Resource Format
=====================

An example of the photon data entries for the emissions from
:sup:`140`\ La decay is shown below in :numref:`ex-origen-dec-la140`. The header
record for each nuclide contains the nuclide ID, the total number of emission
lines in the evaluation, as well as the number of discrete x-ray lines,
discrete gamma lines, and number of pseudo lines used to represent
continuum data if present in an evaluation used to reconstruct
continuous energy emission spectra from the discrete representation. The
last entries in the header record include the total gamma energy (MeV),
and the character nuclide name. The emission spectrum is listed using
pairs of entries for the photon energy (MeV) and photon emission
(photons per disintegration).

.. literalinclude:: figs/ORIGENdata/gam-la140.txt
   :caption: Gamma resource format example showing :sup:`140`\ La decay photon
             emission.
   :name: ex-origen-dec-la140
   :language: none

.. _5-2d:

ORIGEN "end7dec" Nuclide Set
============================

:numref:`tab-origen-end7dec-nucs` shows a list of the 2,237 nuclides on the
origen.rev04.end7dec ORIGEN binary decay-only library, and because this
library provides the basis for all other libraries, effectively the set
of nuclides tracked by ORIGEN in any decay or irradiation calculation.
The "index" column is the index of that nuclide in the set (internally
every ORIGEN isotopics vector has this order), the "sublib" column is
the sublibrary (LT=light nuclide, AC=actinide, FP=fission product) in
which the nuclide resides, the "nuclide" column is the nuclide
identifier, the "mass" column is the mass of the nuclide in grams per
mole, the "abundance" column is the natural abundance in atom percent
for the nuclide (note only light nuclides have abundances), and the
"decay" column is the decay constant. Note that the mass and abundance
data are embedded on the library with the values from the current SCALE
Standard Composition Library.

.. table:: Nuclide listing for "end7dec" ORIGEN library
   :name: tab-origen-end7dec-nucs
   :class: longtable

   ========= ========== =========== ========= =========== =========
   **index** **sublib** **nuclide** **mass (\ **abundance **decay**
				                            g/mol)**  (atom%)**
							                                            **(1/s)**
   ========= ========== =========== ========= =========== =========
   1         LT         1-H-1       1.0078    1.00E+02    0.00E+00
   2         LT         1-H-2       2.0141    1.15E-02    0.00E+00
   3         LT         1-H-3       3.0161    0.00E+00    1.78E-09
   4         LT         2-He-3      3.0160    1.00E-04    0.00E+00
   5         LT         2-He-4      4.0026    1.00E+02    0.00E+00
   6         LT         2-He-5      5.0122    0.00E+00    6.93E+02
   7         LT         2-He-6      6.0189    0.00E+00    8.59E-01
   8         LT         3-Li-6      6.0151    7.59E+00    0.00E+00
   9         LT         3-Li-7      7.0160    9.24E+01    0.00E+00
   10        LT         3-Li-8      8.0225    0.00E+00    8.27E-01
   11        LT         4-Be-7      7.0169    0.00E+00    1.51E-07
   12        LT         4-Be-8      8.0053    0.00E+00    6.93E+02
   13        LT         4-Be-9      9.0122    1.00E+02    0.00E+00
   14        LT         4-Be-10     10.0135   0.00E+00    1.45E-14
   15        LT         4-Be-11     11.0217   0.00E+00    5.02E-02
   16        LT         5-B-10      10.0129   1.99E+01    0.00E+00
   17        LT         5-B-11      11.0093   8.01E+01    0.00E+00
   18        LT         5-B-12      12.0143   0.00E+00    3.43E+01
   19        LT         6-C-12      12.0000   9.89E+01    0.00E+00
   20        LT         6-C-13      13.0034   1.07E+00    0.00E+00
   21        LT         6-C-14      14.0032   0.00E+00    3.85E-12
   22        LT         6-C-15      15.0106   0.00E+00    2.83E-01
   23        LT         7-N-13      13.0057   0.00E+00    1.16E-03
   24        LT         7-N-14      14.0031   9.96E+01    0.00E+00
   25        LT         7-N-15      15.0001   3.64E-01    0.00E+00
   26        LT         7-N-16      16.0061   0.00E+00    9.72E-02
   27        LT         8-O-16      15.9949   9.98E+01    0.00E+00
   28        LT         8-O-17      16.9991   3.80E-02    0.00E+00
   29        LT         8-O-18      17.9992   2.05E-01    0.00E+00
   30        LT         8-O-19      19.0036   0.00E+00    2.58E-02
   31        LT         9-F-19      18.9984   1.00E+02    0.00E+00
   32        LT         9-F-20      20.0000   0.00E+00    6.21E-02
   33        LT         10-Ne-20    19.9924   9.05E+01    0.00E+00
   34        LT         10-Ne-21    20.9939   2.70E-01    0.00E+00
   35        LT         10-Ne-22    21.9914   9.25E+00    0.00E+00
   36        LT         10-Ne-23    22.9945   0.00E+00    1.86E-02
   37        LT         11-Na-22    21.9944   0.00E+00    8.44E-09
   38        LT         11-Na-23    22.9898   1.00E+02    0.00E+00
   39        LT         11-Na-24    23.9910   0.00E+00    1.28E-05
   40        LT         11-Na-24m   23.9910   0.00E+00    3.43E+01
   41        LT         11-Na-25    24.9900   0.00E+00    1.17E-02
   42        LT         12-Mg-24    23.9850   7.90E+01    0.00E+00
   43        LT         12-Mg-25    24.9858   1.00E+01    0.00E+00
   44        LT         12-Mg-26    25.9826   1.10E+01    0.00E+00
   45        LT         12-Mg-27    26.9843   0.00E+00    1.22E-03
   46        LT         12-Mg-28    27.9839   0.00E+00    9.21E-06
   47        LT         13-Al-26    25.9869   0.00E+00    3.06E-14
   48        LT         13-Al-27    26.9815   1.00E+02    0.00E+00
   49        LT         13-Al-28    27.9819   0.00E+00    5.15E-03
   50        LT         13-Al-29    28.9804   0.00E+00    1.76E-03
   51        LT         13-Al-30    29.9830   0.00E+00    1.91E-01
   52        LT         14-Si-28    27.9769   9.22E+01    0.00E+00
   53        LT         14-Si-29    28.9765   4.69E+00    0.00E+00
   54        LT         14-Si-30    29.9738   3.09E+00    0.00E+00
   55        LT         14-Si-31    30.9754   0.00E+00    7.34E-05
   56        LT         14-Si-32    31.9741   0.00E+00    1.44E-10
   57        LT         15-P-31     30.9738   1.00E+02    0.00E+00
   58        LT         15-P-32     31.9739   0.00E+00    5.62E-07
   59        LT         15-P-33     32.9717   0.00E+00    3.17E-07
   60        LT         15-P-34     33.9736   0.00E+00    5.58E-02
   61        LT         16-S-32     31.9721   9.50E+01    0.00E+00
   62        LT         16-S-33     32.9715   7.50E-01    0.00E+00
   63        LT         16-S-34     33.9679   4.25E+00    0.00E+00
   64        LT         16-S-35     34.9690   0.00E+00    9.17E-08
   65        LT         16-S-36     35.9671   1.00E-02    0.00E+00
   66        LT         16-S-37     36.9711   0.00E+00    2.29E-03
   67        LT         17-Cl-35    34.9688   7.58E+01    0.00E+00
   68        LT         17-Cl-36    35.9683   0.00E+00    7.30E-14
   69        LT         17-Cl-37    36.9659   2.42E+01    0.00E+00
   70        LT         17-Cl-38    37.9680   0.00E+00    3.10E-04
   71        LT         17-Cl-38m   37.9680   0.00E+00    9.69E-01
   72        LT         18-Ar-36    35.9675   3.37E-01    0.00E+00
   73        LT         18-Ar-37    36.9668   0.00E+00    2.29E-07
   74        LT         18-Ar-38    37.9627   6.32E-02    0.00E+00
   75        LT         18-Ar-39    38.9643   0.00E+00    8.17E-11
   76        LT         18-Ar-40    39.9624   9.96E+01    0.00E+00
   77        LT         18-Ar-41    40.9645   0.00E+00    1.05E-04
   78        LT         18-Ar-42    41.9631   0.00E+00    6.68E-10
   79        LT         19-K-39     38.9637   9.33E+01    0.00E+00
   80        LT         19-K-40     39.9640   1.17E-02    1.76E-17
   81        LT         19-K-41     40.9618   6.73E+00    0.00E+00
   82        LT         19-K-42     41.9624   0.00E+00    1.56E-05
   83        LT         19-K-43     42.9607   0.00E+00    8.63E-06
   84        LT         19-K-44     43.9616   0.00E+00    5.22E-04
   85        LT         20-Ca-40    39.9626   9.69E+01    0.00E+00
   86        LT         20-Ca-41    40.9623   0.00E+00    2.15E-13
   87        LT         20-Ca-42    41.9586   6.47E-01    0.00E+00
   88        LT         20-Ca-43    42.9588   1.35E-01    0.00E+00
   89        LT         20-Ca-44    43.9555   2.09E+00    0.00E+00
   90        LT         20-Ca-45    44.9562   0.00E+00    4.93E-08
   91        LT         20-Ca-46    45.9537   4.00E-03    0.00E+00
   92        LT         20-Ca-47    46.9546   0.00E+00    1.77E-06
   93        LT         20-Ca-48    47.9525   1.87E-01    9.55E-28
   94        LT         20-Ca-49    48.9557   0.00E+00    1.33E-03
   95        LT         21-Sc-44    43.9594   0.00E+00    4.85E-05
   96        LT         21-Sc-44m   43.9594   0.00E+00    3.29E-06
   97        LT         21-Sc-45    44.9559   1.00E+02    0.00E+00
   98        LT         21-Sc-45m   44.9559   0.00E+00    2.18E+00
   99        LT         21-Sc-46    45.9552   0.00E+00    9.57E-08
   100       LT         21-Sc-46m   45.9552   0.00E+00    3.70E-02
   101       LT         21-Sc-47    46.9524   0.00E+00    2.40E-06
   102       LT         21-Sc-48    47.9522   0.00E+00    4.41E-06
   103       LT         21-Sc-49    48.9500   0.00E+00    2.02E-04
   104       LT         21-Sc-50    49.9522   0.00E+00    6.76E-03
   105       LT         22-Ti-44    43.9597   0.00E+00    3.66E-10
   106       LT         22-Ti-45    44.9581   0.00E+00    6.25E-05
   107       LT         22-Ti-46    45.9526   8.25E+00    0.00E+00
   108       LT         22-Ti-47    46.9518   7.44E+00    0.00E+00
   109       LT         22-Ti-48    47.9479   7.37E+01    0.00E+00
   110       LT         22-Ti-49    48.9479   5.41E+00    0.00E+00
   111       LT         22-Ti-50    49.9448   5.18E+00    0.00E+00
   112       LT         22-Ti-51    50.9466   0.00E+00    2.01E-03
   113       LT         23-V-48     47.9523   0.00E+00    5.02E-07
   114       LT         23-V-49     48.9485   0.00E+00    2.43E-08
   115       LT         23-V-50     49.9472   2.50E-01    1.57E-25
   116       LT         23-V-51     50.9440   9.98E+01    0.00E+00
   117       LT         23-V-52     51.9448   0.00E+00    3.09E-03
   118       LT         23-V-53     52.9443   0.00E+00    7.49E-03
   119       LT         23-V-54     53.9464   0.00E+00    1.39E-02
   120       LT         24-Cr-48    47.9540   0.00E+00    8.93E-06
   121       LT         24-Cr-49    48.9513   0.00E+00    2.73E-04
   122       LT         24-Cr-50    49.9460   4.35E+00    0.00E+00
   123       LT         24-Cr-51    50.9448   0.00E+00    2.90E-07
   124       LT         24-Cr-52    51.9405   8.38E+01    0.00E+00
   125       LT         24-Cr-53    52.9407   9.50E+00    0.00E+00
   126       LT         24-Cr-54    53.9389   2.37E+00    0.00E+00
   127       LT         24-Cr-55    54.9408   0.00E+00    3.30E-03
   128       LT         25-Mn-52    51.9456   0.00E+00    1.43E-06
   129       LT         25-Mn-53    52.9413   0.00E+00    5.94E-15
   130       LT         25-Mn-54    53.9404   0.00E+00    2.57E-08
   131       LT         25-Mn-55    54.9380   1.00E+02    0.00E+00
   132       LT         25-Mn-56    55.9389   0.00E+00    7.47E-05
   133       LT         25-Mn-57    56.9383   0.00E+00    8.12E-03
   134       LT         25-Mn-58    57.9400   0.00E+00    2.31E-01
   135       LT         26-Fe-54    53.9396   5.85E+00    0.00E+00
   136       LT         26-Fe-55    54.9383   0.00E+00    8.00E-09
   137       LT         26-Fe-56    55.9349   9.18E+01    0.00E+00
   138       LT         26-Fe-57    56.9354   2.12E+00    0.00E+00
   139       LT         26-Fe-58    57.9333   2.82E-01    0.00E+00
   140       LT         26-Fe-59    58.9349   0.00E+00    1.80E-07
   141       LT         26-Fe-60    59.9341   0.00E+00    1.46E-14
   142       LT         27-Co-55    54.9420   0.00E+00    1.10E-05
   143       LT         27-Co-56    55.9398   0.00E+00    1.04E-07
   144       LT         27-Co-57    56.9363   0.00E+00    2.95E-08
   145       LT         27-Co-58m   57.9358   0.00E+00    2.12E-05
   146       LT         27-Co-58    57.9357   0.00E+00    1.13E-07
   147       LT         27-Co-59    58.9332   1.00E+02    0.00E+00
   148       LT         27-Co-60    59.9338   0.00E+00    4.17E-09
   149       LT         27-Co-60m   59.9338   0.00E+00    1.10E-03
   150       LT         27-Co-61    60.9325   0.00E+00    1.17E-04
   151       LT         27-Co-62    61.9341   0.00E+00    7.70E-03
   152       LT         28-Ni-56    55.9421   0.00E+00    1.32E-06
   153       LT         28-Ni-57    56.9398   0.00E+00    5.41E-06
   154       LT         28-Ni-58    57.9353   6.81E+01    0.00E+00
   155       LT         28-Ni-59    58.9343   0.00E+00    2.89E-13
   156       LT         28-Ni-60    59.9308   2.62E+01    0.00E+00
   157       LT         28-Ni-61    60.9311   1.14E+00    0.00E+00
   158       LT         28-Ni-62    61.9283   3.63E+00    0.00E+00
   159       LT         28-Ni-63    62.9297   0.00E+00    2.17E-10
   160       LT         28-Ni-64    63.9280   9.26E-01    0.00E+00
   161       LT         28-Ni-65    64.9301   0.00E+00    7.65E-05
   162       LT         28-Ni-66    65.9291   0.00E+00    3.53E-06
   163       LT         29-Cu-62    61.9326   0.00E+00    1.19E-03
   164       LT         29-Cu-63    62.9296   6.92E+01    0.00E+00
   165       LT         29-Cu-64    63.9298   0.00E+00    1.52E-05
   166       LT         29-Cu-65    64.9278   3.09E+01    0.00E+00
   167       LT         29-Cu-66    65.9289   0.00E+00    2.26E-03
   168       LT         29-Cu-67    66.9277   0.00E+00    3.11E-06
   169       LT         30-Zn-63    62.9332   0.00E+00    3.00E-04
   170       LT         30-Zn-64    63.9291   4.83E+01    0.00E+00
   171       LT         30-Zn-65    64.9292   0.00E+00    3.29E-08
   172       LT         30-Zn-66    65.9260   2.80E+01    0.00E+00
   173       LT         30-Zn-67    66.9271   4.10E+00    0.00E+00
   174       LT         30-Zn-68    67.9248   1.90E+01    0.00E+00
   175       LT         30-Zn-69    68.9266   0.00E+00    2.05E-04
   176       LT         30-Zn-69m   68.9266   0.00E+00    1.40E-05
   177       LT         30-Zn-70    69.9253   6.31E-01    0.00E+00
   178       LT         30-Zn-71    70.9277   0.00E+00    4.72E-03
   179       LT         30-Zn-71m   70.9277   0.00E+00    4.86E-05
   180       LT         30-Zn-72    71.9269   0.00E+00    4.14E-06
   181       LT         31-Ga-67    66.9282   0.00E+00    2.46E-06
   182       LT         31-Ga-68    67.9280   0.00E+00    1.71E-04
   183       LT         31-Ga-69    68.9256   6.01E+01    0.00E+00
   184       LT         31-Ga-70    69.9260   0.00E+00    5.46E-04
   185       LT         31-Ga-71    70.9247   3.99E+01    0.00E+00
   186       LT         31-Ga-72    71.9264   0.00E+00    1.37E-05
   187       LT         31-Ga-72m   71.9264   0.00E+00    1.75E+01
   188       LT         32-Ge-68    67.9281   0.00E+00    2.96E-08
   189       LT         32-Ge-69    68.9280   0.00E+00    4.93E-06
   190       LT         32-Ge-70    69.9242   2.04E+01    0.00E+00
   191       LT         32-Ge-71    70.9249   0.00E+00    7.02E-07
   192       LT         32-Ge-71m   70.9249   0.00E+00    3.40E+01
   193       LT         32-Ge-72    71.9221   2.73E+01    0.00E+00
   194       LT         32-Ge-73    72.9235   7.76E+00    0.00E+00
   195       LT         32-Ge-73m   72.9235   0.00E+00    1.39E+00
   196       LT         32-Ge-74    73.9212   3.67E+01    0.00E+00
   197       LT         32-Ge-75    74.9229   0.00E+00    1.40E-04
   198       LT         32-Ge-75m   74.9229   0.00E+00    1.45E-02
   199       LT         32-Ge-76    75.9214   7.83E+00    0.00E+00
   200       LT         32-Ge-77    76.9236   0.00E+00    1.70E-05
   201       LT         32-Ge-77m   76.9236   0.00E+00    1.31E-02
   202       LT         33-As-71    70.9271   0.00E+00    2.95E-06
   203       LT         33-As-72    71.9268   0.00E+00    7.41E-06
   204       LT         33-As-73    72.9238   0.00E+00    9.99E-08
   205       LT         33-As-74    73.9239   0.00E+00    4.51E-07
   206       LT         33-As-75    74.9216   1.00E+02    0.00E+00
   207       LT         33-As-75m   74.9216   0.00E+00    3.93E+01
   208       LT         33-As-76    75.9224   0.00E+00    7.34E-06
   209       LT         33-As-77    76.9206   0.00E+00    4.96E-06
   210       LT         34-Se-72    71.9271   0.00E+00    9.55E-07
   211       LT         34-Se-73    72.9268   0.00E+00    2.69E-05
   212       LT         34-Se-74    73.9225   8.90E-01    0.00E+00
   213       LT         34-Se-75    74.9225   0.00E+00    6.70E-08
   214       LT         34-Se-76    75.9192   9.37E+00    0.00E+00
   215       LT         34-Se-77    76.9199   7.63E+00    0.00E+00
   216       LT         34-Se-77m   76.9199   0.00E+00    3.99E-02
   217       LT         34-Se-78    77.9173   2.38E+01    0.00E+00
   218       LT         34-Se-79    78.9185   0.00E+00    7.45E-14
   219       LT         34-Se-79m   78.9185   0.00E+00    2.95E-03
   220       LT         34-Se-80    79.9165   4.96E+01    0.00E+00
   221       LT         34-Se-81    80.9180   0.00E+00    6.26E-04
   222       LT         34-Se-81m   80.9180   0.00E+00    2.02E-04
   223       LT         34-Se-82    81.9167   8.73E+00    0.00E+00
   224       LT         34-Se-83    82.9191   0.00E+00    5.18E-04
   225       LT         34-Se-83m   82.9191   0.00E+00    9.89E-03
   226       LT         35-Br-76    75.9245   0.00E+00    1.19E-05
   227       LT         35-Br-77    76.9214   0.00E+00    3.38E-06
   228       LT         35-Br-77m   76.9214   0.00E+00    2.70E-03
   229       LT         35-Br-78    77.9212   0.00E+00    1.79E-03
   230       LT         35-Br-79    78.9183   5.07E+01    0.00E+00
   231       LT         35-Br-80    79.9185   0.00E+00    6.53E-04
   232       LT         35-Br-80m   79.9185   0.00E+00    4.36E-05
   233       LT         35-Br-81    80.9163   4.93E+01    0.00E+00
   234       LT         35-Br-82    81.9168   0.00E+00    5.46E-06
   235       LT         35-Br-82m   81.9168   0.00E+00    1.88E-03
   236       LT         35-Br-83    82.9152   0.00E+00    8.02E-05
   237       LT         36-Kr-76    75.9259   0.00E+00    1.30E-05
   238       LT         36-Kr-77    76.9247   0.00E+00    1.55E-04
   239       LT         36-Kr-78    77.9204   3.55E-01    0.00E+00
   240       LT         36-Kr-79    78.9201   0.00E+00    5.49E-06
   241       LT         36-Kr-79m   78.9201   0.00E+00    1.39E-02
   242       LT         36-Kr-80    79.9164   2.29E+00    0.00E+00
   243       LT         36-Kr-81    80.9166   0.00E+00    9.59E-14
   244       LT         36-Kr-81m   80.9166   0.00E+00    5.29E-02
   245       LT         36-Kr-82    81.9135   1.16E+01    0.00E+00
   246       LT         36-Kr-83    82.9141   1.15E+01    0.00E+00
   247       LT         36-Kr-83m   82.9141   0.00E+00    1.05E-04
   248       LT         36-Kr-84    83.9115   5.70E+01    0.00E+00
   249       LT         36-Kr-85    84.9125   0.00E+00    2.04E-09
   250       LT         36-Kr-85m   84.9125   0.00E+00    4.30E-05
   251       LT         36-Kr-86    85.9106   1.73E+01    0.00E+00
   252       LT         36-Kr-87    86.9134   0.00E+00    1.51E-04
   253       LT         36-Kr-88    87.9145   0.00E+00    6.78E-05
   254       LT         37-Rb-82    81.9182   0.00E+00    9.19E-03
   255       LT         37-Rb-83    82.9151   0.00E+00    9.31E-08
   256       LT         37-Rb-84    83.9144   0.00E+00    2.44E-07
   257       LT         37-Rb-85    84.9118   7.22E+01    0.00E+00
   258       LT         37-Rb-86    85.9112   0.00E+00    4.31E-07
   259       LT         37-Rb-86m   85.9112   0.00E+00    1.14E-02
   260       LT         37-Rb-87    86.9092   2.78E+01    4.57E-19
   261       LT         37-Rb-88    87.9113   0.00E+00    6.50E-04
   262       LT         37-Rb-89    88.9123   0.00E+00    7.63E-04
   263       LT         38-Sr-82    81.9184   0.00E+00    3.16E-07
   264       LT         38-Sr-83    82.9176   0.00E+00    5.94E-06
   265       LT         38-Sr-84    83.9134   5.60E-01    0.00E+00
   266       LT         38-Sr-85    84.9129   0.00E+00    1.24E-07
   267       LT         38-Sr-85m   84.9129   0.00E+00    1.71E-04
   268       LT         38-Sr-86    85.9093   9.86E+00    0.00E+00
   269       LT         38-Sr-87    86.9089   7.00E+00    0.00E+00
   270       LT         38-Sr-87m   86.9089   0.00E+00    6.84E-05
   271       LT         38-Sr-88    87.9056   8.26E+01    0.00E+00
   272       LT         38-Sr-89    88.9074   0.00E+00    1.59E-07
   273       LT         38-Sr-90    89.9077   0.00E+00    7.63E-10
   274       LT         38-Sr-91    90.9102   0.00E+00    2.00E-05
   275       LT         38-Sr-93    92.9140   0.00E+00    1.56E-03
   276       LT         39-Y-86     85.9149   0.00E+00    1.31E-05
   277       LT         39-Y-87     86.9109   0.00E+00    2.41E-06
   278       LT         39-Y-87m    86.9109   0.00E+00    1.44E-05
   279       LT         39-Y-88     87.9095   0.00E+00    7.52E-08
   280       LT         39-Y-89     88.9059   1.00E+02    0.00E+00
   281       LT         39-Y-89m    88.9059   0.00E+00    4.43E-02
   282       LT         39-Y-90     89.9072   0.00E+00    3.01E-06
   283       LT         39-Y-90m    89.9072   0.00E+00    6.04E-05
   284       LT         39-Y-91     90.9073   0.00E+00    1.37E-07
   285       LT         39-Y-91m    90.9073   0.00E+00    2.32E-04
   286       LT         39-Y-92     91.9090   0.00E+00    5.44E-05
   287       LT         39-Y-93     92.9096   0.00E+00    1.89E-05
   288       LT         39-Y-93m    92.9096   0.00E+00    8.45E-01
   289       LT         39-Y-94     93.9116   0.00E+00    6.18E-04
   290       LT         39-Y-96     95.9159   0.00E+00    1.30E-01
   291       LT         40-Zr-86    85.9165   0.00E+00    1.17E-05
   292       LT         40-Zr-87    86.9148   0.00E+00    1.15E-04
   293       LT         40-Zr-88    87.9102   0.00E+00    9.62E-08
   294       LT         40-Zr-89    88.9089   0.00E+00    2.46E-06
   295       LT         40-Zr-90    89.9047   5.15E+01    0.00E+00
   296       LT         40-Zr-90m   89.9047   0.00E+00    8.57E-01
   297       LT         40-Zr-91    90.9056   1.12E+01    0.00E+00
   298       LT         40-Zr-92    91.9050   1.72E+01    0.00E+00
   299       LT         40-Zr-93    92.9065   0.00E+00    1.44E-14
   300       LT         40-Zr-94    93.9063   1.74E+01    0.00E+00
   301       LT         40-Zr-95    94.9080   0.00E+00    1.25E-07
   302       LT         40-Zr-96    95.9083   2.80E+00    1.10E-27
   303       LT         40-Zr-97    96.9109   0.00E+00    1.15E-05
   304       LT         41-Nb-90    89.9113   0.00E+00    1.32E-05
   305       LT         41-Nb-90m   89.9113   0.00E+00    3.69E-02
   306       LT         41-Nb-91    90.9070   0.00E+00    3.23E-11
   307       LT         41-Nb-91m   90.9070   0.00E+00    1.32E-07
   308       LT         41-Nb-92    91.9072   0.00E+00    6.33E-16
   309       LT         41-Nb-92m   91.9072   0.00E+00    7.90E-07
   310       LT         41-Nb-93    92.9064   1.00E+02    0.00E+00
   311       LT         41-Nb-93m   92.9064   0.00E+00    1.36E-09
   312       LT         41-Nb-94    93.9073   0.00E+00    1.08E-12
   313       LT         41-Nb-94m   93.9073   0.00E+00    1.84E-03
   314       LT         41-Nb-95    94.9068   0.00E+00    2.29E-07
   315       LT         41-Nb-95m   94.9068   0.00E+00    2.22E-06
   316       LT         41-Nb-96    95.9081   0.00E+00    8.25E-06
   317       LT         41-Nb-97    96.9081   0.00E+00    1.60E-04
   318       LT         41-Nb-97m   96.9081   0.00E+00    1.18E-02
   319       LT         41-Nb-98    97.9103   0.00E+00    2.42E-01
   320       LT         41-Nb-100   99.9142   0.00E+00    4.62E-01
   321       LT         42-Mo-92    91.9068   1.48E+01    0.00E+00
   322       LT         42-Mo-93m   92.9068   0.00E+00    2.81E-05
   323       LT         42-Mo-93    92.9068   0.00E+00    5.49E-12
   324       LT         42-Mo-94    93.9051   9.23E+00    0.00E+00
   325       LT         42-Mo-95    94.9058   1.59E+01    0.00E+00
   326       LT         42-Mo-96    95.9047   1.67E+01    0.00E+00
   327       LT         42-Mo-97    96.9060   9.56E+00    0.00E+00
   328       LT         42-Mo-98    97.9054   2.42E+01    0.00E+00
   329       LT         42-Mo-99    98.9077   0.00E+00    2.92E-06
   330       LT         42-Mo-100   99.9075   9.67E+00    3.01E-27
   331       LT         42-Mo-101   100.9103  0.00E+00    7.91E-04
   332       LT         43-Tc-95    94.9077   0.00E+00    9.63E-06
   333       LT         43-Tc-95m   94.9077   0.00E+00    1.32E-07
   334       LT         43-Tc-96    95.9079   0.00E+00    1.87E-06
   335       LT         43-Tc-97    96.9064   0.00E+00    5.22E-15
   336       LT         43-Tc-97m   96.9064   0.00E+00    8.82E-08
   337       LT         43-Tc-98    97.9072   0.00E+00    5.23E-15
   338       LT         43-Tc-99    98.9062   0.00E+00    1.04E-13
   339       LT         43-Tc-99m   98.9062   0.00E+00    3.21E-05
   340       LT         43-Tc-100   99.9077   0.00E+00    4.48E-02
   341       LT         43-Tc-101   100.9073  0.00E+00    8.14E-04
   342       LT         44-Ru-96    95.9076   5.54E+00    0.00E+00
   343       LT         44-Ru-97    96.9076   0.00E+00    2.83E-06
   344       LT         44-Ru-98    97.9053   1.87E+00    0.00E+00
   345       LT         44-Ru-99    98.9059   1.28E+01    0.00E+00
   346       LT         44-Ru-100   99.9042   1.26E+01    0.00E+00
   347       LT         44-Ru-101   100.9056  1.71E+01    0.00E+00
   348       LT         44-Ru-102   101.9044  3.16E+01    0.00E+00
   349       LT         44-Ru-103   102.9063  0.00E+00    2.04E-07
   350       LT         44-Ru-104   103.9054  1.86E+01    0.00E+00
   351       LT         44-Ru-105   104.9078  0.00E+00    4.34E-05
   352       LT         44-Ru-106   105.9073  0.00E+00    2.16E-08
   353       LT         44-Ru-107   106.9099  0.00E+00    3.08E-03
   354       LT         45-Rh-99    98.9081   0.00E+00    4.98E-07
   355       LT         45-Rh-99m   98.9081   0.00E+00    4.10E-05
   356       LT         45-Rh-100   99.9081   0.00E+00    9.26E-06
   357       LT         45-Rh-101   100.9062  0.00E+00    6.66E-09
   358       LT         45-Rh-101m  100.9062  0.00E+00    1.85E-06
   359       LT         45-Rh-102   101.9068  0.00E+00    3.87E-08
   360       LT         45-Rh-102m  101.9068  0.00E+00    5.87E-09
   361       LT         45-Rh-103   102.9055  1.00E+02    0.00E+00
   362       LT         45-Rh-103m  102.9055  0.00E+00    2.06E-04
   363       LT         45-Rh-104   103.9067  0.00E+00    1.64E-02
   364       LT         45-Rh-104m  103.9067  0.00E+00    2.66E-03
   365       LT         45-Rh-105   104.9057  0.00E+00    5.45E-06
   366       LT         45-Rh-105m  104.9057  0.00E+00    1.73E-02
   367       LT         45-Rh-106   105.9073  0.00E+00    2.31E-02
   368       LT         45-Rh-106m  105.9073  0.00E+00    8.82E-05
   369       LT         45-Rh-107   106.9068  0.00E+00    5.32E-04
   370       LT         46-Pd-100   99.9085   0.00E+00    2.21E-06
   371       LT         46-Pd-101   100.9083  0.00E+00    2.27E-05
   372       LT         46-Pd-102   101.9056  1.02E+00    0.00E+00
   373       LT         46-Pd-103   102.9061  0.00E+00    4.72E-07
   374       LT         46-Pd-104   103.9040  1.11E+01    0.00E+00
   375       LT         46-Pd-105   104.9051  2.23E+01    0.00E+00
   376       LT         46-Pd-106   105.9035  2.73E+01    0.00E+00
   377       LT         46-Pd-107   106.9051  0.00E+00    3.38E-15
   378       LT         46-Pd-107m  106.9051  0.00E+00    3.25E-02
   379       LT         46-Pd-108   107.9039  2.65E+01    0.00E+00
   380       LT         46-Pd-109   108.9060  0.00E+00    1.41E-05
   381       LT         46-Pd-109m  108.9060  0.00E+00    2.46E-03
   382       LT         46-Pd-110   109.9052  1.17E+01    0.00E+00
   383       LT         46-Pd-111   110.9077  0.00E+00    4.94E-04
   384       LT         46-Pd-111m  110.9077  0.00E+00    3.50E-05
   385       LT         46-Pd-112   111.9073  0.00E+00    9.16E-06
   386       LT         47-Ag-105   104.9065  0.00E+00    1.94E-07
   387       LT         47-Ag-106   105.9067  0.00E+00    4.82E-04
   388       LT         47-Ag-106m  105.9067  0.00E+00    9.69E-07
   389       LT         47-Ag-107   106.9051  5.18E+01    0.00E+00
   390       LT         47-Ag-107m  106.9051  0.00E+00    1.56E-02
   391       LT         47-Ag-108   107.9060  0.00E+00    4.85E-03
   392       LT         47-Ag-108m  107.9060  0.00E+00    5.01E-11
   393       LT         47-Ag-109   108.9047  4.82E+01    0.00E+00
   394       LT         47-Ag-109m  108.9047  0.00E+00    1.75E-02
   395       LT         47-Ag-110   109.9061  0.00E+00    2.82E-02
   396       LT         47-Ag-110m  109.9062  0.00E+00    3.21E-08
   397       LT         47-Ag-111   110.9053  0.00E+00    1.08E-06
   398       LT         47-Ag-111m  110.9053  0.00E+00    1.07E-02
   399       LT         47-Ag-112   111.9070  0.00E+00    6.15E-05
   400       LT         48-Cd-106   105.9065  1.25E+00    0.00E+00
   401       LT         48-Cd-107   106.9066  0.00E+00    2.96E-05
   402       LT         48-Cd-108   107.9042  8.90E-01    0.00E+00
   403       LT         48-Cd-109   108.9050  0.00E+00    1.74E-08
   404       LT         48-Cd-110   109.9030  1.25E+01    0.00E+00
   405       LT         48-Cd-111   110.9042  1.28E+01    0.00E+00
   406       LT         48-Cd-111m  110.9042  0.00E+00    2.38E-04
   407       LT         48-Cd-112   111.9028  2.41E+01    0.00E+00
   408       LT         48-Cd-113   112.9044  1.22E+01    2.73E-24
   409       LT         48-Cd-113m  112.9044  0.00E+00    1.56E-09
   410       LT         48-Cd-114   113.9034  2.87E+01    0.00E+00
   411       LT         48-Cd-115   114.9054  0.00E+00    3.60E-06
   412       LT         48-Cd-115m  114.9051  0.00E+00    1.80E-07
   413       LT         48-Cd-116   115.9048  7.49E+00    7.09E-28
   414       LT         48-Cd-117   116.9072  0.00E+00    7.73E-05
   415       LT         48-Cd-117m  116.9072  0.00E+00    5.73E-05
   416       LT         48-Cd-119   118.9099  0.00E+00    4.29E-03
   417       LT         48-Cd-121   120.9130  0.00E+00    5.13E-02
   418       LT         49-In-111   110.9051  0.00E+00    2.86E-06
   419       LT         49-In-112   111.9055  0.00E+00    7.72E-04
   420       LT         49-In-113   112.9041  4.29E+00    0.00E+00
   421       LT         49-In-113m  112.9041  0.00E+00    1.16E-04
   422       LT         49-In-114   113.9049  0.00E+00    9.64E-03
   423       LT         49-In-114m  113.9049  0.00E+00    1.62E-07
   424       LT         49-In-115   114.9039  9.57E+01    4.98E-23
   425       LT         49-In-115m  114.9039  0.00E+00    4.29E-05
   426       LT         49-In-116   115.9053  0.00E+00    4.92E-02
   427       LT         49-In-116m  115.9053  0.00E+00    2.13E-04
   428       LT         49-In-117   116.9045  0.00E+00    2.67E-04
   429       LT         49-In-117m  116.9045  0.00E+00    9.94E-05
   430       LT         49-In-118   117.9063  0.00E+00    1.39E-01
   431       LT         49-In-119   118.9059  0.00E+00    4.81E-03
   432       LT         49-In-119m  118.9059  0.00E+00    6.42E-04
   433       LT         49-In-120   119.9080  0.00E+00    2.25E-01
   434       LT         49-In-120m  119.9080  0.00E+00    1.50E-02
   435       LT         49-In-121   120.9079  0.00E+00    3.00E-02
   436       LT         49-In-121m  120.9079  0.00E+00    2.98E-03
   437       LT         50-Sn-112   111.9048  9.70E-01    0.00E+00
   438       LT         50-Sn-113   112.9052  0.00E+00    6.97E-08
   439       LT         50-Sn-113m  112.9052  0.00E+00    5.40E-04
   440       LT         50-Sn-114   113.9028  6.60E-01    0.00E+00
   441       LT         50-Sn-115   114.9033  3.40E-01    0.00E+00
   442       LT         50-Sn-116   115.9017  1.45E+01    0.00E+00
   443       LT         50-Sn-117   116.9029  7.68E+00    0.00E+00
   444       LT         50-Sn-117m  116.9029  0.00E+00    5.90E-07
   445       LT         50-Sn-118   117.9016  2.42E+01    0.00E+00
   446       LT         50-Sn-119   118.9033  8.59E+00    0.00E+00
   447       LT         50-Sn-119m  118.9033  0.00E+00    2.74E-08
   448       LT         50-Sn-120   119.9022  3.26E+01    0.00E+00
   449       LT         50-Sn-121   120.9042  0.00E+00    7.12E-06
   450       LT         50-Sn-121m  120.9042  0.00E+00    5.00E-10
   451       LT         50-Sn-122   121.9034  4.63E+00    0.00E+00
   452       LT         50-Sn-123   122.9057  0.00E+00    6.21E-08
   453       LT         50-Sn-123m  122.9057  0.00E+00    2.88E-04
   454       LT         50-Sn-124   123.9053  5.79E+00    0.00E+00
   455       LT         50-Sn-125   124.9078  0.00E+00    8.32E-07
   456       LT         50-Sn-125m  124.9078  0.00E+00    1.21E-03
   457       LT         50-Sn-126   125.9077  0.00E+00    9.55E-14
   458       LT         51-Sb-118   117.9055  0.00E+00    3.21E-03
   459       LT         51-Sb-119   118.9039  0.00E+00    5.04E-06
   460       LT         51-Sb-120   119.9051  0.00E+00    7.27E-04
   461       LT         51-Sb-120m  119.9051  0.00E+00    1.39E-06
   462       LT         51-Sb-121   120.9038  5.72E+01    0.00E+00
   463       LT         51-Sb-122   121.9052  0.00E+00    2.95E-06
   464       LT         51-Sb-122m  121.9052  0.00E+00    2.76E-03
   465       LT         51-Sb-123   122.9042  4.28E+01    0.00E+00
   466       LT         51-Sb-124   123.9059  0.00E+00    1.33E-07
   467       LT         51-Sb-124m  123.9059  0.00E+00    7.45E-03
   468       LT         51-Sb-125   124.9053  0.00E+00    7.96E-09
   469       LT         51-Sb-126   125.9072  0.00E+00    6.50E-07
   470       LT         51-Sb-126m  125.9072  0.00E+00    6.03E-04
   471       LT         51-Sb-127   126.9069  0.00E+00    2.08E-06
   472       LT         52-Te-118   117.9058  0.00E+00    1.34E-06
   473       LT         52-Te-119   118.9064  0.00E+00    1.20E-05
   474       LT         52-Te-119m  118.9064  0.00E+00    1.71E-06
   475       LT         52-Te-120   119.9040  9.00E-02    0.00E+00
   476       LT         52-Te-121   120.9049  0.00E+00    4.19E-07
   477       LT         52-Te-121m  120.9049  0.00E+00    4.89E-08
   478       LT         52-Te-122   121.9030  2.55E+00    0.00E+00
   479       LT         52-Te-123   122.9043  8.90E-01    0.00E+00
   480       LT         52-Te-123m  122.9043  0.00E+00    6.73E-08
   481       LT         52-Te-124   123.9028  4.74E+00    0.00E+00
   482       LT         52-Te-125   124.9044  7.07E+00    0.00E+00
   483       LT         52-Te-125m  124.9044  0.00E+00    1.40E-07
   484       LT         52-Te-126   125.9033  1.88E+01    0.00E+00
   485       LT         52-Te-127   126.9052  0.00E+00    2.06E-05
   486       LT         52-Te-127m  126.9052  0.00E+00    7.36E-08
   487       LT         52-Te-128   127.9045  3.17E+01    2.50E-27
   488       LT         52-Te-129   128.9066  0.00E+00    1.66E-04
   489       LT         52-Te-129m  128.9074  0.00E+00    2.39E-07
   490       LT         52-Te-130   129.9062  3.41E+01    0.00E+00
   491       LT         52-Te-131   130.9085  0.00E+00    4.62E-04
   492       LT         52-Te-131m  130.9085  0.00E+00    5.79E-06
   493       LT         52-Te-132   131.9086  0.00E+00    2.50E-06
   494       LT         53-I-122    121.9076  0.00E+00    3.18E-03
   495       LT         53-I-123    122.9056  0.00E+00    1.46E-05
   496       LT         53-I-124    123.9062  0.00E+00    1.92E-06
   497       LT         53-I-125    124.9046  0.00E+00    1.35E-07
   498       LT         53-I-126    125.9056  0.00E+00    6.20E-07
   499       LT         53-I-127    126.9045  1.00E+02    0.00E+00
   500       LT         53-I-128    127.9058  0.00E+00    4.62E-04
   501       LT         53-I-129    128.9050  0.00E+00    1.40E-15
   502       LT         53-I-130    129.9067  0.00E+00    1.56E-05
   503       LT         53-I-130m   129.9067  0.00E+00    1.31E-03
   504       LT         53-I-131    130.9061  0.00E+00    1.00E-06
   505       LT         53-I-132    131.9080  0.00E+00    8.39E-05
   506       LT         53-I-133    132.9078  0.00E+00    9.26E-06
   507       LT         54-Xe-122   121.9084  0.00E+00    9.58E-06
   508       LT         54-Xe-123   122.9085  0.00E+00    9.26E-05
   509       LT         54-Xe-124   123.9059  9.52E-02    0.00E+00
   510       LT         54-Xe-125   124.9064  0.00E+00    1.14E-05
   511       LT         54-Xe-125m  124.9064  0.00E+00    1.22E-02
   512       LT         54-Xe-126   125.9043  8.90E-02    0.00E+00
   513       LT         54-Xe-127   126.9052  0.00E+00    2.20E-07
   514       LT         54-Xe-127m  126.9052  0.00E+00    1.00E-02
   515       LT         54-Xe-128   127.9035  1.91E+00    0.00E+00
   516       LT         54-Xe-129   128.9048  2.64E+01    0.00E+00
   517       LT         54-Xe-129m  128.9048  0.00E+00    9.03E-07
   518       LT         54-Xe-130   129.9035  4.07E+00    0.00E+00
   519       LT         54-Xe-131   130.9051  2.12E+01    0.00E+00
   520       LT         54-Xe-131m  130.9051  0.00E+00    6.78E-07
   521       LT         54-Xe-132   131.9041  2.69E+01    0.00E+00
   522       LT         54-Xe-133   132.9059  0.00E+00    1.53E-06
   523       LT         54-Xe-133m  132.9059  0.00E+00    3.66E-06
   524       LT         54-Xe-134   133.9054  1.04E+01    0.00E+00
   525       LT         54-Xe-135   134.9072  0.00E+00    2.11E-05
   526       LT         54-Xe-135m  134.9072  0.00E+00    7.56E-04
   527       LT         54-Xe-136   135.9072  8.86E+00    0.00E+00
   528       LT         54-Xe-137   136.9116  0.00E+00    3.03E-03
   529       LT         55-Cs-128   127.9078  0.00E+00    3.19E-03
   530       LT         55-Cs-129   128.9061  0.00E+00    6.01E-06
   531       LT         55-Cs-130   129.9067  0.00E+00    3.95E-04
   532       LT         55-Cs-131   130.9055  0.00E+00    8.28E-07
   533       LT         55-Cs-132   131.9064  0.00E+00    1.24E-06
   534       LT         55-Cs-133   132.9055  1.00E+02    0.00E+00
   535       LT         55-Cs-134   133.9067  0.00E+00    1.06E-08
   536       LT         55-Cs-134m  133.9067  0.00E+00    6.61E-05
   537       LT         55-Cs-135   134.9060  0.00E+00    9.55E-15
   538       LT         55-Cs-136   135.9073  0.00E+00    6.10E-07
   539       LT         55-Cs-137   136.9071  0.00E+00    7.30E-10
   540       LT         55-Cs-138   137.9110  0.00E+00    3.46E-04
   541       LT         56-Ba-128   127.9083  0.00E+00    3.30E-06
   542       LT         56-Ba-129   128.9087  0.00E+00    8.63E-05
   543       LT         56-Ba-130   129.9063  1.06E-01    0.00E+00
   544       LT         56-Ba-131   130.9069  0.00E+00    6.98E-07
   545       LT         56-Ba-131m  130.9069  0.00E+00    7.91E-04
   546       LT         56-Ba-132   131.9051  1.01E-01    0.00E+00
   547       LT         56-Ba-133   132.9060  0.00E+00    2.09E-09
   548       LT         56-Ba-133m  132.9060  0.00E+00    4.95E-06
   549       LT         56-Ba-134   133.9045  2.42E+00    0.00E+00
   550       LT         56-Ba-135   134.9057  6.59E+00    0.00E+00
   551       LT         56-Ba-135m  134.9057  0.00E+00    6.71E-06
   552       LT         56-Ba-136   135.9046  7.85E+00    0.00E+00
   553       LT         56-Ba-136m  135.9046  0.00E+00    2.25E+00
   554       LT         56-Ba-137   136.9058  1.12E+01    0.00E+00
   555       LT         56-Ba-137m  136.9058  0.00E+00    4.53E-03
   556       LT         56-Ba-138   137.9052  7.17E+01    0.00E+00
   557       LT         56-Ba-139   138.9088  0.00E+00    1.39E-04
   558       LT         56-Ba-140   139.9106  0.00E+00    6.29E-07
   559       LT         56-Ba-141   140.9144  0.00E+00    6.32E-04
   560       LT         57-La-134   133.9085  0.00E+00    1.79E-03
   561       LT         57-La-135   134.9070  0.00E+00    9.87E-06
   562       LT         57-La-136   135.9076  0.00E+00    1.17E-03
   563       LT         57-La-137   136.9065  0.00E+00    3.66E-13
   564       LT         57-La-138   137.9071  9.00E-02    2.15E-19
   565       LT         57-La-139   138.9064  9.99E+01    0.00E+00
   566       LT         57-La-140   139.9095  0.00E+00    4.78E-06
   567       LT         57-La-141   140.9110  0.00E+00    4.91E-05
   568       LT         58-Ce-134   133.9089  0.00E+00    2.54E-06
   569       LT         58-Ce-135   134.9091  0.00E+00    1.09E-05
   570       LT         58-Ce-136   135.9072  1.85E-01    0.00E+00
   571       LT         58-Ce-137   136.9078  0.00E+00    2.14E-05
   572       LT         58-Ce-137m  136.9078  0.00E+00    5.60E-06
   573       LT         58-Ce-138   137.9060  2.51E-01    0.00E+00
   574       LT         58-Ce-139   138.9066  0.00E+00    5.83E-08
   575       LT         58-Ce-139m  138.9066  0.00E+00    1.26E-02
   576       LT         58-Ce-140   139.9054  8.85E+01    0.00E+00
   577       LT         58-Ce-141   140.9083  0.00E+00    2.47E-07
   578       LT         58-Ce-142   141.9092  1.11E+01    0.00E+00
   579       LT         58-Ce-143   142.9124  0.00E+00    5.83E-06
   580       LT         58-Ce-144   143.9137  0.00E+00    2.82E-08
   581       LT         58-Ce-145   144.9172  0.00E+00    3.84E-03
   582       LT         59-Pr-140   139.9091  0.00E+00    3.41E-03
   583       LT         59-Pr-141   140.9077  1.00E+02    0.00E+00
   584       LT         59-Pr-142   141.9100  0.00E+00    1.01E-05
   585       LT         59-Pr-142m  141.9100  0.00E+00    7.91E-04
   586       LT         59-Pr-143   142.9108  0.00E+00    5.91E-07
   587       LT         59-Pr-144   143.9133  0.00E+00    6.69E-04
   588       LT         59-Pr-144m  143.9133  0.00E+00    1.60E-03
   589       LT         59-Pr-145   144.9145  0.00E+00    3.22E-05
   590       LT         60-Nd-140   139.9095  0.00E+00    2.38E-06
   591       LT         60-Nd-141   140.9096  0.00E+00    7.73E-05
   592       LT         60-Nd-141m  140.9096  0.00E+00    1.12E-02
   593       LT         60-Nd-142   141.9077  2.72E+01    0.00E+00
   594       LT         60-Nd-143   142.9098  1.22E+01    0.00E+00
   595       LT         60-Nd-144   143.9101  2.38E+01    9.59E-24
   596       LT         60-Nd-145   144.9126  8.30E+00    0.00E+00
   597       LT         60-Nd-146   145.9131  1.72E+01    0.00E+00
   598       LT         60-Nd-147   146.9161  0.00E+00    7.31E-07
   599       LT         60-Nd-148   147.9169  5.70E+00    0.00E+00
   600       LT         60-Nd-149   148.9202  0.00E+00    1.11E-04
   601       LT         60-Nd-150   149.9209  5.60E+00    2.78E-27
   602       LT         60-Nd-151   150.9238  0.00E+00    9.29E-04
   603       LT         61-Pm-143   142.9109  0.00E+00    3.03E-08
   604       LT         61-Pm-144   143.9126  0.00E+00    2.21E-08
   605       LT         61-Pm-145   144.9128  0.00E+00    1.24E-09
   606       LT         61-Pm-146   145.9147  0.00E+00    3.97E-09
   607       LT         61-Pm-147   146.9151  0.00E+00    8.37E-09
   608       LT         61-Pm-148   147.9175  0.00E+00    1.49E-06
   609       LT         61-Pm-148m  147.9207  0.00E+00    1.94E-07
   610       LT         61-Pm-149   148.9183  0.00E+00    3.63E-06
   611       LT         61-Pm-150   149.9210  0.00E+00    7.18E-05
   612       LT         61-Pm-151   150.9212  0.00E+00    6.78E-06
   613       LT         61-Pm-152   151.9235  0.00E+00    2.80E-03
   614       LT         62-Sm-144   143.9120  3.07E+00    0.00E+00
   615       LT         62-Sm-145   144.9134  0.00E+00    2.36E-08
   616       LT         62-Sm-146   145.9130  0.00E+00    2.13E-16
   617       LT         62-Sm-147   146.9149  1.50E+01    2.07E-19
   618       LT         62-Sm-148   147.9148  1.12E+01    3.14E-24
   619       LT         62-Sm-149   148.9172  1.38E+01    0.00E+00
   620       LT         62-Sm-150   149.9173  7.38E+00    0.00E+00
   621       LT         62-Sm-151   150.9199  0.00E+00    2.44E-10
   622       LT         62-Sm-152   151.9197  2.68E+01    0.00E+00
   623       LT         62-Sm-153   152.9221  0.00E+00    4.14E-06
   624       LT         62-Sm-154   153.9222  2.28E+01    0.00E+00
   625       LT         62-Sm-155   154.9246  0.00E+00    5.18E-04
   626       LT         63-Eu-145   144.9163  0.00E+00    1.35E-06
   627       LT         63-Eu-146   145.9172  0.00E+00    1.75E-06
   628       LT         63-Eu-147   146.9167  0.00E+00    3.33E-07
   629       LT         63-Eu-148   147.9181  0.00E+00    1.47E-07
   630       LT         63-Eu-149   148.9179  0.00E+00    8.62E-08
   631       LT         63-Eu-150   149.9197  0.00E+00    5.95E-10
   632       LT         63-Eu-150m  149.9197  0.00E+00    1.50E-05
   633       LT         63-Eu-151   150.9198  4.78E+01    0.00E+00
   634       LT         63-Eu-152   151.9217  0.00E+00    1.62E-09
   635       LT         63-Eu-152m  151.9217  0.00E+00    2.07E-05
   636       LT         63-Eu-153   152.9212  5.22E+01    0.00E+00
   637       LT         63-Eu-154   153.9230  0.00E+00    2.55E-09
   638       LT         63-Eu-155   154.9229  0.00E+00    4.62E-09
   639       LT         63-Eu-156   155.9247  0.00E+00    5.28E-07
   640       LT         63-Eu-157   156.9254  0.00E+00    1.27E-05
   641       LT         64-Gd-146   145.9183  0.00E+00    1.66E-07
   642       LT         64-Gd-147   146.9191  0.00E+00    5.06E-06
   643       LT         64-Gd-148   147.9181  0.00E+00    2.94E-10
   644       LT         64-Gd-149   148.9193  0.00E+00    8.65E-07
   645       LT         64-Gd-150   149.9187  0.00E+00    1.23E-14
   646       LT         64-Gd-151   150.9203  0.00E+00    6.47E-08
   647       LT         64-Gd-152   151.9198  2.00E-01    2.03E-22
   648       LT         64-Gd-153   152.9218  0.00E+00    3.34E-08
   649       LT         64-Gd-154   153.9209  2.18E+00    0.00E+00
   650       LT         64-Gd-155m  154.9226  0.00E+00    2.17E+01
   651       LT         64-Gd-155   154.9226  1.48E+01    0.00E+00
   652       LT         64-Gd-156   155.9221  2.05E+01    0.00E+00
   653       LT         64-Gd-157   156.9240  1.57E+01    0.00E+00
   654       LT         64-Gd-158   157.9241  2.48E+01    0.00E+00
   655       LT         64-Gd-159   158.9264  0.00E+00    1.04E-05
   656       LT         64-Gd-160   159.9270  2.19E+01    0.00E+00
   657       LT         64-Gd-161   160.9297  0.00E+00    3.16E-03
   658       LT         64-Gd-162   161.9310  0.00E+00    1.38E-03
   659       LT         65-Tb-152   151.9241  0.00E+00    1.10E-05
   660       LT         65-Tb-153   152.9234  0.00E+00    3.43E-06
   661       LT         65-Tb-154   153.9247  0.00E+00    8.96E-06
   662       LT         65-Tb-154m  153.9247  0.00E+00    2.05E-05
   663       LT         65-Tb-155   154.9235  0.00E+00    1.51E-06
   664       LT         65-Tb-156   155.9247  0.00E+00    1.50E-06
   665       LT         65-Tb-156m  155.9247  0.00E+00    7.89E-06
   666       LT         65-Tb-157   156.9240  0.00E+00    3.09E-10
   667       LT         65-Tb-158   157.9254  0.00E+00    1.22E-10
   668       LT         65-Tb-159   158.9254  1.00E+02    0.00E+00
   669       LT         65-Tb-160   159.9272  0.00E+00    1.11E-07
   670       LT         65-Tb-161   160.9276  0.00E+00    1.16E-06
   671       LT         65-Tb-162   161.9295  0.00E+00    1.52E-03
   672       LT         66-Dy-154   153.9244  0.00E+00    7.32E-15
   673       LT         66-Dy-155   154.9258  0.00E+00    1.94E-05
   674       LT         66-Dy-156   155.9243  5.60E-02    0.00E+00
   675       LT         66-Dy-157   156.9255  0.00E+00    2.37E-05
   676       LT         66-Dy-158   157.9244  9.50E-02    0.00E+00
   677       LT         66-Dy-159   158.9257  0.00E+00    5.56E-08
   678       LT         66-Dy-160   159.9252  2.33E+00    0.00E+00
   679       LT         66-Dy-161   160.9269  1.89E+01    0.00E+00
   680       LT         66-Dy-162   161.9268  2.55E+01    0.00E+00
   681       LT         66-Dy-163   162.9287  2.49E+01    0.00E+00
   682       LT         66-Dy-164   163.9292  2.83E+01    0.00E+00
   683       LT         66-Dy-165   164.9317  0.00E+00    8.25E-05
   684       LT         66-Dy-165m  164.9317  0.00E+00    9.19E-03
   685       LT         66-Dy-166   165.9328  0.00E+00    2.36E-06
   686       LT         67-Ho-160   159.9287  0.00E+00    4.51E-04
   687       LT         67-Ho-160m  159.9287  0.00E+00    3.84E-05
   688       LT         67-Ho-161   160.9279  0.00E+00    7.76E-05
   689       LT         67-Ho-163   162.9287  0.00E+00    4.81E-12
   690       LT         67-Ho-163m  162.9287  0.00E+00    6.36E-01
   691       LT         67-Ho-164   163.9302  0.00E+00    3.98E-04
   692       LT         67-Ho-164m  163.9302  0.00E+00    3.08E-04
   693       LT         67-Ho-165   164.9303  1.00E+02    0.00E+00
   694       LT         67-Ho-166   165.9323  0.00E+00    7.18E-06
   695       LT         67-Ho-166m  165.9324  0.00E+00    1.83E-11
   696       LT         68-Er-160   159.9291  0.00E+00    6.74E-06
   697       LT         68-Er-161   160.9300  0.00E+00    6.00E-05
   698       LT         68-Er-162   161.9288  1.39E-01    0.00E+00
   699       LT         68-Er-163   162.9300  0.00E+00    1.54E-04
   700       LT         68-Er-164   163.9292  1.60E+00    0.00E+00
   701       LT         68-Er-165   164.9307  0.00E+00    1.86E-05
   702       LT         68-Er-166   165.9303  3.35E+01    0.00E+00
   703       LT         68-Er-167   166.9321  2.29E+01    0.00E+00
   704       LT         68-Er-167m  166.9321  0.00E+00    3.05E-01
   705       LT         68-Er-168   167.9324  2.70E+01    0.00E+00
   706       LT         68-Er-169   168.9346  0.00E+00    8.54E-07
   707       LT         68-Er-170   169.9355  1.49E+01    0.00E+00
   708       LT         68-Er-171   170.9380  0.00E+00    2.56E-05
   709       LT         68-Er-172   171.9394  0.00E+00    3.91E-06
   710       LT         69-Tm-165   164.9324  0.00E+00    6.41E-06
   711       LT         69-Tm-166   165.9335  0.00E+00    2.50E-05
   712       LT         69-Tm-167   166.9328  0.00E+00    8.67E-07
   713       LT         69-Tm-168   167.9342  0.00E+00    8.62E-08
   714       LT         69-Tm-169   168.9342  1.00E+02    0.00E+00
   715       LT         69-Tm-170   169.9358  0.00E+00    6.24E-08
   716       LT         69-Tm-171   170.9364  0.00E+00    1.14E-08
   717       LT         69-Tm-172   171.9384  0.00E+00    3.03E-06
   718       LT         69-Tm-173   172.9396  0.00E+00    2.34E-05
   719       LT         70-Yb-166   165.9339  0.00E+00    3.40E-06
   720       LT         70-Yb-167   166.9350  0.00E+00    6.60E-04
   721       LT         70-Yb-168   167.9339  1.30E-01    0.00E+00
   722       LT         70-Yb-169   168.9352  0.00E+00    2.51E-07
   723       LT         70-Yb-170   169.9348  3.04E+00    0.00E+00
   724       LT         70-Yb-171   170.9363  1.43E+01    0.00E+00
   725       LT         70-Yb-172   171.9364  2.18E+01    0.00E+00
   726       LT         70-Yb-173   172.9382  1.61E+01    0.00E+00
   727       LT         70-Yb-174   173.9389  3.18E+01    0.00E+00
   728       LT         70-Yb-175   174.9413  0.00E+00    1.92E-06
   729       LT         70-Yb-175m  174.9413  0.00E+00    1.02E+01
   730       LT         70-Yb-176   175.9426  1.28E+01    0.00E+00
   731       LT         70-Yb-177   176.9453  0.00E+00    1.01E-04
   732       LT         71-Lu-169   168.9377  0.00E+00    5.65E-06
   733       LT         71-Lu-170   169.9385  0.00E+00    3.99E-06
   734       LT         71-Lu-171   170.9379  0.00E+00    9.74E-07
   735       LT         71-Lu-172   171.9391  0.00E+00    1.20E-06
   736       LT         71-Lu-172m  171.9391  0.00E+00    3.12E-03
   737       LT         71-Lu-173   172.9389  0.00E+00    1.60E-08
   738       LT         71-Lu-174   173.9403  0.00E+00    6.64E-09
   739       LT         71-Lu-174m  173.9403  0.00E+00    5.65E-08
   740       LT         71-Lu-175   174.9408  9.74E+01    0.00E+00
   741       LT         71-Lu-176   175.9427  2.59E+00    5.84E-19
   742       LT         71-Lu-176m  175.9427  0.00E+00    5.30E-05
   743       LT         71-Lu-177   176.9438  0.00E+00    1.21E-06
   744       LT         71-Lu-177m  176.9438  0.00E+00    5.00E-08
   745       LT         72-Hf-170   169.9396  0.00E+00    1.20E-05
   746       LT         72-Hf-171   170.9405  0.00E+00    1.59E-05
   747       LT         72-Hf-172   171.9395  0.00E+00    1.17E-08
   748       LT         72-Hf-173   172.9405  0.00E+00    8.16E-06
   749       LT         72-Hf-174   173.9400  1.60E-01    1.10E-23
   750       LT         72-Hf-175   174.9415  0.00E+00    1.15E-07
   751       LT         72-Hf-176   175.9414  5.26E+00    0.00E+00
   752       LT         72-Hf-177   176.9432  1.86E+01    0.00E+00
   753       LT         72-Hf-177m  176.9432  0.00E+00    6.36E-01
   754       LT         72-Hf-178   177.9437  2.73E+01    0.00E+00
   755       LT         72-Hf-178m  177.9437  0.00E+00    1.73E-01
   756       LT         72-Hf-179   178.9458  1.36E+01    0.00E+00
   757       LT         72-Hf-179m  178.9458  0.00E+00    3.71E-02
   758       LT         72-Hf-180   179.9465  3.51E+01    0.00E+00
   759       LT         72-Hf-180m  179.9465  0.00E+00    3.50E-05
   760       LT         72-Hf-181   180.9491  0.00E+00    1.89E-07
   761       LT         72-Hf-182   181.9505  0.00E+00    2.47E-15
   762       LT         73-Ta-177   176.9445  0.00E+00    3.40E-06
   763       LT         73-Ta-178   177.9458  0.00E+00    1.24E-03
   764       LT         73-Ta-179   178.9459  0.00E+00    1.21E-08
   765       LT         73-Ta-180m  179.9475  1.20E-02    0.00E+00
   766       LT         73-Ta-180   179.9475  0.00E+00    2.36E-05
   767       LT         73-Ta-181   180.9480  1.00E+02    0.00E+00
   768       LT         73-Ta-182   181.9501  0.00E+00    6.99E-08
   769       LT         73-Ta-182m  181.9501  0.00E+00    2.45E+00
   770       LT         73-Ta-183   182.9514  0.00E+00    1.57E-06
   771       LT         74-W-178    177.9459  0.00E+00    3.71E-07
   772       LT         74-W-180    179.9467  1.20E-01    1.22E-26
   773       LT         74-W-181    180.9482  0.00E+00    6.62E-08
   774       LT         74-W-182    181.9482  2.65E+01    0.00E+00
   775       LT         74-W-183m   182.9502  0.00E+00    1.33E-01
   776       LT         74-W-183    182.9502  1.43E+01    0.00E+00
   777       LT         74-W-184    183.9509  3.06E+01    0.00E+00
   778       LT         74-W-185    184.9534  0.00E+00    1.07E-07
   779       LT         74-W-185m   184.9534  0.00E+00    6.92E-03
   780       LT         74-W-186    185.9544  2.84E+01    1.29E-28
   781       LT         74-W-187    186.9572  0.00E+00    8.02E-06
   782       LT         74-W-188    187.9585  0.00E+00    1.15E-07
   783       LT         74-W-189    188.9619  0.00E+00    1.08E-03
   784       LT         75-Re-181   180.9501  0.00E+00    9.68E-06
   785       LT         75-Re-182   181.9512  0.00E+00    3.01E-06
   786       LT         75-Re-182m  181.9512  0.00E+00    1.52E-05
   787       LT         75-Re-183   182.9508  0.00E+00    1.15E-07
   788       LT         75-Re-184   183.9525  0.00E+00    2.27E-07
   789       LT         75-Re-184m  183.9525  0.00E+00    4.75E-08
   790       LT         75-Re-185   184.9530  3.74E+01    0.00E+00
   791       LT         75-Re-186   185.9550  0.00E+00    2.16E-06
   792       LT         75-Re-186m  185.9550  0.00E+00    1.10E-13
   793       LT         75-Re-187   186.9557  6.26E+01    5.07E-19
   794       LT         75-Re-188   187.9581  0.00E+00    1.13E-05
   795       LT         75-Re-188m  187.9581  0.00E+00    6.21E-04
   796       LT         75-Re-189   188.9592  0.00E+00    7.92E-06
   797       LT         76-Os-182   181.9521  0.00E+00    8.82E-06
   798       LT         76-Os-183   182.9531  0.00E+00    1.48E-05
   799       LT         76-Os-184   183.9525  2.00E-02    0.00E+00
   800       LT         76-Os-185   184.9540  0.00E+00    8.57E-08
   801       LT         76-Os-186   185.9538  1.59E+00    1.10E-23
   802       LT         76-Os-187   186.9557  1.96E+00    0.00E+00
   803       LT         76-Os-188   187.9558  1.32E+01    0.00E+00
   804       LT         76-Os-189   188.9581  1.62E+01    0.00E+00
   805       LT         76-Os-189m  188.9581  0.00E+00    3.31E-05
   806       LT         76-Os-190   189.9585  2.63E+01    0.00E+00
   807       LT         76-Os-190m  189.9585  0.00E+00    1.17E-03
   808       LT         76-Os-191   190.9609  0.00E+00    5.21E-07
   809       LT         76-Os-191m  190.9609  0.00E+00    1.47E-05
   810       LT         76-Os-192   191.9615  4.08E+01    0.00E+00
   811       LT         76-Os-193   192.9642  0.00E+00    6.39E-06
   812       LT         76-Os-194   193.9652  0.00E+00    3.66E-09
   813       LT         77-Ir-185   184.9567  0.00E+00    1.34E-05
   814       LT         77-Ir-186   185.9579  0.00E+00    1.16E-05
   815       LT         77-Ir-188   187.9588  0.00E+00    4.64E-06
   816       LT         77-Ir-189   188.9587  0.00E+00    6.08E-07
   817       LT         77-Ir-189m  188.9587  0.00E+00    5.21E+01
   818       LT         77-Ir-190   189.9606  0.00E+00    6.81E-07
   819       LT         77-Ir-191   190.9606  3.73E+01    0.00E+00
   820       LT         77-Ir-191m  190.9606  0.00E+00    1.41E-01
   821       LT         77-Ir-192   191.9626  0.00E+00    1.09E-07
   822       LT         77-Ir-192m  191.9626  0.00E+00    7.97E-03
   823       LT         77-Ir-193   192.9629  6.27E+01    0.00E+00
   824       LT         77-Ir-193m  192.9629  0.00E+00    7.62E-07
   825       LT         77-Ir-194   193.9651  0.00E+00    9.99E-06
   826       LT         77-Ir-194m  193.9651  0.00E+00    2.18E+01
   827       LT         77-Ir-196   195.9684  0.00E+00    1.33E-02
   828       LT         77-Ir-196m  195.9684  0.00E+00    1.38E-04
   829       LT         78-Pt-188   187.9594  0.00E+00    7.87E-07
   830       LT         78-Pt-189   188.9608  0.00E+00    1.77E-05
   831       LT         78-Pt-190   189.9599  1.40E-02    3.38E-20
   832       LT         78-Pt-191   190.9617  0.00E+00    2.86E-06
   833       LT         78-Pt-192   191.9610  7.82E-01    0.00E+00
   834       LT         78-Pt-193   192.9630  0.00E+00    4.39E-10
   835       LT         78-Pt-193m  192.9630  0.00E+00    1.85E-06
   836       LT         78-Pt-194   193.9627  3.30E+01    0.00E+00
   837       LT         78-Pt-195   194.9648  3.38E+01    0.00E+00
   838       LT         78-Pt-195m  194.9648  0.00E+00    2.00E-06
   839       LT         78-Pt-196   195.9650  2.52E+01    0.00E+00
   840       LT         78-Pt-197   196.9673  0.00E+00    9.68E-06
   841       LT         78-Pt-197m  196.9673  0.00E+00    1.21E-04
   842       LT         78-Pt-198   197.9679  7.16E+00    0.00E+00
   843       LT         78-Pt-199   198.9706  0.00E+00    3.75E-04
   844       LT         78-Pt-199m  198.9706  0.00E+00    5.10E-02
   845       LT         78-Pt-200   199.9714  0.00E+00    1.53E-05
   846       LT         79-Au-193   192.9642  0.00E+00    1.09E-05
   847       LT         79-Au-194   193.9654  0.00E+00    5.06E-06
   848       LT         79-Au-195   194.9650  0.00E+00    4.31E-08
   849       LT         79-Au-195m  194.9650  0.00E+00    2.27E-02
   850       LT         79-Au-196   195.9666  0.00E+00    1.30E-06
   851       LT         79-Au-197   196.9666  1.00E+02    0.00E+00
   852       LT         79-Au-197m  196.9666  0.00E+00    8.97E-02
   853       LT         79-Au-198   197.9682  0.00E+00    2.98E-06
   854       LT         79-Au-198m  197.9682  0.00E+00    3.53E-06
   855       LT         79-Au-199   198.9688  0.00E+00    2.56E-06
   856       LT         79-Au-200   199.9707  0.00E+00    2.39E-04
   857       LT         79-Au-200m  199.9707  0.00E+00    1.03E-05
   858       LT         80-Hg-193   192.9667  0.00E+00    5.07E-05
   859       LT         80-Hg-193m  192.9667  0.00E+00    1.63E-05
   860       LT         80-Hg-194   193.9654  0.00E+00    4.95E-11
   861       LT         80-Hg-195   194.9667  0.00E+00    1.83E-05
   862       LT         80-Hg-195m  194.9667  0.00E+00    4.63E-06
   863       LT         80-Hg-196   195.9658  1.50E-01    0.00E+00
   864       LT         80-Hg-197   196.9672  0.00E+00    3.00E-06
   865       LT         80-Hg-197m  196.9672  0.00E+00    8.09E-06
   866       LT         80-Hg-198   197.9668  9.97E+00    0.00E+00
   867       LT         80-Hg-199   198.9683  1.69E+01    0.00E+00
   868       LT         80-Hg-199m  198.9683  0.00E+00    2.71E-04
   869       LT         80-Hg-200   199.9683  2.31E+01    0.00E+00
   870       LT         80-Hg-201   200.9703  1.32E+01    0.00E+00
   871       LT         80-Hg-202   201.9706  2.99E+01    0.00E+00
   872       LT         80-Hg-203   202.9729  0.00E+00    1.72E-07
   873       LT         80-Hg-204   203.9735  6.87E+00    0.00E+00
   874       LT         80-Hg-205   204.9761  0.00E+00    2.25E-03
   875       LT         80-Hg-206   205.9775  0.00E+00    1.39E-03
   876       LT         81-Tl-200   199.9710  0.00E+00    7.38E-06
   877       LT         81-Tl-201   200.9708  0.00E+00    2.64E-06
   878       LT         81-Tl-202   201.9721  0.00E+00    6.52E-07
   879       LT         81-Tl-203   202.9723  2.95E+01    0.00E+00
   880       LT         81-Tl-204   203.9739  0.00E+00    5.81E-09
   881       LT         81-Tl-205   204.9744  7.05E+01    0.00E+00
   882       LT         81-Tl-206   205.9761  0.00E+00    2.75E-03
   883       LT         81-Tl-207   206.9774  0.00E+00    2.42E-03
   884       LT         82-Pb-200   199.9718  0.00E+00    8.96E-06
   885       LT         82-Pb-202   201.9722  0.00E+00    4.18E-13
   886       LT         82-Pb-203   202.9734  0.00E+00    3.71E-06
   887       LT         82-Pb-204   203.9730  1.40E+00    1.58E-25
   888       LT         82-Pb-205   204.9745  0.00E+00    1.27E-15
   889       LT         82-Pb-205m  204.9745  0.00E+00    1.25E+02
   890       LT         82-Pb-206   205.9745  2.41E+01    0.00E+00
   891       LT         82-Pb-207   206.9759  2.21E+01    0.00E+00
   892       LT         82-Pb-207m  206.9759  0.00E+00    8.60E-01
   893       LT         82-Pb-208   207.9767  5.24E+01    0.00E+00
   894       LT         82-Pb-209   208.9811  0.00E+00    5.92E-05
   895       LT         82-Pb-210   209.9842  0.00E+00    9.89E-10
   896       LT         83-Bi-205   204.9774  0.00E+00    5.24E-07
   897       LT         83-Bi-206   205.9785  0.00E+00    1.29E-06
   898       LT         83-Bi-207   206.9785  0.00E+00    6.96E-10
   899       LT         83-Bi-208   207.9797  0.00E+00    5.97E-14
   900       LT         83-Bi-209   208.9804  1.00E+02    1.16E-27
   901       LT         83-Bi-210   209.9841  0.00E+00    1.60E-06
   902       LT         83-Bi-210m  209.9841  0.00E+00    7.23E-15
   903       LT         83-Bi-211   210.9873  0.00E+00    5.40E-03
   904       LT         84-Po-206   205.9805  0.00E+00    9.12E-07
   905       LT         84-Po-207   206.9816  0.00E+00    3.32E-05
   906       LT         84-Po-208   207.9812  0.00E+00    7.58E-09
   907       LT         84-Po-209   208.9824  0.00E+00    2.15E-10
   908       LT         84-Po-210   209.9829  0.00E+00    5.80E-08
   909       LT         84-Po-211   210.9866  0.00E+00    1.34E+00
   910       LT         84-Po-211m  210.9866  0.00E+00    2.75E-02
   911       AC         2-He-3      3.0160    0.00E+00    0.00E+00
   912       AC         2-He-4      4.0026    0.00E+00    0.00E+00
   913       AC         3-Li-6      6.0151    0.00E+00    0.00E+00
   914       AC         3-Li-7      7.0160    0.00E+00    0.00E+00
   915       AC         4-Be-7      7.0169    0.00E+00    1.51E-07
   916       AC         6-C-12      12.0000   0.00E+00    0.00E+00
   917       AC         80-Hg-206   205.9775  0.00E+00    1.39E-03
   918       AC         81-Tl-203   202.9723  0.00E+00    0.00E+00
   919       AC         81-Tl-205   204.9744  0.00E+00    0.00E+00
   920       AC         81-Tl-206   205.9761  0.00E+00    2.75E-03
   921       AC         81-Tl-207   206.9774  0.00E+00    2.42E-03
   922       AC         81-Tl-208   207.9820  0.00E+00    3.78E-03
   923       AC         81-Tl-209   208.9854  0.00E+00    5.25E-03
   924       AC         81-Tl-210   209.9901  0.00E+00    8.89E-03
   925       AC         82-Pb-203   202.9734  0.00E+00    3.71E-06
   926       AC         82-Pb-204   203.9730  0.00E+00    1.58E-25
   927       AC         82-Pb-205   204.9745  0.00E+00    1.27E-15
   928       AC         82-Pb-206   205.9745  0.00E+00    0.00E+00
   929       AC         82-Pb-207   206.9759  0.00E+00    0.00E+00
   930       AC         82-Pb-207m  206.9759  0.00E+00    8.60E-01
   931       AC         82-Pb-208   207.9767  0.00E+00    0.00E+00
   932       AC         82-Pb-209   208.9811  0.00E+00    5.92E-05
   933       AC         82-Pb-210   209.9842  0.00E+00    9.89E-10
   934       AC         82-Pb-211   210.9887  0.00E+00    3.20E-04
   935       AC         82-Pb-212   211.9919  0.00E+00    1.81E-05
   936       AC         82-Pb-214   213.9998  0.00E+00    4.31E-04
   937       AC         83-Bi-206   205.9785  0.00E+00    1.29E-06
   938       AC         83-Bi-207   206.9785  0.00E+00    6.96E-10
   939       AC         83-Bi-208   207.9797  0.00E+00    5.97E-14
   940       AC         83-Bi-209   208.9804  0.00E+00    1.16E-27
   941       AC         83-Bi-210m  209.9841  0.00E+00    7.23E-15
   942       AC         83-Bi-210   209.9841  0.00E+00    1.60E-06
   943       AC         83-Bi-211   210.9873  0.00E+00    5.40E-03
   944       AC         83-Bi-212   211.9913  0.00E+00    1.91E-04
   945       AC         83-Bi-212m  211.9913  0.00E+00    4.62E-04
   946       AC         83-Bi-213   212.9944  0.00E+00    2.53E-04
   947       AC         83-Bi-214   213.9987  0.00E+00    5.81E-04
   948       AC         84-Po-207   206.9816  0.00E+00    3.32E-05
   949       AC         84-Po-208   207.9812  0.00E+00    7.58E-09
   950       AC         84-Po-209   208.9824  0.00E+00    2.15E-10
   951       AC         84-Po-210   209.9829  0.00E+00    5.80E-08
   952       AC         84-Po-211m  210.9866  0.00E+00    2.75E-02
   953       AC         84-Po-211   210.9866  0.00E+00    1.34E+00
   954       AC         84-Po-212   211.9889  0.00E+00    6.93E+02
   955       AC         84-Po-213   212.9929  0.00E+00    6.93E+02
   956       AC         84-Po-214   213.9952  0.00E+00    6.93E+02
   957       AC         84-Po-215   214.9994  0.00E+00    3.89E+02
   958       AC         84-Po-216   216.0019  0.00E+00    4.78E+00
   959       AC         84-Po-218   218.0090  0.00E+00    3.73E-03
   960       AC         85-At-216   216.0024  0.00E+00    6.93E+02
   961       AC         85-At-217   217.0047  0.00E+00    2.15E+01
   962       AC         85-At-218   218.0087  0.00E+00    4.62E-01
   963       AC         86-Rn-216   216.0003  0.00E+00    6.93E+02
   964       AC         86-Rn-217   217.0039  0.00E+00    6.93E+02
   965       AC         86-Rn-218   218.0056  0.00E+00    1.98E+01
   966       AC         86-Rn-219   219.0095  0.00E+00    1.75E-01
   967       AC         86-Rn-220   220.0114  0.00E+00    1.25E-02
   968       AC         86-Rn-222   222.0176  0.00E+00    2.10E-06
   969       AC         87-Fr-220   220.0123  0.00E+00    2.53E-02
   970       AC         87-Fr-221   221.0143  0.00E+00    2.36E-03
   971       AC         87-Fr-222   222.0175  0.00E+00    8.14E-04
   972       AC         87-Fr-223   223.0197  0.00E+00    5.25E-04
   973       AC         88-Ra-220   220.0110  0.00E+00    3.85E+01
   974       AC         88-Ra-222   222.0154  0.00E+00    1.92E-02
   975       AC         88-Ra-223   223.0185  0.00E+00    7.02E-07
   976       AC         88-Ra-224   224.0202  0.00E+00    2.19E-06
   977       AC         88-Ra-225   225.0236  0.00E+00    5.38E-07
   978       AC         88-Ra-226   226.0254  0.00E+00    1.37E-11
   979       AC         88-Ra-227   227.0292  0.00E+00    2.74E-04
   980       AC         88-Ra-228   228.0311  0.00E+00    3.82E-09
   981       AC         89-Ac-224   224.0217  0.00E+00    6.93E-05
   982       AC         89-Ac-225   225.0232  0.00E+00    8.02E-07
   983       AC         89-Ac-226   226.0261  0.00E+00    6.56E-06
   984       AC         89-Ac-227   227.0278  0.00E+00    1.01E-09
   985       AC         89-Ac-228   228.0310  0.00E+00    3.13E-05
   986       AC         90-Th-226   226.0249  0.00E+00    3.78E-04
   987       AC         90-Th-227   227.0277  0.00E+00    4.29E-07
   988       AC         90-Th-228   228.0287  0.00E+00    1.15E-08
   989       AC         90-Th-229   229.0318  0.00E+00    2.99E-12
   990       AC         90-Th-230   230.0331  0.00E+00    2.91E-13
   991       AC         90-Th-231   231.0363  0.00E+00    7.55E-06
   992       AC         90-Th-232   232.0381  0.00E+00    1.56E-18
   993       AC         90-Th-233   233.0416  0.00E+00    5.18E-04
   994       AC         90-Th-234   234.0436  0.00E+00    3.33E-07
   995       AC         91-Pa-228   228.0311  0.00E+00    8.75E-06
   996       AC         91-Pa-229   229.0321  0.00E+00    5.35E-06
   997       AC         91-Pa-230   230.0345  0.00E+00    4.61E-07
   998       AC         91-Pa-231   231.0359  0.00E+00    6.70E-13
   999       AC         91-Pa-232   232.0386  0.00E+00    6.08E-06
   1000      AC         91-Pa-233   233.0403  0.00E+00    2.97E-07
   1001      AC         91-Pa-234m  234.0433  0.00E+00    9.97E-03
   1002      AC         91-Pa-234   234.0433  0.00E+00    2.87E-05
   1003      AC         91-Pa-235   235.0454  0.00E+00    4.73E-04
   1004      AC         92-U-230    230.0339  0.00E+00    3.86E-07
   1005      AC         92-U-231    231.0363  0.00E+00    1.91E-06
   1006      AC         92-U-232    232.0372  0.00E+00    3.19E-10
   1007      AC         92-U-233    233.0396  0.00E+00    1.38E-13
   1008      AC         92-U-234    234.0410  0.00E+00    8.95E-14
   1009      AC         92-U-235    235.0439  0.00E+00    3.12E-17
   1010      AC         92-U-235m   235.0439  0.00E+00    4.44E-04
   1011      AC         92-U-236    236.0456  0.00E+00    9.38E-16
   1012      AC         92-U-237    237.0487  0.00E+00    1.19E-06
   1013      AC         92-U-238    238.0508  0.00E+00    4.92E-18
   1014      AC         92-U-239    239.0543  0.00E+00    4.93E-04
   1015      AC         92-U-240    240.0566  0.00E+00    1.37E-05
   1016      AC         92-U-241    241.0603  0.00E+00    2.31E-03
   1017      AC         93-Np-234   234.0429  0.00E+00    1.82E-06
   1018      AC         93-Np-235   235.0441  0.00E+00    2.03E-08
   1019      AC         93-Np-236m  236.0466  0.00E+00    8.56E-06
   1020      AC         93-Np-236   236.0466  0.00E+00    1.44E-13
   1021      AC         93-Np-237   237.0482  0.00E+00    1.02E-14
   1022      AC         93-Np-238   238.0509  0.00E+00    3.79E-06
   1023      AC         93-Np-239   239.0529  0.00E+00    3.41E-06
   1024      AC         93-Np-240m  240.0562  0.00E+00    1.60E-03
   1025      AC         93-Np-240   240.0562  0.00E+00    1.87E-04
   1026      AC         93-Np-241   241.0582  0.00E+00    8.31E-04
   1027      AC         94-Pu-236   236.0461  0.00E+00    7.69E-09
   1028      AC         94-Pu-237m  237.0484  0.00E+00    3.85E+00
   1029      AC         94-Pu-237   237.0484  0.00E+00    1.76E-07
   1030      AC         94-Pu-238   238.0496  0.00E+00    2.50E-10
   1031      AC         94-Pu-239   239.0522  0.00E+00    9.11E-13
   1032      AC         94-Pu-240   240.0538  0.00E+00    3.35E-12
   1033      AC         94-Pu-241   241.0569  0.00E+00    1.54E-09
   1034      AC         94-Pu-242   242.0587  0.00E+00    5.88E-14
   1035      AC         94-Pu-243   243.0620  0.00E+00    3.89E-05
   1036      AC         94-Pu-244   244.0642  0.00E+00    2.71E-16
   1037      AC         94-Pu-245   245.0677  0.00E+00    1.83E-05
   1038      AC         94-Pu-246   246.0702  0.00E+00    7.40E-07
   1039      AC         94-Pu-247   247.0741  0.00E+00    3.53E-06
   1040      AC         95-Am-239   239.0530  0.00E+00    1.62E-05
   1041      AC         95-Am-240   240.0553  0.00E+00    3.79E-06
   1042      AC         95-Am-241   241.0568  0.00E+00    5.08E-11
   1043      AC         95-Am-242m  242.0595  0.00E+00    1.56E-10
   1044      AC         95-Am-242   242.0596  0.00E+00    1.20E-05
   1045      AC         95-Am-243   243.0614  0.00E+00    2.98E-12
   1046      AC         95-Am-244m  244.0646  0.00E+00    4.44E-04
   1047      AC         95-Am-244   244.0643  0.00E+00    1.91E-05
   1048      AC         95-Am-245   245.0665  0.00E+00    9.39E-05
   1049      AC         95-Am-246   246.0698  0.00E+00    2.96E-04
   1050      AC         95-Am-246m  246.0698  0.00E+00    4.62E-04
   1051      AC         95-Am-247   247.0721  0.00E+00    5.02E-04
   1052      AC         96-Cm-240   240.0555  0.00E+00    2.97E-07
   1053      AC         96-Cm-241   241.0576  0.00E+00    2.45E-07
   1054      AC         96-Cm-242   242.0588  0.00E+00    4.92E-08
   1055      AC         96-Cm-243   243.0614  0.00E+00    7.55E-10
   1056      AC         96-Cm-244   244.0627  0.00E+00    1.21E-09
   1057      AC         96-Cm-245   245.0655  0.00E+00    2.58E-12
   1058      AC         96-Cm-246   246.0672  0.00E+00    4.61E-12
   1059      AC         96-Cm-247   247.0703  0.00E+00    1.41E-15
   1060      AC         96-Cm-248   248.0724  0.00E+00    6.31E-14
   1061      AC         96-Cm-249   249.0759  0.00E+00    1.80E-04
   1062      AC         96-Cm-250   250.0784  0.00E+00    2.65E-12
   1063      AC         96-Cm-251   251.0823  0.00E+00    6.88E-04
   1064      AC         97-Bk-245   245.0664  0.00E+00    1.62E-06
   1065      AC         97-Bk-246   246.0687  0.00E+00    4.46E-06
   1066      AC         97-Bk-247   247.0703  0.00E+00    1.59E-11
   1067      AC         97-Bk-248   248.0731  0.00E+00    2.44E-09
   1068      AC         97-Bk-248m  248.0731  0.00E+00    8.12E-06
   1069      AC         97-Bk-249   249.0750  0.00E+00    2.51E-08
   1070      AC         97-Bk-250   250.0783  0.00E+00    5.99E-05
   1071      AC         97-Bk-251   251.0808  0.00E+00    2.08E-04
   1072      AC         98-Cf-246   246.0688  0.00E+00    5.39E-06
   1073      AC         98-Cf-248   248.0722  0.00E+00    2.41E-08
   1074      AC         98-Cf-249   249.0748  0.00E+00    6.26E-11
   1075      AC         98-Cf-250   250.0764  0.00E+00    1.68E-09
   1076      AC         98-Cf-251   251.0796  0.00E+00    2.45E-11
   1077      AC         98-Cf-252   252.0816  0.00E+00    8.30E-09
   1078      AC         98-Cf-253   253.0851  0.00E+00    4.50E-07
   1079      AC         98-Cf-254   254.0873  0.00E+00    1.33E-07
   1080      AC         98-Cf-255   255.0910  0.00E+00    1.36E-04
   1081      AC         99-Es-251   251.0800  0.00E+00    5.83E-06
   1082      AC         99-Es-252   252.0830  0.00E+00    1.70E-08
   1083      AC         99-Es-253   253.0848  0.00E+00    3.92E-07
   1084      AC         99-Es-254m  254.0880  0.00E+00    4.90E-06
   1085      AC         99-Es-254   254.0880  0.00E+00    2.91E-08
   1086      AC         99-Es-255   255.0903  0.00E+00    2.02E-07
   1087      FP         1-H-3       3.0161    0.00E+00    1.78E-09
   1088      FP         2-He-3      3.0160    0.00E+00    0.00E+00
   1089      FP         2-He-4      4.0026    0.00E+00    0.00E+00
   1090      FP         26-Fe-65    64.9454   0.00E+00    8.56E-01
   1091      FP         27-Co-65    64.9365   0.00E+00    5.98E-01
   1092      FP         28-Ni-65    64.9301   0.00E+00    7.65E-05
   1093      FP         29-Cu-65    64.9278   0.00E+00    0.00E+00
   1094      FP         24-Cr-66    65.9734   0.00E+00    6.93E+01
   1095      FP         25-Mn-66    65.9611   0.00E+00    1.08E+01
   1096      FP         26-Fe-66    65.9468   0.00E+00    1.58E+00
   1097      FP         27-Co-66    65.9398   0.00E+00    3.47E+00
   1098      FP         28-Ni-66    65.9291   0.00E+00    3.53E-06
   1099      FP         29-Cu-66    65.9289   0.00E+00    2.26E-03
   1100      FP         30-Zn-66    65.9260   0.00E+00    0.00E+00
   1101      FP         31-Ga-66    65.9316   0.00E+00    2.03E-05
   1102      FP         32-Ge-66    65.9338   0.00E+00    8.52E-05
   1103      FP         24-Cr-67    66.9796   0.00E+00    1.39E+01
   1104      FP         25-Mn-67    66.9641   0.00E+00    1.47E+01
   1105      FP         26-Fe-67    66.9510   0.00E+00    1.67E+00
   1106      FP         27-Co-67    66.9409   0.00E+00    1.63E+00
   1107      FP         28-Ni-67    66.9316   0.00E+00    3.30E-02
   1108      FP         29-Cu-67    66.9277   0.00E+00    3.11E-06
   1109      FP         30-Zn-67    66.9271   0.00E+00    0.00E+00
   1110      FP         31-Ga-67    66.9282   0.00E+00    2.46E-06
   1111      FP         32-Ge-67    66.9327   0.00E+00    6.11E-04
   1112      FP         25-Mn-68    67.9693   0.00E+00    2.48E+01
   1113      FP         26-Fe-68    67.9537   0.00E+00    3.71E+00
   1114      FP         27-Co-68    67.9449   0.00E+00    3.48E+00
   1115      FP         28-Ni-68    67.9319   0.00E+00    2.39E-02
   1116      FP         29-Cu-68    67.9296   0.00E+00    2.23E-02
   1117      FP         29-Cu-68m   67.9296   0.00E+00    3.08E-03
   1118      FP         30-Zn-68    67.9248   0.00E+00    0.00E+00
   1119      FP         31-Ga-68    67.9280   0.00E+00    1.71E-04
   1120      FP         32-Ge-68    67.9281   0.00E+00    2.96E-08
   1121      FP         25-Mn-69    68.9728   0.00E+00    4.95E+01
   1122      FP         26-Fe-69    68.9588   0.00E+00    6.36E+00
   1123      FP         27-Co-69    68.9463   0.00E+00    3.15E+00
   1124      FP         28-Ni-69    68.9356   0.00E+00    6.08E-02
   1125      FP         29-Cu-69    68.9294   0.00E+00    4.05E-03
   1126      FP         30-Zn-69    68.9266   0.00E+00    2.05E-04
   1127      FP         30-Zn-69m   68.9266   0.00E+00    1.40E-05
   1128      FP         31-Ga-69    68.9256   0.00E+00    0.00E+00
   1129      FP         32-Ge-69    68.9280   0.00E+00    4.93E-06
   1130      FP         33-As-69    68.9323   0.00E+00    7.59E-04
   1131      FP         26-Fe-70    69.9615   0.00E+00    7.37E+00
   1132      FP         27-Co-70    69.9510   0.00E+00    5.82E+00
   1133      FP         28-Ni-70    69.9365   0.00E+00    1.16E-01
   1134      FP         29-Cu-70    69.9324   0.00E+00    1.56E-02
   1135      FP         29-Cu-70m   69.9324   0.00E+00    2.10E-02
   1136      FP         30-Zn-70    69.9253   0.00E+00    0.00E+00
   1137      FP         31-Ga-70    69.9260   0.00E+00    5.46E-04
   1138      FP         32-Ge-70    69.9242   0.00E+00    0.00E+00
   1139      FP         26-Fe-71    70.9667   0.00E+00    2.48E+01
   1140      FP         27-Co-71    70.9529   0.00E+00    8.77E+00
   1141      FP         28-Ni-71    70.9407   0.00E+00    2.71E-01
   1142      FP         29-Cu-71    70.9327   0.00E+00    3.55E-02
   1143      FP         30-Zn-71    70.9277   0.00E+00    4.72E-03
   1144      FP         30-Zn-71m   70.9277   0.00E+00    4.86E-05
   1145      FP         31-Ga-71    70.9247   0.00E+00    0.00E+00
   1146      FP         32-Ge-71    70.9249   0.00E+00    7.02E-07
   1147      FP         32-Ge-71m   70.9249   0.00E+00    3.40E+01
   1148      FP         33-As-71    70.9271   0.00E+00    2.95E-06
   1149      FP         26-Fe-72    71.9696   0.00E+00    6.93E+02
   1150      FP         27-Co-72    71.9578   0.00E+00    1.16E+01
   1151      FP         28-Ni-72    71.9421   0.00E+00    4.42E-01
   1152      FP         29-Cu-72    71.9358   0.00E+00    1.05E-01
   1153      FP         30-Zn-72    71.9269   0.00E+00    4.14E-06
   1154      FP         31-Ga-72    71.9264   0.00E+00    1.37E-05
   1155      FP         31-Ga-72m   71.9264   0.00E+00    1.75E+01
   1156      FP         32-Ge-72    71.9221   0.00E+00    0.00E+00
   1157      FP         33-As-72    71.9268   0.00E+00    7.41E-06
   1158      FP         34-Se-72    71.9271   0.00E+00    9.55E-07
   1159      FP         27-Co-73    72.9602   0.00E+00    1.69E+01
   1160      FP         28-Ni-73    72.9465   0.00E+00    8.25E-01
   1161      FP         29-Cu-73    72.9367   0.00E+00    1.65E-01
   1162      FP         30-Zn-73    72.9298   0.00E+00    2.95E-02
   1163      FP         31-Ga-73    72.9252   0.00E+00    3.96E-05
   1164      FP         32-Ge-73    72.9235   0.00E+00    0.00E+00
   1165      FP         32-Ge-73m   72.9235   0.00E+00    1.39E+00
   1166      FP         33-As-73    72.9238   0.00E+00    9.99E-08
   1167      FP         34-Se-73    72.9268   0.00E+00    2.69E-05
   1168      FP         34-Se-73m   72.9268   0.00E+00    2.90E-04
   1169      FP         27-Co-74    73.9654   0.00E+00    2.31E+01
   1170      FP         28-Ni-74    73.9481   0.00E+00    1.02E+00
   1171      FP         29-Cu-74    73.9399   0.00E+00    3.96E-01
   1172      FP         30-Zn-74    73.9295   0.00E+00    7.25E-03
   1173      FP         31-Ga-74    73.9269   0.00E+00    1.42E-03
   1174      FP         31-Ga-74m   73.9269   0.00E+00    7.30E-02
   1175      FP         32-Ge-74    73.9212   0.00E+00    0.00E+00
   1176      FP         33-As-74    73.9239   0.00E+00    4.51E-07
   1177      FP         34-Se-74    73.9225   0.00E+00    0.00E+00
   1178      FP         27-Co-75    74.9683   0.00E+00    2.04E+01
   1179      FP         28-Ni-75    74.9529   0.00E+00    1.16E+00
   1180      FP         29-Cu-75    74.9419   0.00E+00    5.66E-01
   1181      FP         30-Zn-75    74.9329   0.00E+00    6.80E-02
   1182      FP         31-Ga-75    74.9265   0.00E+00    5.50E-03
   1183      FP         32-Ge-75    74.9229   0.00E+00    1.40E-04
   1184      FP         32-Ge-75m   74.9229   0.00E+00    1.45E-02
   1185      FP         33-As-75    74.9216   0.00E+00    0.00E+00
   1186      FP         33-As-75m   74.9216   0.00E+00    3.93E+01
   1187      FP         34-Se-75    74.9225   0.00E+00    6.70E-08
   1188      FP         35-Br-75    74.9258   0.00E+00    1.19E-04
   1189      FP         28-Ni-76    75.9553   0.00E+00    2.91E+00
   1190      FP         29-Cu-76    75.9453   0.00E+00    1.06E+00
   1191      FP         30-Zn-76    75.9333   0.00E+00    1.22E-01
   1192      FP         31-Ga-76    75.9288   0.00E+00    2.13E-02
   1193      FP         32-Ge-76    75.9214   0.00E+00    0.00E+00
   1194      FP         33-As-76    75.9224   0.00E+00    7.34E-06
   1195      FP         34-Se-76    75.9192   0.00E+00    0.00E+00
   1196      FP         28-Ni-77    76.9605   0.00E+00    1.14E+01
   1197      FP         29-Cu-77    76.9479   0.00E+00    1.48E+00
   1198      FP         30-Zn-77    76.9370   0.00E+00    3.33E-01
   1199      FP         31-Ga-77    76.9292   0.00E+00    5.25E-02
   1200      FP         32-Ge-77    76.9236   0.00E+00    1.70E-05
   1201      FP         32-Ge-77m   76.9236   0.00E+00    1.31E-02
   1202      FP         33-As-77    76.9206   0.00E+00    4.96E-06
   1203      FP         34-Se-77    76.9199   0.00E+00    0.00E+00
   1204      FP         34-Se-77m   76.9199   0.00E+00    3.99E-02
   1205      FP         35-Br-77    76.9214   0.00E+00    3.38E-06
   1206      FP         35-Br-77m   76.9214   0.00E+00    2.70E-03
   1207      FP         36-Kr-77    76.9247   0.00E+00    1.55E-04
   1208      FP         28-Ni-78    77.9632   0.00E+00    6.30E+00
   1209      FP         29-Cu-78    77.9520   0.00E+00    2.07E+00
   1210      FP         30-Zn-78    77.9384   0.00E+00    4.72E-01
   1211      FP         31-Ga-78    77.9316   0.00E+00    1.36E-01
   1212      FP         32-Ge-78    77.9229   0.00E+00    1.31E-04
   1213      FP         33-As-78    77.9218   0.00E+00    1.27E-04
   1214      FP         34-Se-78    77.9173   0.00E+00    0.00E+00
   1215      FP         35-Br-78    77.9212   0.00E+00    1.79E-03
   1216      FP         36-Kr-78    77.9204   0.00E+00    0.00E+00
   1217      FP         29-Cu-79    78.9546   0.00E+00    3.69E+00
   1218      FP         30-Zn-79    78.9426   0.00E+00    6.97E-01
   1219      FP         31-Ga-79    78.9329   0.00E+00    2.43E-01
   1220      FP         32-Ge-79    78.9254   0.00E+00    3.65E-02
   1221      FP         32-Ge-79m   78.9254   0.00E+00    1.78E-02
   1222      FP         33-As-79    78.9210   0.00E+00    1.28E-03
   1223      FP         34-Se-79    78.9185   0.00E+00    7.45E-14
   1224      FP         34-Se-79m   78.9185   0.00E+00    2.95E-03
   1225      FP         35-Br-79    78.9183   0.00E+00    0.00E+00
   1226      FP         35-Br-79m   78.9183   0.00E+00    1.43E-01
   1227      FP         36-Kr-79    78.9201   0.00E+00    5.49E-06
   1228      FP         36-Kr-79m   78.9201   0.00E+00    1.39E-02
   1229      FP         37-Rb-79    78.9240   0.00E+00    5.04E-04
   1230      FP         29-Cu-80    79.9609   0.00E+00    4.08E+00
   1231      FP         30-Zn-80    79.9443   0.00E+00    1.28E+00
   1232      FP         31-Ga-80    79.9365   0.00E+00    4.14E-01
   1233      FP         32-Ge-80    79.9254   0.00E+00    2.35E-02
   1234      FP         33-As-80    79.9225   0.00E+00    4.56E-02
   1235      FP         34-Se-80    79.9165   0.00E+00    0.00E+00
   1236      FP         35-Br-80    79.9185   0.00E+00    6.53E-04
   1237      FP         35-Br-80m   79.9185   0.00E+00    4.36E-05
   1238      FP         36-Kr-80    79.9164   0.00E+00    0.00E+00
   1239      FP         30-Zn-81    80.9505   0.00E+00    2.17E+00
   1240      FP         31-Ga-81    80.9378   0.00E+00    5.70E-01
   1241      FP         32-Ge-81    80.9288   0.00E+00    9.12E-02
   1242      FP         32-Ge-81m   80.9288   0.00E+00    9.12E-02
   1243      FP         33-As-81    80.9221   0.00E+00    2.08E-02
   1244      FP         34-Se-81    80.9180   0.00E+00    6.26E-04
   1245      FP         34-Se-81m   80.9180   0.00E+00    2.02E-04
   1246      FP         35-Br-81    80.9163   0.00E+00    0.00E+00
   1247      FP         36-Kr-81    80.9166   0.00E+00    9.59E-14
   1248      FP         36-Kr-81m   80.9166   0.00E+00    5.29E-02
   1249      FP         37-Rb-81    80.9190   0.00E+00    4.21E-05
   1250      FP         30-Zn-82    81.9544   0.00E+00    1.33E+01
   1251      FP         31-Ga-82    81.9430   0.00E+00    1.16E+00
   1252      FP         32-Ge-82    81.9296   0.00E+00    1.52E-01
   1253      FP         33-As-82    81.9245   0.00E+00    3.63E-02
   1254      FP         33-As-82m   81.9245   0.00E+00    5.10E-02
   1255      FP         34-Se-82    81.9167   0.00E+00    0.00E+00
   1256      FP         35-Br-82    81.9168   0.00E+00    5.46E-06
   1257      FP         35-Br-82m   81.9168   0.00E+00    1.88E-03
   1258      FP         36-Kr-82    81.9135   0.00E+00    0.00E+00
   1259      FP         30-Zn-83    82.9610   0.00E+00    1.61E+01
   1260      FP         31-Ga-83    82.9470   0.00E+00    2.25E+00
   1261      FP         32-Ge-83    82.9346   0.00E+00    3.75E-01
   1262      FP         33-As-83    82.9250   0.00E+00    5.17E-02
   1263      FP         34-Se-83    82.9191   0.00E+00    5.18E-04
   1264      FP         34-Se-83m   82.9191   0.00E+00    9.89E-03
   1265      FP         35-Br-83    82.9152   0.00E+00    8.02E-05
   1266      FP         36-Kr-83    82.9141   0.00E+00    0.00E+00
   1267      FP         36-Kr-83m   82.9141   0.00E+00    1.05E-04
   1268      FP         37-Rb-83    82.9151   0.00E+00    9.31E-08
   1269      FP         38-Sr-83    82.9176   0.00E+00    5.94E-06
   1270      FP         31-Ga-84    83.9527   0.00E+00    8.15E+00
   1271      FP         32-Ge-84    83.9375   0.00E+00    7.27E-01
   1272      FP         33-As-84    83.9291   0.00E+00    1.65E-01
   1273      FP         34-Se-84    83.9185   0.00E+00    3.54E-03
   1274      FP         35-Br-84    83.9165   0.00E+00    3.64E-04
   1275      FP         35-Br-84m   83.9165   0.00E+00    1.93E-03
   1276      FP         36-Kr-84    83.9115   0.00E+00    0.00E+00
   1277      FP         37-Rb-84    83.9144   0.00E+00    2.44E-07
   1278      FP         38-Sr-84    83.9134   0.00E+00    0.00E+00
   1279      FP         31-Ga-85    84.9570   0.00E+00    1.44E+01
   1280      FP         32-Ge-85    84.9430   0.00E+00    1.30E+00
   1281      FP         33-As-85    84.9320   0.00E+00    3.43E-01
   1282      FP         34-Se-85    84.9222   0.00E+00    2.19E-02
   1283      FP         35-Br-85    84.9156   0.00E+00    3.98E-03
   1284      FP         36-Kr-85    84.9125   0.00E+00    2.04E-09
   1285      FP         36-Kr-85m   84.9125   0.00E+00    4.30E-05
   1286      FP         37-Rb-85    84.9118   0.00E+00    0.00E+00
   1287      FP         38-Sr-85    84.9129   0.00E+00    1.24E-07
   1288      FP         38-Sr-85m   84.9129   0.00E+00    1.71E-04
   1289      FP         39-Y-85     84.9164   0.00E+00    7.18E-05
   1290      FP         31-Ga-86    85.9631   0.00E+00    2.39E+01
   1291      FP         32-Ge-86    85.9465   0.00E+00    7.30E+00
   1292      FP         33-As-86    85.9365   0.00E+00    7.33E-01
   1293      FP         34-Se-86    85.9243   0.00E+00    4.85E-02
   1294      FP         35-Br-86    85.9188   0.00E+00    1.26E-02
   1295      FP         36-Kr-86    85.9106   0.00E+00    0.00E+00
   1296      FP         37-Rb-86    85.9112   0.00E+00    4.31E-07
   1297      FP         37-Rb-86m   85.9112   0.00E+00    1.14E-02
   1298      FP         38-Sr-86    85.9093   0.00E+00    0.00E+00
   1299      FP         32-Ge-87    86.9525   0.00E+00    4.95E+00
   1300      FP         33-As-87    86.9399   0.00E+00    1.24E+00
   1301      FP         34-Se-87    86.9285   0.00E+00    1.26E-01
   1302      FP         35-Br-87    86.9207   0.00E+00    1.25E-02
   1303      FP         36-Kr-87    86.9134   0.00E+00    1.51E-04
   1304      FP         37-Rb-87    86.9092   0.00E+00    4.57E-19
   1305      FP         38-Sr-87    86.9089   0.00E+00    0.00E+00
   1306      FP         38-Sr-87m   86.9089   0.00E+00    6.84E-05
   1307      FP         39-Y-87     86.9109   0.00E+00    2.41E-06
   1308      FP         39-Y-87m    86.9109   0.00E+00    1.44E-05
   1309      FP         40-Zr-87    86.9148   0.00E+00    1.15E-04
   1310      FP         32-Ge-88    87.9569   0.00E+00    1.05E+01
   1311      FP         33-As-88    87.9449   0.00E+00    6.19E+00
   1312      FP         34-Se-88    87.9314   0.00E+00    4.53E-01
   1313      FP         35-Br-88    87.9241   0.00E+00    4.26E-02
   1314      FP         36-Kr-88    87.9145   0.00E+00    6.78E-05
   1315      FP         37-Rb-88    87.9113   0.00E+00    6.50E-04
   1316      FP         38-Sr-88    87.9056   0.00E+00    0.00E+00
   1317      FP         39-Y-88     87.9095   0.00E+00    7.52E-08
   1318      FP         40-Zr-88    87.9102   0.00E+00    9.62E-08
   1319      FP         32-Ge-89    88.9638   0.00E+00    1.78E+01
   1320      FP         33-As-89    88.9494   0.00E+00    1.17E+01
   1321      FP         34-Se-89    88.9364   0.00E+00    1.69E+00
   1322      FP         35-Br-89    88.9264   0.00E+00    1.58E-01
   1323      FP         36-Kr-89    88.9176   0.00E+00    3.67E-03
   1324      FP         37-Rb-89    88.9123   0.00E+00    7.63E-04
   1325      FP         38-Sr-89    88.9074   0.00E+00    1.59E-07
   1326      FP         39-Y-89     88.9059   0.00E+00    0.00E+00
   1327      FP         39-Y-89m    88.9059   0.00E+00    4.43E-02
   1328      FP         40-Zr-89    88.9089   0.00E+00    2.46E-06
   1329      FP         40-Zr-89m   88.9089   0.00E+00    2.78E-03
   1330      FP         41-Nb-89    88.9134   0.00E+00    9.48E-05
   1331      FP         33-As-90    89.9555   0.00E+00    1.61E+01
   1332      FP         34-Se-90    89.9400   0.00E+00    4.31E+00
   1333      FP         35-Br-90    89.9306   0.00E+00    3.61E-01
   1334      FP         36-Kr-90    89.9195   0.00E+00    2.14E-02
   1335      FP         37-Rb-90    89.9148   0.00E+00    4.39E-03
   1336      FP         37-Rb-90m   89.9148   0.00E+00    2.69E-03
   1337      FP         38-Sr-90    89.9077   0.00E+00    7.63E-10
   1338      FP         39-Y-90     89.9072   0.00E+00    3.01E-06
   1339      FP         39-Y-90m    89.9072   0.00E+00    6.04E-05
   1340      FP         40-Zr-90    89.9047   0.00E+00    0.00E+00
   1341      FP         40-Zr-90m   89.9047   0.00E+00    8.57E-01
   1342      FP         41-Nb-90    89.9113   0.00E+00    1.32E-05
   1343      FP         41-Nb-90m   89.9113   0.00E+00    3.69E-02
   1344      FP         42-Mo-90    89.9139   0.00E+00    3.40E-05
   1345      FP         33-As-91    90.9604   0.00E+00    1.58E+01
   1346      FP         34-Se-91    90.9460   0.00E+00    2.57E+00
   1347      FP         35-Br-91    90.9340   0.00E+00    1.28E+00
   1348      FP         36-Kr-91    90.9234   0.00E+00    8.09E-02
   1349      FP         37-Rb-91    90.9165   0.00E+00    1.19E-02
   1350      FP         38-Sr-91    90.9102   0.00E+00    2.00E-05
   1351      FP         39-Y-91     90.9073   0.00E+00    1.37E-07
   1352      FP         39-Y-91m    90.9073   0.00E+00    2.32E-04
   1353      FP         40-Zr-91    90.9056   0.00E+00    0.00E+00
   1354      FP         41-Nb-91    90.9070   0.00E+00    3.23E-11
   1355      FP         41-Nb-91m   90.9070   0.00E+00    1.32E-07
   1356      FP         42-Mo-91    90.9118   0.00E+00    7.46E-04
   1357      FP         33-As-92    91.9668   0.00E+00    2.57E+01
   1358      FP         34-Se-92    91.9499   0.00E+00    7.45E+00
   1359      FP         35-Br-92    91.9393   0.00E+00    2.02E+00
   1360      FP         36-Kr-92    91.9262   0.00E+00    3.77E-01
   1361      FP         37-Rb-92    91.9197   0.00E+00    1.54E-01
   1362      FP         38-Sr-92    91.9110   0.00E+00    7.10E-05
   1363      FP         39-Y-92     91.9090   0.00E+00    5.44E-05
   1364      FP         40-Zr-92    91.9050   0.00E+00    0.00E+00
   1365      FP         41-Nb-92    91.9072   0.00E+00    6.33E-16
   1366      FP         41-Nb-92m   91.9072   0.00E+00    7.90E-07
   1367      FP         42-Mo-92    91.9068   0.00E+00    0.00E+00
   1368      FP         34-Se-93    92.9563   0.00E+00    1.12E+01
   1369      FP         35-Br-93    92.9430   0.00E+00    6.80E+00
   1370      FP         36-Kr-93    92.9313   0.00E+00    5.39E-01
   1371      FP         37-Rb-93    92.9220   0.00E+00    1.19E-01
   1372      FP         38-Sr-93    92.9140   0.00E+00    1.56E-03
   1373      FP         39-Y-93     92.9096   0.00E+00    1.89E-05
   1374      FP         39-Y-93m    92.9096   0.00E+00    8.45E-01
   1375      FP         40-Zr-93    92.9065   0.00E+00    1.44E-14
   1376      FP         41-Nb-93    92.9064   0.00E+00    0.00E+00
   1377      FP         41-Nb-93m   92.9064   0.00E+00    1.36E-09
   1378      FP         42-Mo-93    92.9068   0.00E+00    5.49E-12
   1379      FP         42-Mo-93m   92.9068   0.00E+00    2.81E-05
   1380      FP         43-Tc-93    92.9102   0.00E+00    7.00E-05
   1381      FP         34-Se-94    93.9605   0.00E+00    1.17E+01
   1382      FP         35-Br-94    93.9487   0.00E+00    9.90E+00
   1383      FP         36-Kr-94    93.9344   0.00E+00    3.27E+00
   1384      FP         37-Rb-94    93.9264   0.00E+00    2.57E-01
   1385      FP         38-Sr-94    93.9154   0.00E+00    9.20E-03
   1386      FP         39-Y-94     93.9116   0.00E+00    6.18E-04
   1387      FP         40-Zr-94    93.9063   0.00E+00    0.00E+00
   1388      FP         41-Nb-94    93.9073   0.00E+00    1.08E-12
   1389      FP         41-Nb-94m   93.9073   0.00E+00    1.84E-03
   1390      FP         42-Mo-94    93.9051   0.00E+00    0.00E+00
   1391      FP         35-Br-95    94.9529   0.00E+00    1.05E+01
   1392      FP         36-Kr-95    94.9398   0.00E+00    6.08E+00
   1393      FP         37-Rb-95    94.9293   0.00E+00    1.84E+00
   1394      FP         38-Sr-95    94.9194   0.00E+00    2.90E-02
   1395      FP         39-Y-95     94.9128   0.00E+00    1.12E-03
   1396      FP         40-Zr-95    94.9080   0.00E+00    1.25E-07
   1397      FP         41-Nb-95    94.9068   0.00E+00    2.29E-07
   1398      FP         41-Nb-95m   94.9068   0.00E+00    2.22E-06
   1399      FP         42-Mo-95    94.9058   0.00E+00    0.00E+00
   1400      FP         43-Tc-95    94.9077   0.00E+00    9.63E-06
   1401      FP         43-Tc-95m   94.9077   0.00E+00    1.32E-07
   1402      FP         44-Ru-95    94.9104   0.00E+00    1.17E-04
   1403      FP         35-Br-96    95.9585   0.00E+00    1.65E+01
   1404      FP         36-Kr-96    95.9431   0.00E+00    8.66E+00
   1405      FP         37-Rb-96    95.9343   0.00E+00    3.41E+00
   1406      FP         38-Sr-96    95.9217   0.00E+00    6.48E-01
   1407      FP         39-Y-96     95.9159   0.00E+00    1.30E-01
   1408      FP         39-Y-96m    95.9159   0.00E+00    7.22E-02
   1409      FP         40-Zr-96    95.9083   0.00E+00    1.10E-27
   1410      FP         41-Nb-96    95.9081   0.00E+00    8.25E-06
   1411      FP         42-Mo-96    95.9047   0.00E+00    0.00E+00
   1412      FP         43-Tc-96    95.9079   0.00E+00    1.87E-06
   1413      FP         44-Ru-96    95.9076   0.00E+00    0.00E+00
   1414      FP         35-Br-97    96.9628   0.00E+00    1.73E+01
   1415      FP         36-Kr-97    96.9486   0.00E+00    1.10E+01
   1416      FP         37-Rb-97    96.9373   0.00E+00    4.10E+00
   1417      FP         38-Sr-97    96.9261   0.00E+00    1.62E+00
   1418      FP         39-Y-97     96.9181   0.00E+00    1.85E-01
   1419      FP         39-Y-97m    96.9181   0.00E+00    5.92E-01
   1420      FP         40-Zr-97    96.9109   0.00E+00    1.15E-05
   1421      FP         41-Nb-97    96.9081   0.00E+00    1.60E-04
   1422      FP         41-Nb-97m   96.9081   0.00E+00    1.18E-02
   1423      FP         42-Mo-97    96.9060   0.00E+00    0.00E+00
   1424      FP         43-Tc-97    96.9064   0.00E+00    5.22E-15
   1425      FP         43-Tc-97m   96.9064   0.00E+00    8.82E-08
   1426      FP         44-Ru-97    96.9076   0.00E+00    2.83E-06
   1427      FP         36-Kr-98    97.9519   0.00E+00    1.51E+01
   1428      FP         37-Rb-98    97.9418   0.00E+00    6.08E+00
   1429      FP         38-Sr-98    97.9285   0.00E+00    1.06E+00
   1430      FP         39-Y-98     97.9222   0.00E+00    1.26E+00
   1431      FP         39-Y-98m    97.9222   0.00E+00    3.47E-01
   1432      FP         40-Zr-98    97.9127   0.00E+00    2.26E-02
   1433      FP         41-Nb-98    97.9103   0.00E+00    2.42E-01
   1434      FP         41-Nb-98m   97.9103   0.00E+00    2.25E-04
   1435      FP         42-Mo-98    97.9054   0.00E+00    0.00E+00
   1436      FP         43-Tc-98    97.9072   0.00E+00    5.23E-15
   1437      FP         44-Ru-98    97.9053   0.00E+00    0.00E+00
   1438      FP         36-Kr-99    98.9576   0.00E+00    2.57E+01
   1439      FP         37-Rb-99    98.9454   0.00E+00    1.28E+01
   1440      FP         38-Sr-99    98.9332   0.00E+00    2.57E+00
   1441      FP         39-Y-99     98.9246   0.00E+00    4.72E-01
   1442      FP         40-Zr-99    98.9165   0.00E+00    3.30E-01
   1443      FP         41-Nb-99    98.9116   0.00E+00    4.62E-02
   1444      FP         41-Nb-99m   98.9116   0.00E+00    4.62E-03
   1445      FP         42-Mo-99    98.9077   0.00E+00    2.92E-06
   1446      FP         43-Tc-99    98.9062   0.00E+00    1.04E-13
   1447      FP         43-Tc-99m   98.9062   0.00E+00    3.21E-05
   1448      FP         44-Ru-99    98.9059   0.00E+00    0.00E+00
   1449      FP         45-Rh-99    98.9081   0.00E+00    4.98E-07
   1450      FP         45-Rh-99m   98.9081   0.00E+00    4.10E-05
   1451      FP         46-Pd-99    98.9118   0.00E+00    5.40E-04
   1452      FP         36-Kr-100   99.9611   0.00E+00    9.90E+01
   1453      FP         37-Rb-100   99.9499   0.00E+00    1.36E+01
   1454      FP         38-Sr-100   99.9353   0.00E+00    3.43E+00
   1455      FP         39-Y-100    99.9278   0.00E+00    9.43E-01
   1456      FP         40-Zr-100   99.9178   0.00E+00    9.76E-02
   1457      FP         41-Nb-100   99.9142   0.00E+00    4.62E-01
   1458      FP         41-Nb-100m  99.9142   0.00E+00    2.32E-01
   1459      FP         42-Mo-100   99.9075   0.00E+00    3.01E-27
   1460      FP         43-Tc-100   99.9077   0.00E+00    4.48E-02
   1461      FP         44-Ru-100   99.9042   0.00E+00    0.00E+00
   1462      FP         37-Rb-101   100.9532  0.00E+00    2.17E+01
   1463      FP         38-Sr-101   100.9405  0.00E+00    5.87E+00
   1464      FP         39-Y-101    100.9303  0.00E+00    1.54E+00
   1465      FP         40-Zr-101   100.9211  0.00E+00    3.01E-01
   1466      FP         41-Nb-101   100.9153  0.00E+00    9.76E-02
   1467      FP         42-Mo-101   100.9103  0.00E+00    7.91E-04
   1468      FP         43-Tc-101   100.9073  0.00E+00    8.14E-04
   1469      FP         44-Ru-101   100.9056  0.00E+00    0.00E+00
   1470      FP         45-Rh-101   100.9062  0.00E+00    6.66E-09
   1471      FP         45-Rh-101m  100.9062  0.00E+00    1.85E-06
   1472      FP         46-Pd-101   100.9083  0.00E+00    2.27E-05
   1473      FP         37-Rb-102   101.9589  0.00E+00    1.87E+01
   1474      FP         38-Sr-102   101.9430  0.00E+00    1.00E+01
   1475      FP         39-Y-102    101.9336  0.00E+00    1.93E+00
   1476      FP         40-Zr-102   101.9230  0.00E+00    2.39E-01
   1477      FP         41-Nb-102   101.9180  0.00E+00    1.61E-01
   1478      FP         41-Nb-102m  101.9180  0.00E+00    5.33E-01
   1479      FP         42-Mo-102   101.9103  0.00E+00    1.02E-03
   1480      FP         43-Tc-102   101.9092  0.00E+00    1.31E-01
   1481      FP         43-Tc-102m  101.9092  0.00E+00    2.66E-03
   1482      FP         44-Ru-102   101.9044  0.00E+00    0.00E+00
   1483      FP         45-Rh-102   101.9068  0.00E+00    3.87E-08
   1484      FP         45-Rh-102m  101.9068  0.00E+00    5.87E-09
   1485      FP         46-Pd-102   101.9056  0.00E+00    0.00E+00
   1486      FP         38-Sr-103   102.9490  0.00E+00    1.02E+01
   1487      FP         39-Y-103    102.9367  0.00E+00    3.01E+00
   1488      FP         40-Zr-103   102.9266  0.00E+00    5.33E-01
   1489      FP         41-Nb-103   102.9191  0.00E+00    4.62E-01
   1490      FP         42-Mo-103   102.9132  0.00E+00    1.03E-02
   1491      FP         43-Tc-103   102.9092  0.00E+00    1.28E-02
   1492      FP         44-Ru-103   102.9063  0.00E+00    2.04E-07
   1493      FP         45-Rh-103   102.9055  0.00E+00    0.00E+00
   1494      FP         45-Rh-103m  102.9055  0.00E+00    2.06E-04
   1495      FP         46-Pd-103   102.9061  0.00E+00    4.72E-07
   1496      FP         47-Ag-103   102.9090  0.00E+00    1.76E-04
   1497      FP         38-Sr-104   103.9523  0.00E+00    1.61E+01
   1498      FP         39-Y-104    103.9410  0.00E+00    3.85E+00
   1499      FP         40-Zr-104   103.9288  0.00E+00    5.78E-01
   1500      FP         41-Nb-104   103.9225  0.00E+00    1.41E-01
   1501      FP         41-Nb-104m  103.9225  0.00E+00    7.37E-01
   1502      FP         42-Mo-104   103.9138  0.00E+00    1.16E-02
   1503      FP         43-Tc-104   103.9115  0.00E+00    6.31E-04
   1504      FP         44-Ru-104   103.9054  0.00E+00    0.00E+00
   1505      FP         45-Rh-104   103.9067  0.00E+00    1.64E-02
   1506      FP         45-Rh-104m  103.9067  0.00E+00    2.66E-03
   1507      FP         46-Pd-104   103.9040  0.00E+00    0.00E+00
   1508      FP         38-Sr-105   104.9586  0.00E+00    1.25E+01
   1509      FP         39-Y-105    104.9449  0.00E+00    7.88E+00
   1510      FP         40-Zr-105   104.9331  0.00E+00    1.16E+00
   1511      FP         41-Nb-105   104.9239  0.00E+00    2.35E-01
   1512      FP         42-Mo-105   104.9170  0.00E+00    1.95E-02
   1513      FP         43-Tc-105   104.9117  0.00E+00    1.52E-03
   1514      FP         44-Ru-105   104.9078  0.00E+00    4.34E-05
   1515      FP         45-Rh-105   104.9057  0.00E+00    5.45E-06
   1516      FP         45-Rh-105m  104.9057  0.00E+00    1.73E-02
   1517      FP         46-Pd-105   104.9051  0.00E+00    0.00E+00
   1518      FP         47-Ag-105   104.9065  0.00E+00    1.94E-07
   1519      FP         47-Ag-105m  104.9065  0.00E+00    1.60E-03
   1520      FP         48-Cd-105   104.9095  0.00E+00    2.08E-04
   1521      FP         39-Y-106    105.9498  0.00E+00    1.05E+01
   1522      FP         40-Zr-106   105.9359  0.00E+00    2.57E+00
   1523      FP         41-Nb-106   105.9280  0.00E+00    7.45E-01
   1524      FP         42-Mo-106   105.9181  0.00E+00    7.94E-02
   1525      FP         43-Tc-106   105.9144  0.00E+00    1.95E-02
   1526      FP         44-Ru-106   105.9073  0.00E+00    2.16E-08
   1527      FP         45-Rh-106   105.9073  0.00E+00    2.31E-02
   1528      FP         45-Rh-106m  105.9073  0.00E+00    8.82E-05
   1529      FP         46-Pd-106   105.9035  0.00E+00    0.00E+00
   1530      FP         47-Ag-106   105.9067  0.00E+00    4.82E-04
   1531      FP         47-Ag-106m  105.9067  0.00E+00    9.69E-07
   1532      FP         48-Cd-106   105.9065  0.00E+00    0.00E+00
   1533      FP         39-Y-107    106.9541  0.00E+00    2.31E+01
   1534      FP         40-Zr-107   106.9408  0.00E+00    4.62E+00
   1535      FP         41-Nb-107   106.9303  0.00E+00    2.31E+00
   1536      FP         42-Mo-107   106.9217  0.00E+00    1.98E-01
   1537      FP         43-Tc-107   106.9151  0.00E+00    3.27E-02
   1538      FP         44-Ru-107   106.9099  0.00E+00    3.08E-03
   1539      FP         45-Rh-107   106.9068  0.00E+00    5.32E-04
   1540      FP         46-Pd-107   106.9051  0.00E+00    3.38E-15
   1541      FP         46-Pd-107m  106.9051  0.00E+00    3.25E-02
   1542      FP         47-Ag-107   106.9051  0.00E+00    0.00E+00
   1543      FP         47-Ag-107m  106.9051  0.00E+00    1.56E-02
   1544      FP         48-Cd-107   106.9066  0.00E+00    2.96E-05
   1545      FP         49-In-107   106.9103  0.00E+00    3.57E-04
   1546      FP         39-Y-108    107.9595  0.00E+00    1.44E+01
   1547      FP         40-Zr-108   107.9440  0.00E+00    8.66E+00
   1548      FP         41-Nb-108   107.9348  0.00E+00    3.59E+00
   1549      FP         42-Mo-108   107.9234  0.00E+00    6.36E-01
   1550      FP         43-Tc-108   107.9185  0.00E+00    1.34E-01
   1551      FP         44-Ru-108   107.9102  0.00E+00    2.54E-03
   1552      FP         45-Rh-108   107.9087  0.00E+00    4.13E-02
   1553      FP         45-Rh-108m  107.9087  0.00E+00    1.93E-03
   1554      FP         46-Pd-108   107.9039  0.00E+00    0.00E+00
   1555      FP         47-Ag-108   107.9060  0.00E+00    4.85E-03
   1556      FP         47-Ag-108m  107.9060  0.00E+00    5.01E-11
   1557      FP         48-Cd-108   107.9042  0.00E+00    0.00E+00
   1558      FP         40-Zr-109   108.9492  0.00E+00    5.92E+00
   1559      FP         41-Nb-109   108.9376  0.00E+00    3.65E+00
   1560      FP         42-Mo-109   108.9278  0.00E+00    1.31E+00
   1561      FP         43-Tc-109   108.9200  0.00E+00    8.06E-01
   1562      FP         44-Ru-109   108.9132  0.00E+00    2.01E-02
   1563      FP         45-Rh-109   108.9087  0.00E+00    8.66E-03
   1564      FP         46-Pd-109   108.9060  0.00E+00    1.41E-05
   1565      FP         46-Pd-109m  108.9060  0.00E+00    2.46E-03
   1566      FP         47-Ag-109   108.9047  0.00E+00    0.00E+00
   1567      FP         47-Ag-109m  108.9047  0.00E+00    1.75E-02
   1568      FP         48-Cd-109   108.9050  0.00E+00    1.74E-08
   1569      FP         49-In-109   108.9072  0.00E+00    4.62E-05
   1570      FP         40-Zr-110   109.9529  0.00E+00    7.07E+00
   1571      FP         41-Nb-110   109.9424  0.00E+00    4.08E+00
   1572      FP         42-Mo-110   109.9297  0.00E+00    2.31E+00
   1573      FP         43-Tc-110   109.9238  0.00E+00    7.53E-01
   1574      FP         44-Ru-110   109.9141  0.00E+00    5.98E-02
   1575      FP         45-Rh-110   109.9111  0.00E+00    2.17E-01
   1576      FP         45-Rh-110m  109.9111  0.00E+00    2.43E-02
   1577      FP         46-Pd-110   109.9052  0.00E+00    0.00E+00
   1578      FP         47-Ag-110   109.9061  0.00E+00    2.82E-02
   1579      FP         47-Ag-110m  109.9062  0.00E+00    3.21E-08
   1580      FP         48-Cd-110   109.9030  0.00E+00    0.00E+00
   1581      FP         41-Nb-111   110.9456  0.00E+00    8.66E+00
   1582      FP         42-Mo-111   110.9344  0.00E+00    3.47E+00
   1583      FP         43-Tc-111   110.9257  0.00E+00    2.39E+00
   1584      FP         44-Ru-111   110.9177  0.00E+00    3.27E-01
   1585      FP         45-Rh-111   110.9116  0.00E+00    6.30E-02
   1586      FP         46-Pd-111   110.9077  0.00E+00    4.94E-04
   1587      FP         46-Pd-111m  110.9077  0.00E+00    3.50E-05
   1588      FP         47-Ag-111   110.9053  0.00E+00    1.08E-06
   1589      FP         47-Ag-111m  110.9053  0.00E+00    1.07E-02
   1590      FP         48-Cd-111   110.9042  0.00E+00    0.00E+00
   1591      FP         48-Cd-111m  110.9042  0.00E+00    2.38E-04
   1592      FP         49-In-111   110.9051  0.00E+00    2.86E-06
   1593      FP         49-In-111m  110.9051  0.00E+00    1.50E-03
   1594      FP         50-Sn-111   110.9077  0.00E+00    3.27E-04
   1595      FP         41-Nb-112   111.9508  0.00E+00    1.00E+01
   1596      FP         42-Mo-112   111.9368  0.00E+00    2.42E+00
   1597      FP         43-Tc-112   111.9292  0.00E+00    2.48E+00
   1598      FP         44-Ru-112   111.9190  0.00E+00    3.96E-01
   1599      FP         45-Rh-112   111.9144  0.00E+00    3.30E-01
   1600      FP         46-Pd-112   111.9073  0.00E+00    9.16E-06
   1601      FP         47-Ag-112   111.9070  0.00E+00    6.15E-05
   1602      FP         48-Cd-112   111.9028  0.00E+00    0.00E+00
   1603      FP         49-In-112   111.9055  0.00E+00    7.72E-04
   1604      FP         49-In-112m  111.9055  0.00E+00    5.62E-04
   1605      FP         50-Sn-112   111.9048  0.00E+00    0.00E+00
   1606      FP         41-Nb-113   112.9547  0.00E+00    2.31E+01
   1607      FP         42-Mo-113   112.9419  0.00E+00    6.93E+00
   1608      FP         43-Tc-113   112.9316  0.00E+00    4.33E+00
   1609      FP         44-Ru-113   112.9225  0.00E+00    8.66E-01
   1610      FP         45-Rh-113   112.9155  0.00E+00    2.48E-01
   1611      FP         46-Pd-113   112.9101  0.00E+00    7.45E-03
   1612      FP         47-Ag-113   112.9066  0.00E+00    3.59E-05
   1613      FP         47-Ag-113m  112.9066  0.00E+00    1.01E-02
   1614      FP         48-Cd-113   112.9044  0.00E+00    2.73E-24
   1615      FP         48-Cd-113m  112.9044  0.00E+00    1.56E-09
   1616      FP         49-In-113   112.9041  0.00E+00    0.00E+00
   1617      FP         49-In-113m  112.9041  0.00E+00    1.16E-04
   1618      FP         50-Sn-113   112.9052  0.00E+00    6.97E-08
   1619      FP         50-Sn-113m  112.9052  0.00E+00    5.40E-04
   1620      FP         51-Sb-113   112.9094  0.00E+00    1.73E-03
   1621      FP         42-Mo-114   113.9449  0.00E+00    8.66E+00
   1622      FP         43-Tc-114   113.9359  0.00E+00    4.62E+00
   1623      FP         44-Ru-114   113.9243  0.00E+00    1.33E+00
   1624      FP         45-Rh-114   113.9188  0.00E+00    3.75E-01
   1625      FP         46-Pd-114   113.9104  0.00E+00    4.77E-03
   1626      FP         47-Ag-114   113.9088  0.00E+00    1.51E-01
   1627      FP         48-Cd-114   113.9034  0.00E+00    0.00E+00
   1628      FP         49-In-114   113.9049  0.00E+00    9.64E-03
   1629      FP         49-In-114m  113.9049  0.00E+00    1.62E-07
   1630      FP         50-Sn-114   113.9028  0.00E+00    0.00E+00
   1631      FP         42-Mo-115   114.9503  0.00E+00    7.53E+00
   1632      FP         43-Tc-115   114.9387  0.00E+00    9.50E+00
   1633      FP         44-Ru-115   114.9287  0.00E+00    9.37E-01
   1634      FP         45-Rh-115   114.9203  0.00E+00    7.00E-01
   1635      FP         46-Pd-115   114.9137  0.00E+00    2.77E-02
   1636      FP         47-Ag-115   114.9088  0.00E+00    5.78E-04
   1637      FP         47-Ag-115m  114.9088  0.00E+00    3.85E-02
   1638      FP         48-Cd-115   114.9054  0.00E+00    3.60E-06
   1639      FP         48-Cd-115m  114.9051  0.00E+00    1.80E-07
   1640      FP         49-In-115   114.9039  0.00E+00    4.98E-23
   1641      FP         49-In-115m  114.9039  0.00E+00    4.29E-05
   1642      FP         50-Sn-115   114.9033  0.00E+00    0.00E+00
   1643      FP         51-Sb-115   114.9066  0.00E+00    3.60E-04
   1644      FP         52-Te-115   114.9119  0.00E+00    1.99E-03
   1645      FP         43-Tc-116   115.9434  0.00E+00    7.70E+00
   1646      FP         44-Ru-116   115.9308  0.00E+00    3.40E+00
   1647      FP         45-Rh-116   115.9241  0.00E+00    1.02E+00
   1648      FP         46-Pd-116   115.9142  0.00E+00    5.87E-02
   1649      FP         47-Ag-116   115.9114  0.00E+00    2.92E-03
   1650      FP         47-Ag-116m  115.9114  0.00E+00    3.47E-02
   1651      FP         48-Cd-116   115.9048  0.00E+00    7.09E-28
   1652      FP         49-In-116   115.9053  0.00E+00    4.92E-02
   1653      FP         49-In-116m  115.9053  0.00E+00    2.13E-04
   1654      FP         50-Sn-116   115.9017  0.00E+00    0.00E+00
   1655      FP         43-Tc-117   116.9465  0.00E+00    1.73E+01
   1656      FP         44-Ru-117   116.9356  0.00E+00    4.88E+00
   1657      FP         45-Rh-117   116.9260  0.00E+00    1.58E+00
   1658      FP         46-Pd-117   116.9178  0.00E+00    1.61E-01
   1659      FP         47-Ag-117   116.9117  0.00E+00    9.52E-03
   1660      FP         47-Ag-117m  116.9117  0.00E+00    1.30E-01
   1661      FP         48-Cd-117   116.9072  0.00E+00    7.73E-05
   1662      FP         48-Cd-117m  116.9072  0.00E+00    5.73E-05
   1663      FP         49-In-117   116.9045  0.00E+00    2.67E-04
   1664      FP         49-In-117m  116.9045  0.00E+00    9.94E-05
   1665      FP         50-Sn-117   116.9029  0.00E+00    0.00E+00
   1666      FP         50-Sn-117m  116.9029  0.00E+00    5.90E-07
   1667      FP         51-Sb-117   116.9048  0.00E+00    6.88E-05
   1668      FP         52-Te-117   116.9087  0.00E+00    1.86E-04
   1669      FP         43-Tc-118   117.9515  0.00E+00    1.05E+01
   1670      FP         44-Ru-118   117.9378  0.00E+00    5.64E+00
   1671      FP         45-Rh-118   117.9301  0.00E+00    2.61E+00
   1672      FP         46-Pd-118   117.9190  0.00E+00    3.65E-01
   1673      FP         47-Ag-118   117.9146  0.00E+00    1.84E-01
   1674      FP         47-Ag-118m  117.9146  0.00E+00    3.47E-01
   1675      FP         48-Cd-118   117.9069  0.00E+00    2.30E-04
   1676      FP         49-In-118   117.9063  0.00E+00    1.39E-01
   1677      FP         49-In-118m  117.9063  0.00E+00    2.60E-03
   1678      FP         50-Sn-118   117.9016  0.00E+00    0.00E+00
   1679      FP         51-Sb-118   117.9055  0.00E+00    3.21E-03
   1680      FP         51-Sb-118m  117.9055  0.00E+00    3.85E-05
   1681      FP         52-Te-118   117.9058  0.00E+00    1.34E-06
   1682      FP         44-Ru-119   118.9428  0.00E+00    4.28E+00
   1683      FP         45-Rh-119   118.9321  0.00E+00    4.05E+00
   1684      FP         46-Pd-119   118.9231  0.00E+00    7.53E-01
   1685      FP         47-Ag-119   118.9157  0.00E+00    3.30E-01
   1686      FP         48-Cd-119   118.9099  0.00E+00    4.29E-03
   1687      FP         48-Cd-119m  118.9099  0.00E+00    5.25E-03
   1688      FP         49-In-119   118.9059  0.00E+00    4.81E-03
   1689      FP         49-In-119m  118.9059  0.00E+00    6.42E-04
   1690      FP         50-Sn-119   118.9033  0.00E+00    0.00E+00
   1691      FP         50-Sn-119m  118.9033  0.00E+00    2.74E-08
   1692      FP         51-Sb-119   118.9039  0.00E+00    5.04E-06
   1693      FP         52-Te-119   118.9064  0.00E+00    1.20E-05
   1694      FP         44-Ru-120   119.9453  0.00E+00    4.65E+00
   1695      FP         45-Rh-120   119.9364  0.00E+00    5.10E+00
   1696      FP         46-Pd-120   119.9247  0.00E+00    1.39E+00
   1697      FP         47-Ag-120   119.9188  0.00E+00    5.64E-01
   1698      FP         47-Ag-120m  119.9188  0.00E+00    2.17E+00
   1699      FP         48-Cd-120   119.9099  0.00E+00    1.36E-02
   1700      FP         49-In-120   119.9080  0.00E+00    2.25E-01
   1701      FP         49-In-120m  119.9080  0.00E+00    1.50E-02
   1702      FP         50-Sn-120   119.9022  0.00E+00    0.00E+00
   1703      FP         51-Sb-120   119.9051  0.00E+00    7.27E-04
   1704      FP         51-Sb-120m  119.9051  0.00E+00    1.39E-06
   1705      FP         52-Te-120   119.9040  0.00E+00    0.00E+00
   1706      FP         45-Rh-121   120.9387  0.00E+00    4.59E+00
   1707      FP         46-Pd-121   120.9289  0.00E+00    2.43E+00
   1708      FP         47-Ag-121   120.9199  0.00E+00    8.89E-01
   1709      FP         48-Cd-121   120.9130  0.00E+00    5.13E-02
   1710      FP         48-Cd-121m  120.9130  0.00E+00    8.35E-02
   1711      FP         49-In-121   120.9079  0.00E+00    3.00E-02
   1712      FP         49-In-121m  120.9079  0.00E+00    2.98E-03
   1713      FP         50-Sn-121   120.9042  0.00E+00    7.12E-06
   1714      FP         50-Sn-121m  120.9042  0.00E+00    5.00E-10
   1715      FP         51-Sb-121   120.9038  0.00E+00    0.00E+00
   1716      FP         52-Te-121   120.9049  0.00E+00    4.19E-07
   1717      FP         52-Te-121m  120.9049  0.00E+00    4.89E-08
   1718      FP         53-I-121    120.9074  0.00E+00    9.08E-05
   1719      FP         45-Rh-122   121.9432  0.00E+00    6.42E+00
   1720      FP         46-Pd-122   121.9305  0.00E+00    3.96E+00
   1721      FP         47-Ag-122   121.9235  0.00E+00    1.31E+00
   1722      FP         47-Ag-122m  121.9235  0.00E+00    3.47E+00
   1723      FP         48-Cd-122   121.9133  0.00E+00    1.32E-01
   1724      FP         49-In-122   121.9103  0.00E+00    4.62E-01
   1725      FP         49-In-122m  121.9103  0.00E+00    6.73E-02
   1726      FP         50-Sn-122   121.9034  0.00E+00    0.00E+00
   1727      FP         51-Sb-122   121.9052  0.00E+00    2.95E-06
   1728      FP         51-Sb-122m  121.9052  0.00E+00    2.76E-03
   1729      FP         52-Te-122   121.9030  0.00E+00    0.00E+00
   1730      FP         46-Pd-123   122.9349  0.00E+00    2.84E+00
   1731      FP         47-Ag-123   122.9249  0.00E+00    2.31E+00
   1732      FP         48-Cd-123   122.9170  0.00E+00    3.30E-01
   1733      FP         48-Cd-123m  122.9170  0.00E+00    3.81E-01
   1734      FP         49-In-123   122.9104  0.00E+00    1.12E-01
   1735      FP         49-In-123m  122.9104  0.00E+00    1.46E-02
   1736      FP         50-Sn-123   122.9057  0.00E+00    6.21E-08
   1737      FP         50-Sn-123m  122.9057  0.00E+00    2.88E-04
   1738      FP         51-Sb-123   122.9042  0.00E+00    0.00E+00
   1739      FP         52-Te-123   122.9043  0.00E+00    0.00E+00
   1740      FP         52-Te-123m  122.9043  0.00E+00    6.73E-08
   1741      FP         53-I-123    122.9056  0.00E+00    1.46E-05
   1742      FP         46-Pd-124   123.9369  0.00E+00    1.82E+01
   1743      FP         47-Ag-124   123.9286  0.00E+00    4.03E+00
   1744      FP         48-Cd-124   123.9176  0.00E+00    5.55E-01
   1745      FP         49-In-124   123.9132  0.00E+00    2.22E-01
   1746      FP         49-In-124m  123.9132  0.00E+00    1.87E-01
   1747      FP         50-Sn-124   123.9053  0.00E+00    0.00E+00
   1748      FP         51-Sb-124   123.9059  0.00E+00    1.33E-07
   1749      FP         51-Sb-124m  123.9059  0.00E+00    7.45E-03
   1750      FP         52-Te-124   123.9028  0.00E+00    0.00E+00
   1751      FP         53-I-124    123.9062  0.00E+00    1.92E-06
   1752      FP         54-Xe-124   123.9059  0.00E+00    0.00E+00
   1753      FP         47-Ag-125   124.9304  0.00E+00    4.18E+00
   1754      FP         48-Cd-125   124.9212  0.00E+00    1.02E+00
   1755      FP         49-In-125   124.9136  0.00E+00    2.94E-01
   1756      FP         49-In-125m  124.9136  0.00E+00    5.68E-02
   1757      FP         50-Sn-125   124.9078  0.00E+00    8.32E-07
   1758      FP         50-Sn-125m  124.9078  0.00E+00    1.21E-03
   1759      FP         51-Sb-125   124.9053  0.00E+00    7.96E-09
   1760      FP         52-Te-125   124.9044  0.00E+00    0.00E+00
   1761      FP         52-Te-125m  124.9044  0.00E+00    1.40E-07
   1762      FP         53-I-125    124.9046  0.00E+00    1.35E-07
   1763      FP         54-Xe-125   124.9064  0.00E+00    1.14E-05
   1764      FP         54-Xe-125m  124.9064  0.00E+00    1.22E-02
   1765      FP         47-Ag-126   125.9345  0.00E+00    6.48E+00
   1766      FP         48-Cd-126   125.9223  0.00E+00    1.35E+00
   1767      FP         49-In-126   125.9165  0.00E+00    4.53E-01
   1768      FP         49-In-126m  125.9165  0.00E+00    4.23E-01
   1769      FP         50-Sn-126   125.9077  0.00E+00    9.55E-14
   1770      FP         51-Sb-126   125.9072  0.00E+00    6.50E-07
   1771      FP         51-Sb-126m  125.9072  0.00E+00    6.03E-04
   1772      FP         52-Te-126   125.9033  0.00E+00    0.00E+00
   1773      FP         53-I-126    125.9056  0.00E+00    6.20E-07
   1774      FP         54-Xe-126   125.9043  0.00E+00    0.00E+00
   1775      FP         47-Ag-127   126.9368  0.00E+00    6.36E+00
   1776      FP         48-Cd-127   126.9264  0.00E+00    1.87E+00
   1777      FP         49-In-127   126.9174  0.00E+00    6.36E-01
   1778      FP         49-In-127m  126.9174  0.00E+00    1.89E-01
   1779      FP         50-Sn-127   126.9104  0.00E+00    9.17E-05
   1780      FP         50-Sn-127m  126.9104  0.00E+00    2.80E-03
   1781      FP         51-Sb-127   126.9069  0.00E+00    2.08E-06
   1782      FP         52-Te-127   126.9052  0.00E+00    2.06E-05
   1783      FP         52-Te-127m  126.9052  0.00E+00    7.36E-08
   1784      FP         53-I-127    126.9045  0.00E+00    0.00E+00
   1785      FP         54-Xe-127   126.9052  0.00E+00    2.20E-07
   1786      FP         54-Xe-127m  126.9052  0.00E+00    1.00E-02
   1787      FP         55-Cs-127   126.9074  0.00E+00    3.08E-05
   1788      FP         47-Ag-128   127.9412  0.00E+00    1.20E+01
   1789      FP         48-Cd-128   127.9278  0.00E+00    2.48E+00
   1790      FP         49-In-128   127.9202  0.00E+00    8.25E-01
   1791      FP         49-In-128m  127.9202  0.00E+00    9.63E-01
   1792      FP         50-Sn-128   127.9105  0.00E+00    1.96E-04
   1793      FP         50-Sn-128m  127.9105  0.00E+00    1.07E-01
   1794      FP         51-Sb-128   127.9092  0.00E+00    2.14E-05
   1795      FP         51-Sb-128m  127.9092  0.00E+00    1.11E-03
   1796      FP         52-Te-128   127.9045  0.00E+00    2.50E-27
   1797      FP         53-I-128    127.9058  0.00E+00    4.62E-04
   1798      FP         54-Xe-128   127.9035  0.00E+00    0.00E+00
   1799      FP         47-Ag-129   128.9437  0.00E+00    1.51E+01
   1800      FP         48-Cd-129   128.9321  0.00E+00    2.57E+00
   1801      FP         49-In-129   128.9217  0.00E+00    1.14E+00
   1802      FP         49-In-129m  128.9217  0.00E+00    5.64E-01
   1803      FP         50-Sn-129   128.9135  0.00E+00    5.18E-03
   1804      FP         50-Sn-129m  128.9135  0.00E+00    1.67E-03
   1805      FP         51-Sb-129   128.9091  0.00E+00    4.38E-05
   1806      FP         51-Sb-129m  128.9091  0.00E+00    6.53E-04
   1807      FP         52-Te-129   128.9066  0.00E+00    1.66E-04
   1808      FP         52-Te-129m  128.9074  0.00E+00    2.39E-07
   1809      FP         53-I-129    128.9050  0.00E+00    1.40E-15
   1810      FP         54-Xe-129   128.9048  0.00E+00    0.00E+00
   1811      FP         54-Xe-129m  128.9048  0.00E+00    9.03E-07
   1812      FP         55-Cs-129   128.9061  0.00E+00    6.01E-06
   1813      FP         56-Ba-129   128.9087  0.00E+00    8.63E-05
   1814      FP         47-Ag-130   129.9505  0.00E+00    1.39E+01
   1815      FP         48-Cd-130   129.9339  0.00E+00    4.28E+00
   1816      FP         49-In-130   129.9250  0.00E+00    2.39E+00
   1817      FP         49-In-130m  129.9250  0.00E+00    1.28E+00
   1818      FP         50-Sn-130   129.9140  0.00E+00    3.11E-03
   1819      FP         50-Sn-130m  129.9140  0.00E+00    6.80E-03
   1820      FP         51-Sb-130   129.9117  0.00E+00    2.92E-04
   1821      FP         51-Sb-130m  129.9117  0.00E+00    1.83E-03
   1822      FP         52-Te-130   129.9062  0.00E+00    0.00E+00
   1823      FP         53-I-130    129.9067  0.00E+00    1.56E-05
   1824      FP         53-I-130m   129.9067  0.00E+00    1.31E-03
   1825      FP         54-Xe-130   129.9035  0.00E+00    0.00E+00
   1826      FP         48-Cd-131   130.9407  0.00E+00    1.02E+01
   1827      FP         49-In-131   130.9268  0.00E+00    2.48E+00
   1828      FP         49-In-131m  130.9268  0.00E+00    1.98E+00
   1829      FP         50-Sn-131   130.9170  0.00E+00    1.24E-02
   1830      FP         50-Sn-131m  130.9170  0.00E+00    1.19E-02
   1831      FP         51-Sb-131   130.9120  0.00E+00    5.02E-04
   1832      FP         52-Te-131   130.9085  0.00E+00    4.62E-04
   1833      FP         52-Te-131m  130.9085  0.00E+00    5.79E-06
   1834      FP         53-I-131    130.9061  0.00E+00    1.00E-06
   1835      FP         54-Xe-131   130.9051  0.00E+00    0.00E+00
   1836      FP         54-Xe-131m  130.9051  0.00E+00    6.78E-07
   1837      FP         55-Cs-131   130.9055  0.00E+00    8.28E-07
   1838      FP         56-Ba-131   130.9069  0.00E+00    6.98E-07
   1839      FP         48-Cd-132   131.9456  0.00E+00    7.15E+00
   1840      FP         49-In-132   131.9330  0.00E+00    3.35E+00
   1841      FP         50-Sn-132   131.9178  0.00E+00    1.75E-02
   1842      FP         51-Sb-132   131.9145  0.00E+00    4.14E-03
   1843      FP         51-Sb-132m  131.9145  0.00E+00    2.82E-03
   1844      FP         52-Te-132   131.9086  0.00E+00    2.50E-06
   1845      FP         53-I-132    131.9080  0.00E+00    8.39E-05
   1846      FP         53-I-132m   131.9080  0.00E+00    1.39E-04
   1847      FP         54-Xe-132   131.9041  0.00E+00    0.00E+00
   1848      FP         55-Cs-132   131.9064  0.00E+00    1.24E-06
   1849      FP         56-Ba-132   131.9051  0.00E+00    0.00E+00
   1850      FP         49-In-133   132.9378  0.00E+00    4.20E+00
   1851      FP         50-Sn-133   132.9238  0.00E+00    4.75E-01
   1852      FP         51-Sb-133   132.9153  0.00E+00    4.62E-03
   1853      FP         52-Te-133   132.9110  0.00E+00    9.24E-04
   1854      FP         52-Te-133m  132.9110  0.00E+00    2.09E-04
   1855      FP         53-I-133    132.9078  0.00E+00    9.26E-06
   1856      FP         53-I-133m   132.9078  0.00E+00    7.70E-02
   1857      FP         54-Xe-133   132.9059  0.00E+00    1.53E-06
   1858      FP         54-Xe-133m  132.9059  0.00E+00    3.66E-06
   1859      FP         55-Cs-133   132.9055  0.00E+00    0.00E+00
   1860      FP         56-Ba-133   132.9060  0.00E+00    2.09E-09
   1861      FP         57-La-133   132.9082  0.00E+00    4.92E-05
   1862      FP         49-In-134   133.9442  0.00E+00    4.95E+00
   1863      FP         50-Sn-134   133.9283  0.00E+00    6.60E-01
   1864      FP         51-Sb-134   133.9204  0.00E+00    8.89E-01
   1865      FP         51-Sb-134m  133.9204  0.00E+00    6.88E-02
   1866      FP         52-Te-134   133.9114  0.00E+00    2.76E-04
   1867      FP         53-I-134    133.9097  0.00E+00    2.20E-04
   1868      FP         53-I-134m   133.9097  0.00E+00    3.28E-03
   1869      FP         54-Xe-134   133.9054  0.00E+00    0.00E+00
   1870      FP         54-Xe-134m  133.9054  0.00E+00    2.39E+00
   1871      FP         55-Cs-134   133.9067  0.00E+00    1.06E-08
   1872      FP         55-Cs-134m  133.9067  0.00E+00    6.61E-05
   1873      FP         56-Ba-134   133.9045  0.00E+00    0.00E+00
   1874      FP         49-In-135   134.9493  0.00E+00    7.53E+00
   1875      FP         50-Sn-135   134.9347  0.00E+00    1.31E+00
   1876      FP         51-Sb-135   134.9252  0.00E+00    4.13E-01
   1877      FP         52-Te-135   134.9164  0.00E+00    3.65E-02
   1878      FP         53-I-135    134.9100  0.00E+00    2.93E-05
   1879      FP         54-Xe-135   134.9072  0.00E+00    2.11E-05
   1880      FP         54-Xe-135m  134.9072  0.00E+00    7.56E-04
   1881      FP         55-Cs-135   134.9060  0.00E+00    9.55E-15
   1882      FP         55-Cs-135m  134.9060  0.00E+00    2.18E-04
   1883      FP         56-Ba-135   134.9057  0.00E+00    0.00E+00
   1884      FP         56-Ba-135m  134.9057  0.00E+00    6.71E-06
   1885      FP         57-La-135   134.9070  0.00E+00    9.87E-06
   1886      FP         58-Ce-135   134.9091  0.00E+00    1.09E-05
   1887      FP         50-Sn-136   135.9393  0.00E+00    2.77E+00
   1888      FP         51-Sb-136   135.9303  0.00E+00    7.51E-01
   1889      FP         52-Te-136   135.9201  0.00E+00    3.96E-02
   1890      FP         53-I-136    135.9147  0.00E+00    8.31E-03
   1891      FP         53-I-136m   135.9147  0.00E+00    1.48E-02
   1892      FP         54-Xe-136   135.9072  0.00E+00    0.00E+00
   1893      FP         55-Cs-136   135.9073  0.00E+00    6.10E-07
   1894      FP         55-Cs-136m  135.9073  0.00E+00    3.65E-02
   1895      FP         56-Ba-136   135.9046  0.00E+00    0.00E+00
   1896      FP         56-Ba-136m  135.9046  0.00E+00    2.25E+00
   1897      FP         50-Sn-137   136.9460  0.00E+00    3.65E+00
   1898      FP         51-Sb-137   136.9353  0.00E+00    1.54E+00
   1899      FP         52-Te-137   136.9253  0.00E+00    2.78E-01
   1900      FP         53-I-137    136.9179  0.00E+00    2.83E-02
   1901      FP         54-Xe-137   136.9116  0.00E+00    3.03E-03
   1902      FP         55-Cs-137   136.9071  0.00E+00    7.30E-10
   1903      FP         56-Ba-137   136.9058  0.00E+00    0.00E+00
   1904      FP         56-Ba-137m  136.9058  0.00E+00    4.53E-03
   1905      FP         57-La-137   136.9065  0.00E+00    3.66E-13
   1906      FP         58-Ce-137   136.9078  0.00E+00    2.14E-05
   1907      FP         51-Sb-138   137.9408  0.00E+00    4.13E+00
   1908      FP         52-Te-138   137.9292  0.00E+00    4.95E-01
   1909      FP         53-I-138    137.9223  0.00E+00    1.11E-01
   1910      FP         54-Xe-138   137.9140  0.00E+00    8.20E-04
   1911      FP         55-Cs-138   137.9110  0.00E+00    3.46E-04
   1912      FP         55-Cs-138m  137.9110  0.00E+00    3.97E-03
   1913      FP         56-Ba-138   137.9052  0.00E+00    0.00E+00
   1914      FP         57-La-138   137.9071  0.00E+00    2.15E-19
   1915      FP         58-Ce-138   137.9060  0.00E+00    0.00E+00
   1916      FP         51-Sb-139   138.9460  0.00E+00    5.46E+00
   1917      FP         52-Te-139   138.9347  0.00E+00    2.00E+00
   1918      FP         53-I-139    138.9261  0.00E+00    3.04E-01
   1919      FP         54-Xe-139   138.9188  0.00E+00    1.75E-02
   1920      FP         55-Cs-139   138.9134  0.00E+00    1.25E-03
   1921      FP         56-Ba-139   138.9088  0.00E+00    1.39E-04
   1922      FP         57-La-139   138.9064  0.00E+00    0.00E+00
   1923      FP         58-Ce-139   138.9066  0.00E+00    5.83E-08
   1924      FP         58-Ce-139m  138.9066  0.00E+00    1.26E-02
   1925      FP         59-Pr-139   138.9089  0.00E+00    4.37E-05
   1926      FP         52-Te-140   139.9388  0.00E+00    2.28E+00
   1927      FP         53-I-140    139.9310  0.00E+00    8.06E-01
   1928      FP         54-Xe-140   139.9216  0.00E+00    5.10E-02
   1929      FP         55-Cs-140   139.9173  0.00E+00    1.09E-02
   1930      FP         56-Ba-140   139.9106  0.00E+00    6.29E-07
   1931      FP         57-La-140   139.9095  0.00E+00    4.78E-06
   1932      FP         58-Ce-140   139.9054  0.00E+00    0.00E+00
   1933      FP         59-Pr-140   139.9091  0.00E+00    3.41E-03
   1934      FP         60-Nd-140   139.9095  0.00E+00    2.38E-06
   1935      FP         52-Te-141   140.9447  0.00E+00    3.25E+00
   1936      FP         53-I-141    140.9350  0.00E+00    1.61E+00
   1937      FP         54-Xe-141   140.9267  0.00E+00    4.01E-01
   1938      FP         55-Cs-141   140.9200  0.00E+00    2.79E-02
   1939      FP         56-Ba-141   140.9144  0.00E+00    6.32E-04
   1940      FP         57-La-141   140.9110  0.00E+00    4.91E-05
   1941      FP         58-Ce-141   140.9083  0.00E+00    2.47E-07
   1942      FP         59-Pr-141   140.9077  0.00E+00    0.00E+00
   1943      FP         60-Nd-141   140.9096  0.00E+00    7.73E-05
   1944      FP         60-Nd-141m  140.9096  0.00E+00    1.12E-02
   1945      FP         61-Pm-141   140.9136  0.00E+00    5.53E-04
   1946      FP         52-Te-142   141.9491  0.00E+00    3.47E+00
   1947      FP         53-I-142    141.9402  0.00E+00    3.12E+00
   1948      FP         54-Xe-142   141.9297  0.00E+00    5.64E-01
   1949      FP         55-Cs-142   141.9243  0.00E+00    4.12E-01
   1950      FP         56-Ba-142   141.9164  0.00E+00    1.09E-03
   1951      FP         57-La-142   141.9141  0.00E+00    1.27E-04
   1952      FP         58-Ce-142   141.9092  0.00E+00    0.00E+00
   1953      FP         59-Pr-142   141.9100  0.00E+00    1.01E-05
   1954      FP         59-Pr-142m  141.9100  0.00E+00    7.91E-04
   1955      FP         60-Nd-142   141.9077  0.00E+00    0.00E+00
   1956      FP         53-I-143    142.9446  0.00E+00    2.34E+00
   1957      FP         54-Xe-143   142.9351  0.00E+00    2.31E+00
   1958      FP         55-Cs-143   142.9274  0.00E+00    3.87E-01
   1959      FP         56-Ba-143   142.9206  0.00E+00    4.78E-02
   1960      FP         57-La-143   142.9161  0.00E+00    8.14E-04
   1961      FP         58-Ce-143   142.9124  0.00E+00    5.83E-06
   1962      FP         59-Pr-143   142.9108  0.00E+00    5.91E-07
   1963      FP         60-Nd-143   142.9098  0.00E+00    0.00E+00
   1964      FP         61-Pm-143   142.9109  0.00E+00    3.03E-08
   1965      FP         62-Sm-143   142.9146  0.00E+00    1.32E-03
   1966      FP         62-Sm-143m  142.9146  0.00E+00    1.05E-02
   1967      FP         53-I-144    143.9500  0.00E+00    3.57E+00
   1968      FP         54-Xe-144   143.9385  0.00E+00    6.03E-01
   1969      FP         55-Cs-144   143.9321  0.00E+00    6.97E-01
   1970      FP         56-Ba-144   143.9229  0.00E+00    6.03E-02
   1971      FP         57-La-144   143.9196  0.00E+00    1.70E-02
   1972      FP         58-Ce-144   143.9137  0.00E+00    2.82E-08
   1973      FP         59-Pr-144   143.9133  0.00E+00    6.69E-04
   1974      FP         59-Pr-144m  143.9133  0.00E+00    1.60E-03
   1975      FP         60-Nd-144   143.9101  0.00E+00    9.59E-24
   1976      FP         61-Pm-144   143.9126  0.00E+00    2.21E-08
   1977      FP         62-Sm-144   143.9120  0.00E+00    0.00E+00
   1978      FP         54-Xe-145   144.9441  0.00E+00    3.69E+00
   1979      FP         55-Cs-145   144.9355  0.00E+00    1.18E+00
   1980      FP         56-Ba-145   144.9276  0.00E+00    1.61E-01
   1981      FP         57-La-145   144.9216  0.00E+00    2.80E-02
   1982      FP         58-Ce-145   144.9172  0.00E+00    3.84E-03
   1983      FP         59-Pr-145   144.9145  0.00E+00    3.22E-05
   1984      FP         60-Nd-145   144.9126  0.00E+00    0.00E+00
   1985      FP         61-Pm-145   144.9128  0.00E+00    1.24E-09
   1986      FP         62-Sm-145   144.9134  0.00E+00    2.36E-08
   1987      FP         54-Xe-146   145.9478  0.00E+00    1.88E+00
   1988      FP         55-Cs-146   145.9403  0.00E+00    2.16E+00
   1989      FP         56-Ba-146   145.9302  0.00E+00    3.12E-01
   1990      FP         57-La-146   145.9258  0.00E+00    1.11E-01
   1991      FP         57-La-146m  145.9258  0.00E+00    6.93E-02
   1992      FP         58-Ce-146   145.9188  0.00E+00    8.54E-04
   1993      FP         59-Pr-146   145.9176  0.00E+00    4.78E-04
   1994      FP         60-Nd-146   145.9131  0.00E+00    0.00E+00
   1995      FP         61-Pm-146   145.9147  0.00E+00    3.97E-09
   1996      FP         62-Sm-146   145.9130  0.00E+00    2.13E-16
   1997      FP         54-Xe-147   146.9536  0.00E+00    6.93E+00
   1998      FP         55-Cs-147   146.9442  0.00E+00    3.01E+00
   1999      FP         56-Ba-147   146.9350  0.00E+00    7.75E-01
   2000      FP         57-La-147   146.9282  0.00E+00    1.71E-01
   2001      FP         58-Ce-147   146.9227  0.00E+00    1.23E-02
   2002      FP         59-Pr-147   146.9190  0.00E+00    8.62E-04
   2003      FP         60-Nd-147   146.9161  0.00E+00    7.31E-07
   2004      FP         61-Pm-147   146.9151  0.00E+00    8.37E-09
   2005      FP         62-Sm-147   146.9149  0.00E+00    2.07E-19
   2006      FP         63-Eu-147   146.9167  0.00E+00    3.33E-07
   2007      FP         64-Gd-147   146.9191  0.00E+00    5.06E-06
   2008      FP         55-Cs-148   147.9492  0.00E+00    4.75E+00
   2009      FP         56-Ba-148   147.9377  0.00E+00    1.13E+00
   2010      FP         57-La-148   147.9322  0.00E+00    5.50E-01
   2011      FP         58-Ce-148   147.9244  0.00E+00    1.24E-02
   2012      FP         59-Pr-148   147.9221  0.00E+00    5.04E-03
   2013      FP         59-Pr-148m  147.9221  0.00E+00    5.75E-03
   2014      FP         60-Nd-148   147.9169  0.00E+00    0.00E+00
   2015      FP         61-Pm-148   147.9175  0.00E+00    1.49E-06
   2016      FP         61-Pm-148m  147.9207  0.00E+00    1.94E-07
   2017      FP         62-Sm-148   147.9148  0.00E+00    3.14E-24
   2018      FP         55-Cs-149   148.9529  0.00E+00    1.39E+01
   2019      FP         56-Ba-149   148.9426  0.00E+00    2.02E+00
   2020      FP         57-La-149   148.9347  0.00E+00    6.60E-01
   2021      FP         58-Ce-149   148.9284  0.00E+00    1.31E-01
   2022      FP         59-Pr-149   148.9237  0.00E+00    5.11E-03
   2023      FP         60-Nd-149   148.9202  0.00E+00    1.11E-04
   2024      FP         61-Pm-149   148.9183  0.00E+00    3.63E-06
   2025      FP         62-Sm-149   148.9172  0.00E+00    0.00E+00
   2026      FP         63-Eu-149   148.9179  0.00E+00    8.62E-08
   2027      FP         64-Gd-149   148.9193  0.00E+00    8.65E-07
   2028      FP         55-Cs-150   149.9582  0.00E+00    1.39E+01
   2029      FP         56-Ba-150   149.9457  0.00E+00    2.31E+00
   2030      FP         57-La-150   149.9388  0.00E+00    8.06E-01
   2031      FP         58-Ce-150   149.9304  0.00E+00    1.73E-01
   2032      FP         59-Pr-150   149.9267  0.00E+00    1.12E-01
   2033      FP         60-Nd-150   149.9209  0.00E+00    2.78E-27
   2034      FP         61-Pm-150   149.9210  0.00E+00    7.18E-05
   2035      FP         62-Sm-150   149.9173  0.00E+00    0.00E+00
   2036      FP         55-Cs-151   150.9622  0.00E+00    1.39E+01
   2037      FP         56-Ba-151   150.9508  0.00E+00    2.68E+00
   2038      FP         57-La-151   150.9417  0.00E+00    8.91E-01
   2039      FP         58-Ce-151   150.9340  0.00E+00    3.94E-01
   2040      FP         59-Pr-151   150.9283  0.00E+00    3.67E-02
   2041      FP         60-Nd-151   150.9238  0.00E+00    9.29E-04
   2042      FP         61-Pm-151   150.9212  0.00E+00    6.78E-06
   2043      FP         62-Sm-151   150.9199  0.00E+00    2.44E-10
   2044      FP         63-Eu-151   150.9198  0.00E+00    0.00E+00
   2045      FP         64-Gd-151   150.9203  0.00E+00    6.47E-08
   2046      FP         65-Tb-151   150.9231  0.00E+00    1.09E-05
   2047      FP         56-Ba-152   151.9543  0.00E+00    3.04E+00
   2048      FP         57-La-152   151.9462  0.00E+00    1.54E+00
   2049      FP         58-Ce-152   151.9365  0.00E+00    4.95E-01
   2050      FP         59-Pr-152   151.9315  0.00E+00    1.91E-01
   2051      FP         60-Nd-152   151.9247  0.00E+00    1.01E-03
   2052      FP         61-Pm-152   151.9235  0.00E+00    2.80E-03
   2053      FP         61-Pm-152m  151.9235  0.00E+00    1.54E-03
   2054      FP         62-Sm-152   151.9197  0.00E+00    0.00E+00
   2055      FP         63-Eu-152   151.9217  0.00E+00    1.62E-09
   2056      FP         63-Eu-152m  151.9217  0.00E+00    2.07E-05
   2057      FP         64-Gd-152   151.9198  0.00E+00    2.03E-22
   2058      FP         56-Ba-153   152.9596  0.00E+00    4.39E+00
   2059      FP         57-La-153   152.9496  0.00E+00    2.03E+00
   2060      FP         58-Ce-153   152.9406  0.00E+00    7.08E-01
   2061      FP         59-Pr-153   152.9338  0.00E+00    1.62E-01
   2062      FP         60-Nd-153   152.9277  0.00E+00    2.19E-02
   2063      FP         61-Pm-153   152.9241  0.00E+00    2.20E-03
   2064      FP         62-Sm-153   152.9221  0.00E+00    4.14E-06
   2065      FP         63-Eu-153   152.9212  0.00E+00    0.00E+00
   2066      FP         64-Gd-153   152.9218  0.00E+00    3.34E-08
   2067      FP         65-Tb-153   152.9234  0.00E+00    3.43E-06
   2068      FP         57-La-154   153.9545  0.00E+00    3.04E+00
   2069      FP         58-Ce-154   153.9434  0.00E+00    8.94E-01
   2070      FP         59-Pr-154   153.9375  0.00E+00    3.01E-01
   2071      FP         60-Nd-154   153.9295  0.00E+00    2.68E-02
   2072      FP         61-Pm-154   153.9265  0.00E+00    6.68E-03
   2073      FP         61-Pm-154m  153.9265  0.00E+00    4.31E-03
   2074      FP         62-Sm-154   153.9222  0.00E+00    0.00E+00
   2075      FP         63-Eu-154   153.9230  0.00E+00    2.55E-09
   2076      FP         63-Eu-154m  153.9230  0.00E+00    2.51E-04
   2077      FP         64-Gd-154   153.9209  0.00E+00    0.00E+00
   2078      FP         57-La-155   154.9583  0.00E+00    3.77E+00
   2079      FP         58-Ce-155   154.9480  0.00E+00    1.47E+00
   2080      FP         59-Pr-155   154.9401  0.00E+00    8.14E-01
   2081      FP         60-Nd-155   154.9329  0.00E+00    7.79E-02
   2082      FP         61-Pm-155   154.9281  0.00E+00    1.67E-02
   2083      FP         62-Sm-155   154.9246  0.00E+00    5.18E-04
   2084      FP         63-Eu-155   154.9229  0.00E+00    4.62E-09
   2085      FP         64-Gd-155   154.9226  0.00E+00    0.00E+00
   2086      FP         64-Gd-155m  154.9226  0.00E+00    2.17E+01
   2087      FP         65-Tb-155   154.9235  0.00E+00    1.51E-06
   2088      FP         66-Dy-155   154.9258  0.00E+00    1.94E-05
   2089      FP         58-Ce-156   155.9513  0.00E+00    1.88E+00
   2090      FP         59-Pr-156   155.9443  0.00E+00    9.46E-01
   2091      FP         60-Nd-156   155.9350  0.00E+00    1.26E-01
   2092      FP         61-Pm-156   155.9311  0.00E+00    2.60E-02
   2093      FP         62-Sm-156   155.9255  0.00E+00    2.05E-05
   2094      FP         63-Eu-156   155.9247  0.00E+00    5.28E-07
   2095      FP         64-Gd-156   155.9221  0.00E+00    0.00E+00
   2096      FP         65-Tb-156   155.9247  0.00E+00    1.50E-06
   2097      FP         65-Tb-156m  155.9247  0.00E+00    7.89E-06
   2098      FP         66-Dy-156   155.9243  0.00E+00    0.00E+00
   2099      FP         58-Ce-157   156.9563  0.00E+00    2.85E+00
   2100      FP         59-Pr-157   156.9474  0.00E+00    1.16E+00
   2101      FP         60-Nd-157   156.9390  0.00E+00    3.64E-01
   2102      FP         61-Pm-157   156.9330  0.00E+00    6.56E-02
   2103      FP         62-Sm-157   156.9284  0.00E+00    1.44E-03
   2104      FP         63-Eu-157   156.9254  0.00E+00    1.27E-05
   2105      FP         64-Gd-157   156.9240  0.00E+00    0.00E+00
   2106      FP         65-Tb-157   156.9240  0.00E+00    3.09E-10
   2107      FP         66-Dy-157   156.9255  0.00E+00    2.37E-05
   2108      FP         59-Pr-158   157.9520  0.00E+00    5.17E+00
   2109      FP         60-Nd-158   157.9416  0.00E+00    5.21E-01
   2110      FP         61-Pm-158   157.9366  0.00E+00    1.44E-01
   2111      FP         62-Sm-158   157.9300  0.00E+00    2.18E-03
   2112      FP         63-Eu-158   157.9279  0.00E+00    2.52E-04
   2113      FP         64-Gd-158   157.9241  0.00E+00    0.00E+00
   2114      FP         65-Tb-158   157.9254  0.00E+00    1.22E-10
   2115      FP         65-Tb-158m  157.9254  0.00E+00    6.48E-02
   2116      FP         66-Dy-158   157.9244  0.00E+00    0.00E+00
   2117      FP         59-Pr-159   158.9555  0.00E+00    6.57E+00
   2118      FP         60-Nd-159   158.9461  0.00E+00    8.97E-01
   2119      FP         61-Pm-159   158.9390  0.00E+00    4.72E-01
   2120      FP         62-Sm-159   158.9332  0.00E+00    6.10E-02
   2121      FP         63-Eu-159   158.9291  0.00E+00    6.38E-04
   2122      FP         64-Gd-159   158.9264  0.00E+00    1.04E-05
   2123      FP         65-Tb-159   158.9254  0.00E+00    0.00E+00
   2124      FP         66-Dy-159   158.9257  0.00E+00    5.56E-08
   2125      FP         67-Ho-159   158.9277  0.00E+00    3.50E-04
   2126      FP         67-Ho-159m  158.9277  0.00E+00    8.35E-02
   2127      FP         60-Nd-160   159.9491  0.00E+00    1.18E+00
   2128      FP         61-Pm-160   159.9430  0.00E+00    4.44E-01
   2129      FP         62-Sm-160   159.9351  0.00E+00    7.22E-02
   2130      FP         63-Eu-160   159.9320  0.00E+00    1.82E-02
   2131      FP         64-Gd-160   159.9270  0.00E+00    0.00E+00
   2132      FP         65-Tb-160   159.9272  0.00E+00    1.11E-07
   2133      FP         66-Dy-160   159.9252  0.00E+00    0.00E+00
   2134      FP         60-Nd-161   160.9539  0.00E+00    1.42E+00
   2135      FP         61-Pm-161   160.9459  0.00E+00    6.51E-01
   2136      FP         62-Sm-161   160.9388  0.00E+00    1.44E-01
   2137      FP         63-Eu-161   160.9337  0.00E+00    2.67E-02
   2138      FP         64-Gd-161   160.9297  0.00E+00    3.16E-03
   2139      FP         65-Tb-161   160.9276  0.00E+00    1.16E-06
   2140      FP         66-Dy-161   160.9269  0.00E+00    0.00E+00
   2141      FP         67-Ho-161   160.9279  0.00E+00    7.76E-05
   2142      FP         67-Ho-161m  160.9279  0.00E+00    1.03E-01
   2143      FP         68-Er-161   160.9300  0.00E+00    6.00E-05
   2144      FP         61-Pm-162   161.9503  0.00E+00    2.59E+00
   2145      FP         62-Sm-162   161.9412  0.00E+00    2.89E-01
   2146      FP         63-Eu-162   161.9370  0.00E+00    6.54E-02
   2147      FP         64-Gd-162   161.9310  0.00E+00    1.38E-03
   2148      FP         65-Tb-162   161.9295  0.00E+00    1.52E-03
   2149      FP         66-Dy-162   161.9268  0.00E+00    0.00E+00
   2150      FP         67-Ho-162   161.9291  0.00E+00    7.70E-04
   2151      FP         67-Ho-162m  161.9291  0.00E+00    1.72E-04
   2152      FP         68-Er-162   161.9288  0.00E+00    0.00E+00
   2153      FP         61-Pm-163   162.9537  0.00E+00    3.47E+00
   2154      FP         62-Sm-163   162.9454  0.00E+00    3.97E-01
   2155      FP         63-Eu-163   162.9392  0.00E+00    9.00E-02
   2156      FP         64-Gd-163   162.9340  0.00E+00    1.02E-02
   2157      FP         65-Tb-163   162.9306  0.00E+00    5.92E-04
   2158      FP         66-Dy-163   162.9287  0.00E+00    0.00E+00
   2159      FP         67-Ho-163   162.9287  0.00E+00    4.81E-12
   2160      FP         67-Ho-163m  162.9287  0.00E+00    6.36E-01
   2161      FP         68-Er-163   162.9300  0.00E+00    1.54E-04
   2162      FP         62-Sm-164   163.9483  0.00E+00    5.65E-01
   2163      FP         63-Eu-164   163.9430  0.00E+00    2.44E-01
   2164      FP         64-Gd-164   163.9359  0.00E+00    1.54E-02
   2165      FP         65-Tb-164   163.9333  0.00E+00    3.85E-03
   2166      FP         66-Dy-164   163.9292  0.00E+00    0.00E+00
   2167      FP         67-Ho-164   163.9302  0.00E+00    3.98E-04
   2168      FP         67-Ho-164m  163.9302  0.00E+00    3.08E-04
   2169      FP         68-Er-164   163.9292  0.00E+00    0.00E+00
   2170      FP         62-Sm-165   164.9530  0.00E+00    9.07E-01
   2171      FP         63-Eu-165   164.9457  0.00E+00    3.01E-01
   2172      FP         64-Gd-165   164.9394  0.00E+00    6.73E-02
   2173      FP         65-Tb-165   164.9349  0.00E+00    5.47E-03
   2174      FP         66-Dy-165   164.9317  0.00E+00    8.25E-05
   2175      FP         66-Dy-165m  164.9317  0.00E+00    9.19E-03
   2176      FP         67-Ho-165   164.9303  0.00E+00    0.00E+00
   2177      FP         68-Er-165   164.9307  0.00E+00    1.86E-05
   2178      FP         69-Tm-165   164.9324  0.00E+00    6.41E-06
   2179      FP         63-Eu-166   165.9500  0.00E+00    1.73E+00
   2180      FP         64-Gd-166   165.9416  0.00E+00    1.44E-01
   2181      FP         65-Tb-166   165.9380  0.00E+00    2.76E-02
   2182      FP         66-Dy-166   165.9328  0.00E+00    2.36E-06
   2183      FP         67-Ho-166   165.9323  0.00E+00    7.18E-06
   2184      FP         67-Ho-166m  165.9324  0.00E+00    1.83E-11
   2185      FP         68-Er-166   165.9303  0.00E+00    0.00E+00
   2186      FP         69-Tm-166   165.9335  0.00E+00    2.50E-05
   2187      FP         70-Yb-166   165.9339  0.00E+00    3.40E-06
   2188      FP         63-Eu-167   166.9532  0.00E+00    3.47E+00
   2189      FP         64-Gd-167   166.9456  0.00E+00    2.31E-01
   2190      FP         65-Tb-167   166.9400  0.00E+00    3.57E-02
   2191      FP         66-Dy-167   166.9357  0.00E+00    1.86E-03
   2192      FP         67-Ho-167   166.9331  0.00E+00    6.21E-05
   2193      FP         68-Er-167   166.9321  0.00E+00    0.00E+00
   2194      FP         68-Er-167m  166.9321  0.00E+00    3.05E-01
   2195      FP         69-Tm-167   166.9328  0.00E+00    8.67E-07
   2196      FP         70-Yb-167   166.9350  0.00E+00    6.60E-04
   2197      FP         64-Gd-168   167.9484  0.00E+00    2.31E+00
   2198      FP         65-Tb-168   167.9436  0.00E+00    8.45E-02
   2199      FP         66-Dy-168   167.9371  0.00E+00    1.33E-03
   2200      FP         67-Ho-168   167.9355  0.00E+00    3.86E-03
   2201      FP         68-Er-168   167.9324  0.00E+00    0.00E+00
   2202      FP         69-Tm-168   167.9342  0.00E+00    8.62E-08
   2203      FP         70-Yb-168   167.9339  0.00E+00    0.00E+00
   2204      FP         64-Gd-169   168.9529  0.00E+00    6.93E-01
   2205      FP         65-Tb-169   168.9462  0.00E+00    3.47E-01
   2206      FP         66-Dy-169   168.9403  0.00E+00    1.78E-02
   2207      FP         67-Ho-169   168.9369  0.00E+00    2.45E-03
   2208      FP         68-Er-169   168.9346  0.00E+00    8.54E-07
   2209      FP         69-Tm-169   168.9342  0.00E+00    0.00E+00
   2210      FP         70-Yb-169   168.9352  0.00E+00    2.51E-07
   2211      FP         70-Yb-169m  168.9352  0.00E+00    1.51E-02
   2212      FP         71-Lu-169   168.9377  0.00E+00    5.65E-06
   2213      FP         71-Lu-169m  168.9377  0.00E+00    4.33E-03
   2214      FP         65-Tb-170   169.9503  0.00E+00    2.31E-01
   2215      FP         66-Dy-170   169.9424  0.00E+00    2.31E-02
   2216      FP         67-Ho-170   169.9396  0.00E+00    4.19E-03
   2217      FP         67-Ho-170m  169.9396  0.00E+00    1.61E-02
   2218      FP         68-Er-170   169.9355  0.00E+00    0.00E+00
   2219      FP         69-Tm-170   169.9358  0.00E+00    6.24E-08
   2220      FP         70-Yb-170   169.9348  0.00E+00    0.00E+00
   2221      FP         65-Tb-171   170.9533  0.00E+00    1.39E+00
   2222      FP         66-Dy-171   170.9462  0.00E+00    1.16E-01
   2223      FP         67-Ho-171   170.9415  0.00E+00    1.31E-02
   2224      FP         68-Er-171   170.9380  0.00E+00    2.56E-05
   2225      FP         69-Tm-171   170.9364  0.00E+00    1.14E-08
   2226      FP         70-Yb-171   170.9363  0.00E+00    0.00E+00
   2227      FP         71-Lu-171   170.9379  0.00E+00    9.74E-07
   2228      FP         71-Lu-171m  170.9379  0.00E+00    8.77E-03
   2229      FP         72-Hf-171   170.9405  0.00E+00    1.59E-05
   2230      FP         66-Dy-172   171.9488  0.00E+00    2.31E-01
   2231      FP         67-Ho-172   171.9448  0.00E+00    2.77E-02
   2232      FP         68-Er-172   171.9394  0.00E+00    3.91E-06
   2233      FP         69-Tm-172   171.9384  0.00E+00    3.03E-06
   2234      FP         70-Yb-172   171.9364  0.00E+00    0.00E+00
   2235      FP         71-Lu-172   171.9391  0.00E+00    1.20E-06
   2236      FP         71-Lu-172m  171.9391  0.00E+00    3.12E-03
   2237      FP         72-Hf-172   171.9395  0.00E+00    1.17E-08
   ========= ========== =========== ========= =========== =========

.. bibliography:: bibs/data-resource-refs.bib
