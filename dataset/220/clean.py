"""
A Python implementation of the quick select algorithm, which is efficient for
calculating the value that would appear in the index of a list if it would be
sorted, even if it is not already sorted
https://en.wikipedia.org/wiki/Quickselect
"""
import random

def _partition(data: list, pivot) -> tuple:
    """
    Three way partition the data into smaller, equal and greater lists,
    in relationship to the pivot
    :param data: The data to be sorted (a list)
    :param pivot: The value to partition the data on
    :return: Three list: smaller, equal and greater
    """
    less, equal, greater = ([], [], [])
    for element in data:
        if element < pivot:
            less.append(element)
        elif element > pivot:
            greater.append(element)
        else:
            equal.append(element)
    return (less, equal, greater)

def quick_select(items: list, index: int):
    if index >= len(items) or index < 0:
        return None
    pivot = items[random.randint(0, len(items) - 1)]
    count = 0
    smaller, equal, larger = _partition(items, pivot)
    count = len(equal)
    m = len(smaller)
    if m <= index < m + count:
        return pivot
    elif m > index:
        return quick_select(smaller, index)
    else:
        return quick_select(larger, index - (m + count))

def median(items: list):
    """One common application of Quickselect is finding the median, which is
    the middle element (or average of the two middle elements) in a sorted dataset.
    It works efficiently on unsorted lists by partially sorting the data without
    fully sorting the entire list."""
    mid, rem = divmod(len(items), 2)
    if rem != 0:
        return quick_select(items=items, index=mid)
    else:
        low_mid = quick_select(items=items, index=mid - 1)
        high_mid = quick_select(items=items, index=mid)
        return (low_mid + high_mid) / 2