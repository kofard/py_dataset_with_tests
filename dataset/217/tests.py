import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert list(slow_primes(0)) == []
    assert list(slow_primes(-1)) == []
    assert list(slow_primes(-10)) == []
    assert list(slow_primes(25)) == [2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert list(slow_primes(11)) == [2, 3, 5, 7, 11]
    assert list(slow_primes(33)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    assert list(slow_primes(1000))[-1] == 997
    assert list(primes(0)) == []
    assert list(primes(-1)) == []
    assert list(primes(-10)) == []
    assert list(primes(25)) == [2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert list(primes(11)) == [2, 3, 5, 7, 11]
    assert list(primes(33)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    assert list(primes(1000))[-1] == 997
    assert list(fast_primes(0)) == []
    assert list(fast_primes(-1)) == []
    assert list(fast_primes(-10)) == []
    assert list(fast_primes(25)) == [2, 3, 5, 7, 11, 13, 17, 19, 23]
    assert list(fast_primes(11)) == [2, 3, 5, 7, 11]
    assert list(fast_primes(33)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    assert list(fast_primes(1000))[-1] == 997
