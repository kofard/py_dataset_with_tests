import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert encode("Hello", "MONARCHY") == 'CFSUPM'
    assert encode("attack on the left flank", "EMERGENCY") == 'DQZSBYFSDZFMFNLOHFDRSG'
    assert encode("Sorry!", "SPECIAL") == 'AVXETX'
    assert encode("Number 1", "NUMBER") == 'UMBENF'
    assert encode("Photosynthesis!", "THE SUN") == 'OEMHQHVCHESUKE'
    assert decode("BMZFAZRZDH", "HAZARD") == 'FIREHAZARD'
    assert decode("HNBWBPQT", "AUTOMOBILE") == 'DRIVINGX'
    assert decode("SLYSSAQS", "CASTLE") == 'ATXTACKX'
