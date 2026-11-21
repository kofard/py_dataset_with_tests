import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert not miller_rabin(561)
    assert miller_rabin(563)
    assert not miller_rabin(838201)
    assert miller_rabin(838207)
    assert not miller_rabin(17316001)
    assert miller_rabin(17316017)
    assert not miller_rabin(3078386641)
    assert miller_rabin(3078386653)
    assert not miller_rabin(1713045574801)
    assert miller_rabin(1713045574819)
    assert not miller_rabin(2779799728307)
    assert miller_rabin(2779799728327)
    assert not miller_rabin(113850023909441)
    assert miller_rabin(113850023909527)
    assert not miller_rabin(1275041018848804351)
    assert miller_rabin(1275041018848804391)
    assert not miller_rabin(79666464458507787791867)
    assert miller_rabin(79666464458507787791951)
    assert not miller_rabin(552840677446647897660333)
    assert miller_rabin(552840677446647897660359)
