"""
A recursive implementation of the insertion sort algorithm
"""
from __future__ import annotations
from collections.abc import MutableSequence
from typing import Protocol

class Comparable(Protocol):

    def __lt__(self, other: object, /) -> bool:
        ...

def rec_insertion_sort[T: Comparable](collection: MutableSequence[T], n: int) -> None:
    """Given a collection of comparable elements and its length, sorts the
    collection in place in ascending order.

    :param collection: A mutable collection of comparable elements
    :param n: The length of collection"""
    if len(collection) <= 1 or n <= 1:
        return
    insert_next(collection, n - 1)
    rec_insertion_sort(collection, n - 1)

def insert_next[T: Comparable](collection: MutableSequence[T], index: int) -> None:
    """Inserts the '(index-1)th' element into place"""
    if index >= len(collection) or not collection[index] < collection[index - 1]:
        return
    collection[index - 1], collection[index] = (collection[index], collection[index - 1])
    insert_next(collection, index + 1)