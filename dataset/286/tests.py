import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert vol_cube(1) == 1.0
    assert vol_cube(3) == 27.0
    assert vol_cube(0) == 0.0
    assert vol_cube(1.6) == 4.096000000000001
    assert vol_spherical_cap(1, 2) == 5.235987755982988
    assert vol_spherical_cap(1.6, 2.6) == 16.621119532592402
    assert vol_spherical_cap(0, 0) == 0.0
    assert vol_spheres_intersect(2, 2, 1) == 21.205750411731103
    assert vol_spheres_intersect(2.6, 2.6, 1.6) == 40.71504079052372
    assert vol_spheres_intersect(0, 0, 0) == 0.0
    assert vol_spheres_union(2, 2, 1) == 45.814892864851146
    assert vol_spheres_union(1.56, 2.2, 1.4) == 48.77802773671288
    assert vol_cuboid(1, 1, 1) == 1.0
    assert vol_cuboid(1, 2, 3) == 6.0
    assert vol_cuboid(1.6, 2.6, 3.6) == 14.976
    assert vol_cuboid(0, 0, 0) == 0.0
    assert vol_cone(10, 3) == 10.0
    assert vol_cone(1, 1) == 0.3333333333333333
    assert vol_cone(1.6, 1.6) == 0.8533333333333335
    assert vol_cone(0, 0) == 0.0
    assert vol_right_circ_cone(2, 3) == 12.566370614359172
    assert vol_right_circ_cone(0, 0) == 0.0
    assert vol_right_circ_cone(1.6, 1.6) == 4.289321169701265
    assert vol_prism(10, 2) == 20.0
    assert vol_prism(11, 1) == 11.0
    assert vol_prism(1.6, 1.6) == 2.5600000000000005
    assert vol_prism(0, 0) == 0.0
    assert vol_pyramid(10, 3) == 10.0
    assert vol_pyramid(1.5, 3) == 1.5
    assert vol_pyramid(1.6, 1.6) == 0.8533333333333335
    assert vol_pyramid(0, 0) == 0.0
    assert vol_sphere(5) == 523.5987755982989
    assert vol_sphere(1) == 4.1887902047863905
    assert vol_sphere(1.6) == 17.15728467880506
    assert vol_sphere(0) == 0.0
    assert vol_hemisphere(1) == 2.0943951023931953
    assert vol_hemisphere(7) == 718.377520120866
    assert vol_hemisphere(1.6) == 8.57864233940253
    assert vol_hemisphere(0) == 0.0
    assert vol_circular_cylinder(1, 1) == 3.141592653589793
    assert vol_circular_cylinder(4, 3) == 150.79644737231007
    assert vol_circular_cylinder(1.6, 1.6) == 12.867963509103795
    assert vol_circular_cylinder(0, 0) == 0.0
    assert vol_hollow_circular_cylinder(1, 2, 3) == 28.274333882308138
    assert vol_hollow_circular_cylinder(1.6, 2.6, 3.6) == 47.50088092227767
    assert vol_conical_frustum(45, 7, 28) == 48490.482608158454
    assert vol_conical_frustum(1, 1, 2) == 7.330382858376184
    assert vol_conical_frustum(1.6, 2.6, 3.6) == 48.7240076620753
    assert vol_conical_frustum(0, 0, 0) == 0.0
    assert vol_torus(1, 1) == 19.739208802178716
    assert vol_torus(4, 3) == 710.6115168784338
    assert vol_torus(3, 4) == 947.4820225045784
    assert vol_torus(1.6, 1.6) == 80.85179925372404
    assert vol_torus(0, 0) == 0.0
    from math import isclose
    assert isclose(vol_octahedron(2.5), 7.36569563735987) == True
    assert isclose(vol_octahedron(10), 471.40452079103168) == True
    assert isclose(vol_octahedron(5), 58.92556509887896) == True
    assert isclose(vol_octahedron(3.5), 20.21146882891548) == True
    assert vol_octahedron(0) == 0.0
    from math import isclose
    assert isclose(vol_icosahedron(2.5), 34.088984228514256) == True
    assert isclose(vol_icosahedron(10), 2181.694990624912374) == True
    assert isclose(vol_icosahedron(5), 272.711873828114047) == True
    assert isclose(vol_icosahedron(3.49), 92.740688412033628) == True
    assert vol_icosahedron(0) == 0.0
