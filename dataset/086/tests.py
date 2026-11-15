import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    assert arr.array[:arr.size]  # Display only the filled part of the array == [1, 2, 3]
    arr.append(4)
    assert arr.array[:arr.size] == [1, 2, 3, 4]
    arr.append(5)
    assert arr.array[:arr.size] == [1, 2, 3, 4, 5]
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    arr._resize(10)
    assert arr.capacity == 10
    assert arr.array[:arr.size] == [1, 2]
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    assert arr.get(0) == 1
    assert arr.get(1) == 2
    arr = DynamicArray()
    arr.append(1)
    assert len(arr) == 1
    arr.append(2)
    assert len(arr) == 2
    arr.append(3)
    assert len(arr) == 3
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    assert str(arr) == '[1, 2, 3]'
    arr.append(4)
    assert str(arr) == '[1, 2, 3, 4]'
