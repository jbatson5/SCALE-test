.. _11-1:

AMPX Library Utility Modules
============================

*D. Wiarda, L. M. Petrie*

Abstract

The purpose of this section is to document selected AMPX modules that
can benefit the analyst interested in editing, converting, or combining
cross-section libraries normally used by the SCALE system modules. The
input description for these codes is provided in the documentation of
the AMPX nuclear data processing code system that is distributed with
SCALE package.

.. _11-1-1:

Introduction
------------

AMPX is a modular system [1]_ that generates continuous energy (CE) and
multigroup (MG) cross section data from evaluated nuclear data files
such as ENDF/B. All the nuclear data libraries distributed with SCALE
have been processed using AMPX. In addition to data processing modules,
AMPX also includes a number of useful utility modules for checking,
manipulating, and editing the libraries in SCALE. This section lists and
briefly describes some of the AMPX utility codes that may be useful to
SCALE users. Input instructions for these codes can be found the AMPX
code documentation, which is distributed with the SCALE code package.
Additional AMPX modules of interest may also found in the documentation.

.. _11-1-2:

AJAX: MODULE TO MERGE, COLLECT, ASSEMBLE, REORDER, JOIN, AND/OR COPY SELECTED DATA FROM AMPX MASTER LIBRARIES
-------------------------------------------------------------------------------------------------------------

AJAX (**A**\ utomatic **J**\ oining of **A**\ MPX **X**-Sections) is a
module to combine data from different AMPX libraries. Options are
provided to allow merging from any number of files.

.. _11-1-3:

ALPO: MODULE TO CONVERT AMPX LIBRARIES INTO ANISN FORMAT
--------------------------------------------------------

ALPO (**A**\ NISN **L**\ IBRARY **P**\ RODUCTION **O**\ PTION) is a
module for converting AMPX working libraries into the library format
used by the legacy discrete ordinates transport codes ANISN and
DORT/TORT contained in the DOORS package. [2]_

.. _11-1-4:

CADILLAC: MODULE TO MERGE MULTIPLE COVARIANCE DATA FILES
--------------------------------------------------------

CADILLAC (**C**\ ombine **A**\ ll **D**\ ata **I**\ dentifiers
**L**\ isted in **L**\ ogical **A**\ MPX **C**\ overx-format) is a
module that can be used to combine multiple covariance data files in
COVERX format into a single covariance data file. The material IDs can
be changed as needed by the user.

.. _11-1-5:

COGNAC: MODULE TO CONVERT COVARIANCE DATA FILES IN COVERX FORMAT
----------------------------------------------------------------

COGNAC (**C**\ onversion **O**\ perations for **G**\ roup-dependent
**N**\ uclides in **A**\ MPX **C**\ overx-format) is a module that can
be used to convert a single COVERX-formatted data file from bcd format
to binary. Also, COGNAC can be used to convert from binary to bcd,
binary to binary, and bcd to bcd.

.. _11-1-6:

LAVA: MODULE TO MAKE AN AMPX WORKING LIBRARY FROM AN ANISN LIBRARY
------------------------------------------------------------------

LAVA (**L**\ et **A**\ NISN **V**\ isit **A**\ MPX) is a module that can
convert an ANISN formatted library (neutron, gamma, or coupled
neutron-gamma) to an AMPX working library that can be used in XSDRNPM.

.. _11-1-7:

MALOCS: MODULE TO COLLAPSE AMPX MASTER CROSS-SECTION LIBRARIES
--------------------------------------------------------------

MALOCS (**M**\ iniature **A**\ MPX **L**\ ibrary **O**\ f **C**\ ross
**S**\ ections) is a module to collapse AMPX master cross-section
libraries. The module can be used to collapse neutron, gamma-ray, or
coupled neutron-gamma master libraries.

.. _11-1-8:

PALEALE: MODULE TO LIST INFORMATION FROM AMPX LIBRARIES
--------------------------------------------------------

PALEALE lists selected data by nuclide, reaction, data-type from AMPX
master and working libraries.

.. _11-1-9:

RADE: MODULE TO CHECK AMPX CROSS-SECTION LIBRARIES
--------------------------------------------------

RADE (**R**\ ancid **A**\ MPX **D**\ ata **E**\ xposer) is provided to
check AMPX- and ANISN-formatted multigroup libraries. It will check
neutron, gamma, or coupled neutron-gamma libraries.

.. _11-1-10:

TOC: MODULE TO PRINT AN AMPX LIBRARY TABLE OF CONTENTS
------------------------------------------------------

Program TOC is a utility program to print a sorted table of contents of
an AMPX cross section library. It is designed to be run interactively,
with the cross section library specified as the argument.

References
~~~~~~~~~~

.. [1]
   D. Wiarda, M. L. Williams, C. Celik, and M. E. Dunn, “AMPX: A
   Modern Cross Section Processing System For Generating Nuclear Data
   Libraries,” *Proceedings of International Conference on Nuclear
   Criticality Safety,* Charlotte, NC, Sept 13-17 2015.

.. [2]
   **“**\ \ DOORS3.2a:   One, Two- and Three-Dimensional Discrete
   Ordinates Neutron/Photon Transport Code System”, Radiation Shielding
   Information Center package CCC-650, Oak Ridge National Laboratory
   (2003).
