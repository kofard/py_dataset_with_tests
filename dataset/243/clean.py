"""
Given two line segments, determine whether they intersect.

This is based on the algorithm described in Introduction to Algorithms
(CLRS), Chapter 33.

Reference:
    - https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    - https://en.wikipedia.org/wiki/Orientation_(geometry)
"""
from __future__ import annotations
from typing import NamedTuple

class Point(NamedTuple):
    """A point in 2D space."""
    x: float
    y: float

def direction(pivot: Point, target: Point, query: Point) -> float:
    """Return the cross product of vectors (pivot->query) and (pivot->target).

    The sign of the result encodes the orientation of the ordered triple
    (pivot, target, query):
      - Negative  ->  counter-clockwise (left turn)
      - Positive  ->  clockwise (right turn)
      - Zero      ->  collinear"""
    return (query.x - pivot.x) * (target.y - pivot.y) - (target.x - pivot.x) * (query.y - pivot.y)

def on_segment(seg_start: Point, seg_end: Point, point: Point) -> bool:
    """Check whether *point*, known to be collinear with the segment, lies on it."""
    return min(seg_start.x, seg_end.x) <= point.x <= max(seg_start.x, seg_end.x) and min(seg_start.y, seg_end.y) <= point.y <= max(seg_start.y, seg_end.y)

def segments_intersect(p1: Point, p2: Point, p3: Point, p4: Point) -> bool:
    """Return True if line segment p1p2 intersects line segment p3p4.

    Uses the CLRS cross-product / orientation method.  Handles both the
    general case (proper crossing) and degenerate cases where one endpoint
    lies exactly on the other segment."""
    d1 = direction(p3, p4, p1)
    d2 = direction(p3, p4, p2)
    d3 = direction(p1, p2, p3)
    d4 = direction(p1, p2, p4)
    if (d1 < 0 < d2 or d2 < 0 < d1) and (d3 < 0 < d4 or d4 < 0 < d3):
        return True
    if d1 == 0 and on_segment(p3, p4, p1):
        return True
    if d2 == 0 and on_segment(p3, p4, p2):
        return True
    if d3 == 0 and on_segment(p1, p2, p3):
        return True
    return d4 == 0 and on_segment(p1, p2, p4)