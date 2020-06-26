.. _MAVRIC:

MAVRIC: Monaco with Automated Variance Reduction using Importance Calculations
==============================================================================

*D. E. Peplow and C. Celik*

Introduction
------------

Monte Carlo particle transport calculations for deep penetration problems can require very long run times in order to achieve an acceptable level of statistical uncertainty in the final answers. Discrete-ordinates codes can be faster but have limitations relative to the discretization of space, energy, and direction. Monte Carlo calculations can be modified (biased) to produce results with the same variance in less time if an approximate answer or some other additional information is already known about the problem. If an importance can be assigned to different particles based on how much they will contribute to the final answer, more time can be spent on important particles with less time devoted to unimportant particles. One of the best ways to bias a Monte Carlo code for a particular tally is to form an importance map from the adjoint flux based on that tally. Unfortunately, determining the exact adjoint flux could be just as difficult as computing the original problem itself. However, an approximate adjoint can still be very useful in biasing the Monte Carlo solution :cite:`wagner_acceleration_1997`. Discrete ordinates can be used to quickly compute that approximate adjoint. Together, Monte Carlo and discrete ordinates can be used to find solutions to thick shielding problems in reasonable times.

The MAVRIC (Monaco with Automated Variance Reduction using Importance Calculations) sequence is based on the CADIS (Consistent Adjoint Driven Importance Sampling) and FW-CADIS (Forward-Weighted CADIS) methodologies :cite:`wagner_automated_1998` :cite:`wagner_automated_2002` :cite:`haghighat_monte_2003` :cite:`wagner_forward-weighted_2007` MAVRIC automatically performs a three-dimensional, discrete-ordinates calculation using Denovo to compute the adjoint flux as a function of position and energy. This adjoint flux information is then used to construct an importance map (i.e., target weights for weight windows) and a biased source distribution that work together—particles are born with a weight matching the target weight of the cell into which they are born. The fixed-source Monte Carlo radiation transport Monaco then uses the importance map for biasing during particle transport and the biased source distribution as its source. During transport, the particle weight is compared with the importance map after each particle interaction and whenever a particle crosses into a new importance cell in the map.

For problems that do not require variance reduction to complete in a reasonable time, execution of MAVRIC without the importance map calculation provides an easy way to run Monaco. For problems that do require variance reduction to complete in a reasonable time, MAVRIC removes the burden of setting weight windows from the user and performs it automatically with a minimal amount of additional input. Note that the MAVRIC sequence can be used with the final Monaco calculation as either a multigroup (MG) or a continuous-energy (CE) calculation.

Monaco has a wide variety of tally options: it can calculate fluxes (by group) at a point in space, over any geometrical region, or for a user-defined, three-dimensional, rectangular grid. These tallies can also integrate the fluxes with either standard response functions from the cross section library or user-defined response functions. All of these tallies are available in the MAVRIC sequence.

While originally designed for CADIS, the MAVRIC sequence is also capable of creating importance maps using both forward and adjoint deterministic estimates. The FW-CADIS method can be used for optimizing several tallies at once, a mesh tally over a large region, or a mesh tally over the entire problem. Several other methods for producing importance maps are also available in MAVRIC and are explored in Appendix C.

CADIS Methodology
-----------------

MAVRIC is an implementation of CADIS (Consistent Adjoint Driven Importance Sampling) using the Denovo SN and Monaco Monte Carlo functional modules. Source biasing and a mesh-based importance map, overlaying the physical geometry, are the basic methods of variance reduction. In order to make the best use of an importance map, the map must be made consistent with the source biasing. If the source biasing is inconsistent with the weight windows that will be used during the transport process, source particles will undergo Russian roulette or splitting immediately, wasting computational time and negating the intent of the biasing.

Overview of CADIS
~~~~~~~~~~~~~~~~~

CADIS has been well described in the literature, so only a
brief overview is given here. Consider a class source-detector problem
described by a unit source with emission probability distribution
function :math:`q\left(\overrightarrow{r},E \right)` and a detector
response function :math:`\sigma_{d}\left(\overrightarrow{r},E \right)`.
To determine the total detector response, *R*, the forward scalar flux
:math:`\phi\left(\overrightarrow{r},E \right)` must be known. The
response is found by integrating the product of the detector response
function and the flux over the detector volume :math:`V_{d}`.


.. math::
  :label: mavric-1

  R = \int_{V_{d}}^{}{\int_{E}^{}{\sigma_{d}\left( \overrightarrow{r},E \right)}}\phi\left(\overrightarrow{r},E \right)\textit{dE dV.}


Alternatively, if the adjoint scalar flux,
:math:`\phi^{+}\left(\overrightarrow{r},E \right)`, is known from the
corresponding adjoint problem with adjoint source
:math:`q^{+}\left(\overrightarrow{r},E \right) = \sigma_{d}\left(\overrightarrow{r},E \right)`,
then the total detector response could be found by integrating the
product of the forward source and the adjoint flux over the source
volume, :math:`V_{s}`.


.. math::
  :label: mavric-2

  R = \int_{V_{s}}^{}{\int_{E}^{}{q\left(\overrightarrow{r},E \right)}}\phi^{+}\left( \overrightarrow{r},E \right)\textit{dE dV.}

Unfortunately, the exact adjoint flux may be just as difficult to
determine as the forward flux, but an approximation of the adjoint flux
can still be used to form an importance map and a biased source
distribution for use in the forward Monte Carlo calculation.

Wagner\ :sup:`1` showed that if an estimate of the adjoint scalar flux
for the corresponding adjoint problem could be found, then an estimate
of the response *R* could be made using Eq. . The adjoint source for the
adjoint problem is typically separable and corresponds to the detector
response and spatial area of tally to be optimized:
:math:`q^{+}\left(\overrightarrow{r},E \right) = \sigma_{d}\left(E \right)g\left( \overrightarrow{r} \right)`,
where :math:`\sigma_{d}\left( E \right)` is a flux-to-dose conversion
factor and :math:`g\left( \overrightarrow{r} \right)` is 1 in the tally
volume and 0 otherwise. Then, from the adjoint flux
:math:`\phi^{+}\left( \overrightarrow{r},E \right)` and response
estimate *R*, a biased source distribution,
:math:`\widehat{q}\left( \overrightarrow{r},E \right)`, for source
sampling of the form


.. math::
  :label: mavric-3

  \widehat{q}\left(\overrightarrow{r},E \right) = \frac{1}{R}q\left(\overrightarrow{r},E\right)\phi^{+}\left( \overrightarrow{r},E \right)


and weight window target values,
:math:`\overline{w}\left( \overrightarrow{r},E \right)`, for particle
transport of the form


.. math::
  :label: mavric-4

  \overline{w}\left( \overrightarrow{r},E \right) = \frac{R}{\phi^{+}\left( \overrightarrow{r},E \right)}


could be constructed, which minimize the variance in the forward Monte
Carlo calculation of *R*.

When a particle is sampled from the biased source distribution
:math:`\widehat{q}\left( \overrightarrow{r},E \right)`, to preserve a
fair game, its initial weight is set to


.. math::
  :label: mavric-5

  w_{0}\left(\overrightarrow{r},E \right) = \frac{q\left(\overrightarrow{r},E \right)}{\widehat{q}\left( \overrightarrow{r},E \right)} = \frac{R}{\phi^{+}\left( \overrightarrow{r},E \right)}\,


which exactly matches the target weight for that particle’s position and
energy. This is the “consistent” part of CADIS—source particles are born
with a weight matching the weight window of the region/energy they are
born into. The source biasing and the weight windows work together.

CADIS has been applied to many problems—including reactor ex-core
detectors, well-logging instruments, cask shielding studies, and
independent spent fuel storage facility models—and has demonstrated very
significant speed-ups in calculation time compared to analog
simulations.

Multiple sources with CADIS
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a typical Monte Carlo calculation with multiple sources (each with a
probability distribution function
:math:`q_{i}\left( \overrightarrow{r},E \right)` and a strength
:math:`S_{i}`, giving a total source strength of
:math:`S = \sum_{}^{}S_{i}`), the source is sampled in two steps. First,
the specific source *i* is sampled with probability
:math:`p\left( i \right) = \ S_{i}/S`, and then the particle is sampled
from the specific source distribution
:math:`q_{i}\left( \overrightarrow{r},E \right)`.

The source sampling can be biased at both levels: which source to sample
from and how to sample each source. For example, the specific source can
be sampled using some arbitrary distribution,
:math:`\widehat{p}\left( i \right)`, and then the individual sources can
be sampled using distributions
:math:`{\widehat{q}}_{i}\left( \overrightarrow{r},E \right)`. Particles
would then have a birth weight of


.. math::
  :label: mavric-6

  w_{0} \equiv \ \left(\frac{p\left( i \right)}{\widehat{p}\left( i \right)} \right)\left(\frac{q_{i}\left( \overrightarrow{r},E \right)}{{\widehat{q}}_{i}\left( \overrightarrow{r},E \right)} \right)\text{.}


For CADIS, a biased multiple source needs to be developed so that the
birth weights of sampled particles still match the target weights of the
importance map. For a problem with multiple sources (each with a
distribution :math:`q_{i}\left( \overrightarrow{r},E \right)` and a
strength :math:`S_{i}`), the goal of the Monte Carlo calculation is to
compute some response :math:`R` for a response function
:math:`\sigma_{d}\left( \overrightarrow{r},E \right)` at a given
detector.


.. math::
  :label: mavric-7

  R = \ \int_{V}^{}{\int_{E}^{}{\sigma_{d}\left( \overrightarrow{r},E \right)\text{ϕ}\left( \overrightarrow{r},E \right)\textit{dE dV.}}}


Note that the flux :math:`\phi\left( \overrightarrow{r},E \right)` has
contributions from each source. The response, :math:`R_{i}`, from each
specific source (:math:`S_{i}` with
:math:`q_{i}\left( \overrightarrow{r},E \right)`) can be expressed using
just the flux from that source,
:math:`\phi_{i}\left( \overrightarrow{r},E \right)`, as


.. math::
  :label: mavric-8

  R_{i} = \ \int_{V}^{}{\int_{E}^{}{\sigma_{d}\left(\overrightarrow{r},E \right)\ \phi_{i}\left(\overrightarrow{r},E \right)\textit{dE dV .}}}


The total response is then found as :math:`R = \sum_{i}^{}R_{i}`.

For the adjoint problem, using the adjoint source of
:math:`q^{+}\left( \overrightarrow{r},E \right) = \sigma_{d}\left( \overrightarrow{r},E \right)`,
the response :math:`R` can also be calculated as


.. math::
  :label: mavric-9

  R = \ \int_{V}^{}{\int_{E}^{}{\left\lbrack \sum_{i}^{}{S_{i}q_{i}\left( \overrightarrow{r},E \right)} \right\rbrack\ \phi^{+}\left( \overrightarrow{r},E \right)\textit{dE dV}}},


with response contribution from each specific source being


.. math::
  :label: mavric-10

  R_{i} = \ \int_{V}^{}{\int_{E}^{}{\ {S_{i}q_{i}\left( \overrightarrow{r},E \right)\text{ϕ}}^{+}\left( \overrightarrow{r}, E \right)\textit{dE dV.}}}


The target weights
:math:`\overline{w}\left( \overrightarrow{r},E \right)` of the
importance map are found using


.. math::
  :label: mavric-11

  \overline{w}\left( \overrightarrow{r},E \right) = \frac{R/S}{\text{ϕ}^{+}\left( \overrightarrow{r},E \right)\ }.


Each biased source
:math:`{\widehat{q}}_{i}\left( \overrightarrow{r},E \right)` pdf is
found using

.. math::
  :label: mavric-12

  {\widehat{q}}_{i}\left(\overrightarrow{r},E \right) = \frac{S_{i}}{R_{i}}{q_{i}\left( \overrightarrow{r},E \right)\text{ϕ}}^{+}\left( \overrightarrow{r}, E \right)\ ,


and the biased distribution used to select an individual source is
:math:`\widehat{p}\left( i \right) = \ R_{i}/\sum_{}^{}{R_{i} = R_{i}/R}`.

When using the biased distribution used to select an individual source,
:math:`\widehat{p}\left( i \right)`, and the biased source distribution,
:math:`{\widehat{q}}_{i}\left( \overrightarrow{r},E \right)`, the birth
weight of the sampled particle will be


.. math::
  :label: mavric-13

   \begin{matrix}
      w_{0} & \equiv & \left( \frac{p\left( i \right)}{\widehat{p}\left( i \right)} \right)\left( \frac{q_{i}\left( \overrightarrow{r}, E \right)}{{\widehat{q}}_{i}\left(\overrightarrow{r},E \right)} \right) \\ & = & \ \left( \frac{\frac{S_{i}}{S}}{\frac{R_{i}}{R}} \right) \left( \frac{q_{i}\left( \overrightarrow{r},E \right)}{\frac{S_{i}}{R_{i}}{q_{i}\left( \overrightarrow{r},E \right)\text{ϕ}}^{+}\left( \overrightarrow{r},E \right)} \right) \\
      & = & \frac{R/S}{\text{ϕ}^{+}\left( \overrightarrow{r},E \right)\ }, \\
  \end{matrix}


which matches the target weight,
:math:`\overline{w}\left( \overrightarrow{r},E \right)`.

Multiple tallies with CADIS
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The CADIS methodology works quite well for classic source/detector problems. The statistical uncertainty of the tally that serves as the adjoint source is greatly reduced since the Monte Carlo transport is optimized to spend more simulation time on those particles that contribute to the tally, at the expense of tracking particles in other parts of phase space. However, more recently, Monte Carlo has been applied to problems where multiple tallies need to all be found with low statistical uncertainties. The extension of this idea is the mesh tally—where each voxel is a tally where the user desires low statistical uncertainties. For these problems, the user must accept a total simulation time that is controlled by the tally with the slowest convergence and simulation results where the tallies have a wide range of relative uncertainties.

The obvious way around this problem is to create a separate problem for each tally and use CADIS to optimize each. Each simulation can then be run until the tally reaches the level of acceptable uncertainty. For more than a few tallies, this approach becomes complicated and time-consuming for the user. For large mesh tallies, this approach is not reasonable.

Another approach to treat several tallies, if they are in close proximity to each other, or a mesh tally covering a small portion of the physical problem is to use the CADIS methodology with the adjoint source near the middle of the tallies to be optimized. Since particles in the forward Monte Carlo simulation are optimized to reach the location of the adjoint source, all the tallies surrounding that adjoint source should converge quickly. The drawback to this approach is the difficult question of “how close.” If the tallies are too far apart, certain energies or regions that are needed for one tally may be of low importance for getting particles to the central adjoint source. This may under-predict the flux or dose at the tally sites far from the adjoint source.

MAVRIC has the capability to have multiple adjoint sources with this problem in mind. For several tallies that are far from each other, multiple adjoint sources could be used. In the forward Monte Carlo, particles would be drawn to one of those adjoint sources. The difficulty with this approach is that typically the tally that is closest to the true physical source converges faster than the other tallies—showing the closest adjoint source seems to attract more particles than the others. Assigning more strength to the adjoint source further from the true physical source helps, but finding the correct strengths so that all of the tallies converge to the same relative uncertainty in one simulation is an iterative process for the user.

Forward-weighted CADIS
~~~~~~~~~~~~~~~~~~~~~~

In order to converge several tallies to the same relative uncertainty in
one simulation, the adjoint source corresponding to each of those
tallies needs to be weighted inversely by the expected tally value. In
order to calculate the dose rate at two points—say one near a reactor
and one far from a reactor—in one simulation, then the total adjoint
source used to develop the weight windows and biased source needs to
have two parts. The adjoint source far from the reactor needs to have
more strength than the adjoint source near the reactor by a factor equal
to the ratio of the expected near dose rate to the expected far dose
rate.

This concept can be extended to mesh tallies as well. Instead of using a
uniform adjoint source strength over the entire mesh tally volume, each
voxel of the adjoint source should be weighted inversely by the expected
forward tally value for that voxel. Areas of low flux or low dose rate
would have more adjoint source strength than areas of high flux or high
dose rate.

An estimate of the expected tally results can be found by using a quick
discrete-ordinates calculation. This leads to an extension of the CADIS
method: forward-weighted CADIS (FW-CADIS).**Error! Bookmark not
defined.** First, a forward S\ :sub:`N` calculation is performed to
estimate the expected tally results. A total adjoint source is
constructed where the adjoint source corresponding to each tally is
weighted inversely by those forward tally estimates. Then the standard
CADIS approach is used—an importance map (target weight windows) and a
biased source are made using the adjoint flux computed from the adjoint
S\ :sub:`N` calculation.

For example, if the goal is to calculate a detector response function
:math:`\sigma_{d}\left( E \right)` (such as dose rate using
flux-to-dose-rate conversion factors) over a volume (defined by
:math:`g\left( \overrightarrow{r} \right)`) corresponding to mesh tally,
then instead of simply using
:math:`q^{+}\left( \overrightarrow{r},E \right) = \sigma_{d}\left( E \right)\ g(\overrightarrow{r})`,
the adjoint source would be


.. math::
  :label: mavric-14

   q^{+}\left( \overrightarrow{r},E \right) = \frac{\sigma_{d}\left( E \right)\text{g}\left( \overrightarrow{r} \right)}{\int_{}^{}{\sigma_{d}\left( E \right)\text{ϕ}\left( \overrightarrow{r},E \right)}\textit{dE}}\ ,

where :math:`\phi\left( \overrightarrow{r},E \right)` is an estimate of
the forward flux and the energy integral is over the voxel at :math:`\overrightarrow{r}`.
The adjoint source is nonzero only where the mesh tally is defined
(:math:`g\left( \overrightarrow{r} \right)`), and its strength is
inversely proportional to the forward estimate of dose rate.

The relative uncertainty of a tally is controlled by two components:
first, the number of tracks contributing to the tally and, second, the
shape of the distribution of scores contributing to that tally. In the
Monte Carlo game, the number of simulated particles,
:math:`m\left( \overrightarrow{r},E \right)`, can be related to the true
physical particle density, :math:`n\left( \overrightarrow{r},E \right),`
by the average Monte Carlo weight of scoring particles,
:math:`\overline{w}\left( \overrightarrow{r},E \right)`, by


.. math::
  :label: mavric-15

  n\left( \overrightarrow{r},E \right) = \ \overline{w}\left( \overrightarrow{r},E \right)\text{m}\left( \overrightarrow{r},E \right).


In a typical Monte Carlo calculation, tallies are made by adding some
score, multiplied by the current particle weight, to an accumulator. To
calculate a similar quantity related to the Monte Carlo particle density
would be very close to calculating any other quantity but without
including the particle weight. The goal of FW-CADIS is to make the Monte
Carlo particle density, :math:`m\left( \overrightarrow{r},E \right)`,
uniform over the tally areas, so an importance map needs to be developed
that represents the importance to achieving uniform Monte Carlo particle
density. By attempting to keep the Monte Carlo particle density more
uniform, more uniform relative errors for the tallies should be
realized.

Two options for forward weighting are possible. For tallies over some
area where the entire group-wise flux is needed with low relative
uncertainties, the adjoint source should be weighted inversely by the
forward flux, :math:`\phi\left( \overrightarrow{r},E \right)`. The other
option, for a tally where only an energy-integrated quantity is desired,
is to weight the adjoint inversely by that energy-integrated
quantity,\ :math:`\int_{}^{}{\sigma_{d}\left( E \right)\text{ϕ}\left( \overrightarrow{r},E \right)}\text{\ dE}`.
For a tally where the total flux is desired, then the response in the
adjoint source is simply :math:`\sigma_{d}\left( E \right) = 1`.

To optimize the forward Monte Carlo simulation for the calculation of
some quantity at multiple tally locations or across a mesh tally, the
adjoint source needs to be weighted by the estimate of that quantity.
For a tally defined by its spatial location
:math:`g\left( \overrightarrow{r} \right)` and its optional response
:math:`\sigma_{d}\left( E \right)`, the standard adjoint source would be
:math:`q^{+}\left( \overrightarrow{r},E \right) = \sigma_{d}\left( E \right)\text{g}\left( \overrightarrow{r} \right)`.
The forward-weighted adjoint source,
:math:`q^{+}\left( \overrightarrow{r},E \right)`, depending on what
quantity is to be optimized, is listed below.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **For the calculation of**                                                                                                                                                                                                                       | **Adjoint source**                                                                                                                                                                                                                                                                                                                                                      |
+==================================================================================================================================================================================================================================================+=========================================================================================================================================================================================================================================================================================================================================================================+
| Energy and spatially dependent flux.       :math:`\phi\left(\overrightarrow{r},E \right)`                                                                                                                                                        | .. math:: \frac{g\left( \overrightarrow{r}\right)}{\phi\left(\overrightarrow{r},E \right)}                                                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Spatially dependent total flux.         :math:`\int_{}^{}{\phi\left( \overrightarrow{r},E \right)}\textit{dE}`                                                                                                                                   | .. math:: \frac{g\left( \overrightarrow{r}\right)}{\int_{}^{}{\phi\left( \overrightarrow{r},E \right)}\textit{dE}}                                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Spatially dependent total response.         :math:`\int_{}^{}{\sigma_{d}\left( E \right)\text{ϕ}\left(\overrightarrow{r},E\right)}\textit{dE}`                                                                                                   | .. math:: \frac{\sigma_{d}\left( E \right)\text{g}\left( \overrightarrow{r} \right)}{\int_{}^{}{\sigma_{d}\left( E \right)\text{ϕ}\left( \overrightarrow{r},E \right)}\textit{dE}}                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The bottom line of FW-CADIS is that in order to calculate a quantity at
multiple tally locations (or across a mesh tally) with more uniform
relative uncertainties, an adjoint source needs to be developed for an
objective function that keeps some non-physical quantity—related to the
Monte Carlo particle density and similar in form to the desired
quantity—constant. FW-CADIS uses the solution of a forward
discrete-ordinates calculation to properly weight the adjoint source.
After that, the standard CADIS approach is used.

Composition block
~~~~~~~~~~~~~~~~~

Material information input follows the standard SCALE format for
material input. Basic materials known to the SCALE library may be used
as well as completely user-defined materials (using isotopes with known
cross sections). Input instructions are located in the XSProc chapter in
the SCALE manual. The Standard Composition Library chapter lists the
different cross section libraries and the names of standard materials.
An example is as follows:

::

   read composition

       uo2 1 0.2 293.0 92234 0.0055 92235 3.5 92238 96.4945 end

       orconcrete 2 1.0 293.0 end

       ss304 3 1.0 293.0 end

   end composition

Details on the cell data block are also included in the XSProc chapter.
When using different libraries for the importance map production (listed
at the top of the input) and the final Monte Carlo calculation (listed
in the parameters block, if different), make sure that the materials are
present in both libraries.


.. list-table:: Overall input format
   :widths: 30 30
   :header-rows: 1
   :align: center

   * - input file
     - Comment
   * - ::

         =mavric
         Some title for this problem
         v7-27n19g
         read composition
            ...
         end composition
         read celldata
            ...
         end celldata
         read geometry
            ...
         end geometry
         read array
            ...
         end array
         read volume
            ...
         end volume
         read plot
            ...
         end plot
         read definitions
            ...
         end definitions
         read sources
            ...
         end sources
         read tallies
            ...
         end tallies
         read parameters
            ...
         end parameters
         read biasing
            ...
         end biasing
         read importanceMap
            ...
         end importanceMap
         end data
         end
     - ::

          name of sequence
          title
          cross section library name
          SCALE material compositions
              [required block]

          SCALE resonance self-shielding
              [optional block]

          SCALE SGGP geometry
              [required block]

          SCALE SGGP arrays
              [optional block]

          SCALE SGGP volume calc
              [optional block]

          SGGP Plots
              [optional block]

          Definitions
              [possibly required]

          Sources definition
              [required block]

          Tally specifications
              [optional block]

          Monte Carlo parameters
              [optional block]

          Biasing information
              [optional block]

          Importance map
              [optional block]

          end of all blocks
          end of MAVRIC input


.. bibliography:: /bibs/mavric.bib  
