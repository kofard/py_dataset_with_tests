from __future__ import annotations
import random
from collections.abc import Iterable
from typing import Any, TypeVar
T = TypeVar('T', bound=bool)

class RandomizedHeapNode[T: bool]:
    """
    One node of the randomized heap. Contains the value and references to
    two children.
    """

    def __init__(self, value: T) -> None:
        self._value: T = value
        self.left: RandomizedHeapNode[T] | None = None
        self.right: RandomizedHeapNode[T] | None = None

    @property
    def value(self) -> T:
        """Return the value of the node."""
        return self._value

    @staticmethod
    def merge(root1: RandomizedHeapNode[T] | None, root2: RandomizedHeapNode[T] | None) -> RandomizedHeapNode[T] | None:
        """Merge 2 nodes together."""
        if not root1:
            return root2
        if not root2:
            return root1
        if root1.value > root2.value:
            root1, root2 = (root2, root1)
        if random.choice([True, False]):
            root1.left, root1.right = (root1.right, root1.left)
        root1.left = RandomizedHeapNode.merge(root1.left, root2)
        return root1

class RandomizedHeap[T: bool]:
    """A data structure that allows inserting a new value and to pop the smallest
    values. Both operations take O(logN) time where N is the size of the
    structure.
    Wiki: https://en.wikipedia.org/wiki/Randomized_meldable_heap"""

    def __init__(self, data: Iterable[T] | None=()) -> None:
        self._root: RandomizedHeapNode[T] | None = None
        if data:
            for item in data:
                self.insert(item)

    def insert(self, value: T) -> None:
        """Insert the value into the heap."""
        self._root = RandomizedHeapNode.merge(self._root, RandomizedHeapNode(value))

    def pop(self) -> T | None:
        """Pop the smallest value from the heap and return it."""
        result = self.top()
        if self._root is None:
            return None
        self._root = RandomizedHeapNode.merge(self._root.left, self._root.right)
        return result

    def top(self) -> T:
        """Return the smallest value from the heap."""
        if not self._root:
            raise IndexError("Can't get top element for the empty heap.")
        return self._root.value

    def clear(self) -> None:
        """Clear the heap."""
        self._root = None

    def to_sorted_list(self) -> list[Any]:
        """Returns sorted list containing all the values in the heap."""
        result = []
        while self:
            result.append(self.pop())
        return result

    def __bool__(self) -> bool:
        """Check if the heap is not empty."""
        return self._root is not None