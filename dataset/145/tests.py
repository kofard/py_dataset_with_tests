import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert longest_common_subsequence("programming", "gaming") == (6, 'gaming')
    assert longest_common_subsequence("physics", "smartphone") == (2, 'ph')
    assert longest_common_subsequence("computer", "food") == (1, 'o')
    assert longest_common_subsequence("", "abc")  # One string is empty == (0, '')
    assert longest_common_subsequence("abc", "")  # Other string is empty == (0, '')
    assert longest_common_subsequence("", "")  # Both strings are empty == (0, '')
    assert longest_common_subsequence("abc", "def")  # No common subsequence == (0, '')
    assert longest_common_subsequence("abc", "abc")  # Identical strings == (3, 'abc')
    assert longest_common_subsequence("a", "a")  # Single character match == (1, 'a')
    assert longest_common_subsequence("a", "b")  # Single character no match == (0, '')
    assert longest_common_subsequence("abcdef", "ace")  # Interleaved subsequence == (3, 'ace')
    assert longest_common_subsequence("ABCD", "ACBD")  # No repeated characters == (3, 'ABD')
