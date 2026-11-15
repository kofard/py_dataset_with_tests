import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert is_operand("1") == True
    assert is_operand("+") == False
    assert evaluate("+ 9 * 2 6") == 21
    assert evaluate("/ * 10 2 + 4 1 ") == 4.0
    assert evaluate("2") == 2
    assert evaluate("+ * 2 3 / 8 4") == 8.0
    assert evaluate_recursive(['2']) == 2
    expression = ['+', '*', '2', '3', '/', '8', '4']
    assert evaluate_recursive(expression) == 8.0
    assert expression == []
    assert evaluate_recursive(['+', '9', '*', '2', '6']) == 21
    assert evaluate_recursive(['/', '*', '10', '2', '+', '4', '1']) == 4.0
