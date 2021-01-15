.. _9-1AB:


XSDRNPM	Appendices A and B
==========================

.. _9-1a:

XSDRNPM	APPENDIX A: Special XSDRNPM Files
-----------------------------------------

Three special files that can be optionally produced by XSDRNPM are
described in this appendix. (See Sect. 10.1.5 and the discussion of the
logical units in the 0$ array.) The files will be created with file
names of the form **ftNNfXXX.EXT** where **NN** is the 2 digit logical
unit number (from the 0$$ array), **XXX** is a 3 digit number which is
incremented by one starting with one to make the name unique, and
**EXT** is an extension identifying which type of file it is (**acf**
for activity file, **btf** for balance table file, and **idf** for input
and derived data file).

.. _9-1a-1:

Activity file
~~~~~~~~~~~~~

The data on the activity file depends on what input options are
specified. The data is in ASCII sets, which consist of a label record
followed by the record(s) of the activity. There will be at most **IAZ**
sets ordered as the 49$ and 50$ arrays. The first sets of data will be
the activities by interval (if the input parameter **IAI** was
specified). A set will be formatted as below.

**activity by interval for nuclide** *nnnnnnnn* **reaction type**
*rrrrrrrr*

**Activity(first interval)**

    **.**

    **.**

    **.**

    **.**

**Activity(last interval)**


The preceding set will be repeated **IAZ** times. Then sets giving the
activities by zone will be given. They will be formatted as below.

| **activity by zone for nuclide** *nnnnnnnn* **reaction** *rrrrrrrr*
| **Activity(first zone)**

    **.**

    **.**

    **.**

    **.**

**Activity(last zone)**


.. _9-1a-2:

Balance table file
~~~~~~~~~~~~~~~~~~

The contents of the balance table are defined in :numref:`tab9-1a-1` and
:numref:`tab9-1a-2`. The structure of the “balance table file” written
to **LBTF** is:

Record 1 **KEFF, SP**

   **KEFF** – k\ :sub:`effective` for problem

   **SP** – search parameter for case

Record 2 – Sets of ASCII data consisting of a label record followed by
data records.

  Record last

  A set of data is as follows (igp is the total number of groups plus
  one):

**fine(few) group summary for zone** *zzzzz* **set type**

**Set type data(group 1)**

**Set type data(group 2)**

    **.**

    **.**

    **.**

    **.**

**Set type data(group igp)**

The data for a set type will be written for each zone of the problem,
plus a system summary if there is more than one zone. After one set type
is finished, the next set type will be written. The order of the set
types is as follows:

**fixed source**

**fission source**

**absorption rate**

**total leakage**

**fission rate**

**flux**

**<n,2n> rate**

**buckling loss**

**right current**

**left current**

**right leakage**

**left leakage**

The fine group summary data will be written if **LBTF** is > 0. After
the fine group data is finished, the few group summary data will follow
if a weighting calculation is specified with a broad group collapse.

.. _9-1a-3:

Input and derived data file
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The contents of the input and derived data file (specified by **LIDF**)
is as follows:

Record 1 – **title** (80 characters)

Record 2 – **1$$ array** (label)

Record 3,4 – **data from 1$ array**

Record 5 – **2$$ array** (label)

Record 6 – **data from 2$ array**

Record 7 – **3$$ array** (label)

Record 8,9 – **data from 3$ array**

Record 10 – **4$$ array** (label)

Record 11 – **data from 4$ array**

Record 12 – **5*\* array** (label)

Record 13,14 – **data from the 5\* array**

Record 15 – **cross section parameters** (label)

Record 16 – **total groups, neutron groups, gamma groups, first thermal
group**

Record 17 – **nuclides on library** (label)

Records 17a – **list of nuclides on the cross section library**

Record 18 – **mixture numbers** (label)

Records 18a – **data from the 13$ array**

Record 19 – **component numbers** (label)

Records 19a – **data from the 14$ array**

Record 20 – **densities** (label)

Records 20a – **data from the 15\* array**

Record 21 – **cccc identifiers** (label)

Records 21a – **data from the 16$ array**

Record 22 – **neutron energy group boundaries** (label)

Records 22a –- **list of the energy boundaries for the neutron groups**

Record 23 – **neutron lethargy group boundaries** (label)

Records 23a – **list of the lethargy boundaries for the neutron groups**

Record 24 – **neutron weighted velocities** (label)

Record 24a – **list of the neutron average velocities**

Record 25 – **gamma energy group boundaries** (label)

Record 25a – **list of the energy boundaries for the gamma groups**

Record 26 – **gamma lethargy group boundaries** (label)

Records 26a – **list of the lethargy boundaries for the gamma groups**

Record 27 – **gamma weighted velocities** (label)

Records 27a – **list of the gamma velocities**

Record 28 – **broad group numbers** (label)

Records 28a – **list of the broad group numbers by fine group - 51$
array**

Record 29 – **group band** (label)

Records 29a – **group band numbers by fine group**

Record 30 – **calculation type** (label)

Records 30a – **calculation type by fine group**

Record 31 – **right albedo** (label)

Records 31a – **list of the right boundary albedos by group - 47\*
array**

Record 32 – **left albedo** (label)

Records 32a – **list of the left boundary albedos by group - 48\*
array**

Record 34 – **mixture by zone** (label)

Records 34a – **data from the 39$ array**

Record 35 – **order of scattering by zone** (label)

Records 35a – **data from the 40$ array**

Record 36 – **activity materials** (label)

Records 36a – **data from the 49$ array**

Record 37 – **activity reaction types** (label)

Records 37a – **data from the 50$ array**

Record 38 – **quadrature weights** (label)

Records 38a – **data from the 43\* array**

Record 39 – **quadrature cosines** (label)

Records 39a – **data from the 42\* array**

Record 40 – **weights x cosines** (label)

Records 40a – **product of quadrature weights times quadrature**

Record 41 – **reflected directions** (label)

Records 41a – **reflected direction index array**

Record 42 – **pl scattering constants** (label)

Records 42a – **constants for converting from discrete angles to
Legendre moments**

Record 43 – **interval boundaries** (label)

Records 43a – **data from the 35\* array**

Record 44 – **interval midpoints** (label)

Records 44a – **array containing the midpoints of each interval**

Record 45 – **zone by interval** (label)

Records 45a – **data from the 36$ array**

Record 46 – **interval boundary areas** (label)

Records 46a – **area of each interval boundary**

Record 47 – **interval volumes** (label)

Records 47a – **volume of each interval**

Record 48 – **interval density factors** (label)

Records 48a – **data from the 38\* array**

Record 49 – **zone width modifiers** (label)

Records 49a – **data from the 41\* array**

Record 50 – **source spectrum by interval** (label)

Records 50a – **data from the 30$ array**

.. _tab9-1a-1:
.. list-table:: Balance table definitions.
  :align: center
  :class: longtable
  :widths: 30

  * - **FS** = Fission Source\ :sub:`grp,zone` =  :math:`1 / \lambda \Sigma_{\text {i} \subset \text{zone}}\left[X_{i, \operatorname{grp}} \Sigma_{\operatorname{grp}^{\prime}}\left(v \Sigma_{\text {fgrp }^{\prime}, i} \varphi_{\text {grp }^{\prime}, \mathrm{i}}\right) V_{i}\right]`
  * - **XS** = Fixed Source\ :sub:`grp,zone` = :math:`\Sigma_{1 \subset \text{zone} \text{}}\left[Q_{\text {grp }, i} V_{i}+A_{i} \Sigma_{\mu m>0} B S_{i, \text { grp, } m} \mu_{m} w_{m}-A_{i+1} \Sigma_{\mu m<0} B S_{i, \text { grp }, m} \mu_{m} w_{m}\right]`
  * - **IS** = Inscatter\ :sub:`grp,zone` = :math:`\Sigma_{\text {i} \subset \text{zone}} \sum_{j \neq \operatorname{grp}}\left[\Sigma_{j \rightarrow \operatorname{grp}, i} \varphi_{j, i} V_{i}\right]`
  * - **SS** = Selfscatter\ :sub:`grp,zone` =  :math:`\Sigma_{\text {i} \subset \text{zone}}\left[\Sigma_{\text {grp } \rightarrow \operatorname{grp}} \varphi_{\text {grp }, \mathrm{i}} \mathrm{V}_{\mathrm{i}}\right]`
  * - **OS** = Outscatter\ :sub:`grp,zone` =  :math:`\Sigma_{\text {i} \subset \text{zone}} \sum_{j \neq \operatorname{grp}}\left[\sum_{\operatorname{grp} \rightarrow j} \varphi_{\text {grp }, i} V_{i}\right]`
  * - **AB** = Absorption\ :sub:`grp,zone` =  :math:`\Sigma_{\text {i} \subset \text{zone}}\left[\Sigma_{\text {abs grp }, i} \varphi_{\text {grp }, \mathrm{i}} \mathrm{V}_{\mathrm{i}}\right]`
  * - **LK** = Leakage\ :sub:`grp,zone` = :math:`\left\lbrack A_{\text{zr}}\Sigma_{m}\left( \psi_{m,\mathrm{\mspace{6mu}}\text{zr}}\mu_{m}w_{m} \right)\mathrm{\quad} - \mathrm{\quad}A_{z1}\Sigma_{m}\left( \psi_{m,\mathrm{\mspace{6mu}}z1}\mu_{m}w_{m} \right) \right\rbrack`
  * - **RF** = Right Boundary Flux\ :sub:`grp,zone` = :math:`\Sigma_{\mathrm{m}}\left(\psi_{\mathrm{m}, \mathrm{zr}, \mathrm{grp}} \mathrm{W}_{\mathrm{m}}\right)`
  * - **LF** = Left Boundary Flux\ :sub:`grp,zone` = :math:`\Sigma_{\mathrm{m}}\left(\psi_{\mathrm{m}, \mathrm{zr}, \mathrm{grp}} \mathrm{W}_{\mathrm{m}}\right)`
  * - **RL** = Right Leakage\ :sub:`grp,zone` = :math:`\mathrm{A}_{\mathrm{zr}} \Sigma_{\mathrm{m}}\left(\psi_{\mathrm{m}, \mathrm{zr}, \mathrm{grp}} \mu_{\mathrm{m}} \mathrm{W}_{\mathrm{m}}\right)`
  * - **LL** = Left Leakage\ :sub:`grp,zone` = :math:`A_{z l} \Sigma_{m}\left(\psi_{m, z l, g r p} \mu_{m} W_{m}\right)`
  * - **NN** = n,2n Rate\ :sub:`grp,zone` = :math:`\Sigma_{i \subset \text { zone }} \Sigma_{p \geq 2}\left[p / 2 \Sigma_{n, p n} \varphi_{g r p, i} V_{i}\right]`
  * - **FR** = Fission Rate\ :sub:`grp,zone` = :math:`\sum_{i \subset \text { zone }}\left[\Sigma_{f g r p, i} \varphi_{g r p, i} V_{i}\right]`
  * - **DB** = DB\ :sup:`2` Flux\ :sub:`grp,zone` = :math:`\sum_{i \subset zone}\left[D_{g r p, i} B_{g r p, i}^{2} \varphi_{g r p, i} V_{i}\right]`
  * - **TF** = Total Flux\ :sub:`grp,zone` = :math:`\sum_{i \subset z o n e}\left[\varphi_{g r p, i} V_{i}\right]`
  * - **BAL = {FS+XS+IS+NN+max(LL,0)-min(RL,0)} / {OS+AB+max(RL,0)-min(LL,0)}**

.. _tab9-1a-2:
.. list-table:: Balance table definition symbols.
  :align: center
  :class: longtable
  :width: 30

  * - :math:`\sum_{\mathrm{i} \subset \mathrm{zone}}` is the sum over all intervals i in the zone
  * - :math:`\sum_{\mathrm{grp}}` is the sum over all groups grp
  * - :math:`\sum_{j \neq g r p}` is the sum over all groups j not equal to group grp
  * - :math:`\sum_{\mathrm{m}}` is the sum over the quadrature
  * - :math:`\sum_{\mathrm{p} \geq 2}` is the sum over all processes :math:`\sum_{\mathrm{n}, \mathrm{pn}}`
  * - :math:`\lambda \quad=\text { the eigenvalue }`
  * - :math:`\chi \quad=\text { the fission spectrum }`
  * - :math:`\mathbf{V}` = the average number of neutrons produced in a fission
  * - :math:`\sum_{\mathrm{f}}` = the fission cross section
  * - :math:`\varphi` =  the scalar flux
  * - V = the volume of a mesh interval
  * - Q = the volumetric external source in a mesh interval
  * - A = the area of a boundary of a mesh interval
  * - BS = the angular flux boundary source on an interval boundary
  * - :math:`\mu_{\mathrm{m}}` = the mth discrete angle of the quadrature
  * - :math:`\mathrm{W}_{\mathrm{m}}` =  the mth weight of the quadrature
  * - :math:`\sum_{j \rightarrow g r p}` =  the scattering cross section for scattering from group j to group grp
  * - :math:`\sum_{\mathrm{grp} \rightarrow \mathrm{j}}` =  the scattering cross section for scattering from group grp to group j
  * - :math:`\sum_{\operatorname{grp} \rightarrow \operatorname{grp}}` =  the scattering cross section for within-group scattering (i.e., from group grp to the same group grp)
  * - :math:`\sum_{\mathrm{abs}}` =  the absorption cross section
  * - :math:`\psi` =  the angular flux
  * - A\ :sub:`zr` = the area of the right-hand boundary of the zone
  * - A\ :sub:`zl` = the area of the left-hand boundary of the zone
  * - :math:`\sum_{\mathrm{n}, \mathrm{pn}}` =  the cross section for producing p neutrons, p=2,3,...,p an integer
  * - D = the diffusion coefficient (used in providing a buckling correction for 2 and 3 dimensions)
  * - B\ :sup:`2` = the buckling for the second and third dimensions (includes an extrapolation distance)
  * - **max(LL,0)** means that a positive Left Leakage is a source into the zone
  * - **min(RL,0)** means that a negative Right Leakage is a source into the zone. It is included with a minus sign to make it a positive source
  * - **max(RL,0)** means that a positive Right Leakage is a loss from the zone
  * - **min(LL,0)** means that a negative Left Leakage is a loss from the zone. It is included with a minus sign to make it a positive loss

.. _9-1b:

APPENDIX B: XSDRNPM Mixed Cross Sections
----------------------------------------

When **IPRT** (2$$ array) is set > −1, XSDRNPM prints the mixed reaction
rate cross sections that are used in its calculations. The order of the
cross sections for each group is given below in :numref:`tab9-1b-1`. The
diffusion coefficient is used in computing buckling corrections, and in
some of the options for computing the current used in weighting the
transport cross section. The upscatter cross section is used to checking
upscatter convergence. The <n,2n> cross section is used in computing the
balance for the balance tables. It is actually a weighted sum of all the
multiple neutron exit reactions other than fission. These are all
treated in XSDRNPM as scattering reactions. Chi is the fission spectrum,
and is used to distribute the fission source in energy space. The
fission cross section is used to compute the fission rate reported in
the balance tables. The absorption cross section is used to compute the
absorptions in the balance tables, and to compute the absorption term in
the eigenvalue. Nu*fission cross section is used to generate the source
term for all except a fixed source calculation. The total cross section
is used to determine the neutron transport.

.. _tab9-1b-1:
.. table:: Order of mixed reaction cross sections
  :align: center

  +------------------------------------------------------------+
  | 1. Diffusion coefficient (for use in buckling corrections) |
  +------------------------------------------------------------+
  | 2. Upscatter cross section                                 |
  +------------------------------------------------------------+
  | 3. <n,2n> cross section                                    |
  +------------------------------------------------------------+
  | 4. Chi (fission spectrun)                                  |
  +------------------------------------------------------------+
  | 5. Fission cross section                                   |
  +------------------------------------------------------------+
  | 6. Absorption cross section                                |
  +------------------------------------------------------------+
  | 7. Nu*Fission cross section                                |
  +------------------------------------------------------------+
  | 8. Total cross section                                     |
  +------------------------------------------------------------+







....
