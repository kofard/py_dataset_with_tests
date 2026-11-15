import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert simple_interest(18000.0, 0.06, 3) == 3240.0
    assert simple_interest(0.5, 0.06, 3) == 0.09
    assert simple_interest(18000.0, 0.01, 10) == 1800.0
    assert simple_interest(18000.0, 0.0, 3) == 0.0
    assert simple_interest(5500.0, 0.01, 100) == 5500.0
    assert compound_interest(10000.0, 0.05, 3) == 1576.2500000000014
    assert compound_interest(10000.0, 0.05, 1) == 500.00000000000045
    assert compound_interest(0.5, 0.05, 3) == 0.07881250000000006
    assert apr_interest(10000.0, 0.05, 3) == 1618.223072263547
    assert apr_interest(10000.0, 0.05, 1) == 512.6749646744732
    assert apr_interest(0.5, 0.05, 3) == 0.08091115361317736
