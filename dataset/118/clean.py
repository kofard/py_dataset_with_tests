from __future__ import annotations
from collections.abc import Iterator
from typing import Any

class ContainsLoopError(Exception):
    pass

class Node:

    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next_node: Node | None = None

    def __iter__(self) -> Iterator[Any]:
        node = self
        visited = set()
        while node:
            if node in visited:
                raise ContainsLoopError
            visited.add(node)
            yield node.data
            node = node.next_node

    @property
    def has_loop(self) -> bool:
        """A loop is when the exact same Node appears more than once in a linked list."""
        try:
            list(self)
            return False
        except ContainsLoopError:
            return True