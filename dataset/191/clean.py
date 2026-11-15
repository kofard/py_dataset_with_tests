"""A non-recursive Segment Tree implementation with range query and single element update,
works virtually with any list of the same type of elements with a "commutative"
combiner.

Explanation:
https://www.geeksforgeeks.org/iterative-segment-tree-range-minimum-query/
https://www.geeksforgeeks.org/segment-tree-efficient-implementation/"""
from __future__ import annotations
from collections.abc import Callable
from typing import TypeVar, cast
T = TypeVar('T')

class SegmentTree[T]:

    def __init__(self, arr: list[T], fnc: Callable[[T, T], T]) -> None:
        """Segment Tree constructor, it works just with commutative combiner.
        :param arr: list of elements for the segment tree
        :param fnc: commutative function for combine two elements"""
        self.N: int = len(arr)
        self.st: list[T] = [cast(T, None) for _ in range(self.N)] + arr
        self.fn = fnc
        self.build()

    def build(self) -> None:
        for p in range(self.N - 1, 0, -1):
            self.st[p] = self.fn(self.st[p * 2], self.st[p * 2 + 1])

    def update(self, p: int, v: T) -> None:
        """Update an element in log(N) time
        :param p: position to be update
        :param v: new value"""
        p += self.N
        self.st[p] = v
        while p > 1:
            p = p // 2
            self.st[p] = self.fn(self.st[p * 2], self.st[p * 2 + 1])

    def query(self, left: int, right: int) -> T | None:
        """Get range query value in log(N) time
        :param left: left element index
        :param right: right element index
        :return: element combined in the range [left, right]"""
        left, right = (left + self.N, right + self.N)
        res: T | None = None
        while left <= right:
            if left % 2 == 1:
                res = self.st[left] if res is None else self.fn(res, self.st[left])
            if right % 2 == 0:
                res = self.st[right] if res is None else self.fn(res, self.st[right])
            left, right = ((left + 1) // 2, (right - 1) // 2)
        return res