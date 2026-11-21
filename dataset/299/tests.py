import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})


def test_solution():
    left = BloomFilter(4096, 5)
    right = BloomFilter(4096, 5)
    assert left.inserts == 0
    assert left.to_bytes() == bytes(512)
    assert left.expected_false_positive_rate() == 0.0
    assert not left.might_contain("missing")

    for word in ("apple", "banana", "вишня", b"\x00\xff"):
        left.add(word)
        assert left.might_contain(word)
    for word in ("carrot", "pear", "banana"):
        right.add(word)
        assert right.might_contain(word)
    assert left.inserts == 4
    assert right.inserts == 3
    assert 0 < left.expected_false_positive_rate() < 1

    both = left.union(right)
    for word in ("apple", "banana", "вишня", b"\x00\xff", "carrot", "pear"):
        assert both.might_contain(word)
    assert both.inserts == 7
    assert both.to_bytes() != left.to_bytes()

    intersection = left.intersection(right)
    assert intersection.might_contain("banana")
    assert intersection.inserts == 3

    copy = BloomFilter.from_bytes(4096, 5, left.to_bytes())
    assert copy.to_bytes() == left.to_bytes()
    assert copy.might_contain("apple")
    assert copy.might_contain("вишня")
    assert left.to_bytes() == BloomFilter.from_bytes(4096, 5, copy.to_bytes()).to_bytes()

    for invalid in ((0, 2), (20, 0), (-1, 3), (True, 2)):
        try:
            BloomFilter(*invalid)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid Bloom filter parameters were accepted")
    try:
        left.union(BloomFilter(128, 5))
    except ValueError:
        pass
    else:
        raise AssertionError("incompatible filters were combined")
    try:
        BloomFilter.from_bytes(10, 2, b"x")
    except ValueError:
        pass
    else:
        raise AssertionError("invalid payload was accepted")
    try:
        left.add(123)
    except TypeError:
        pass
    else:
        raise AssertionError("unsupported key type was accepted")
