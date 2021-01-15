.. _5-0:

Depletion, Activation, and Spent Fuel Source Terms Overview
===========================================================

*Introduction by W. A. Wieselquist*

SCALE’s general depletion, activation, and spent fuel source terms analysis
capabilities are enabled through a family of modules related to the main ORIGEN
depletion/irradiation/decay solver. The nuclide tracking in ORIGEN is based on
the principle of explicitly modeling all available nuclides and transitions in
the current fundamental nuclear data for decay and neutron-induced transmutation
and relies on fundamental cross section and decay data in ENDF/B VII. Cross
section data for materials and reaction processes not available in ENDF/B-VII
are obtained from the JEFF-3.0/A special purpose European activation library
containing 774 materials and 23 reaction channels with 12,617 neutron-induced
reactions below 20 MeV. Resonance cross section corrections in the resolved and
unresolved range are performed using a continuous-energy treatment by data
modules in SCALE. All nuclear decay data, fission product yields, and gamma-ray
emission data are developed from ENDF/B-VII.1 evaluations. Decay data include
all ground and metastable state nuclides with half-lives greater than 1
millisecond. Using these data sources, ORIGEN currently tracks 174 actinides,
1149 fission products, and 974 activation products. The purpose of this chapter
is to describe the stand-alone capabilities and underlying methodology of
ORIGEN—as opposed to the integrated depletion capability it provides in all
coupled neutron transport/depletion sequences in SCALE, as described in other
chapters. Through the stand-alone capabilities, there is generality to handle
arbitrary systems (e.g., fast reactor fuel depletion or structural activation)
by providing arbitrary flux spectra and arbitrary one-group cross sections to
the module COUPLE, which in turn creates ORIGEN library (.f33) files containing
the problem-dependent, one-group reaction coefficients required to solve the
actual equations governing depletion/decay. These libraries are required input
for the ORIGEN module, along with the initial isotopics and irradiation history,
in terms of either a time-dependent power or flux level. Two high-performance
equation solvers are available: the hybrid linear chains and matrix exponential
method and a new Chebyshev Rational Approximation Method (CRAM). Typical
execution times are on the order of a few seconds for a multi-step solution,
with each individual solution (step) taking approximately 10 milliseconds.
ORIGEN also includes capabilities for continuous feed and removal by element.
Output capabilities include isotopics (moles or grams), source spectra (alpha,
beta, gamma, and neutron), activity (becquerels or curies), decay heat (total
watts or gamma only), and radiological hazard factors (maximum permissible
concentrations in air or water). These results can be displayed in the output
file (.out extension) and/or archived in an ORIGEN binary results file (.f71
extension). The use of current, fundamental data resources is a key feature of
ORIGEN, including nuclear decay data, multigroup neutron reaction cross
sections, neutron-induced fission product yields, and decay emission data for
photons, neutrons, alpha particles, and beta particles. The nuclear decay data
are based primarily on ENDF/B-VII.1 evaluations. The multigroup nuclear reaction
cross section libraries now include evaluations from the JEFF 3.0/A neutron
activation file containing data for 774 target nuclides, more than 12,000
neutron-induced reactions, and more than 20 different reaction types below 20
MeV, provided in various energy group structures. Energy-dependent
ENDF/B-VII.0-based fission product yields are available for 30 fissionable
actinides. Gamma-ray and x-ray emission data libraries are based on
ENDF/B-VII.1. The photon libraries contain discrete photon line energy and
intensity data for decay gamma-ray and x-rays emission for 1,132 radionuclides,
prompt and delayed continuum spectra for spontaneous fission, (α,n) reactions in
oxide fuel, and bremsstrahlung from decay beta (electron and positron) particles
slowing down in either a UO2 fuel or water matrix. Methods and data libraries
used to calculate the neutron yields and energy spectra for spontaneous fission,
(α,n) reactions, and delayed neutron emission are adopted from the SOURCES4C
code. Capabilities to calculate the beta and alpha particle emission source and
spectra have also been added.

The ORIGEN reactor libraries distributed with SCALE include a set of
pre-calculated ORIGEN libraries (with TRITON) for a variety of fuel assembly
designs:

  -	BWR 7×7, 8×8-1, 8×8-2, 9×9-2, 9×9-9, 10×10-9, 10×10-8, SVEA-64,
    SVEA-96, and SVEA-100;

  -	PWR 14×14, 15×15, 16×16, 17×17, 18×18;

  -	CANDU reactor (19-, 28-, and 37-element bundle designs);

  -	Magnox graphite reactor;

  -	Advanced Gas-Cooled Reactor (AGR);

  -	VVER 440 and VVER 1000;

  -	RBMK;

  -	IRT;

  -	MOX BWR 7×7, 8×8-1, 8×8-2, 9×9-2, 9×9-9, 10×10-9, 10×10-8, SVEA-64, SVEA-96, and
    SVEA-100;

  -	MOX PWR 14×14, 15×15, 16×16, 17×17, 18×18.

These libraries may be
used to rapidly assess spent fuel isotopics and source terms in these systems
for arbitrary burnups and decay times. For UO2-based assembly isotopics, the new
ORIGAMI sequence provides a very convenient, easy-to-use interface. The most
general capability, and requiring more user input, is available using the ARP
interpolator module in conjunction with the ORIGEN solver module. Finally, with
regards to user interfaces, ORIGEN has a new keyword-based input in SCALE 6.2
but also maintains the ability to read SCALE 6.1 input. Both ORIGEN and ORIGAMI
are tightly integrated with the SCALE graphical user interface, Fulcrum, which
includes syntax highlighting, input checking with immediate feedback, and (.f71)
output viewing. Additionally, Fulcrum provides an ORIGAMI Automator project
interface to characterize the fuel inventory for an entire reactor site and
generate data needed for severe accident analysis. ORIGAMI Automator is not
documented in this chapter, but a primer is available with step by step
instructions on its use.
