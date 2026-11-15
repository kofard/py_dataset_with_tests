"""
Floyd's cycle detection algorithm is a popular algorithm used to detect cycles
in a linked list. It uses two pointers, a slow pointer and a fast pointer,
to traverse the linked list. The slow pointer moves one node at a time while the fast
pointer moves two nodes at a time. If there is a cycle in the linked list,
the fast pointer will eventually catch up to the slow pointer and they will
meet at the same node. If there is no cycle, the fast pointer will reach the end of
the linked list and the algorithm will terminate.

For more information: https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare
"""
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any, Self

@dataclass
class Node:
    """
    A class representing a node in a singly linked list.
    """
    data: Any
    next_node: Self | None = None

@dataclass
class LinkedList:
    """
    A class representing a singly linked list.
    """
    head: Node | None = None

    def __iter__(self) -> Iterator:
        """Iterates through the linked list.

        Returns:
            Iterator: An iterator over the linked list.

        Examples:"""
        visited = []
        node = self.head
        while node:
            if node in visited:
                return
            visited.append(node)
            yield node.data
            node = node.next_node

    def add_node(self, data: Any) -> None:
        """Adds a new node to the end of the linked list.

        Args:
            data (Any): The data to be stored in the new node.

        Examples:"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node is not None:
            current_node = current_node.next_node
        current_node.next_node = new_node

    def detect_cycle(self) -> bool:
        """Detects if there is a cycle in the linked list using
        Floyd's cycle detection algorithm.

        Returns:
            bool: True if there is a cycle, False otherwise.

        Examples:"""
        if self.head is None:
            return False
        slow_pointer: Node | None = self.head
        fast_pointer: Node | None = self.head
        while fast_pointer is not None and fast_pointer.next_node is not None:
            slow_pointer = slow_pointer.next_node if slow_pointer else None
            fast_pointer = fast_pointer.next_node.next_node
            if slow_pointer == fast_pointer:
                return True
        return False