"""XOR Linked List implementation
A memory-efficient doubly linked list that uses the XOR of node addresses.
Each node stores one pointer that is the XOR of the previous and next node addresses.
https://en.wikipedia.org/wiki/XOR_linked_list
Example:"""
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    both: int = 0

class XORLinkedList:

    def __init__(self) -> None:
        """Initializes an empty XOR Linked List."""
        self.head: Node | None = None
        self.tail: Node | None = None
        self._nodes: dict[int, Node] = {}

    def _xor(self, node_a: Node | None, node_b: Node | None) -> int:
        """
        Helper function to get the XOR of two node IDs (simulated addresses).
        Names 'node_a' and 'node_b' are used for descriptive parameters.
        """
        id_a = id(node_a) if node_a else 0
        id_b = id(node_b) if node_b else 0
        return id_a ^ id_b

    def insert(self, value: int) -> None:
        """Inserts a value at the end of the list."""
        node = Node(value)
        self._nodes[id(node)] = node
        node_id = id(node)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.both = id(self.tail)
            if self.tail:
                self.tail.both ^= node_id
            self.tail = node

    def to_list(self) -> list[int]:
        """Converts the XOR list to a standard Python list (forward traversal)."""
        result = []
        prev_id = 0
        current = self.head
        while current:
            result.append(current.value)
            current_id = id(current)
            next_id = prev_id ^ current.both
            prev_id = current_id
            current = self._nodes.get(next_id)
        return result