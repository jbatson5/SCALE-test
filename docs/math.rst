math (quicker builds)
=====================

.. math::
  :label: eq8-1-3

  & \frac{1}{\mathrm{v}}\frac{\partial\Phi}{\partial t}\left( X,E,\Omega,t \right) + \Omega \bullet \nabla\Phi\left( X,E,\Omega,t \right) + \Sigma_{t}\left( X,E,\Omega,t \right)\Phi\left( X,E,\Omega,t \right)

    & \ \ \ \ \ \ \ \ = S\left( X,E,\Omega,t \right)

  & \ \ \ \ \ \ \ \ + \int_{E^{'}}^{}{\int_{\Omega^{'}}^{}{\Sigma_{s}\left( X,E^{'} \rightarrow E,\Omega^{'} \rightarrow \Omega,t \right)\Phi\left( X,E^{'},\Omega^{'},t \right)}}d\Omega^{'}dE^{'}\ ,


where

     Φ(X,E,Ω,t) = neutron flux (neutrons/cm:sup:`2`/s) per unit energy at
     energy E per steradian about direction Ω at position X at time t
     moving at speed v corresponding to E;

     Σ\ :sub:`t`\ (X,E,Ω,t) = macroscopic total cross section of the media
     (cm:sup:`−1`) at position X, energy E, direction Ω and time t;

     Σ\ :sub:`s`\ (X,E′→E,Ω′→Ω,t) = macroscopic differential cross section
     of the media (cm:sup:`−1`) per unit energy at energy E′ per steradian
     about direction Ω′ at position X, and time t, for scattering to
     energy E and direction Ω;

     S(X,E,Ω,t) = neutrons/cm\ :sup:`3`/s born at position X and time t
     per unit energy at energy E per steradian about direction Ω (excludes
     scatter source).

Defining q(X,E,Ω,t) as the total source resulting from the external
source, scattering, fission, and all other contributions, the following
relationship can be written.

.. math::
  :label: eq8-1-4

  q(X,E,\Omega, t) =

  & S(X,E,\omega, t) + \int_{E^{'}}^{}{\int_{\Omega^{'}}^{}{\Sigma_{s}\left( X,E^{'} \rightarrow E,\Omega^{'} \rightarrow \Omega,t \right)\Phi\left( X,E^{'},\Omega^{'},t \right)}}d\Omega^{'}dE^{'}\ ,



Combining :eq:`eq8-1-3` and :eq:`eq8-1-4`, assuming media to be stationary and ignoring time-dependence, yields

.. math::
  :label: eq8-1-5

  \ \Omega \bullet \nabla\Phi\left( X,E,\Omega \right)+ \Sigma_{t}\left( X,E,\Omega \right)\Phi\left( X,E,\Omega \right) = q\left( X,E,\Omega \right)

.. _8-1-6-2:

Continuous energy mode solution procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using the relationship X′ = X − RΩ, using an integrating factor on both
sides of :eq:`eq8-1-5`, and defining

.. math::

  T(R) = \int_{0}^{R} \Sigma_{t}(X - R^{'}\Omega, E)dR^{'} ,

the following equation can be written.

At this point, the problem becomes an eigenvalue problem. If there is no
external source, the source may be defined as

.. math::
  :label: eq8-1-6

  \Phi(X,E,\Omega) = \int_{O}^{\infty}q(X - R\Omega,E,\Omega)e^{-T(R)}dR

At this point, the problem becomes an eigenvalue problem. If there is no external source, the source may be defined as


.. math::
  :label: eq8-1-7

  q\left( X,E,\Omega \right) = & \int_{}^{}{\int_{}^{}{{dE^{'}d\Omega^{'}\ \Phi\left( X,E^{'},\Omega^{'} \right)\ \Sigma}_{s}\left( X,E^{'} \rightarrow E,\Omega^{'} \cdot \Omega \right)}}

  & + \ \frac{1}{k}Q^{'}(X,E,\Omega) ,

where

k
  is the largest eigenvalue of the integral equation,

Q′(X,E,Ω)
  is the fission source at position X for energy E and
  direction Ω (all fission contributions to point E from all energy
  points in the previous generation),

Σ\ :sub:`s`\ (X,E′→E,Ω′ Ω)
  is the scattering cross section for
  scattering at position X from energy point E′ and direction Ω′ to
  energy point E and direction Ω.

Assuming the fission neutrons to be isotropic, the fission source
Q′(X,E,Ω) can be written as

.. math::
  :label: eq8-1-8

  Q^{'}(X,E,\Omega) = \frac{1}{4\pi}\int_{E^{'}}^{}\int_{\Omega^{'}}^{}dE^{'}d\Omega^{'}\Phi(X,E^{'},\Omega^{'})\chi(X,E^{'}\rightarrow E)\nu(X,E^{'})\Sigma_{f}(X,E^{'}) ,

where

   χ(X,E′→E) is the fraction of neutrons born at energy point E from
   fission at energy point E′ in the media at position X,

   ν(X,E′) is the number of neutrons resulting from a fission at energy
   point E′ at position X,

   Σ\ :sub:`f`\ (X,E′) is the macroscopic fission cross section of the
   material at position X for a neutron at energy point E′.

Substituting :eq:`eq8-1-7` into :eq:`eq8-1-6` yields the following equation:

.. math::
  :label: eq8-1-9

   \ {\Phi\left( X,E,\Omega \right) = \int_{0}^{\infty}{\text{dR }e^{- T\left( R \right)}\left\{ \frac{1}{k}Q^{'}\left( X - R\Omega,E,\Omega \right) \right.\ }}

   {+ \left. \ \int_{E^{'}}^{}{\int_{\Omega^{'}}^{}{{dE^{'}d\Omega^{'}\Phi\left( X - R\Omega,E^{'},\Omega^{'} \right)\Sigma}_{s}\left( X - R\Omega,E^{'} \rightarrow E,\Omega^{'} \cdot \Omega \right)}} \right\}}

The definition of k may be given as the ratio of the number of neutrons
produced in the (n + 1)\ *th* generation to the number of neutrons
produced in the n\ *th* generation or the largest eigenvalue of the
integral equation. Using :eq:`eq8-1-8`, :eq:`eq8-1-6` can be written as

.. math::
  :label: eq8-1-10

  \ {\Phi\left( X,E,\Omega \right) =

  \int_{0}^{\infty}{\text{dR }e^{-T\left( R \right)}\left\{ \ \frac{1}{k}\int_{E^{'}}^{}{\int_{\Omega^{'}}^{}{{\nu\left( X - R\Omega,E^{'}\right)\text{ Σ}}_{f}\left( X - R\Omega,E^{'} \right)}\chi\left( X - R\Omega,E^{'}\rightarrow E \right)}\Phi\left( X - R\Omega,E^{'},\Omega^{'} \right)dE^{'}\frac{d\Omega^{'}}{4\pi}\  \right.\ }}

  {+ \left. \ \int_{E^{'}}^{}{\int_{\Omega^{'}}^{}{{dE^{'}d\Omega^{'}\text{ Φ}\left( X - R\Omega,E^{'},\Omega^{'} \right)\text{ Σ}}_{s}\left( X - R\Omega,E^{'}\rightarrow E,\Omega^{'} \cdot \Omega \right)}} \right\}}

Writing :eq:`eq9-1-10` in generation notation, multiplying and dividing
certain terms by Σ\ :sub:`t`\ (X,E) and multiplying both sides of the
equation by ν(X,E)Σ\ :sub:`f`\ (X,E), yields the following equation,
which is solved by KENO V in the continuous energy mode:

.. math::
  :label: eq8-1-11

  {\frac{{\nu\left( X,E \right)\text{ Σ}}_{f}\left( X,E \right)}{\Sigma_{t}\left( X,E \right)}\Sigma_{t}\left( X,E \right)\Phi_{n}\left( X,E,\Omega \right) = \frac{{\nu\left(X,E \right)\text{ Σ}}_{f}\left( X,E \right)}{\Sigma_{t}\left(X,E \right)}\Sigma_{t}\left( X,E \right)\int_{0}^{\infty}{\text{dR }e^{- T\left( R\right)}}}

  {{\left\{ \ \frac{1}{k}\int_{E^{'}}^{}{\int_{\Omega^{'}}^{}\frac{{\nu\left( X - R\Omega,E^{'} \right)\text{ Σ}}_{f}\left( X - R\Omega,E^{'} \right)}{\text{ Σ}_{t}\left( X - R\Omega,E^{'} \right)}\chi\left( X - R\Omega,E^{'} \rightarrow E \right)\text{ Σ}_{t}\left( X - R\Omega,E^{'} \right)}\Phi_{n - 1}\left( X - R\Omega,E^{'},\Omega^{'}\right)dE^{'}\frac{d\Omega^{'}}{4\pi} \right.\ }

  {\left. \  + \int_{E^{'}}^{}{\int_{\Omega^{'}}^{}\frac{\Sigma_{s}\left( X - R\Omega,E^{'} \rightarrow E,\Omega^{'} \cdot \Omega \right)}{\text{ Σ}_{t}\left( X -R\Omega,E^{'} \right)}\text{ Σ}_{t}\left( X - R\Omega,E^{'} \right)}\Phi_{n}\left(X - R\Omega,E^{'},\Omega^{'} \right)dE^{'}d\Omega^{'} \right\},}}

where n indicates the n\ *th* generation and n − 1 is the (n − 1)\ *th*
generation. Note that the left-hand side of the equation, ν(X,E)
Σ\ :sub:`f`\ (X,E)Φ:sub:`n`\ (X,E,Ω) is the fission production for the
n\ *th* generation.

The solution strategy used by KENO solves :eq:`eq9-1-11` by using an
iterative procedure. The fission production at point X at energy point E
due to neutrons in the (n − 1)\ *th* generation, normalized to the
system multiplication, is

.. math::

  \frac{1}{k}\int_{E^{'}}{}\int_{\Omega^{'}}{}\frac{\nu(X,E^{'})\Sigma_{f}(X,E^{'})}{\Sigma_{t}(X,E^{'})}\chi(X,E^{'}\rightarrow E)\Sigma_{t}(X,E)\Phi_{n-1}(X,E^{'}\Omega^{'})dE^{'}\frac{d\Omega^{'}}{4\pi}

The collision points used in KENO are chosen by selecting path lengths
from the distribution

e\ :sup:`−T(R)` ,

which is the probability of transport from any position X − RΩ to
position X.

The first collision density of neutrons at energy E per unit solid angle
about Ω resulting from the fission source produced by the (n − 1)
generation, normalized to the system multiplication, is
