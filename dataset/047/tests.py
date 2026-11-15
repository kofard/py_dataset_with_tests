import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    tree = Node(10)
    tree.left = Node(5)
    tree.right = Node(-3)
    tree.left.left = Node(3)
    tree.left.right = Node(2)
    tree.right.right = Node(11)
    tree.left.left.left = Node(3)
    tree.left.left.right = Node(-2)
    tree.left.right.right = Node(1)
    assert BinaryTreePathSum().path_sum(tree, 8) == 3
    assert BinaryTreePathSum().path_sum(tree, 7) == 2
    tree.right.right = Node(10)
    assert BinaryTreePathSum().path_sum(tree, 8) == 2
    assert BinaryTreePathSum().path_sum(None, 0) == 0
    assert BinaryTreePathSum().path_sum(tree, 0) == 0
    tree2 = Node(0)
    tree2.left = Node(5)
    tree2.right = Node(5)
    assert BinaryTreePathSum().path_sum(tree2, 5) == 4
    assert BinaryTreePathSum().path_sum(tree2, -1) == 0
    assert BinaryTreePathSum().path_sum(tree2, 0) == 1
