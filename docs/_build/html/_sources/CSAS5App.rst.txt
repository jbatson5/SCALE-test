.. _CSAS5App:

Additional Example Applications of CSAS5
========================================

Several example uses of CSAS5 are shown in this section for a variety of
applications. Note that many of these examples have been provided since
the earliest versions of the CSAS sequences and output data shown may
not represent the most current version.

Typical search
--------------

EXAMPLE 1. CSAS5S — Determine the optimum pitch for an array of
Example 4 fuel assemblies

Consider a 4 × 4 × 1 array of fuel assemblies in a square aluminum cask.
Each assembly consists of a 17 × 17 × 1 array of zirconium-clad,
2.35%-enriched UO\ :sub:`2` fuel pins in a square pitched array. The
UO\ :sub:`2` has a density of 9.21 g/cc. The pin diameter is 0.8 cm and
is 366 cm long. The clad is 0.07 cm thick, and the pitch is 1.3 cm. Each
fuel bundle is contained in a 0.65-cm-thick Boral sheath. The bundles
are separated by an edge-to-edge spacing of 1 cm. The array of bundles
is centered in a 10-cm-thick aluminum cask whose inside dimensions are
0.5 cm beyond the outer edges of the fuel bundles. Search for the
assembly spacing that yields the maximum value of *k*\ :sub:`eff`. Because the
spacing between the assemblies is to be altered, the last region of
unit 2 will be altered. In order to do this, the fuel assembly shroud
cannot be defined as a replicate, because the code does not know the
size of the array until later. In order to perform a pitch or dimension
search, the code calculates the distance between the outermost region of
the unit and the region interior to it. Therefore, the fuel assembly gap
must be defined as a cuboid, and the water gap between assemblies can be
entered as either a cuboid or a replicate. This search has been defined
as an optimum dimension search. The input data for this problem follow.

.. highlight:: scale

::

  =CSAS5S
  SAMPLE FUEL CASK EXAMPLE
  V7-238
  READ COMP
  UO2 1 DEN=9.21 1.0 293.  92235 2.35 92238 97.65 END
  ZR 2 1 END
  H2O 3 1 END
  B4C 4 0.367 END
  AL 4 0.636 END
  AL 5 1 END
  END COMP
  READ CELLDATA
  LATTICECELL SQUAREPITCH PITCH=1.3 3 FUELD=0.8 1 CLADD=0.94 2 END
  END CELLDATA
  READ PARAM TME=6.0 NUB=YES FAR=YES GEN=103
  END PARAM
  READ GEOM UNIT 1 COM='FUEL PIN'
  CYLINDER 1 1 0.4 2P183.0 CYLINDER 2 1 0.47 2P183.07
  CUBOID 3 1 4P0.65 2P183.07
  UNIT 2
  COM='FUEL ASSEMBLY'
  ARRAY 1 2R-11.05 -183.07 CUBOID 4 1 4P11.7 2P183.72
  REPLICATE 3 1 6*0.5 1
  GLOBAL UNIT 3
  COM='FUEL CASK CONTAINING 4X4 ARRAY OF ASSEMBLIES'
  ARRAY 2 2R-48.8 -184.22
  REPLICATE 5 1 6R10.0 1
  END GEOM
  READ ARRAY ARA=1 NUX=17 NUY=17 NUZ=1 FILL F1 END FILL
  ARA=2 NUX=4 NUY=4 NUZ=1 FILL F2 END FILL
  END ARRAY
  END DATA
  READ SEARCH OPTIMUM DIMENSION MORE
  ALTER UNIT=2 REG=3 +X=1 -X=1 +Y=1 -Y=1
  +CON=0.204918      -CON= -0.0409836
  END SEARCH
  END

An alternative method of entering the search data for this problem is to
define the search as an optimum pitch search and require that the
spacing of the fuel pin cells remain unchanged. Because a pitch search
is always conducted at the lowest array level, in this case the spacing
between the pins in the fuel assembly (the outer region of unit 1), it
is necessary to countermand the automatic alteration of the outer region
of unit 1 by entering the KEEP command. Search constants must be entered
for the X and Y faces to instruct the code to KEEP those dimensions
unchanged. It is easier to use the keyword ALL, which applies the KEEP
command to all of the faces since the optimum pitch search would have
changed only the X and Y faces leaving the Z faces unchanged. The ALTER
command must then be entered to instruct the search to alter the spacing
between the fuel assemblies (region 3 of unit 2). Only the X and
Y dimensions are to be altered; so the search constants are entered
individually for those dimensions. It is acceptable to enter ALL=1 +Z=0
−Z=0 rather than +X=1 −X=1 +Y=1 −Y=1. It is not necessary to enter the
constraints for an optimum pitch search (+CON= and −CON=). They were
entered in this case to ensure that the alternative data more nearly
duplicate the optimum dimension search data from the previous example.
These alternative search data are:

::

  READ SEARCH OPTIMUM PITCH MORE
  KEEP UNIT=1 REG=3 ALL=1
  ALTER UNIT=2 REG=3 +X=1 −X=1 +Y=1 −Y=1 END SEARCH

Auxiliary search commands
-------------------------

Auxiliary search commands are entered ONLY if the word MORE was entered
in the search type specification data. These data are used to define the
method the search will use to alter the pitch, geometry or concentration
data and to set the constraints for the parameter search. The auxiliary
search commands consist of (1) INDIVIDUAL SEARCH COMMANDS and (2) SEARCH
PARAMETER CONSTRAINTS.

**EXAMPLE 1**

Consider an example in which region 2 of unit 1 is a cuboid and all of
the dimensions of the cuboid are to be altered. The search data could be
entered as:

::

   ALTER UNIT=1 REG=2 ALL=1.0

or

::

   ALTER UNIT=1 REG=2 +X=1.0 −X=1.0 +Y=1.0 −Y=1.0 +Z=1.0 −Z=1.0

Because all of the search constants are nonzero, all of the dimensions
will be changed. Because the search constants are identical, the
original relationship between the dimensions will be preserved as they
are altered.

For example, if region 2 of unit 1 is a cylinder and if all the
dimensions of the cylinder are to be altered, and if unit 1 is tied to
unit cell 1 the search data could be entered as:

::

   ALTER UNIT=1 REG=2 ALL=1.0 CELL=1

or

::

   ALTER UNIT=1 REG=2 RADIUS=1.0 +H=1.0 ?H=1.0 CELL=1

Because all of the search constants are nonzero, all of the dimensions
will be changed. Because the search constants are identical, the
original relationship between the dimensions will be preserved as they
are altered. If the original height-to-diameter ratio is 1.5, that ratio
will be preserved throughout the search only if the search constants for
the radius and + and − height are identical.

Search constants can be entered sequentially with each new entry
overriding only identical previous entries. For example, if region 2 of
unit 1 is a cuboid and if all of the dimensions except the −Z dimension
are to be altered, the search data could be entered as:

::

  ALTER UNIT=1 REG=2 +X=1.0 −X=1.0 +Y=1.0 −Y=1.0 +Z=1.0

or

::

  ALTER UNIT=1 REG=2 ALL=1.0 −Z=0.0

In the second example, all of the search constants corresponding to the
cuboid’s dimensions are set to 1.0 by using the ALL= command. This
includes the −Z dimension. To reset the search constant for the
−Z dimension to zero, −Z=0.0 is added following the ALL=1.0 command. If
the search commands are reversed, −Z=0.0 ALL=1.0, the −Z dimension will
also be altered because the −Z portion of the ALL= command will override
the previously entered −Z=0.0 command.

**EXAMPLE 2**

A search command must be entered for each unit and region specification.
Consider a problem having units 1, 2, and 3. Unit 1 consists of three
concentric spheres in a cuboid. Unit 2 consists of a single sphere in a
cuboid, and unit 3 contains three concentric cuboids. A search is to be
made that changes the inner sphere and outer cuboid of unit 1, and the
sphere and cuboid of unit 2, and the exterior cuboid of unit 3. The
thicknesses of the outer spheres of unit 1 are to be maintained, and the
two inner cuboids of unit 3 are to remain unchanged. The search data for
this problem can be entered as follows:

::

  ALTER UNIT=1 REG=1 ALL=1.0
  ALTER UNIT=1 REG=4 ALL=1.0 MAINTAIN UNIT=1 REG=2 TO 3 ALL=1.0 ALTER UNIT=2 REG=1 TO 2 ALL=1.0 ALTER UNIT=3 REG=3 ALL=1.0

Search constraints for dimension or pitch searches
--------------------------------------------------

SEARCH PARAMETER CONSTRAINTS set the parameter limits for the search.
The minimum constraint is the minimum value of the parameter allowed in
the search. The maximum constraint is the maximum value of the parameter
allowed in the search. The initial geometry configuration corresponds to
a parameter value of 0.0. A physical limit occurs when the value of the
parameter causes geometry intersections. Constraints should be entered
for a DIMENSION search. Only one set of constraints (i.e., min and max)
are allowed per problem. These constraints apply to all the dimensions
that are being altered.


For a DIMENSION search, the constraints are given by :eq:`CSASapp-1` and :eq:`CSASapp-2`

.. math::
  :label: CSASapp-1

  C_{min} = ((D_{min}/D_i) - 1.0)/SC ,

.. math::
  :label: CSASapp-2

  C_{max} = ((D_{min}/D_i) - 1.0)/SC ,

Where

   C\ :sub:`min` is the minimum constraint for the search

   C\ :sub:`max` is the maximum constraint for the search

   | D\ :sub:`min` is the minimum allowed dimension for the search [For
     a chord, D\ :sub:`min` = (Radius:sub:`min` +
   | Chord\ :sub:`min` )/ 2 Radius ] min

   | D\ :sub:`max` is the maximum allowed dimension for the search [For
     a chord, D\ :sub:`max` = (Radius:sub:`max` +
   | Chord\ :sub:`max` )/ 2 Radius\ :sub:`max`]

   D\ :sub:`i` is the initial dimension [For a chord, D\ :sub:`i` =
   (Radius:sub:`initial` + Chord\ :sub:`initial` )/2
   Radius\ :sub:`initial`]

   SC is the search constant for that dimension (i.e., +X, −X, RADIUS,
   etc.)

For example, the initial radius of a sphere is 6 cm, and a search is to
be conducted to determine the radius at which the sphere is critical.
The minimum radius the user wishes to allow is 3 cm, and the maximum
radius to be allowed is 9 cm. A nonzero search constant must be entered
to cause the radius to be changed. A search constant of 1.0, will be
used for the radius (RADIUS=1.0). The constraints calculated from :eq:`CSASapp-1`
and :eq:`CSASapp-2` are:


   C\ :sub:`min` = ((3.0/6.0)−1.0)/1.0 = −0.5

   C\ :sub:`max` = ((9.0/6.0)−1.0)/1.0 = 0.5

The constraints would be entered in the problem by entering the
following data:

::

  -CON=-0.5 +CON=0.5

For a PITCH search, the minimum constraint defines the limit for
shrinking the system, and the maximum constraint defines the limit for
expanding the system:

.. math::

  & \ \ \ \ \ \ \ \ \ \text{i = number of faces}

  & C_{min} - \text{MAX} \left[D_{+},D_{\_}\right] \text{for shrinking} \ ,

  & \ \ \ \ \ \ \ \ \ \text{i=1}


.. math::

  & \ \ \ \ \ \ \ \ \ \text{i = number of faces}

  & C_{max} - \text{MIN} \left[D_{+},D_{\_}\right] \text{for expanding} \ ,

  & \ \ \ \ \ \ \ \ \ \text{i=1}

where

   C\ :sub:`min` is the minimum constraint,

   C\ :sub:`max` is the maximum constraint,

   D\ :sub:`+` are face constraints for the positive dimensions,

   D\ :sub:`−` are face constraints for the negative dimensions.

Face constraints must be calculated for each face using :eq:`CSASapp-3`  and :eq:`CSASapp-4` :

.. math::
  :label: CSASapp-3

  D_{+} = \frac{(X_{d+} - X_{i+})(SC_{+} \times \text{del}_{+}\text{SC}_{\_} \times \text{del}_{\_})}{(X_{i+} - X_{i-})(\text{SC}_{+}\text{**}2 \times \text{del}_{\_})}

.. math::
  :label: CSASapp-4

  D_{\_} = \frac{(X_{d-} - X_{i-})(SC_{+} \times \text{del}_{+}\text{SC}_{\_} \times \text{del}_{\_})}{(X_{i+} - X_{i-})(\text{SC}_{+}\text{**}2 \times \text{del}_{\_})}

where

   X :sub:`d+` is the desired limit of the positive dimension of the
   spacing cuboid in that direction (positive dimension of X, Y, or Z,
   whichever dimension is under consideration)

   X\ :sub:`i+` is the initial positive dimension of the spacing cuboid
   in that direction (positive dimension of X, Y, or Z, whichever
   dimension is under consideration)

   X\ :sub:`d−` is the desired limit of the negative dimension of the
   spacing cuboid in that direction (negative dimension of X, Y, or Z,
   whichever dimension is under consideration)

   X\ :sub:`i−` is the initial negative dimension of the spacing cuboid
   in that direction (negative dimension of X, Y, or Z, whichever
   dimension is under consideration)

   SC\ :sub:`+` is the search constant for the positive dimension of the
   spacing cuboid in that direction (positive dimension of X, Y, or Z,
   whichever dimension is under consideration)

   SC\ :sub:`−` is the search constant for the negative dimension of the
   spacing cuboid in that direction (negative dimension of X, Y, or Z,
   whichever dimension is under consideration)

.. note::
   Using a search constant of 1.0 simplifies the determination
   of C\ :sub:`max` and C\ :sub:`min` when the dimensions are to change
   proportionately.

\

   del\ :sub:`+` is the initial distance from the spacing cuboid to the
   closest interior region in the positive direction (positive dimension of
   X, Y, or Z, whichever dimension is under consideration)

   del\ :sub:`−` is the initial distance from the spacing cuboid to the
   closest interior region in the negative direction (negative dimension of
   X, Y, or Z, whichever dimension is under consideration)

The search parameter constraints are entered using the following keywords:

−CON=pp is used to set the minimum constraint for the current parameter.
The value of pp is defaulted to −10E10 for a dimension search. The value
of pp is defaulted to a value that allows geometry regions to touch for
a pitch search unless a value was entered for MINPITCH, in which case
the parameter corresponding to that pitch is calculated and used.

+CON=rr is used to set the maximum constraint for the current parameter.
The value of rr is defaulted to +10E10 for a dimension search and to −5
× pp for a pitch search.

.. note::

   A search will reset a constraint (entered using the keyword
   +CON= or −CON=) that falls outside the default range to the default
   value. If a PITCH search is specified and if a value has been entered
   for MAXPITCH and/or MINPITCH, values should not be entered for the
   constraints. If values are entered for +CON= and/or −CON= for a PITCH
   search and if MAXPITCH and/or MINPITCH were specified in the optional
   search parameters, the maximum and minimum constraints will be set to
   the values corresponding to MAXPITCH and MINPITCH, even though the
   value of MINPITCH may result in an intersection.

Individual concentration search commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An INDIVIDUAL SEARCH COMMAND for a concentration search consists of
(1) a command definition, (2) the mixture number of the mixture to be
altered, (3) the name of the standard composition to be altered, (4) a
search constant, and (5) a unit cell containing the mixture. A series of
individual search commands can be entered to govern the search process.
A new search command is initiated whenever a command definition,
item (1) above, is encountered.

The COMMAND DEFINITION defines the action to be taken for the specified
mixture and standard composition component. ALTER, CHANGE, or MODIFY are
used to cause the concentration (number densities) of the specified
standard composition in the specified mixture to be modified.

ALTER CHANGE MODIFY
  The commands to the left are command definitions, item (1) above.  These commands instruct the code to modify the specified concentration data.



The MIXTURE NUMBER, item (2) above, defines the mixture that contains
the standard composition whose concentration is to be varied during the
search. The keyword **MIX=** is entered, followed by the mixture number,
nn.

MIX=nn
  is used to define the mixture number associated with the component that is to be changed.  The keyword MIX= is entered, followed by the mixture number, nn.  There is no default value of nn.

The STANDARD COMPOSITION NAME, item (3) above, defines the standard
composition whose concentration will be changed in the defined mixture.
Only standard compositions listed in the Standard Composition Library
chapter can be entered.

**SCNAME=**\ mm
  is used to specify the standard composition name of the
  component that is to be altered. The keyword SCNAME= is entered,
  followed by the mixture number, mm. There is no default value for mm.

.. note::
   If the standard composition component name specified in the
   Material Information Data (item 1 of the Standard Composition
   Specification Data) is a solution, for example, SOLNUO2(NO3)2, and
   the Concentration Search Data specifies SCNAME=UO2(NO3)2, the amount
   of UO2(NO3)2 in the solution will be altered, but the amount of water
   and nitric acid will not be changed. Thus, the resultant mixture may
   no longer meet the criteria associated with the SOLN specification.

The SEARCH CONSTANT for a concentration search, item (4) above, is a
proportional factor that applies to the standard composition being
altered. The keyword FACTOR= followed by a proportionality search
constant is used to specify the search constant for a concentration
search.

**FACTOR=**\ pc
  is used to specify the search constant. The keyword
  FACTOR= is entered, followed by the value of the search constant or
  proportionality factor, pc.

The UNIT CELL NUMBER, item (5) above, defines the unit cell containing
the mixture to be varied during the search. The keyword **CELL=** is
entered, followed by the unit cell number, mm.

**CELL=**\ mm
  is used to link mixture nn to unit cell mm. The keyword
  CELL= is entered, followed by the unit cell number, mm. The code
  defaults the cell number to the unit cell containing the mixture
  specified using MIX=.

ENTERING AUXILIARY SEARCH COMMANDS IN THE CONCENTRATION SEARCH DATA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

EXAMPLE 1

Consider an example in which the density of water is to be varied and is
contained in unit cell 2. Full density water, mixture 1, was specified
in the standard composition specification data as: H2O 1 END The
auxiliary search data could be entered as follows:

::

	ALTER  MIX=1  SCNAME=H2O  FACTOR=1.0 CELL=2

			or

	ALTER  MIX=1  SCNA=H2O    FAC=1.0    CE=2

			or

	ALTER  M=1    S=H2O       F=1.0      C=2

Note that terse input allows truncation of the keywords.

EXAMPLE 2

Consider an example in which the density of UO\ :sub:`2`\ F\ :sub:`2`,
is to be varied in mixture 2 contained in unit cell 4, a uranyl fluoride
solution. The uranyl fluoride solution was specified as:

::

  SOLNUO2F2   2   300   0   1   293   92235   5   92238   95   END

The auxiliary search data could be entered as follows:

::

	ALTER  MIX=2  SCNAME=UO2F2  FACTOR=1  CELL=4

		or

	ALTER  M=2    S=UO2F2       F=1       C=4

The terse input option allows truncation of the keywords.

Search constraints for concentration searches
---------------------------------------------

A SEARCH PARAMETER CONSTRAINT for concentration searches sets the
parameter limits for the search. The minimum constraint is the minimum
value of the parameter allowed in the search. The maximum constraint is
the maximum value of the parameter allowed in the search. The initial
concentration corresponds to a parameter value of 0.0. A physical limit
occurs when the value of the parameter causes the density of the
specified standard composition to become negative. The search can
produce an unrealistically high density. Users should manually eliminate
those results or set constraints to avoid them. Only one set of
constraints (i.e., min and max) are allowed per problem. These
constraints apply to all the standard compositions that are being
altered.

For a CONCENTRATION search, the constraints are given by :eq:`CSASApp-5` and :eq:`CSASApp-6`. The
maximum constraint must be larger than the minimum constraint.

.. math::
  :label: CSASApp-5

  C_{min} = \frac{((\frac{D_{min}}{D_{i}})-1)}{\text{FACTOR}},

.. math::
  :label: CSASApp-6

  C_{max} = \frac{((\frac{D_{max}}{D_{i}})-1)}{\text{FACTOR}},

where

   C\ :sub:`min` is the minimum constraint for the search,

   C\ :sub:`max` is the maximum constraint for the search,

   D\ :sub:`min` is the minimum allowed density for the specified
   standard composition,

   D\ :sub:`max` is the maximum allowed density for the specified
   standard composition,

   D\ :sub:`i` is the initial density of the specified standard
   composition,

   FACTOR is the search constant for the standard composition that is
   being varied.

Default search constraints are calculated if +CON and −CON are not
entered. The default concentration search constraints are calculated as
follows:

.. math::

  +\text{CON} =
  \begin{Bmatrix}
  \text{min}(\frac{1}{FACTOR}) , \text{if any FACTOR} < 0

  \text{-S} \times (\text{-CON}), \text{if all FACTOR} > 0
  \end{Bmatrix}

.. math::

  -\text{CON} =
  \begin{Bmatrix}
  \text{-S}(+\text{CON}) , \text{if all FACTOR} < 0

  \text{max}(\frac{-1}{FACTOR}), \text{if any FACTOR} > 0
  \end{Bmatrix}

Search considerations
---------------------

DIMENSION, PITCH, and CONCENTRATION searches can be performed using
CSAS5S. A DIMENSION search alters only those regions specified in the
search data. A PITCH search alters the center-to-center spacing of units
in an array and any other dimensions specified in the auxiliary data.
A CONCENTRATION search alters the density of the standard compositions
in the mixtures specified.

By default a pitch search is performed at the lowest array level and
changes the spacing in either the X dimension for a slab, the X and
Y dimensions for an array of cylinders, or the X, Y and Z dimensions for
an array of spheres. For example, if an array of fuel assemblies is
described in the geometry, the lowest array level is the array of fuel
pins comprising an assembly. Therefore, an optimum pitch search would
alter the spacing between the fuel pins within the assembly. The spacing
can be expanded until the array intersects the first region external to
it. The exterior size of the fuel pin array would grow or shrink within
the confines of the exterior region (fuel assembly shroud). If the
external regions are described using replicate regions, the array can
grow or shrink within the confines of the maximum and minimum
constraints.

If replicate regions are used outside an altered region or an array
whose spacing units are altered, the dimensions of the replicate regions
are recalculated (maintaining the thickness) at each search pass without
having to enter search data for those regions. However, geometry regions
specified by a geometry shape (sphere, cuboid, cylinder, etc.) that
exist outside an altered region or an array whose spacing units are
being altered will remain unchanged unless search data are provided for
them. In other words, REPLICATE regions will grow and shrink in response
to changes in the dimensions of the interior region, but other geometry
shapes will not.

Some of the limitations applicable to a pitch or dimension search are:

1. A pitch search is performed only at the lowest array level unless
search commands are entered to keep the lowest array level unit
unchanged and other commands are entered to cause other units to be
altered.

2. A pitch search alters the spacing in either the X dimension for a
slab, the X and Y dimensions for an array of cylinders, or the X Y and
Z dimensions for an array of spheres. Entering a search constant of zero
for +X, −X, +Y, −Y, +Z, and/or −Z will keep the corresponding dimension
from being altered.

3. A pitch search alters only the outer region of the unit(s) used in
the array at the lowest array level unless the search data specifying
otherwise is input.

4. A search cannot alter a region whose boundaries are set by the code
(i.e., an ARRAY, CORE BOUNDARY, or REPLICATE following an ARRAY). If the
dimensions of a replicate region are to be altered, the dimensions of
the region interior to it must be explicitly defined. For example, the
interior region can be a standard geometry shape (sphere, cylinder,
cuboid, etc.), but cannot be a replicate following an array or core
boundary.

5. All searches allow auxiliary search data.

Concentration searches can also be performed using CSAS5S. A
concentration search alters only those standard compositions specified
in the search data. Care must be taken when searching on standard
compositions beginning with SOLN, ATOM, WTPT, or ARBM (predecessor to
ATOM and WTPT in earlier SCALE versions). One or more of their
components can be altered but this will not directly affect the other
components. For example, if the standard composition component name
specified in the material information data is SOLN (SOLNUO2F2) and the
concentration search data specifies SCNAME=UO2F2, the amount of uranyl
fluoride salt, UO2F2, in the solution will be altered, but the amount of
water and hydrofluoric acid in the solution will remain unchanged.
Therefore, the resultant mixture may no longer meet the criteria for a
solution (SOLN) specification.

Physically, the concentration can vary from zero to some upper limit.
The code will prevent the concentration from falling below zero, but the
user is responsible for setting constraints that prevent the
concentration from exceeding reasonable values. The theoretical density
is a reasonable upper limit.

Optimum pitch search
--------------------

An optimum pitch search searches for the pitch that yields the highest
value of *k*\ :sub:`eff` An optimum pitch search is activated by entering
“OPTIMUM PITCH” in the search data. By default, the search is
performed at the lowest array level and only the spacing in the
X-direction for slabs, the X and
Y-directions for cylindrical arrays, and the X, Y, and Z-directions
for spherical arrays. The search constants are defaulted to 1.0 for
the applicable +X, −X, +Y, −Y, +Z, and −Z dimensions of the outermost
region. The dimensions of other geometry regions will not be changed
(their search constants are defaulted to 0.0) unless additional search
data containing appropriate instructions are supplied.

The limits for an optimum pitch search can be set using either the
MAXPITCH= and MINPITCH= options in the optional search parameters or the
+CON= and −CON= options in the search parameter constraints of the
auxiliary search commands. MAXPITCH= and MINPITCH= are used to enter a
value of the maximum allowed pitch and minimum allowed pitch
respectively. +CON= and −CON= are used to enter values for the parameter
constraints (i.e., the maximum and minimum allowed value of the search
parameter). Typically, it is easier to set the maximum allowed pitch and
minimum allowed pitch using MAXPITCH= and MINPITCH= than it is to
calculate the value of the parameter corresponding to those pitches. The
default minimum constraint corresponds to MINPITCH, the pitch at which
the largest interior region of a unit used in the array is in contact
with the spacing cuboid of that unit. The maximum constraint is
defaulted to −5 times the minimum constraint. In the first search pass,
the code calculates *k*\ :sub:`eff` for the initial problem geometry. The next
two passes calculate the *k*\ :sub:`eff` for the dimensions corresponding to
the minimum constraint and maximum constraint. Subsequent passes fit the
previous results to a cubic equation to select new dimensions.

Consider a 10 × 10 × 10 array of uranium spheres surrounded by water
having a “square” pitch. The uranium spheres are 2 cm in radius, and the
center-to-center spacing is 8 cm. The uranium spheres and their
associated spacing are defined to be unit 1, and the 10 × 10 × 10 array
is defined to be array 1. Search data and results for some optimum pitch
searches using this example are given in inputs 1 through 6 below.

Default Search — Array of Centered Spheres
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem contains search data for a default optimum pitch search.
The problem consists of a 10 × 10 × 10 array of uranium spheres
surrounded by low density water. The spheres are 90% \ :sup:`235`\ U and
10% \ :sup:`238`\ U and have a radius of 2.0 cm. The spheres are
originally centered on an 8.0 cm X, Y, and Z pitch with interstitial low
density (0.01 gm/cc) water. The problem searches for the pitch that will
produce the maximum *k*\ :sub:`eff` for the system.

::

  =CSAS5S
  10x10x10 ARRAY DEFAULT PITCH SEARCH
  V7-238
  READ COMP
  URANIUM 1 1.0  300.0 92235 90.0 92238 10.0 END
  H2O     2 0.01 300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SPHSQUAREP PITCH=8.0 2 FUELD=4.0 1 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  SPHERE  1 1 2.0
  CUBOID  2 1 6P4.0
  END GEOMETRY
  READ ARRAY
  ARA=1 NUX=10 NUY=10 NUZ=10 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  OPTIMUM PITCH  END SEARCH
  END

This data will cause the code to alter the +X, −X, +Y, −Y, +Z, and
−Z dimensions of the outer region of unit 1 and search for the
dimensions that give the maximum *k*\ :sub:`eff`. Because the next to last
outer dimension of the unit contained in the array are spheres, all six
dimensions are altered. The original relationship between the dimensions
is preserved (i.e., the original ratio of the X to Y to Z dimensions of
the cuboid is preserved throughout the search). Because this is an
optimum pitch search, the sphere dimensions will not be changed. For
this particular example, results for six passes are given. A final
search results for the problem follow:

::

  *******************   search pass  1     keff=  5.05769E-01 + or -  1.10681E-03    ******************
                                             the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  1.28382E+00 + or -  1.70155E-03   ******************
                                             the parameter was -5.00000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  2.58700E-01 + or -  8.16664E-04   ******************
                                             the parameter was  2.50000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  2.86712E-01 + or -  8.92672E-04   ******************
                                             the parameter was  1.25000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  5     keff=  2.66952E-01 + or -  8.42503E-04   ******************
                                             the parameter was  1.96018E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  6     keff=  2.63611E-01 + or -  7.74438E-04   ******************
                                             the parameter was  2.16471E+00
  1                                        10x10x10 array default pitch search
   ****************************************************************************************************
   ****************************************************************************************************
                    convergence was achieved on pass  2  the parameter was  -5.00000E-0
                                the equation used in the search was:

                   k-eff = +6.69365E-01 -7.39837E-01*p +4.33577E-01*p**2 -8.22064E-02*p**3

               k-effective=  1.28382E+00 + or -  1.70155E-03   the corresponding geometry follows;
           media bias      geometry description for those units utilized in this problem
   region   num  id
                                      -----   unit     1   -----
   1 sphere   1  1  radius = 2.0000   the center is located at (  0.0000 ,  0.0000 ,  0.0000 ).
   2 cuboid   2  1  +x = 2.0000  -x = -2.0000  +y = 2.0000  -y = -2.0000  +z = 2.0000  -z = -2.0000
   ****************************************************************************************************
   ****************************************************************************************************

Default Search — Array of Off-Centered Spheres
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the same problem as described above except the spheres are now
off-centered in the X and Y dimensions. The input data and the final
search results for this problem follow:

::

  =CSAS5S
  10x10x10 ARRAY DEFAULT PITCH SEARCH- OFFSET
  V7-238
  READ COMP
  URANIUM 1 1.0  300.0 92235 90.0 92238 10.0 END
  H2O     2 0.01 300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SPHSQUAREP PITCH=8.0 2 FUELD=4.0 1 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  SPHERE  1 1 2.0
  CUBOID  2 1 6.0 -2.0  3.0  -5.0  4.0  -4.0
  END GEOMETRY
  READ ARRAY
  ARA=1 NUX=10 NUY=10 NUZ=10 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  OPTIMUM PITCH  END SEARCH
  END

::

  *******************   search pass  1     keff=  5.06585E-01 + or -  1.12636E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  1.28382E+00 + or -  1.70155E-03   ******************
                                       the parameter was -5.00000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  2.58916E-01 + or -  8.16022E-04   ******************
                                        the parameter was  2.50000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  2.87506E-01 + or -  8.38203E-04   ******************
                                       the parameter was  1.25000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  5     keff=  2.67987E-01 + or -  8.48127E-04   ******************
                                       the parameter was  1.95962E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  6     keff=  2.64640E-01 + or -  7.99055E-04   ******************
                                       the parameter was  2.15903E+00
                               10x10x10 array default pitch search - offset
   ****************************************************************************************************
   ****************************************************************************************************
                     convergence was achieved on pass  2  the parameter was  -5.00000E-01
                                 the equation used in the search was:

                 k-eff = +6.69265E-01 -7.40343E-01*p +4.35409E-01*p**2 -8.28404E-02*p**3

            k-effective=  1.28382E+00 + or -  1.70155E-03   the corresponding geometry follows;       media bias      geometry description for those units utilized in this problem
   region  num  id
                                     -----   unit     1   -----
   1 sphere  1  1  radius = 2.0000    the center is located at ( 0.0000 ,  0.0000 ,  0.0000 ).
   2 cuboid  2  1  +x = 2.0000  -x = -2.0000  +y = 2.0000  -y = -2.0000  +z = 2.000   -z = -2.0000
   ****************************************************************************************************
   ****************************************************************************************************

Array of Centered Spheres — Constant :math:`Z` Spacing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the same problem as the first problem described above except the
array does not change in the Z dimensions. This is done by using MORE
and specifying a KEEP command. The input data and the final search
results for this problem follow:

::

  =CSAS5S
  10x10x10 ARRAY DEFAULT PITCH SEARCH - CHANGE IN X & Y ONLY
  V7-238
  READ COMP
  URANIUM 1 1.0  300.0 92235 90.0 92238 10.0 END
  H2O     2 0.01 300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SPHSQUAREP PITCH=8.0 2 FUELD=4.0 1 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  SPHERE  1 1 2.0
  CUBOID  2 1 6p4.0
  END GEOMETRY
  READ ARRAY
  ARA=1 NUX=10 NUY=10 NUZ=10 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  OPTIMUM PITCH  MORE
  KEEP UNIT=1  REG=2  +Z=1.0  -Z=1.0
  END SEARCH
  END

::

  *******************   search pass  1     keff=  5.05769E-01 + or -  1.10681E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  9.06304E-01 + or -  1.57239E-03   ******************
                                       the parameter was -5.00000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  2.82956E-01 + or -  8.20501E-04   ******************
                                       the parameter was  2.50000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  3.19086E-01 + or -  9.27655E-04   ******************
                                       the parameter was  1.25000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  5     keff=  2.94889E-01 + or -  8.49552E-04   ******************
                                       the parameter was  1.91631E+00
                          10x10x10 array default pitch search - change in x & y only
   ****************************************************************************************************
   ****************************************************************************************************
                   convergence was achieved on pass  2  the parameter was  -5.00000E-01
                                 the equation used in the search was:

                 k-eff = +5.70750E-01 -4.42912E-01*p +2.39464E-01*p**2 -4.35513E-02*p**3

             k-effective=  9.06304E-01 + or -  1.57239E-03   the corresponding geometry follows         media bias      geometry description for those units utilized in this problem
   region   num   id
                                         -----   unit     1   -----
   1 sphere  1  1  radius = 2.0000     the center is located at ( 0.0000 ,  0.0000 ,  0.0000 ).
   2 cuboid  2  1  +x = 2.0000  -x = -2.000   +y = 2.0000  -y = -2.0000  +z = 4.0000  -z = -4.0000
   ****************************************************************************************************
   ****************************************************************************************************

Default Search — Array of Centered Cylinders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem contains search data for a default optimum pitch search.
The problem consists of a 10 × 10 × 10 array of uranium cylinders
surrounded by low density water. The cylinders are 90% \ :sup:`235`\ U
and 10% :sup:`238`\ U and have a radius of 2.0 cm and a length of 20 cm.
The cylinders are originally centered on an 8.0 cm X and Y pitch and a
24 cm Z pitch with interstitial low density (0.01 gm/cc) water. The
problem searches for the pitch that will produce the maximum *k*\ :sub:`eff`
for the system. Because this is an array of cylinders, by default only
the X and Y dimensions are modified during the search. The input data
and the final search results for this problem follow:

::

  =CSAS5S
  10x10x10 ARRAY DEFAULT PITCH SEARCH - CHANGE IN X & Y ONLY
  V7-238
  READ COMP
  URANIUM 1 1.0  300.0 92235 90.0 92238 10.0 END
  H2O     2 0.01 300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SQUAREPITCH PITCH=8.0 2 FUELD=4.0 1 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  CYLINDER  1 1 2.0  10.0  -10.0
  CUBOID  2 1 4p4.0  2p12.0
  END GEOMETRY
  READ ARRAY
  ARA=1 NUX=10 NUY=10 NUZ=10 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  OPTIMUM  PITCH
  END SEARCH
  END

::

  *******************    search pass  1     keff=  1.09882E+00 + or -  1.75627E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  1.66591E+00 + or -  1.93770E-03   ******************
                                       the parameter was -5.00000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  5.08235E-01 + or -  1.28586E-03   ******************
                                       the parameter was  2.50000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  6.33884E-01 + or -  1.28582E-03   ******************
                                       the parameter was  1.25000E+00
                         10x10x10 array default pitch search - change in x & y only
   ****************************************************************************************************
   ****************************************************************************************************
                   convergence was achieved on pass  2  the parameter was  -5.00000E-01
                                   the equation used in the search was:

                k-eff = +1.09882E+00 -8.48276E-01*p +5.17313E-01*p**2 -1.08998E-01*p**3

            k-effective=  1.66591E+00 + or -  1.93770E-03   the corresponding geometry follows;
            media bias      geometry description for those units utilized in this problem
   regio     num  id
                                                        -----   unit     1   -----
   1 cylinder  1  1  radius = 2.0000  +z = 10.000  -z = -10.000  centerline is at  x = 0.000  y = 0.000
   2 cuboid    2  1  +x = 2.0000  -x = -2.0000  +y = 2.0000  -y = -2.0000  +z = 12.000  -z = -12.000
   ****************************************************************************************************
   ****************************************************************************************************

Array of Centered Cylinders — Search Extended to :math:`Z` Dimension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the same problem as given above except the search has been
extended to include the Z dimension. The input data causes the code to
alter the +X, −X, +Y, −Y, +Z, and −Z dimensions of the outer region of
unit 1 and search for the dimensions that give the maximum *k\ eff.* The
+Z and −Z search constants were chosen to maintain the same spacing
between cylinder surfaces in the X, Y and Z dimensions throughout the
search. Because this is an optimum pitch search, the cylinder dimensions
will not be changed. The input data and the final search results for
this problem follow:

::

  =CSAS5S
  10x10x10 ARRAY DEFAULT PITCH SEARCH - CHANGE IN X, Y, Z
  V7-238
  READ COMP
  URANIUM 1 1.0  300.0 92235 90.0 92238 10.0 END
  H2O     2 0.01 300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SQUAREPITCH PITCH=8.0 2 FUELD=4.0 1 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  CYLINDER  1 1 2.0  10.0  -10.0
  CUBOID  2 1 4p4.0  2p12.0
  END GEOMETRY
  READ ARRAY
  ARA=1 NUX=10 NUY=10 NUZ=10 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  OPTIMUM  PITCH  MORE
  ALTER  UNIT=1  REG=2  +Z=0.33333  -Z=0.33333
  END SEARCH
  END

::

  *******************   search pass  1     keff=  1.09882E+00 + or -  1.75627E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  1.77881E+00 + or -  1.79505E-03   ******************
                                       the parameter was -5.00000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  4.54894E-01 + or -  1.09005E-03   ******************
                                       the parameter was  2.50000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  5.70747E-01 + or -  1.32088E-03   ******************
                                       the parameter was  1.25000E+00
                            10x10x10 array default pitch search - change in x, y, z                    ****************************************************************************************************
   ****************************************************************************************************
                    convergence was achieved on pass  2  the parameter was  -5.00000E-01
                               the equation used in the search was:

                  k-eff = +1.09882E+00 -1.00799E+00*p +6.36691E-01*p**2 -1.34609E-01*p**3

            k-effective=  1.77881E+00 + or -  1.79505E-03   the corresponding geometry follows;
          media bias      geometry description for those units utilized in this problem
   region  num   id
                                       -----   unit     1   -----
   1 cylinder  1  1  radius = 2.0000  +z = 10.000  -z = -10.000  centerline is at  x = 0.000  y = 0.000
   2 cuboid    2  1  +x = 2.0000  -x = -2.0000  +y = 2.0000  -y = -2.0000  +z = 10.000  -z = -10.000
   ****************************************************************************************************
   ****************************************************************************************************

Minimum pitch search
--------------------

A minimum pitch search searches for the pitch that yields the lowest
value of *k\ eff.* A minimum pitch search is activated by entering
“MINIMUM PITCH” in the search data. By default, the search is performed
at the lowest array level and only the spacing in the X-direction for
slabs, the X and Y directions for cylindrical arrays, and the X, Y, and
Z directions for spherical arrays. The search constants are defaulted to
1.0 for the applicable +X, −X, +Y, −Y, +Z, and −Z dimensions of the
outermost region. The dimensions of other geometry regions will not be
changed (their search constants are defaulted to 0.0) unless additional
search data containing appropriate instructions are supplied.

The limits for a minimum pitch search are the same as an optimum pitch
search as described in the previous section.

Array of Centered Uranium Slabs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider a 10 × 1 × 1 array of uranium metal slabs. The uranium slabs
are 2 cm in thick in the X dimension and 200 cm thick in the Y and
Z dimensions. On each side of the uranium slab in the X dimension is
1 cm of H\ :sub:`2`\ O, then 1 cm of Boral, then 1 cm of H\ :sub:`2`\ O
resulting in an initial center-to-center spacing is 8.0 cm. The slabs
are 90% :sup:`235`\ U and 10% :sup:`238`\ U, the water is full density,
and the Boral is 36.7% B\ :sub:`4`\ C. The uranium slabs and their
associated materials are defined to be unit 1, and the 10 × 1 × 1 array
is defined to be array 1. A minimum pitch of 6.01 cm is specified,
MINPITCH=6.01, and a maximum pitch of 14.0 cm is specified,
MAXPITCH=14.0. The input data and the final search results for this
problem follow:

::

  =CSAS5S
  10x1x1 ARRAY DEFAULT PITCH SEARCH - SLAB
  V7-238
  READ COMP
  URANIUM 1 1.0   300.0 92235 90.0 92238 10.0 END
  H2O     2 1.0   300.0 END
  B4C     3 0.367 300.0 END
  Al      3 0.633 300.0 END
  H2O     4 1.0   300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SYMMSLABCELL PITCH=8.0 4 FUELD=2.0 1
                           CLADD=6.01 3 GAPD=4.0 2 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  CUBOID  1 1 1.0  -1.0  4P100.0
  CUBOID  2 1 2.0  -2.0  4p100.0
  CUBOID  3 1 3.0  -3.0  4P100.0
  CUBOID  4 1 4.0  -4.0  4P100.0
  END GEOMETRY
  READ ARRAY
  ARA=1 NUX=10 NUY=1 NUZ=1 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  MINIMUM  PITCH
  MINPITCH=6.0  MAXPITCH=14.0
  END SEARCH
  END

::

  *******************   search pass  1     keff=  1.13755E+00 + or -  1.50108E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  1.43116E+00 + or -  1.57018E-03   ******************
                                       the parameter was -2.50000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  8.04815E-01 + or -  1.47600E-03   ******************
                                       the parameter was  7.50000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  9.05346E-01 + or -  1.47107E-03   ******************
                                       the parameter was  3.75000E-01
                                   10x1x1 array default pitch search - slab
   ****************************************************************************************************
   ****************************************************************************************************
                    convergence was achieved on pass  3  the parameter was   7.50000E-01
                                 the equation used in the search was:

                   k-eff = +1.13755E+00 -9.12964E-01*p +9.40907E-01*p**2 -4.20205E-01*p**3

            k-effective=  8.04815E-01 + or -  1.47600E-03   the corresponding geometry follows;
           media bias      geometry description for those units utilized in this problem
   region   num   id
                                   -----   unit     1   -----
   1 cuboid    1  1   +x = 1.0000  -x = -1.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   2 cuboid    2  1   +x = 2.0000  -x = -2.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   3 cuboid    3  1   +x = 3.0000  -x = -3.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   4 cuboid    4  1   +x = 7.0000  -x = -7.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   ****************************************************************************************************
   ****************************************************************************************************

Critical pitch search
---------------------

A critical pitch search alters the outer region of the unit or units at
the lowest array level in search of a specified value of *k*\ :sub:`eff`. A
critical pitch search is activated by entering “CRITICAL PITCH” in the
search data. By default, the search is performed at the lowest array
level, and only the spacing in the X and Y directions (the X and
Y dimensions of the outermost region of the unit(s) used in the array at
the lowest array level) will be changed. The search constants are
defaulted to 1.0 for the +X, −X, +Y, and −Y dimensions of the region.
The dimensions of other geometry regions will not be changed (their
search constants are defaulted to 0.0) unless additional search data
containing appropriate instructions are supplied.

The limits for a critical pitch search can be set using either MAXPITCH=
and MINPITCH= in the optional search parameters or +CON= and −CON= in
the search parameter constraints of the auxiliary search commands.
MAXPITCH= and MINPITCH= are used to enter a value of the maximum allowed
pitch and minimum allowed pitch respectively. Parameters +CON= and −CON=
are used to enter values for the parameter constraints (i.e., the
maximum and minimum allowed value of the search parameter). Typically,
it is easier to set the maximum allowed pitch and minimum allowed pitch
using MAXPITCH= and MINPITCH= than it is to calculate the value of the
parameter corresponding to those pitches. The default minimum constraint
corresponds to MINPITCH, the pitch at which the largest interior region
of a unit used in the array is in contact with the spacing cuboid of
that unit. The maximum constraint is defaulted to −5 times the minimum
constraint. The code calculates *k*\ :sub:`eff` for the initial geometry first.
Then the dimensions corresponding to the minimum constraint and maximum
constraint are calculated.

Default Search — Array of Centered Spheres
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem contains search data for a default critical pitch search
with *k*\ :sub:`eff` specified to be 0.95. The problem consists of a
10 × 10 × 10 array of uranium spheres surrounded by low density water.
The spheres are 90% :sup:`235`\ U and 10% :sup:`238`\ U and have a
radius of 2.0 cm. The spheres are originally centered on an 8.0 cm X, Y,
and Z pitch with interstitial low density (0.01 gm/cc) water. The
problem searches for the pitch that will produce a *k*\ :sub:`eff` = 0.95 for
the system.

::

  =CSAS5S
  10x10x10 ARRAY DEFAULT PITCH SEARCH
  V7-238
  READ COMP
  URANIUM 1 1.0  300.0 92235 90.0 92238 10.0 END
  H2O     2 0.01 300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SPHSQUAREP PITCH=8.0 2 FUELD=4.0 1 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  SPHERE  1 1 2.0
  CUBOID  2 1 6P4.0
  END GEOMETRY
  READ ARRAY
  ARA=1 NUX=10 NUY=10 NUZ=10 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  CRITICAL  PITCH  KEF=0.95  END SEARCH
  END

::

  *******************   search pass  1     keff=  5.05769E-01 + or -  1.10681E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  2.58700E-01 + or -  8.16664E-04   ******************
                                       the parameter was  2.50000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  1.28382E+00 + or -  1.70155E-03   ******************
                                       the parameter was -5.00000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  8.08580E-01 + or -  1.54692E-03   ******************
                                       the parameter was -3.04076E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  5     keff=  9.37897E-01 + or -  1.63624E-03   ******************
                                       the parameter was -3.73908E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  6     keff=  9.49167E-01 + or -  1.64684E-03   ******************
                                       the parameter was -3.79251E-01
                                    10x10x10 array default pitch search
   ****************************************************************************************************
   ****************************************************************************************************
                 convergence was achieved on pass  6  the parameter was  -3.79251E-01
                                 the equation used in the search was:

                 k-eff = +5.33889E-01 -9.31824E-02*p +2.29294E+00*p**2 -9.20141E-01*p**3

               k-effective=  9.49167E-01 + or -  1.64684E-03   the corresponding geometry follows;
           media bias      geometry description for those units utilized in this problem
   region   num  id
                                        -----   unit     1   -----
   1 sphere   1  1  radius = 2.0000     the center is located at (  0.0000 ,  0.0000 ,  0.0000 ).
   2 cuboid   2  1  +x =  2.4830  -x = -2.4830  +y = 2.4830  -y = -2.4830  +z = 2.4830  -z = -2.4830
   ****************************************************************************************************
   ****************************************************************************************************
                                    10x10x10 array default pitch search
   ****************************************************************************************************
   ****************************************************************************************************
              based on the preceding data, the best estimate of the parameter is   -3.79602E-01

                            the geometry corresponding to this parameter follows:
          media bias      geometry description for those units utilized in this problem
   region  num  id
                                        -----   unit     1   -----
   1 sphere  1  1  radius = 2.0000     the center is located at (  0.0000 ,  0.0000 ,  0.0000 ).
   2 cuboid  2  1  +x = 2.4816  -x = -2.4816  +y = 2.4816  -y = -2.4816  +z = 2.4816  -z = -2.4816
   ****************************************************************************************************
   ****************************************************************************************************

Array of Centered Cylinders — Search Extended to :math:`Z` Dimension
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem contains search data for a default critical pitch search
with *k*\ :sub:`eff` specified to be 0.95. The problem consists of a
10 × 10 × 10 array of uranium cylinders surrounded by low density water.
The cylinders are 90% :sup:`235`\ U and 10% :sup:`238`\ U and have a
radius of 2.0 cm and a length of 20 cm. The cylinders are originally
centered on an 8.0 cm X and Y pitch and a 24 cm Z pitch with
interstitial low density (0.01 gm/cc) water. The problem searches for
the pitch that will produce a *k*\ :sub:`eff` = 0.95 for the system. Because
this is an array of cylinders, by default only the X and Y dimensions
are modified during the search. The +Z and −Z search constants were
included and chosen such that the same spacing is maintained between
cylinder surfaces in the X, Y and Z dimensions throughout the search.
The input data and the final search results for this problem follow:

::

  =CSAS5S
  10x10x10 ARRAY DEFAULT PITCH SEARCH - CHANGE IN X, Y, Z
  V7-238
  READ COMP
  URANIUM 1 1.0  300.0 92235 90.0 92238 10.0 END
  H2O     2 0.01 300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SQUAREPITCH PITCH=8.0 2 FUELD=4.0 1 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  CYLINDER  1 1 2.0  10.0  -10.0
  CUBOID  2 1 4p4.0  2p12.0
  END GEOMETRY
  READ ARRAY
  ARA=1 NUX=10 NUY=10 NUZ=10 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  CRITICAL  PITCH  KEFF=0.95  MORE
  ALTER  UNIT=1  REG=2  +Z=0.33333  -Z=0.33333
  END SEARCH
  END

::

  *******************   search pass  1     keff=  1.09882E+00 + or -  1.75627E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  1.77881E+00 + or -  1.79505E-03   ******************
                                       the parameter was -5.00000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  1.00616E+00 + or -  1.61956E-03   ******************
                                       the parameter was  1.09424E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  9.48455E-01 + or -  1.66901E-03   ******************
                                       the parameter was  1.91336E-01
                            10x10x10 array default pitch search - change in x, y, z
   ****************************************************************************************************
   ****************************************************************************************************
                    convergence was achieved on pass  4  the parameter was   1.91336E-01
                                 the equation used in the search was:

                  k-eff = +1.09882E+00 -9.31106E-01*p +7.86483E-01*p**2 -1.42575E-01*p**3

             k-effective=  9.48455E-01 + or -  1.66901E-03   the corresponding geometry follows;
            media bias      geometry description for those units utilized in this problem
   region    num  id
                                    -----   unit     1   -----
   1 cylinder  1  1  radius = 2.0000  +z = 10.000  -z = -10.000  centerline is at  x = 0.000  y = 0.000
   2 cuboid    2  1  +x = 4.7653  -x = -4.7653     +y = 4.7653  -y = -4.7653  +z = 12.765  -z = -12.765
   ****************************************************************************************************
   ****************************************************************************************************
                              10x10x10 array default pitch search - change in x, y, z
   ****************************************************************************************************
   ****************************************************************************************************0
  based on the preceding data, the best estimate of the parameter is    1.88950E-01

                                 the geometry corresponding to this parameter follows:
           media bias      geometry description for those units utilized in this problem
   region    num  id
                                                        -----   unit     1   -----
   1 cylinder  1  1  radius = 2.0000  +z = 10.000  -z = -10.000  centerline is at  x = 0.000  y = 0.000
   2 cuboid    2  1  +x =  4.7558  -x = -4.7558  +y =  4.7558  -y = -4.7558  +z =  12.756  -z = -12.756
   ****************************************************************************************************
   ****************************************************************************************************

Array of Centered Uranium Slabs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider a 10 × 1 × 1 array of uranium metal slabs. The uranium slabs
are 2 cm thick in the X dimension and 200 cm thick in the Y and
Z dimensions. On each side of the uranium slab in the X dimension is
1 cm of H\ :sub:`2`\ O, then 1 cm of Boral, then 1 cm of H\ :sub:`2`\ O
resulting in an initial center-to-center spacing of 8.0 cm. The slabs
are 90% :sup:`235`\ U and 10% :sup:`238`\ U, the water is full density,
and the Boral is 36.7% B\ :sub:`4`\ C. The uranium slabs and their
associated materials are defined to be unit 1, and the 10 × 1 × 1 array
is defined to be array 1. A minimum pitch of 6.0 cm is specified,
MINPITCH=6.0, and a maximum pitch of 14.0 cm is specified,
MAXPITCH=14.0. The code searches for the default value of *k*\ :sub:`eff`. The
input data and the final search results for this problem follow:

::

  =CSAS5S
  10x1x1 ARRAY DEFAULT PITCH SEARCH - SLAB
  V7-238
  READ COMP
  URANIUM 1 1.0   300.0 92235 90.0 92238 10.0 END
  H2O     2 1.0   300.0 END
  B4C     3 0.367 300.0 END
  Al      3 0.633 300.0 END
  H2O     4 1.0   300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SYMMSLABCELL PITCH=8.0 4 FUELD=2.0 1
                           CLADD=6.0 3 GAPD=4.0 2 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  CUBOID  1 1 1.0  -1.0  4P100.0
  CUBOID  2 1 2.0  -2.0  4p100.0
  CUBOID  3 1 3.0  -3.0  4P100.0
  CUBOID  4 1 4.0  -4.0  4P100.0
  END GEOMETRY
  READ ARRAY
  ARA=1 GBL=1 NUX=10 NUY=1 NUZ=1 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  CRITICAL  PITCH
  MINPITCH=6.0  MAXPITCH=14.0
  END SEARCH
  END

::

  *******************   search pass  1     keff=  1.13755E+00 + or -  1.50108E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  1.43116E+00 + or -  1.57018E-03   ******************
                                       the parameter was -2.50000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  1.04384E+00 + or -  1.47394E-03   ******************
                                       the parameter was  1.17120E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  9.97707E-01 + or -  1.60798E-03   ******************
                                       the parameter was  1.89330E-01
                                10x1x1 array default pitch search - slab
   ****************************************************************************************************
   ****************************************************************************************************
                  convergence was achieved on pass  4  the parameter was   1.89330E-01
                         the equation used in the search was:
                k-eff = +1.13755E+00 -9.08380E-01*p +9.68867E-01*p**2 -3.81717E-01*p**3

            k-effective=  9.97707E-01 + or -  1.60798E-03   the corresponding geometry follows;
           media bias      geometry description for those units utilized in this problem
   region    num   id
                                           -----   unit     1   -----
   1 cuboid   1  1  +x = 1.0000  -x = -1.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   2 cuboid   2  1  +x = 2.0000  -x = -2.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   3 cuboid   3  1  +x = 3.0000  -x = -3.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   4 cuboid   4  1  +x = 4.7573  -x = -4.7573  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   ****************************************************************************************************
   ****************************************************************************************************
                                 10x1x1 array default pitch search - slab
   ****************************************************************************************************
   ****************************************************************************************************
              based on the preceding data, the best estimate of the parameter is    1.85414E-01

                         the geometry corresponding to this parameter follows:
           media bias      geometry description for those units utilized in this problem
   region   num  id
                                     -----   unit     1   -----
   1 cuboid   1  1  +x = 1.0000  -x = -1.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   2 cuboid   2  1  +x = 2.0000  -x = -2.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   3 cuboid   3  1  +x = 3.0000  -x = -3.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   4 cuboid   4  1  +x = 4.7417  -x = -4.7417  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   ****************************************************************************************************
   ****************************************************************************************************

Optimum dimension search
------------------------

An optimum dimension search searches for the geometry dimensions that
yield the highest value of *k\ eff.* An optimum dimension search is
activated by entering “OPTIMUM DIMENSION” in the search data. There are
no defaulted search data in a dimension search. The user must specify
the dimensions to be changed and the manner in which they will be
changed as described in the auxiliary search commands.

A dimension search is performed by altering the regions having nonzero
search constants specified in the auxiliary search commands portion of
the search data. By default, the search constants for every dimension in
the problem are zero. Only those dimensions having a nonzero search
constant are altered by the code.

By default, a dimension search sets the minimum constraint to −10E10 and
the maximum constraint to +10E10. The relationship between the
constraints and the search constants are given in :eq:`CSASapp-1`  and :eq:`CSASapp-2`. If the
default values of the constraints are used, appropriate search constants
must be calculated using these equations. It may be simpler to set the
search constants to 1.0 and calculate the corresponding maximum and
minimum constraints. Several dimension search examples are shown below.

Array of Centered Spheres — Search in :math:`X`, :math:`Y`, and :math:`Z` Dimensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider a 10 × 10 × 10 array of uranium spheres arranged in an array
having a “square” pitch. The uranium spheres are 2 cm in radius, and the
center-to-center spacing is 8 cm. The uranium spheres and their
associated spacing are defined to be unit 1, and the 10 × 10 × 10 array
is defined to be array 1. The constraints are set to be consistent with
those of this optimum pitch search case. The search data and results for
an optimum dimension search that alters the X, Y, and Z dimensions of
region 2 of unit 1 are given as follows.

::

  =CSAS5S
  10x10x10 ARRAY - DIMENSION SEARCH
  V7-238
  READ COMP
  URANIUM 1 1.0  300.0 92235 90.0 92238 10.0 END
  H2O     2 0.01 300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SPHSQUAREP PITCH=8.0 2 FUELD=4.0 1 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  SPHERE  1 1 2.0
  CUBOID  2 1 6P4.0
  END GEOMETRY
  READ ARRAY
  ARA=1 NUX=10 NUY=10 NUZ=10 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  OPTIMUM  DIMENSION  MORE
  ALTER  UNIT=1  REG=2  ALL=1.0
  -CON=-0.5  +CON=2.5
  END SEARCH
  END

::

  *******************   search pass  1     keff=  5.05769E-01 + or -  1.10681E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  1.28075E+00 + or -  1.89662E-03   ******************
                                       the parameter was -5.00000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  2.59110E-01 + or -  8.15306E-04   ******************
                                       the parameter was  2.50000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  2.87025E-01 + or -  8.24079E-04   ******************
                                       the parameter was  1.25000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  5     keff=  2.65737E-01 + or -  7.89427E-04   ******************
                                       the parameter was  1.96019E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  6     keff=  2.63297E-01 + or -  8.48658E-04   ******************
                                       the parameter was  2.17436E+00
                                    10x10x10 array - dimension search
   ****************************************************************************************************
   ****************************************************************************************************
                 convergence was achieved on pass  2  the parameter was  -5.00000E-01
                                 the equation used in the search was:

                   k-eff = +6.70283E-01 -7.35957E-01*p +4.26318E-01*p**2 -7.98562E-02*p**3

           k-effective=  1.28075E+00 + or -  1.89662E-03   the corresponding geometry follows;
           media bias      geometry description for those units utilized in this problem
   region   num  id

                                      -----   unit     1   -----
   1 sphere   1  1  radius = 2.0000     the center is located at (  0.0000 ,  0.0000 ,  0.0000 ).
   2 cuboid   2  1  +x = 2.0000  -x = -2.0000  +y = 2.0000  -y = -2.0000  +z = 2.0000  -z = -2.0000
   ****************************************************************************************************
   ****************************************************************************************************

These MORE search data will cause the code to alter the +X, −X, +Y, −Y,
−Z, and +Z dimensions of the outer region (region 2) of unit 1 and
search for the dimensions that give the maximum *k*\ :sub:`eff`. Since all the
UNIT 1 outer dimensions are the same (4 or −4) and all the search
constants are the same (ALL=1.0) the code will alter each dimension the
same amount for a search pass thus preserving the original relationship
between dimensions. Because this is an optimum pitch search, the sphere
dimensions will not be changed. The optimum dimension for this problem
is when the spheres touch as shown in the output data above.

Array of Centered Spheres — Search in :math:`X` and :math:`Y` Dimensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the same problem as described above except the spacing is only
varied in the X and Y dimensions. Since only changes in the X and
Y dimensions of the outer region are desired, the +X, −X, +Y, and
−Y search constants must be set. Since all dimensions are to change at
the same rate and have the same initial value, the search constants for
the changing surfaces must be the same. The +Z and −Z search constants
by default are zero so these dimensions will not change. The input data
and the final search results for this problem follow:

::

  =CSAS5S
  10x10x10 ARRAY - X & Y DIMENSION OPTIMUM  SEARCH
  V7-238
  READ COMP
  URANIUM 1 1.0  300.0 92235 90.0 92238 10.0 END
  H2O     2 0.01 300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SPHSQUAREP PITCH=8.0 2 FUELD=4.0 1 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  SPHERE  1 1 2.0
  CUBOID  2 1 6P4.0
  END GEOMETRY
  READ ARRAY
  ARA=1 NUX=10 NUY=10 NUZ=10 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  OPTIMUM  DIMENSION  MORE
  ALTER  UNIT=1  REG=2  +X=1.0 -X=1.0 +Y=1.0 -Y=1.0
  -CON=-0.5  +CON=2.5
  END SEARCH
  END

::

  *******************   search pass  1     keff=  5.05769E-01 + or -  1.10681E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  9.06304E-01 + or -  1.57239E-03   ******************
                                       the parameter was -5.00000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  2.82956E-01 + or -  8.20501E-04   ******************
                                       the parameter was  2.50000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  3.19086E-01 + or -  9.27655E-04   ******************
                                       the parameter was  1.25000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  5     keff=  2.94889E-01 + or -  8.49552E-04   ******************
                                       the parameter was  1.91631E+00
                              10x10x10 array - x & y dimension optimum search
   ****************************************************************************************************
   ****************************************************************************************************
                   convergence was achieved on pass  2  the parameter was  -5.00000E-01
                               the equation used in the search was:

               k-eff = +5.70750E-01 -4.42912E-01*p +2.39464E-01*p**2 -4.35513E-02*p**3

         k-effective=  9.06304E-01 + or -  1.57239E-03   the corresponding geometry follows;
          media bias      geometry description for those units utilized in this problem
   region  num  id
                                    -----   unit     1   -----
   1 sphere   1  1  radius = 2.0000     the center is located at (  0.0000 ,  0.0000 ,  0.000  ).
   2 cuboid   2  1  +x = 2.0000  -x = -2.0000  +y = 2.0000  -y = -2.0000  +z = 4.0000  -z = -4.0000
   ****************************************************************************************************
   ****************************************************************************************************

Array of Offset Spheres — Search in :math:`X` and :math:`Y` Dimensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the same problem as described above except the spheres are now
off-centered in the X and Y dimensions. Since only changes in the X and
Y dimensions of the outer region are desired, the +X, −X, +Y, and
−Y search constants must be set. All dimensions are to change at the
same rate but they have different initial values. The search constants
specify how surfaces change relative to each other. For this case the
search constants were chosen so that the moderator spacing for the X and
Y dimensions will change at the same rate. The +Z and −Z search
constants by default are zero so these dimensions will not change.

The input data and the final search results for this problem follow:

::

  =CSAS5S
  10x10x10 ARRAY - X & Y DIMENSION OPTIMUM SEARCH - OFFSET
  V7-238
  READ COMP
  URANIUM 1 1.0  300.0 92235 90.0 92238 10.0 END
  H2O     2 0.01 300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SPHSQUAREP PITCH=8.0 2 FUELD=4.0 1 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  SPHERE  1 1 2.0  ORIGIN  2.0  1.0  0.0
  CUBOID  2 1 6.0 -2.0 5.0 -3.0 2P4.0
  END GEOMETRY
  READ ARRAY
  ARA=1 NUX=10 NUY=10 NUZ=10 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  OPTIMUM  DIMENSION  MORE
  ALTER  UNIT=1  REG=2  +X=0.3333333 -X=1.0 +Y=0.4 -Y=0.6666666
  -CON=-1.0  +CON=5.0
  END SEARCH
  END

::

  *******************   search pass  1     keff=  5.07412E-01 + or -  1.16598E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  ***
   *******************   search pass  2     keff=  9.05152E-01 + or -  1.53983E-03   ******************
                                       the parameter was -1.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  2.83216E-01 + or -  8.07313E-04   ******************
                                       the parameter was  5.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  3.20108E-01 + or -  7.96799E-04   ******************
                                       the parameter was  2.50000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  5     keff=  2.93841E-01 + or -  8.39609E-04   ******************
                                       the parameter was  3.82730E+00
                               10x10x10 array - x & y dimension optimum search - offset
   ****************************************************************************************************
   ****************************************************************************************************
                    convergence was achieved on pass  2  the parameter was  -1.00000E+00
                                 the equation used in the search was:

                k-eff = +5.73236E-01 -2.19195E-01*p +5.80895E-02*p**2 -5.19734E-03*p**3

             k-effective=  9.05152E-01 + or -  1.53983E-03   the corresponding geometry follows;
           media bias      geometry description for those units utilized in this problem
   region   num  id
                                     -----   unit     1   -----
   1 sphere   1  1  radius = 2.0000     the center is located at (  2.0000 ,  1.0000 ,  0.0000 ).
   2 cuboid   2  1  +x = 4.0000  -x =  0.0000  +y = 3.0000  -y = -1.0000  +z = 4.0000  -z = -4.0000
   ****************************************************************************************************
   ****************************************************************************************************

Array of Cylinders — Search in :math:`X`, :math:`Y`, and :math:`Z` Dimensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is the same array of cylinder problem as described in the previous
section, except the search is an optimum dimension search. Since changes
in the X, Y, and Z dimensions of the outer region are desired, the +X,
−X, +Y, −Y, +Z, and −Z search constants must be set. The search data
ALL=1.0 sets all the outer region search constants to 1.0. However, a
constant ratio for the center-to-center spacing of the units in desired
so the Z dimensions will need to be reset to a lower value of 0.333333.
This will ensure that the Z dimensions change at 1/3 the rate of the X
and Y dimensions relative to their initial values. The input data and
the final search results for this problem follow:


::

  =CSAS5S
  10x10x10 ARRAY, OPTIMUM DIMENSION SEARCH - MAINTAIN C-TO-C SPACING RATIO
  V7-238
  READ COMP
  URANIUM 1 1.0  300.0 92235 90.0 92238 10.0 END
  H2O     2 0.01 300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SQUAREPITCH PITCH=8.0 2 FUELD=4.0 1 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  CYLINDER  1 1 2.0  10.0  -10.0
  CUBOID  2 1 4p4.0  2p12.0
  END GEOMETRY
  READ ARRAY
  ARA=1 NUX=10 NUY=10 NUZ=10 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  OPTIMUM  DIMENSION  MORE
  ALTER  UNIT=1  REG=2  ALL=1.0  +Z=0.3333333  -Z=0.3333333
  -CON= -0.5  +CON=2.5
  END SEARCH
  END

::

  *******************   search pass  1     keff=  1.09882E+00 + or -  1.75627E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  1.78193E+00 + or -  2.12022E-03   ******************
                                       the parameter was -5.00000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  4.54369E-01 + or -  1.10229E-03   ******************
                                       the parameter was  2.50000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  5.67573E-01 + or -  1.26038E-03   ******************
                                       the parameter was  1.25000E+00
                   10x10x10 array, optimum dimension search - maintain c-to-c spacing ratio
   ****************************************************************************************************
   ****************************************************************************************************
                    convergence was achieved on pass  2  the parameter was  -5.00000E-01
                                 the equation used in the search was:

                 k-eff = +1.09882E+00 -1.01312E+00*p +6.38864E-01*p**2 -1.34691E-01*p**3

          k-effective=  1.78193E+00 + or -  2.12022E-03   the corresponding geometry follows;
           media bias      geometry description for those units utilized in this problem
   region   num  id
                                    -----   unit     1   -----
   1 cylinder   1  1  radius = 2.0000  +z =  10.000  -z = -10.000 centerline is at x = 0.000  y = 0.000
   2 cuboid     2  1  +x = 2.0000  -x = -2.0000  +y = 2.0000  -y = -2.0000  +z = 10.000  -z = -10.000
   ****************************************************************************************************
   ****************************************************************************************************

Minimum dimension search
------------------------

A minimum dimension search searches for the geometry dimensions that
yield the lowest value of *k*\ :sub:`eff`. A minimum dimension search is
activated by entering “MINIMUM DIMENSION” in the search data. There are
no defaulted search data in a dimension search. The user must specify
the dimensions to be changed and the manner in which they will be
changed as described in the auxiliary search commands.

A dimension search is performed by altering the regions having nonzero
search constants specified in the auxiliary search commands portion of
the search data. By default, the search constants for every dimension in
the problem are zero. Only those dimensions having a nonzero search
constant are altered by the code.

By default, a dimension search sets the minimum constraint to −10E10 and
the maximum constraint to +10E10. The relationship between the
constraints and the search constants are given in :eq:`CSASapp-1`. and :eq:`CSASapp-2`. If the
default values of the constraints are used, appropriate search constants
must be calculated using these equations. In some cases it may be
simpler to set the search constants to 1.0 and calculate the
corresponding maximum and minimum constraints. Several dimension search
examples are shown below.

Infinite Array of Fuel Bundles Separated by Flux Traps — Search in :math:`X` and :math:`Y`-Dimensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The fuel bundles in this problem represent 17 × 17 PWR fuel assemblies.
The fuel pins are smeared together, making a mixture 100. The fuel pins
consist of 2.35 wt % :sup:`235`\ U having a diameter of 0.823 cm,
zirconium cladding having an outer diameter of 0.9627 cm, and a pitch of
1.275 cm. The fuel bundle is represented as a 10.8375 cm × 10.8375 cm ×
366 cm cuboid of mixture 100 surrounded by Boral and then water. The
Boral has a density of 2.65 g/cm\ :sup:`3` and is composed of 35.17 wt %
B\ :sub:`4`\ C and 64.83 wt % Al. The fuel bundles are at a fixed pitch
of 13.0 cm. The problem searches for the thickness of Boral that will
produce the lowest system *k*\ :sub:`eff`. The input data and the final search
results for this problem follow:

::

  =csas5s
  array of fuel bundles with flux trap
  v7-238
  read comp
  uo2    1 .84 300.  92235 2.35 92238 97.65 end
  zr     2 1 end
  h2o    3 1 end
  b4c    4 den=2.65 0.3517 end
  al     4 den=2.65 0.6483 end
  h2o    5 1 end
  end comp
  read celldata
  latticecell squarepitch pitch=1.275 2 fueld=0.823 1 gapd=0.9627 2 cellmix=100 end
  end celldata
  read param far=yes gen=203 npg=1000 end param
  read geom
  global unit 1
  cuboid 100 1 4p10.8375 2p183.0
  cuboid   4 1 4p11.0    2p183.0
  cuboid   5 1 4p13.0    2p183.0
  end geom
  read bounds xfc=mirror yfc=mirror end bounds
  end data
  read search  minimum dimension  more
  alter unit=1 reg=2 +x=1.0 -x=1.0 +y=1.0 -y=1.0
  -con=-0.009  +con=0.181818
  end search
  end

::

  *******************   search pass  1     keff=  7.18665E-01 + or -  1.69354E-03   ******************
                                       the parameter was  0.00000E+00
      **** xsdrnpm mesh intervals ****
          4 mesh intervals in zone  1
          4 mesh intervals in zone  2
         14 mesh intervals in zone  3
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  7.95965E-01 + or -  1.50272E-03   ******************
                                       the parameter was  1.81818E-01
      **** xsdrnpm mesh intervals ****
          4 mesh intervals in zone  1
          4 mesh intervals in zone  2
         14 mesh intervals in zone  3
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  7.12247E-01 + or -  1.42902E-03   ******************
                                       the parameter was  6.06060E-02
      **** xsdrnpm mesh intervals ****
          4 mesh intervals in zone  1
          4 mesh intervals in zone  2
         14 mesh intervals in zone  3
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  7.40472E-01 + or -  1.45576E-03   ******************
                                       the parameter was  1.21212E-01
      **** xsdrnpm mesh intervals ****
          4 mesh intervals in zone  1
          4 mesh intervals in zone  2
         14 mesh intervals in zone  3
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  5     keff=  7.08528E-01 + or -  1.56618E-03   ******************
                                       the parameter was  4.01175E-02
                                   array of fuel bundles with flux trap
   ****************************************************************************************************
   ****************************************************************************************************
                       convergence was achieved on pass  5  the parameter was   4.01175E-02
                                 the equation used in the search was:

                  k-eff = +7.18297E-01 -5.33084E-01*p +7.78791E+00*p**2 -1.40353E+01*p**3

             k-effective=  7.08528E-01 + or -  1.56618E-03   the corresponding geometry follows;
           media bias      geometry description for those units utilized in this problem
   region   num  id
                         *******************   global   *******************
                                      -----   unit     1   -----
   1 cuboid 100  1  +x = 10.837  -x = -10.837  +y = 10.837  -y = -10.837  +z = 183.00  -z = -183.00
   2 cuboid   4  1  +x = 11.441  -x = -11.441  +y = 11.441  -y = -11.441  +z = 183.00  -z = -183.00
   3 cuboid   5  1  +x = 13.000  -x = -13.000  +y = 13.000  -y = -13.000  +z = 183.00  -z = -183.00
   ****************************************************************************************************
   ****************************************************************************************************                              array of fuel bundles with flux trap
   ****************************************************************************************************
   ****************************************************************************************************
             based on the preceding data, the best estimate of the parameter is    3.81620E-02

                              the geometry corresponding to this parameter follows:
           media bias      geometry description for those units utilized in this problem
   region   num  id
                        *******************   global   *******************
                                    -----   unit     1   -----
   1 cuboid 100  1  +x = 10.837  -x = -10.837  +y = 10.837  -y = -10.837  +z = 183.00  -z = -183.00
   2 cuboid   4  1  +x = 11.420  -x = -11.420  +y = 11.420  -y = -11.420  +z = 183.00  -z = -183.00
   3 cuboid   5  1  +x = 13.000  -x = -13.000  +y = 13.000  -y = -13.000  +z = 183.00  -z = -183.00
   ****************************************************************************************************
   ****************************************************************************************************

Two Uranium Slabs Separated by a Flux Trap — Search in +\ :math:`X` Dimensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem consists of two 90 wt % enriched uranium metal slabs
separated by a flux trap. Each uranium slab is 3.0 cm thick. The spacing
between the slabs is 4 cm. Between the slabs is a Boral plate at each
slab surface and water in between the two Boral plates. This problem
searches for the thickness of the Boral plates and separating water that
produces the lowest system *k*\ :sub:`eff`. The input data and the final search
results for this problem follow:

::

  =CSAS5S
  MINIMUM DIMENSION SEARCH - SLAB
  V7-238
  READ COMP
  URANIUM 1 1.0 300.0 92235 90.0 92238 10.0 END
  B4C 2 0.367 300.0 END
  AL 2 0.633 300.0 END
  H2O 3 1.0 300.0 END
  END COMP
  READ CELLDATA
    MULTIREGION SLAB RIGHT_BDY=VACUUM LEFT_BDY=REFLECTED END
    3 1 2 2 1 5 END ZONE
  END CELLDATA
  READ GEOMETRY
  GLOBAL UNIT 1
  CUBOID 3 1 1.0 0.0 4P100.0
  CUBOID 2 1 2.0 0.0 4P100.0
  CUBOID 1 1 5.0 0.0 4P100.0
  END GEOMETRY
  READ BOUNDS
  -XB=MIRROR
  END BOUNDS
  END DATA
  READ SEARCH MINIMUM DIMENSION MORE
  ALTER UNIT=1 REG=1 +X=1.0 CELL=1
  -CON=-1.0 +CON=1.0
  END SEARCH
  END

::

  *******************   search pass  1     keff=  8.60439E-01 + or -  1.55744E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  8.72016E-01 + or -  1.60673E-03   ******************
                                       the parameter was -1.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  1.08607E+00 + or -  1.73386E-03   ******************
                                       the parameter was  1.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  8.59819E-01 + or -  1.41625E-03   ******************
                                       the parameter was  5.00000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  5     keff=  8.56856E-01 + or -  1.53569E-03   ******************
                                      the parameter was  2.75785E-01
                                     minimum dimension search - slab
   ****************************************************************************************************
   ****************************************************************************************************
                   convergence was achieved on pass  5  the parameter was   2.75785E-01
                                 the equation used in the search was:

                   k-eff = +8.71321E-01 -9.39460E-02*p +9.57041E-02*p**2 +1.97682E-01*p**3

              k-effective=  8.56856E-01 + or -  1.53569E-03   the corresponding geometry follows;
          media bias      geometry description for those units utilized in this problem
   region  num  id
                         *******************   global   *******************
                                     -----   unit     1   -----
   1 cuboid   3  1   +x = 1.2758  -x =  0.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   2 cuboid   2  1   +x = 2.0000  -x =  0.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   3 cuboid   1  1   +x = 5.0000  -x =  0.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   ****************************************************************************************************
   ****************************************************************************************************
                                          minimum dimension search - slab
   ****************************************************************************************************
   ****************************************************************************************************
             based on the preceding data, the best estimate of the parameter is    2.68105E-01

                                 the geometry corresponding to this parameter follows:
           media bias      geometry description for those units utilized in this problem
   region   num  id
                           *******************   global   *******************
                                       -----   unit     1   -----
   1 cuboid   3  1   +x = 1.2681  -x =  0.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   2 cuboid   2  1   +x = 2.0000  -x =  0.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   3 cuboid   1  1   +x = 5.0000  -x =  0.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   ****************************************************************************************************
   ****************************************************************************************************

Critical dimension search
-------------------------

A critical dimension search searches for the geometry dimensions that
yield a specified value of *k*\ :sub:`eff`. A critical dimension search is
activated by entering “CRITICAL DIMENSION” in the search data. No
defaulted search data are in a dimension search. The user must specify
the dimensions to be changed and the manner in which they will be
changed.

A dimension search is performed by altering the regions having nonzero
search constants specified in the individual search commands portion of
the search data. By default, the search constants for every dimension in
the problem are zero. Only those dimensions having a nonzero search
constant are altered by the code.

By default, a dimension search sets the minimum constraint to −10E10 and
the maximum constraint to +10E10. The relationship between the
constraints and the search constants is given in :eq:`CSASapp-1` and :eq:`CSASapp-2`. If the
default values of the constraints are used, appropriate search constants
must be calculated using these equations. It may be simpler to set the
search constants to 1.0 and calculate the corresponding maximum and
minimum constraints. Several critical dimension search examples are
shown below.

Array of Centered Spheres — Search in :math:`X`, :math:`Y`, and :math:`Z` Dimensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider a 10 × 10 × 10 array of uranium spheres arranged in an array
having a “square” pitch. The uranium spheres are 2 cm in radius, and the
center-to-center spacing is 8 cm. The uranium spheres and their
associated spacing are defined to be unit 1, and the 10 × 10 × 10 array
is defined to be array 1. A critical dimension search is performed on
the outer dimension of the cuboid that will produce a system *k*\ :sub:`eff` of
1.0. In the MORE search data, All=1.0 on region 2 of unit 1 specifies
all six surfaces of the cuboid change identically. The search
constraints are set to search from a sphere center-to-center spacing of
4 cm to 20 cm. The search data and results are given below.

::

  =CSAS5S
  10x10x10 ARRAY - DIMENSION SEARCH
  V7-238
  READ COMP
  URANIUM 1 1.0  300.0 92235 90.0 92238 10.0 END
  H2O     2 0.01 300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SPHSQUAREP PITCH=8.0 2 FUELD=4.0 1 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  SPHERE  1 1 2.0
  CUBOID  2 1 6P4.0
  END GEOMETRY
  READ ARRAY
  ARA=1 NUX=10 NUY=10 NUZ=10 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  CRITICAL  DIMENSION  MORE
  ALTER  UNIT=1  REG=2  ALL=1.0  CELL=1
  -CON=-0.5  +CON=2.5
  END SEARCH

::

  *******************   search pass  1     keff=  5.05364E-01 + or -  1.20323E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  2.59843E-01 + or -  8.30139E-04   ******************
                                       the parameter was  2.50000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  1.27927E+00 + or -  1.51758E-03   ******************
                                       the parameter was -5.00000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  8.62177E-01 + or -  1.51303E-03   ******************
                                       the parameter was -3.36734E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  5     keff=  9.92494E-01 + or -  1.58120E-03   ******************
                                       the parameter was -3.98906E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  6     keff=  1.00529E+00 + or -  1.78980E-03   ******************
                                       the parameter was -4.01988E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  7     keff=  1.00145E+00 + or -  1.59308E-03   ******************
                                       the parameter was -4.00885E-01
                                      10x10x10 array - dimension search
   ****************************************************************************************************
   ****************************************************************************************************
                  convergence was achieved on pass  7  the parameter was  -4.00885E-0
                                the equation used in the search was:
              k-eff = +4.71062E-01 +7.54530E-02*p +2.99529E+00*p**2 -1.22324E+00*p**3

               k-effective=  1.00145E+00 + or -  1.59308E-03   the corresponding geometry follows;
           media bias      geometry description for those units utilized in this problem
   region   num  id
                                      -----   unit     1   -----
   1 sphere   1  1  radius = 2.0000  the center is located at (  0.0000 ,  0.0000 ,  0.0000 ).
   2 cuboid   2  1  +x = 2.3965  -x = -2.3965  +y = 2.3965  -y = -2.3965  +z = 2.3965  -z = -2.3965
   ****************************************************************************************************
   ****************************************************************************************************
                                 10x10x10 array - dimension search
   ****************************************************************************************************
   ****************************************************************************************************
            based on the preceding data, the best estimate of the parameter is   -4.00545E-01

                         the geometry corresponding to this parameter follows:
           media bias      geometry description for those units utilized in this problem
   region   num  id
                                    -----   unit     1   -----
   1 sphere   1  1  radius =  2.0000  the center is located at (  0.0000 ,  0.0000 ,  0.0000 ).
   2 cuboid   2  1  +x = 2.3978  -x = -2.3978  +y = 2.3978  -y = -2.3978  +z = 2.3978  -z = -2.3978
   ****************************************************************************************************
   ****************************************************************************************************

Array of Centered Spheres — Search in :math:`X`, :math:`Y`, and :math:`Z` Dimensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider a 10 × 10 × 10 array of uranium spheres arranged in an array
having a “square” pitch. The uranium spheres are 2 cm in radius, and the
center-to-center spacing is 8 cm. The uranium spheres and their
associated spacing are defined to be unit 1, and the 10 × 10 × 10 array
is defined to be array 1. A critical dimension search is performed on
the radius of the uranium sphere that will produce a system *k*\ :sub:`eff` of
1.0. In the MORE search data, RADIUS=1.0 on region 1 of unit 1 specifies
the sphere’s radius is to be altered. The search constraints are set to
search from a radius of 0.5 cm to 4.0 cm. The search data and results
are given below.

::

  =CSAS5S
  10x10x10 ARRAY - DIMENSION SEARCH
  V7-238
  READ COMP
  URANIUM 1 1.0  300.0 92235 90.0 92238 10.0 END
  H2O     2 0.01 300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SPHSQUAREP PITCH=8.0 2 FUELD=4.0 1 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  SPHERE  1 1 2.0
  CUBOID  2 1 6P4.0
  END GEOMETRY
  READ ARRAY
  ARA=1 NUX=10 NUY=10 NUZ=10 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  CRITICAL  DIMENSION  MORE
  ALTER  UNIT=1  CELL=1  REG=1  RADIUS=1.0
  -CON=-0.75  +CON=1.0
  END SEARCH
  END

::

  *******************   search pass  1     keff=  5.05364E-01 + or -  1.20323E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  1.79497E+00 + or -  1.93055E-03   ******************
                                       the parameter was  1.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  9.91353E-01 + or -  1.56062E-03   ******************
                                       the parameter was  3.83555E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  9.97513E-01 + or -  1.61171E-03   ******************
                                       the parameter was  3.90304E-01
                                       10x10x10 array - dimension search
   ****************************************************************************************************
   ****************************************************************************************************
                   convergence was achieved on pass  4  the parameter was   3.90304E-01
                                the equation used in the search was:

                 k-eff = +5.05364E-01 +1.84705E+00*p -2.10615E+00*p**2 +1.54871E+00*p**3

           k-effective=  9.97513E-01 + or -  1.61171E-03   the corresponding geometry follows;
           media bias      geometry description for those units utilized in this problem
   region   num  id
                                    -----   unit     1   -----
   1 sphere   1  1  radius = 2.7806     the center is located at (  0.0000 ,  0.0000 ,  0.0000 ).
   2 cuboid   2  1  +x = 4.0000  -x = -4.0000  +y = 4.0000  -y = -4.0000  +z = 4.0000  -z = -4.0000
   ****************************************************************************************************
   ****************************************************************************************************
                                    10x10x10 array - dimension search
   ****************************************************************************************************
               based on the preceding data, the best estimate of the parameter is    3.93037E-01

                             the geometry corresponding to this parameter follows:
           media bias      geometry description for those units utilized in this problem
   region   num  id
                                          -----   unit     1   -----
   1 sphere   1  1  radius =  2.7861     the center is located at (  0.0000 ,  0.0000 ,  0.0000 ).
   2 cuboid   2  1  +x = 4.0000  -x = -4.0000  +y = 4.0000  -y = -4.0000  +z = 4.0000  -z = -4.0000
  ****************************************************************************************************

Array of Centered Cylinders — Search in :math:`X` and :math:`Y` Dimensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem contains search data for a critical dimension search with
*k*\ :sub:`eff` specified to be 0.95. The problem consists of a
10 × 10 × 2 array of uranium cylinders surrounded by low density water.
The cylinders are 90% :sup:`235`\ U and 10% :sup:`238`\ U and have a
radius of 2.0 cm and a length of 20 cm. The cylinders are originally
centered on an 8.0 cm X and Y pitch and a 24 cm Z pitch with
interstitial low density (0.01 gm/cc) water. The problem searches for
the cylinder center-to-center spacing that will produce a
*k*\ :sub:`eff` = 0.95 for the system. Because this is a dimension search, all
search data must be specified. The +X, −X, +Y, and −Y search constants
are specified as well as the −CON and +CON search constraints. The
search data is set up to alter the cylinder center-to-center spacing
from 4.0 cm to 16.0 cm during the search. The MORE search data CELL=1
ties the search data to the first unit cell thus ensuring they change in
unison properly modifying the cross-section processing. The input data
and the final search results for this problem follow:

::

  =CSAS5S
  10x10x2 ARRAY DIMENSION SEARCH - CHANGE IN X, Y
  V7-238
  READ COMP
  URANIUM 1 1.0  300.0 92235 90.0 92238 10.0 END
  H2O     2 0.01 300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SQUAREPITCH PITCH=8.0 2 FUELD=4.0 1 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  CYLINDER  1 1 2.0  10.0  -10.0
  CUBOID  2 1 4p4.0  2p12.0
  END GEOMETRY
  READ ARRAY
  ARA=1 NUX=10 NUY=10 NUZ=2 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  CRITICAL  DIMENSION  KEFF=0.95  MORE
  ALTER  UNIT=1  REG=2  +X=1.0 -X=1.0 +Y=1.0 -Y=1.0 CELL=1
  -CON=-0.5  +CON=2.0
  END SEARCH
  END

::

  *******************   search pass  1     keff=  8.48434E-01 + or -  1.50137E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  4.22734E-01 + or -  9.98609E-04   ******************
                                       the parameter was  2.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  1.49380E+00 + or -  1.81532E-03   ******************
                                       the parameter was -4.77172E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  9.23415E-01 + or -  1.68810E-03   ******************
                                       the parameter was -8.66017E-02
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  5     keff=  9.47041E-01 + or -  1.57053E-03   ******************
                                       the parameter was -1.13412E-01
                             10x10x2 array dimension search - change in x, y
   ****************************************************************************************************
   ****************************************************************************************************
                    convergence was achieved on pass  5  the parameter was  -1.13412E-01
                                 the equation used in the search was:

                     k-eff = +8.52892E-01 -6.96099E-01*p +1.13262E+00*p**2 -4.46134E-01*p**3

               k-effective=  9.47041E-01 + or -  1.57053E-03   the corresponding geometry follows;
           media bias      geometry description for those units utilized in this problem
   region   num  id
                                        -----   unit     1   -----
   1 cylinder 1  1  radius = 2.0000  +z = 10.000  -z = -10.000  centerline is at  x = 0.000  y =  0.000
   2 cuboid   2  1  +x = 3.5464  -x = -3.5464  +y = 3.5464  -y = -3.5464  +z = 12.000  -z = -12.000
   ****************************************************************************************************
   ****************************************************************************************************
                            10x10x2 array dimension search - change in x, y
   ****************************************************************************************************
   ****************************************************************************************************
               based on the preceding data, the best estimate of the parameter is   -1.16433E-01

                              the geometry corresponding to this parameter follows:
           media bias      geometry description for those units utilized in this problem
   region   num  id
                                      -----   unit     1   -----
   1 cylinder 1  1  radius = 2.0000  +z = 10.000  -z = -10.000  centerline is at  x = 0.000   y = 0.000
   2 cuboid   2  1  +x = 3.5343  -x = -3.5343  +y = 3.5343  -y = -3.5343  +z = 12.000  -z = -12.000
   ****************************************************************************************************
   ****************************************************************************************************z

Array of Centered Uranium Slabs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider a 10 × 1 × 1 array of uranium metal slabs. The uranium slabs
are 2 cm thick in the X dimension and 200 cm thick in the Y and
Z dimensions. On each side of the uranium slab in the X dimension is
1 cm of H\ :sub:`2`\ O, then 1 cm of Boral, then 1 cm of H\ :sub:`2`\ O
resulting in an initial center-to-center spacing of 8.0 cm. The slabs
are 90% :sup:`235`\ U and 10% :sup:`238`\ U, the water is full density,
and the Boral is 36.7% B\ :sub:`4`\ C. The uranium slabs and their
associated materials are defined to be Unit 1, and the 10 × 1 × 1 array
is defined to be array 1. The problem searches for the slab
center-to-center spacing that will produce a *k*\ :sub:`eff` = 1.0 for the
system, which is the default search value. Because this is a dimension
search all search data must be specified. The +X and −X search constants
are specified as well as the −CON and +CON search constraints. The
search data is set up to alter the cylinder change the water slab
thickness between the Boral plates from 0.8 cm to 10.0 cm thick during
the search. The MORE search data CELL=1 ties the search data to the
first unit cell thus ensuring they change in unison properly modifying
the cross-section processing. The input data and the final search
results for this problem follow:

::

  =CSAS5S
  10x1x1 ARRAY DIMENSION SEARCH - SLAB
  V7-238
  READ COMP
  URANIUM 1 1.0   300.0 92235 90.0 92238 10.0 END
  H2O     2 1.0   300.0 END
  B4C     3 0.367 300.0 END
  AL      3 0.633 300.0 END
  H2O     4 1.0   300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SYMMSLABCELL PITCH=8.0 4 FUELD=2.0 1
                           GAPD=6.0 3 CLADD=4.0 2 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  CUBOID  1 1 1.0  -1.0  4P100.0
  CUBOID  2 1 2.0  -2.0  4p100.0
  CUBOID  3 1 3.0  -3.0  4P100.0
  CUBOID  4 1 4.0  -4.0  4P100.0
  END GEOMETRY
  READ ARRAY
  ARA=1 GBL=1 NUX=10 NUY=1 NUZ=1 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  CRITICAL  DIMENSION  MORE
  ALTER  UNIT=1  REG=4  +X=1.0  -X=1.0  CELL=1
  -CON=-0.24  +CON=1.0
  END SEARCH
  END

::

  *******************   search pass  1     keff=  1.13914E+00 + or -  1.53132E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  1.41849E+00 + or -  1.58152E-03   ******************
                                       the parameter was -2.40000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  1.04012E+00 + or -  1.79880E-03   ******************
                                       the parameter was  1.19536E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  9.99495E-01 + or -  1.65714E-03   ******************
                                       the parameter was  1.80331E-01
                                   10x1x1 array dimension search - slab
   ****************************************************************************************************
   ****************************************************************************************************
                      convergence was achieved on pass  4  the parameter was   1.80331E-01
                                 the equation used in the search was:

              k-eff = +1.13914E+00 -9.36766E-01*p +9.20374E-01*p**2 -1.09475E-01*p**3

           k-effective=  9.99495E-01 + or -  1.65714E-03   the corresponding geometry follows;
           media bias      geometry description for those units utilized in this problem
   region   num  id
                                         -----   unit     1   -----
   1 cuboid   1  1   +x = 1.0000  -x = -1.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   2 cuboid   2  1   +x = 2.0000  -x = -2.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   3 cuboid   3  1   +x = 3.0000  -x = -3.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   4 cuboid   4  1   +x = 4.7213  -x = -4.7213  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   ****************************************************************************************************
   ****************************************************************************************************
                                 10x1x1 array dimension search - slab
   ****************************************************************************************************
   ****************************************************************************************************
            based on the preceding data, the best estimate of the parameter is    1.79511E-01

                            the geometry corresponding to this parameter follows:
          media bias      geometry description for those units utilized in this problem
   region  num  id
                                           -----   unit     1   -----
   1 cuboid   1  1   +x = 1.0000  -x = -1.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   2 cuboid   2  1   +x = 2.0000  -x = -2.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   3 cuboid   3  1   +x = 3.0000  -x = -3.0000  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   4 cuboid   4  1   +x = 4.7180  -x = -4.7180  +y = 100.00  -y = -100.00  +z = 100.00  -z = -100.00
   ****************************************************************************************************
   ****************************************************************************************************

Search on Multiple Units and Regions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider a problem having Units 1, 2, and 3. Unit 1 consists of three
concentric spheres in a cuboid. Unit 2 consists of a single sphere in a
cuboid, and Unit 3 contains three concentric cuboids. A search is to be
made that changes the exterior dimensions of the three units, the inner
sphere of Unit 1, and the sphere of Unit 2. The thicknesses of the outer
spheres of Unit 1 are to be maintained, and the two inner cuboids of
Unit 3 are to remain unchanged. The search data and results for this
problem are the following:

::

  =CSAS5S
  DEMONSTRATION OF CRITICAL DIMENSION SEARCH
  V7-252
  READ COMP
  URANIUM  1 0.985 293  92235 93.2 92238 5.6 92234 1.0 92236 0.2 END
  PLEXIGLAS  2 END
  SS304    3 END
  END COMP
  READ PARAMETERS  GEN=203 NPG=1500
  END PARAMETERS
  READ GEOMETRY
  UNIT 1
  SPHERE 1 1 3.0
  SPHERE 0 1 3.25
  SPHERE 2 1 3.5
  CUBE   0 1 2P5.0
  UNIT 2
  SPHERE 1 1 3.0
  CUBE   0 1 2P5.0
  UNIT 3
  CUBE   0 1 2P4.9
  CUBE   3 1 2P5.0
  CUBE   0 1 2P5.0
  END GEOMETRY
  READ ARRAY ARA=1 NUX=3 NUY=3 NUZ=3 FILL
  1 3 2 3 2 3 2 3 1
  3 2 3 1 3 2 3 1 3
  2 3 1 3 1 3 1 3 2
  END FILL END ARRAY
  END DATA
  READ SEARCH   CRITICAL DIMENSION
  KEF=1.000  EPS=0.005  MORE
  ALTER UNIT=1 REG=1 ALL=1.0
  ALTER UNIT=1 REG=4 ALL=1.0
  ALTER UNIT=2 REG=1 TO 2 ALL=1.0
  ALTER UNIT=3 REG=3 ALL=1.0
  MAINTAIN UNIT=1 REG=2 TO 3 ALL=1.0
  +CON=2.0  -CON=-0.5
  END SEARCH
  END

::

  *******************   search pass  1     keff=  4.04885E-01 + or -  8.44823E-04   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  1.07404E+00 + or -  1.44587E-03   ******************
                                       the parameter was  2.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  1.01654E+00 + or -  1.38559E-03   ******************
                                       the parameter was  1.77869E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  9.94811E-01 + or -  1.34462E-03   ******************
                                       the parameter was  1.71784E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  5     keff=  9.99482E-01 + or -  1.35858E-03   ******************
                                       the parameter was  1.73183E+00
                            search demonstration of critical dimension search
   ****************************************************************************************************
   ****************************************************************************************************
                 convergence was achieved on pass  5  the parameter was   1.73183E+00
                                 the equation used in the search was:

                 k-eff = +4.05037E-01 -7.56139E-02*p +4.77691E-01*p**2 -1.36173E-01*p**3

           k-effective=  9.99482E-01 + or -  1.35858E-03   the corresponding geometry follows;
           media bias      geometry description for those units utilized in this problem
   region   num  id
                                      -----   unit     1   -----
   1 sphere   1  1  radius =  8.1955     the center is located at (  0.0000 ,  0.0000 ,  0.0000 ).
   2 sphere   0  1  radius =  8.4455     the center is located at (  0.0000 ,  0.0000 ,  0.0000 ).
   3 sphere   2  1  radius =  8.6955     the center is located at (  0.0000 ,  0.0000 ,  0.0000 ).
   4 cuboid   0  1  +x =  13.659  -x = -13.659  +y =  13.659  -y = -13.659  +z =  13.659  -z = -13.659

                                      -----   unit     2   -----
   1 sphere   1  1  radius =  8.1955     the center is located at (  0.0000 ,  0.0000 ,  0.0000 ).
   2 cuboid   0  1  +x =  13.65   -x = -13.659  +y =  13.659  -y = -13.659  +z =  13.659  -z = -13.659

                                     -----   unit     3   -----
   1 cuboid   0  1  +x =  4.9000  -x = -4.9000  +y =  4.9000  -y = -4.9000  +z =  4.9000  -z = -4.9000
   2 cuboid   3  1  +x =  5.0000  -x = -5.0000  +y =  5.0000  -y = -5.0000  +z =  5.0000  -z = -5.0000
   3 cuboid   0  1  +x =  13.659  -x = -13.659  +y =  13.659  -y = -13.659  +z =  13.659  -z = -13.659
   ****************************************************************************************************
   ****************************************************************************************************
                              search demonstration of critical dimension search
   ****************************************************************************************************
   ****************************************************************************************************
             based on the preceding data, the best estimate of the parameter is    1.73328E+00

                        the geometry corresponding to this parameter follows:
           media bias      geometry description for those units utilized in this problem
   region   num  id
                                      -----   unit     1   -----
   1 sphere   1  1  radius =  8.1998     the center is located at (  0.0000 ,  0.0000 ,  0.0000 ).
   2 sphere   0  1  radius =  8.4498     the center is located at (  0.0000 ,  0.0000 ,  0.0000 ).
   3 sphere   2  1  radius =  8.6998     the center is located at (  0.0000 ,  0.0000 ,  0.0000 ).
   4 cuboid   0  1  +x =  13.666  -x = -13.666  +y =  13.666  -y = -13.666  +z =  13.666  -z = -13.666
                                      -----   unit     2   -----
   1 sphere   1  1  radius =  8.1998     the center is located at (  0.0000 ,  0.0000 ,  0.000  ).
   2 cuboid   0  1  +x =  13.666  -x = -13.666  +y =  13.666  -y = -13.666  +z =  13.666  -z = -13.666

                                     -----   unit     3   -----
   1 cuboid   0  1  +x =  4.9000  -x = -4.9000  +y =  4.9000  -y = -4.9000  +z =  4.9000  -z = -4.9000
   2 cuboid   3  1  +x =  5.0000  -x = -5.0000  +y =  5.0000  -y = -5.0000  +z =  5.0000  -z = -5.0000
   3 cuboid   0  1  +x =  13.666  -x = -13.666  +y =  13.666  -y = -13.666  +z =  13.666  -z = -13.666
   ****************************************************************************************************
   ****************************************************************************************************

UO\ :sub:`2`\ F\ :sub:`2` Solution Tank — Critical Search on Chord Length
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Consider a large spherical tank partially filled with
UO\ :sub:`2`\ F\ :sub:`2` solution. The tank has a radius of 34.6 cm and
is initially filled with solution to a height of 10.0 cm above the
midpoint. The tank is composed of a 0.759-cm-thick Al shell. The
UO\ :sub:`2`\ F\ :sub:`2` solution is composed of three standard
compositions: UO\ :sub:`2`\ F\ :sub:`2`, HF acid, and H\ :sub:`2`\ O.
The code combines these using a set algorithm. This may or may not
produce a solution at the desired density. If the density of the
solution is known it should be entered. Also, extra acid can be added to
the solution by specifying a non-zero acid molarity.

A critical dimension search is performed on the length of the chord
yielding system *k*\ :sub:`eff` = 0.98. In the MORE search data, UNIT=1 REG=1
CHORD=1 specifies that the chord length of region 1 in Unit 1 is to be
altered with the limits defined by the search constraints. The minimum
search constraint is set so region 1 consists of the part of the sphere
below an X-Y plane 10.0 cm below the sphere’s midpoint. The maximum
search constraint is set so region 1 consists of almost the entire
sphere.

The constraints are calculated as follows:

  D\ :sub:`i` = ( Radius\ :sub:`i` + Chord\ :sub:`i` ) / (
  2*Radius\ :sub:`i` ) = ( 34.6 + 10.0 ) / 2*34.6 ) = 0.6445

  D\ :sub:`min` = ( Radius\ :sub:`min` + Chord\ :sub:`min` ) / (
  2*Radius\ :sub:`min` ) = ( 34.6 + − 10.0 ) / 2*34.6 ) = 0.3555

  D\ :sub:`max` = ( Radius\ :sub:`max` + Chord\ :sub:`max` ) / (
  2*Radius\ :sub:`max` ) = ( 34.6 + 34.6 ) / 2*34.6 ) = 1.0

The maximum constraint is calculated according to:

  +CON = [ ( D\ :sub:`max` / D\ :sub:`i` ) −1.0 ] / CHORD = [ ( 1.0 /
  0.6445 ) −1.0 ] / 1.0 = 0.5515

The minimum constraint is calculated according to:

  −CON = [ ( D\ :sub:`min` / D\ :sub:`i` ) − 1.0 ] / CHORD = [ ( 0.3555 /
  0.6445 ) − 1.0 ] / 1.0 = −0.4484

The search data and final search results for this problem follow:

::

  =csas5s
  sample problem 6 soln tank - crit.  dim.  search on chord
  v7-238
  read comp
  solnuo2f2  1 500 0 1 300.0 92235 4.89 92238 95.09 92234 0.02 end
  al         2 1.0 300.0 end
  end comp
  sample problem 6 soln tank - crit.  dim.  search on chord
  read geom
  unit 1
  hemisphe-z  1 1 34.6   chord 10.
  sphere      0 1 34.6
  sphere      2 1 34.759
  end geom
  end data
  READ SEARCH  CRITICAL  DIMENSION KEF=0.98  MORE
  ALTER  UNIT=1  REG=1  CHORD=1.0
  -CON=-0.4484  +CON=0.5515
  END SEARCH
  end

::

   *******************   search pass  1     keff=  9.32087E-01 + or -  1.25932E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  1.00306E+00 + or -  1.54366E-03   ******************
                                       the parameter was  5.51500E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  9.95554E-01 + or -  1.33223E-03   ******************
                                       the parameter was  3.72325E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  9.80534E-01 + or -  1.47774E-03   ******************
                                       the parameter was  2.37245E-01
                          solution tank - critical dimension search on chord length
   ****************************************************************************************************
   ****************************************************************************************************
                      convergence was achieved on pass  4  the parameter was   2.37245E-01
                                 the equation used in the search was:

                   k-eff = +9.32087E-01 +2.68165E-01*p -2.82174E-01*p**2 +5.30631E-02*p**3

               k-effective=  9.80534E-01 + or -  1.47774E-03   the corresponding geometry follows;
              media bias      geometry description for those units utilized in this problem
   region       num id
                           *******************   global   *******************
                                         -----   unit     1   -----
   1 -zhemisphere 1 1 radius = 34.600 existing in the -z direction center=(0.00,0.00,0.00) chord=20.581
   2 sphere       0 1 radius = 34.600     the center is located at ( 0.0000 , 0.0000 , 0.0000 ).
   3 sphere       2 1 radius = 34.759     the center is located at ( 0.0000 , 0.0000 , 0.0000 ).
   ****************************************************************************************************
   ****************************************************************************************************
                        solution tank - critical dimension search on chord length
   ****************************************************************************************************
   ****************************************************************************************************
              based on the preceding data, the best estimate of the parameter is    2.33538E-01

                             the geometry corresponding to this parameter follows:
              media bias      geometry description for those units utilized in this problem
   region       num id
                              *******************   global   *******************
                                          -----   unit     1   -----
   1 -zhemisphere 1 1 radius = 34.600 existing in the -z direction center=(0.00,0.00,0.00) chord=20.416
   2 sphere      0 1 radius = 34.600     the center is located at ( 0.0000 , 0.0000 , 0.0000 ).
   3 sphere      2 1 radius = 34.759     the center is located at ( 0.0000 , 0.0000 , 0.0000 ).
   ****************************************************************************************************
   ****************************************************************************************************

Optimum concentration search
----------------------------

An optimum concentration search alters the concentration of the
specified standard composition in the specified mixture to determine the
highest value of *k*\ :sub:`eff`. The limits for an optimum concentration
search are governed by the values entered for the parameter constraints.
An optimum concentration search is activated by entering “OPTIMUM
CONCENTRATION” in the search data. No defaulted search data are in a
concentration search. The user must specify the material and standard
composition name to be changed and the manner in which they will be
changed.

A concentration search is performed by altering the atom densities of
the specified standard compositions in the specified materials. The
ratio of how the standard compositions change relative to each other is
controlled using FACTOR. If a material and standard composition is not
listed in the search data it remains unchanged. The concentration search
can vary from zero to some upper limit. The code will prevent the
concentration from falling below zero, but the user is responsible for
setting constraints that prevent the concentration from exceeding
reasonable values. In most cases the theoretical density is a reasonable
upper limit.

Array of Spheres in H\ :sub:`2`\ O — Search on H\ :sub:`2`\ O Density
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider a 10 × 10 × 10 array of uranium spheres arranged in an array
having a “square” pitch. The uranium spheres are 2 cm in radius, and the
center-to-center spacing is 8 cm. The uranium spheres and their
associated spacing are defined to be unit 1, and the 10 × 10 × 10 array
is defined to be array 1. The spheres are initially moderated by ½
density water.

An optimum concentration search is performed on the water yielding the
maximum system *k*\ :sub:`eff` for various densities of water. In the MORE
search data, MIX=2 and SCNAME=H2O specify that the water component of
mixture 2 is to be altered during the search. The maximum allowed
density is full density water. The minimum allowed density is
0.05 density water.

The maximum constraint is calculated according to:

.. math::

  +\text{CON}= \frac {\left(\frac{\text{D}_{max}}{\text{D}_{initial}} - 1 \right)}{\text{FACTOR}}    \ \ \ \ \    +\text{CON}= \frac{\left(\frac{1.0}{0.5} - 1 \right)}{1} = \frac{1}{0}


The minimum constraint is calculated according to:

.. math::

  -\text{CON}= \frac {\left(\frac{\text{D}_{min}}{\text{D}_{initial}} - 1 \right)}{\text{FACTOR}}    \ \ \ \ \    -\text{CON}= \frac{\left(\frac{0.05}{0.5} - 1 \right)}{1} = -0.9


The search data and final search results for this problem follow:

::

  =CSAS5S
  10x10x10 ARRAY - CONCENTRATION SEARCH
  V7-238
  READ COMP
  URANIUM 1 1.0 300.0 92235 90.0 92238 10.0 END
  H2O     2 0.5 300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SPHSQUAREP PITCH=8.0 2 FUELD=4.0 1 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  SPHERE  1 1 2.0
  CUBOID  2 1 6P4.0
  END GEOMETRY
  READ ARRAY
  ARA=1 NUX=10 NUY=10 NUZ=10 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  OPTIMUM  CONCENTRATION  MORE
  ALTER  MIX=2  SCNAME=H2O  FACTOR=1.0
  -CON=-0.9  +CON=1.0
  END SEARCH
  END

::

  *******************   search pass  1     keff=  1.22228E+00 + or -  1.75549E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  5.58399E-01 + or -  1.29164E-03   ******************
                                       the parameter was -9.00000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  1.01673E+00 + or -  1.58517E-03   ******************
                                       the parameter was  1.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  1.14752E+00 + or -  1.59590E-03   ******************
                                       the parameter was  5.00000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  5     keff=  1.22423E+00 + or -  1.82022E-03   ******************
                                       the parameter was  4.32687E-02
                                   10x10x10 array - concentration search
   ****************************************************************************************************
   ****************************************************************************************************
                 convergence was achieved on pass  5  the parameter was   4.32687E-02
                                 the equation used in the search was:

                 k-eff = +1.22278E+00 +5.50106E-02*p -5.25565E-01*p**2 +2.61295E-01*p**3

           k-effective=  1.22423E+00 + or -  1.82022E-03   the corresponding geometry follows;
                                10x10x10 array - concentration search
                                            mixing table

                              number of scattering angles =  2
                           cross section message threshold =5.7E-02

   mixture =     1          density(g/cc) =  19.050
    nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   1092235  4.39277E-02  9.00000E-01  92235  235.0441   92u 235 bnl evalapr77 m.r.bhat mod3 02/28/89
   1092238  4.81921E-03  1.00000E-01  92238  238.0510   92U 238 ANL+ EVALJUN77 E.PENNINGTONMOD3 02/13/92

   mixture =     2          density(g/cc) = 0.52068
    nuclide  atom-dens.    wgt.  frac.      za      awt               nuclide title
   2001001 3.48291E-02  1.11926E-01  1001   1.0077    hydrogen in water 1301/1002  mod1 11/23/92
   2008016 1.74146E-02  8.88073E-01  8016  15.9904    8O 16 from version 6 evaluation

              based on the preceding data, the best estimate of the parameter is    5.45542E-02

                          the mixing table corresponding to this parameter follows:
                                     10x10x10 array - concentration search
                                             mixing table

                                  number of scattering angles =  2
                               cross section message threshold =5.7E-02

   mixture =     1          density(g/cc) =  19.050
   nuclide   atom-dens.   wgt.  frac.    za      awt               nuclide title
   1092235  4.39277E-02 9.00000E-01  92235  235.0441  92u 235 bnl evalapr77 m.r.bhat mod3 02/28/89
   1092238  4.81921E-03 1.00000E-01  92238  238.0510  92U 238 ANL+ EVALJUN77 E.PENNINGTON MOD3 02/13/92

   mixture =     2          density(g/cc) = 0.52631
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   2001001  3.52059E-02  1.11927E-01   1001    1.0077   hydrogen in water 1301/1002    mod1   11/23/92
   2008016  1.76029E-02  8.88073E-01   8016   15.9904   8O 16 from version 6 evaluation
   ****************************************************************************************************
   ****************************************************************************************************

Array of Cylinders in H\ :sub:`2`\ O — Search on H\ :sub:`2`\ O Density
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem contains search data for an optimum concentration search.
The problem consists of a 10 × 10 × 1 array of uranium cylinders
surrounded initially by 0.5 gm/cc density water. The cylinders are 90%
:sup:`235`\ U and 10% :sup:`238`\ U and have a radius of 2.0 cm and a
length of 200 cm. The cylinders are originally centered on an 8.0 cm X
and Y pitch with interstitial low density (0.5 gm/cc) water. The problem
searches for the H\ :sub:`2`\ O density that will produce the maximum
system *k*\ :sub:`eff`. In the MORE search data, MIX=2 and SCNAME=H2O specify
that the water component of mixture 2 is to be altered during the
search. The maximum allowed density is full density water. The minimum
allowed density is 0.05 density water.

The maximum constraint is calculated according to:

.. math::

  +\text{CON}= \frac {\left(\frac{\text{D}_{max}}{\text{D}_{initial}} - 1 \right)}{\text{FACTOR}}    \ \ \ \ \    +\text{CON}= \frac{\left(\frac{1.0}{0.5} - 1 \right)}{1} = -1.0

The minimum constraint is calculated according to:

.. math::

  -\text{CON}= \frac {\left(\frac{\text{D}_{min}}{\text{D}_{initial}} - 1 \right)}{\text{FACTOR}}    \ \ \ \ \    -\text{CON}= \frac{\left(\frac{0.05}{0.5} - 1 \right)}{1} = -0.9


The search data and final search results for this problem follow:

::

  =CSAS5S
  10x10x1 ARRAY CONCENTRATION SEARCH - CHANGE H2O
  V7-238
  READ COMP
  URANIUM 1 1.0 300.0 92235 90.0 92238 10.0 END
  H2O     2 0.5 300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SQUAREPITCH PITCH=8.0 2 FUELD=4.0 1 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  CYLINDER  1 1 2.0  100.0  -100.0
  CUBOID  2 1 4p4.0  2p100.0
  END GEOMETRY
  READ ARRAY
  ARA=1 NUX=10 NUY=10 NUZ=1 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  OPTIMUM  CONCENTRATION  MORE
  ALTER  MIX=2  SCNAME=H2O  FACTOR=1.0
  -CON=-0.9  +CON=1.0
  END SEARCH
  END

::

  *******************   search pass  1     keff=  1.63537E+00 + or -  1.70164E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  1.26936E+00 + or -  1.79640E-03   ******************
                                       the parameter was -9.00000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  1.51475E+00 + or -  1.50298E-03   ******************
                                       the parameter was  1.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  1.61045E+00 + or -  1.48777E-03   ******************
                                       the parameter was  5.00000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  5     keff=  1.63831E+00 + or -  1.43843E-03   ******************
                                       the parameter was  1.29491E-01
                               10x10x10 array concentration search - change h2o
   ****************************************************************************************************
   ****************************************************************************************************
                      convergence was achieved on pass  5  the parameter was   1.29491E-01

                                the equation used in the search was:

                    k-eff = +1.63481E+00 +6.23193E-02*p -2.85686E-01*p**2 +1.05562E-01*p**3

           k-effective=  1.63831E+00 + or -  1.43843E-03   the corresponding geometry follows;
                              10x10x10 array concentration search - change h2o
                                          mixing table
                                 number of scattering angles =  2
                             cross section message threshold =5.7E-02

   mixture =     1          density(g/cc) =  19.050
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   1092235  4.39277E-02  9.00000E-01  92235  235.0441  92u 235 bnl evalapr77 m.r.bhat  mod3 02/28/89
   1092238  4.81921E-03  1.00000E-01  92238  238.0510  92U 238 ANL+ EVALJUN77 E.PENNINGTON MOD3 02/13/92

   mixture =     2          density(g/cc) = 0.56371
   nuclide   atom-dens.    wgt.  frac.    za      awt               nuclide title
   2001001  3.77076E-02  1.11926E-01  1001   1.0077  hydrogen in water 1301/1002    mod1   11/23/92
   2008016  1.88538E-02  8.88073E-01  8016  15.9904  8O 16 from version 6 evaluation
            based on the preceding data, the best estimate of the parameter is    1.16606E-01

                        the mixing table corresponding to this parameter follows:
                             10x10x10 array concentration search - change h2o
                                            mixing table

                                    number of scattering angles =  2
                                cross section message threshold =5.7E-02

   mixture =     1          density(g/cc) =  19.050
   nuclide   atom-dens.   wgt.  frac.     za     awt               nuclide title
   1092235  4.39277E-02 9.00000E-01  92235  235.0441  92u 235 bnl evalapr77 m.r.bhat mod3 02/28/89
   1092238  4.81921E-03 1.00000E-01  92238  238.0510  92U 238 ANL+ EVALJUN77 E.PENNINGTON MOD3 02/13/92

   mixture =     2          density(g/cc) = 0.55728
   nuclide   atom-dens.    wgt.  frac.    za     awt             nuclide title
   2001001  3.72774E-02  1.11927E-01  1001   1.0077  hydrogen in water 1301/1002 mod1 11/23/92
   2008016  1.86387E-02  8.88074E-01  8016  15.9904  8O 16 from version 6 evaluation
   ****************************************************************************************************
   ****************************************************************************************************

Cell-Weighted Array of Uranium Cylinders in H\ :sub:`2`\ O — Search on H\ :sub:`2`\ O Density
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem contains search data for an optimum concentration search.
The problem consists of a single material representing a
10 × 10 × 1 array of uranium cylinders surrounded initially by 0.5 gm/cc
density water. The cylinders are 90% \ :sup:`235`\ U and
10% \ :sup:`238`\ U and have a radius of 2.0 cm and a length of 200 cm.
The cylinders are originally centered on an 8.0 cm X and Y-pitch with
interstitial low density (0.5 gm/cc) water. The keyword CELL=100 in the
unit cell data indicates this will be a cell-weighted problem with
mixture 100 representing the array of uranium rods in water. The problem
searches for the H\ :sub:`2`\ O density that will produce the maximum
system *k*\ :sub:`eff`. In the MORE search data, MIX=2 and
SCNAME=H\ :sub:`2`\ O specify that the water component of mixture 2 is
to be altered during the search. On each pass the water density is
altered, XSDRNPM is run to produce a new mixture 100, and mixture 100 is
used in KENO V.a to calculate a new system *k*\ :sub:`eff`. The cylinder and
cuboid in unit 1 and the array contained in the above problem are
replaced by a cuboid of the same size as the array containing
mixture 100. The maximum allowed density is full density water. The
minimum allowed density is 0.05 density water.

The maximum constraint is calculated according to:

.. math::

  +\text{CON}= \frac {\left(\frac{\text{D}_{max}}{\text{D}_{initial}} - 1 \right)}{\text{FACTOR}}    \ \ \ \ \    +\text{CON}= \frac{\left(\frac{1.0}{0.5} - 1 \right)}{1} = -1.0


The minimum constraint is calculated according to:

.. math::

  -\text{CON}= \frac {\left(\frac{\text{D}_{min}}{\text{D}_{initial}} - 1 \right)}{\text{FACTOR}}    \ \ \ \ \    -\text{CON}= \frac{\left(\frac{0.05}{0.5} - 1 \right)}{1} = -0.9

The search data and final search results for this problem follow:

::

  =CSAS5S
  10x10x1 ARRAY CONCENTRATION SEARCH - CHANGE H2O
  V7-238
  READ COMP
  URANIUM 1 1.0 300.0 92235 90.0 92238 10.0 END
  H2O     2 0.5 300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL  CELL=100 SQUAREPITCH PITCH=8.0 2 FUELD=4.0 1 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  CUBOID  100 1 4p40.0  2p100.0
  END GEOMETRY
  END DATA
  READ SEARCH  OPTIMUM  CONCENTRATION  MORE
  ALTER  MIX=2  SCNAME=H2O  FACTOR=1.0
  -CON=-0.9  +CON=1.0
  END SEARCH
  END

::

   *******************   search pass  1     keff=  1.63905E+00 + or -  1.69932E-03   ******************
                                       the parameter was  0.00000E+00
     **** xsdrnpm mesh intervals ****
         20 mesh intervals in zone  1
          4 mesh intervals in zone  2
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  1.28883E+00 + or -  1.67697E-03   ******************
                                       the parameter was -9.00000E-01
     **** xsdrnpm mesh intervals ****
         20 mesh intervals in zone  1
         20 mesh intervals in zone  2
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  1.51930E+00 + or -  1.21366E-03   ******************
                                       the parameter was  1.00000E+00
     **** xsdrnpm mesh intervals ****
         20 mesh intervals in zone  1
         20 mesh intervals in zone  2
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  1.61577E+00 + or -  1.47397E-03   ******************
                                       the parameter was  5.00000E-01
  0  **** xsdrnpm mesh intervals ****
         20 mesh intervals in zone  1
         20 mesh intervals in zone  2
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  5     keff=  1.64316E+00 + or -  1.70752E-03   ******************
                                       the parameter was  1.35197E-01
                             10x10x10 array concentration search - change h2o
   ****************************************************************************************************
   ****************************************************************************************************
                     convergence was achieved on pass  5  the parameter was   1.35197E-01
                                 the equation used in the search was:

                    k-eff = +1.63882E+00 +6.77742E-02*p -2.75913E-01*p**2 +8.93705E-02*p**3

              k-effective=  1.64316E+00 + or -  1.70752E-03   the corresponding geometry follows;
                                    10x10x10 array concentration search - change h2o
                                                    mixing table

                                         number of scattering angles =  2
                                     cross section message threshold =5.7E-02

   mixture =     1          density(g/cc) =  19.050
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   1092235  4.39277E-02  9.00000E-01  92235  235.0441  92u 235 bnl evalapr77 m.r.bhat mod3 02/28/89
   1092238  4.81921E-03  1.00000E-01  92238  238.0510  92U 238 ANL+ EVALJUN77 E.PENNINGTON MOD3 02/13/92

   mixture =     2          density(g/cc) = 0.56656
   nuclide   atom-dens.    wgt.  frac.    za    awt           nuclide title
   2001001  3.78981E-02  1.11926E-01  1001   1.0077  hydrogen in water 1301/1002    mod1   11/23/92
   2008016  1.89490E-02  8.88073E-01  8016  15.9904  8O 16 from version 6 evaluation

   mixture =   100          density(g/cc) =  0.0000
   nuclide   atom-dens.    wgt.  frac.     za      awt           nuclide title
   2001001  0.00000E+00  0.00000E+00   1001    1.0077  hydrogen in water 1301/1002 mod1   11/23/92
   2008016  0.00000E+00  0.00000E+00   8016   15.9904  8O 16 from version 6 evaluation
   1092235  0.00000E+00  0.00000E+00  92235  235.0441  92u 235 bnl evalapr77 m.r.bhat  mod3 02/28/89
   1092238  0.00000E+00  0.00000E+00  92238  238.0510  92U 238 ANL+ EVALJUN77 E.PENNINGTON MOD3 02/13/92



           based on the preceding data, the best estimate of the parameter is    1.31179E-01

                       the mixing table corresponding to this parameter follows:
                           10x10x10 array concentration search - change h2o
                                         mixing table
                                   number of scattering angles =  2
                               cross section message threshold =5.7E-02

   mixture =     1          density(g/cc) =  19.050
   nuclide   atom-dens.    wgt.  frac.     za     awt             nuclide title
   1092235  4.39277E-02  9.00000E-01  92235  235.0441  92u 235 bnl evalapr77 m.r.bhat mod3 02/28/89
   1092238  4.81921E-03  1.00000E-01  92238  238.0510  92U 238 ANL+ EVALJUN77 E.PENNINGTON MOD3 02/13/92

   mixture =     2          density(g/cc) = 0.56455
   nuclide   atom-dens.    wgt.  frac.    za     awt            nuclide title
   2001001  3.77639E-02  1.11927E-01  1001   1.0077  hydrogen in water 1301/1002    mod1   11/23/92
   2008016  1.88820E-02  8.88074E-01  8016  15.9904  8O 16 from version 6 evaluation

   mixture =   100          density(g/cc) =  0.0000
   nuclide   atom-dens.    wgt.  frac.     za      awt            nuclide title
   2001001  0.00000E+00  0.00000E+00   1001    1.0077  hydrogen in water 1301/1002 mod 11/23/92
   2008016  0.00000E+00  0.00000E+00   8016   15.9904  8O 16 from version 6 evaluation
   1092235  0.00000E+00  0.00000E+00  92235  235.0441  92u 235 bnl evalapr77 m.r.bhat mod3 02/28/89
   1092238  0.00000E+00  0.00000E+00  92238  238.0510  92U 238 ANL+ EVALJUN77 E.PENNINGTON A.  MOD3 02/13/92
   ****************************************************************************************************
   ****************************************************************************************************

Minimum concentration search
----------------------------

A minimum concentration search searches for the standard composition
density that yields the lowest value of *k*\ :sub:`eff`. A minimum
concentration search is activated by entering “MINIMUM CONCENTRATION” in
the search data. There are no defaulted search data in a concentration
search. The user must specify the material and standard composition name
to be changed and the manner in which they will be changed as described
in the auxiliary search commands.

A concentration search is performed by altering the atom densities of
the specified standard compositions in the specified materials. The
ratio of how the standard compositions change relative to each other is
controlled using FACTOR. If a material and standard composition is not
listed in the search data it remains unchanged. The concentration search
can vary from zero to some upper limit. The code will prevent the
concentration from falling below zero, but the user is responsible for
setting constraints that prevent the concentration from exceeding
reasonable values. In most cases the theoretical density is a reasonable
upper limit.

Infinite Array of Fuel Bundles Separated by Flux Traps — Search on H\ :sub:`2`\ O Density in Trap
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The fuel bundles in this problem represent 17 × 17 PWR fuel assemblies.
The fuel pins are smeared together, making a mixture 100. The fuel pins
consist of 2.35 wt % :sup:`235`\ U having a diameter of 0.823 cm,
zirconium cladding having an outer diameter of 0.9627 cm, and a pitch of
1.275 cm. The fuel bundle is represented as a 10.8375 cm × 10.8375 cm ×
366 cm cuboid of mixture 100 surrounded by Boral and then water. The
Boral has a density of 2.65 g/cm\ :sup:`3` and is composed of 35.17 wt %
B\ :sub:`4`\ C and 64.83 wt % Al. The fuel bundles are at a fixed pitch
of 13.0 cm. This is the same problem as described for a minimum
dimension search above with the water component of the trap size
optimized, thus producing a minimum system *k*\ :sub:`eff`. The input data and
the final search results for this problem follow:

::

  =csas5s
  array of fuel bundles with flux trap
  v7-238
  read comp
  uo2    1 .84 300.  92235 2.35 92238 97.65 end
  zr     2 1 end
  h2o    3 1 end
  b4c    4 den=2.65 0.3517 end
  al     4 den=2.65 0.6483 end
  h2o    5 0.5 end
  end comp
  read celldata
  latticecell squarepitch pitch=1.275 3 fueld=0.823 1 cladd=0.9627 2 cellmix=100 end
  end celldata
  read param far=yes gen=203 npg=1000 end param
  read geom
  cuboid 100 1 4p10.8375 2p183.0
  cuboid   4 1 4p11.0    2p183.0
  cuboid   5 1 4p13.0    2p183.0
  end geom
  read bounds xfc=mirror yfc=mirror end bounds
  end data
  read search  minimum concentration  more
  alter mix=5  scname=h2o  factor=1.0
  -con=-0.9  +con=1.0
  end search
  end

::

   *******************   search pass  1     keff=  7.70310E-01 + or -  1.31009E-03   ******************
                                       the parameter was  0.00000E+00
     **** xsdrnpm mesh intervals ****
        4 mesh intervals in zone  1
        4 mesh intervals in zone  2
       14 mesh intervals in zone  3
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  8.62695E-01 + or -  1.43366E-03   ******************
                                       the parameter was -9.00000E-01
     **** xsdrnpm mesh intervals ****
        4 mesh intervals in zone  1
        4 mesh intervals in zone  2
       14 mesh intervals in zone  3
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  7.04284E-01 + or -  1.44875E-03   ******************
                                       the parameter was  1.00000E+00
     **** xsdrnpm mesh intervals ****
        4 mesh intervals in zone  1
        4 mesh intervals in zone  2
       14 mesh intervals in zone  3
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  7.36291E-01 + or -  1.54213E-03   ******************
                                       the parameter was  5.00000E-01
                                   array of fuel bundles with flux trap
   ****************************************************************************************************
   ****************************************************************************************************
                    convergence was achieved on pass  3  the parameter was   1.00000E+00
                                 the equation used in the search was:

                   k-eff = +7.70310E-01 -7.54970E-02*p +2.03650E-02*p**2 -1.08939E-02*p**3

            k-effective=  7.04284E-01 + or -  1.44875E-03   the corresponding geometry follows;
                               array of fuel bundles with flux trap
                                           mixing table

                                   number of scattering angles =  2
                                cross section message threshold =5.7E-02

   mixture =     1          density(g/cc) =  9.2064
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   1008016  4.10743E-02  1.18465E-01   8016   15.9904  8O 16 from version 6 evaluation
   1092235  4.88650E-04  2.07161E-02  92235  235.0441  92u 235 bnl evalapr77 m.r.bhat mod3 02/28/89
   1092238  2.00485E-02  8.60819E-01  92238  238.0510  92U 238 ANL+ EVALJUN77 E.PENNINGTON MOD3 02/13/92

   mixture =     2          density(g/cc) =  6.4900
   nuclide   atom-dens.    wgt.  frac.     za     awt           nuclide title
   2040000  4.28457E-02  1.00000E+00  40000   91.2196  40zr sai evalapr76 m.drake d.sa  mod2 01/03/89

   mixture =     3          density(g/cc) = 0.99817
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   3001001  6.67692E-02  1.11927E-01   1001    1.0077   hydrogen in water 1301/1002  mod1 11/23/92
   3008016  3.33846E-02  8.88074E-01   8016   15.9904   8O 16 from version 6 evaluation

   mixture =     4          density(g/cc) =  2.6500
   nuclide   atom-dens.    wgt.  frac.      za     awt               nuclide title
   4005010  8.08716E-03  5.07413E-02   5010  10.0130  5b 100lasl evaldec76 g.hale mod1 12/11/92 free gas
   4005011  3.25519E-02  2.24568E-01   5011  11.0096  5b11 gebnl evalsep71 cowan mod1 12/11/92 free gas
   4006012  1.01598E-02  7.63956E-02   6000  12.0001  6c ornl evaldec73 c.y.fu mod2 12/11/92 free gas
   4013027  3.83444E-02  6.48295E-01  13027  26.9818   13al 270lasl evaldec73 p.g.  young mod1 11/29/88

   mixture =     5          density(g/cc) = 0.99817
   nuclide   atom-dens.    wgt.  frac.     za    awt               nuclide title
   5001001  6.67692E-02  1.11927E-01   1001   1.0077   hydrogen in water 1301/1002  mod1   11/23/92
   5008016  3.33846E-02  8.88074E-01   8016  15.9904   8O 16 from version 6 evaluation

   mixture =   100          density(g/cc) =  0.0000
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   3001001  0.00000E+00  0.00000E+00   1001    1.0077  hydrogen in water 1301/1002    mod1   11/23/92
   3008016  0.00000E+00  0.00000E+00   8016   15.9904  8O 16 from version 6 evaluation
   1008016  0.00000E+00  0.00000E+00   8016   15.9904  8O 16 from version 6 evaluation
   2040000  0.00000E+00  0.00000E+00  40000   91.2196  40zr sai evalapr76 m.drake d.sa  mod2 01/03/89
   1092235  0.00000E+00  0.00000E+00  92235  235.0441  92u 235 bnl evalapr77 m.r.bhat  mod3 02/28/89
   1092238  0.00000E+00  0.00000E+00  92238  238.0510  92U 238 ANL+ EVALJUN77 E.PENNINGTON MOD3 02/13/92

Critical concentration search
-----------------------------

A critical concentration search alters the concentration of the
specified standard composition in the specified mixture to obtain a
specified value of *k*\ :sub:`eff`. A critical concentration search is
activated by entering “CRITICAL CONCENTRATION” in the search data. There
are no defaulted search data in a critical concentration search except
for the value of *k*\ :sub:`eff`. If something other than *k*\ :sub:`eff` = 1.0 is
desired the user must specify KEF=**, where \*\* is the desired value of
*k*\ :sub:`eff`. The remaining data is entered after the keyword MORE in the
search data block. The user must specify the material and standard
composition name to be changed and the manner in which they will be
changed as described in the auxiliary search commands.

A concentration search is performed by altering the atom densities of
the specified standard compositions in the specified materials. The
ratio of how the standard compositions change relative to each other is
controlled using FACTOR. If a material and standard composition is not
listed in the search data it remains unchanged. The concentration search
can vary from zero to some upper limit. The code will prevent the
concentration from falling below zero, but the user is responsible for
setting constraints that prevent the concentration from exceeding
reasonable values. In most cases the theoretical density is a reasonable
upper limit.

Array of Spheres in H\ :sub:`2`\ O — Search on H\ :sub:`2`\ O Density
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider a 10 × 10 × 10 array of uranium spheres arranged in an array
having a “square” pitch. The uranium spheres are 2 cm in radius, and the
center-to-center spacing is 8 cm. The uranium spheres and their
associated spacing are defined to be unit 1, and the 10 × 10 × 10 array
is defined to be array 1.0 cm. The spheres are initially moderated by ½
density water.

A critical concentration search is performed on the water yielding
system *k*\ :sub:`eff` = 1.0 for various densities of water. In the MORE search
data, MIX=2 and SCNAME=H2O specify that the water component of mixture 2
is to be altered during the search from an initial density of 0.5 gm/cc.
The maximum allowed density is full density water (1.0 gm/cc). The
minimum allowed water density is 0.0005 gm/cc.

The maximum constraint is calculated according to:

  +CON= (1.0/0.5 − 1)/1.0 = 1.0

The minimum constraint is calculated according to:

  −CON= (0.0005/0.5 − 1)/1.0 = −0.999

The search data and final search results for this problem follow:

::

  =CSAS5S
  10x10x10 ARRAY - CONCENTRATION SEARCH
  V7-238
  READ COMP
  URANIUM 1 1.0  300.0 92235 90.0 92238 10.0 END
  H2O     2 0.5  300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SPHSQUAREP PITCH=8.0 2 FUELD=4.0 1 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  SPHERE  1 1 2.0
  CUBOID  2 1 6P4.0
  END GEOMETRY
  READ ARRAY
  ARA=1 NUX=10 NUY=10 NUZ=10 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  CRITICAL  CONCENTRATION KEF=1.0  MORE
  ALTER  MIX=2  SCNAME=H2O  factor=1.0
  -CON=-0.999  +CON=1.0
  END SEARCH
  END

::

   *******************   search pass  1     keff=  1.22228E+00 + or -  1.75549E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  4.97499E-01 + or -  1.19161E-03   ******************
                                       the parameter was -9.99000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  1.15356E+00 + or -  1.85214E-03   ******************
                                       the parameter was -3.06377E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  9.72210E-01 + or -  1.89881E-03   ******************
                                       the parameter was -5.52436E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  5     keff=  1.00805E+00 + or -  1.91023E-03   ******************
                                       the parameter was -5.21036E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  6     keff=  1.00056E+00 + or -  2.05463E-03   ******************
                                  the parameter was -5.28450E-01
                              10x10x10 array - concentration search
   ****************************************************************************************************
   ****************************************************************************************************
                   convergence was achieved on pass  6  the parameter was  -5.28450E-01
                                 the equation used in the search was:

                 k-eff = +1.19891E+00 -5.90957E-01*p -2.41575E+00*p**2 -1.11098E+00*p**3

           k-effective=  1.00056E+00 + or -  2.05463E-03   the corresponding geometry follows;
                                      10x10x10 array - concentration search
                                                mixing table

                                          number of scattering angles =  2
                                      cross section message threshold =5.7E-02

   mixture =     1          density(g/cc) =  19.050
   nuclide   atom-dens.    wgt.  frac.    za      awt               nuclide title
   1092235  4.39277E-02  9.00000E-01  92235  235.0441  92u 235 bnl evalapr77 m.r.bhat mod3 02/28/89
   1092238  4.81921E-03  1.00000E-01  92238  238.0510  92U 238 ANL+ EVALJUN77 E.PENNINGTON MOD3 02/13/92

   mixture =     2          density(g/cc) = 0.23534
   nuclide   atom-dens.    wgt.  frac.    za      awt               nuclide title
   2001001  1.57425E-02  1.11926E-01  1001    1.0077  hydrogen in water 1301/1002    mod1   11/23/92
   2008016  7.87126E-03  8.88074E-01  8016   15.9904  8O 16 from version 6 evaluation
           based on the preceding data, the best estimate of the parameter is   -5.28963E-01

                          the mixing table corresponding to this parameter follows:
                                10x10x10 array - concentration search
                                             mixing table

                                   number of scattering angles =  2
                               cross section message threshold =5.7E-02

   mixture =     1          density(g/cc) =  19.050
   nuclide   atom-dens.    wgt.  frac.     za      awt               nuclide title
   1092235  4.39277E-02  9.00000E-01  92235  235.0441  92u 235 bnl evalapr77 m.r.bhat mod3 02/28/89
   1092238  4.81921E-03  1.00000E-01  92238  238.0510  92U 238 ANL+ EVALJUN77 E.PENNINGTON MOD3 02/13/92

   mixture =     2          density(g/cc) = 0.23509
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   2001001  1.57254E-02  1.11927E-01   1001    1.0077   hydrogen in water 1301/1002  mod1 11/23/92
   2008016  7.86270E-03  8.88074E-01   8016   15.9904   8O 16 from version 6 evaluation

   ****************************************************************************************************
   ****************************************************************************************************

Array of Spheres in H\ :sub:`2`\ O — Search on H\ :sub:`2`\ O Density
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the same problem as described above with the exception of the
initial water density, which is now 0.25 gm/cc. A critical concentration
search is performed on the water yielding a system *k*\ :sub:`eff` = 1.0 for
various densities of water. In the MORE search data, MIX=2 and
SCNAME=H2O specify that the water component of mixture 2 is to be
altered during the search from an initial value of 0.25 gm/cc. The
maximum allowed density is ½ density water (0.5 gm/cc). The minimum
allowed water density is 0.1 gm/cc.

The maximum constraint is calculated according to:

  +CON= (5.0/0.25 − 1)/1.0 = 1.0

The minimum constraint is calculated according to:

  −CON= (0.1/0.25 − 1)/1.0 = − 0.6

The search data and final search results for this problem follow:

::

  =CSAS5S
  10x10x10 ARRAY - CONCENTRATION SEARCH
  V7-238
  READ COMP
  URANIUM 1 1.0  300.0 92235 90.0 92238 10.0 END
  H2O     2 0.25  300.0 END
  END COMP
  READ CELLDATA
  LATTICECELL SPHSQUAREP PITCH=8.0 2 FUELD=4.0 1 END
  END CELLDATA
  READ GEOMETRY
  UNIT 1
  SPHERE  1 1 2.0
  CUBOID  2 1 6P4.0
  END GEOMETRY
  READ ARRAY
  ARA=1 NUX=10 NUY=10 NUZ=10 FILL F1 END FILL
  END ARRAY
  END DATA
  READ SEARCH  CRITICAL  CONCENTRATION KEF=1.0  MORE
  ALTER  MIX=2  SCNAME=H2O  factor=1.0
  -CON=-0.6  +CON=1.0
  END SEARCH
  END

::

   *******************   search pass  1     keff=  1.02599E+00 + or -  1.98346E-03   ******************
                                       the parameter was  0.00000E+00
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  6.69203E-01 + or -  1.55844E-03   ******************
                                       the parameter was -6.00000E-01
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  1.00197E+00 + or -  1.73659E-03   ******************
                                       the parameter was -4.37073E-02
                                 10x10x10 array - concentration search
   ****************************************************************************************************
   ****************************************************************************************************
                     convergence was achieved on pass  3  the parameter was  -4.37073E-02
                                 the equation used in the search was:

                   k-eff = +0.00000E+00 +0.00000E+00*p +0.00000E+00*p**2 +0.00000E+00*p**3

             k-effective=  1.00197E+00 + or -  1.73659E-03   the corresponding geometry follows;
                                  10x10x10 array - concentration search
                                               mixing table

                                       number of scattering angles =  2
                                   cross section message threshold =5.7E-02

   mixture =     1          density(g/cc) =  19.050
   nuclide   atom-dens.    wgt.  frac.      za      awt               nuclide title
   1092235  4.39277E-02  9.00000E-01  92235  235.0441  92u 235 bnl evalapr77 m.r.bhat  mod3 02/28/89
   1092238  4.81921E-03  1.00000E-01  92238  238.0510  92U 238 ANL+ EVALJUN77 E.PENNINGTON MOD3 02/13/92

   mixture =     2          density(g/cc) = 0.23864
   nuclide   atom-dens.    wgt.  frac.     za    awt               nuclide title
   2001001  1.59627E-02  1.11926E-01   1001   1.0077  hydrogen in water 1301/1002  mod1 11/23/92
   2008016  7.98136E-03  8.88074E-01   8016  15.9904  8O 16 from version 6 evaluation


            based on the preceding data, the best estimate of the parameter is   -4.37073E-02

                         the mixing table corresponding to this parameter follows:
                                    10x10x10 array - concentration search
                                                 mixing table

                                        number of scattering angles =  2
                                    cross section message threshold =5.7E-02

   mixture =     1          density(g/cc) =  19.050
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   1092235  4.39277E-02  9.00000E-01  92235  235.0441  92u 235 bnl evalapr77 m.r.bhat mod3 02/28/89
   1092238  4.81921E-03  1.00000E-01  92238  238.0510  92U 238 ANL+ EVALJUN77 E.PENNINGTON MOD3 02/13/92

   mixture =     2          density(g/cc) = 0.23864
   nuclide   atom-dens.    wgt.  frac.     za      awt               nuclide title
   2001001  1.59627E-02  1.11926E-01   1001    1.0077   hydrogen in water 1301/1002  mod1 11/23/92
   2008016  7.98136E-03  8.88074E-01   8016   15.9904   8O 16 from version 6 evaluation
   ****************************************************************************************************
   ****************************************************************************************************

UO\ :sub:`2`\ F\ :sub:`2` Solution Tank — Critical Search on UO\ :sub:`2`\ F\ :sub:`2` Density
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider a large spherical tank partially filled with
UO\ :sub:`2`\ F\ :sub:`2` solution. The tank has a radius of 34.6 cm and
is filled with solution to a height of 30.0 cm above the midpoint. The
tank is composed of a 0.759 cm thick Al shell. The
UO\ :sub:`2`\ F\ :sub:`2` solution is composed of three standard
compositions: UO2F2, HF acid, and H2O. The code combines these using a
set algorithm. This may or may not produce a solution at the desired
density. If the density of the solution is known it should be entered.
Also, extra acid can be added to the solution by specifying a non-zero
acid molarity.

A critical concentration search is performed on the water yielding
system *k*\ :sub:`eff` = 1.0 for various densities of UO\ :sub:`2`\ F\ :sub:`2`
in the solution. In the MORE search data, MIX=1 and SCNAME=UO2F2 specify
that the UO\ :sub:`2`\ F\ :sub:`2` component of the mixture 1 solution
is to be altered during the search. The code calculates the density of
the solution. The initial uranium fuel density is 300 gm/liter. The
maximum allowed uranium density is 600 gm/liter. The minimum allowed
uranium density is 150 gm/liter.

The maximum constraint is calculated according to:

  +CON= (600/300 − 1)/1.0 = 1.0

The minimum constraint is calculated according to:

  −CON= (150/300 − 1)/1.0 = −0.5

The search data and final search results for this problem follow:

::

  =CSAS5S
  SOLUTION TANK - CRITICAL CONCENTRATION SEARCH
  V7-238
  READ COMP
  SOLNUO2F2  1 300 0 1 300.0 92235 4.89 92238 95.09 92234 0.02 END
  AL         2 1.0 300.0 END
  END COMP
  READ GEOM
  HEMISPHE-Z  1 1 34.6   CHORD 30.
  SPHERE      0 1 34.6
  SPHERE      2 1 34.759
  END GEOM
  END DATA
  READ SEARCH  CRITICAL  CONCENTRATION KEF=1.0  MORE
  ALTER  MIX=1  SCNAME=UO2F2  FACTOR=1.0
  -CON=-0.5  +CON=1.0
  END SEARCH
  END

::

   *******************   search pass  1     keff=  8.31461E-01 + or -  1.14626E-03   ******************
                                       the parameter was  0.00000E+00
                      *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  2     keff=  1.05426E+00 + or -  1.63141E-03   ******************
                                       the parameter was  1.00000E+00
                      *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  1.01773E+00 + or -  1.42881E-03   ******************
                                       the parameter was  7.56451E-01
                      *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  9.97887E-01 + or -  1.42235E-03   ******************
                                       the parameter was  6.59454E-01
                                solution tank - critical concentration search
   ****************************************************************************************************
   ****************************************************************************************************
                    convergence was achieved on pass  4  the parameter was   6.59454E-01
                                 the equation used in the search was:

              k-eff = +8.31461E-01 +2.45656E-01*p +7.41484E-02*p**2 -9.70021E-02*p**3

        k-effective=  9.97887E-01 + or -  1.42235E-03   the corresponding geometry follows;
                            solution tank - critical concentration search
                                               mixing table

                                     number of scattering angles =  2
                                 cross section message threshold =5.7E-02


   mixture =     1          density(g/cc) =  1.5960
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   1001001  6.36618E-02  6.67438E-02   1001    1.0077  hydrogen in water 1301/1002    mod1   11/23/92
   1008016  3.43513E-02  5.71507E-01   8016   15.9904  8O 16 from version 6 evaluation
   1009019  2.52040E-03  4.98199E-02   9019   18.9982  9f 19 ornl evaljul74 c.y.fu d.c.lars mod3
   12/16/88
   1092234  2.56198E-07  6.23860E-05  92234  234.0405  92U234 BNL HEDL+EVALJUL78 DIVADEENAM MOD3
   01/10/91
   1092235  6.23730E-05  1.52534E-02  92235  235.0441  92u 235 bnl evalapr77 m.r.bhat mod3 02/28/89
   1092238  1.19757E-03  2.96614E-01  92238  238.0510  92U 238 ANL+ EVALJUN77 E.PENNINGTON MOD3
   02/13/92

   mixture =     2          density(g/cc) =  2.7020
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   2013027  6.03066E-02  1.00000E+00  13027  26.9818  13al 270lasl evaldec73 p.g.  young d.g mod1
   11/29/88

               based on the preceding data, the best estimate of the parameter is    6.69249E-01

                         the mixing table corresponding to this parameter follows:
                              solution tank - critical concentration search
                                                mixing table

                                    number of scattering angles =  2
                                cross section message threshold =5.7E-02

  mixture =     1          density(g/cc) =  1.5998
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   1001001  6.36618E-02  6.65852E-02   1001    1.0077  hydrogen in water 1301/1002   mod1  11/23/92
   1008016  3.43662E-02  5.70395E-01   8016   15.9904  8O 16 from version 6 evaluation
   1009019  2.53528E-03  4.99948E-02   9019   18.9982  9f 19 ornl evaljul74 c.y.fu d.c.lars mod3
   12/16/88
   1092234  2.57710E-07  6.26050E-05  92234  234.0405  92U 234 BNL HEDL+EVALJUL78 DIVADEENAM MOD3
   01/10/91
   1092235  6.27412E-05  1.53069E-02  92235  235.0441  92u 235 bnl evalapr77 m.r.bhat mod3 02/28/89
   1092238  1.20464E-03  2.97655E-01  92238  238.0510  92U 238 ANL+ EVALJUN77 E.PENNINGTON MOD3
   02/13/92

   mixture =     2          density(g/cc) =  2.7020
   nuclide   atom-dens.    wgt.  frac.      za      awt               nuclide title
   2013027  6.03066E-02  1.00000E+00  13027   26.9818  13al 270lasl evaldec73 p.g.  young d.g mod1
   11/29/88

   ****************************************************************************************************
   ****************************************************************************************************

The final solution for this search contains 500 gm/liter of uranium. The
search, however, did not change the amount of acid or water in the
solution. To get a better estimation of the solution density and
*k*\ :sub:`eff` for this concentration of uranium the problem should be run
again with an initial uranium density of 500 gm/liter as shown below.

UO\ :sub:`2`\ F\ :sub:`2` Solution Tank — Critical Search on UO\ :sub:`2`\ F\ :sub:`2` Density, Check
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the same UO\ :sub:`2`\ F\ :sub:`2` solution tank problem
examined above except the initial uranium density is 500 gm/liter. This
problem is run again so the code will calculate water and acid densities
associated with this density of uranium. The search data has also been
modified to account for the new density of uranium.

A critical concentration search is performed on the water yielding
system *k*\ :sub:`eff` = 1.0 for various densities of UO\ :sub:`2`\ F\ :sub:`2`
in the solution. In the MORE search data, MIX=1 and SCNAME=UO2F2 specify
that the UO\ :sub:`2`\ F\ :sub:`2` component of the mixture 1 solution
is to be altered during the search. The code calculates the density of
the solution. The initial uranium fuel density is 500 gm/liter. The
maximum allowed uranium density is 600 gm/liter. The minimum allowed
uranium density is 400 gm/liter.

The maximum constraint is calculated according to:

  +CON= (600/500 − 1)/1.0 = 0.2

The minimum constraint is calculated according to:

  −CON= (400/500 − 1)/1.0 = −0.2

The search data and final search results for this problem follow:

::

  =csas5s
  solution tank - critical concentration search
  v7-238
  read comp
  solnuo2f2  1 500 0 1 300.0 92235 4.89 92238 95.09 92234 0.02 end
  al         2 1.0 300.0 end
  end comp
  read geom
  hemisphe-z  1 1 34.6   chord 30.
  sphere      0 1 34.6
  sphere      2 1 34.759
  end geom
  end data
  READ SEARCH  CRITICAL  CONCENTRATION KEF=1.0  MORE
  ALTER  MIX=1  SCNAME=uo2f2  factor=1.0
  -CON=-0.2  +CON=0.2
  END SEARCH
  end

::

   *******************   search pass  1     keff=  9.99662E-01 + or -  1.40567E-03   ******************
                                       the parameter was  0.00000E+00
                               solution tank - critical concentration search
  ****************************************************************************************************
                  convergence was achieved on pass  1  the parameter was   0.00000E+00

                                 the equation used in the search was:

                k-eff = +0.00000E+00 +0.00000E+00*p +0.00000E+00*p**2 +0.00000E+00*p**3

           k-effective=  9.99662E-01 + or -  1.40567E-03   the corresponding geometry follows;
                            solution tank - critical concentration search
                                              mixing table

                                     number of scattering angles =  2
                               cross section message threshold =5.7E-02

   mixture =     1          density(g/cc) =  1.5656
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   1001001  6.14448E-02  6.56680E-02   1001    1.0077  hydrogen in water 1301/1002  mod1 11/23/92
   1008016  3.32538E-02  5.63969E-01   8016   15.9904  8O 16 from version 6 evaluation
   1009019  2.53136E-03  5.10061E-02   9019   18.9982  9f 19 ornl evaljul74 c.y.fu d.c.lars
   mod312/16/88
   1092234  2.57312E-07  6.38714E-05  92234  234.0405  92U 234 BNL HEDL+EVALJUL78 DIVADEENAMMOD3
   01/10/91
   1092235  6.26441E-05  1.56166E-02  92235  235.0441  92u 235 bnl evalapr77 m.r.bhat mod3 02/28/89
   1092238  1.20278E-03  3.03676E-01  92238  238.0510  92U 238 ANL+ EVALJUN77 E.PENNINGTON MOD3
   02/13/92

   mixture =     2          density(g/cc) =  2.7020
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   2013027  6.03066E-02  1.00000E+00  13027   26.9818  13al 270lasl evaldec73 p.g.  young d.g mod1
   11/29/88

              based on the preceding data, the best estimate of the parameter is    0.00000E+00

                        the mixing table corresponding to this parameter follows:
                              solution tank - critical concentration search
                                            mixing table

                                 number of scattering angles =  2
                             cross section message threshold =5.7E-02

   mixture =     1          density(g/cc) =  1.5656
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   1001001  6.14448E-02  6.56680E-02   1001    1.0077  hydrogen in water 1301/1002  mod1 11/23/92
   1008016  3.32538E-02  5.63969E-01   8016   15.9904  8O 16 from version 6 evaluation
   1009019  2.53136E-03  5.10061E-02   9019   18.9982  9f 19 ornl evaljul74 c.y.fu d.c.lars mod3
   12/16/88
   1092234  2.57312E-07  6.38714E-05  92234  234.0405  92U 234 BNL HEDL+EVALJUL78 DIVADEENAM MOD3
   01/10/91
   1092235  6.26441E-05  1.56166E-02  92235  235.0441  92u 235 bnl evalapr77 m.r.bhat mod3 02/28/89
   1092238  1.20278E-03  3.03676E-01  92238  238.0510  92U 238 ANL+ EVALJUN77 E.PENNINGTON MOD3
   02/13/92

   mixture =     2          density(g/cc) =  2.7020
   nuclide   atom-dens.    wgt.  frac.     za      awt               nuclide title
   2013027  6.03066E-02  1.00000E+00  13027   26.9818  13al 270lasl evaldec73 p.g.  young d.g mod1
   11/29/88

  ****************************************************************************************************

This problem converged on the first pass, so the amount of uranium, HF
acid, and water in the solution were reasonably good estimates. For this
problem the HF acid and H\ :sub:`2`\ O only changed marginally and,
therefore, had very little effect on the system *k*\ :sub:`eff`. This is not
always the case; therefore if a search is being done on a solution, the
problem should always be rerun with the final search densities.

Fuel Bundles Separated by Flux Traps — Critical Search Boron and Al Densities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The fuel bundles in this problem represent 17 × 17 PWR fuel assemblies.
The fuel pins are smeared together, making a mixture 100. The fuel pins
consist of 4.35 wt % :sup:`235`\ U having a diameter of 0.823 cm,
zirconium cladding having an outer diameter of 0.9627 cm, and a pitch of
1.275 cm. The fuel bundle is represented as a 10.8375 cm × 10.8375 cm ×
366 cm cuboid of mixture 100 surrounded by Boral and then water. The
Boral has a density of 2.61 g/cm\ :sup:`3` and has an initial composed
of 50.0 wt % B\ :sub:`4`\ C and 50.0 wt % Al. The fuel bundles are at a
fixed pitch of 13.0 cm. Boral plates surrounding the X and Y sides of
each fuel assembly are 0.1625 cm thick. Full density water is between
the Boral plates.

A critical concentration search is performed on the Boral plates
searching for a system *k*\ :sub:`eff` = 0.95. The Boral plates are at a fixed
density of 2.61 gm/cc. As the density of the B\ :sub:`4`\ C changes, the
density of the Al changes in the opposite direction maintaining a
constant Boral density. There are two entries in the MORE search data.
The first entry, MIX=4 SCNAME=b4c factor=1.0 specifies that the
B\ :sub:`4`\ C of mixture 4 is to be altered during the search. The
second entry, MIX=4 SCNAME=al factor = −1.0 specifies that aluminum is
to be changed in the opposite direction and proportionally to
B\ :sub:`4`\ C during the search. Both B\ :sub:`4`\ C and Al have the
same initial density of 0.5 \* 2.61 = 1.305 gm/cc.

The maximum constraint is calculated according to:

  +CON= (2.59695/1.305 − 1)/1.0 = 0.99

The minimum constraint is calculated according to:

  −CON= (0.1305/1.305 − 1)/1.0 = −0.9

The search data and final search results for this problem follow:

::

  =csas5s
  array of fuel bundles with flux trap
  v7-238
  read comp
  uo2    1 .84 300.  92235 4.35 92238 95.65 end
  zr     2 1 end
  h2o    3 1 end
  b4c    4 den=2.61  0.5  end
  al     4 den=2.61 0.5 end
  h2o    5 1.0 end
  end comp
  read celldata
  latticecell squarepitch  pitch=1.275 3 fueld=0.823 1 cladd=0.9627 2 cellmix=100 end
  end celldata
  read param far=yes gen=203 npg=1000 end param
  read geom
  global unit 1
  cuboid 100 1 4p10.8375 2p183.0
  cuboid   4 1 4p11.0    2p183.0
  cuboid   5 1 4p13.0    2p183.0
  end geom
  read bounds xfc=mirror yfc=mirror end bounds
  end data
  read search  critical concentration  kef=0.95 more
  alter mix=4  scname=arbmb4c   factor=1.0
  alter mix=4  scname=al        factor=-1.0
  -con=-0.9  +con=0.99
  end search
  end

::

  =csas5s
  array of fuel bundles with flux trap
  v7-238
  read comp
  uo2    1 .84 300.  92235 4.35 92238 95.65 end
  zr     2 1 end
  h2o    3 1 end
  b4c    4 den=2.61  0.5  end
  al     4 den=2.61 0.5 end
  h2o    5 1.0 end
  end comp
  read celldata
  latticecell squarepitch  pitch=1.275 3 fueld=0.823 1 cladd=0.9627 2 cellmix=100 end
  end celldata
  read param far=yes gen=203 npg=1000 end param
  read geom
  global unit 1
  cuboid 100 1 4p10.8375 2p183.0
  cuboid   4 1 4p11.0    2p183.0
  cuboid   5 1 4p13.0    2p183.0
  end geom
  read bounds xfc=mirror yfc=mirror end bounds
  end data
  read search  critical concentration  kef=0.95 more
  alter mix=4  scname=arbmb4c   factor=1.0
  alter mix=4  scname=al        factor=-1.0
  -con=-0.9  +con=0.99
  end search
  end

   *******************   search pass  1     keff=  8.22991E-01 + or -  1.79474E-03   ******************
                                       the parameter was  0.00000E+00
      **** xsdrnpm mesh intervals ****
      4 mesh intervals in zone  1
      4 mesh intervals in zone  2
     14 mesh intervals in zone  3
                       *****  modified keno v data has been rewritten on unit 95  *****
    *******************   search pass  2     keff=  8.01629E-01 + or -  1.78327E-03   ******************
                                       the parameter was  9.90000E-01
      **** xsdrnpm mesh intervals ****
      4 mesh intervals in zone  1
      4 mesh intervals in zone  2
     14 mesh intervals in zone  3
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  3     keff=  9.82092E-01 + or -  1.63305E-03   ******************
                                       the parameter was -9.00000E-01
      **** xsdrnpm mesh intervals ****
      4 mesh intervals in zone  1
      4 mesh intervals in zone  2
     14 mesh intervals in zone  3
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  4     keff=  9.01534E-01 + or -  1.74845E-03   ******************
                                       the parameter was -7.66111E-01
      **** xsdrnpm mesh intervals ****
      4 mesh intervals in zone  1
      4 mesh intervals in zone  2
     14 mesh intervals in zone  3
                      *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  5     keff=  9.38557E-01 + or -  1.59285E-03   ******************
                                       the parameter was -8.52032E-01
      **** xsdrnpm mesh intervals ****
      4 mesh intervals in zone  1
      4 mesh intervals in zone  2
     14 mesh intervals in zone  3
                     *****  modified keno v data has been rewritten on unit 95  *****
   *******************   search pass  6     keff=  9.48930E-01 + or -  1.69920E-03   ******************
                                       the parameter was -8.65663E-01
                                   array of fuel bundles with flux trap
   ****************************************************************************************************
   ****************************************************************************************************
                     convergence was achieved on pass  6  the parameter was  -8.65663E-01
                                 the equation used in the search was:

                  k-eff = +8.66738E-01 +2.74121E-01*p +5.80563E-02*p**2 -4.25484E-01*p**3

          k-effective=  9.48930E-01 + or -  1.69920E-03   the corresponding geometry follows;
                               array of fuel bundles with flux trap
                                         mixing table

                              number of scattering angles =  2
                          cross section message threshold =5.7E-02

   mixture =     1          density(g/cc) =  9.2064
   nuclide   atom-dens.    wgt.  frac.     za    awt               nuclide title
   1008016  4.10835E-02  1.18491E-01   8016  15.9904  8O 16 from version 6 evaluation
   1092235  9.04496E-04  3.83457E-02  92235 235.0441  92u 235 bnl evalapr77 m.r.bhat  mod3 02/28/89
   1092238  1.96373E-02  8.43163E-01  92238 238.0510  92U 238 ANL+EVALJUN77 E.PENNINGTON MOD3 02/13/92

   mixture =     2          density(g/cc) =  6.4900
   nuclide   atom-dens.    wgt.  frac.     za    awt               nuclide title
   2040000  4.28457E-02  1.00000E+00  40000  91.2196  40zr sai evalapr76 m.drake d.sa  mod2 01/03/89

   mixture =     3          density(g/cc) = 0.99817
   nuclide   atom-dens.    wgt.  frac.     za    awt               nuclide title
   3001001  6.67692E-02  1.11927E-01   1001   1.0077  hydrogen in water 1301/1002    mod1   11/23/92
   3008016  3.33846E-02  8.88074E-01   8016  15.9904  8O 16 from version 6 evaluation

   mixture =     4          density(g/cc) =  2.6100
   nuclide   atom-dens.    wgt.  frac.    za     awt               nuclide title
   4005010  1.52119E-03  9.69077E-03  5010  10.0130   5b100lasl evaldec76 g.hale l.stewart mod1  12/11/92
   4005011  6.12300E-03  4.28888E-02  5011  11.0096 5b11 gebnl evalsep71 c.cowan mod1 12/11/92 free  gas
   4006012  1.91105E-03  1.45903E-02  6000  12.0001 6cornl evaldec73 c.y.fu and f.g.  perey mod2 12/11/92
   4013027  5.43405E-02  9.32830E-01 13027  26.9818 13al270lasl evaldec73 p.g.  young d.g mod1 11/29/88

   mixture =     5          density(g/cc) = 0.99817
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   5001001  6.67692E-02  1.11927E-01   1001    1.0077  hydrogen in water 1301/1002  mod1 11/23/92
   5008016  3.33846E-02  8.88074E-01   8016   15.9904  8O 16 from version 6 evaluation

   mixture =   100          density(g/cc) =  0.0000
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   3001001  0.00000E+00  0.00000E+00   1001    1.0077  hydrogen in water 1301/1002  mod1 11/23/92
   3008016  0.00000E+00  0.00000E+00   8016   15.9904  8O 16 from version 6 evaluation
   1008016  0.00000E+00  0.00000E+00   8016   15.9904  8O 16 from version 6 evaluation
   2040000  0.00000E+00  0.00000E+00  40000   91.2196  40zr sai evalapr76 m.drake d.sa mod2 01/03/89
   1092235  0.00000E+00  0.00000E+00  92235  235.0441  92u 235 bnl evalapr77 m.r.bhat  mod3 02/28/89
   1092238  0.00000E+00  0.00000E+00  92238  238.0510  92U 238 ANL+ EVALJUN77 E.PENNINGTON MOD3
   02/13/92


       based on the preceding data, the best estimate of the parameter is   -8.66988E-01
                      the mixing table corresponding to this parameter follows:
                            array of fuel bundles with flux trap
                                   mixing table

                          number of scattering angles =  2
                       cross section message threshold =5.7E-02

   mixture =     1          density(g/cc) =  9.2064
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   1008016  4.10835E-02  1.18491E-01   8016   15.9904  8O 16 from version 6 evaluation
   1092235  9.04496E-04  3.83457E-02  92235  235.0441  92u 235 bnl evalapr77 m.r.bhat  mod3 02/28/89
   1092238  1.96373E-02  8.43163E-01  92238  238.0510  92U 238 ANL+EVALJUN77 E.PENNINGTON MOD3 02/13/92

   mixture =     2          density(g/cc) =  6.4900
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   2040000  4.28457E-02  1.00000E+00  40000   91.2196  40zr sai evalapr76 m.drake d.sa mod2 01/03/89

   mixture =     3          density(g/cc) = 0.99817
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   3001001  6.67692E-02  1.11927E-01   1001    1.0077  hydrogen in water 1301/1002    mod1   11/23/92
   3008016  3.33846E-02  8.88074E-01   8016   15.9904  8O 16 from version 6 evaluation

   mixture =     4          density(g/cc) =  2.6100
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   4005010  1.50619E-03  9.59518E-03   5010   10.0130 5b 100lasl evaldec76 g.hale l.stewart mod1 12/11/92
   4005011  6.06261E-03  4.24657E-02   5011   11.0096 5b11 gebnl evalsep71 c.cowan mod1 12/11/92 free gas
   4006012  1.89220E-03  1.44464E-02   6000   12.0001 6c ornl evaldec73 c.y.fu and f.g.  perey mod2 12/11/92
   4013027  5.43791E-02  9.33493E-01  13027   26.9818  13al 270lasl evaldec73 p.g.  young d.g mod1 11/29/88

   mixture =     5          density(g/cc) = 0.99817
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   5001001  6.67692E-02  1.11927E-01   1001    1.0077  hydrogen in water 1301/1002    mod1   11/23/92
   5008016  3.33846E-02  8.88074E-01   8016   15.9904  8O 16 from version 6 evaluation

   mixture =   100          density(g/cc) =  0.0000
   nuclide   atom-dens.    wgt.  frac.     za     awt               nuclide title
   3001001  0.00000E+00  0.00000E+00   1001    1.0077  hydrogen in water 1301/1002    mod1   11/23/92
   3008016  0.00000E+00  0.00000E+00   8016   15.9904  8O 16 from version 6 evaluation
   1008016  0.00000E+00  0.00000E+00    8016  15.9904  8O 16 from version 6 evaluation
   2040000  0.00000E+00  0.00000E+00   40000  91.2196  40zr sai evalapr76 m.drake d.sa mod2 01/03/89
   1092235  0.00000E+00  0.00000E+00   92235  235.0441  92u 235 bnl evalapr77 m.r.bhat  mod3 02/28/89
   1092238  0.00000E+00  0.00000E+00   92238  238.0510  92U 238 ANL+ EVALJUN77 E.PENNINGTON MOD3 02/13/92

  *******************************************************************************************************
  *******************************************************************************************************
