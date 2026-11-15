"""
Find the area of various geometric shapes
Wikipedia reference: https://en.wikipedia.org/wiki/Area
"""
from math import pi, sqrt, tan

def surface_area_cube(side_length: float) -> float:
    """Calculate the Surface Area of a Cube."""
    if side_length < 0:
        raise ValueError('surface_area_cube() only accepts non-negative values')
    return 6 * side_length ** 2

def surface_area_cuboid(length: float, breadth: float, height: float) -> float:
    """Calculate the Surface Area of a Cuboid."""
    if length < 0 or breadth < 0 or height < 0:
        raise ValueError('surface_area_cuboid() only accepts non-negative values')
    return 2 * (length * breadth + breadth * height + length * height)

def surface_area_sphere(radius: float) -> float:
    """Calculate the Surface Area of a Sphere.
    Wikipedia reference: https://en.wikipedia.org/wiki/Sphere
    Formula: 4 * pi * r^2"""
    if radius < 0:
        raise ValueError('surface_area_sphere() only accepts non-negative values')
    return 4 * pi * radius ** 2

def surface_area_hemisphere(radius: float) -> float:
    """Calculate the Surface Area of a Hemisphere.
    Formula: 3 * pi * r^2"""
    if radius < 0:
        raise ValueError('surface_area_hemisphere() only accepts non-negative values')
    return 3 * pi * radius ** 2

def surface_area_cone(radius: float, height: float) -> float:
    """Calculate the Surface Area of a Cone.
    Wikipedia reference: https://en.wikipedia.org/wiki/Cone
    Formula: pi * r * (r + (h ** 2 + r ** 2) ** 0.5)"""
    if radius < 0 or height < 0:
        raise ValueError('surface_area_cone() only accepts non-negative values')
    return pi * radius * (radius + (height ** 2 + radius ** 2) ** 0.5)

def lateral_surface_cone(radius: float, height: float) -> float:
    """Calculate the Lateral Surface Area of a Cone.
    Wikipedia reference: https://en.wikipedia.org/wiki/Cone
    Formula: pi * r * (h ** 2 + r ** 2) ** 0.5"""
    if radius < 0 or height < 0:
        raise ValueError('lateral_surface_cone() only accepts non-negative values')
    return pi * radius * (height ** 2 + radius ** 2) ** 0.5

def surface_area_conical_frustum(radius_1: float, radius_2: float, height: float) -> float:
    """Calculate the Surface Area of a Conical Frustum."""
    if radius_1 < 0 or radius_2 < 0 or height < 0:
        raise ValueError('surface_area_conical_frustum() only accepts non-negative values')
    slant_height = (height ** 2 + (radius_1 - radius_2) ** 2) ** 0.5
    return pi * (slant_height * (radius_1 + radius_2) + radius_1 ** 2 + radius_2 ** 2)

def surface_area_cylinder(radius: float, height: float) -> float:
    """Calculate the Surface Area of a Cylinder.
    Wikipedia reference: https://en.wikipedia.org/wiki/Cylinder
    Formula: 2 * pi * r * (h + r)"""
    if radius < 0 or height < 0:
        raise ValueError('surface_area_cylinder() only accepts non-negative values')
    return 2 * pi * radius * (height + radius)

def lateral_surface_cylinder(radius: float, height: float) -> float:
    """Calculate the Lateral Surface Area of a Cylinder.
    Wikipedia reference: https://en.wikipedia.org/wiki/Cylinder
    Formula: 2 * pi * r * h"""
    if radius < 0 or height < 0:
        raise ValueError('lateral_surface_cylinder() only accepts non-negative values')
    return 2 * pi * radius * height

def surface_area_torus(torus_radius: float, tube_radius: float) -> float:
    """Calculate the Area of a Torus.
    Wikipedia reference: https://en.wikipedia.org/wiki/Torus
    :return 4pi^2 * torus_radius * tube_radius"""
    if torus_radius < 0 or tube_radius < 0:
        raise ValueError('surface_area_torus() only accepts non-negative values')
    if torus_radius < tube_radius:
        raise ValueError('surface_area_torus() does not support spindle or self intersecting tori')
    return 4 * pow(pi, 2) * torus_radius * tube_radius

def area_rectangle(length: float, width: float) -> float:
    """Calculate the area of a rectangle."""
    if length < 0 or width < 0:
        raise ValueError('area_rectangle() only accepts non-negative values')
    return length * width

def area_square(side_length: float) -> float:
    """Calculate the area of a square."""
    if side_length < 0:
        raise ValueError('area_square() only accepts non-negative values')
    return side_length ** 2

def area_triangle(base: float, height: float) -> float:
    """Calculate the area of a triangle given the base and height."""
    if base < 0 or height < 0:
        raise ValueError('area_triangle() only accepts non-negative values')
    return base * height / 2

def area_triangle_three_sides(side1: float, side2: float, side3: float) -> float:
    """Calculate area of triangle when the length of 3 sides are known.
    This function uses Heron's formula: https://en.wikipedia.org/wiki/Heron%27s_formula"""
    if side1 < 0 or side2 < 0 or side3 < 0:
        raise ValueError('area_triangle_three_sides() only accepts non-negative values')
    if side1 + side2 < side3 or side1 + side3 < side2 or side2 + side3 < side1:
        raise ValueError('Given three sides do not form a triangle')
    semi_perimeter = (side1 + side2 + side3) / 2
    area = sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))
    return area

def area_parallelogram(base: float, height: float) -> float:
    """Calculate the area of a parallelogram."""
    if base < 0 or height < 0:
        raise ValueError('area_parallelogram() only accepts non-negative values')
    return base * height

def area_trapezium(base1: float, base2: float, height: float) -> float:
    """Calculate the area of a trapezium."""
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError('area_trapezium() only accepts non-negative values')
    return 1 / 2 * (base1 + base2) * height

def area_circle(radius: float) -> float:
    """Calculate the area of a circle."""
    if radius < 0:
        raise ValueError('area_circle() only accepts non-negative values')
    return pi * radius ** 2

def area_ellipse(radius_x: float, radius_y: float) -> float:
    """Calculate the area of a ellipse."""
    if radius_x < 0 or radius_y < 0:
        raise ValueError('area_ellipse() only accepts non-negative values')
    return pi * radius_x * radius_y

def area_rhombus(diagonal_1: float, diagonal_2: float) -> float:
    """Calculate the area of a rhombus."""
    if diagonal_1 < 0 or diagonal_2 < 0:
        raise ValueError('area_rhombus() only accepts non-negative values')
    return 1 / 2 * diagonal_1 * diagonal_2

def area_reg_polygon(sides: int, length: float) -> float:
    """Calculate the area of a regular polygon.
    Wikipedia reference: https://en.wikipedia.org/wiki/Polygon#Regular_polygons
    Formula: (n*s^2*cot(pi/n))/4"""
    if not isinstance(sides, int) or sides < 3:
        raise ValueError('area_reg_polygon() only accepts integers greater than or equal to three as number of sides')
    if length < 0:
        raise ValueError('area_reg_polygon() only accepts non-negative values as length of a side')
    return sides * length ** 2 / (4 * tan(pi / sides))

def surface_area_reg_prism(sides: int, edge: float, height: float) -> float:
    """Calculate the surface area of a regular prism.
    Wikipedia reference: https://en.wikipedia.org/wiki/Prism
    Formula: 2*S(base) + n*a*h"""
    if not isinstance(sides, int) or sides < 3:
        raise ValueError('surface_area_reg_prism() only accepts integers greater than or equal to three as number of sides')
    if edge < 0 or height < 0:
        raise ValueError('surface_area_reg_prism() only accepts non-negative values as length of an edge or height')
    return 2 * area_reg_polygon(sides, edge) + sides * edge * height