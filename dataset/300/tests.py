import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})


def test_solution():
    prereleases = [
        "1.0.0-alpha", "1.0.0-alpha.1", "1.0.0-alpha.beta",
        "1.0.0-beta", "1.0.0-beta.2", "1.0.0-beta.11",
        "1.0.0-rc.1", "1.0.0",
    ]
    assert [str(value) for value in sorted(Version(x) for x in reversed(prereleases))] == prereleases
    assert Version("1.2.3+build.5") == Version("1.2.3+other")
    assert Version("1.2.4") > Version("1.2.3")
    assert Version("2.0.0") > Version("1.99.99")
    assert Version("1.0.0-alpha.9") < Version("1.0.0-alpha.10")
    assert Version("1.0.0-alpha") < Version("1.0.0-alpha.1")
    assert Version("1.0.0-a") > Version("1.0.0-1")
    assert str(Version("1.2.3+metadata")) == "1.2.3+metadata"

    assert satisfies("1.2.3", "")
    assert satisfies("1.2.3", ">=1.0.0, <2.0.0")
    assert not satisfies("2.1.0", ">=1.0.0, <2.0.0")
    assert satisfies("1.9.0", "^1.2.3")
    assert not satisfies("2.0.0", "^1.2.3")
    assert satisfies("0.2.9", "^0.2.3")
    assert not satisfies("0.3.0", "^0.2.3")
    assert satisfies("0.0.4", "^0.0.4")
    assert not satisfies("0.0.5", "^0.0.4")
    assert satisfies("1.2.99", "~1.2.3")
    assert not satisfies("1.3.0", "~1.2.3")
    assert satisfies("1.2.3", "==1.2.3")
    assert not satisfies("1.2.3", "!=1.2.3")
    assert satisfies("1.2.3", "1.2.3")
    assert satisfies(Version("1.2.3"), ">1.2.2, <=1.2.3")

    for invalid in ("1.2", "01.2.3", "1.2.3-01", "1.2.3-", "1.2.3+", "v1.2.3", "1.2.3-alpha..1"):
        try:
            Version(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid version was accepted")
    try:
        satisfies("1.0.0", ">=1.0.0,")
    except ValueError:
        pass
    else:
        raise AssertionError("empty constraint was accepted")
