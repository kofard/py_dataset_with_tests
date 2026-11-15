"""
Implementation of iterative merge sort in Python
Author: Aman Gupta

For doctests run following command:
python3 -m doctest -v iterative_merge_sort.py

For manual testing run:
python3 iterative_merge_sort.py
"""
from __future__ import annotations
from typing import Any, Protocol

class Comparable(Protocol):

    def __lt__(self, other: Any, /) -> bool:
        ...

def merge[T: Comparable](input_list: list[T], low: int, mid: int, high: int) -> list[T]:
    """
    sorting left-half and right-half individually
    then merging them into result
    """
    result: list[T] = []
    left, right = (input_list[low:mid], input_list[mid:high + 1])
    while left and right:
        result.append((left if left[0] <= right[0] else right).pop(0))
    input_list[low:high + 1] = result + left + right
    return input_list

def iter_merge_sort[T: Comparable](input_list: list[T]) -> list[T]:
    """Return a sorted copy of the input list"""
    if len(input_list) <= 1:
        return input_list
    input_list = list(input_list)
    p = 2
    while p <= len(input_list):
        for i in range(0, len(input_list), p):
            low = i
            high = i + p - 1
            mid = (low + high + 1) // 2
            input_list = merge(input_list, low, mid, high)
        if p * 2 >= len(input_list):
            mid = i
            input_list = merge(input_list, 0, mid, len(input_list) - 1)
            break
        p *= 2
    return input_list