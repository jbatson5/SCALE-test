Deterministic Transport Overview
================================

*Introduction by S. M. Bowman*

SCALE deterministic transport capabilities enable criticality safety,
depletion, sensitivity, and uncertainty analysis, as well as hybrid
approaches to Monte Carlo analysis. SCALE provides a one-dimensional
(1D) transport solver for eigenvalue neutronics and fixed source
neutron-gamma analysis with XSDRN, two-dimensional (2D) eigenvalue
neutronics with NEWT, and a three-dimensional (3D) transport solver for
hybrid acceleration of Monte Carlo fixed source and eigenvalue
calculations with Denovo. Generally, the use of these transport solvers
in SCALE is best accessed through the capability specific sequences:
CSAS and Sourcerer for criticality safety, TRITON for 1D and 2D
depletion, TSUNAMI‑1D and TSUNAMI-2D for sensitivity and uncertainty
analysis, and MAVRIC for 3D fixed source hybrid Monte Carlo analysis.

XSDRN
-----

XSDRN is a multigroup discrete-ordinates code that solves the 1D
Boltzmann equation in slab, cylindrical, or spherical coordinates.
Alternatively, the user can select P1 diffusion theory, infinite medium
theory, or Bn theory. A variety of calculational types is available,
including fixed source, eigenvalue, or search calculations. In SCALE,
XSDRN is used for several purposes: eigenvalue (*k*\ :sub:`eff`) determination;
cross section collapsing; and computation of fundamental-mode or
generalized adjoint functions for sensitivity analysis.

NEWT
----

NEWT (New ESC-based Weighting Transport code) is a multigroup
discrete-ordinates radiation transport computer code with flexible
meshing capabilities that allow 2D neutron transport calculations using
complex geometric models. The differencing scheme employed by NEWT—the
Extended Step Characteristic approach—allows a computational mesh based
on arbitrary polygons. Such a mesh can be used to closely approximate
curved or irregular surfaces to provide the capability to model problems
that were formerly difficult or impractical to model directly with
discrete-ordinates methods. Automated grid generation capabilities
provide a simplified user input specification in which elementary bodies
can be defined and placed within a problem domain. NEWT can be used for
eigenvalue, critical-buckling correction, and source calculations, and
it can be used to prepare collapsed weighted cross sections in AMPX
working library format.

Like other SCALE modules, NEWT can be run as a standalone module or as
part of a SCALE sequence. NEWT has been incorporated into SCALE TRITON
control module sequences. TRITON can be used simply to prepare
cross sections for a NEWT transport calculation and then automatically
execute NEWT. TRITON also provides the capability to perform 2D
depletion calculations in which the transport capabilities of NEWT are
combined with multiple ORIGEN depletion calculations to perform 2D
depletion of complex geometries. In the TRITON depletion sequence, NEWT
can also be used to generate lattice-physics parameters and
cross sections for use in subsequent nodal core simulator calculations.
In addition, the SCALE TSUNAMI-2D sequence can be used to perform
sensitivity and uncertainty analysis of 2D geometries in which NEWT is
used to compute the adjoint flux solution to generate sensitivity
coefficients for *k\ eff* and other responses of interest with respect
to the cross sections used in the NEWT model.

DENOVO
------

Denovo [1]_ is a parallel 3D discrete-ordinates code available in SCALE
as part of two control module sequences for different applications, as
described below. Because Denovo can only be run in SCALE via the Monaco
with Automated Variance Reduction using Importance Calculations (MAVRIC)
or Denovo Eigenvalue Calculation (DEVC) as developed for use with
Sourcerer, it is not documented separately in the section entitled
“Deterministic Transport” in this manual.

The MAVRIC hybrid Monte Carlo radiation shielding sequence employs the
Consistent Adjoint Driven Importance Sampling (CADIS) and
Forward-Weighted CADIS (FW-CADIS) methodologies. Denovo is used to
generate adjoint (and, for FW-CADIS, forward) scalar fluxes for the
CADIS methods in MAVRIC. This adjoint flux information is then used by
MAVRIC to construct a space- and energy-dependent importance map (i.e.,
weight windows) to be used for biasing during Monte Carlo particle
transport and as a mesh-based biased source distribution. For use in
MAVRIC/CADIS, it is highly desirable that the S\ :sub:`N` code be fast,
positive, and robust. The phase-space shape of the forward and adjoint
fluxes, as opposed to a highly accurate solution, is the most important
quality for Monte Carlo weight-window generation. Accordingly, Denovo
provides a step-characteristics spatial differencing option that
produces positive scalar fluxes as long as the source (volume plus
in-scatter) is positive. Denovo uses an orthogonal, nonuniform mesh that
is ideal for CADIS applications because of the speed and robustness of
calculations on this mesh type. Denovo can be run stand-alone in MAVRIC
to perform fixed source calculations using the *PARM=forward* (for
forward Denovo) or *PARM=adjoint* (for adjoint Denovo). See the MAVRIC
chapter for details.

The other sequence that uses Denovo is the DEVC sequence. DEVC generates
a reasonably accurate starting source through a Denovo eigenvalue
calculation so that Sourcerer can improve the KENO/CSAS Monte Carlo
calculation by (1) reducing the number of skipped generations required
to converge the fission source distribution in the KENO solution, and
(2) increasing the reliability of the final eigenvalue
(:math:`k_{\mathrm{\text{eff}}}`) for problems with loosely coupled
fissionable areas. Denovo can be run stand-alone in DEVC for calculating
criticality eigenvalue problems. This sequence reads an input file very
similar to a CSAS6 input file that contains an extra block of input for
describing the Denovo mesh grid and calculational parameters. See the
Sourcerer chapter for details.

Reference
---------

.. [1]
   T. M. Evans, A. S. Stafford, R. N. Slaybaugh, and K. T. Clarno,
   “Denovo: A New Three-Dimensional Parallel Discrete Ordinates Code in
   SCALE,” *Nuclear Technology* **171**, 171–200 (2010).
