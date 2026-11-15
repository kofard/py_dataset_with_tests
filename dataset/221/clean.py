from random import randrange
from typing import Any, Protocol

class Comparable(Protocol):

    def __lt__(self, other: Any, /) -> bool:
        ...

def quick_sort_3partition[T: Comparable](sorting: list[T], left: int, right: int) -> None:
    """"
    Python implementation of the quicksort algorithm with 3-way partition.
    The idea of 3-way quicksort is based on "Dutch National Flag algorithm".

    :param sorting: sort list
    :param left: left endpoint of sorting
    :param right: right endpoint of sorting
    :return: None

    Examples:"""
    if right <= left:
        return
    a = i = left
    b = right
    pivot = sorting[left]
    while i <= b:
        if sorting[i] < pivot:
            sorting[a], sorting[i] = (sorting[i], sorting[a])
            a += 1
            i += 1
        elif sorting[i] > pivot:
            sorting[b], sorting[i] = (sorting[i], sorting[b])
            b -= 1
        else:
            i += 1
    quick_sort_3partition(sorting, left, a - 1)
    quick_sort_3partition(sorting, b + 1, right)

def quick_sort_lomuto_partition[T: Comparable](sorting: list[T], left: int, right: int) -> None:
    """A pure Python implementation of the quicksort algorithm(in-place)
    with Lomuto partition scheme:
    https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme

    :param sorting: sort list
    :param left: left endpoint of sorting
    :param right: right endpoint of sorting
    :return: None

    Examples:"""
    if left < right:
        pivot_index = lomuto_partition(sorting, left, right)
        quick_sort_lomuto_partition(sorting, left, pivot_index - 1)
        quick_sort_lomuto_partition(sorting, pivot_index + 1, right)

def lomuto_partition[T: Comparable](sorting: list[T], left: int, right: int) -> int:
    """Example:"""
    pivot = sorting[right]
    store_index = left
    for i in range(left, right):
        if sorting[i] < pivot:
            sorting[store_index], sorting[i] = (sorting[i], sorting[store_index])
            store_index += 1
    sorting[right], sorting[store_index] = (sorting[store_index], sorting[right])
    return store_index

def hoare_partition_by_value[T: Comparable](array: list[T], pivot_value: T, start: int=0, end: int | None=None) -> int:
    """Returns the starting index of the right subarray, which contains the
    elements greater than or equal to `pivot_value`"""
    if end is None:
        end = len(array) - 1
    left = start
    right = end
    while True:
        '\n        In an intermediate iteration, state could look like this:\n\n            lllluuuuuuuuuurrrrr\n                ^        ^\n                |        |\n              left      right\n\n        Where the middle values are unknown (u), since they are not yet traversed.\n        `left-1` points to the end of the left subarray.\n        `right+1` points to the start of the right subarray.\n        '
        while array[left] < pivot_value:
            left += 1
            if left > end:
                return end + 1
        while array[right] >= pivot_value:
            right -= 1
            if right < start:
                return start
        if left > right:
            break
        assert all((i < pivot_value for i in array[start:left]))
        assert all((i >= pivot_value for i in array[right + 1:end]))
        '\n            llllllruuuuulrrrrrr\n                  ^     ^\n                  |     |\n                left   right\n        '
        array[left], array[right] = (array[right], array[left])
        left += 1
        right -= 1
    return right + 1

def hoare_partition_by_pivot[T: Comparable](array: list[T], pivot_index: int, start=0, end: int | None=None) -> int:
    """Returns the new pivot index after partitioning"""
    if end is None:
        end = len(array) - 1

    def swap(i1, i2):
        array[i1], array[i2] = (array[i2], array[i1])
    pivot_value = array[pivot_index]
    swap(pivot_index, end)
    greater_or_equal = hoare_partition_by_value(array, pivot_value, start=start, end=end - 1)
    swap(end, greater_or_equal)
    return greater_or_equal

def quicksort_hoare[T: Comparable](array: list[T], start: int=0, end: int | None=None) -> None:
    """Quicksort using the Hoare partition scheme:
    - https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
    - The Art of Computer Programming, Volume 3: Sorting and Searching"""
    if end is None:
        end = len(array) - 1
    if end + 1 - start <= 1:
        return
    pivot_index_final = hoare_partition_by_pivot(array, randrange(start, end), start, end)
    quicksort_hoare(array, start, pivot_index_final - 1)
    quicksort_hoare(array, pivot_index_final + 1, end)

def three_way_radix_quicksort[T: Comparable](sorting: list[T]) -> list[T]:
    """Three-way radix quicksort:
    https://en.wikipedia.org/wiki/Quicksort#Three-way_radix_quicksort
    First divide the list into three parts.
    Then recursively sort the "less than" and "greater than" partitions."""
    if len(sorting) <= 1:
        return sorting
    return three_way_radix_quicksort([i for i in sorting if i < sorting[0]]) + [i for i in sorting if i == sorting[0]] + three_way_radix_quicksort([i for i in sorting if i > sorting[0]])