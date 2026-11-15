import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert can_string_be_rearranged_as_palindrome_counter("Momo") == True
    assert can_string_be_rearranged_as_palindrome_counter("Mother") == False
    assert can_string_be_rearranged_as_palindrome_counter("Father") == False
    assert can_string_be_rearranged_as_palindrome_counter("A man a plan a canal Panama") == True
    assert can_string_be_rearranged_as_palindrome("Momo") == True
    assert can_string_be_rearranged_as_palindrome("Mother") == False
    assert can_string_be_rearranged_as_palindrome("Father") == False
    assert can_string_be_rearranged_as_palindrome_counter("A man a plan a canal Panama") == True
