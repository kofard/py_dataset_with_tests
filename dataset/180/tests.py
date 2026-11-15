import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert _validated_alphabet("abc") == ['a', 'b', 'c']
    assert move_to_front_encode("banana", "abcdefghijklmnopqrstuvwxyz") == [1, 1, 13, 1, 1, 1]
    assert move_to_front_encode("banana", "abn") == [1, 1, 2, 1, 1, 1]
    assert move_to_front_encode("", "abc") == []
    assert move_to_front_decode([1, 1, 13, 1, 1, 1], "abcdefghijklmnopqrstuvwxyz") == 'banana'
    assert move_to_front_decode([1, 1, 2, 1, 1, 1], "abn") == 'banana'
    assert move_to_front_decode([], "abc") == ''
