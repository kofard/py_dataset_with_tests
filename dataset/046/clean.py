"""
Sum of all nodes in a binary tree.

Python implementation:
    O(n) time complexity - Recurses through :meth:`depth_first_search`
                            with each element.
    O(n) space complexity - At any point in time maximum number of stack
                            frames that could be in memory is `n`
"""
from __future__ import annotations
from collections.abc import Iterator

class Node:
    """
    A Node has a value variable and pointers to Nodes to its left and right.
    """

    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None

class BinaryTreeNodeSum:
    """The below tree looks like this
        10
       /  \\
      5   -3
     /    / \\
    12   8  0"""

    def __init__(self, tree: Node) -> None:
        self.tree = tree

    def depth_first_search(self, node: Node | None) -> int:
        if node is None:
            return 0
        return node.value + (self.depth_first_search(node.left) + self.depth_first_search(node.right))

    def __iter__(self) -> Iterator[int]:
        yield self.depth_first_search(self.tree)