"""
A pure implementation of Dutch national flag (DNF) sort algorithm in Python.
Dutch National Flag algorithm is an algorithm originally designed by Edsger Dijkstra.
It is the most optimal sort for 3 unique values (eg. 0, 1, 2) in a sequence.  DNF can
sort a sequence of n size with [0 <= a[i] <= 2] at guaranteed O(n) complexity in a
single pass.

The flag of the Netherlands consists of three colors: white, red, and blue.
The task is to randomly arrange balls of white, red, and blue in such a way that balls
of the same color are placed together.  DNF sorts a sequence of 0, 1, and 2's in linear
time that does not consume any extra space.  This algorithm can be implemented only on
a sequence that contains three unique elements.

1) Time complexity is O(n).
2) Space complexity is O(1).

More info on: https://en.wikipedia.org/wiki/Dutch_national_flag_problem

For doctests run following command:
python3 -m doctest -v dutch_national_flag_sort.py

For manual testing run:
python dnf_sort.py
"""
red = 0
white = 1
blue = 2
colors = (red, white, blue)

def dutch_national_flag_sort(sequence: list) -> list:
    """A pure Python implementation of Dutch National Flag sort algorithm.
    :param data: 3 unique integer values (e.g., 0, 1, 2) in an sequence
    :return: The same collection in ascending order"""
    if not sequence:
        return []
    if len(sequence) == 1:
        return list(sequence)
    low = 0
    high = len(sequence) - 1
    mid = 0
    while mid <= high:
        if sequence[mid] == colors[0]:
            sequence[low], sequence[mid] = (sequence[mid], sequence[low])
            low += 1
            mid += 1
        elif sequence[mid] == colors[1]:
            mid += 1
        elif sequence[mid] == colors[2]:
            sequence[mid], sequence[high] = (sequence[high], sequence[mid])
            high -= 1
        else:
            msg = f'The elements inside the sequence must contains only {colors} values'
            raise ValueError(msg)
    return sequence