import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert list(SkewHeap([2, 3, 1, 5, 1, 7])) == [1, 1, 2, 3, 5, 7]
    sh = SkewHeap()
    sh.insert(1)
    sh.insert(-1)
    sh.insert(0)
    assert list(sh) == [-1, 0, 1]
    assert SkewNode(0).value == 0
    assert SkewNode(3.14159).value == 3.14159
    assert SkewNode("hello").value == 'hello'
    SkewNode(None).value
    assert SkewNode(True).value == True
    assert SkewNode([]).value == []
    assert SkewNode({}).value == {}
    assert SkewNode(set()).value == set()
    assert SkewNode(0.0).value == 0.0
    assert SkewNode(-1e-10).value == -1e-10
    assert SkewNode(10).value == 10
    assert SkewNode(-10.5).value == -10.5
    assert SkewNode.merge(SkewNode(10),SkewNode(-10.5)).value == -10.5
    assert SkewNode.merge(SkewNode(10),SkewNode(10.5)).value == 10
    assert SkewNode.merge(SkewNode(10),SkewNode(10)).value == 10
    assert SkewNode.merge(SkewNode(-100),SkewNode(-10.5)).value == -100
    sh = SkewHeap([3, 1, 3, 7])
    assert list(sh) == [1, 3, 3, 7]
    sh = SkewHeap()
    assert bool(sh) == False
    sh.insert(1)
    assert bool(sh) == True
    sh.clear()
    assert bool(sh) == False
    sh = SkewHeap([3, 1, 3, 7])
    assert list(sh) == [1, 3, 3, 7]
    sh = SkewHeap()
    sh.insert(3)
    sh.insert(1)
    sh.insert(3)
    sh.insert(7)
    assert list(sh) == [1, 3, 3, 7]
    sh = SkewHeap([3, 1, 3, 7])
    assert sh.pop() == 1
    assert sh.pop() == 3
    assert sh.pop() == 3
    assert sh.pop() == 7
    sh = SkewHeap()
    sh.insert(3)
    assert sh.top() == 3
    sh.insert(1)
    assert sh.top() == 1
    sh.insert(3)
    assert sh.top() == 1
    sh.insert(7)
    assert sh.top() == 1
    sh = SkewHeap([3, 1, 3, 7])
    sh.clear()
