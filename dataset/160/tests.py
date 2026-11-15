import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    binary_heap = BinaryHeap()
    binary_heap.insert(6)
    binary_heap.insert(10)
    binary_heap.insert(15)
    binary_heap.insert(12)
    assert binary_heap.pop() == 15
    assert binary_heap.pop() == 12
    assert binary_heap.get_list == [10, 6]
    assert len(binary_heap) == 2
