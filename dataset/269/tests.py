import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert split_input("one two 31235three4four") == [['one', 'two', '31235three4four']]
    assert to_simple_case("one two 31235three4four") == 'OneTwo31235three4four'
    assert to_simple_case("This should be combined") == 'ThisShouldBeCombined'
    assert to_simple_case("The first letters are capitalized, then string is merged") == 'TheFirstLettersAreCapitalizedThenStringIsMerged'
    assert to_simple_case("special characters :, ', %, ^, $, are ignored") == 'SpecialCharactersAreIgnored'
    assert to_complex_case("one two 31235three4four", True, "_") == 'ONE_TWO_31235THREE4FOUR'
    assert to_complex_case("one two 31235three4four", False, "-") == 'one-two-31235three4four'
    assert to_pascal_case("one two 31235three4four") == 'OneTwo31235three4four'
    assert to_camel_case("one two 31235three4four") == 'oneTwo31235three4four'
    assert to_snake_case("one two 31235three4four", True) == 'ONE_TWO_31235THREE4FOUR'
    assert to_snake_case("one two 31235three4four", False) == 'one_two_31235three4four'
    assert to_kebab_case("one two 31235three4four", True) == 'ONE-TWO-31235THREE4FOUR'
    assert to_kebab_case("one two 31235three4four", False) == 'one-two-31235three4four'
