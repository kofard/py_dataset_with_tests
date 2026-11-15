import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert compare_string('0010','0110') == '0_10'
    assert compare_string('0110','1101') == False
    assert check(['0.00.01.5']) == ['0.00.01.5']
    assert decimal_to_binary(3,[1.5]) == ['0.00.01.5']
    assert is_for_table('__1','011',2) == True
    assert is_for_table('01_','001',1) == False
    assert selection([[1]],['0.00.01.5']) == ['0.00.01.5']
    assert selection([[1]],['0.00.01.5']) == ['0.00.01.5']
    assert prime_implicant_chart(['0.00.01.5'],['0.00.01.5']) == [[1]]
