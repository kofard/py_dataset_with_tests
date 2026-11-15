"""
This is a pure Python implementation of the merge-insertion sort algorithm
Source: https://en.wikipedia.org/wiki/Merge-insertion_sort

For doctests run following command:
python3 -m doctest -v merge_insertion_sort.py
or
python -m doctest -v merge_insertion_sort.py

For manual testing run:
python3 merge_insertion_sort.py
"""
from __future__ import annotations
from typing import Any, Protocol

class Comparable(Protocol):

    def __lt__(self, other: Any, /) -> bool:
        ...

def binary_search_insertion[T: Comparable](sorted_list: list[T], item: T) -> list[T]:
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        middle = (left + right) // 2
        if left == right:
            if sorted_list[middle] < item:
                left = middle + 1
            break
        if sorted_list[middle] < item:
            left = middle + 1
        else:
            right = middle - 1
    sorted_list.insert(left, item)
    return sorted_list

def merge[T: Comparable](left: list[list[T]], right: list[list[T]]) -> list[list[T]]:
    result = []
    while left and right:
        if left[0][0] < right[0][0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right

def sortlist_2d[T: Comparable](list_2d: list[list[T]]) -> list[list[T]]:
    length = len(list_2d)
    if length <= 1:
        return list_2d
    middle = length // 2
    return merge(sortlist_2d(list_2d[:middle]), sortlist_2d(list_2d[middle:]))

def merge_insertion_sort[T: Comparable](collection: list[T]) -> list[T]:
    """Pure implementation of merge-insertion sort algorithm in Python

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:"""
    if len(collection) <= 1:
        return collection
    '\n    Group the items into two pairs, and leave one element if there is a last odd item.\n\n    Example: [999, 100, 75, 40, 10000]\n                -> [999, 100], [75, 40]. Leave 10000.\n    '
    two_paired_list = []
    has_last_odd_item = False
    for i in range(0, len(collection), 2):
        if i == len(collection) - 1:
            has_last_odd_item = True
        else:
            '\n            Sort two-pairs in each groups.\n\n            Example: [999, 100], [75, 40]\n                        -> [100, 999], [40, 75]\n            '
            if collection[i] < collection[i + 1]:
                two_paired_list.append([collection[i], collection[i + 1]])
            else:
                two_paired_list.append([collection[i + 1], collection[i]])
    '\n    Sort two_paired_list.\n\n    Example: [100, 999], [40, 75]\n                -> [40, 75], [100, 999]\n    '
    sorted_list_2d = sortlist_2d(two_paired_list)
    '\n    40 < 100 is sure because it has already been sorted.\n    Generate the sorted_list of them so that you can avoid unnecessary comparison.\n\n    Example:\n           group0 group1\n           40     100\n           75     999\n        ->\n           group0 group1\n           [40,   100]\n           75     999\n    '
    result = [i[0] for i in sorted_list_2d]
    '\n    100 < 999 is sure because it has already been sorted.\n    Put 999 in last of the sorted_list so that you can avoid unnecessary comparison.\n\n    Example:\n           group0 group1\n           [40,   100]\n           75     999\n        ->\n           group0 group1\n           [40,   100,   999]\n           75\n    '
    result.append(sorted_list_2d[-1][1])
    '\n    Insert the last odd item left if there is.\n\n    Example:\n           group0 group1\n           [40,   100,   999]\n           75\n        ->\n           group0 group1\n           [40,   100,   999,   10000]\n           75\n    '
    if has_last_odd_item:
        pivot = collection[-1]
        result = binary_search_insertion(result, pivot)
    "\n    Insert the remaining items.\n    In this case, 40 < 75 is sure because it has already been sorted.\n    Therefore, you only need to insert 75 into [100, 999, 10000],\n    so that you can avoid unnecessary comparison.\n\n    Example:\n           group0 group1\n           [40,   100,   999,   10000]\n            ^ You don't need to compare with this as 40 < 75 is already sure.\n           75\n        ->\n           [40,   75,    100,   999,   10000]\n    "
    is_last_odd_item_inserted_before_this_index = False
    for i in range(len(sorted_list_2d) - 1):
        if result[i] == collection[-1] and has_last_odd_item:
            is_last_odd_item_inserted_before_this_index = True
        pivot = sorted_list_2d[i][1]
        if is_last_odd_item_inserted_before_this_index:
            result = result[:i + 2] + binary_search_insertion(result[i + 2:], pivot)
        else:
            result = result[:i + 1] + binary_search_insertion(result[i + 1:], pivot)
    return result