import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    tree = Node(10)
    assert sum(BinaryTreeNodeSum(tree)) == 10
    tree.left = Node(5)
    assert sum(BinaryTreeNodeSum(tree)) == 15
    tree.right = Node(-3)
    assert sum(BinaryTreeNodeSum(tree)) == 12
    tree.left.left = Node(12)
    assert sum(BinaryTreeNodeSum(tree)) == 24
    tree.right.left = Node(8)
    tree.right.right = Node(0)
    assert sum(BinaryTreeNodeSum(tree)) == 32
