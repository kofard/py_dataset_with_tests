"""
Odd even sort implementation.

https://en.wikipedia.org/wiki/Odd%E2%80%93even_sort
"""
from collections.abc import MutableSequence
from typing import Any, Protocol

class Comparable(Protocol):

    def __gt__(self, other: Any, /) -> bool:
        ...

def odd_even_sort[T: Comparable](collection: MutableSequence[T]) -> MutableSequence[T]:
    """Sort input with odd even sort.

    This algorithm uses the same idea of bubblesort,
    but by first dividing in two phase (odd and even).
    Originally developed for use on parallel processors
    with local interconnections.
    :param collection: mutable ordered sequence of elements
    :return: same collection in ascending order
    Examples:"""
    is_sorted = False
    while is_sorted is False:
        is_sorted = True
        for i in range(0, len(collection) - 1, 2):
            if collection[i] > collection[i + 1]:
                collection[i], collection[i + 1] = (collection[i + 1], collection[i])
                is_sorted = False
        for i in range(1, len(collection) - 1, 2):
            if collection[i] > collection[i + 1]:
                collection[i], collection[i + 1] = (collection[i + 1], collection[i])
                is_sorted = False
    return collection