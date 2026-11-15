import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert is_pangram("The quick brown fox jumps over the lazy dog") == True
    assert is_pangram("Waltz, bad nymph, for quick jigs vex.") == True
    assert is_pangram("Jived fox nymph grabs quick waltz.") == True
    assert is_pangram("My name is Unknown") == False
    assert is_pangram("The quick brown fox jumps over the la_y dog") == False
    assert is_pangram() == True
    assert is_pangram_faster("The quick brown fox jumps over the lazy dog") == True
    assert is_pangram_faster("Waltz, bad nymph, for quick jigs vex.") == True
    assert is_pangram_faster("Jived fox nymph grabs quick waltz.") == True
    assert is_pangram_faster("The quick brown fox jumps over the la_y dog") == False
    assert is_pangram_faster() == True
    assert is_pangram_fastest("The quick brown fox jumps over the lazy dog") == True
    assert is_pangram_fastest("Waltz, bad nymph, for quick jigs vex.") == True
    assert is_pangram_fastest("Jived fox nymph grabs quick waltz.") == True
    assert is_pangram_fastest("The quick brown fox jumps over the la_y dog") == False
    assert is_pangram_fastest() == True
