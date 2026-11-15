"""A merge sort which accepts comparable items and recursively
splits them in half, then sorts and combines the halves.

https://en.wikipedia.org/wiki/Merge_sort
"""
from collections.abc import Iterable
from typing import Protocol

class Comparable(Protocol):

    def __lt__(self, other: object, /) -> bool:
        ...

def merge[T: Comparable](collection: Iterable[T]) -> list[T]:
    """Return a new list of ``collection`` sorted in ascending order.

    The input is copied, so the original iterable is left unchanged.
    Items must be mutually comparable with ``<``."""
    arr = list(collection)
    if len(arr) > 1:
        middle_length = len(arr) // 2
        left_array = merge(arr[:middle_length])
        right_array = merge(arr[middle_length:])
        left_size = len(left_array)
        right_size = len(right_array)
        left_index = 0
        right_index = 0
        index = 0
        while left_index < left_size and right_index < right_size:
            if left_array[left_index] < right_array[right_index]:
                arr[index] = left_array[left_index]
                left_index += 1
            else:
                arr[index] = right_array[right_index]
                right_index += 1
            index += 1
        while left_index < left_size:
            arr[index] = left_array[left_index]
            left_index += 1
            index += 1
        while right_index < right_size:
            arr[index] = right_array[right_index]
            right_index += 1
            index += 1
    return arr