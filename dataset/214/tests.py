import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert add_si_prefix(10000) == '10.0 kilo'
    assert add_binary_prefix(65536) == '64.0 kilo'
    from itertools import islice
    positive = SIUnit.get_positive()
    inc = iter(positive.items())
    assert dict(islice(inc, len(positive) // 2)) == {'yotta': 24, 'zetta': 21, 'exa': 18, 'peta': 15, 'tera': 12}
    assert dict(inc) == {'giga': 9, 'mega': 6, 'kilo': 3, 'hecto': 2, 'deca': 1}
    from itertools import islice
    negative = SIUnit.get_negative()
    inc = iter(negative.items())
    assert dict(islice(inc, len(negative) // 2)) == {'deci': -1, 'centi': -2, 'milli': -3, 'micro': -6, 'nano': -9}
    assert dict(inc) == {'pico': -12, 'femto': -15, 'atto': -18, 'zepto': -21, 'yocto': -24}
