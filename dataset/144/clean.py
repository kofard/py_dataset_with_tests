"""
This is a pure Python implementation of the linear search algorithm.

For doctests run following command:
python3 -m doctest -v linear_search.py

For manual testing run:
python3 linear_search.py
"""

def linear_search(sequence: list, target: int) -> int:
    """A pure Python implementation of a linear search algorithm

    :param sequence: a collection with comparable items (sorting is not required for
        linear search)
    :param target: item value to search
    :return: index of found item or -1 if item is not found

    Examples:"""
    for index, item in enumerate(sequence):
        if item == target:
            return index
    return -1

def rec_linear_search(sequence: list, low: int, high: int, target: int) -> int:
    """A pure Python implementation of a recursive linear search algorithm

    :param sequence: a collection with comparable items (as sorted items not required
        in Linear Search)
    :param low: Lower bound of the array
    :param high: Higher bound of the array
    :param target: The element to be found
    :return: Index of the key or -1 if key not found

    Examples:"""
    if not (0 <= high < len(sequence) and 0 <= low < len(sequence)):
        raise ValueError('Invalid upper or lower bound!')
    if high < low:
        return -1
    if sequence[low] == target:
        return low
    if sequence[high] == target:
        return high
    return rec_linear_search(sequence, low + 1, high - 1, target)