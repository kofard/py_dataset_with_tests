import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert build_sparse_table([8, 1, 0, 3, 4, 9, 3]) == [[8, 1, 0, 3, 4, 9, 3], [1, 0, 0, 3, 4, 3, 0], [0, 0, 0, 3, 0, 0, 0]]
    assert build_sparse_table([3, 1, 9]) == [[3, 1, 9], [1, 1, 0]]
    assert query(build_sparse_table([8, 1, 0, 3, 4, 9, 3]), 0, 4) == 0
    assert query(build_sparse_table([8, 1, 0, 3, 4, 9, 3]), 4, 6) == 3
    assert query(build_sparse_table([3, 1, 9]), 2, 2) == 9
    assert query(build_sparse_table([3, 1, 9]), 0, 1) == 1
