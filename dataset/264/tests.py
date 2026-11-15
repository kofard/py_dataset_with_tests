import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert star_to_delta(complex(2,0),complex(1,0),complex(1,0)) == [(2.5+0j), (5+0j), (5+0j)]
    assert star_to_delta(complex(2,0),complex(1,2),complex(1,6)) == [(-3.5+12j), (8.2+7.6j), (3.702702702702702+1.7837837837837838j)]
    assert delta_to_star(complex(3,0),complex(5,0),complex(7,0)) == [(2.3333333333333335+0j), (1.4+0j), (1+0j)]
    assert delta_to_star(complex(1,3),complex(2,0),complex(0,-3)) == [-2j, (3-1j), (0.6666666666666666+2j)]
