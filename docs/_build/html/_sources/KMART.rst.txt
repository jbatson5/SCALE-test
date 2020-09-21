.. _KMART:

KMART5 and KMART6: Postprocessors for KENO V.A and KENO-VI
==========================================================

*L. M. Petrie*

KMART5 and KMART6 (**K**\ eno **M**\ odule for
**A**\ ctivity-\ **R**\ eaction Rate **T**\ abulation) are modules whose
primary purpose is to postprocess a KENO V.a or KENO-VI restart file
with the corresponding working cross-section library to generate nuclide
activity tables. It also allows collapsing and printing fluxes
calculated by KENO. The KENO problem must have a mixing table, must
calculate the fluxes, and must write a restart file containing the
calculated data. KMART calculations are generally imbedded within a
CSAS5 or CSAS6 input file immediately following the CSAS input as a
stacked input case.

Introduction
------------

KMART5 and KMART6 (**K**\ eno **M**\ odule for
**A**\ ctivity-\ **R**\ eaction Rate **T**\ abulation) are modules whose
primary purpose is to postprocess a KENO V.a or KENO-VI restart file
with the corresponding working cross-section library to generate nuclide
activity tables. It also allows collapsing and printing fluxes
calculated by KENO. The KENO problem must have a mixing table, must
calculate the fluxes, and must write a restart file containing the
calculated data.

KMART Input Data
----------------

Input data for KMART is read into the program using free form blocked
input similar to KENO. The data blocks are started with a READ *BLOCK
NAME* and ended with an END *BLOCK NAME*. There are three data blocks
that KMART can read. The first data block is named INITIAL, and the
input starts with the keywords READ INITIAL. There are ten possible
keyworded entries in this block that may be entered in any order.

+-----------------------+-----------------------+-----------------------+
| Keyword               | Variable              | Description           |
+=======================+=======================+=======================+
| PRTVOLS               | PRINT_VOLUMES         | A flag to cause the   |
|                       |                       | volumes calculated by |
|                       |                       | KENO to be printed by |
|                       |                       | KMART. Off by         |
|                       |                       | default, turn on by   |
|                       |                       | entering.             |
+-----------------------+-----------------------+-----------------------+
| KUNIT=                | KUNIT                 | The logical unit      |
|                       |                       | number of the KENO    |
|                       |                       | restart file. The     |
|                       |                       | default is 35         |
+-----------------------+-----------------------+-----------------------+
| FNI=                  | RESTART               | *Mode_in* extra field |
|                       |                       | in the input restart  |
|                       |                       | file name             |
|                       |                       | [restart\_*mode_in*.k\|
|                       |                       | eno_input]            |
|                       |                       | and                   |
|                       |                       | [restart\_*mode_in*.k\|
|                       |                       | eno_calculated].      |
|                       |                       | The default is an     |
|                       |                       | empty field.          |
+-----------------------+-----------------------+-----------------------+
| XUNIT=                | XUNIT                 | The logical unit      |
|                       |                       | number of the         |
|                       |                       | cross-section         |
|                       |                       | library. The default  |
|                       |                       | is 4                  |
+-----------------------+-----------------------+-----------------------+
| ACTBYGRP              | ACTIVITIES_BY_GROUP   | A flag which turns on |
|                       |                       | printing activities   |
|                       |                       | by group. If the      |
|                       |                       | fluxes are collapsed, |
|                       |                       | the activities will   |
|                       |                       | be by broad group,    |
|                       |                       | otherwise they will   |
|                       |                       | be by fine group. Off |
|                       |                       | by default, turn on   |
|                       |                       | by entering           |
+-----------------------+-----------------------+-----------------------+
| RRPVOL                | REACTION_RATES_PER\_  | A flag causing the    |
|                       | UNIT_VOLUME           | activities to be      |
|                       |                       | printed per unit      |
|                       |                       | volume rather than    |
|                       |                       | integrated over the   |
|                       |                       | volume of the region. |
|                       |                       | Off by default, turn  |
|                       |                       | on by entering        |
+-----------------------+-----------------------+-----------------------+
| KENO3D                | NK3D                  | Unit number on which  |
|                       |                       | to write data for     |
|                       | K3DFILE               | plotting with KENO3D. |
|                       |                       |                       |
|                       |                       | File name of the KENO |
|                       |                       | input file (minus the |
|                       |                       | trailing extension).  |
|                       |                       | The plot data file    |
|                       |                       | will be named         |
|                       |                       | K3DFILE.kmt.          |
+-----------------------+-----------------------+-----------------------+
| NOPRINT               | PRINT_RESULTS         | A flag allowing       |
|                       |                       | suppressing printing  |
|                       |                       | results.              |
+-----------------------+-----------------------+-----------------------+
| FLUXBIN               | FLUX_BIN              | A flag to turn on     |
|                       |                       | generating a          |
|                       |                       | collapsed cross       |
|                       |                       | section file for      |
|                       |                       | TRITON.               |
+-----------------------+-----------------------+-----------------------+
| WUNIT                 | WGTD                  | The logical unit      |
|                       |                       | number on which to    |
|                       |                       | write an AMPX         |
|                       |                       | weighted library of   |
|                       |                       | the 1-D neutron cross |
|                       |                       | sections.             |
+-----------------------+-----------------------+-----------------------+

A sample data block is given below.

.. highlight:: scale

::

  READ INITIAL KUNIT=35 XUNIT=4 END INITIAL

One of the next two blocks is required, but both can be specified if
desired. If both are entered, either one can be first. The next data
block specified is named ACTIVITY, and the input starts with the
keywords READ ACTIVITY. It contains the data specifying which activities
are to be calculated. The activities are specified by pairs of numbers
giving the nuclide identifier and the reaction type identifier desired.
A list of reaction types, also known as MT numbers, can be found in
Appendix A of the XSLib chapter. These pairs are repeated until all the
desired activities have been specified. If the nuclides are identified
by the SCALE scheme, then the nuclide can be specified most explicitly
by following the nuclide by the keyword MIX= and the mixture number the
nuclide is in. By specifying a mixture of zero the activity will be
calculated for each region in which the nuclide occurs. If the nuclide
specifies a natural element identifier (1000*Z) and individual isotopes
occur on the cross-section library, the isotope activities will be
summed to produce the total activity for the element. If the nuclide is
a special nuclide, i.e., identified with a prefix id times a million + a
ZA, then MIX= must be specified as a mixture the nuclide occurs in. The
data pair is described below.

+---------+----------+----------------------------------------------------------------------------------------------------------+
| Keyword | Variable | Description                                                                                              |
+=========+==========+==========================================================================================================+
|         | NUCLIDE  | The nuclide identification number on the cross-section library for this activity request.                |
+---------+----------+----------------------------------------------------------------------------------------------------------+
| MIX     | MIXTURE  | Mixture number of the nuclide for this activity request.  This is an optional entry, and defaults to 0.  |
+---------+----------+----------------------------------------------------------------------------------------------------------+
|         | REACTION | The reaction type identifier for this activity request.                                                  |
+---------+----------+----------------------------------------------------------------------------------------------------------+

If no activities are desired, then the block can be omitted. A sample block is given below.

::

  READ ACTIVITY 92235 18 92235 27 92235 1452 END ACTIVITY

The other input block is named COLLAPSE, and starts with the keywords
READ COLLAPSE. There are two keyword entries that may be input in this
block. A flux factor to normalize the fluxes by can be specified. It
defaults to 1. The last fine group in the current broad group is the
other entry. The broad groups are specified sequentially starting with
group one. If the flux factor is specified more than once, the last
value given is used. The data is specified as below.

+---------+-------------+----------------------------------------------------------------------------------------------------------------------------------+
| Keyword | Variable    | Description                                                                                                                      |
+=========+=============+==================================================================================================================================+
| FACTOR  | FACTOR      | A flux multiplier used to scale the fluxes before printing (default 1.0).                                                        |
+---------+-------------+----------------------------------------------------------------------------------------------------------------------------------+
| LASTG=  | LAST_GROUP  | The last fine group to be included in the current broad group.  The broad groups are input sequentially starting with group one. |
+---------+-------------+----------------------------------------------------------------------------------------------------------------------------------+

If no collapsed fluxes are desired, then the block can be omitted. A sample block is given below.

::

  READ COLLAPSE FACTOR 1.0 LASTG=10 LASTG=20 LASTG=30 LASTG=56
   END COLLAPSE

KMART Sample Input
------------------

Sample input data for KMART5 is given in :numref:`list2-5-1`.

.. code-block:: scale
  :name: list2-5-1
  :caption: KMART5 sample input.

  =kmart5
  read initial kunit=64 xunit=4 prtvols end initial
  read activity
  1001 27
  6012 27
  8016 27
  92235 18 92235 27 92235 1452
  92238 18 92238 27 92238 1452
  94238 18 94238 27 94238 1452
  94239 18 94239 27 94239 1452
  94240 18 94240 27 94240 1452
  94241 18 94241 27 94241 1452
  94242 18 94242 27 94242 1452
  92000 18 92000 27 92000 1452
  94000 18 94000 27 94000 1452
  end activity
  read collapse lastg=10 lastg=20 lastg=30 lastg=56
  end collapse
  end

  end
