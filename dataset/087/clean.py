"""
An implementation of the ear clipping method for triangulating a simple polygon.

Wikipedia : https://en.wikipedia.org/wiki/Polygon_triangulation
"""

def is_ear(polygon: list[tuple[float, float]], point_idx: int, direction: str) -> bool:
    """This function determines whether three points form an ear."""
    prev_idx = (point_idx - 1) % len(polygon)
    next_idx = (point_idx + 1) % len(polygon)
    prev_point = polygon[prev_idx]
    point = polygon[point_idx]
    next_point = polygon[next_idx]
    if is_convex(prev_point, point, next_point, direction):
        for j in range(len(polygon)):
            if j not in (prev_idx, point_idx, next_idx) and is_point_inside_triangle(prev_point, point, next_point, polygon[j]):
                return False
        return True
    return False

def is_convex(point: tuple[float, float], prev_p: tuple[float, float], next_p: tuple[float, float], direction: str) -> bool:
    """Determine with the ccw, if 3 points are convex."""
    if direction == 'counter-clockwise':
        cross_product = (next_p[0] - point[0]) * (prev_p[1] - point[1]) - (prev_p[0] - point[0]) * (next_p[1] - point[1])
    else:
        cross_product = (prev_p[0] - point[0]) * (next_p[1] - point[1]) - (next_p[0] - point[0]) * (prev_p[1] - point[1])
    return cross_product >= 0

def cross_product(p1: tuple[float, float], p2: tuple[float, float], p3: tuple[float, float]) -> float:
    """This function computes the product of two vectors, with 3 points.
    If the vectors are collinear, the output is 0.
    If the three points rotate counterclockwise, the output is positive.
    If three points rotate clockwise, the output is negative."""
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def direction(polygon: list[tuple[float, float]]) -> str:
    """Determine the orientation (clockwise or counterclockwise) of a polygon defined
    by a list of points."""
    point_0 = min(polygon, key=lambda point: (point[1], point[0]))
    idx_p0 = polygon.index(point_0)
    prev_idx = (idx_p0 - 1) % len(polygon)
    next_idx = (idx_p0 + 1) % len(polygon)
    prev_point = polygon[prev_idx]
    next_point = polygon[next_idx]
    while cross_product(point_0, next_point, prev_point) == 0:
        next_idx += 1
        next_point = polygon[next_idx]
    if cross_product(point_0, next_point, prev_point) > 0:
        return 'clockwise'
    return 'counter-clockwise'

def is_point_inside_triangle(p1: tuple[float, float], p2: tuple[float, float], p3: tuple[float, float], test_point: tuple[float, float]) -> bool:
    """Determine whether a given point is located inside a triangle
    formed by three other points.

    This function calculates the area of both the triangle formed by
    the three input points (p1, p2, p3)
    and the sub-triangles formed by replacing one vertex of the main
    triangle with the test_point.
    If the sum of the areas of the sub-triangles is equal to the area of
    the main triangle, the test_point
    is considered to be inside the triangle. Otherwise, it is considered outside."""
    area_triangle = abs(0.5 * (p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])))
    area1 = abs(0.5 * (test_point[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - test_point[1]) + p3[0] * (test_point[1] - p2[1])))
    area2 = abs(0.5 * (p1[0] * (test_point[1] - p3[1]) + test_point[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - test_point[1])))
    area3 = abs(0.5 * (p1[0] * (p2[1] - test_point[1]) + p2[0] * (test_point[1] - p1[1]) + test_point[0] * (p1[1] - p2[1])))
    return area_triangle == area1 + area2 + area3

def triangulate_polygon(coordinates: list[tuple[float, float]]) -> list[list[tuple[float, float]]]:
    """Triangulate a polygon and provide the points of the resulting triangles.
    This function takes a list of coordinates that represent the vertices of a polygon.
    It iteratively finds and removes 'ears' from the polygon to create a list
    of triangles that triangulate the entire polygon.
    The order of vertices in the coordinates list is assumed to be
    consistent (either clockwise or counterclockwise).
    The function uses helper functions 'direction' to determine the polygon's
    orientation and 'is_ear' to identify 'ear' vertices.

    Note: The function assumes that the input coordinates form a valid simple polygon."""
    polygon: list[tuple[float, float]] = coordinates.copy()
    triangles: list = []
    orientation: str = direction(polygon)
    while len(polygon) >= 3:
        ear_found: bool = False
        for i in range(len(polygon)):
            if is_ear(polygon, i, orientation):
                ear_found = True
                prev_idx: int = (i - 1) % len(polygon)
                next_idx: int = (i + 1) % len(polygon)
                prev_point: tuple[float, float] = polygon[prev_idx]
                point: tuple[float, float] = polygon[i]
                next_point: tuple[float, float] = polygon[next_idx]
                triangles.append([prev_point, point, next_point])
                polygon.pop(i)
                break
        if not ear_found:
            break
    return triangles