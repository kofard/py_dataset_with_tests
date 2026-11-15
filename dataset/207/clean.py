"""
This is an implementation of Pigeon Hole Sort.
For doctests run following command:

python3 -m doctest -v pigeon_sort.py
or
python -m doctest -v pigeon_sort.py

For manual testing run:
python pigeon_sort.py
"""
from __future__ import annotations

def pigeon_sort(array: list[int]) -> list[int]:
    """Implementation of pigeon hole sort algorithm
    :param array: Collection of comparable items
    :return: Collection sorted in ascending order"""
    if len(array) == 0:
        return array
    _min, _max = (min(array), max(array))
    holes_range = _max - _min + 1
    holes, holes_repeat = ([0] * holes_range, [0] * holes_range)
    for i in array:
        index = i - _min
        holes[index] = i
        holes_repeat[index] += 1
    index = 0
    for i in range(holes_range):
        while holes_repeat[i] > 0:
            array[index] = holes[i]
            index += 1
            holes_repeat[i] -= 1
    return array