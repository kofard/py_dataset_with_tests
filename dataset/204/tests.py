import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    data = [[2.0149, 0.6192, 10.9263]]
    targets = [-1]
    perceptron = Perceptron(data, targets)
    assert perceptron.training() == 5
    data = [[2.0149, 0.6192, 10.9263]]
    targets = [-1]
    perceptron = Perceptron(data, targets)
    assert perceptron.training() == 5
    assert perceptron.sort([2.0149, 0.6192, 10.9263]) == -1
    data = [[0], [-0.5], [0.5]]
    targets = [1, -1, 1]
    perceptron = Perceptron(data, targets)
    assert perceptron.sign(0) == 1
    assert perceptron.sign(-0.5) == -1
    assert perceptron.sign(0.5) == 1
