.. _7-9:

CAJUN: Module for Combining and Manipulating CENTRM Continuous-Energy Libraries
===============================================================================

*L. M. Petrie and N. M. Greene*

.. _7-9-1:

Introduction
------------

CAJUN is a program used to combine continuous-energy (CE) cross section
libraries for use in the cross-section processing codes CENTRM and PMC.
It is used primarily by SCALE sequences when processing pointwise cross
section data for DOUBLEHET unit cells with the XSProc module (see
:ref:`7-1-1`), although it can also be run standalone in conjunction
with CRAWDAD. CAJUN combines multiple CE libraries into a single
library, adds selected nuclides from one library into another library,
deletes nuclides from a specified library, or renames nuclides in a
library. CAJUN performs an analogous function for CE libraries as AJAX
does for multigroup libraries.

In order for input CE libraries to be read by CAJUN, they must be
assigned a unit number from 1 to 99. The SHELL module can be used to
link individual CE libraries to appropriate file names that are
accessible by unit number.

.. _7-9-2:

CAJUN Input Data
----------------

Input data for CAJUN is read into the program using FIDO type input. The
data is divided into three data blocks. The first data block provides
the output file number and number of libraries processed. The second
data block provides input library numbers, number of nuclides in each
library, and whether nuclides are selected by MAT or ZA number. The
third data block provides current nuclide MAT or ZA numbers and new
nuclide MAT or ZA numbers. Detailed description of the CAJUN input data
is provided below.

.. highlight:: none

::

  Data Block 1

    0$$  	unit assignments (1)

  	1.	lcen – logical unit number of output CE CENTRM library (1)

    1$$  	number of files to process (2)

  	1.	nfile – the number of CENTRM CE libraries to process (1)
  	2.	idtap – identifier for the new library (0)

  	T	terminate data block 1

  ***********************************************************************
   *** repeat data block(s) 2 and 3 "nfile" times to create new library
  ***********************************************************************

  Data Block 2

    2$$	file selection and treatment option (4)

  	1.	log – logical unit number of input CENTRM CE library (77)
  	2.	inum – number of nuclides selected from this library (0)
  		0 - select all nuclides on the library as is.
  		n – select all nuclides on the library as is except for those indicated in the 3$$ array.
  		n – select the "n" nuclides on the library listed in the 3$$ array.
  	3.	iopt – select nuclides by 'mat' or 'nza' number   (1)
  		0 – mat
  		1 – nza (default)
  	4.	nsq – sequence number of file opened on unit LOG (1)

  	T	terminate data block 2

  Data Block 3 (enter if inum is non-zero)

    3$$ 	nuclide selection list (inum)
  	      enter a positive identifier to select a nuclide.
  	      enter a negative identifier to exclude a nuclide.

    4$$ 	new nuclide identifiers (inum)
  	      enter the new nuclide identifiers in the locations corresponding
          to the positive identifier entry in the 3$ array.

    5$$ 	version of the data (–1,0,1,2,3,4/unk,ENDF,JEF,JENDL,BROND,CENDL)  (inum)

    6$$ 	8-Character Identifier for Thermal Kinematics Data  (inum)

    7$$ 	ZA-override Values.  Non-zero values will replace the ZA values in the
          Header Record.  The ZA values in the Data Directory records are not changed.  (inum)

  	T 	terminate data block 3

.. _7-9-3:

CAJUN I/O Units
---------------

CAJUN requires the following I/O devices.

+----------+--+---------------------------+
| Unit No. |  | Purpose                   |
+----------+--+---------------------------+
| 5        |  | Standard definition input |
|          |  |                           |
| 6        |  | Output                    |
|          |  |                           |
| 18       |  | Scratch file              |
+----------+--+---------------------------+
