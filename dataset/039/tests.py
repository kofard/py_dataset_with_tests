import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert encode("hello") == 'AABBBAABAAABABAABABAABBAB'
    assert encode("hello world") == 'AABBBAABAAABABAABABAABBAB BABAAABBABBAAAAABABAAAABB'
    assert decode("AABBBAABAAABABAABABAABBAB BABAAABBABBAAAAABABAAAABB") == 'hello world'
    assert decode("AABBBAABAAABABAABABAABBAB") == 'hello'
