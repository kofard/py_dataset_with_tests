import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    xor_list = XORLinkedList()
    xor_list.insert(10)
    xor_list.insert(20)
    xor_list.insert(30)
    assert xor_list.to_list() == [10, 20, 30]
