.. _11-6:

MALOCS2: Module To Collapse AMPX Master Cross Section libraries
===============================================================

*L.M. Petrie*

.. _11-6-1:

Introduction
------------

MALOCS2 (**M**\ iniature **A**\ MPX **L**\ ibrary **O**\ f **C**\ ross
**S**\ ections) is a module to collapse AMPX master cross-section
libraries. The SCALE MALOCS2 module is an extension of the AMPX module
MALOCS. MALOCS2 provides capability to read the collapsing spectrum from
the output flux file produced by XSDRNPM, and also has extended options
for collapsing Legendre moments of the 2D elastic scattering matrix. The
module can be used to collapse neutron, gamma-ray, or coupled
neutron-gamma master libraries.

.. _11-6-2:

MALOCS Input Data
-----------------

.. describe:: broadfilename

  filename of the collapsed library [no default]

.. describe:: crosssectionprint

  cross section printing option [none]

  none - don't print any cross sections

  onedxsecs - print the 1D cross sections

  twodxsecs N - print the 2D cross sections through Legendre order N

.. describe:: epsilon

  epsilon for when to print invalid moment messages[0.05]

.. describe:: finefilename

  filename of the input library [no default]

.. describe:: fluxfilename

  filename of an xsdrn flux file to be used in the collapse
  [no default]

.. describe:: numgammagroups

  the number of fine gamma groups [no default]

.. describe:: gammacollapse

  the broad group by fine group collapse structure for the
  gammas

  must come after "numgammagroups"

.. describe:: latticezones

  identifies the zones to be used as fuel, gap, clad, and
  moderator [1,2,3,4]

.. describe:: max2dweightorder

  maximum Legendre order to be collapsed [max Legendre
  order of the nuclide]

.. describe:: numneutrongroups

  the number of fine neutron groups [no default]

.. describe:: neutroncollapse

  the broad group by fine group collapse structure for the
  neutrons

  must come after "numneutrongroups"

.. describe:: printepsilon

  not used [2.0D-6]

.. describe:: problemfilename

  filename of the xsdrn data file that corresponds to the
  flux file [no default]

.. describe:: sigmatotalpl

  flag to turn on doing a within group correction using the
  Pl weighted sigma total

  'y' or 'yes' is true, anything else is false [true]

.. describe:: updatechi

  flag to turn on updating the total chi

  'y' or 'yes' is true, anything else is false [true]

.. describe:: validate2ds

  flag to validate the Legendre moments of the collapsed 2D
  cross sections

  'y' or 'yes' is true, anything else is false [true]

.. describe:: weighttype

  type of weighting to be done

  innercell - cell weight over a subset of the zones

  innercell is followed by the largest zone number in the innercell

  cell - cell weight over the whole cell

  zone - weight each zone independently

  region - cell weight each nuclide over only the zones it is in

  default is region

.. describe:: wgtsource

  source of the weighting flux

  nuclideflux - use the flux from the nuclide on the fine group library

  inputflux - read a flux from input

  [default is to use an xsdrn flux]

.. describe:: end

  terminates input stream

.. _11-6-3:

MALOCS Example Problem
----------------------

The following problem shortens the 56 group library to just the nuclides
that will be used to run a fixed source, 1-D discrete ordinates
calculation of a void sphere with a neutron source in it, surrounded by
a sphere of water, and then surrounded by an iron sphere. The flux from
the discrete ordinates problem is then used to collapse the short
library to 14 groups using a zone collapse method. Finally, the
collapsed library is listed showing the nuclides on it, and copied back
to the input directory.

.. code:: scale
  :class: long

  =shell
    ln -s ${DATA}/scale.rev04.xn56v7.1 ft51f001
  end
  =ajax
    0$$ 52 e
    1$$ 1  1t
    2$$ 51 8  2t
    3$$ 1001 1002 8016 8017 26054 26056 26057 26058 3t
  end
  =csas1   parm=bonami
  generate a flx file to be used to collapse a library
  v7-56n
  read composition
    iron  1 1.0 293.0  end iron
    water 2 1.0 293.0  end water
  end composition
  read celldata
    multiregion spherical end
    0 1.0  2 10.0  1 15.0  end zone
    moredata
      ievt=0 iqm=1 ntd=61 fwr=62 source(1)=15
      0.2 0.2 0.2 0.5 0.5 0.5 0.5 0.5 0.5 0.2 0.2 0.2 0.05 0.05 0.05
    end moredata
  end celldata
  end
  =malocs2
  ' the input fine group cross section library to be collapsed
    finefilename=ft52f001
  ' the output collapsed cross section library
    broadfilename=ft53f001
  ' the file with the fluxes from xsdrn to be used to collapse the XSs
    fluxfilename=ft62f001
  ' the file containing the description of the xsdrn problem
    problemfilename=ft61f001
  ' number of fine neutron groups
    numneutrongroups=56
  ' fine group to broad group correspondence array
    neutroncollapse
    4r1 4r2 4r3 4r4 4r5 4r6 4r7 4r8 4r9 4r10 4r11 4r12 4r13 4r14
  ' type of weighting to be used in doing the collapse
    weighttype=zone
    end
  end
  =paleale
    0$$ 53 e 1$$ 0 1t
  end
  =shell
    cp ft53f001 ${OUTDIR}
  end
