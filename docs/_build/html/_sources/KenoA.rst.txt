.. _8-1A:

Keno Appendix A: KENO V.a Shape Descriptions
============================================

The geometry **shape**\ s allowed in KENO V.a geometry description are:

   **CUBE, CUBOID, SPHERE, CYLINDER, ZCYLINDER, XCYLINDER, YCYLINDER,
   HEMISPHERE, HEMISPHE+X, HEMISPHE−X, HEMISPHE+Y,**

   **HEMISPHE−Y, HEMISPHE+Z, HEMISPHE−Z, XHEMICYL+Y, XHEMICYL−Y,
   XHEMICYL+Z, XHEMICYL−Z, YHEMICYL+X, YHEMICYL−X, YHEMICYL+Z,
   YHEMICYL−Z, ZHEMICYL+X, ZHEMICYL−X, ZHEMICYL+Y, ZHEMICYL−Y**

**CUBE**
  specifies a cube. It sets +X = +Y = +Z and −X = −Y = −Z. Note
  that the +X dimension need not equal the −X dimension of the cube (i.e.,
  the origin need not be at the center of the cube).

**CUBOID**
  is a rectangular parallelepiped and may be described anywhere
  relative to the origin.

**SPHERE**
  specifies a sphere that is centered about the origin, unless
  otherwise specified by the optional region origin data.

**CYLINDER**
  specifies a cylinder that has its length described along
  the Z axis. Its centerline must lie on the Z axis, unless otherwise
  specified by the optional region origin data.

**ZCYLINDER**
  specifies a cylinder that has its length described along
  the Z axis. Its centerline must lie on the Z axis, unless otherwise
  specified by the optional region origin data.

**XCYLINDER**
  specifies a cylinder that has its length described along
  the X axis. Its centerline must lie on the X axis, unless otherwise
  specified by the optional region origin data.

**YCYLINDER**
  specifies a cylinder that has its length described along
  the Y axis. Its centerline must lie on the Y axis, unless otherwise
  specified by the optional region origin data.

**HEMISPHERE**
  is used to specify a spherical segment of one base whose
  spherical surface exists in the positive Z direction. The base or flat
  portion of the spherical segment is centered about a point that may be
  specified in the optional region origin data. By default, the center of
  the spherical surface is the origin and the distance to the base from
  the center of the spherical surface is zero.

**HEMISPHE**\ *bc*
  is used to specify a spherical segment of one base
  whose spherical surface exists in the *bc* direction (b = + or −, c = x,
  y, or z). The base or flat portion of the spherical segment is located a
  distance ρ from the center of the spherical surface, and the center may
  be specified in the optional region origin data. **HEMISPHE+Z** is the
  same as the previously described **HEMISPHERE** and **HEMISPHE−Z** is
  the mirror image of **HEMISPHE+Z**, therefore existing only in the
  negative Z direction. By default the center of the spherical surface is
  the origin and the distance of the base from the center of the spherical
  surface is zero.

*b*\ **HEMICYL**\ *cd*
  is used to specify a cylindrical segment whose
  axis is in the *b* direction (b = x, y, or z) and whose cylindrical
  surface exists only in the *c* direction from a plane perpendicular to
  the *d* axis (c = + or −, d = x, y, or z). The position of the plane
  (cut surface) can be specified in the optional region chord data. This
  plane cuts the cylinder parallel to the axis at some distance, ρ, from
  the axis. By default, the axis passes through the origin and ρ is zero.
  (Examples: **ZHEMICYL+X, YHEMICYL−Z, XHEMICYL+Y**)

Up to 6 dimensions follow the shape keyword [*xx(1)* through *xx(6)*].
These entries are separated by one or more blanks and define the size of
the region. Dimensions must be given in cm.

*xx(1)*: Radius for a sphere, cylinder, hemisphere or hemicylinder,

         +X dimension for a cube or cuboid.

*xx(2)*: −X dimension for cube or cuboid,

         +Z for cylinder or Z cylinder,

         +X for X cylinder,

         +Y for Y cylinder,

         +length for hemicylinder,

         omit *xx(2)* for a sphere or hemisphere.

*xx(3)*: +Y dimension for cuboid,

         −Z for cylinder or Z cylinder,

         −X for X cylinder,

         −Y for Y cylinder,

         −length for hemicylinder,

         omit *xx(3)* for a sphere, hemisphere, or cube.

*xx(4)*: −Y dimension for cuboid,

         omit for all other geometry types.

*xx(5)*: +Z dimension for cuboid,

         omit for all other geometry types.

*xx(6)*: −Z dimension for cuboid,

         omit for all other geometry types.
