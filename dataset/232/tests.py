import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert get_significant_digits(['Black','Blue']) == '06'
    assert get_multiplier('Gold') == 0.1
    assert get_tolerance('Green') == 0.5
    assert get_temperature_coeffecient('Yellow') == 25
    assert get_band_type_count(3,'significant') == 2
    assert check_validity(3, ["Black","Blue","Orange"]) == True
    assert calculate_resistance(3, ["Black","Blue","Orange"]) == {'resistance': '6000Ω ±20% '}
    assert calculate_resistance(4, ["Orange","Green","Blue","Gold"]) == {'resistance': '35000000Ω ±5% '}
    assert calculate_resistance(5, ["Violet","Brown","Grey","Silver","Green"]) == {'resistance': '7.18Ω ±0.5% '}
    assert calculate_resistance(6, ["Red","Green","Blue","Yellow","Orange","Grey"]) == {'resistance': '2560000Ω ±0.05% 1 ppm/K'}
