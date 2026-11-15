import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert all(is_palindrome(key) == value for key, value in test_data.items()) == True
    assert is_palindrome("") == True
    assert all(is_palindrome_traversal(key) == value for key, value in test_data.items()) == True
    assert is_palindrome_traversal("") == True
    assert all(is_palindrome_recursive(key) == value for key, value in test_data.items()) == True
    assert is_palindrome_recursive("") == True
    assert all(is_palindrome_slice(key) == value for key, value in test_data.items()) == True
    assert is_palindrome_slice("") == True
    assert is_palindrome_ignore_case_and_spaces("A man a plan a canal Panama") == True
    assert is_palindrome_ignore_case_and_spaces("Was it a car or a cat I saw?") == True
    assert is_palindrome_ignore_case_and_spaces("Hello World") == False
    assert is_palindrome_ignore_case_and_spaces("Never Odd or Even") == True
    assert is_palindrome_ignore_case_and_spaces("") == True
    assert is_palindrome_ignore_case_and_spaces(" !?. ") == True
    assert is_palindrome_ignore_case_and_spaces("1a2") == False
