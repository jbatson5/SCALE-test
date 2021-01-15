.. _3-1abc:

TRITON Appendices
=================

.. _3-1a:

XSDRN Model Block Description
-----------------------------

The model data block for *T-XSDRN* and *T-DEPL-1D* calculations allows
specification of the 1D geometry model and various control parameters
used in the transport solution. The XSDRN *MODEL* block input is
arranged in blocks of data that are similar to the NEWT *MODEL* block
input described in Chapter 9.2. The XSDRN model input starts with an
optional 80-character title, followed by a *PARAMETER* block, and then
the following three data blocks in any order: the *GEOMETRY* data block,
the *MATERIAL* data block, and the optional *COLLAPSE* data block. If
the *PARAMETER*, *GEOMETRY*, and *MATERIAL* data block are not
specified, an error message is printed and the problem is terminated.
Sample input files for *T-XSDRN* and *T-DEPL-1D* calculations are
provided in TRITON sample problem 2 and sample problem 3, respectively,
in :ref:`3-1`.

.. _3-1a-1:

XSDRN *PARAMETER* block
~~~~~~~~~~~~~~~~~~~~~~~

*PARAMETER* Block keyword = parm, para, parameter, or parameters

Valid *PARAMETER* block specifications are described below. For each
keyword, allowable values are listed in parentheses, and the default is
listed in brackets. Input that can take an arbitrary integer value is
indicated by an IN; similarly, any parameter that can take an arbitrary
real/floating point value is indicated by RN as the allowable value.
SCALE read routines allow the input of integers for real numbers, and
vice versa, and the number will be converted accordingly. The order of
the parameters within the block is arbitrary and may be skipped if a
default value is desired for that parameter. If a parameter is listed
multiple times, the final specified value is used.

**bf**\ =(RN) - Buckling factor, equal to twice the extrapolation
distance multiplier used to determine the zero point of the asymptotic
flux. [1.420892]

**collapse**\ =(yes/no) - If collapse=yes is specified, a flux-weighted
collapse is performed by material number; cross sections for each
nuclide in each material in the problem are collapsed to a specified (or
default) group structure based on the average flux in that material. If
collapse=yes, TRITON will look for the *COLLAPSE* block; if not found,
TRITON will generate cross sections based on the original group
structure. [no]

**deltay**\ =(RN) - The first transverse dimension in centimeters used
in a buckling correction to calculate

leakage normal to the principal calculation direction (i.e., the height
of a slab or a cylinder).

**deltaz**\ =(RN) - The second transverse dimension in centimeters used
in a buckling correction (i.e., the width of a slab).

**difftreatment**\ =(mg_1d_sigtr/mg_0d_diff/mg_0d_sigtr/1g_0d_sigtr) -
Diffusion treatment option for transverse leakage corrections. The
mg_1d_sigtr option uses zone-dependent transport cross-sections for the
transverse leakage correction. The mg_0d_diff option uses
flux-volume-weighted homogenized diffusion coefficients. The mg_0d_sigtr
option uses flux-volume weighted homogenized transport cross-sections.
The 1g_0d_sigtr option uses a one-group homogenized transport
cross-section. [1g_0d_sigtr]

**epsglobal**\ =(RN) - Overall problem convergence criteria. [1.0e-6]

**epsouter**\ =(RN) - Scalar flux convergence criteria. [1.0e-6]

**inners**\ =(IN) - Maximum number of inner iterations in an energy
group. [20]

**outers**\ =(IN) - Maximum number of outer iterations. [100]

**prtflux**\ =(yes/no) - Flag indicating whether or not scalar flux
values are should be printed in problem output. [no]

**prtangflux**\ =(yes/no) - Flag indicating whether or not angular flux
values should be printed in problem output. [no]

**prtbalnc**\ =(yes/no) - Flag indicating whether or not fine-group
material balance tables should be printed in problem output. [no]

**prtmxsec**\ =(yes/no/1d) - Flag indicating whether or not material
macroscopic cross sections should be printed in problem output. The 1D
option indicates that 2D scattering tables are not to be printed. [no]

**sn**\ =(2/4/6/8/16/32) - Sn quadrature order for the transport
calculations.

XSDRN *GEOMETRY* block

*GEOMETRY* Block keyword = geom, geometry

The *GEOMETRY* block is used to specify the geometry type (e.g., slab,
cylinder, or sphere), the boundary conditions, the 1D material mesh
(i.e., zone mesh), and the 1D spatial mesh used in the transport
calculation. The order of the parameters entered in the *GEOMETRY* block
is arbitrary and can be any of the following supported keyword
specifications or keyword array specifications.

**geom**\ =(slab/cylinder/sphere) - Problem geometry. Keywords
geometry=, ige=, and cyl for cylinder are also allowed. [slab]

**leftbc**\ =(vaccum/periodic/white/albedo/mirror) - Left-hand boundary
condition. Keywords ibl=, vac for vacuum, refl for mirror, and reflected
for mirror are also allowed. [mirror]

**rightbc**\ =(vaccum/periodic/white/albedo/mirror) - Right-hand
boundary condition. Keywords ibr=, vac for vacuum, refl for mirror, and
reflected for mirror are also allowed. [mirror]

**left_albedo** RN1 RN2 ... RNN **end left_albedo** **-** The left-hand
boundary albedo values as a function of energy group. The left_albedo
array is ignored if leftbc= is vacuum, periodic, white, or mirror. If
the left_albedo array is omitted and leftbc=albedo, white boundary
conditions are used. If the number of entries in the left_albedo array
does not equal the number of energy groups in the cross-section library,
an error message is printed and the problem is terminated.

**right_albedo** RN1 RN2 ... RNN **end right_albedo** **-** The
right-hand boundary albedo values as a function of energy group. The
right_albedo array is ignored if rightbc= is vacuum, periodic, white, or
mirror. If the right_albedo array is omitted and rightbc=albedo, white
boundary conditions are used. If the number of entries in the
right_albedo array does not equal the number of energy groups in the
cross-section library, an error message is printed and the problem is
terminated.

**zoneids** IN1 IN2 ... INN **end zoneids** **-** Material composition
number by zone. The number of entries in the zoneids array defines the
number of zones for the problem. If the zoneids array is not defined, an
error message is printed and the problem is terminated.

**zonedimensions** RN1 RN2 ... RNN **end zonedimensions** **-** The
right-hand boundary for each zone is given in centimeters. Note that the
left-hand boundary of the first zone is 0.0 and must not be entered. If
the zonedimensions array is not defined or the number of entries does
not equal the number of entries in the zoneids array, then an error
message is printed and the problem is terminated.

**zoneintervals** IN1 IN2 ... INN **end zoneintervals** **-** Number of
spatial mesh of constant width per each problem zone. If specified, the
number of entries of the zonedimensions array must equal the number of
entries in the zoneids array. Otherwise, an error message is printed and
the problem is terminated.

**mesh** RN1 RN2 ... RNN **end mesh** **-** The right-hand boundary for
each spatial mesh in centimeters. The spatial mesh is the discretization
used in the transport calculation. Note that the left-hand boundary of
the first spatial mesh is 0.0 and must not be entered. The zone
boundaries in the zonedimensions array must be a subset of the spatial
mesh boundaries in the mesh array. Otherwise, an error message is
printed and the problem is terminated. The mesh array is optional and is
not used if the zoneintervals array is specified. If neither the
zoneintervals array nor the mesh array is specified, an error message is
printed and the problem is terminated.

.. _3-1a-2:

XSDRN *MATERIAL* block
~~~~~~~~~~~~~~~~~~~~~~

*MATERIAL* Block keyword = matl, mat, material, materials

The *MATERIAL* block is used to specify the material numbers for each
material used in the calculation in the order of scattering cross
section to be used for each material. The format of the *MATERIAL* block
is identical to the NEWT *MATERIAL* block that is described in detail in
(:ref:`9-2`). Although source and description specifications are
allowed, these options are not used by XSDRN.

.. _3-1a-3:

XSDRN *COLLAPSE* block
^^^^^^^^^^^^^^^^^^^^^^

*COLLAPSE* Block keyword = collapse, coll

The *COLLAPSE* block is used to define the energy group collapsing
operation to calculate broad group cross-section libraries using the
XSDRN flux solution. The format of the *COLLAPSE* block is identical to
the NEWT *COLLAPSE* block that is described in detail in :ref:`9-2`.

.. _3-1b:

Data Structure for Cross Section Database File xfile016
-------------------------------------------------------

When branch calculations are performed, TRITON archives collapsed
homogenized cross sections in an unformatted, direct-access FORTRAN file
called *xfile016*. The contents and format of this file are described in
this appendix.

TRITON uses a library of SCALE subroutines to read and write blocks of
data to direct-access FORTRAN files. The SCALE subroutine library allows
the blocks of data to have variable length, even though direct-access
FORTRAN files have a fixed record length. The data blocks can be
retrieved from the file at random, provided the block length and block
starting record position are known. The block length is expressed in
terms of 4-byte words. For example, a block of 3-group macroscopic cross
sections that contained the total, fission, capture, chi, and nubar
cross sections would have a block length of 15 (3 × 5), assuming that
the cross sections are stored in single precision 4-byte format.

The *xfile016* file supports 11 different block types. The first seven
block types appear only once in the file, each block type occupying one
of the first seven record positions. The remaining four block types,
types 8–11, are repeated for each branch, at each depletion step,
starting at the eighth record position.

Branch-specific blocks, i.e., block types 8–11, are written in the
following order, for N branch calculations over M depletion steps:

First (t=0) transport calculation, branch 0 (reference state)

First (t=0) transport calculation, branch 1

First (t=0) transport calculation, branch 2

…

First (t=0) transport calculation, branch N

Second transport calculation, branch 0 (reference state)

Second transport calculation, branch 1

Second transport calculation, branch 2

…

Second transport calculation, branch N

…

…

…

(M + 1)\ :sup:`th` transport calculation, branch 0 (reference state)

(M + 1)\ :sup:`th` transport calculation, branch 1

(M + 1)\ :sup:`th` transport calculation, branch 2

…

(M + 1)\ :sup:`th` transport calculation, branch N

Note that (M + 1) × (N + 1) sets are saved for M depletion steps and N
branches. For each set, block types 8 and 9 are always written, whereas
block types 10 and 11 are written only if pin data output was requested
(nx ≠ 0).

.. centered:: Block Type 1: block length data

Length: 13

Position: 1

Type: integer.

Data: datlen(13)

datlen(1) Length of block type 1 (this array), which is 13.

datlen(2) Number of blocks allocated for this file (1000). Currently not
used.

datlen(3) Length of FORTRAN record for this file (512).

datlen(4) Length of block type 2: general dimensioning data.

datlen(5) Length of block type 3: depletion data.

datlen(6) Length of block type 4: branching data.

datlen(7) Length of block type 5: branching data for advanced branch
block (not yet supported).

datlen(8) Length of block type 6: currently not used.

datlen(9) Length of block type 7: energy group boundaries.

datlen(10) Length of block type 8: cross sections and misc data.

datlen(11) Length of block type 9: corner discontinuity factors.

datlen(12) Length of block type 10: pin power factors.

datlen(13) Length of block type 11: groupwise form factors.

.. centered:: Block Type 2: general dimensioning data

Length: datlen(4)

Position: 2

Type: integer, unless specified otherwise

Data: brnchdepl, nobranch, nsets, igm, iftg, ndelay, nadf, ncdf, ipin,
nxpin, nypin, ivers, adftype, branchflag

brnchdepl Number of depletion steps + 1.

nobranch Number of branches.

nsets Number of cross-section sets on library (typically 1).

igm Number of energy groups in collapsed cross sections.

iftg First thermal energy group (max upscatter group).

ndelay Number of delayed neutron precursor groups (6).

nadf Number of assembly discontinuity factors (ADFs).

ncdf Number of corner discontinuity factors (CDFs).

ipin Flag for pin data (0 = no pin data, 1 = pin data included).

nxpin Number of pins in x-direction (0 if ipin = 0).

nypin Number of pins in y-direction (0 if ipin = 0).

ivers Format version number. This appendix describes version 5 of the
database structure.

adftype ADF type: (1= single-assembly, 2= reflector, 3= single-assembly
on arbitrary grid lines).

branchflag (logical) TRUE for simple BRANCH block format, FALSE for
advanced format.

.. centered:: Block Type 3: depletion data

Length: datlen(5)

Position: 3

Type: real

Data: burnup(brnchdepl), time(brnchdepl), power(brnchdepl), sysHMdens

burnup(brnchdepl) Burnup (GWd/MTHM) at each transport step.

time(brnchdepl) Cumulative cycle time (days) at each transport step.

power(brnchdepl) Specific power (MW/MTHM) at each transport step.

sysHMdens System heavy metal mass density (g/cm\ :sup:`3`).

.. centered:: Block Type 4: branching data

Length: datlen(6)

Position: 4

Type: integer, unless specified otherwise

Data: fuelused, modused, crused, fuelcount, modcount, crcount, crref,
tfref, tmref, mdref, sbref, fuelmix(fuelcount), modmix(modcount),
crinmix(crcount), croutmix(crcount), crstate(nobranch), tfuel(nobranch),
tmod(nobranch), dmod(nobranch), sboron(nobranch)

fuelused (logical) TRUE if fuel mixtures were specified for branches.

modused (logical) TRUE if moderator mixtures were specified for
branches.

crused (logical) TRUE if control rod mixtures were specified for
branches.

fuelcount Number of mixtures in fuel definition.

modcount Number of mixtures in moderator definition.

crcount Number of mixture pairs in control rod definition.

crref Reference control rod state (0/1).

tfref (real) Reference fuel temperature (K).

tmref (real) Reference moderator temperature (K).

mdref (real) Referenced moderator density (g/cm\ :sup:`3`).

sbref (real) Reference soluble boron concentration (ppm).

fuelmix(fuelcount) Mixtures defined as fuel.

modmix(modcount) Mixtures defined as moderator.

crinmix(crcount) Mixtures defined for the control-rod in state.

croutmix(crcount) Mixtures defined for the control-rod out state.

crstate(nobranch) Control rod state (0=withdrawn/1=inserted) for each
branch.

tfuel(nobranch) (real) Fuel temperature (K) for each branch.

tmod(nobranch) (real) Moderator temperature (K) for each branch.

dmod(nobranch) (real) Moderator density (g/cm\ :sup:`3`) for each branch.

sboron(nobranch) (real) Soluble boron concentration (ppm) for each
branch.

.. centered:: Block Type 5: advanced branching data

Length: datlen(7)

Position: 5

Type: integer

Data: Stores data for advanced branch block (not yet supported)

.. centered:: Block Type 6: currently not used

..

.. centered:: Block Type 7: energy group boundary data

Length: datlen(9)

Position: 7

Type: real

Data: ebnds(igm+1)

ebnds(igm+1) Energy group boundaries

Blocks 1–7 are written only once. Blocks 8 and 9 (plus 10 and 11 if pin
power data is output) are written for each branch case at each depletion
step.

.. centered:: Block Type 8: cross-section data

Length: datlen(10)

Position: 8 + ( igm + 3 ) [ i \* ( nobranch + 1 ) + j ] ) , i = 0,…,
brnchdepl, j = 0,…, nobranch

Type: real

Data: {kinf(i), beta_eff(1:ndelay, i), lam_eff(1:ndelay, i) , y_i135(i),
y_xe135(i), y_pm149(i), id(i), nden(i), aden(i), [sigt(i,j), siga(i,j),
xemac(i,j), smmac(i,j), sigc(i,j), sigf(i,j), sign2n(i,j), sigtr(i,j),
nusigf(i,j), kappaf(i,j), nu(i,j), chi(i,j), diffcoef(i,j), flux(i,j),
sigselas(i,j), sig_xe(i,j), sig_sm (i,j), detfis(i,j), detflx(i,j),
invvel(i,j), sigtr2(i,j), sigtr(i,j), [(adf(i,j,k),
k=1,nadf),(0,k=nadf+1,12), (current(i,j,k), k=1,nadf),(0,k=nadf+1,12) ],
(sigs(i,j,k), k=1,igm), j=1,igm], i=1,nsets}

Data is saved for i = 1,nsets (number of homogenized regions):

kinf(i) k-infinity

beta_eff(1:ndelay,i) Approximate delayed neutron fractions.

lam_eff(1:ndelay,i) Approximate delayed neutron decay constants
(sec:sup:`-1`).

y_i135(i) Fission product yield for :sup:`135`\ I.

y_xe135(i) Fission product yield for :sup:`135`\ Xe.

y_pm149(i) Fission product yield for :sup:`149`\ Pm.

Data is saved for j = 1, igm (number of energy groups):

sigt(i,j) Total cross section (cm:\ sup:`-1`).

siga(i,j) Effective absorption cross section (cm:\ sup:`-1`).

xemac(i,j) Macroscopic :sup:`135`\ Xe cross section (cm:\ sup:`-1`)

smmac(i,j) Macroscopic :sup:`149`\ Sm cross section (cm:\ sup:`-1`).

sigc(i,j) Capture cross section (cm:\ sup:`-1`).

sigf(i,j) Fission cross section (cm:\ sup:`-1`).

sign2n(i,j) Effective n2n cross section (cm:\ sup:`-1`).

sigtr(i,j) Transport cross section (cm:\ sup:`-1`), determined by
outscatter approximation.

nusigf(i,j) Average total number of neutrons/fission × fission cross
section (cm:\ sup:`-1`).

kappaf(i,j) Energy released per capture × capture cross section +

   Energy released per fission × fission cross section (J/cm).

nu(i,j) Average total number of neutrons released per fission (delayed +
prompt).

chi(i,j) Fission spectrum (delayed + prompt).

diffcoef(i,j) Diffusion coefficient (cm), 1 / ( 3 × sigtr(i,j) ).

flux(i,j) Average flux (n/cm:\ sup:`2`-sec).

sigselas(i,j) Total elastic scattering cross section (cm:\ sup:`-1`).

sig_xe(i,j) Microscopic cross section for :sup:`135`\ Xe (barns).

sig_sm (i,j) Microscopic cross section for :sup:`149`\ Sm (barns).

detfis(i,j) Microscopic :sup:`235`\ U cross section at detector location
(barns).

detflx(i,j) Average flux in detector mixture (n/cm:\ sup:`2`-sec).

invvel(i,j) Inverse neutron velocity (sec/cm).

sigtr2(i,j) Transport cross section (cm:\ sup:`-1`), determined by
inscatter approximation.

sigtr(i,j) Transport cross section (cm:\ sup:`-1`), determined by
outscatter approximation.

adf(1:nadf,i,j) Assembly discontinuity factors for up to 12 faces.

current(1:nadf,i,j) Net current for up to 12 faces (n/cm:\ sup:`2`-sec),
adftype = 3 only.

sigs(i,j,k), k=1,igm Macroscopic scattering cross section, j k
(cm:\ sup:`-1`).

End of data saved for j = 1, igm

End of data saved for i = 1,nsets

.. centered:: Block Type 9: corner discontinuity factors

Length: datlen(11)

Position: 9 + ( igm + 3 ) [ i \* ( nobranch + 1 ) + j ] ) , i = 0,…,
brnchdepl, j = 0,…, nobranch

Type: real

Data: (( cdf(i,j), i=1,ncdf), j=1,igm)

Data is saved for i = 1,ncdf (number of “corner” discontinuity factors):

Data is saved for j = 1, igm (number of energy groups):

cdf(i,j) Corner discontinuity factors

End of data saved for j = 1, igm

End of data saved for i = 1,ncdf

.. centered:: Block Type 10: pin power peaking factors

Length: datlen(12)

Position: 10 + ( igm + 3 ) [ i \* ( nobranch + 1 ) + j ] ) , i = 0,…,
brnchdepl, j = 0,…, nobranch

Type: double precision

Data: (( ppf(i,j), i=1,nx), j=1,ny)

Data is saved for j = 1, ny (number of pins in y direction):

Data is saved for i = 1,nx (number of pins in x direction):

ppf(i,j) Pin power (peaking) factors

End of data saved for i = 1, nx

End of data saved for j = 1, ny

.. centered:: Block Type 11: group form factors

Length: datlen(13)

Position: 10 + k + ( igm + 3 ) [ i \* ( nobranch + 1 ) + j ] ) ,

k = 1,…, igm, i = 0,…, brnchdepl, j = 0,…, nobranch

Type: double precision

Data: (( gff(i,j), i=1,nx), j=1,ny)

Data is saved for j = 1,ny (number of pins in y direction):

Data is saved for j = 1, nx (number of pins in x direction):

gff(i,j,k) Groupwise form factors

End of data saved for i = 1, nx

End of data saved for j = 1, ny

NOTE: Block Type 11 is repeated igm times where igm is the number of
energy groups.

It is recommended that code written to process *xfile016* include the
SCALE subroutine library. Although possible to link in the appropriate
files in the scalelib object library in SCALE, it may be more practical
to copy the appropriate SCALE routines into a new FORTRAN code used in
reading *xfile016*. All direct-access operations needed to operate on
this file are contained in the file direct_access_M.f90 in the scale
src/scalelib directory. This file has dependencies and requires the
following additional subroutines, all in the ``src/scalelib`` directory, in
order to compile:

  Error_functions_M.f90

  common_unit_C.f90

  Vast_kind_param_M.f90

  separator_character_M.f90

  Y0trns_M.f90

  f_exit.c

The single C routine can be eliminated by eliminating the call to f_exit
in subroutine stop of Error_function.f90, e.g., change

.. highlight:: none

::

  if ( stopcode == 0 ) return
  write(npr,'(1x,a,i10)') 'stop code ',stopcode
  call f_exit(npr)

  end subroutine stop

to

::

  if ( stopcode == 0 ) return
  write(npr,'(1x,a,i10)') 'stop code ',stopcode
  write(standard_output,'(a)')npr
  stop

  end subroutine stop

Alternatively, one can utilize the module listed on the following pages,
developed by Mr. Benjamin Collins of the University of Michigan, which
includes all necessary coding wrapped into a single Fortran module.
Although developed from SCALE 5.1 routines, the format of SCALE direct
access does not change and this source should remain compatible with
later versions of SCALE.

.. highlight:: scale

::

  module direct_access
  !     Module taken from SCALE 5.1 source code and modified to eliminate
  !     dependencies to other scale modules
  !     Ben Collins, Doctoral Candidate, University of Michigan

       implicit none

        private
        integer,private,parameter::number_of_units=99
        integer,private:: nblks(number_of_units),lblks(number_of_units),char_word(number_of_units)
        integer,private :: record_length
        integer, parameter :: dp = selected_real_kind(14)
        integer,public :: next(3), nexsav(3), nda
        character(len=1) :: separator='/'
  ! ***change separator character to backslash (‘\’) for Windows***
  !      character(len=1) :: separator='\'
        public :: openda, xtenda, closda, inquir
        public :: reed
  !
  !
  !  set chpwrd to 1 now so that everything is specified in characters rather than
  !      in words when reading or writing character arrays
  !
        integer,public,parameter:: chpwrd=1
  !
      interface reed
        module procedure real_reed, integer_reed, dp_reed
      end interface

::

      contains
  !
        subroutine openda ( nblk,lblk,type,nrr,nunit,optional_name )
  !
        integer                   :: nblk,lblk,nrr,nunit
        real,dimension(lblk)      :: a
        character(len=1)          :: type
        character(len=*),optional :: optional_name
        character(len=16)         :: filnam
        character(len=512)        :: dsname
        character(10)             :: action
        logical                   :: lopen
        integer                   :: i, record_length
  !
        if ( nunit <= 0 .or. nunit >= 100 ) then
          stop 'da error - invalid unit number: program will terminate.'
        else
          inquire(unit=nunit,opened=lopen)
          if ( lopen ) then
            stop 'da error - unit already open: program will terminate.'
          end if
        end if

::

  !
        inquire(iolength=record_length) a
        write(filnam,'(a,i3.3,a8)') 'xfile',nunit,' '
        if ( present(optional_name) ) filnam = optional_name
        if ( type == 'o' .or. type == 'w' ) then
          call fulnam(filnam,dsname)
          select case (type)
          case('o')
            action = 'read'
          case('w')
            action = 'readwrite'
          end select
          open(unit=nunit,access='direct',status='old',action=action, &
               form='unformatted',recl=record_length,file=dsname)
          nblks(nunit) = 999999
          lblks(nunit) = lblk
          inquire(unit=nunit,opened=lopen)
          if (.not.lopen) then
            stop 'da error - unable to open unit: program will terminate.'
          end if
        else
          nblks(nunit) = nblk
          lblks(nunit) = lblk
          open(unit=nunit,access='direct',status='replace', &
          form='unformatted',recl=record_length,file=filnam)
          inquire(unit=nunit,opened=lopen)
          if (.not.lopen) then
            stop 'da error - unable to open unit: program will terminate.'
          end if
        end if
        char_word(nunit) = record_length/lblk

        end subroutine openda

::

  !

        subroutine closda ( nunit )
  !
        integer:: nunit
        logical:: lopen
  !
        inquire(unit=nunit,opened=lopen)
        if (lopen) close(unit=nunit)
        nblks(nunit) = 0
        lblks(nunit) = 0

        end subroutine closda

  !

        subroutine real_reed ( x,lword,nunit,nrec )
  !
        integer::lword,nunit,nrec
        real,dimension(lword)::x
        integer::lb,nb,nr,no,i,nl,j
  !
        call check_unit(nunit, lword)
        lb     = lblks(nunit)
        nb     = (lword+lb-1)/lb
        nr     = nrec
        no     = 1
        do i=1,nb
          if ( nr <= 0 .or. nr > nblks(nunit) ) then
            call print_rel_blk ( nunit, nr )
          end if
          nl     = min(no+lb-1,lword)
          read (nunit,rec=nr) (x(j),j=no,nl)
          nr     = nr + 1
          no     = nl + 1
        end do

        end subroutine real_reed

::

  !

        subroutine integer_reed ( nnx,lword,nunit,nrec )
  !
        integer::lword,nunit,nrec
        integer,dimension(lword)::nnx
        integer::lb,nb,nr,no,i,nl,j
  !
        call check_unit(nunit, lword)
        lb     = lblks(nunit)
        nb     = (lword+lb-1)/lb
        nr     = nrec
        no     = 1
        do i=1,nb
          if ( nr <= 0 .or. nr > nblks(nunit) ) then
            call print_rel_blk ( nunit, nr )
          end if
          nl     = min(no+lb-1,lword)
          read (nunit,rec=nr) (nnx(j),j=no,nl)
          nr     = nr + 1
          no     = nl + 1
        end do

        end subroutine integer_reed

::

  !

        subroutine dp_reed ( x,lword,nunit,nrec )
  !
        integer::lword,nunit,nrec
        real(dp),dimension(:)::x
        integer::lb,nb,nr,no,i,nl,j,lwrd
  !
        lwrd   = ubound(x,1)
        call check_unit(nunit, lwrd)
        lb     = lblks(nunit)/2
        nb     = (lwrd+lb-1)/lb
        nr     = nrec
        no     = 1
        do i=1,nb
          if ( nr <= 0 .or. nr > nblks(nunit) ) then
            call print_rel_blk ( nunit, nr )
          end if
          nl     = min(no+lb-1,lwrd)
          read (nunit,rec=nr) (x(j),j=no,nl)
          nr     = nr + 1
          no     = nl + 1
        end do

        end subroutine dp_reed

::

  !

        subroutine inquir ( nunit,nrec )
  !
        integer::nunit,nrec
  !
        inquire(unit=nunit,nextrec=nrec)

        end subroutine inquir

  !

        subroutine xtenda ( mblk,nunit )
           integer::mblk,nunit
           integer::lblk
           lblk = lblks(nunit)
           nblks(nunit) = nblks(nunit) + mblk
        end subroutine xtenda

  !

        subroutine check_unit(nunit, lword)

        integer :: nunit, lword
        logical :: lopen
        character(len=10)::access
  !
        inquire(unit=nunit,opened=lopen,access=access)
        if (.not.lopen) then
          stop 'da error - unit not open: program will terminate.'
        else
          if ( lword <= 0 ) then
            stop 'da error - invalid block length: program will terminate.'
          end if
        end if

        end subroutine check_unit

::

  !

        subroutine print_rel_blk ( unit, block )

        integer :: unit, block
        stop 'da error - relative block not in data set: program will terminate.'

        end subroutine print_rel_blk

  	  subroutine fulnam ( filnam, name )

  !   routine to convert a simple file name to a full path

        character(len=*)   :: filnam
        character(len=512) :: data_path
        character(len=4)   :: data='DATA'
        character(len=512) :: current_path
        character(len=6)   :: curdir='PWD'
        character(len=16)  :: short_name
        character(len=512) :: name, data_path_name, current_path_name, full_path_name
        logical            :: exists, found
        integer            :: n99=99, iostat

  !   check if filnam already has path
        if (index(filnam(1:3),separator) > 0 ) then
           name = filnam
           return
        end if
  !   get the scale data and tmpdir directory paths from environmental variables
        data_path          = ' '
        current_path       = ' '
        data_path_name     = filnam
        current_path_name  = filnam
        call getenv ( data, data_path )
        call getenv ( curdir, current_path )

::

  !   construct the full path name for the dataset name
        if (    data_path /= ' ' )     data_path_name = (trim(data_path))//separator//filnam
        if ( current_path /= ' ' ) current_path_name  = (trim(current_path))//separator//filnam

  !   if the dataset exists in the current directory (tmpdir), use it
  !   otherwise, look for it in the data directory
        inquire (file=filnam,exist=exists)
        if ( exists ) then
              name = current_path_name
        else
  !   check names constructed in script
           inquire (file='data_directory',exist=exists)
           found = .false.
           if ( exists ) then
              open(n99,status='old',form='formatted',file='data_directory')
              rewind n99
              do
                 read (n99,*,iostat=iostat) short_name, full_path_name
                 if ( iostat /= 0 ) exit
                 if ( short_name == filnam ) then
                    name  = full_path_name
                    found = .true.
                 end if
              end do
           end if
           close (n99)
           if ( found ) return
           inquire (file=data_path_name,exist=exists)
           if ( exists ) then
              name = data_path_name
           else
              name = current_path_name
           end if
        end if

        end subroutine fulnam

        end module direct_access

.. _3-1c:

The Flexible Branch Block
-------------------------

In support of various projects, the “flexible branch block” was
developed to enable a broader set of perturbations than are available in
the typical TRITON branch capability. The typical branch block allows
the user to define a single set of mixtures for 'fuel,' 'mod,' 'crout',
or 'crin'. Having only four material set definitions limits user’s
ability to specify more complex perturbations that may be possible in
some reactors, especially under transient conditions. The flexible
branch block was developed such that the user can specify any number of
material sets, and then apply separate perturbations to those sets. This
capability, for example, enables specification of bypass flow density
branches in BWRs in which the in-channel coolant and out-channel
moderator can set to different densities in the same branch calculation.

The flexible branch block was developed in the SCALE 6.1 implementation
of TRITON and was not modernized for SCALE 6.2. As a result, the
flexible branch block is available in SCALE 6.1 and in the legacy mode
in SCALE 6.2. The legacy mode can be accessed using *t-d* as the
sequence name, rather than the more typical *t-depl*. The flexible
branch block can be accessed using **branchblock** as the block name,
rather than **branch** that is used for the typical branch block.

The following section of the manual explains the syntax of the
**branchblock** and contains short examples of each element within the
the **branchblock**. At the end of this section, a full example of a
**branchblock** is provided so that users can gain an understanding of
how to use all of the parts of the **branchblock** in order to define
needed calculation branches.

SYNTAX:

.. highlight:: scale

::

  read branchblock
    [block keyword specifications]
  end branchblock

The advanced **branchblock** supports five different keyword
specifications described below.

-  **mixset** – used to define a set of mixtures which can be used in
   **swap** and **perturbset** definition,

-  **systemchange** – used to define a system change to, temperatures,
   nuclide concentrations, and Dancoff factors,

-  **swap** - used to define a set of mixtures to swap,

-  **perturbset** – used to define a set of perturbations which apply
   the system changes defined by **systemchange** to a set of mixtures,
   and

-  **branch** – used to define a branch calculation, composed of various
   **swaps** and **perturbsets**. Additional perturbations may also be
   defined.

.. note:: Several keywords in the*\ **branchblock**\ *are defined using
  strings. These strings must be must be delimited, i.e. starts and ends
  with an identifying marker. (Examples: ``title=”cold”``, ``title=#hot``
  ``Doppler#``, ``title=!40%void!``, ``title=(80%void)``). As shown in the following
  examples, the string can optionally start with open angle bracket < and
  end with a closing angle bracket > (Example: ``title=<cold>``). All
  string-value inputs in the*\ **branchblock**\ *are delimited,
  alphanumeric strings with a maximum length of 80 characters. It is
  recommended that users choose a single type of delimiter, and then use
  that delimiter throughout the **branchblock**\

.. centered:: systemchange

SYNTAX:

::

  read branchblock
    [...]
    systemchange title
      [systemchange keyword specifications]
    end systemchange
    [...]
  end branchblock

**systemchange** supports the following keyword specifications:

::

  title
  dancoff=(real value)
  temperature=(real value)
  dendiv N1 f1 N2 f2 end
  denmult N1 f1 N2 f2 end

**title** is required string input and must follow **systemchange**.
Only one title keyword may be specified. Multiple **systemchange**
specifications are allowed, so each specification must have a unique
**title**.

**dancoff** is optional and is used to set a dancoff factor value in the
interval [0,1]. Only one dancoff specification is allowed and can appear
anywhere in the **systemchange** specification following the title.

**temperature** is optional and is used to set a system temperature in
Kelvin. It must be nonnegative. Only one temperature specification is
allowed and can appear anywhere in the **systemchange** specification
following the title.

**dendiv** and **denmult** are keyword arrays used to define nuclide
concentration dividers and multipliers respectively. The arrays must be
terminated with the **end** keyword. Each array is defined by a series
of nuclide/factor pairs where nuclide is the ZZZAAA identifier and
factor is either a multiply or divide factor applied to that nuclide
concentration (Note that the particular mixture for which the factor is
applied is defined in the **perturb** specification described below).
Multiply factors must be >=0. Divide factors must be >0. A nuclide
identifier set to zero implies that the factor is applied to all
nuclides that are not explicitly listed in the array. Multiple dendiv
and denmult arrays are allowed and can appear anywhere in the
**systemchange** specification following the title. TRITON applies the
concentration factors in the order in which they are entered in the
systemchange specification.

Multiple **systemchange** specifications are allowed in the branch
block. They can appear in any order, but must have a unique title.

EXAMPLE:

Define a temperature change to 60 kelvin. (The temperature change will
be applied to a set of mixtures defined in the **perturbset**
specification defined later.)

::

  systemchange <60C>
    temperature=333.15
  end systemchange

.. centered:: swap

SYNTAX:

::

  read branchblock
    [...]
    swap title
      [swap keyword specifications]
    end swap
    [...]
  end branchblock

**swap** supports the following keyword specifications:

::

  title
  group1 [mixture specifications] end
  group2 [mixture specifications] end

**title** is required string and must follow **swap**. Only one title
keyword may be specified. Multiple **swap** specifications are allowed,
so each specification must have a unique **title**.

**group1** and **group2** are used to define a set of mixtures to
exchange. **group1** must follow the **swap** title. **group2** must
follow **group1**. Only one specification for each group is allowed and
they must have the same number of mixtures.

The **group1** and **group2** keywords support the following keyword
specifications:

::

  mixture=(integer value)
  mixtures I1 I2 ... IN end
  mixset=(string value)

**mixture** is used to define a single mixture. **mixtures** is used to
define an array of mixtures and is terminated with the **end** keyword.
**mixset** is used to substitute a **mixset** specification defined
elsewhere in the branchblock. Multiple **mixture**, **mixtures**, and
**mixset** are allowed and can be placed in any order. TRITON will
remove any duplicated mixture identifier, however each mixture must be
defined in the model input.

EXAMPLES:

Exchange material 1 for 4.

::

  swap <1 for 4>
    group1 mixture=1 end
    group2 mixtures 4 end end
  end swap

Exchange a set of mixtures:

::

  swap <RodInsertion>
    group1 mixset=<crout> end
    group2 mixset=<crin> end
  end swap

.. centered:: branch

SYNTAX:

::

  read branchblock
    [...]
    branch title
      [branch keyword specifications]
    end branch
    [...]
  end branchblock

**branch** supports the following keyword specifications.

::

  title
  swap=(string value)
  perturbset=(string value)
  perturb [perturb specification] end

**title** is required string and must follow **branch**. Only one title
keyword may be specified. Multiple **branch** specifications are
allowed, so each specification must have a unique **title**.

**swap** is used to swap different sets of mixtures. The swap value is a
string which is the title of a **swap** specification defined elsewhere
in the branchblock. (The **swap** specification is described below).
Multiple **swap** specifications are allowed and can appear anywhere in
the **branch** specification following the title.

**perturbset** is used to apply a series of system perturbations. The
perturbset value is a string which is the title of a **perturbset**
specification defined elsewhere in the branchblock. (The **perturbset**
specification is described below). Multiple **perturbset**
specifications are allowed and can appear anywhere in the **branch**
specification following the title.

**perturb** is used to apply a system perturbation that is not defined
through the use of a **perturbset** specification. **perturb**
specifications must terminate with the **end** keyword.

**perturb** supports the following keyword specifications.

::

  change=(string value)
  mixture=(integer value)
  mixtures I1 I2 ... IN end
  mixset=(string value)

**change** is a string which is the title of a **systemchange**
specification defined elsewhere in the branchblock. Only one **change**
specification is allowed and may appear anywhere in the **perturb**
specification.

The system change is applied to a set of mixtures defined by the
**mixture**, **mixtures**, and **mixset** specifications. Only one of
each of these keywords is allowed (however all three may be used in the
same **perturb** specification). **mixture**, **mixtures**, and
**mixset** may be placed in any order. TRITON will remove any duplicated
mixture, however each mixture must be defined in the model input. TRITON
will perform **swap** and **perturb** operations in the order they
appear in the input.

EXAMPLES:

Define a branch to charactize the rodded, cold-zero-power condition.
This requires the use of mixture swap entitled <CRodIn> along with the
perturbset definition <ColdMod> which perturbs all of the moderator
mixtures to a cold temperature and density. The fuel mixtures (defined
as <FuelMix>) must also be set to a temperature of 300K.

::

  read branchblock
    [...]  (contains definitions for <CRodIn>, <FuelMix>, and <ColdMod>)
    branch <CZP,rodded>
      perturbset=<ColdMod> swap=<CRodIn>
      perturb change=<300K> mixset=<FuelMix> end
    end branch
    systemchange <300K> temperature=300 end systemchange
  end branchblock

Define a branch to characterize the BWR instantaneous 100% void branch.
This requires that:

-  in-channel moderator mixtures (<ChannelMod>) are perturbed from 40%
   void to 100% void (defined by systemchange <40vf-100vf>).

-  Water-rod moderator mixtures (<WaterRodMod>) are perturbed from 0%
   void to 5% void (<0vf-5vf>)

-  Bypass moderator mixtures (<BypassMod>) are perturbed from 0% void to
   3% void (<0vf-3vf>)

-  Corner Rod Fuel mixture (mixture 1) dancoff factor changes (described
   by <100vf-cornerDF>)

-  Edge Fuel Rod Mixtures (3,4,5,6,7,10) dancoff factor changes
   (described by <100vf-edgeDF>)

::

  read branchblock
    [...]   (contains all other definitions)
    branch <100VF>
      perturb change=<40vf-100vf> mixset=<ChannelMod>  end
      perturb change=<0vf-5vf>    mixset=<WaterRodMod> end
      perturb change=<0vf-3vf>    mixset=<BypassMod> end
      perturb mixture=1 change=<100vf-cornerDF> end
      perturb mixtures 3 4 5 6 7 10 end change=<100vf-edgeDF> end
    end branch
  end branchblock

.. centered:: mixset

**mixset** – used to define a set of mixtures used in **swap**,
**perturbset**, and **perturb** specifications.

SYNTAX:

::

  read branchblock
    [...]
    mixset title
      [mixset keyword specifications]
    end mixset
    [...]
  end branchblock

**mixset** supports the following keyword specifications:

::

  title
  mixture=(integer value)
  mixtures I1 I2 ... IN end
  mixset=(string value)

**title** is required string and must follow **mixset**. Only one title
keyword may be specified. Multiple **mixset** specifications are
allowed, so each specification must have a unique **title**.

**mixture** is used to define a single mixture. **mixtures** is used to
define an array of mixtures and is terminated with the **end** keyword.
**mixset** is used to substitute a **mixset** specification defined
elsewhere in the branchblock. Multiple **mixture**, **mixtures**, and
**mixset** are allowed and can be placed in any order. TRITON will
remove any duplicated mixture identifier, however each mixture must be
defined in the model input. If **mixset** is used to, the mixture set
must be *previously* defined in the branchblock.

EXAMPLE:

In previous example for 100% void fraction, define a mixture set to be
used for the edge rod dancoff factor perturbation.

::

  read branchblock
    [...]   !contains all other definitions
    branch <100VF>
      perturb change=<40vf-100vf> mixset=<ChannelMod>  end
      perturb change=<0vf-5vf>    mixset=<WaterRodMod> end
      perturb change=<0vf-3vf>    mixset=<BypassMod> end
      perturb mixture=1 change=<100vf-cornerDF> end
      perturb change=<100vf-edgeDF> mixset=<edge-fuel> end
    end branch
    mixset <edge-fuel>
      mixtures 3 4 5 6 7 10 end
    end mixset
  end branchblock

**perturbset** – used to define a set of system perturbations that can
be used in **branch** specifications.

SYNTAX:

::

  read branchblock
    [...]
    perturbset title
      [perturbset keyword specifications]
    end perturbset
    [...]
  end branchblock

**perturbset** supports the following keyword specifications:

::

  title
  perturb [perturb specification] end

**title** is required string and must follow **perturbset**. Only one
title keyword may be specified. Multiple **perturbset** specifications
are allowed, so each specification must have a unique **title**.

After title, multiple **perturb** specifications can be used to defined
a set of perturbations. The **perturbset** can then be used in
**branch** specifications to simplify the **branch** input. TRITON will
apply the perturbations in the order in which they appear in the
**perturbset** specification.

EXAMPLE:

In previous example for 100% void fraction, define a perturbset for the
moderator perturbations, and a separate perturbset for the fuel
perturbations.

::

  read branchblock
    [...]   !contains all other definitions
    perturbset <modChange>
      perturb change=<40vf-100vf> mixset=<ChannelMod>  end
      perturb change=<0vf-5vf>    mixset=<WaterRodMod> end
      perturb change=<0vf-3vf>    mixset=<BypassMod> end
    end perturbset
    branch <100VF> perturbset=<modChange> perturbset=<fuelChange>  end branch
    perturbset <fuelChange>
      perturb mixture=1 change=<100vf-cornerDF> end
      perturb change=<100vf-edgeDF> mixset=<edge-fuel> end
    end perturbset
    mixset <edge-fuel>
      mixtures 3 4 5 6 7 10 end
    end mixset
  end branchblock

**branchblock** **Full Example**

Because the **branchblock** input is so flexible, it may be difficult
for users to know where to begin. For that reason, we have provided a
sample **branchblock** that is typical to a BWR analysis. In this
example, the open and close parentheses are using instead of angle
brackets. In the example provided, the **branchblock** is separated into
### different sections: definition of **mixsets**, definition of
**systemchanges**, definition of **swaps**, definition of
**perturbsets** (which are composed of multiple **systemchanges**), and
definition of **branches**. This example may appear complicated, but in
essence, it is quite straightforward. First, all of the mixture IDs in
the problem are defined into logical **mixsets**. Then, other large
**mixsets** are composed of the individual **mixsets**. The first two
**systemchanges**, (1/nom) and (1/liq), are a very important items.
These **systemchanges** are density divisors that divide the number
densities of a specified moderator mixture by the nominal or liquid
density, making the resulting density 1.0. Then, **systemchanges** that
are density multipliers are specified as the actual density, which make
the **branchblock** much easier to read and understand. By using the
special density divisors, an almost identical **branchblock** can be use
for different nominal densities – only the density specified in (1/nom)
needs to be modified for a different nominal density.

Following the **systemchanges**, a number of **perturbsets** are defined
to make multiple perturbations to the collant or moderator density. For
example, the (00%Void353) **perturbset** shown below makes six changes:
(1) divide all coolant (in-channel) mixtures by the nominal density,
then (2) multiple all coolant mixtures by the specified density, (3)
divide all liquid water moderator (out-channel) features by the
saturated liquid density, then (4) multiple all liquid water features by
the specified density, and then, (5) and (6) change the Dancoff factors
to their appropriate values corresponding to the coolant and moderator
densities.

::

  perturbset (00%Void353)
   perturb mixset=(coolant)    change=(1/nom)             end
   perturb mixset=(coolant)    change=(00V-353)           end
   perturb mixset=(solidmod)   change=(1/liq)             end
   perturb mixset=(solidmod)   change=(00V-353)           end
   perturb mixset=(cornerfuel) change=(00VCold-dfCO)      end
   perturb mixset=(edgefuel)   change=(00VCold-dfEO)      end
  end perturbset

To end the file, all branch calculations are specified in a single block
using the previously defined **perturbsets**. Note that unlike the
typical **branch** block, the flexible **branchblock** does not need the
first branch to correspond to the nominal conditions. It is important to
note that in the *xfile016* and *txtfile16* files, the branch conditions
(moderator density, temperature, soluble boron, and CR state) will not
be listed correctly in the file header as they are for the typical
**branch** block. When using the **branchblock** input, TRITON no longer
knows the condition for any given branch, however, the branch order
specified in the input file is maintained in the *xfile016* and
*txtfile16* files.

Also note that in the example provided, no soluble boron changes have
been specified (as this is a BWR example). However, soluble poisons
(boron or other), are also fairly straightforward to specify using the
density divisors and density multipliers.

**BWR branchblock** **Example**

::

  read branchblock
    mixset (1f127E)      mixtures   701                  end   end mixset
    mixset (1f127C)      mixtures   702                  end   end mixset
    mixset (1f169C)      mixtures   703                  end   end mixset
    mixset (1f169E)      mixtures   704                  end   end mixset
    mixset (1f194)       mixtures   705                  end   end mixset
    mixset (1f194C)      mixtures   706                  end   end mixset
    mixset (1f194E)      mixtures   707                  end   end mixset
    mixset (1f279)       mixtures   708                  end   end mixset
    mixset (1f279E)      mixtures   709                  end   end mixset
    mixset (1f279gd40)   mixtures   710 711 712 713 714  end   end mixset

    mixset (gap)       mixtures   800 801 802 803 804 805 806 807 808 809 end   end mixset
    mixset (clad)      mixtures   825 826 827 828 829 830 831 832 833 834 end   end mixset
    mixset (coolant)   mixtures   850 851 852 853 854 855 856 857 858 859 end   end mixset

    mixset (mod1)       mixtures   1001                    end   end mixset
    mixset (can)        mixtures   1004                    end   end mixset
    mixset (cbpois)     mixtures   1002                    end   end mixset
    mixset (cbstru)     mixtures   1003                    end   end mixset
    mixset (cbclad)     mixtures   1005                    end   end mixset

    mixset (cbpoisout)  mixtures   1012                    end   end mixset
    mixset (cbstruout)  mixtures   1013                    end   end mixset
    mixset (cbcladout)  mixtures   1015                    end   end mixset

    mixset (allfuel)     mixsets  (1f127E)
                                  (1f127C)
                                  (1f169C)
                                  (1f169E)
                                  (1f194)
                                  (1f194C)
                                  (1f194E)
                                  (1f279)
                                  (1f279E)
                                  (1f279gd40)             end   end mixset

    mixset (cornerfuel)  mixsets  (1f127C)
                                  (1f169C)
                                  (1f194C)                end   end mixset

    mixset (edgefuel)    mixsets  (1f127E)
                                  (1f169E)
                                  (1f194E)
                                  (1f279E)                end   end mixset

::


  mixset (solidmod)    mixsets  (mod1) (cbpoisout) (cbstruout) (cbcladout)       end   end mixset
    mixset (crin)        mixsets  (cbpois) (cbstru) (cbclad)                       end   end mixset
    mixset (crout)       mixsets  (cbpoisout) (cbstruout) (cbcladout)              end   end mixset
    mixset (allmod)      mixsets  (coolant)  (solidmod)                            end   end mixset

    systemchange (1/nom)      dendiv 0 0.4573 end      end systemchange
    systemchange (1/liq)      dendiv 0 0.7373 end      end systemchange

    systemchange (00V)       denmult 0 0.7373 end      end systemchange
    systemchange (40V)       denmult 0 0.4573 end      end systemchange
    systemchange (70V)       denmult 0 0.2473 end      end systemchange
    systemchange (90V)       denmult 0 0.1073 end      end systemchange
    systemchange (100V)      denmult 0 0.0373 end      end systemchange
    systemchange (00V-293)   denmult 0 0.9982 end      end systemchange
    systemchange (00V-313)   denmult 0 0.9922 end      end systemchange
    systemchange (00V-333)   denmult 0 0.9837 end      end systemchange
    systemchange (00V-353)   denmult 0 0.9718 end      end systemchange

    systemchange (293.15K)   temperature= 293.15    end systemchange
    systemchange (313.15K)   temperature= 313.15    end systemchange
    systemchange (333.15K)   temperature= 333.15    end systemchange
    systemchange (353.15K)   temperature= 353.15    end systemchange
    systemchange (300.00K)   temperature= 300.00    end systemchange
    systemchange (500.00K)   temperature= 500.00    end systemchange
    systemchange (1500.00K)  temperature=1500.00    end systemchange
    systemchange (560.29K)   temperature= 560.29    end systemchange
    systemchange (948.45K)   temperature= 948.45    end systemchange

::

  ' 0% void, cold Dancoff Factors
    systemchange (00VCold-dfCO) dancoff=0.084       end systemchange
    systemchange (00VCold-dfEO) dancoff=0.125       end systemchange
  ' 0% void, Dancoff Factors
    systemchange (00V-dfCO)     dancoff=0.116       end systemchange
    systemchange (00V-dfEO)     dancoff=0.171       end systemchange
  ' 40% void, Dancoff Factors
    systemchange (40V-dfCO)     dancoff=0.180       end systemchange
    systemchange (40V-dfEO)     dancoff=0.256       end systemchange
  ' 70% void, Dancoff Factors
    systemchange (70V-dfCO)     dancoff=0.281       end systemchange
    systemchange (70V-dfEO)     dancoff=0.376       end systemchange
  ' 90% void, Dancoff Factors
    systemchange (90V-dfCO)     dancoff=0.421       end systemchange
    systemchange (90V-dfEO)     dancoff=0.524       end systemchange

    swap (cr)
      group1 mixset=(crout) end
      group2 mixset=(crin)  end
    end swap

    perturbset (00%Void293)
      perturb mixset=(coolant)    change=(1/nom)             end
      perturb mixset=(coolant)    change=(00V-293)           end
      perturb mixset=(solidmod)   change=(1/liq)             end
      perturb mixset=(solidmod)   change=(00V-293)           end
      perturb mixset=(cornerfuel) change=(00VCold-dfCO)      end
      perturb mixset=(edgefuel)   change=(00VCold-dfEO)      end
    end perturbset
    perturbset (00%Void313)
      perturb mixset=(coolant)    change=(1/nom)             end
      perturb mixset=(coolant)    change=(00V-313)           end
      perturb mixset=(solidmod)   change=(1/liq)             end
      perturb mixset=(solidmod)   change=(00V-313)           end
      perturb mixset=(cornerfuel) change=(00VCold-dfCO)      end
      perturb mixset=(edgefuel)   change=(00VCold-dfEO)      end
    end perturbset
    perturbset (00%Void333)
      perturb mixset=(coolant)    change=(1/nom)             end
      perturb mixset=(coolant)    change=(00V-333)           end
      perturb mixset=(solidmod)   change=(1/liq)             end
      perturb mixset=(solidmod)   change=(00V-333)           end
      perturb mixset=(cornerfuel) change=(00VCold-dfCO)      end
      perturb mixset=(edgefuel)   change=(00VCold-dfEO)      end
    end perturbset
    perturbset (00%Void353)
      perturb mixset=(coolant)    change=(1/nom)             end
      perturb mixset=(coolant)    change=(00V-353)           end
      perturb mixset=(solidmod)   change=(1/liq)             end
      perturb mixset=(solidmod)   change=(00V-353)           end
      perturb mixset=(cornerfuel) change=(00VCold-dfCO)      end
      perturb mixset=(edgefuel)   change=(00VCold-dfEO)      end
    end perturbset

::

  perturbset (00%Void)
    perturb mixset=(coolant)    change=(1/nom)             end
    perturb mixset=(coolant)    change=(00V)               end
    perturb mixset=(cornerfuel) change=(00V-dfCO)          end
    perturb mixset=(edgefuel)   change=(00V-dfEO)          end
  end perturbset
  perturbset (40%Void)
    perturb mixset=(coolant)    change=(1/nom)             end
    perturb mixset=(coolant)    change=(40V)               end
    perturb mixset=(cornerfuel) change=(40V-dfCO)          end
    perturb mixset=(edgefuel)   change=(40V-dfEO)          end
  end perturbset
  perturbset (70%Void)
    perturb mixset=(coolant)    change=(1/nom)             end
    perturb mixset=(coolant)    change=(70V)               end
    perturb mixset=(cornerfuel) change=(70V-dfCO)          end
    perturb mixset=(edgefuel)   change=(70V-dfEO)          end
  end perturbset
  perturbset (90%Void)
    perturb mixset=(coolant)    change=(1/nom)             end
    perturb mixset=(coolant)    change=(90V)               end
    perturb mixset=(cornerfuel) change=(90V-dfCO)          end
    perturb mixset=(edgefuel)   change=(90V-dfEO)          end
  end perturbset

  perturbset (Tf=293.15)
    perturb mixset=(allfuel)     change=(293.15K)           end
  end perturbset
  perturbset (Tf=313.15)
    perturb mixset=(allfuel)     change=(313.15K)           end
  end perturbset
  perturbset (Tf=333.15)
    perturb mixset=(allfuel)     change=(333.15K)           end
  end perturbset
  perturbset (Tf=353.15)
    perturb mixset=(allfuel)     change=(353.15K)           end
  end perturbset
  perturbset (Tf=948.45)
    perturb mixset=(allfuel)     change=(948.45K)           end
  end perturbset
  perturbset (Tf=500.00)
    perturb mixset=(allfuel)     change=(500.00K)           end
  end perturbset
  perturbset (Tf=1500.00)
    perturb mixset=(allfuel)     change=(1500.00K)          end
  end perturbset

  perturbset (Tm=293.15)
    perturb mixset=(allmod)     change=(293.15K)           end
  end perturbset
  perturbset (Tm=313.15)
    perturb mixset=(allmod)     change=(313.15K)           end
  end perturbset
  perturbset (Tm=333.15)
    perturb mixset=(allmod)     change=(333.15K)           end
  end perturbset
  perturbset (Tm=353.15)
    perturb mixset=(allmod)     change=(353.15K)           end
  end perturbset
  perturbset (Tm=560.29)
    perturb mixset=(allmod)     change=(560.29K)           end
  end perturbset

::

  '          Name                    Void Frac     Fuel Temp     Mod Temp            CR Pos
    branch  (branch  1) perturbsets (00%Void)      (Tf=948.45)   (Tm=560.29)   end             end branch
    branch  (branch  2) perturbsets (40%Void)      (Tf=948.45)   (Tm=560.29)   end             end branch
    branch  (branch  3) perturbsets (70%Void)      (Tf=948.45)   (Tm=560.29)   end             end branch
    branch  (branch  4) perturbsets (90%Void)      (Tf=948.45)   (Tm=560.29)   end             end branch
    branch  (branch  5) perturbsets (00%Void)      (Tf=948.45)   (Tm=560.29)   end  swap=(cr)  end branch
    branch  (branch  6) perturbsets (40%Void)      (Tf=948.45)   (Tm=560.29)   end  swap=(cr)  end branch
    branch  (branch  7) perturbsets (70%Void)      (Tf=948.45)   (Tm=560.29)   end  swap=(cr)  end branch
    branch  (branch  8) perturbsets (90%Void)      (Tf=948.45)   (Tm=560.29)   end  swap=(cr)  end branch
    branch  (branch  9) perturbsets (00%Void)      (Tf=500.00)   (Tm=560.29)   end             end branch
    branch  (branch 10) perturbsets (40%Void)      (Tf=500.00)   (Tm=560.29)   end             end branch
    branch  (branch 11) perturbsets (70%Void)      (Tf=500.00)   (Tm=560.29)   end             end branch
    branch  (branch 12) perturbsets (90%Void)      (Tf=500.00)   (Tm=560.29)   end             end branch
    branch  (branch 13) perturbsets (00%Void)      (Tf=1500.00)  (Tm=560.29)   end             end branch
    branch  (branch 14) perturbsets (40%Void)      (Tf=1500.00)  (Tm=560.29)   end             end branch
    branch  (branch 15) perturbsets (70%Void)      (Tf=1500.00)  (Tm=560.29)   end             end branch
    branch  (branch 16) perturbsets (90%Void)      (Tf=1500.00)  (Tm=560.29)   end             end branch
    branch  (branch 17) perturbsets (00%Void293)   (Tf=293.15)   (Tm=293.15)   end             end branch
    branch  (branch 18) perturbsets (00%Void313)   (Tf=313.15)   (Tm=313.15)   end             end branch
    branch  (branch 19) perturbsets (00%Void333)   (Tf=333.15)   (Tm=333.15)   end             end branch
    branch  (branch 20) perturbsets (00%Void353)   (Tf=353.15)   (Tm=353.15)   end             end branch
    branch  (branch 21) perturbsets (00%Void293)   (Tf=293.15)   (Tm=293.15)   end  swap=(cr)  end branch
    branch  (branch 22) perturbsets (00%Void313)   (Tf=313.15)   (Tm=313.15)   end  swap=(cr)  end branch
    branch  (branch 23) perturbsets (00%Void333)   (Tf=333.15)   (Tm=333.15)   end  swap=(cr)  end branch
    branch  (branch 24) perturbsets (00%Void353)   (Tf=353.15)   (Tm=353.15)   end  swap=(cr)  end branch
  end branchblock
