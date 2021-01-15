.. _6-4:

TSAR: Tool for Sensitivity Analysis of Reactivity Responses
===========================================================

ABSTRACT

TSAR (Tool for Sensitivity Analysis of Reactivity Responses) is a SCALE
functional module that computes nuclear data sensitivity coefficients for
eigenvalue-difference responses such as reactor reactivity and worth
coefficients.  Examples include void reactivity, Doppler coefficients, and
control rod worths.  TSAR reads previously computed sensitivity coefficients for
the k-eigenvalues at two states of a reactor system (or for two different
systems) and combines them to obtain sensitivity coefficients for the
difference.  The k-eigenvalue sensitivities are typically obtained using the
TSUNAMI-3D or -1D control sequences in SCALE.  The reactivity sensitivity
coefficients are combined with nuclear data covariance information to determine
the uncertainty in the reactivity response.

ACKNOWLEDGMENT

Development of the TSAR code was funded by the U. S. Nuclear Regulatory
Commission Office of Research.

.. _6-4-1:

Introduction
------------

The TSUNAMI-1D, -2D, or -3D control sequences in SCALE compute
multigroup sensitivity coefficients and uncertainties for the critical
multiplication factor *k*, the reciprocal of the λ-eigenvalue of the
neutron transport equation for a multiplying medium. The TSAR module in
SCALE performs sensitivity/uncertainty (S/U) calculations for responses
represented by the *difference* of two eigenvalues. These types of
responses are often of interest in reactor physics applications. For
example, TSAR can compute data sensitivities and uncertainties of
reactivity responses such as control rod worths, fuel and moderator
temperature coefficients, and void coefficients for two defined states
of a power reactor :cite:`williams_sensitivity_2006`. Another potential application is in the
analysis of benchmark critical experiments for nuclear data testing and
validation studies. Data and methods deficiencies can introduce a
computational bias manifested as a trend in calculated critical
eigenvalues versus experiment parameters. TSAR can be applied to the
*difference* in the computed eigenvalues of two benchmarks to establish
the sensitivity of the bias trend to various nuclear data used in the
calculations.

TSAR builds upon capabilities of other SCALE modules. TSUNAMI is first
used to calculate sensitivities for the multiplication factors of the
reference and altered states of the reactor, respectively. TSAR reads
the sensitivity data files (.sdf file) produced by TSUNAMI *k\ eff*
calculations and uses them to compute relative or absolute sensitivities
of an eigenvalue-difference response. The reactivity sensitivities are
written to an output file for subsequent applications or visualization.
TSAR also combines the calculated reactivity sensitivity coefficients
with input nuclear data covariance matrices included in SCALE to
determine the uncertainty of the reactivity response.

.. _6-4-2:

Methodology
-----------

A detailed description of the S/U methodology for reactivity responses is given
in Reference D D; thus, only a brief overview is presented here.  The
lambda-eigenvalue form of the neutron transport equation for a multiplying
medium is given by

.. math::
  :label: eq6-4-1

  (\mathbf{L}-\lambda \mathbf{P}) \Phi=0

where L and P are the loss and production operators, respectively, for
the Boltzmann equation describing a multiplying medium and :math:`\lambda =\frac{1}{k}`  is the
fundamental lambda-eigenvalue. It is assumed that the system is
initially in a well-defined state 1 having a lambda- eigenvalue of
λ\ :sub:`1.` The reactivity for state 1 is defined as :math:`{{\rho }_{\text{1}}}\ =\ \text{1}\,-{{\lambda }_{\text{1}}}` . Suppose that
changes in L and/or P transformed the original system into a new
distinct configuration designated as state 2, with the lambda eigenvalue
of λ\ :sub:`2` and static reactivity of ρ\ :sub:`2` = 1- λ\ :sub:`2`.
For example, the configuration change could be caused by moving a
control rod or by voiding of the coolant. The reactivity
insertion/withdrawal associated with the designated change in conditions
is defined as

.. math::
  :label: eq6-4-2

  \rho_{1 \rightarrow 2}=\rho_{2}-\rho_{1}=\lambda_{1}-\lambda_{2} .

:eq:`eq6-4-2` defines the eigenvalue-difference (i.e., reactivity) response
addressed by TSAR.  The code edits the eigenvalues for the two reactor states
and the value of the reactivity obtained from :eq:`eq6-4-2`.

.. _6-4-2-1:

Reactivity sensitivity coefficients
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The relative k-sensitivity coefficient for an arbitrary data parameter α
appearing in the transport equation is equal to

.. math::
  :label: eq6-4-3

  \mathrm{S}_{\mathrm{k}, \alpha}=\frac{\alpha \partial \mathrm{k}}{\mathrm{k} \partial \alpha}=-\frac{\alpha \partial \lambda}{\lambda \partial \alpha}

An analogous expression defines the relative sensitivity coefficient of the
reactivity response:

.. math::
  :label: eq6-4-4

  \mathrm{S}_{\rho, \alpha}=\frac{\alpha \partial \rho_{1 \rightarrow 2}}{\rho_{1 \rightarrow 2} \partial \alpha}

Unlike the multiplication factor, the reactivity response can be negative.
This can be source of confusion when interpreting the relative sensitivity
coefficient; hence, by convention TSAR defines sensitivities relative to the
*absolute value* of the reactivity; thus,

.. math::
  :label: eq6-4-5

  \mathrm{S}_{\rho, \alpha} \rightarrow \frac{\alpha}{\left|\rho_{1 \rightarrow 2}\right|} \frac{\partial \rho_{1 \rightarrow 2}}{\partial \alpha} .

In this way, a positive value for the relative sensitivity coefficient means
that increasing the value of α always increases the value of the reactivity
(i.e., a positive ρ becomes more positive, and a negative ρ becomes less
negative).  Conversely, a negative relative sensitivity coefficient means that
increasing α always decreases the reactivity (i.e., a positive ρ becomes less
positive, and a negative ρ becomes more negative).  This convention is used in
TSAR for all relative quantities involving the reactivity.

From the definitions in :eq:`eq6-4-2` and :eq:`eq6-4-3`, :eq:`eq6-4-4` is simplified to
the following expression used in TSAR:

.. math::
  :label: eq6-4-6

  \mathrm{S}_{\rho, \alpha}=\frac{\lambda_{2} \mathrm{~S}_{\mathrm{k} 2, \alpha}-\lambda_{1} \mathrm{~S}_{\mathrm{kl}, \alpha}}{\left|\rho_{1 \rightarrow 2}\right|} ,

where :math:`\text{S}_{\text{k1,}\alpha }^{{}}` and :math:`\text{S}_{\text{k2,}\alpha}^{{}}`
are the k-sensitivities for the two states.  The relative change in the
reactivity response due to an arbitrary relative variation (or uncertainty) in
parameter α can be found very easily once the ρ-sensitivities are determined
that is,

.. math::
  :label: eq6-4-7

  \frac{\Delta \rho_{1 \rightarrow 2}}{\left|\rho_{1 \rightarrow 2}\right|} \sim \mathrm{S}_{\rho, \alpha} \frac{\Delta \alpha}{\alpha} .

In cases where the net reactivity change is very small, the denominator
of :eq:`eq6-4-6` approaches zero; thus, the relative sensitivity coefficient can
increase without bound. For this reason TSAR provides an input option to
compute U\ *absolute*\ U rather than U\ *relative*\ U sensitivity
coefficients. Absolute quantities are indicated here by the presence of
a tilde (∼), while relative quantities have no tilde. The absolute
sensitivity coefficient is defined in TSAR as the absolute change in the
reactivity, expressed in pcm (percent-milli), due to a fractional change
in data:

.. math::
  :label: eq6-4-8

  \mathrm{S}_{\rho, \alpha}=\left(\lambda_{2} \mathrm{~S}_{\mathrm{k} 2, \alpha}-\lambda_{1} \mathrm{~S}_{\mathrm{k} 1, \alpha}\right) \times 10^{5} ,

so that

.. math::
  :label: eq6-4-9

  \Delta \rho_{1 \rightarrow 2}(p c m) \sim \mathrm{S}_{\rho, \alpha} \frac{\Delta \alpha}{\alpha} .

Prior to executing TSAR, it is necessary to perform TSUNAMI calculations
for each reactor state, in order to evaluate the relative k-sensitivity
coefficients in :eq:`eq6-4-3`. These are written out in the SDF sensitivity file
format and saved for input to TSAR. TSAR reads the two previously
prepared files and uses them to evaluate :eq:`eq6-4-6` or :eq:`eq6-4-8` for the reactivity
sensitivities. The ρ-sensitivities are then output to another SDF file.
As discussed in :ref:`6-1` of the SCALE documentation, the complete
sensitivities calculated by TSUNAMI include implicit effects associated
with perturbations in resonance self-shielding; hence, the reactivity
sensitivities also account for these effects, which can be significant.

TSAR prints the number of different sensitivity profiles that are
computed and optionally can edit the input k-sensitivities corresponding
to each reactor state, as well the calculated ρ-sensitivities.
Sensitivities may be edited by a sum over group for each
nuclide-reaction pair. In addition, the TSAR output SDF file containing
multigroup ρ-sensitivities for each nuclide-reaction pair can be read by
Fulcrum to produce plots of the energy-dependent sensitivities. The
filename of the reactivity sensitivity data file is given as
*job_name.react.sdf*, where *job_name* is the name of the TSAR input
file (i.e., *job_name.inp*, *job_name.input*, or simply *job_name*).
Additionally, if the user requests edits of the input k-sensitivities
using the *print=all* option, the k-sensitivity data files are copied to
the return directory as *job_name.kstate1.sdf* and
*job_name.kstate2.sdf*. The *print* keyword is further described in the
TSAR input section.

.. _6-4-2-2:

Reactivity uncertainty analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TSAR performs uncertainty analysis for eigenvalue-difference responses in much
the same manner as the TSUNAMI sequences for the multiplication factor, except
that either absolute or relative uncertainties may be computed.  Assume that the
transport calculations for the eigenvalues of the two reactor states use “N”
input parameters, consisting of nuclear data for all groups, reaction types, and
nuclides.  The relative sensitivity coefficients for these data can be expressed
as components of the N-dimension column vector :math:`\mathbf{S}_{\rho }^{{}}` and
similarly for the absolute sensitivities :math:`\mathbf{S}_{\rho }^{{}}`.  The
relative and absolute reactivity variances—indicated as :math:`\sigma _{\rho}^{\text{2}}`
and :math:`\sigma _{\rho }^{\text{2}}`, respectively—are calculated in
TSAR as

.. math::
  :label: eq6-4-10

  \sigma_{\rho}^{2}=\frac{\sigma_{\rho}^{2}}{\rho^{2}}=\mathbf{S}_{\boldsymbol{\rho}}^{\mathbf{T}} \mathbf{C}_{\boldsymbol{a} \boldsymbol{a}} \mathbf{S}_{\boldsymbol{\rho}} \quad \text { and } \quad \sigma_{\rho}^{2}=\mathbf{S}_{\boldsymbol{\rho}}^{\mathbf{T}} \mathbf{C}_{\boldsymbol{a} \boldsymbol{\alpha}} \mathbf{S}_{\boldsymbol{\rho}} ,

where :math:`\mathbf{C}_{\boldsymbol{a} \boldsymbol{a}}`

is the relative covariance matrix describing nuclear data uncertainties and correlations, which are read from the SCALE covariance libraries.  Due to the manner in which the absolute sensitivity coefficient is defined in Eq. (6.4.8), the absolute variance of the reactivity still uses the relative covariance matrix of the nuclear data.

The reactivity variance is related to the uncertainties and correlations in the
calculated eigenvalues of the two reactor states.  It can be shown that
expression in :eq:`eq6-4-10` for the relative variance in an eigenvalue-difference
response is equivalent to

.. math::
  :label: eq6-4-11

  \sigma_{\rho}^{2}=\frac{\lambda_{1}^{2}}{\left(\lambda_{1}-\lambda_{2}\right)^{2}} \sigma_{\mathrm{k} 1}^{2}+\frac{\lambda_{2}^{2}}{\left(\lambda_{1}-\lambda_{2}\right)^{2}} \sigma_{\mathrm{k} 2}^{2}-2 \mathrm{c}_{1 \rightarrow 2} \frac{2 \lambda_{1} \lambda_{2}}{\left(\lambda_{1}-\lambda_{2}\right)^{2}} \sigma_{\mathrm{k} 1} \sigma_{\mathrm{k} 2} .

In the above equations, :math:`\sigma _{\text{k1}}^{{}}` and :math:`\sigma _{\text{k2}}^{{}}`
are relative standard deviations of the
multiplication factors and the correlation coefficient between the two
reactor states is designated as c\ :sub:`1→2` ∈ [-1,1]. The eigenvalue
calculations of the two states are correlated because they both use the
same nuclear data libraries; therefore, the variance in the
eigenvalue-difference is not simply the sum of the variances of the
eigenvalues. A positive correlation (i.e., c\ :sub:`1→2` > 0) reduces
the uncertainty in the reactivity because common uncertainties tend to
cancel from the eigenvalue difference. On the other hand, negative
correlations increase the reactivity uncertainty. It also can be seen
from :eq:`eq6-4-11`. that whenever the difference in the eigenvalues of the two
states is small, the relative variance of the reactivity is
substantially greater than the individual eigenvalue variances because
the coefficients of :math:`\sigma _{\text{k1}}^{\text{2}}` and :math:`\sigma _{\text{k2}}^{\text{2}}`
are large. Since this is usually the case for
reactivity changes in a reactor, relative uncertainties in reactivity
responses tend to be much larger than those for eigenvalues. If the
reactivity response is close to zero, it is usually preferable to
consider absolute rather than relative uncertainties. Whenever the
eigenvalue difference is less than 10\ :sup:`-10`, TSAR will abort the
calculation if a relative uncertainty is specified.

TSAR calculates the variance in the reactivity response using the
expressions in :eq:`eq6-4-10`. The square root of the variance corresponds to the
standard deviation, which indicates the reactivity uncertainty. TSAR
edits this value, as well the individual contributions of each
nuclide-reaction pair (including cross correlations) to the overall
uncertainty.

.. _6-4-2-3:

Cross-section-covariance data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The cross-section-covariance data are read from the COVERX-formatted
covariance library identified by *coverx=* in the *PARAMETER* data block
on the TSAR input file. Cross-section-covariance data files distributed
with SCALE are discussed in :ref:`11-3`, and the format of the COVERX
data file is presented if :ref:`6-7abc`. The recommended SCALE
covariance libraries include uncertainty data for all materials in
ENDF/B-VII. These data were obtained from a variety of sources,
including ENDF/B-VI and VII, JENDL, and approximate values based on
uncertainties in measured integral parameters. :cite:`williams_scale-6_2008`. The *COVARIANCE*
data block can be used to override and/or supplement the library
uncertainty values for specified nuclide-reaction pairs. The keyword
*use_icov* is entered in the *PARAMETER* data block to utilize the
covariance data defined in the *COVARIANCE* data block. Additionally, a
default uniform standard deviation value can be assigned for any missing
covariance data. This default value is defined by the *udcov=* keyword
in the *PARAMETER* data block, and the keyword *use_dcov* is entered to
activate the option. Warning messages are printed to identify
substituted covariance matrices.

When *use_dcov* and/or *use_icov* and *cov_fix* are specified in the
*PARAMETER* data block, and a reaction has zero or large (standard
deviation > 1000%) values on the diagonal of the covariance matrix, the
diagonal elements and off-diagonal terms are replaced according to the
user-input criteria. Warning messages are printed to identify the
replaced values. Additional options for user-specified covariance data
are given in :ref:`6-4-3-2`.

In the reactivity-uncertainty-analysis edit, a single asterisk (“*”)
identifies uncertainty contributions from nuclide-reaction pairs for
which the default cross-section-covariance data is applied. Likewise,
the markers (“**”), (“***”), (“****”), denote (a) user-input covariance
data, (b) covariance library data replaced by default values, and (c)
covariance library data replaced by user-input values, respectively. In
the HTML output, these uncertainty contributions are distinguished by
using unique HTML colors. The different HTML colors are specified by the
HTML block keywords *ud_clr*\ =, *ui_clr*\ =, *udfix_clr*\ =, and
*uifix_clr*\ =. The HTML block keyword options are discussed in more
detail in :ref:`6-4-3-3`.

TSAR computes a problem-specific covariance library that contains
cross-section covariances only for the nuclide-reaction pairs (including
cross correlations) listed on the k\ :sub:`1`-and
k\ :sub:`2`-sensitivity data files. This covariance library, referred to
as the working covariance library, is written in COVERX format like the
SCALE covariance library. The working covariance library contains any
default or user-input covariance data for nuclide-reaction pairs that
were not on the input covariance library as well as any modified
cross-section-covariance data. The working covariance library can be
read by the Javapeño plotting tool to visualize the
cross-section-covariance data used in the reactivity uncertainty
analysis.

.. _6-4-3:

Input Description
-----------------

The user input for TSAR consists of a SCALE Analytic Sequence
Specification Record (i.e., *=tsar*), an optional title followed by
three blocks of data in free-form keyword format, and a SCALE input
termination END record. The data blocks begin with **READ KEYNAME**\ and
end with **END KEYNAME**, where **KEYNAME** is the name of an individual
data block. The *PARAMETER* data block is the only required block of
data, while the *HTML* and *COVARIANCE* data blocks are optional. The
data blocks can be entered in any order.

.. _6-4-3-1:

Parameter data
~~~~~~~~~~~~~~

The *PARAMETER* block of data is used to specify the name of the
previously prepared k-sensitivity data files, the name of the
ρ-sensitivity data file, and other keyword options that control the code
execution. The keyword options are listed in :numref:`tab6-4-1` along with
their default values and description. A keyword that ends with “\ *=*\ ”
must be followed by additional data. Keywords that do not end with
“\ *=*\ ” are Boolean flags that are used to turn on certain features of
the code, such as the computation of certain data or certain output
edits. If the keyword is present for a Boolean entry, the value is set
to true. Otherwise, the value is set to false.

.. _tab6-4-1:
.. table:: Input data for parameter block of TSAR input.
  :align: center
  :class: longtable

  +-----------------------+-----------------------+-----------------------+
  | **Keyword**           | **Default value**     | **Description**       |
  +=======================+=======================+=======================+
  | *cov_fix*             | False                 | Replace zero and      |
  |                       |                       | large (standard       |
  | (optional)            |                       | deviation >           |
  |                       |                       | *large_cov*) values   |
  |                       |                       | on diagonal of        |
  |                       |                       | cross-section-covaria\|
  |                       |                       | nce                   |
  |                       |                       | data with user-input  |
  |                       |                       | values or default     |
  |                       |                       | values.               |
  +-----------------------+-----------------------+-----------------------+
  | *coverx=*             | 44groupcov            | Name of               |
  |                       |                       | cross-section-covaria\|
  | (optional)            |                       | nce                   |
  |                       |                       | data file to use in   |
  |                       |                       | analysis.             |
  +-----------------------+-----------------------+-----------------------+
  | *large_cov=*          | 10.0                  | Cutoff fractional     |
  |                       |                       | standard deviation    |
  | (optional)            |                       | value for *cov_fix*.  |
  |                       |                       | Covariance data with  |
  |                       |                       | uncertainties larger  |
  |                       |                       | than *large_cov* are  |
  |                       |                       | replaced with         |
  |                       |                       | user-defined or       |
  |                       |                       | default values.       |
  |                       |                       | Default =10, which is |
  |                       |                       | 1000% uncertainty.    |
  +-----------------------+-----------------------+-----------------------+
  | *nocovar*             | False                 | If *nocovar* is       |
  |                       |                       | present, the          |
  | (optional)            |                       | reactivity            |
  |                       |                       | uncertainty           |
  |                       |                       | calculation is        |
  |                       |                       | bypassed.             |
  +-----------------------+-----------------------+-----------------------+
  | *nohtml*              | False                 | If *nohtml* is        |
  |                       |                       | present,              |
  | (optional)            |                       | HTML-formatted output |
  |                       |                       | is not generated.     |
  +-----------------------+-----------------------+-----------------------+
  | *print=*              | rho                   | Available options are |
  |                       |                       | *rho*, *all*, or      |
  | (optional)            |                       | *none*. If            |
  |                       |                       | *print=rho*,          |
  |                       |                       | ρ-sensitivities edits |
  |                       |                       | are generated. If     |
  |                       |                       | *print=all*, ρ-,      |
  |                       |                       | k\ :sub:`1`-, and     |
  |                       |                       | k\ :sub:`2`-sensitivi\|
  |                       |                       | ties                  |
  |                       |                       | edits are generated.  |
  |                       |                       | The *print=none*      |
  |                       |                       | option turns off all  |
  |                       |                       | sensitivity edits.    |
  +-----------------------+-----------------------+-----------------------+
  | *return_work_cov*     | False                 | If *return_work_cov*  |
  |                       |                       | is present, the       |
  | (optional)            |                       | working covariance    |
  |                       |                       | library is copied to  |
  |                       |                       | the return directory  |
  |                       |                       | with the file name    |
  |                       |                       | *job_name.wrk.cov,*   |
  |                       |                       | where *job_name* is   |
  |                       |                       | the name of the input |
  |                       |                       | file. If              |
  |                       |                       | *return_work_cov* is  |
  |                       |                       | not present, the      |
  |                       |                       | working covariance    |
  |                       |                       | library remains in    |
  |                       |                       | the temporary working |
  |                       |                       | directory with the    |
  |                       |                       | file name             |
  |                       |                       | *job_name.wrk*.       |
  +-----------------------+-----------------------+-----------------------+
  | *sdf_file_1=*         | n/a                   | The file name of the  |
  |                       |                       | initial state         |
  | (required)            |                       | k\ :sub:`1`-sensitivi\|
  |                       |                       | ty                    |
  |                       |                       | data file.            |
  +-----------------------+-----------------------+-----------------------+
  | *sdf_file_2=*         | n/a                   | The file name of the  |
  |                       |                       | final state           |
  | (required)            |                       | k\ :sub:`2`-sensitivi\|
  |                       |                       | ty                    |
  |                       |                       | data file.            |
  +-----------------------+-----------------------+-----------------------+
  | *type=*               | relative              | Available options are |
  |                       |                       | *relative* (or *rel*) |
  | (optional)            |                       | and *absolute* (or    |
  |                       |                       | *abs*). If            |
  |                       |                       | *type=relative*, the  |
  |                       |                       | output reactivity     |
  |                       |                       | sensitivity data file |
  |                       |                       | contains relative     |
  |                       |                       | ρ–sensitivities. If   |
  |                       |                       | *type=absolute*, the  |
  |                       |                       | output reactivity     |
  |                       |                       | sensitivity data file |
  |                       |                       | contains absolute     |
  |                       |                       | ρ–sensitivities       |
  |                       |                       | (i.e., pcm units).    |
  +-----------------------+-----------------------+-----------------------+
  | *udcov=*              | 0.05                  | User-defined default  |
  |                       |                       | value of standard     |
  | (optional)            |                       | deviation in          |
  |                       |                       | cross-section data to |
  |                       |                       | use for all groups    |
  |                       |                       | for nuclide-reaction  |
  |                       |                       | pairs for which       |
  |                       |                       | cross-section-covaria\|
  |                       |                       | nce                   |
  |                       |                       | data are too large or |
  |                       |                       | not available on the  |
  |                       |                       | input covariance      |
  |                       |                       | library.              |
  +-----------------------+-----------------------+-----------------------+
  | *udcov_corr=*         | 1.0                   | User-defined default  |
  |                       |                       | correlation value to  |
  | (optional)            |                       | use for               |
  |                       |                       | nuclide-reaction      |
  |                       |                       | pairs for which       |
  |                       |                       | cross-section-covaria\|
  |                       |                       | nce                   |
  |                       |                       | data are not          |
  |                       |                       | available on the      |
  |                       |                       | input covariance      |
  |                       |                       | library.              |
  +-----------------------+-----------------------+-----------------------+
  | *udcov_corr_type=*    | zone                  | User-defined default  |
  |                       |                       | correlation in        |
  | (optional)            |                       | cross-section data to |
  |                       |                       | use for               |
  |                       |                       | nuclide-reaction      |
  |                       |                       | pairs for which       |
  |                       |                       | cross-section-covaria\|
  |                       |                       | nce                   |
  |                       |                       | data are not          |
  |                       |                       | available on the      |
  |                       |                       | input SCALE           |
  |                       |                       | covariance library.   |
  |                       |                       | Allowed values are    |
  |                       |                       | *long*, *zone*, and   |
  |                       |                       | *short*. See          |
  |                       |                       | :numref:`tab6-4-2` for|
  |                       |                       | details on *long*,    |
  |                       |                       | *zone*, and *short.*  |
  +-----------------------+-----------------------+-----------------------+
  | *udcov_therm=*        | 0.0                   | User-defined default  |
  |                       |                       | value of standard     |
  | (optional)            |                       | deviation in          |
  |                       |                       | cross-section data to |
  |                       |                       | use for thermal data  |
  |                       |                       | for nuclide-reaction  |
  |                       |                       | pairs for which       |
  |                       |                       | cross-section-covaria\|
  |                       |                       | nce                   |
  |                       |                       | data are too large or |
  |                       |                       | not available on the  |
  |                       |                       | input covariance      |
  |                       |                       | library. If input,    |
  |                       |                       | the                   |
  |                       |                       | *udcov*\ \_\ *therm*  |
  |                       |                       | value overrides the   |
  |                       |                       | *udcov* value in the  |
  |                       |                       | thermal range (i.e.,  |
  |                       |                       | neutron energies      |
  |                       |                       | below 0.625 eV).      |
  +-----------------------+-----------------------+-----------------------+
  | *udcov_inter=*        | 0.0                   | User-defined default  |
  |                       |                       | value of standard     |
  | (optional)            |                       | deviation in          |
  |                       |                       | cross-section data to |
  |                       |                       | use for intermediate  |
  |                       |                       | data for              |
  |                       |                       | nuclide-reaction      |
  |                       |                       | pairs for which       |
  |                       |                       | cross-section-covaria\|
  |                       |                       | nce                   |
  |                       |                       | data are too large or |
  |                       |                       | not available on the  |
  |                       |                       | input covariance      |
  |                       |                       | library. If input,    |
  |                       |                       | the *udcov_inter*     |
  |                       |                       | value overrides the   |
  |                       |                       | *udcov* value in the  |
  |                       |                       | intermediate range    |
  |                       |                       | (i.e., neutron        |
  |                       |                       | energies above 0.625  |
  |                       |                       | eV and below 25 keV). |
  +-----------------------+-----------------------+-----------------------+
  | *udcov_fast=*         | 0.0                   | User-defined default  |
  |                       |                       | value of standard     |
  | (optional)            |                       | deviation in          |
  |                       |                       | cross-section data to |
  |                       |                       | use for fast data for |
  |                       |                       | nuclide-reaction      |
  |                       |                       | pairs for which       |
  |                       |                       | cross-section-covaria\|
  |                       |                       | nce                   |
  |                       |                       | data are too large or |
  |                       |                       | not available on the  |
  |                       |                       | input covariance      |
  |                       |                       | library. If input,    |
  |                       |                       | the *udcov_fast*      |
  |                       |                       | value overrides the   |
  |                       |                       | *udcov* value in the  |
  |                       |                       | fast range (i.e.,     |
  |                       |                       | neutron energies      |
  |                       |                       | above 25 keV).        |
  +-----------------------+-----------------------+-----------------------+
  | *use_dcov*            | False                 | Use user-defined      |
  |                       |                       | default               |
  | (optional)            |                       | cross-section-covaria\|
  |                       |                       | nce                   |
  |                       |                       | data for              |
  |                       |                       | nuclide-reaction      |
  |                       |                       | pairs not included on |
  |                       |                       | the input covariance  |
  |                       |                       | library.              |
  +-----------------------+-----------------------+-----------------------+
  | *use_icov*            | False                 | Use user-defined      |
  |                       |                       | cross-section-covaria\|
  | (optional)            |                       | nce                   |
  |                       |                       | data input in the     |
  |                       |                       | *COVARIANCE* input    |
  |                       |                       | data block in place   |
  |                       |                       | of the default values |
  |                       |                       | for user-input        |
  |                       |                       | nuclide-reaction      |
  |                       |                       | pairs that are not on |
  |                       |                       | the input covariance  |
  |                       |                       | library.              |
  +-----------------------+-----------------------+-----------------------+

.. _6-4-3-2:

User-input covariance data
~~~~~~~~~~~~~~~~~~~~~~~~~~

The *COVARIANCE* data block described in :numref:`tab6-4-2` allows the user
to specify a covariance matrix for specific nuclide-reaction pairs for
which covariance data are not present on the input covariance library or
that have zero or large values on the diagonal. The *COVARIANCE* data
block must begin with *READ COVARIANCE* and end with *END COVARIANCE*.

.. _tab6-4-2:
.. table:: Input data for covariance block of TSAR input.
  :align: center
  :class: longtable

  +-------------+-------------+-------------+-------------+-------------+
  | **Input     | **Requireme\| **Default   | **Allowed   | **Descripti\|
  | parameter** | nt**        | value**     | values**    | on**        |
  +=============+=============+=============+=============+=============+
  | Nuclide     | Required    | none        | Nuclide     | Nuclide for |
  |             |             |             | name or ZA  | which       |
  |             |             |             | number      | covariance  |
  |             |             |             |             | data are to |
  |             |             |             |             | be entered  |
  +-------------+-------------+-------------+-------------+-------------+
  | Reaction    | Required    | none        | Reaction    | Reaction    |
  |             |             |             | name or ZA  | for which   |
  |             |             |             | number      | covariance  |
  |             |             |             |             | data are to |
  |             |             |             |             | be entered. |
  |             |             |             |             | See the     |
  |             |             |             |             | TSUNAMI-IP  |
  |             |             |             |             | manual for  |
  |             |             |             |             | available   |
  |             |             |             |             | reaction    |
  |             |             |             |             | types.      |
  +-------------+-------------+-------------+-------------+-------------+
  | *all=*      | Optional    | 0.0         | any number  | Fractional  |
  |             |             |             |             | standard    |
  |             |             |             |             | deviation   |
  |             |             |             |             | value to be |
  |             |             |             |             | applied to  |
  |             |             |             |             | all groups  |
  +-------------+-------------+-------------+-------------+-------------+
  | *fast=*     | Optional    | 0.0         | any number  | Fractional  |
  |             |             |             |             | standard    |
  |             |             |             |             | deviation   |
  |             |             |             |             | value to be |
  |             |             |             |             | applied to  |
  |             |             |             |             | fast        |
  |             |             |             |             | groups. If  |
  |             |             |             |             | input, the  |
  |             |             |             |             | *fast*      |
  |             |             |             |             | value       |
  |             |             |             |             | overrides   |
  |             |             |             |             | the *all*   |
  |             |             |             |             | value in    |
  |             |             |             |             | the fast    |
  |             |             |             |             | range       |
  |             |             |             |             | (i.e.,      |
  |             |             |             |             | neutron     |
  |             |             |             |             | energies    |
  |             |             |             |             | above 25    |
  |             |             |             |             | keV).       |
  +-------------+-------------+-------------+-------------+-------------+
  | *therm=*    | Optional    | 0.0         | any number  | Fractional  |
  |             |             |             |             | standard    |
  |             |             |             |             | deviation   |
  |             |             |             |             | value to be |
  |             |             |             |             | applied to  |
  |             |             |             |             | thermal     |
  |             |             |             |             | groups. If  |
  |             |             |             |             | input, the  |
  |             |             |             |             | *therm*     |
  |             |             |             |             | value       |
  |             |             |             |             | overrides   |
  |             |             |             |             | the *all*   |
  |             |             |             |             | value in    |
  |             |             |             |             | the thermal |
  |             |             |             |             | range       |
  |             |             |             |             | (i.e.,      |
  |             |             |             |             | neutron     |
  |             |             |             |             | energies    |
  |             |             |             |             | below 0.625 |
  |             |             |             |             | eV).        |
  +-------------+-------------+-------------+-------------+-------------+
  | *inter=*    | Optional    | 0.0         | any number  | Fractional  |
  |             |             |             |             | standard    |
  |             |             |             |             | deviation   |
  |             |             |             |             | value to be |
  |             |             |             |             | applied to  |
  |             |             |             |             | intermediat\|
  |             |             |             |             | e           |
  |             |             |             |             | groups. If  |
  |             |             |             |             | input, the  |
  |             |             |             |             | *inter*     |
  |             |             |             |             | value       |
  |             |             |             |             | overrides   |
  |             |             |             |             | the *all*   |
  |             |             |             |             | value in    |
  |             |             |             |             | the         |
  |             |             |             |             | intermediat\|
  |             |             |             |             | e           |
  |             |             |             |             | range       |
  |             |             |             |             | (i.e.,      |
  |             |             |             |             | neutron     |
  |             |             |             |             | energies    |
  |             |             |             |             | above 0.625 |
  |             |             |             |             | eV and      |
  |             |             |             |             | below 25    |
  |             |             |             |             | keV).       |
  +-------------+-------------+-------------+-------------+-------------+
  | *corr=*     | Optional    | 1.0         | any number  | Correlation |
  |             |             |             | from -1.0   | between     |
  |             |             |             | to 1.0      | groups      |
  +-------------+-------------+-------------+-------------+-------------+
  | corr_type\  | Optional    | *zone*      | *long,      | Type of     |
  | *=*         |             |             | short,      | correlation |
  |             |             |             | zone*       | applied     |
  |             |             |             |             | from        |
  |             |             |             |             | group-to-gr\|
  |             |             |             |             | oup         |
  |             |             |             |             | covariance  |
  |             |             |             |             | values      |
  |             |             |             |             |             |
  |             |             |             |             | *long* –    |
  |             |             |             |             | correlation |
  |             |             |             |             | is applied  |
  |             |             |             |             | between all |
  |             |             |             |             | groups      |
  |             |             |             |             |             |
  |             |             |             |             | *short* –   |
  |             |             |             |             | correlation |
  |             |             |             |             | is applied  |
  |             |             |             |             | only        |
  |             |             |             |             | between     |
  |             |             |             |             | adjacent    |
  |             |             |             |             | groups      |
  |             |             |             |             |             |
  |             |             |             |             | *zone* –    |
  |             |             |             |             | correlation |
  |             |             |             |             | is applied  |
  |             |             |             |             | within      |
  |             |             |             |             | fast,       |
  |             |             |             |             | intermediat\|
  |             |             |             |             | e,          |
  |             |             |             |             | and thermal |
  |             |             |             |             | groups, but |
  |             |             |             |             | no          |
  |             |             |             |             | correlation |
  |             |             |             |             | is applied  |
  |             |             |             |             | between     |
  |             |             |             |             | zones       |
  +-------------+-------------+-------------+-------------+-------------+
  | *end*       | Required    |             |             | Denotes end |
  |             |             |             |             | of input    |
  |             |             |             |             | for current |
  |             |             |             |             | nuclide/rea\|
  |             |             |             |             | ction       |
  +-------------+-------------+-------------+-------------+-------------+

Any MT number or reaction name will be treated as a valid input, but
only those present on the k\ :sub:`1`- or k\ :sub:`2`-sensitivity data
files will impact the results. The reaction sensitivity types computed
by SAMS from TSUNAMI-1D and TSUNAMI-3D are described in the TSUNAMI-IP
manual. An energy-covariance matrix is created for the specified
nuclide-reaction pair with the square of the entered standard deviation
for the diagonal terms for all groups using the *all=* value. Groups in
the fast, intermediate, and thermal energies are then set to the square
of the standard deviation value entered for *fast=*, *inter=*, and
*therm=*, respectively. The off-diagonal terms of the energy matrix are
generated according to the input for *corr=*, and *corr_type=*, with
default settings of *1.0* and *zone.* Data entered in this block are
used only for missing data and do not override values on the input
covariance data file. The SCALE 5.1 input format is supported where data
are entered in triplets with the nuclide name (e.g., u-235), then the
reaction MT number or name (e.g., 18 or fission), and then a standard
deviation value. In this case, the *end* keyword must not be entered.
The standard deviation value is applied to all groups with default
setting for correlations. These data are only used if *use_icov* is
specified in the *PARAMETER* data block. When both *use_icov* and
*cov_fix* are specified in the *PARAMETER* data block, and a reaction
has zero or large (standard deviation > 1000%) values on the diagonal of
the covariance matrix, these values are replaced with the square of the
user input standard deviation value, and the corresponding off-diagonal
terms are substituted according to the values of *corr* and *corr_type*.

.. _6-4-3-3:

HTML data
~~~~~~~~~

The optional *HTML* data block is used to customize HTML-formatted
output. The *HTML* data block must begin with *READ HTML* and end with
*END HTML*. The data input to the *HTML* data block consists of several
keywords that are shown, along with their default values and
descriptions, in Table 6.4.3X. A keyword that ends with “\ *=*\ ” must
be followed by text data. For color entries, any valid html color name
can be entered or the hexadecimal representation can be used if preceded
by a # sign. For example, to change the background color of the html
output to white, *bg_clr=white* and *bg_clr=#ffffff* have the same
effect, because ffffff is the hexadecimal representation of white. An
extensive list of available colors for customized output is shown in
:ref:`6-7abc`. Please note that not all features are supported by all
browsers.

.. _tab6-4-3:
.. table:: Input data for html block of TSAR input.
  :align: center
  :class: longtable

  +-----------------------+-----------------------+-----------------------+
  | **Keyword**           | **Default value**     | **Description**       |
  +-----------------------+-----------------------+-----------------------+
  | *bg_clr=*             | papayawhip            | Background color      |
  +-----------------------+-----------------------+-----------------------+
  | *h1_clr=*             | maroon                | Color used for major  |
  |                       |                       | headings              |
  +-----------------------+-----------------------+-----------------------+
  | *h2_clr=*             | navy                  | Color used for        |
  |                       |                       | sub-headings          |
  +-----------------------+-----------------------+-----------------------+
  | *txt_clr=*            | black                 | Color for plain text  |
  +-----------------------+-----------------------+-----------------------+
  | *lnk_clr=*            | navy                  | Color for hyperlinks  |
  +-----------------------+-----------------------+-----------------------+
  | *lnk_dec=*            | none                  | Decoration for        |
  |                       |                       | hyperlinks. (none,    |
  |                       |                       | underline, overline,  |
  |                       |                       | line-through, blink)  |
  +-----------------------+-----------------------+-----------------------+
  | *vlnk_clr*            | navy                  | Color for visited     |
  |                       |                       | hyperlinks            |
  +-----------------------+-----------------------+-----------------------+
  | *ud_clr=*             | blue                  | Color for values in   |
  |                       |                       | tables that use       |
  |                       |                       | default covariance    |
  |                       |                       | data                  |
  +-----------------------+-----------------------+-----------------------+
  | *ui_clr=*             | red                   | Color for values in   |
  |                       |                       | tables that use       |
  |                       |                       | user-input covariance |
  |                       |                       | data                  |
  +-----------------------+-----------------------+-----------------------+
  | *udfix_clr=*          | royalblue             | Color for values in   |
  |                       |                       | tables that use       |
  |                       |                       | default corrected     |
  |                       |                       | covariance data       |
  +-----------------------+-----------------------+-----------------------+
  | *uifix_clr=*          | green                 | Color for values in   |
  |                       |                       | tables that use       |
  |                       |                       | user-input corrected  |
  |                       |                       | covariance data       |
  +-----------------------+-----------------------+-----------------------+

.. _6-4-4:

Sample Problem and Output Description
-------------------------------------

.. _6-4-4-1:

Input and text output
~~~~~~~~~~~~~~~~~~~~~

An example of TSAR input is given in :numref:`list6-4-1` Each section of the
text output, not shown, is described in order below.

1. Input Listing and Summary of Calculations – The TSAR input data is
   printed for each data block. Both user-specified and default values
   for the various keywords are edited.

2. k\ 1-Sensitivity Data File Summary and Sensitivity Coefficients – The
   header information for the k\ :sub:`1`-sensitivity data files follows
   the input data. This includes the title on the sensitivity data file,
   the number of energy groups, the number of sensitivity profiles, and
   the values of k\ :sub:`1` and λ\ :sub:`1`. If *print=all* is
   specified in the *PARAMETER* data block, the energy, region, and
   mixture-integrated k\ :sub:`1`-sensitivity coefficients are edited
   for each nuclide-reaction pair.

3. k\ 2-Sensitivity Data File Summary and Sensitivity Coefficients – The
   header information for the k\ :sub:`2`-sensitivity data files follows
   the k\ :sub:`1`-sensitivity data file edit. This includes the title
   on the sensitivity data file, the number of energy groups, the number
   of sensitivity profiles, and the values of k\ :sub:`2` and
   λ\ :sub:`1`. If *print=all* is specified in the *PARAMETER* data
   block, the energy, region, and mixture-integrated
   k\ :sub:`2`-sensitivity coefficients are edited for each
   nuclide-reaction pair.

4. Reactivity Value and Optional ρ–Sensitivity Coefficients – After the
   k\ :sub:`1` and k\ :sub:`2` sensitivity edits, the reactivity between
   the two states is edited in pcm units. If *print=all* or *print=rho*
   is specified in the *PARAMETER* data block, the energy, region, and
   mixture-integrated ρ–sensitivity coefficients are edited for each
   nuclide-reaction pair.

5. Reactivity Uncertainty Analysis – Following the edit of the
   reactivity value and the optional ρ‑sensitivity edit, the reactivity
   uncertainty analysis is printed on the text output. First, a message
   is printed that states that the working covariance library is being
   generated. If *PARAMETER* block keywords *use_dcov, use_icov,* and/or
   *cov_fix* are specified, covariance warnings are printed whenever
   user-input covariance data are included in the reactivity uncertainty
   analysis. Following the covariance warnings, the total reactivity
   uncertainty is printed along with the reactivity uncertainty
   contributions from individual energy covariance matrices. The
   reactivity uncertainty contributions are sorted in descending order.


.. code-block:: scale
  :name: list6-4-1
  :caption: TSAR sample problem input.

  =shell
    cp $SCALE/output/tsunami-1d1.sdf .
    cp $SCALE/output/tsunami-1d1_147HtoU.sdf .
  end
  =tsar
  tsar example problem
  read parameter
    sdf_file_1=tsunami-1d1.sdf
    sdf_file_2=tsunami-1d1_147HtoU.sdf
    use_dcov
    use_icov
    cov_fix
    print=all
    udcov_fast=0.10
    udcov_inter=0.15
    udcov_therm=0.08
    udcov_corr_type=zone
    udcov_corr=1.0
    return_work_cov
  end parameter
  read html
   bg_clr=Aliceblue
   ud_clr=blue
   ui_clr=read
   udfix_clr=green
   uifix_clr=darkorange
  end html
  end

.. _6-4-5:

HTML Output
-----------

The input file for the TSAR sample problem shown in :numref:`list6-4-1` is
named tsar1.input. In this case, the HTML-formatted output is stored in
a file called tsar1.html and additional resources are stored in
directories called tsar1.htmd and applet_resources. This section
contains example TSAR HTML-formatted output only for demonstration of
the interface. The problem does not correspond to the sample problem
distributed with SCALE and is included for illustrative purposes only.
When tsar1.html is opened in a web browser, the information shown in
:numref:`fig6-4-2` is displayed.

.. _fig6-4-2:
.. figure:: figs/TSAR/fig1.png
  :align: center
  :width: 600

  Initial screen from TSAR HTML output.

The title of the input file is displayed between the two SCALE logos.
Clicking on the SCALE logo will link the user directly to the SCALE
website, if Internet access is available. Because this SCALE input file
only executed TSAR, only a single output listing is available. The text
“1. TSAR” is a hyperlink to view the output from TSAR. Clicking on the
“1. TSAR” hyperlink will bring up the information shown in
:numref:`fig6-4-3`.

The initial page of output from TSAR is shown in :numref:`fig6-4-3`. Program
verification information is shown in the table under the TSAR logo. This
table includes information about the code that was executed and the date
and time it was run. The menu on the left side of the screen contains
hyperlinks to specific portions of the code output. Echoes of the input
data are available in the Input Data section. Any errors or warning
messages are available in the Messages sections. Results from the code
execution are shown in the results section.


.. _fig6-4-3:
.. figure:: figs/TSAR/fig3.png
  :align: center
  :width: 600

  Program verification screen from TSAR HTML output.

Selecting Input Parameters will reveal the menu of available input data.
Selecting Input Parameters causes the table shown in :numref:`fig6-4-4` to be
displayed.  Other input data can also be displayed by selecting the desired data
from the menu.

.. _fig6-4-4:
.. figure:: figs/TSAR/fig4.png
  :align: center
  :width: 600

  Input parameters from TSAR HTML output.

Selecting Results causes a menu of available results to be revealed.  From this
menu, selecting Reactivity Sensitivities causes a submenu to be revealed. From
the submenu, the Reactivity Sensitivities can be visualized in tabular format or
plot format.  Selecting Energy, Region, and Mixture Integrated Sensitivity
Coefficients from this submenu causes the information shown in :numref:`fig6-4-5` to
appear.


.. _fig6-4-5:
.. figure:: figs/TSAR/fig5.png
  :align: center
  :width: 600

  Global integral indices from TSAR HTML output.

Plots of sensitivity data from the initial and final states as well as
the reactivity sensitivities are available for viewing in the TSAR HTML
output. If the *return_work_cov* keyword option is included in the
PARAMETER block on the TSAR input file, then the covariance data can be
viewed by selecting “XS Covariance Plot” in the results submenu. A Java
applet version of Javapeño will appear in the browser window with the
working covariance library preloaded. Data can be added to the plot by
double-clicking on the list of available data on the right side of
Javapeño. The plot shown in :numref:`fig6-4-6` was produced with this
procedure.

.. _fig6-4-6:
.. figure:: figs/TSAR/fig6.png
  :align: center
  :width: 600

  Covariance data from TSAR HTML output.

.. bibliography:: bibs/TSAR.bib
