from typing import Protocol

class Comparable(Protocol):

    def __lt__(self, other: object, /) -> bool:
        ...

def stooge_sort[T: Comparable](arr: list[T]) -> list[T]:
    """Examples:"""
    stooge(arr, 0, len(arr) - 1)
    return arr

def stooge[T: Comparable](arr: list[T], i: int, h: int) -> None:
    if i >= h:
        return
    if arr[h] < arr[i]:
        arr[i], arr[h] = (arr[h], arr[i])
    if h - i + 1 > 2:
        t = int((h - i + 1) / 3)
        stooge(arr, i, h - t)
        stooge(arr, i + t, h)
        stooge(arr, i, h - t)