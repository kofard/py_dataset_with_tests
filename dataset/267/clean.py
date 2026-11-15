import operator
from typing import Protocol

class Comparable(Protocol):

    def __lt__(self, other: object, /) -> bool:
        ...

    def __gt__(self, other: object, /) -> bool:
        ...

def strand_sort[T: Comparable](arr: list[T], reverse: bool=False, solution: list[T] | None=None) -> list[T]:
    """Strand sort implementation
    source: https://en.wikipedia.org/wiki/Strand_sort

    :param arr: Unordered input list
    :param reverse: Descent ordering flag
    :param solution: Ordered items container

    Examples:"""
    _operator = operator.lt if reverse else operator.gt
    solution = solution or []
    if not arr:
        return solution
    sublist = [arr.pop(0)]
    for i, item in enumerate(arr):
        if _operator(item, sublist[-1]):
            sublist.append(item)
            arr.pop(i)
    if not solution:
        solution.extend(sublist)
    else:
        while sublist:
            item = sublist.pop(0)
            for i, xx in enumerate(solution):
                if not _operator(item, xx):
                    solution.insert(i, item)
                    break
            else:
                solution.append(item)
    strand_sort(arr, reverse, solution)
    return solution