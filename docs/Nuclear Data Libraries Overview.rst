.. _10-0:

SCALE Nuclear Data Libraries
============================

*Introduction by M. L. Williams and D. Wiarda*

Chapter 10 describes the SCALE cross section data libraries for use with
deterministic and Monte Carlo radiation transport modules. All cross section
libraries were processed from ENDF/B-VII.0 or -VII.1 evaluated data files using
the AMPX code system. [1]_  SCALE includes continuous-energy libraries, as well as
multigroup libraries with several group structures. Libraries are available for
neutron, gamma, and coupled neutron-gamma transport calculations. The fine and
broad multigroup libraries provided for reactor physics and criticality safety
applications in SCALE 6.2 include intermediate resonance parameters (lambdas)
and improved Bondarenko data for self-shielding calculations using the
Bondarenko method, or the traditional CENTRM-based procedures in SCALE can be
used for self-shielding. Section 10.1 in this chapter describes the available
cross section libraries.

Fine and broad group covariance libraries containing cross section uncertainties
and correlations are also distributed with SCALE for sensitivity/uncertainty
analysis with the Sampler and TSUNAMI modules. The covariance libraries include
a comprehensive collection of data for all nuclides included in the SCALE cross
section libraries. New 252-group and 56-group covariances based on ENDF/B-VII.1
and other data sources are available, along with the older 44-group covariance
library distributed with earlier releases of SCALE. The Covariance Libraries
chapter describes the contents of the SCALE 6.2 covariance libraries and
explains how they were processed.

Additional libraries used for transmutation calculations with ORIGEN are
described in the ORIGEN Data Resources section of the ORIGEN chapter. These
libraries include fission product yields, decay data, decay gamma spectra, etc.,
as well as supplemental cross section data not available in ENDF/B.

Reference
---------

.. [1]
  D. Wiarda, M. L. Williams, C. Celik, and M. E. Dunn, “AMPX: A Modern Cross Section Processing System for Generating Nuclear Data Libraries,” Proceedings of International Conference on Nuclear Criticality Safety, Charlotte, NC, Sept. 13–17, 2015.
