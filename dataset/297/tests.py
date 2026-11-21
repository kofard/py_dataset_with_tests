import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})


def test_solution():
    document = {"": "empty", "a/b": {"~key": [10, 20, {"x": 30}]}, "list": ["a", "b"]}
    assert JSONPointer("").get(document) is document
    assert JSONPointer("/").get(document) == "empty"
    assert JSONPointer("/a~1b/~0key/0").get(document) == 10
    assert JSONPointer("/a~1b/~0key/2/x").get(document) == 30
    assert JSONPointer("/list/1").get(document) == "b"
    assert JSONPointer("/a~1b/~0key/2/x").set(document, 99) is document
    assert JSONPointer("/a~1b/~0key/2/x").get(document) == 99
    assert JSONPointer("/list/-").set(document, "c") is document
    assert document["list"] == ["a", "b", "c"]
    assert JSONPointer("/list/0").remove(document) == "a"
    assert document["list"] == ["b", "c"]
    assert JSONPointer("/a~1b/~0key/1").remove(document) == 20
    assert JSONPointer("/a~1b/~0key").get(document) == [10, {"x": 99}]
    assert JSONPointer("").set(document, {"new": 1}) == {"new": 1}

    for invalid in ("abc", "/~", "/a~2", "/~11~3"):
        try:
            JSONPointer(invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid JSON Pointer was accepted")
    for bad_index in ("/list/01", "/list/-1", "/list/100", "/list/-"):
        try:
            JSONPointer(bad_index).get(document)
        except IndexError:
            pass
        else:
            raise AssertionError("invalid array index was accepted")
    try:
        JSONPointer("/not-here").get(document)
    except KeyError:
        pass
    else:
        raise AssertionError("missing key was accepted")
    try:
        JSONPointer("").remove(document)
    except ValueError:
        pass
    else:
        raise AssertionError("deleting the root was accepted")
