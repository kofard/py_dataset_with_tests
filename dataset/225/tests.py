import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert RandomizedHeap([2, 3, 1, 5, 1, 7]).to_sorted_list() == [1, 1, 2, 3, 5, 7]
    rh = RandomizedHeap()
    rh.insert(1)
    rh.insert(-1)
    rh.insert(0)
    assert rh.to_sorted_list() == [-1, 0, 1]
    rhn = RandomizedHeapNode(10)
    assert rhn.value == 10
    rhn = RandomizedHeapNode(-10)
    assert rhn.value == -10
    rhn1 = RandomizedHeapNode(10)
    rhn2 = RandomizedHeapNode(20)
    assert RandomizedHeapNode.merge(rhn1, rhn2).value == 10
    rhn1 = RandomizedHeapNode(20)
    rhn2 = RandomizedHeapNode(10)
    assert RandomizedHeapNode.merge(rhn1, rhn2).value == 10
    rhn1 = RandomizedHeapNode(5)
    rhn2 = RandomizedHeapNode(0)
    assert RandomizedHeapNode.merge(rhn1, rhn2).value == 0
    rh = RandomizedHeap([3, 1, 3, 7])
    assert rh.to_sorted_list() == [1, 3, 3, 7]
    rh = RandomizedHeap()
    rh.insert(3)
    rh.insert(1)
    rh.insert(3)
    rh.insert(7)
    assert rh.to_sorted_list() == [1, 3, 3, 7]
    rh = RandomizedHeap([3, 1, 3, 7])
    assert rh.pop() == 1
    assert rh.pop() == 3
    assert rh.pop() == 3
    assert rh.pop() == 7
    rh = RandomizedHeap()
    rh.insert(3)
    assert rh.top() == 3
    rh.insert(1)
    assert rh.top() == 1
    rh.insert(3)
    assert rh.top() == 1
    rh.insert(7)
    assert rh.top() == 1
    rh = RandomizedHeap([3, 1, 3, 7])
    rh.clear()
    rh = RandomizedHeap([3, 1, 3, 7])
    assert rh.to_sorted_list() == [1, 3, 3, 7]
    rh = RandomizedHeap()
    assert bool(rh) == False
    rh.insert(1)
    assert bool(rh) == True
    rh.clear()
    assert bool(rh) == False
