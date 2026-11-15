"""
Pure Python implementation of the jump search algorithm.
This algorithm iterates through a sorted collection with a step of n^(1/2),
until the element compared is bigger than the one searched.
It will then perform a linear search until it matches the wanted number.
If not found, it returns -1.

https://en.wikipedia.org/wiki/Jump_search
"""
import math
from collections.abc import Sequence
from typing import Any, Protocol

class Comparable(Protocol):

    def __lt__(self, other: Any, /) -> bool:
        ...

def jump_search[T: Comparable](arr: Sequence[T], item: T) -> int:
    """Python implementation of the jump search algorithm.
    Return the index if the `item` is found, otherwise return -1.

    Examples:"""
    if not arr:
        return -1
    arr_size = len(arr)
    block_size = int(math.sqrt(arr_size))
    prev = 0
    step = block_size
    while arr[min(step, arr_size) - 1] < item:
        prev = step
        step += block_size
        if prev >= arr_size:
            return -1
    while arr[prev] < item:
        prev += 1
        if prev == min(step, arr_size):
            return -1
    if arr[prev] == item:
        return prev
    return -1