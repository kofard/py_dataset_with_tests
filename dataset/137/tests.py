import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    kmp = "knuth_morris_pratt"
    assert all(
   knuth_morris_pratt(kmp, s) == kmp.find(s)
   for s in ("kn", "h_m", "rr", "tt", "not there")
) == True
