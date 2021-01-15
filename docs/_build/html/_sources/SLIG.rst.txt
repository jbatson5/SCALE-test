.. _5A:

SCALE/Origen Library Generator (SLIG)
=====================================

.. sectionauthor:: B. R. Betzler
.. program:: SLIG

This Python script (:file:`slig.py`) semi-automates the process of generating
sets of cross-section libraries for ORIGEN calculations for spent fuel
depletion, decay, and source term analysis. SLIG performs several tasks:


  #. reads standard-format template files, obtaining information (e.g,
     enrichments, burnups, moderator densities, etc.) from the file
     header

  #. generates a set of input files according to this header
     information;

  #. builds a directory tree to house these input files;

  #. writes the addition to the :file:`arpdata.txt` file;

  #.  moves the final libraries to a new directory; and

  #.  reads the burnup list for each set of libraries and writes them in
      the addition to the :file:`arpdata.txt` file.

This manual is divided into five main sections based on the desired
application:

   :ref:`sect-SLIG-running` for running SCALE on a local machine or a computing cluster
   without a queue system;

   :ref:`sect-SLIG-advanced` for running SCALE on a cluster with a queue system;

   :ref:`sect-SLIG-examples` for editing and writing template files;

   :ref:`sect-SLIG-troubleshooting` for issues running SLIG; and

   :ref:`sect-SLIG-code-info` for making changes to the code.


.. _sect-SLIG-running:

Quick Start Directions
----------------------

The SLIG package is located in the SCALE source directory in
:file:`./packages/etc/slig/`. Because it is necessary to run SCALE to generate
the appropriate cross-section libraries, SLIG runs in a disjointed,
three-step process:

   #. Copy the contents of the :file:`./slig/src/` directory into
      :file:`./slig/testing/`. Move to the :file:`./slig/testing/` directory and use
      :command:`./slig.py -g` to perform tasks 1) through 4). If SLIG returns an error,
      follow the directions in the error message (see
      :ref:`sect-SLIG-troubleshooting`). After a successful run, three new
      items will appear in the current directory:

      :file:`runSpace/`
         the directory tree containing the input files,

      :file:`arpLibList.txt`
         a list of the locations of the libraries in the directory tree, and

      :file:`addToArpData.txt`
         additional lines for the arpdata.txt file.


   #. Run SCALE with each input within the directory tree (:file:`runSpace/`).
      Each input is located within the directory tree in the location
      :file:`./runSpace/templateName/inputID/`, where templateName is the prefix of
      the template file (i.e., :file:`templateName_template.inp`) and inputID is
      a string identifying the enrichment (eNN), moderator density (wMM, if
      applicable), and plutonium vector (vPP, if applicable) for the input.


   #. After all SCALE calculations are complete, use :command:`./slig.py -f` to
      perform task 5) and 6). SLIG will identify any missing libraries.
      After a successful run, two changes will be made in the current
      directory:

      :file:`newLibraries/`
         this directory containing the new libraries will appear, and

      :file:`addToArpData.txt`
         the burnup lists will be written on the this file.


The final result is an addition to the :file:`arpdata.txt` file
(:file:`addToArpData.txt`) and a directory containing all generated libraries
(:file:`newLibraries/`). Do not delete any files associated with :file:`slig.py` unless
it directs you to do so. The following options are available to the user
(see :ref:`sect-SLIG-running` for more options):

.. option:: -p <PATH>, -path=<PATH>

  This specifies the location of the template files. SLIG will search
  PATH and all its subdirectories for template files. The default path
  is the current directory.

.. option:: -x <XSLIB>, -xsections=<XSLIB>

  This specifies the cross section library used in all calculations.
  The default is ``v7-252``.

.. _sect-SLIG-advanced:

Advanced Options
----------------

The following are more advanced options available to the user:

.. option:: -e <EXT>, -extension=<EXT>

  This specifies the file extension that identifies a template file. By
  default, SLIG searches for files ending in ``_template.inp``).

.. option:: -a, -add

      This flag is used with the ``-g`` option (:command:`./slig.py -ga`) to
      add input files to the current directory tree (runSpace/). It also adds
      library information to addToArpData.txt and adds the location of the
      libraries in the directory tree to file:`arpLibList.txt`.

      This flag is used with the ``-f`` option (:command:`./slig.py -fa`) to
      add newly generated libraries to the current library directory
      (:file:`newLibraries/`).

.. option:: -d, -document

   This flag turns on documentation routines that automatically generate
   a LaTeX file (libraryInformation.tex) with data about each template
   file using information on the file header. This also generates a .pdf
   file (libraryInformation.pdf) using pdflatex (required for this to
   function properly). Additionally, any figures referenced within the
   templates must be located within the current directory or any of its
   subdirectories.

.. option:: -s, -submit

   This flag turns on routines that generate a PBS submit script for
   each input file for running on clusters with a queue system. It also
   generates a shell script to submit these jobs (with :command:`qsub`). The
   PBS submit script template (:file:`run1proc.pbs`) must be placed in the
   current directory.


The first two steps of the three-step process for running
SLIG (see :ref:`sect-SLIG-running`) change:

   1. Use :command:`./slig.py -gs` to perform tasks 1) through 4). After a
      successful run, four new items will appear in the current directory:

      :file:`runSpace/`
         the directory tree containing the input files,

      :file:`arpLibList.txt`
         a list of the locations of the libraries in the directory tree,

      :file:`addToArpData.txt`
         additional lines for the arpdata.txt file, and

      :file:`submitSLIGjobs`
         a shell script for submitting jobs to the queue.

   2. Run the shell script (:file:`./submitSLIGjobs`) to submit jobs to the
      queue. Note that this may submit a very large number of jobs to the
      queue.


When using :command:`./slig.py -ga`, SLIG will check for documentation and submit
scripts and will proceed with the same settings that were used for the
initial run of SLIG. For example, if the user initially runs
:command:`./slig.py -gds` to generate documentation and submit scripts then later uses
:command:`./slig.py -ga`, SLIG will proceed with adding documentation for the
additional templates and generating submit scripts. When SLIG generates
additional submit scripts, a separate numbered file is generated for
each new template (e.g., :file:`submitSLIGjobs1`).

.. _sect-SLIG-examples:

Template File Rules and Examples
--------------------------------

Example templates are provided with the SCALE distribution. For creating
new templates, it is best to use these templates as starter files and
make incremental changes as necessary for the new application. The
header at the top of each template file contains the information that
will be used to generate input files and documentation. Each line of
this header must start with an apostrophe; each line is a comment line
according to the SCALE standard input. There are two main sections in
this header:

   1. The **template header** (see :numref:`ex-SLIG-BWR` and :numref:`ex-SLIG-MOX`).
      This header has a parameter list and an option list:

      a. The *parameter list* identifies the strings within the template
         file that SLIG will replace as it generates input files. These
         parameters are found throughout the template file; SLIG will replace
         these with values as it generates each input files. SLIG identifies
         the parameter list starting from the first line containing the
         'parameter' string and each line thereafter that is indented more
         than five blank spaces (not including the apostrophe). The following
         is a list of rules for entering parameters:


            * Each parameter is entered on a separate line in the form "parameter-description".

            * Each parameter must be a unique string of characters.

            * Each parameter is a single string without spaces.

            * SLIG uses the "description" to characterize the parameter. If these
              descriptions are changed, SLIG may not be able to properly characterize
              each parameter. Thus, it is suggested that the descriptions in the
              following list are not changed.

            * There is some flexibility in changing the parameter strings.


      b. The *option list* identifies the quantities or values that SLIG
         uses to determine the values that will replace the parameters in each
         input file. SLIG identifies the option list starting from the first
         line containing the 'option' string and each line thereafter that is
         indented more than five blank spaces (not including the apostrophe).

         The following is a list of rules for entering options:

            * Each option is entered on a separate line in the
              form ``option - values``.

            * SLIG uses the "option" to recognize what to do with the values. If
              this is changed, SLIG may not be able to properly characterize each
              option. Thus, it is suggested that the options (to the left of the
              dash) in the following list are not changed.

            * For options with multiple values, each value must be separated with
              a comma.

            * For values to continue onto the next line, the last value in a line
              must end with a comma and the next line must be indented and must
              begin with the next value.

            * The values may be changed.


   2. The **documentation header** (see :numref:`ex-SLIG-MOX-doc-header`).
      The documentation header has two purposes. First, it is used to track
      information about the template (e.g., author, date created, and methodology)
      and the source documents that contributed to the template's creation. This
      simplifies updating input files for new versions of SCALE. Second,
      SLIG uses this header information to generate documentation files.
      SLIG identifies the documentation header starting from the first line
      containing 'Documentation' to the line starting with an apostrophe
      followed by a space and five dashes (``' -----``).

.. code-block:: none
   :name: ex-SLIG-BWR
   :caption: A typical BWR template header.

   ' ----------------------------------------------------------------
   '  template to generate libraries for ORIGEN-S
   '  parameters are: u235wt%       - wt% U235
   '                  u234wt%       - wt% U234
   '                  u236wt%       - wt% U236
   '                  u238wt%       - wt% U238
   '                  ddd           - coolant density (g/cc)
   '                  dancoff1      - dancoff factor 1
   '                  dancoff2      - dancoff factor 2
   '                  namelibrary   - name of generated ORIGEN library
   '                  specpow       - average specific power
   '                  daystoburn    - depletion interval in days
   '  options are:    name          - g10_
   '                  enrichment    - 0.5, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0
   '                  cool. density - 0.1, 0.3, 0.5, 0.7, 0.9
   '                  dancoff1      - 0.5041, 0.3937, 0.3182, 0.2631,
   '                                  0.2211
   '                  dancoff2      - 0.3229, 0.2541, 0.2069, 0.1722,
   '                                  0.1455
   '                  spec. power   - 25.0
   ' ----------------------------------------------------------------


.. code-block:: none
   :name: ex-SLIG-MOX
   :caption: A typical BWR MOX template header.

   ' ----------------------------------------------------------------
   '  template to generate libraries for ORIGEN-S
   '  parameters are: IcontentPu    - wt% plutonium: inner
   '                  IcontentU     - wt% uranium: inner
   '                  IEcontentPu   - wt% plutonium: inside edge
   '                  IEcontentU    - wt% uranium: inside edge
   '                  EcontentPu    - wt% plutonium: edge
   '                  EcontentU     - wt% uranium: edge
   '                  CcontentPu    - wt% plutonium: corner
   '                  CcontentU     - wt% uranium: corner
   '                  pu238wt%      - wt% Pu238
   '                  pu239wt%      - wt% Pu239
   '                  pu240wt%      - wt% Pu240
   '                  pu241wt%      - wt% Pu241
   '                  pu242wt%      - wt% Pu242
   '                  densityAm     - americium density (g/cc)
   '                  ddd           - coolant density (g/cc)
   '                  dancoff1      - dancoff factor 1
   '                  dancoff2      - dancoff factor 2
   '                  namelibrary   - name of generated ORIGEN library
   '                  specpow       - average specific power
   '                  daystoburn    - depletion interval in days
   '  options are:    name          - mox_g10_
   '                  pu content    - 4.0, 7.0, 10.0
   '                  pu vector     - 50.0, 55.0, 60.0, 65.0, 70.0
   '                  cool. density - 0.1, 0.3, 0.5, 0.7, 0.9
   '                  dancoff1      - 0.5041, 0.3937, 0.3182, 0.2631,
   '                                  0.2211
   '                  dancoff2      - 0.3229, 0.2541, 0.2069, 0.1722,
   '                                  0.1455
   '                  spec. power   - 25.0
   '                  burnups       - 0, 1, 2, 3, 4.5, 6, 7.5, 9,
   '                                  10.5, 12, 13.5, 15, 16.5, 18,
   '                                  19.5, 21, 24, 27, 30, 33, 36,
   '                                  39, 42, 45, 48, 51, 54, 57, 60,
   '                                  63, 66, 69, 72
   '                  pin_zone      - 26, 16, 24, 12
   '                  pin_gad       - 14
   '                  avg_pin_dens. - 10.4
   ' ----------------------------------------------------------------

.. code-block:: none
   :name: ex-SLIG-MOX-doc-header
   :caption: A typical MOX BWR documentation header.

   ' ----------------------------------------------------------------
   ' Documentation and Notes (empty fields are auto-populated):
   '  [Change Log]
   '    Rev 0: Generated by J. Doe |
   '    Rev 1: Generated by B. R. Betzler, June 2014 |
   '    Rev 2: Generated by B. R. Betzler, September 2015
   '  [Author(s)] B. R. Betzler
   '  [SCALE Version] SCALE 6.2
   '  [Reactor Type] Mixed Oxide Boiling Water Reactor General Electric 10x10-8
   '  [Model Info] 2D t-depl full assembly model (see Figure \ref{fi:mox_ge10x10-8}), xsLib cross-section library
   '  [Sources]
   '    1. B. J. Ade, ``Generation of Collapsed Cross Sections for Hatch 1 Cycles 1-3 and Generation of Generic BWR Reflector Cross Sections'', ORNL/LTR-2012/559, Oak Ridge National Laboratory, 2012. |
   '    2. H. Smith, J. Peterson, and J. Hu, ``Fuel Assembly Modeling for the Modeling and Simulation Toolset'', ORNL/LTR-2012-555 Rev. 1, Oak Ridge National Laboratory, 2013. |
   '    3. I. C. Gauld, ``MOX Cross-Section Libraries for ORIGEN-ARP'', ORNL/TM-2003/2, Oak Ridge National Laboratory, Oak Ridge, Tennessee, 2003. |
   '    4. U. Mertyurek and I. C. Gauld, ``Development of ORIGEN Libraries for Mixed Oxide (MOX) Fuel Assembly Designs'', to be published, 2015.
   '    5. H. Smith, J. Peterson, and J. Hu, ``Fuel Assembly Modeling for the Modeling and Simulation Toolset'', ORNL/LTR-2012-555 Rev. 1, Oak Ridge National Laboratory, 2013.
   '  [Data Range]
   '  [Libraries]
   '  [Power]
   '  [Other Info]
   '    Channel box data, fuel/gap/channel moderator densities, and temperatures from Reference 1.
   '    All other dimensions, materials, etc. from Reference 2.
   '    Gad layout altered according to best engineering judgement.
   '    MOX isotopic vector information from Reference 3.
   '    MOX zoning pattern from section 4.1 of Reference 4 (see Table 2, Eq.~3, and Eq.~4).
   '    Specific power from Reference 5.
   '  figure{mox_ge10x10-8.pdf: MOX BWR GE 10x10-8.}
   ' ----------------------------------------------------------------

UOX fuel parameters
~~~~~~~~~~~~~~~~~~~

The following (:numref:`ex-slig-uox-opts`) is a list of some of the parameters
available to the user for working with most PWR and BWR lattices:

.. code-block:: none
   :name: ex-slig-uox-opts
   :caption: SLIG input options for UOX-based templates

   u235wt% - wt% U235
   u234wt% - wt% U234
   u236wt% - wt% U236
   u238wt% - wt% U238

   ddd - coolant density (g/cc)

   dancoff1 - dancoff factor 1
   dancoff2 - dancoff factor 2

   namelibrary - name of generated ORIGEN library

   specpow - average specific power
   daystoburn - depletion interval in days


.. code-block:: none
   :name: ex-slig-uox-sample
   :caption: Example of a fully-specified UOX input.

   name - abb_

   enrichment - 0.5, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0

   cool. density - 0.1, 0.3, 0.5, 0.7, 0.9 (or mod. density - 1.65)

   dancoff1 - 0.4686, 0.3429, 0.2651, 0.2122, 0.1742
   dancoff2 - 0.3103, 0.2316, 0.1823, 0.1484, 0.1237

   spec. power - 25.0

   burnups - 0, 1, 2, 3, 4.5, 6, 7.5, 9,
             10.5, 12, 13.5, 15, 16.5, 18,
             19.5, 21, 24, 27, 30, 33, 36,
             39, 42, 45, 48, 51, 54, 57, 60,
             63, 66, 69, 72


MOX fuel parameters
~~~~~~~~~~~~~~~~~~~

For mixed oxide (MOX) PWR and BWR assemblies, there is a different
set of parameters available to the user. SLIG will recognize a file
as a MOX template by searching for the Pu-239 parameter. SLIG
automatically generates a MOX zoning pattern (see :numref:`fig-mox-zoning`) for
BWR and PWR lattices according to the values of ``pin_zone``, ``pin_gad``, and
``avg_pin_dens.``.

.. code-block:: none
   :name: ex-SLIG-mox-opts
   :caption: SLIG input options for MOX-based templates.

   IcontentPu - wt% plutonium: inner
   IcontentU - wt% uranium: inner

   IEcontentPu - wt% plutonium: inside edge
   IEcontentU - wt% uranium: inside edge

   EcontentPu - wt% plutonium: edge
   EcontentU - wt% uranium: edge

   CcontentPu - wt% plutonium: corner
   CcontentU - wt% uranium: corner

   pu238wt% - wt% Pu238
   pu239wt% - wt% Pu239
   pu240wt% - wt% Pu240
   pu241wt% - wt% Pu241
   pu242wt% - wt% Pu242

   densityAm - americium density (g/cc)

   ddd - coolant density (g/cc)

   dancoff1 - dancoff factor 1
   dancoff2 - dancoff factor 2

   namelibrary - name of generated ORIGEN library

   specpow - average specific power

   daystoburn - depletion interval in days


.. _fig-mox-zoning:
.. figure:: figs/SLIG/fig3.png
  :align: center
  :width: 500

  MOX zoning layout for a Westinghouse 14×14 PWR assembly
  showing the corner (green), edge (salmon), inside edge (magenta), and
  inner (red) pin zones.



.. code-block:: none
   :name: ex-mox-sample
   :caption: Example of a fully-specified MOX input.

   name - mox_abb_

   pu content - 4.0, 7.0, 10.0
   pu vector - 50.0, 55.0, 60.0, 65.0, 70.0

   cool. density - 0.1, 0.3, 0.5, 0.7, 0.9

   dancoff1 - 0.4686, 0.3429, 0.2651, 0.2122, 0.1742
   dancoff2 - 0.3103, 0.2316, 0.1823, 0.1484, 0.1237

   spec. power - 25.0

   burnups - 0, 1, 2, 3, 4.5, 6, 7.5, 9,
             10.5, 12, 13.5, 15, 16.5, 18,
             19.5, 21, 24, 27, 30, 33, 36,
             39, 42, 45, 48, 51, 54, 57, 60,
             63, 66, 69, 72

   pin_zone - 11, 20, 16, 12

   pin_gad - 4

   avg_pin_dens. - 10.4

The following is an explanation of each option:

.. describe:: name

      This is the prefix for the name of the final generated libraries. It
      should be unique to the template (i.e., other templates should have a
      different name).

.. describe:: enrichment

      This is a list of the :sup:`235`\ U enrichments [%] for which SLIG
      will create separate inputs.

.. describe:: cool.\ density, mod.\ density

      This is a list of the coolant or moderator densities [g/cm\ :sup:`3`]
      for which SLIG will create separate inputs.

.. describe:: dancoffN

      This is a list of dancoff factors that correspond to pin N. The
      length of this list must match the length of the coolant/moderator
      density list (the dancoff factor varies significantly with this
      density).

.. describe:: spec.\ power

      This is the specific power [MW/MTU] of the assembly.

.. describe:: burnups

      This is a list of cumulative burnup steps [GWd/MTU] that will be used
      to create the depletion steps. If a small step is not included, SLIG
      will print a warning and automatically insert one at the beginning of
      the calculation (for Xe equilibrium).

.. describe:: pu\ content

      This is a MOX-specific parameter that is a list of the average
      content of plutonium [%] in the assembly for which SLIG will create
      separate inputs. These quantities are calculated as a percentage of
      the total heavy metal loading in the assembly.

.. describe:: pu\ vector

      This is a MOX-specific parameter that is a list of the enrichments of
      :sup:`239`\ Pu [%] for which SLIG will create separate inputs. These
      quantities are calculated as a percentage of the total plutonium in
      the assembly and are used to calculate the entire plutonium
      vector :cite:`Gauld2003`.

.. describe:: pin_zone

      This is a MOX-specific parameter that lists of the number of pins in
      the inner, inside edge, edge, and corner zones (see Figure 5.A.3).
      This varies for each assembly.

.. describe:: pin_gad

      This is a MOX-specific parameter that specifies the number of
      Gd-bearing pins in the assembly. SLIG uses this quantity to calculate
      ensure that the specified Pu content of the assembly is correctly
      represented :cite:`Gauld2003`.

.. describe:: avg_pin_dens.

      This is a MOX-specific parameter that specifies the average density
      [g/cm\ :sup:`3`] of the pins in the assembly. SLIG uses this quantity
      to calculate ensure that the specified Pu content of the assembly is
      correctly represented.

Documentation header
~~~~~~~~~~~~~~~~~~~~

The documentation header has a free form–style entry, where sections
are specified by ``[Section Name]`` and the text for each section
follows afterward. Figures are referenced as ``figure{figureName.pdf:
Figure caption.}``. Any reference to the figure within the header must
be in LaTeX-like form; for this, the figure is labeled as
``fi:figureName``. The section name keywords ``[Data Range]``,
``[Libraries]``, and ``[Power]`` are reserved to be auto-populated by
SLIG according to information provided within the vars list. All
information within this header is transferred to the documentation
file.

The parameters in the file headers are located within the template file
in the appropriate locations. See the example templates for the proper
usage. The burndata card in the input file should only be three lines:

.. code-block:: none

   read burndata
   power=specpow burn=daystoburn down=0 end
   end burndata

because it will be populated by the burnup points listed in the file
header. There should also be a shell command at the end of the input
file to save the cross-section library:

.. code-block:: none

   =shell
     cp ft33f001.cmbined $RTNDIR/namelibrary
   end


.. _sect-SLIG-troubleshooting:

Troubleshooting
---------------

If at any time an error occurs, SLIG will exit after printing the reason
for the error and offer a possible solution. Following these
instructions should resolve most issues with SLIG. The following is a
list of factors to consider when having trouble running SLIG.

   * SLIG uses the module argparse.py (see
     https://docs.python.org/3/library/argparse.html) to handle command
     line arguments; SLIG will crash if it does not have access to it. For
     versions of Python that do not inherently support this module,
     download the :file:`argparse.py` file and include it in the directory with
     :file:`slig.py`.

   * If SLIG is crashing, there may be an issue with the version of
     Python. SLIG was developed to be functional with Python 2.7.6.

   * After running :command:`./slig.py -g`, the :file:`addToArpData.txt` file
     will have dummy placeholders instead of the burnup lists. These
     placeholders are replaced with the burnup lists that are read off of the
     SCALE output files. The burnup lists in the documentation file are the
     burnup lists specified in the template files.

.. _sect-SLIG-code-info:

Code Information
----------------

SLIG consists of a :class:`main`, one SCALE-specific class (:class:`manageTemplate`), and
three generic classes (:class:`messenger`, :class:`manageDirectory`, and
:class:`manageFile`):

   * :class:`main` reads and validates arguments, and contains a loop to make
     inputs and collect libraries

   * :class:`manageTemplate` manages templates (reads/sorts options, calculates
     concentrations)

   * :class:`messenger` manages all prints to the screen

   * :class:`manageDirectory` manages external directories (searching, making,
     etc.)

   * :class:`manageFile` manages external files (reading, writing, searching,
     copying, etc.)

SLIG calls a separate Python script (:file:`collectinfov04.py`) to perform
documentation functions. This script uses a template (:file:`basedoc.v04.tex`)
to generate the documentation file.

.. raw:: latex

  \clearpage

..
      . U. Mertyurek and I. C. Gauld, "Development of ORIGEN Libraries
      for Mixed Oxide (MOX) Fuel Assembly Designs," to be published,
      2015.
