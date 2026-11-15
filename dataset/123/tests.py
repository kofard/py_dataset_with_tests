import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert ipv4_to_decimal("192.168.0.1") == 3232235521
    assert ipv4_to_decimal("10.0.0.255") == 167772415
    assert alt_ipv4_to_decimal("192.168.0.1") == 3232235521
    assert alt_ipv4_to_decimal("10.0.0.255") == 167772415
    assert decimal_to_ipv4(3232235521) == '192.168.0.1'
    assert decimal_to_ipv4(167772415) == '10.0.0.255'
