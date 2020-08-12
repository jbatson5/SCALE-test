.. _appendixb:

MAVRIC Appendix B: MAVRIC Utilities
===================================

Introduction
------------

Several utilities are provided to aid users in dealing with some of the
output files produced by Monaco and MAVRIC. These utilities were
developed at ORNL for specific projects and have been added to SCALE so
that all users can benefit. More utilities have been added that deal
with Denovo, including the older \*.varscl files for flux output used in
SCALE 6.1 and the current binary \*.dff file for flux output used in
SCALE 6.2. These tools do not have the modern block/keyword input
structure but instead have a fixed format, which is fairly simple since
each utility is made for a very specific function.

Each is described in the following sections. Five sample problems,
``mavricUtilities1.inp``, ````mavricUtilities2.inp``, ``mavricUtilities3.inp``,
``mavricUtilities4.inp`` and ``mavricUtilities5.inp`` demonstrate the use of
some of these. For all of these utilities, filenames should be enclosed
in quotes.

Utilities working with Monaco mesh tally (\*.3DMAP) files
---------------------------------------------------------

+-----------------+-----------------+
| mt2ascii        | Convert a mesh  |
|                 | tally into an   |
|                 | ASCII text      |
|                 | file.           |
+-----------------+-----------------+
| mt2msl          | Convert a mesh  |
|                 | tally into a    |
|                 | mesh source     |
|                 | lite.           |
+-----------------+-----------------+
| mt2msm          | Convert a mesh  |
|                 | tally into a    |
|                 | mesh source.    |
| mt2silo         | Convert a mesh  |
|                 | tally file into |
|                 | a Silo file for |
|                 | VisIt.          |
+-----------------+-----------------+
| mt2vtk          | Convert one     |
|                 | dataset of one  |
|                 | family in a     |
|                 | mesh tally to   |
|                 | VTK format.     |
+-----------------+-----------------+
| mtAdder         | Add several     |
|                 | Monaco mesh     |
|                 | tally files     |
|                 | together into   |
|                 | one mesh tally. |
+-----------------+-----------------+
| mtAverager      | Average several |
|                 | Monaco mesh     |
|                 | tally files     |
|                 | into one mesh   |
|                 | tally.          |
+-----------------+-----------------+
| mtBinOp         | Binary          |
|                 | operation of    |
|                 | mesh tally      |
|                 | files: sum,     |
|                 | difference,     |
|                 | product, and    |
|                 | ratio.          |
+-----------------+-----------------+
| mtDisp          | Display the     |
|                 | basics of a     |
|                 | mesh tally      |
|                 | file.           |
+-----------------+-----------------+
| mtExpand        | Expand a        |
|                 | space-only mesh |
|                 | from a mesh     |
|                 | tally with an   |
|                 | energy          |
|                 | function.       |
+-----------------+-----------------+
| mtFilter        | Perform various |
|                 | filters on a    |
|                 | mesh tally      |
|                 | file.           |
+-----------------+-----------------+
| mtInv           | Invert all of   |
|                 | the values in a |
|                 | mesh tally.     |
+-----------------+-----------------+
| mtMask          | Keep only or    |
|                 | remove          |
|                 | specified       |
|                 | voxels of a     |
|                 | mesh tally      |
|                 | based on        |
|                 | geometry.       |
+-----------------+-----------------+
| mtMinMax        | Find the        |
|                 | location/value  |
|                 | of the min or   |
|                 | max of each     |
|                 | real mesh in a  |
|                 | mesh tally.     |
+-----------------+-----------------+
| mtMultiply      | Multiply a mesh |
|                 | tally by a      |
|                 | constant        |
|                 | factor.         |
+-----------------+-----------------+
| mtPull          | Pull values     |
|                 | from certain    |
|                 | voxels out of a |
|                 | mesh tally      |
|                 | file.           |
+-----------------+-----------------+
| mtRefine        | Subdivide the   |
|                 | mesh into       |
|                 | smaller meshes  |
|                 | for better      |
|                 | visualization.  |
+-----------------+-----------------+
| mtResp          | Apply a         |
|                 | response        |
|                 | function to one |
|                 | family of a     |
|                 | mesh tally      |
|                 | file.           |
+-----------------+-----------------+
| mtSplit         | Split off part  |
|                 | of a mesh tally |
|                 | file into a     |
|                 | separate mesh   |
|                 | tally file.     |
+-----------------+-----------------+

**mt2ascii - Convert a mesh tally into an ASCII text file.**

Intended use: Since mesh tally files are in binary, the viewer can be
used to list mesh values. To get the values from the entire file, this
utility can be used to create an ASCII text version.

Input: The mesh tally file name and the filename for the resulting ASCII
file

Output: An ASCII formatted file

Example:

.. highlight:: none

::

    =mt2ascii
    “/optional/path/meshTallyFilename.3dmap”  ! the mesh tally
    “/optional/path/outputFilename.txt”       ! output file name
    end

**mt2msl - Convert a mesh tally into a mesh source lite.**

Intended use: Convert a fissionSource.3dmap mesh tally computed by KENO
into a meshSoureLite (\*.msl) file that can be used by a subsequent KENO
run using starting source type nst=9.

Input: Name of mesh tally (\*.3dmap) file

Output: A mesh source lite (\*.msl) file

Example:

::

    =mt2msl
    "input.3dmap"    ! mesh file (*.3dmap) name
    1                ! family
    14               ! group, or 0 for family total
    "result.msl"     ! mesh source lite (*.msl) file name
    end

**mt2msm - Convert a mesh tally into a mesh source.**

Intended use: Turn a tally of fission rate data into a mesh source file.
Mesh tallies are stored in a generic \*.3dmap format, which consist of
several families, each with one or more datasets. A typical mesh tally
(without the “noGroupFluxes” keyword) contains three families: the
neutron fluxes with each energy group as a dataset, the photon fluxes
with each energy group as a data set, and the responses with each
response as a dataset. This program uses the spatial information of the
mesh tally and combines a user-given energy distribution for all voxels.
A second way to use this program is to use a whole family (all the
energy groups) without a user-given energy distribution.

Input:

Line 1: filename of mesh tally

Line 2: which family of tally

Line 3: which dataset of that family (or 0 for sum of family)

Line 4: source type: 1-neutron, 2-photon

Line 5: number of bins for mesh source

Lines : energy (eV) and pdf values

Lines : energy (eV) and pdf values

... ...

Lines : energy (eV) and pdf values

Line : energy (eV)

Line last: desired output name

Input:

Line 1: filename of mesh tally

Line 2: which family of tally

Line 3: -1 (meaning use the whole family)

Line 4: source type: 1-neutron, 2-photon

Line 5: desired output name

Output: The resulting mesh source stored with the desired filename

Notes: Statistics of mesh tally are discarded.

Example:

::

    =shell
       cp ${RTNDIR}/barrel1.mt1.3dmap .
    end

    =mt2msm
    “barrel1.mt1.3dmap”    ! mesh tally
    3                      ! mesh tally family (1-n, 2-p, 3-responses)
    1                      ! real mesh in that family (0 means total of family)
    1                      ! mesh source particle type  1-neutron, 2-photon
    143                    ! number of bins in binned histogram distribution
    1.9640E+07 1.29403E-08 ! E_1  pdf_1
    1.7332E+07 4.60970E-07 ! E_2  pdf_2
    1.6905E+07 2.56619E-06 ! E_3  pdf_3
       ...        ...
    1.2341E+03 5.28408E-06 ! E_142  pdf_142
    9.6112E+02 1.77756E-06 ! E_143  pdf_143
    7.4852E+02             ! E_144
    “barrel.fission.msm”   ! output filename
    end

    =shell
       cp barrel.fission.msm ${RTNDIR}
    end

Example:

::

  =mt2msm
  “fissionSource.3dmap”
  1                       ! neutron flux (for KENO 3dmap files there is only one family)
  -1                      ! use the whole family (keep all the energy groups)
  1                       ! particle type (neutron)
  “caas.kenovi.fissionSource.msm”
  end

In SCALE 6.1, the fission source distribution mesh tally produced by
KENO contained data representing the number of fissions in each mesh
cell in each energy group. In SCALE 6.2, the data stored was changed to
be the fissions per unit volume – the fission density. This is more
consistent with other mesh tallies from Monaco which store flux or dose
rates that represent averages over the mesh cells. This change also
allows the MeshFileViewer to display the KENO fission source
distribution better. The mt2msm utility program also changed from SCALE
6.1 to SCALE 6.2 to account for the change in what is stored in the KENO
mesh tally file. Therefore, **KENO-produced fission source mesh tallies
and the mt2msm utility should not be mixed-and-matched across versions
of SCALE.** Doing so would result in the final Monaco mesh source file
being improperly normalized, which would not properly represent the KENO
fission source distribution and would give incorrect results in
subsequent MAVRIC calculations. Because there is not a specific ‘version
flag’ in a mesh tally file or mesh source map file, the user must ensure
that they have used the same version of SCALE for both the CSAS6 and
MAVRIC sequences any time the CAAS capability is used.

**mt2silo - Convert a mesh tally file into a Silo file for VisIt.**

Input: Name of mesh file (\*.3dmap), name of a Silo file, and a format

Output: A new Silo file

Notes: For format, use either 2 (PDB) or 7 (HDF5).

Example:

::

    =mt2silo
    "perfect.3dmap"        ! the existing mesh tally
    "perfect.silo"         ! the new silo file
    7                      ! format - HDF5
    end

**mt2vtk - Convert one dataset of one family in a mesh tally to VTK
format.**

Intended use: This is a way to transfer Monaco mesh tally data into a
common format that can be used by many data visualization packages,
including VisIt. Mesh tallies are stored in a generic \*.3dmap format,
which consist of several families, each with one or more datasets. A
typical mesh tally contains three families: the neutron fluxes with each
energy group as a dataset, the photon fluxes with each energy group as a
data set, and the responses with each response as a dataset. This
program selects one dataset of one family and saves the data (and
optionally the absolute uncertainties) in an ASCII file using a VTK file
format.

Input: The mesh file name, which family, which dataset of that family,
whether or not to include absolute uncertainties and the filename for
the resulting VTK file

Output: An ASCII VTK-formatted file

Example:

::

    =mt2vtk
    “/optional/path/meshTallyFilename.3dmap”  ! the mesh tally
    1                                         ! neutron flux family
    5                                         ! energy group 5
    true                                      ! include uncertainties
    “/optional/path/outputFilename.vtk”       ! output file name
    end

Example:

::

    =mt2vtk
    “/optional/path/meshTallyFilename.3dmap”  ! the mesh tally
    3                                         ! the response family
    1                                         ! first response
    false                                     ! do not include uncertainties
    “/optional/path/outputFilename.vtk”       ! output file name
    end

**mtAdder - Add several Monaco mesh tally files together into one mesh
tally.**

Intended use: Add mesh tally results from different sources into one
tally. The resulting mesh tally is the sum of all the components in the
several mesh tallies—fluxes are added and responses are added. For
example, two runs of MAVRIC from two different sources can be made. The
mesh tally results can then be added together, getting the total fluxes
and total responses from each.

Input: The number of files, followed by the list of mesh tally filenames
to add, then the name of the total mesh tally

::

    =mtAdder
    n
    “filename_1”
    “filename_2”
    ...
    “filename_n”
    “resultFilename”
  end


Output: A new mesh tally file

Notes: All of the mesh tally files must be the same size and shape
(number of families, x cells, y cells, z cells, and energy groups in
each family) and have the same number of responses. Responses (if any)
must be consistent to calculate meaningful results.

Example:

::

    =mtAdder
    3
    “meshFilename_1.3dmap”
    “meshFilename_2.3dmap”
    “meshFilename_3.3dmap”
    “meshFilenameTotal.3dmap”
    end

**mtAverager - Average several Monaco mesh tally files into one mesh
tally.**

Intended use: Combine (average) separate runs of the same problem with
different random number seeds into one tally. For example, if a user
does 10 separate runs of the same problem (poor man’s parallel) and
wants to combine the results as if they were from one run, an average is
needed. The average and uncertainties are weighted by the number of
histories in each run, to maintain proper statistics.

Input: The number of files, each filename and how many histories, then
the name of the total mesh tally

::

    =mtAverager
    n
    “filename_1”   histories_1
    “filename_2”   histories_2
    ...           ...
    “filename_n”   histories_n
    “resultFilename”
    end

Output: A new mesh tally file

Notes: All of the mesh tally files must be the same size and shape
(number of families, x cells, y cells, z cells, and energy groups in
each family) and have the same number of responses. Responses (if any)
must be consistent to calculate meaningful results.

Example:

::

    =mtAverager
    3
    “meshFilename_1.3dmap”   800000
    “meshFilename_2.3dmap”   900000
    “meshFilename_3.3dmap”   800000
    “/home/area/meshFilename.ave.3dmap”
    end

**mtBinOp - Binary operation of mesh tally files: sum, difference,
product, and ratio.**

Intended use: Apply simple math to the results stored in mesh tally
files

Input: The first mesh tally, the operator: add (or sum, +), subtract (or
difference, -), multiply (or product, x, \*) and divide (or ratio, ÷,”
/”), the second mesh tally name and then name of the resulting mesh
tally file.

Output: A new mesh tally file

Notes: Uncertainties are propagated assuming the two mesh tallies are
uncorrelated, which may not always be a good assumption. Mesh tallies
need to have the same grid structure and number of families and groups.
Dataset names in the results are inherited from the first mesh tally and
may not make sense after the operation. When using the / (slash) for
division, enclose it in quotes (“/”).

::

    =mtBinOp
    “neutron.3dmap”     ! first operand
    divide              ! operation
    “total.3dmap”       ! second operand
    “ratio.3dmap”       ! output file name
    end

**mtDisp - Display the basics of a mesh tally file.**

Input: A mesh tally (\*.3dmap) file

Output: Some of the basic details of mesh file

Example:

::

    =mtDisp
    "simulation.mt2.dff"    ! existing mesh file
    end

**mtExpand - Expand a space-only mesh from a mesh tally with an energy
function**

Input: A mesh tally (\*.3dmap) file and some parameters

Output: A mesh file similar to a mesh source but with uncertainty

Example:

::

    =mtExpand
    'activate.mt1.3dmap'
    2 1  ! response family, first response - cobalt activate rate
    true ! multiply by voxel volumes
    2    ! make photon source
    19   ! groups
    2.00E+07 0
    1.00E+07 0
    8.00E+06 0
    6.50E+06 0
    5.00E+06 0
    4.00E+06 0
    3.00E+06 0
    2.50E+06 0
    2.00E+06 0
    1.66E+06 0.5
    1.33E+06 1.5
    1.00E+06 0
    8.00E+05 0
    6.00E+05 0
    4.00E+05 0
    3.00E+05 0
    2.00E+05 0
    1.00E+05 0
    4.50E+04 0
    1.00E+04
    'photonSource.3dmap'
    end

**mtFilter - Perform various filters on a mesh tally file.**

Input: A \*.3dmap mesh tally file and a group-wise response function

Output: A \*.3dmap mesh tally file

Notes: Three basics types of filters: 0) flattening filter, 1) high-pass
filter, 2) low-pass filter. For types 1 and 2, the values plus a given
number of standard deviations will be compared to the criteria. The
input list depends on filter type. Types 1 and 2 require a value and a
number of standard deviations (n_sigma). A flattening filter turns any
positive value into the value of “1.0”.

Filtering performed based on following comparisons;

value + n_sigmas*abs_unc > minValue (high-pass)

or

value + n_sigmas*abs_unc < maxValue (low-pass)

The number of sigmas can be positive or negative.

Examples:

::

    =mtFilter
    "doseRates.3dmap"     ! existing mesh tally file
    1                     ! high-pass filter:
    0.150                 !    keep dose rates above 0.150
    -3.0                  ! add -3.0 standard deviations to values before comparing
    "above.3dmap"         ! new mesh tally file
    end

    =mtFilter
    "above.3dmap"         ! existing mesh tally file
    0                     ! flattening filter
    "boolean.3dmap"       ! new mesh tally file
    end

**mtInv - Invert all of the values in a mesh tally.**

Intended use: Invert non-zero values in a mesh tally to be used in
further processing.

Input: The original mesh tally, the name of the resulting mesh tally
file

Output: A new mesh tally file

Notes: Uncertainties are propagated (the relative uncertainty of the
reciprocal of a value is the same as the relative uncertainty of the
value).

Example:

::

    =mtInv
    'someTally.3dmap'      ! existing mesh tally file
    'inverted.3dmap'       ! new mesh tally file
    end

**mtMask - Keep only or remove specified voxels of a mesh tally based on
geometry.**

Intended use: Only keep or remove certain portions of a mesh tally based
on the unit, media, or mixture at the center of the voxel.

Input: A mesh tally file, an action (keeponly or remove), an operation
(intersection or union) of the unit=u, media=r and mixture=m, a
replacement value for voxels not kept and the file name of the resulting
mesh tally file. User can specify things such as 1) keep only the voxels
that have unit=2 and mixture=5, 2) keep only the voxels that have
media=3 or mixture=4, 3) remove voxels that have unit=2 and mixture=5,
4) remove voxels that have media=3 or mixture=4. To not include the
unit, media, or mixture in the specification, use a value of -1.

Output: A new mesh tally file.

Notes: When processing a file before finding the maximum, make the
replacement value something very low. If mtMask is being used before
finding the minimum, then set the replacement value high. Media is the
SGGP media number within the unit.

::

    =mtMask
    "theTally.3dmap"       ! existing mesh tally file
    keeponly               ! use 'keeponly' or 'remove'
    intersection           ! use 'intersection' or 'union'
    2 -1 5                 ! unit=2 AND mixture=5
    0.0                    ! replacement value for voxels not kept
    'new.3dmap'            ! new mesh tally file
    end

    =mtMask
    "theTally.3dmap"       ! existing mesh tally file
    remove                 ! use 'keeponly' or 'remove'
    union                  ! use 'intersection' or 'union'
    -1 3 4                 ! media=3 OR mixture=4
    0.0                    ! replacement value for voxels removed
    'new.3dmap'            ! new mesh tally file
    end

**mtMinMax - Find the location/value of the min or max of each real mesh
in a mesh tally.**

Intended use: Determine the minimum or maximum values in a mesh tally.

Input: The mesh tally, what to find (minimums or maximums), how many
mins/maxs for each real mesh in the mesh tally, and the name of the text
output file to store the results

Output: A text output containing the values and locations of the
minimums or maximums of each real mesh in a tally file

Notes: The same information is also in the main SCALE output file.

Example:

::

    =mtMinMax
    'bigOleMeshTally.3dmap'   ! existing mesh tally file
    maximum                   ! find either minimums or maximums
    5                         ! list top 5 maximum values in each real mesh
    'theList.txt'             ! file name to store all of the results
    end

**mtMultiply - Multiply a mesh tally by a constant factor.**

Intended use: Multiply every group of every family in a mesh tally for
either a change in source strength or a change in units.

Input: The original mesh tally, the multiplier, and the name of the
resulting mesh tally file

Output: A new mesh tally file

Example:

::

    =mtMultiply
    “simulation.mt1.3dmap”       ! the mesh tally
    25.0                         ! source strength increase of 25
    “simulation.bigger.3dmap”    ! output file name
    end

**mtPull - Pull values from certain voxels out of a mesh tally file.**

Intended use: Get energy-dependent fluxes for certain locations from a
mesh file.

Input: A mesh file (\*.3dmap) file and a list of positions and/or voxels

Output: Listing of energy-dependent fluxes from each desired location to
an ASCII text file

Notes: Can pull fluxes either by a physical coordinate position or by
voxel indices. Positions should be entered as a set of x, y, z for
Cartesian coordinate system and r, θ, z for cylindrical coordinate
system.

Example:

::

    =mtPull
    "duh.mt2.3dmap"    ! existing mesh file
    n                  ! number of x,y,z points to pull
    x_1 y_1 z_1        ! coordinates of point 1
    x_1 y_2 z_2        ! coordinates of point 2
    ...
    x_n y_n z_n        ! coordinates of point n
    m                  ! number of i,j,k voxels to pull
    i_1 j_1 k_1        ! indices of voxel 1
    i_2 j_2 k_2        ! indices of voxel 2
    ...
    i_m j_m k_m        ! indices of voxel m
    "outputName.txt"   ! name of output text file
    =end

**mtRefine - Subdivide the mesh into smaller meshes.**

Input: A \*.3dmap mesh tally file with geometry mesh size (I,J,K) and
three integers describing how many subdivisions of each voxel to create
in each dimension

Output: A \*.3dmap mesh tally file with geometry mesh size
(I*nx,J*ny,K*nz)

Example:

::

    =mtRefine
    "fluxes.3dmap"        ! existing *.3dmap mesh tally file (I,J,K)
    nx ny nz              ! how to subdivide each
    "refined.3dmap"       ! new (largerer) *.3dmap mesh tally file (I*nx,J*ny,K*nz)
    end

**mtResp - Apply a response function to one family of a mesh tally
file.**

Intended use: Compute group-wise dose or reaction rates by combining a
response function with the scalar fluxes.

Input: A \*.3dmap mesh tally file and a group-wise response function

Output: A \*.3dmap mesh tally file containing one family

Example:

::

    =mtResp
    "fluxes.3dmap"        ! existing *.3dmap mesh tally file
    200                   ! number of bins in response
    1                     ! which family
    2.2675480E-04         ! response group 1
    2.2283355E-04         ! response group 2
    2.1878259E-04         ! response group 3
    ...
    3.6748440E-06         ! response group nbins-2
    3.6748443E-06         ! response group nbins-1
    3.6748436E-06         ! response group nbins
    "doseByGroup.3dmap"   ! new (smaller) *.3dmap mesh tally file
    end

**mtSplit - Split off part of a mesh tally file into a separate mesh
tally file.**

Intended use: Some mesh tallies may become so large that the
MeshFileViewer cannot load the entire file to view. This utility allows
users to split off one family or just one group of one family into a
separate mesh tally file.

Input: The original mesh tally, which family (neutron, photon, or
responses), and which dataset (usually a group). Instead of a dataset,
users may specify 0 to get the total of a family or -1 to get all
datasets for that family. The name of the resulting mesh tally also
needs to be given.

Output: A new, smaller, mesh tally file

Example:

::

    =mtSplit
    “mavricUtilities3.mt1.3dmap”       ! the mesh tally
    1                                  ! the family of neutron fluxes
    5                                  ! fifth neutron flux group
    “mavricUtilities3.nfluxg5.3dmap”   ! output file name
    end

Utilities for working with DENOVO binary flux (\*.dff) files
------------------------------------------------------------

These utilities include the following:

+-----------------------------------+-----------------------------------+
| dff2dso                           | Convert a Denovo flux file into a |
|                                   | Denovo spatial output file.       |
+-----------------------------------+-----------------------------------+
| dff2mai                           | Convert a Denovo flux file into a |
|                                   | mesh angular information file.    |
+-----------------------------------+-----------------------------------+
| dff2mim                           | Invert a Denovo flux file and     |
|                                   | store as a mesh importance map.   |
+-----------------------------------+-----------------------------------+
| dff2msl                           | Convert a Denovo flux file into a |
|                                   | mesh source lite.                 |
+-----------------------------------+-----------------------------------+
| dffBinOp                          | Binary operation of Denovo flux   |
|                                   | files: sum, difference, product,  |
|                                   | and ratio.                        |
+-----------------------------------+-----------------------------------+
| dffDisp                           | Display the basics of a Denovo    |
|                                   | flux file.                        |
+-----------------------------------+-----------------------------------+
| dffExpand                         | Expand a space-only Denovo flux   |
|                                   | file by an energy function.       |
+-----------------------------------+-----------------------------------+
| dffFilter                         | Perform various filters on a      |
|                                   | Denovo flux file.                 |
+-----------------------------------+-----------------------------------+
| dffFix                            | Fix the zero and negative values  |
|                                   | in a Denovo flux file.            |
+-----------------------------------+-----------------------------------+
| dffInt                            | Integrate a single particle type  |
|                                   | from a Denovo flux file.          |
+-----------------------------------+-----------------------------------+
| dffInv                            | Invert the values in a Denovo     |
|                                   | flux file.                        |
+-----------------------------------+-----------------------------------+
| dffMult                           | Multiply a Denovo flux file by a  |
|                                   | constant factor.                  |
+-----------------------------------+-----------------------------------+
| dffPull                           | Pull fluxes from certain voxels   |
|                                   | out of a Denovo flux file.        |
+-----------------------------------+-----------------------------------+
| dffResp                           | Apply a response function to      |
|                                   | scalar fluxes in a Denovo flux    |
|                                   | file.                             |
+-----------------------------------+-----------------------------------+
| dffSplit                          | Split off a single particle type  |
|                                   | from a Denovo flux file.          |
+-----------------------------------+-----------------------------------+

**dff2dso - Convert a Denovo flux file into a Denovo spatial output
file.**

Input: A binary (stream) Denovo flux file and which particle types to
convert

Output: A binary (stream) Denovo Spatial Output file

Notes: For particle type, use 1 for neutron, 2 for photon, and 0 for all
types.

Example:

::

    =dff2dso
    "neatStuff.dff"       ! existing Denovo flux file
    1                     ! keep only neutron information
    "neatStuff.dso"       ! new Denovo spatial output file
    end

**dff2mai - Convert a Denovo flux file into a mesh angular information
file.**

Intended use: Take the optional net current information from a Denovo
flux file and create the adjoint current unit vectors and lambda
parameters required for directional CADIS. This is stored in a mesh
angular information (\*.mai) file.

Input: A binary (stream) denovoFluxFile

Output: A binary (stream) meshAngularInfoFile, a mesh angular
information file

Example:

::

    =dff2mai
    "mavricUtilities3.adjoint.dff"           ! new denovoFluxFile
    "mavricUtilities3.mai"                   ! mesh angular info file
    end

**dff2mim - Invert a Denovo flux file and store as a mesh importance
map.**

Intended use: Make weight targets without a consistent biased mesh
source.

Input: A Denovo flux (\*.dff) file, a scalar constant, and the name of
Monaco mesh importance map (\*.mim) file.

Output: A Monaco mesh importance map (\*.mim) file.

Example:

::

    =dff2mim
    "adjoint.dff"    ! existing adjoint denovoFluxFile
    3.0e-10          ! constant  targetWeight = constant/adjFlux
    "test.mim"       ! new Monaco mesh importance map
    end

**dff2msl - Convert a Denovo flux file into a mesh source lite.**

Intended use: Take Denovo fission source information stored in a \*.dff
file and convert it to a mesh source lite file (\*.msl) to be used as a
KENO starting source, nst=9.

Input: A Denovo flux (\*.dff) file

Output: A mesh source lite (\*.msl) file

Example:

::

    =dff2msl
    "wishfulThinking.dff"    ! existing Denovo flux file
    "startingSource.msl"     ! mesh source lite file
    end

**dffBinOp - Binary operation of Denovo flux files: sum, difference,
product and ratio.**

Intended use: Apply simple math to the results stored in Denovo flux
files.

Input: The first flux file, the operator: add (or sum, +), subtract (or
difference, -), multiply (or product, x, \*), or divide (or ratio, ÷,
"/"), the second flux file name, and the name of the resulting flux file

Output: A Denovo flux file

Notes: Flux files need to have the same grid structure and number of
groups. When using the / (slash) for division, enclose it in quotes
("/").

Example:

::

    =dffBinOp
    "neutron.dff"     ! first operand
    divide            ! operation
    "total.dff"       ! second operand
    "ratio.dff"       ! output file name
    end

**dffDisp - Display the basics of a Denovo flux file.**

Input: A Denovo flux (\*.dff) file

Output: Some of the basic details of the Denovo flux file

Example:

::

    =dffDisp
    "fluxes.dff"          ! existing Denovo flux file
    end

**dffExpand - Expand a space-only Denovo flux file by an energy
function.**

Input: A Denovo flux (\*.dff) file (with a single group - a space-only
function), one or more particle types, and an energy function for each

Output: A full space/energy Denovo flux file

Example:

::

    =dffExpand
    "spatialFluxes.dff"       ! existing Denovo flux file (single group)
    2                         ! number of particles
    1                         ! particle type (1-neutron, 2-photon)
    27                        ! number of bins in binned histogram distribution
    2.00000E+07 3.0658021E-09 ! E_1  amount_1
    6.37630E+06 6.9767163E-09 ! E_2  amount_2
    3.01190E+06 1.1495182E-08 ! E_3  amount_3
       ...        ...
    3.00000E-02 1.7127996E-04 ! E_26  amount_26
    1.00000E-02 3.0910611E-04 ! E_27  amount_27
    1.00000E-05               ! E_28
    2                         ! particle type (1-neutron, 2-photon)
    19                        ! number of bins in binned histogram distribution
    2.00E+07 0.0              ! E_1  amount_1
    1.00E+07 0.0              ! E_2  amount_2
    8.00E+06 0.0              ! E_3  amount_3
       ...        ...
    1.00E+05 0.0              ! E_17  amount_17
    4.50E+04 0.0              ! E_18  amount_18
    1.00E+04                  ! E_19
    "expanded.dff"            ! new Denovo flux file
    end

**dffFilter - Perform various filters on a Denovo flux file.**

Intended use: Keep fluxes in a \*.dff file where the flux or response
meets a specified criterion.

Input: A Denovo flux file name, filter type, filter options, the output
file name

Output: A Denovo flux file

Notes: There are three basics types of filters: 0) flattening filter, 1)
high-pass filter, 2) low-pass filter. For types 1 and 2, the criteria
could be a computed response. The input list changes depending on the
filter type and whether a response function is included. For no response
function, use 0 for the number of groups. A flattening filter turns any
positive value into a value of “1.0”.

Examples:

::

    =dffFilter
    "some.dff"               ! input Denovo flux filename
    0                        ! filter type
    "flattened.dff"          ! output Denovo flux filename
    end

    =dffFilter
    "some.dff"               ! input Denovo flux filename
    2                        ! filter type
    10.0                     ! maximum value
    0                        ! number of groups for response function
    "simpleFiltered.dff"     ! output Denovo flux filename
    end

    =dffFilter
    "some.dff"               ! input Denovo flux filename
    1                        ! filter type
    10.0                     ! minimum value
    19                       ! number of groups for response function
    1.1620022E-05            !   should match total groups in file
    8.7445696E-06
    7.4596655E-06
    6.3505804E-06
    5.3994922E-06
    4.6016462E-06
    3.9522688E-06
    3.4588520E-06
    3.0130868E-06
    2.6200121E-06
    2.1944491E-06
    1.8269592E-06
    1.5149031E-06
    1.1595382E-06
    8.7044964E-07
    6.2187445E-07
    3.7080767E-07
    2.6877788E-07
    5.9327226E-07
    "respFiltered.dff"       ! output Denovo flux filename
    end

**dffFix - Fix the zero and negative values in a Denovo flux file.**

Intended use: Replace zero or negative values with nearest good
neighboring value. Checks previous group, previous x voxel, previous y
voxel, then previous z voxel.

Input: A Denovo flux file

Output: A new Denovo flux file

Example:

::

    =dffFix
    "original.dff"    ! existing Denovo flux file
    "repaired.dff"    ! new Denovo flux file
    end

**dffInt - Integrate a single particle type from a Denovo flux file.**

Input: A Denovo flux file, which particle type to integrate (1-neutron,
2-photon), and the filename of the resulting integrated file

Output: A single-group Denovo flux file

Example:

::

    =dffInt
    "coupled.dff"       ! existing Denovo flux file
    2                   ! particle type
    "photonTotal.dff"   ! new Denovo flux file (single group)
    end

**dffInv - Invert the values in a Denovo flux file.**

Input: A Denovo flux file

Output: A Denovo flux file

Notes: Only non-zero values are inverted

Example:

::

    =dffInv
    "fluxes.dff"        ! existing Denovo flux file
    "inverted.dff"      ! new Denovo flux file
    end

**dffMult - Multiply a Denovo flux file by a constant factor.**

Intended use: source strength change, change in units, etc.

Input: A Denovo flux file and a constant factor

Output: A Denovo flux file

Example:

::

    =dffMult
    "fluxes.dff"        ! existing Denovo flux file
    10000.0             ! change units from (/cm^2/s) to (/m^2/s)
    "multiplied.dff"    ! new Denovo flux file
    end

**dffPull - Pull fluxes from certain voxels out of a Denovo flux file.**

Intended use: Get energy-dependent fluxes for certain locations from a
flux file.

Input: A Denovo flux file and a list of positions and/or voxels

Output: Listing of energy-dependent fluxes from each desired location to
an ASCII text file

Notes: Can pull fluxes either by a physical coordinate position or by
voxel indices.

Example:

::

    =dffPull
    "fluxes.dff"       ! file with the scalar fluxes you want
    n                  ! number of x,y,z points to pull
    x_1 y_1 z_1        ! coordinates of point 1
    x_1 y_2 z_2        ! coordinates of point 2
    ...
    x_n y_n z_n        ! coordinates of point n
    m                  ! number of i,j,k voxels to pull
    i_1 j_1 k_1        ! indices of voxel 1
    i_2 j_2 k_2        ! indices of voxel 2
    ...
    i_m j_m k_m        ! indices of voxel m
    "outputName.txt"   ! name of output text file
    =end

**dffResp - Apply a response function to scalar fluxes in a Denovo flux
file.**

Intended use: Compute group-wise dose or reaction rates by combining a
response function with the scalar fluxes. This can be done for every
particle type in the flux file or a single specific particle type.

Input: A Denovo flux file, particle indicator and a group-wise response
function

Output: A Denovo flux file

Notes: 0-all particles, 1-neutron, 2-photon

Example:

::

    =dffResp
    "fluxes.dff"          ! existing coupled Denovo flux file
    1                     ! keep only neutron information
    200                   ! number of bins in response
    2.2675480E-04         ! response group 1
    2.2283355E-04         ! response group 2
    2.1878259E-04         ! response group 3
    ...
    3.6748440E-06         ! response group nbins-2
    3.6748443E-06         ! response group nbins-1
    3.6748436E-06         ! response group nbins
    "doses.dff"           ! new (smaller) Denovo flux fle
    end

or

::

    =dffResp
    "fluxes.dff"          ! existing Denovo flux file
    0                     ! keep all particles information
    46                    ! number of bins in response
    1.6151395E-04         ! response group 1, first neutron
    1.4451494E-04         ! response group 2
    1.2703618E-04         ! response group 3
    ...
    3.6748447E-06         ! response group 27, last neutron
    1.1620022E-05         ! response group 28, first photon
    8.7445696E-06         ! response group 29
    7.4596655E-06         ! response group 30
    ...
    5.9327226E-07         ! response group 46, last photon
    "doses.dff"           ! new Denovo flux file
    end

**dffSplit - Split off a single particle type from a Denovo flux file.**

Intended use: Make a flux file containing a single particle type from
another Denovo flux file.

Input: A Denovo flux file and a particle type

Output: A (smaller) Denovo flux file

Notes: 1-neutron, 2-photon

Example:

::

    =dffSplit
    "coupled.dff"     ! existing Denovo flux file
    2                 ! particle type
    "photons.dff"     ! new (smaller) Denovo flux file
    end

Utilities for working with DENOVO \*.varscl (a TORT format) files
-----------------------------------------------------------------

These utilities include the following:

+-----------------------------------+-----------------------------------+
| vs2dff                            | Convert a varscl file into a      |
|                                   | Denovo flux file.                 |
+-----------------------------------+-----------------------------------+
| vsAdder                           | Add two TORT \*.varscl files      |
|                                   | together into one \*.varscl file. |
+-----------------------------------+-----------------------------------+
| vsBinOp                           | Binary operation of TORT          |
|                                   | \*.varscl files: sum, difference, |
|                                   | product and ratio.                |
+-----------------------------------+-----------------------------------+
| vsDisp                            | Display the basic contents of a   |
|                                   | TORT \*.varscl file.              |
+-----------------------------------+-----------------------------------+
| vsFilter                          | Perform various filters on a TORT |
|                                   | \*.varscl file.                   |
+-----------------------------------+-----------------------------------+
| vsInt                             | Integrate a single particle type  |
|                                   | from a TORT \*.varscl file.       |
+-----------------------------------+-----------------------------------+
| vsInv                             | Invert the values in a TORT       |
|                                   | \*.varscl file.                   |
+-----------------------------------+-----------------------------------+
| vsMult                            | Multiply a TORT \*.varscl file by |
|                                   | a constant factor.                |
+-----------------------------------+-----------------------------------+
| vsPull                            | Pull fluxes from certain voxels   |
|                                   | out of a TORT \*.varscl file.     |
+-----------------------------------+-----------------------------------+
| vsReGrp                           | Regroup a TORT \*.varscl file.    |
+-----------------------------------+-----------------------------------+
| vsResp                            | Apply a response function to      |
|                                   | scalar fluxes in a TORT \*.varscl |
|                                   | file.                             |
+-----------------------------------+-----------------------------------+
| vsSplit                           | Split off part of a TORT          |
|                                   | \*.varscl file into a separate    |
|                                   | \*.varscl file.                   |
+-----------------------------------+-----------------------------------+

These utilities work with the \*.varscl files produced with SCALE 6 and
SCALE 6.1. The \*.varscl format (a TORT format) is a single precision,
binary format that has been replaced with the double precision, binary
\*.dff file (Denovo flux file) in SCALE 6.2. SCALE 6 and SCALE 6.1 users
can request the executable binaries for these utilities by sending an
email to scaleHelp@ornl.gov.

**vs2dff - Convert a varscl file into a Denovo flux file.**

Intended use: Convert a varscl file (used in previous versions of
MAVRIC) into a Denovo flux file (introduced in SCALE 6.2).

Input: The \*varscl file name, whether or not it is an adjoint flux, and
the filename for the resulting denovoFluxfile

Output: A binary (stream) denovoFluxFile

Example:

::

    =vs2dff
    "mavricUtilities3.adjoint.varscl"        ! the TORT varscl file
    true                                     ! it is an adjoint flux
    "mavricUtilities3.adjoint.dff"           ! new denovoFluxFile
    end

**vsAdder - Add two TORT \*.varscl files together into one \*.varscl
file.**

Intended use: Beta versions of MAVRIC used TORT and GRTUNC-3D and could
add the \*.varscl files from each together before using them to create
importance maps. MAVRIC now uses Denovo and no longer needs to add
separate GRTUNC/TORT files. This utility is designed for people wishing
to use the older files with the latest MAVRIC.

Input: Two \*.varscl file names, typically one from GRTUNC-3D and the
other from TORT, the filename of the added file, whether you want lots
of output displayed (“true” or “false”) and whether or not there is a
minimum value of flux to use. If so, it is then listed.

Output: A single \*.varscl with the specified name

Notes: Addition is commutative, but not all varscl files are created
equal. Do not mix up the GRTUNCL and the TORT files. GRTUNCL3D does not
fill in the header info quite right, so the added varscl file takes
header info only from the TORT varscl file.

Example:

::

    =vsAdder
    “/some/path/problem.gtunc.adjoint.varscl”
    “/some/path/problem.tort.adjoint.varscl”
    “total.varscl”
    f
    t
    1.0e-25
    end

    =shell
      cp total.varscl ${RTNDIR}/total.varscl
    end

**vsBinOp - Binary operation of TORT \*.varscl files: sum, difference,
product and ratio.**

Intended use: Apply simple math to the results stored in TORT \*.varscl
files.

Input: The first flux file, the operator: add (or sum, +), subtract (or
difference, -), multiply (or product, x, \*), and divide (or ratio, ÷,
"/"), the second flux file name, and the name of the resulting flux file

Output: A TORT \*.varscl file

Notes: Flux files need to have the same grid structure and number of
groups. When using the / (slash) for division, enclose it in quotes
("/").

Example:

::

    =vsBinOp
    "neutron.varscl"     ! first operand
    false                ! are these adjoint files?
    divide               ! operation
    "total.varscl"       ! second operand
    "ratio.varscl"       ! output file name
    end

**vsDisp - Display the basic contents of a TORT \*.varscl file.**

Input: A TORT \*.varscl file name and adjoint flag

Output: Text display

Examples:

::

    =vsDisp
    "some.varscl"            ! input TORT *.varscl filename
    false                    ! is this an adjoint varscl?
    end

    =vsDisp
    "some.varscl"            ! input TORT *.varscl filename
    adjoint                  ! is this an adjoint varscl?
    end

**vsFilter - Perform various filters on a TORT \*.varscl file.**

Intended use: Keep fluxes in a \*.varscl file where the flux or response
meets a specified criterion.

Input: A TORT \*.varscl file name, filter type, filter options, the
output file name

Output: A TORT \*.varscl file

Notes: There are three basics types of filters: 0) flattening filter, 1)
high-pass filter, 2) low-pass filter. For types 1 and 2, the criteria
could be a computed response. The input list changes depending on the
filter type and whether a response function is included. For no response
function, use 0 for the number of groups.

Examples:

::

    =vsFilter
    "some.varscl"            ! input TORT *.varscl filename
    false                    ! is this an adjoint varscl?
    0                        ! filter type
    "flattened.varscl"       ! output TORT *.varscl filename
    end

    =vsFilter
    "some.varscl"            ! input TORT *.varscl filename
    false                    ! is this an adjoint varscl?
    2                        ! filter type
    10.0                     ! maximum value
    0                        ! number of groups for response function
    "simpleFiltered.varscl"  ! output TORT *.varscl filename
    end

    =vsFilter
    "some.varscl"            ! input TORT *.varscl filename
    false                    ! is this an adjoint varscl?
    1                        ! filter type
    10.0                     ! minimum value
    19                       ! number of groups for response function
    1.1620022E-05            !   should match total groups in file
    8.7445696E-06
    7.4596655E-06
    6.3505804E-06
    5.3994922E-06
    4.6016462E-06
    3.9522688E-06
    3.4588520E-06
    3.0130868E-06
    2.6200121E-06
    2.1944491E-06
    1.8269592E-06
    1.5149031E-06
    1.1595382E-06
    8.7044964E-07
    6.2187445E-07
    3.7080767E-07
    2.6877788E-07
    5.9327226E-07
    "respFiltered.varscl"    ! output TORT *.varscl filename

**vsInt - Integrate a single particle type from a TORT \*.varscl file.**

Input: A TORT \*.varscl file

Output: A single-group TORT \*.varscl file

Example:

::

    =vsInt
    "coupled.varscl"       ! existing TORT *.varscl file
    false                  ! is this an adjoint file?
    2                      ! particle type (0-all, 1-neutron, 2-photon)
    "photonTotal.varscl"   ! new TORT *.varscl file (single group)
    end

**vsInv - Invert the values in a TORT \*.varscl file.**

Input: A TORT \*.varscl file

Output: A TORT \*.varscl file

Notes: Only non-zero values are inverted

Example:

::

    =vsInv
    "fluxes.varscl"        ! existing TORT *.varscl file
    false                  ! is this an adjoint file?
    "inverted.varscl"      ! new TORT *.varscl file
    end

**vsMult - Multiply a TORT \*.varscl file by a constant factor.**

Intended use: source strength change, change in units, etc.

Input: A TORT \*.varscl file and a constant factor

Output: A TORT \*.varscl file

Example:

::

    =vsMult
    "fluxes.varscl"        ! existing TORT *.varscl file
    false                  ! is this an adjoint file?
    10000.0                ! change units from (/cm^2/s) to (/m^2/s)
    "multiplied.varscl"    ! new TORT *.varscl file
    end

**vsPull - Pull fluxes from certain voxels out of a TORT \*.varscl
file.**

Intended use: Get energy-dependent fluxes for certain locations from a
flux file.

Input: A TORT \*.varscl file and a list of positions and/or voxels

Output: Listing of energy-dependent fluxes from each desired location to
an ASCII text file

Notes: Can pull fluxes either by a physical coordinate position or by
voxel indices.

Example:

::

    =vsPull
    "fluxes.varscl"    ! file with the scalar fluxes you want
    false              ! is this an adjoint file?
    n                  ! number of x,y,z points to pull
    x_1 y_1 z_1        ! coordinates of point 1
    x_1 y_2 z_2        ! coordinates of point 2
    ...
    x_n y_n z_n        ! coordinates of point n
    m                  ! number of i,j,k voxels to pull
    i_1 j_1 k_1        ! indices of voxel 1
    i_2 j_2 k_2        ! indices of voxel 2
    ...
    i_m j_m k_m        ! indices of voxel m
    "outputName.txt"   ! name of output text file
    end

**vsReGrp - Regroup a TORT \*.varscl file.**

Input: A TORT \*.varscl file and adjoint flag, then a list of how the
new groups should be formed from the old groups

Output: A smaller TORT \*.varscl file

Example:

::

    =vsReGrp
    "coupled.varscl"       ! existing TORT *.varscl file
    false                  ! is this an adjoint file?
    27                     ! number of neutron groups in file
    1                      ! new group assignment for each
    1                      !     existing neutron group
    1                      !   must start with one
    2                      !   each entry is same as last or
    ...                   !     increases by 1
    8                      ! new group assignment for neutron group 27
    19                     ! number of photon groups in file
    1                      ! new group assignment for each
    1                      !     existing photon group
    1                      !   must start with one
    2                      !   each entry is same as last or
    ...                   !     increases by 1
    4                      ! new group assignment for photon group 19
    "smaller.varscl"       ! new TORT *.varscl file name
    end

**vsResp - Apply a response function to scalar fluxes in a TORT
\*.varscl file.**

Intended use: Compute group-wise dose or reaction rates by combining a
response function with the scalar fluxes.

Input: A TORT \*.varscl file and a group-wise response function

Output: A TORT \*.varscl file

Example:

::

    =vsResp
    "fluxes.varscl"       ! existing coupled TORT *.varscl file
    false                 ! is this an adjoint file?
    200                   ! number of bins in response
    2.2675480E-04         ! response group 1
    2.2283355E-04         ! response group 2
    2.1878259E-04         ! response group 3
    ...
    3.6748440E-06         ! response group 198
    3.6748443E-06         ! response group 199
    3.6748436E-06         ! response group 200
    "doses.varscl"        ! new (smaller) Denovo flux fle
    end

**vsSplit - Split off part of a TORT \*.varscl file into a separate
\*.varscl file.**

Intended use: Make a flux file containing a single particle type from
another TORT \*.varscl file.

Input: A TORT \*.varscl file and a particle type

Output: A (smaller) TORT \*.varscl file

Example:

::

    =vsSplit
    "coupled.varscl"     ! existing TORT *.varscl file
    false                ! is this an adjoint file?
    2                    ! particle type (1-neutron, 2-photon)
    "photons.varscl"     ! new (smaller) TORT *.varscl file
    end

Miscellaneous utilities
-----------------------

These utilities include the following:

+-----------+----------------------------------------------------------------+
| dsi2asc   | Convert a Denovo simple input (\*.dsi) from binary to ASCII.   |
+===========+================================================================+
| dsiDisp   | Display the basics of a Denovo simple input file.              |
+-----------+----------------------------------------------------------------+
| dso2msl   | Use a Denovo spatial output to create a mesh source lite.      |
+-----------+----------------------------------------------------------------+
| dsoDisp   | Display the basics of a Denovo spatial output file.            |
+-----------+----------------------------------------------------------------+
| mim2wwinp | Convert a mesh importance map into an MCNP weight window file. |
+-----------+----------------------------------------------------------------+
| mimDisp   | Display the basics of a mesh importance map (\*.mim) file.     |
+-----------+----------------------------------------------------------------+
| mimNorm   | Normalize a mesh importance map to a given location/energy.    |
+-----------+----------------------------------------------------------------+
| msmDisp   | Display the basics of a mesh source map (\*.msm) file.         |
+-----------+----------------------------------------------------------------+

**dsi2asc - Convert a Denovo simple input (\*.dsi) from binary to ASCII**.

Intended use: Check a Denovo input file for correctness.

Input: Names of original binary Denovo simple input (\*.dsi) file and the desired ASCII text file

Output: Human-readable form of the Denovo input file

Example:

::

    =dsi2asc
    "input.dsi"    ! Denovo simple input file (binary)
    "ascii.txt"    ! new ascii text file
    end

**dsiDisp - Display the basics of a Denovo simple input file.**

Input:  A Denovo simple input (\*.dsi) file

Output:  Some of the basic details of the Denovo simple input file

Example:

::

    =dsiDisp
    "godiva.dsi"          ! existing Denovo simple input file
    end



**dso2msl - Use a Denovo spatial output to create a mesh source lite.**

Input: A \*.dso file is made of three-dimensional data sets called fields. Which field to convert? 1-n: convert that field    0: convert sum of all fields

Output: A mesh source lite (\*.msl) file for KENO-VI.

Example:

::

    =dso2msl
    "fisSource.dso"  ! Denovo spatial output file with many fields
    1                ! which field to use
    "test.msl"       ! new Monaco mesh source lite
    end


**dsoDisp - Display the basics of a Denovo spatial output file.**

Input: A Denovo spatial output (\*.dsi) file

Output: Some of the basic details of the Denovo spatial output file

Example:

::

    =dsoDisp
    "godiva.dso"          ! existing Denovo spatial output file
    end

**mim2wwinp - Convert a mesh importance map into an MCNP weight window
file.**

Intended Use: To create an MCNP weight window file from a Monaco mesh
importance map file outside of a MAVRIC calculation. Monaco mesh
importance map files store target weights, but MCNP wwinp files store
lower weight bounds. To convert, the user needs to supply the
windowRatio, *r* (the ratio of the upper weight bound for splitting to
the lower weight bound for roulette). Target weights, *t*, are the
average of the upper, *u*, and lower, *l*, weight window bounds, so
*l*\ =2\ *t*/(*r*\ +1). For example, for a Monaco target weight of 1.0
and a windowRatio of 10.0, the MCNP lower weight bound will be
*l*\ =2(1.0)/(10.0+1)=0.1818. To reduce the size of the map, the user
can specify which neutron and photon groups to store in the new file. If
the last group is less than the first group, no groups of that particle
will be stored.

Input:

Line 1: filename of the Monaco mesh importance map file

Line 2: windowRatio (>1.0)

Line 3: first_neutron_group last_neutron_group

Line 4: first_photon_group last_photon_group

Line 5: filename of the MCNP weight window input file

Output: The resulting weight window input file stored with the desired
filename

Notes: Geometry information in the Monaco mesh importance map file is
lost since the MCNP wwinp format does not support it.

Example:

::

      =mim2wwinp
    "/scale/smplprbs/mavric.graphiteCADIS.mim"  ! importance map
    19.0                                        ! window ratio
    5 22                                        ! save n groups 5-22
    19 1                                        ! save no p groups
    "/scale/test9/testmimww.wwinp"              ! new file
    end

**mimDisp - Display the basics of a mesh importance map file.**

Input: A mesh importance map (\*.mim) file

Output: Some of the basic details of mesh importance map file

Example:

::

    =mimDisp
    "the.mim"    ! existing mesh importance map file
    end

**mimNorm - Normalize a mesh importance map to a given
location/energy.**

Input: A mesh importance map (\*.mim) file, a location (x, y, z), a
particle type and energy, and a filename for the normalized map file.
Use 1 for neutron and 2 for photon. Energy should be in eV. The new
importance map file will be normalized such that the given
location/energy has a target weight of 1. If a particle type or energy
is 0, then the energy group with the minimum non-zero target value at
the given location will be the group that is set to 1.0 in the new file.
(This option is similar to the MCNP weight window generator.)

Output: A mesh importance map file

Example:

::

    =mimNorm
    "the.mim"       ! existing mesh importance map file
    27.5 -16.5 32.0 ! location
    1 1.0e6         ! neutron, 1 MeV
    "normed.mim"    ! new file that is normalized
    end

**msmDisp - Display the basics of a mesh source map file.**

Input: A mesh source map (\*.msm) file

Output: Some of the basic details of mesh source map file

Example:

::

    =msmDisp
    "the.msm"    ! existing mesh source map file
