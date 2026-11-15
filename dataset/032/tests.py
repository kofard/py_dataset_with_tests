import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert surface_area_cube(1) == 6
    assert surface_area_cube(1.6) == 15.360000000000003
    assert surface_area_cube(0) == 0
    assert surface_area_cube(3) == 54
    assert surface_area_cuboid(1, 2, 3) == 22
    assert surface_area_cuboid(0, 0, 0) == 0
    assert surface_area_cuboid(1.6, 2.6, 3.6) == 38.56
    assert surface_area_sphere(5) == 314.1592653589793
    assert surface_area_sphere(1) == 12.566370614359172
    assert surface_area_sphere(1.6) == 32.169908772759484
    assert surface_area_sphere(0) == 0.0
    assert surface_area_hemisphere(5) == 235.61944901923448
    assert surface_area_hemisphere(1) == 9.42477796076938
    assert surface_area_hemisphere(0) == 0.0
    assert surface_area_hemisphere(1.1) == 11.40398133253095
    assert surface_area_cone(10, 24) == 1130.9733552923256
    assert surface_area_cone(6, 8) == 301.59289474462014
    assert surface_area_cone(1.6, 2.6) == 23.387862992395807
    assert surface_area_cone(0, 0) == 0.0
    assert lateral_surface_cone(10, 20) == 702.4814731040726
    assert lateral_surface_cone(6, 8) == 188.49555921538757
    assert lateral_surface_cone(0, 0) == 0.0
    assert surface_area_conical_frustum(1, 2, 3) == 45.511728065337266
    assert surface_area_conical_frustum(4, 5, 6) == 300.7913575056268
    assert surface_area_conical_frustum(0, 0, 0) == 0.0
    assert surface_area_conical_frustum(1.6, 2.6, 3.6) == 78.57907060751548
    assert surface_area_cylinder(7, 10) == 747.6990515543707
    assert surface_area_cylinder(1.6, 2.6) == 42.22300526424682
    assert surface_area_cylinder(0, 0) == 0.0
    assert surface_area_cylinder(6, 8) == 527.7875658030853
    assert lateral_surface_cylinder(10, 20) == 1256.6370614359173
    assert lateral_surface_cylinder(6, 8) == 301.59289474462014
    assert lateral_surface_cylinder(0, 0) == 0.0
    assert surface_area_torus(1, 1) == 39.47841760435743
    assert surface_area_torus(4, 3) == 473.7410112522892
    assert surface_area_torus(1.6, 1.6) == 101.06474906715503
    assert surface_area_torus(0, 0) == 0.0
    assert area_rectangle(10, 20) == 200
    assert area_rectangle(1.6, 2.6) == 4.16
    assert area_rectangle(0, 0) == 0
    assert area_square(10) == 100
    assert area_square(0) == 0
    assert area_square(1.6) == 2.5600000000000005
    assert area_triangle(10, 10) == 50.0
    assert area_triangle(1.6, 2.6) == 2.08
    assert area_triangle(0, 0) == 0.0
    assert area_triangle_three_sides(5, 12, 13) == 30.0
    assert area_triangle_three_sides(10, 11, 12) == 51.521233486786784
    assert area_triangle_three_sides(0, 0, 0) == 0.0
    assert area_triangle_three_sides(1.6, 2.6, 3.6) == 1.8703742940919619
    assert area_parallelogram(10, 20) == 200
    assert area_parallelogram(1.6, 2.6) == 4.16
    assert area_parallelogram(0, 0) == 0
    assert area_trapezium(10, 20, 30) == 450.0
    assert area_trapezium(1.6, 2.6, 3.6) == 7.5600000000000005
    assert area_trapezium(0, 0, 0) == 0.0
    assert area_circle(20) == 1256.6370614359173
    assert area_circle(1.6) == 8.042477193189871
    assert area_circle(0) == 0.0
    assert area_ellipse(10, 10) == 314.1592653589793
    assert area_ellipse(10, 20) == 628.3185307179587
    assert area_ellipse(0, 0) == 0.0
    assert area_ellipse(1.6, 2.6) == 13.06902543893354
    assert area_rhombus(10, 20) == 100.0
    assert area_rhombus(1.6, 2.6) == 2.08
    assert area_rhombus(0, 0) == 0.0
    assert area_reg_polygon(3, 10) == 43.301270189221945
    assert area_reg_polygon(4, 10) == 100.00000000000001
    assert surface_area_reg_prism(3, 10, 20) == 686.6025403784439
    assert surface_area_reg_prism(4, 10, 10) == 600.0
