import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert get_word_pattern("") == ''
    assert get_word_pattern(" ") == '0'
    assert get_word_pattern("pattern") == '0.1.2.2.3.4.5'
    assert get_word_pattern("word pattern") == '0.1.2.3.4.5.6.7.7.8.2.9'
    assert get_word_pattern("get word pattern") == '0.1.2.3.4.5.6.7.3.8.9.2.2.1.6.10'
