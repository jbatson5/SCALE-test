.. _6-1a:

XSDRNPM Data File Formats
=========================

As part of the development of the sensitivity capabilities in SCALE, the
XSDRNPM module was modified to allow the writing of a new interface file
containing information needed for sensitivity calculations.  This same data
file is used by TSUNAMI-1D.  This information is written on unit NTD in the
XSDRNPM input, when NTD is positive.  When TSUNAMI-1D creates the inputs for
the forward and adjoint XSDRNPM criticality calculations, NTD is set to 31 for
the forward case and 32 for the adjoint case.  The files written are ft31f001
and ft32f001, respectively.

.. _6-1a-1:

XSDRNPM forward output file
---------------------------

For a forward case, XSDRNPM writes the following unformatted records on unit NTD:

.. describe:: RECORD 1:  IZM,IM,MXX,MS,ISCT,MM,JT,IGM

	| IZM	         —      Number of zones
	| IM		       —      Number of spatial intervals
	| MXX	         —      Number of compositions (mixtures)
	| MS		       —      Length of the XSDRNPM mixing table
	| ISCT	       —      Order of the Legendre scattering expansion
	| MM	         —      Number of angles in the angular quadrature
	| JT		       —      Number of flux moments
	| IGM	         —      Number of energy groups

.. describe:: RECORD 2:  IGE,IBL,IBR,ISN,IFTG,MMT,NT1,T

  | IGE	   —       Geometry:  1/2/3 = plane/cylinder/sphere
  | IBL	   —       	Left-boundary condition:  0/1/2/3 = vacuum/reflected/periodic/white
  | IBR	   —       Right-boundary condition
  | ISN	   —       	S\ :sub:`n` quadrature order
  | IFTG   —       	First thermal group
  | MMT	   —       Number of neutron groups
  | NT1	   —       Unit number of working cross-section library
  | T		   —      Problem title containing 80 characters

.. describe:: RECORD 3:  V,R

  | V(IM)	    —  Volumes of the spatial mesh cells (single-precision)
  | R(IM+1)	  —    Boundaries of the spatial mesh cells (single-precision)

.. describe:: RECORD 4:  W,PNC

  | W(MM)	       —   Weights in the angular quadrature (single-precision)
  | PNC(MM,JT)	 —        Scattering constants used to obtain flux moments from angular fluxes (single-precision)

.. describe:: RECORD 5:  MA,MZ

	| MA(IM)	—    Zone number by interval
	| MZ(IZM)	—   Mixture number by zone

.. describe:: RECORD 6:  MB,MC,XMD

	| MB(MS)	 —     Mixture number in the cross-section mixing table
	| MC(MS)	 —     Component (nuclide) in the cross-section mixing table
	| XMD(MS)	 —   Atom density in the cross-section mixing table (single-precision)

.. describe:: RECORD 7:  CHI,FISNU

	| CHI(IGM,MXX)	  —   :math:`\chi` for each mixture (single-precision)
	| FISNU(IGM,MXX)	—   :math:`\bar{v}` times the fission cross section for each mixture (single-precision)

.. describe:: RECORD 8:  EIGEN

	| EIGEN	*k*\ :sub:`eff` (single-precision)

.. describe:: NEXT IGM RECORDS:  XNDC

	XNDC(IM,MM) —	Mesh cell centered angular flux for one group (double-precision)

.. describe:: LAST RECORD:  TLEAKAGE

	TLEAKAGE(IGM)	— Total leakage from the system (single-precision)

.. _6-1a-2:

XSDRNPM adjoint output file
---------------------------

For an adjoint case, XSDRNPM writes the following unformatted records on unit
NTD, containing the following information:

.. describe::  RECORD 1:  EIGEN

	| EIGEN —	*k*\ :sub:`eff` value (single-precision)

.. describe:: NEXT IGM RECORDS:  XNDC

	XNDC(IM,MM)	— Mesh cell centered angular flux for one group (double-precision)

The adjoint angular fluxes are reversed in direction such that each angular
flux is the importance for that direction in the forward case.  This reversal
is done by using the reflected angle.  Also, the records are written in forward
order such that the first record corresponds to the highest-energy group.
