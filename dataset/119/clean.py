"""
A pure Python implementation of the heap sort algorithm.
"""
from typing import Protocol

class Comparable(Protocol):

    def __lt__(self, other: object, /) -> bool:
        ...

def heapify[T: Comparable](unsorted: list[T], index: int, heap_size: int) -> None:
    """:param unsorted: unsorted list containing comparable items
    :param index: index
    :param heap_size: size of the heap
    :return: None"""
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[largest] < unsorted[left_index]:
        largest = left_index
    if right_index < heap_size and unsorted[largest] < unsorted[right_index]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = (unsorted[index], unsorted[largest])
        heapify(unsorted, largest, heap_size)

def heap_sort[T: Comparable](unsorted: list[T]) -> list[T]:
    """A pure Python implementation of the heap sort algorithm.

    :param unsorted: a mutable collection of comparable items
    :return: the same collection ordered by ascending

    Examples:"""
    n = len(unsorted)
    for i in range(n // 2 - 1, -1, -1):
        heapify(unsorted, i, n)
    for i in range(n - 1, 0, -1):
        unsorted[0], unsorted[i] = (unsorted[i], unsorted[0])
        heapify(unsorted, 0, i)
    return unsorted