"""
Andrew's Monotone Chain Convex Hull Algorithm.

Reference: https://en.wikipedia.org/wiki/Convex_hull_algorithms#Andrew's_monotone_chain_algorithm
Reference: Andrew, A. M. (1979). "Another efficient algorithm for convex hulls
           in two dimensions". Information Processing Letters, 9(5), 216-219.

Andrew's monotone chain algorithm computes the convex hull of a set of 2D points
in O(n log n) time. It first sorts the points lexicographically (by x-coordinate,
and in case of a tie, by y-coordinate) and then constructs the lower and upper
hulls in two separate O(n) passes.
"""
from __future__ import annotations
from typing import NamedTuple

class Point(NamedTuple):
    """A 2D point with real-valued coordinates."""
    x: float
    y: float

def cross_product_direction(origin: Point, point_a: Point, point_b: Point) -> float:
    """Compute the 2D cross product of vectors (origin -> point_a) and (origin -> point_b).

    The return value encodes the orientation of the ordered triplet
    (origin, point_a, point_b):
        > 0 : Counter-clockwise turn (left turn)
        < 0 : Clockwise turn (right turn)
        = 0 : Collinear points

    Parameters:
        origin: The reference pivot point.
        point_a: The first endpoint.
        point_b: The second endpoint.

    Returns:
        The signed magnitude of the 2D cross product."""
    return (point_a.x - origin.x) * (point_b.y - origin.y) - (point_a.y - origin.y) * (point_b.x - origin.x)

def monotone_chain(points: list[Point]) -> list[Point]:
    """Compute the convex hull of a set of 2D points in counter-clockwise order
    using Andrew's Monotone Chain algorithm.

    Parameters:
        points: A list of 2D points.

    Returns:
        A list of vertices forming the convex hull in counter-clockwise order.

    Time Complexity: O(n log n) where n is the number of points.
    Space Complexity: O(n)

    Examples:"""
    unique_sorted_points = sorted(set(points))
    if len(unique_sorted_points) <= 1:
        return unique_sorted_points
    lower_hull: list[Point] = []
    for candidate_point in unique_sorted_points:
        while len(lower_hull) >= 2 and cross_product_direction(lower_hull[-2], lower_hull[-1], candidate_point) <= 0:
            lower_hull.pop()
        lower_hull.append(candidate_point)
    upper_hull: list[Point] = []
    for candidate_point in reversed(unique_sorted_points):
        while len(upper_hull) >= 2 and cross_product_direction(upper_hull[-2], upper_hull[-1], candidate_point) <= 0:
            upper_hull.pop()
        upper_hull.append(candidate_point)
    return lower_hull[:-1] + upper_hull[:-1]