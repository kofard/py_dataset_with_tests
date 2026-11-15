"""
Find the volume of various shapes.

* https://en.wikipedia.org/wiki/Volume
* https://en.wikipedia.org/wiki/Spherical_cap
"""
from __future__ import annotations
from math import pi, pow

def vol_cube(side_length: float) -> float:
    """Calculate the Volume of a Cube."""
    if side_length < 0:
        raise ValueError('vol_cube() only accepts non-negative values')
    return pow(side_length, 3)

def vol_spherical_cap(height: float, radius: float) -> float:
    """Calculate the volume of the spherical cap."""
    if height < 0 or radius < 0:
        raise ValueError('vol_spherical_cap() only accepts non-negative values')
    return 1 / 3 * pi * pow(height, 2) * (3 * radius - height)

def vol_spheres_intersect(radius_1: float, radius_2: float, centers_distance: float) -> float:
    """Calculate the volume of the intersection of two spheres.

    The intersection is composed by two spherical caps and therefore its volume is the
    sum of the volumes of the spherical caps.
    First, it calculates the heights :math:`(h_1, h_2)` of the spherical caps,
    then the two volumes and it returns the sum.
    The height formulas are

    .. math::
        h_1 = \\frac{(radius_1 - radius_2 + centers\\_distance)
                    \\cdot (radius_1 + radius_2 - centers\\_distance)}
                   {2 \\cdot centers\\_distance}

        h_2 = \\frac{(radius_2 - radius_1 + centers\\_distance)
                    \\cdot (radius_2 + radius_1 - centers\\_distance)}
                   {2 \\cdot centers\\_distance}

    if `centers_distance` is 0 then it returns the volume of the smallers sphere

    :return: ``vol_spherical_cap`` (:math:`h_1`, :math:`radius_2`)
             + ``vol_spherical_cap`` (:math:`h_2`, :math:`radius_1`)"""
    if radius_1 < 0 or radius_2 < 0 or centers_distance < 0:
        raise ValueError('vol_spheres_intersect() only accepts non-negative values')
    if centers_distance == 0:
        return vol_sphere(min(radius_1, radius_2))
    h1 = (radius_1 - radius_2 + centers_distance) * (radius_1 + radius_2 - centers_distance) / (2 * centers_distance)
    h2 = (radius_2 - radius_1 + centers_distance) * (radius_2 + radius_1 - centers_distance) / (2 * centers_distance)
    return vol_spherical_cap(h1, radius_2) + vol_spherical_cap(h2, radius_1)

def vol_spheres_union(radius_1: float, radius_2: float, centers_distance: float) -> float:
    """Calculate the volume of the union of two spheres that possibly intersect.

    It is the sum of sphere :math:`A` and sphere :math:`B` minus their intersection.
    First, it calculates the volumes :math:`(v_1, v_2)` of the spheres,
    then the volume of the intersection :math:`i` and
    it returns the sum :math:`v_1 + v_2 - i`.
    If `centers_distance` is 0 then it returns the volume of the larger sphere

    :return: ``vol_sphere`` (:math:`radius_1`) + ``vol_sphere`` (:math:`radius_2`)
             - ``vol_spheres_intersect``
             (:math:`radius_1`, :math:`radius_2`, :math:`centers\\_distance`)"""
    if radius_1 <= 0 or radius_2 <= 0 or centers_distance < 0:
        raise ValueError('vol_spheres_union() only accepts non-negative values, non-zero radius')
    if centers_distance == 0:
        return vol_sphere(max(radius_1, radius_2))
    return vol_sphere(radius_1) + vol_sphere(radius_2) - vol_spheres_intersect(radius_1, radius_2, centers_distance)

def vol_cuboid(width: float, height: float, length: float) -> float:
    """Calculate the Volume of a Cuboid.

    :return: multiple of `width`, `length` and `height`"""
    if width < 0 or height < 0 or length < 0:
        raise ValueError('vol_cuboid() only accepts non-negative values')
    return float(width * height * length)

def vol_cone(area_of_base: float, height: float) -> float:
    """| Calculate the Volume of a Cone.
    | Wikipedia reference: https://en.wikipedia.org/wiki/Cone

    :return: :math:`\\frac{1}{3} \\cdot area\\_of\\_base \\cdot height`"""
    if height < 0 or area_of_base < 0:
        raise ValueError('vol_cone() only accepts non-negative values')
    return area_of_base * height / 3.0

def vol_right_circ_cone(radius: float, height: float) -> float:
    """| Calculate the Volume of a Right Circular Cone.
    | Wikipedia reference: https://en.wikipedia.org/wiki/Cone

    :return: :math:`\\frac{1}{3} \\cdot \\pi \\cdot radius^2 \\cdot height`"""
    if height < 0 or radius < 0:
        raise ValueError('vol_right_circ_cone() only accepts non-negative values')
    return pi * pow(radius, 2) * height / 3.0

def vol_prism(area_of_base: float, height: float) -> float:
    """| Calculate the Volume of a Prism.
    | Wikipedia reference: https://en.wikipedia.org/wiki/Prism_(geometry)

    :return: :math:`V = B \\cdot h`"""
    if height < 0 or area_of_base < 0:
        raise ValueError('vol_prism() only accepts non-negative values')
    return float(area_of_base * height)

def vol_pyramid(area_of_base: float, height: float) -> float:
    """| Calculate the Volume of a Pyramid.
    | Wikipedia reference: https://en.wikipedia.org/wiki/Pyramid_(geometry)

    :return: :math:`\\frac{1}{3} \\cdot B \\cdot h`"""
    if height < 0 or area_of_base < 0:
        raise ValueError('vol_pyramid() only accepts non-negative values')
    return area_of_base * height / 3.0

def vol_sphere(radius: float) -> float:
    """| Calculate the Volume of a Sphere.
    | Wikipedia reference: https://en.wikipedia.org/wiki/Sphere

    :return: :math:`\\frac{4}{3} \\cdot \\pi \\cdot r^3`"""
    if radius < 0:
        raise ValueError('vol_sphere() only accepts non-negative values')
    return 4 / 3 * pi * pow(radius, 3)

def vol_hemisphere(radius: float) -> float:
    """| Calculate the volume of a hemisphere
    | Wikipedia reference: https://en.wikipedia.org/wiki/Hemisphere
    | Other references: https://www.cuemath.com/geometry/hemisphere

    :return: :math:`\\frac{2}{3} \\cdot \\pi \\cdot radius^3`"""
    if radius < 0:
        raise ValueError('vol_hemisphere() only accepts non-negative values')
    return pow(radius, 3) * pi * 2 / 3

def vol_circular_cylinder(radius: float, height: float) -> float:
    """| Calculate the Volume of a Circular Cylinder.
    | Wikipedia reference: https://en.wikipedia.org/wiki/Cylinder

    :return: :math:`\\pi \\cdot radius^2 \\cdot height`"""
    if height < 0 or radius < 0:
        raise ValueError('vol_circular_cylinder() only accepts non-negative values')
    return pow(radius, 2) * height * pi

def vol_hollow_circular_cylinder(inner_radius: float, outer_radius: float, height: float) -> float:
    """Calculate the Volume of a Hollow Circular Cylinder."""
    if inner_radius < 0 or outer_radius < 0 or height < 0:
        raise ValueError('vol_hollow_circular_cylinder() only accepts non-negative values')
    if outer_radius <= inner_radius:
        raise ValueError('outer_radius must be greater than inner_radius')
    return pi * (pow(outer_radius, 2) - pow(inner_radius, 2)) * height

def vol_conical_frustum(height: float, radius_1: float, radius_2: float) -> float:
    """| Calculate the Volume of a Conical Frustum.
    | Wikipedia reference: https://en.wikipedia.org/wiki/Frustum"""
    if radius_1 < 0 or radius_2 < 0 or height < 0:
        raise ValueError('vol_conical_frustum() only accepts non-negative values')
    return 1 / 3 * pi * height * (pow(radius_1, 2) + pow(radius_2, 2) + radius_1 * radius_2)

def vol_torus(torus_radius: float, tube_radius: float) -> float:
    """| Calculate the Volume of a Torus.
    | Wikipedia reference: https://en.wikipedia.org/wiki/Torus

    :return: :math:`2 \\pi^2 \\cdot torus\\_radius \\cdot tube\\_radius^2`"""
    if torus_radius < 0 or tube_radius < 0:
        raise ValueError('vol_torus() only accepts non-negative values')
    return 2 * pow(pi, 2) * torus_radius * pow(tube_radius, 2)

def vol_octahedron(oct_side: float) -> float:
    """| Calculate the Volume of an Octahedron.
    | Wikipedia reference: https://en.wikipedia.org/wiki/Regular_octahedron"""
    if oct_side < 0:
        raise ValueError('vol_octahedron() only accepts non-negative values')
    return oct_side ** 3 * 2 ** 0.5 / 3

def vol_icosahedron(tri_side: float) -> float:
    """| Calculate the Volume of an Icosahedron.
    | Wikipedia reference: https://en.wikipedia.org/wiki/Regular_icosahedron"""
    if tri_side < 0:
        raise ValueError('vol_icosahedron() only accepts non-negative values')
    return tri_side ** 3 * (3 + 5 ** 0.5) * 5 / 12

def main() -> None:
    """Print the Results of Various Volume Calculations."""
    print('Volumes:')
    print(f'Cube: vol_cube(2) = {vol_cube(2)!r}')
    print(f'Cuboid: vol_cuboid(2, 2, 2) = {vol_cuboid(2, 2, 2)!r}')
    print(f'Cone: vol_cone(2, 2) = {vol_cone(2, 2)!r}')
    print(f'Right Circular Cone: vol_right_circ_cone(2, 2) = {vol_right_circ_cone(2, 2)!r}')
    print(f'Prism: vol_prism(2, 2) = {vol_prism(2, 2)!r}')
    print(f'Pyramid: vol_pyramid(2, 2) = {vol_pyramid(2, 2)!r}')
    print(f'Sphere: vol_sphere(2) = {vol_sphere(2)!r}')
    print(f'Hemisphere: vol_hemisphere(2) = {vol_hemisphere(2)!r}')
    print(f'Circular Cylinder: vol_circular_cylinder(2, 2) = {vol_circular_cylinder(2, 2)!r}')
    print(f'Torus: vol_torus(2, 2) = {vol_torus(2, 2)!r}')
    print(f'Conical Frustum: vol_conical_frustum(2, 2, 4) = {vol_conical_frustum(2, 2, 4)!r}')
    print(f'Spherical cap: vol_spherical_cap(1, 2) = {vol_spherical_cap(1, 2)!r}')
    print(f'Spheres intersection: vol_spheres_intersect(2, 2, 1) = {vol_spheres_intersect(2, 2, 1)!r}')
    print(f'Spheres union: vol_spheres_union(2, 2, 1) = {vol_spheres_union(2, 2, 1)!r}')
    print(f'Hollow Circular Cylinder: vol_hollow_circular_cylinder(1, 2, 3) = {vol_hollow_circular_cylinder(1, 2, 3)!r}')
    print(f'Octahedron: vol_octahedron(2.5) = {vol_octahedron(2.5)!r}')
    print(f'Icosahedron: vol_icosahedron(2.5) = {vol_icosahedron(2.5)!r}')