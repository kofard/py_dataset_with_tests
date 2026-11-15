"""
This is a type of divide and conquer algorithm which divides the search space into
3 parts and finds the target value based on the property of the array or list
(usually monotonic property).

Time Complexity  : O(log3 N)
Space Complexity : O(1)
"""
from __future__ import annotations
precision = 10

def lin_search(left: int, right: int, array: list[int], target: int) -> int:
    """Perform linear search in list. Returns -1 if element is not found.

    Parameters
    ----------
    left : int
        left index bound.
    right : int
        right index bound.
    array : List[int]
        List of elements to be searched on
    target : int
        Element that is searched

    Returns
    -------
    int
        index of element that is looked for.

    Examples
    --------"""
    for i in range(left, right):
        if array[i] == target:
            return i
    return -1

def ite_ternary_search(array: list[int], target: int) -> int:
    """Iterative method of the ternary search algorithm."""
    left = 0
    right = len(array)
    while left <= right:
        if right - left < precision:
            return lin_search(left, right, array, target)
        one_third = left + (right - left) // 3
        two_third = right - (right - left) // 3
        if array[one_third] == target:
            return one_third
        elif array[two_third] == target:
            return two_third
        elif target < array[one_third]:
            right = one_third
        elif array[two_third] < target:
            left = two_third + 1
        else:
            left = one_third + 1
            right = two_third
    return -1

def rec_ternary_search(left: int, right: int, array: list[int], target: int) -> int:
    """Recursive method of the ternary search algorithm."""
    if left < right:
        if right - left < precision:
            return lin_search(left, right, array, target)
        one_third = left + (right - left) // 3
        two_third = right - (right - left) // 3
        if array[one_third] == target:
            return one_third
        elif array[two_third] == target:
            return two_third
        elif target < array[one_third]:
            return rec_ternary_search(left, one_third, array, target)
        elif array[two_third] < target:
            return rec_ternary_search(two_third + 1, right, array, target)
        else:
            return rec_ternary_search(one_third + 1, two_third, array, target)
    else:
        return -1