import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert celsius_to_fahrenheit(273.354, 3) == 524.037
    assert celsius_to_fahrenheit(273.354, 0) == 524.0
    assert celsius_to_fahrenheit(-40.0) == -40.0
    assert celsius_to_fahrenheit(-20.0) == -4.0
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(20) == 68.0
    assert celsius_to_fahrenheit("40") == 104.0
    assert celsius_to_kelvin(273.354, 3) == 546.504
    assert celsius_to_kelvin(273.354, 0) == 547.0
    assert celsius_to_kelvin(0) == 273.15
    assert celsius_to_kelvin(20.0) == 293.15
    assert celsius_to_kelvin("40") == 313.15
    assert celsius_to_rankine(273.354, 3) == 983.707
    assert celsius_to_rankine(273.354, 0) == 984.0
    assert celsius_to_rankine(0) == 491.67
    assert celsius_to_rankine(20.0) == 527.67
    assert celsius_to_rankine("40") == 563.67
    assert fahrenheit_to_celsius(273.354, 3) == 134.086
    assert fahrenheit_to_celsius(273.354, 0) == 134.0
    assert fahrenheit_to_celsius(0) == -17.78
    assert fahrenheit_to_celsius(20.0) == -6.67
    assert fahrenheit_to_celsius(40.0) == 4.44
    assert fahrenheit_to_celsius(60) == 15.56
    assert fahrenheit_to_celsius(80) == 26.67
    assert fahrenheit_to_celsius("100") == 37.78
    assert fahrenheit_to_kelvin(273.354, 3) == 407.236
    assert fahrenheit_to_kelvin(273.354, 0) == 407.0
    assert fahrenheit_to_kelvin(0) == 255.37
    assert fahrenheit_to_kelvin(20.0) == 266.48
    assert fahrenheit_to_kelvin(40.0) == 277.59
    assert fahrenheit_to_kelvin(60) == 288.71
    assert fahrenheit_to_kelvin(80) == 299.82
    assert fahrenheit_to_kelvin("100") == 310.93
    assert fahrenheit_to_rankine(273.354, 3) == 733.024
    assert fahrenheit_to_rankine(273.354, 0) == 733.0
    assert fahrenheit_to_rankine(0) == 459.67
    assert fahrenheit_to_rankine(20.0) == 479.67
    assert fahrenheit_to_rankine(40.0) == 499.67
    assert fahrenheit_to_rankine(60) == 519.67
    assert fahrenheit_to_rankine(80) == 539.67
    assert fahrenheit_to_rankine("100") == 559.67
    assert kelvin_to_celsius(273.354, 3) == 0.204
    assert kelvin_to_celsius(273.354, 0) == 0.0
    assert kelvin_to_celsius(273.15) == 0.0
    assert kelvin_to_celsius(300) == 26.85
    assert kelvin_to_celsius("315.5") == 42.35
    assert kelvin_to_fahrenheit(273.354, 3) == 32.367
    assert kelvin_to_fahrenheit(273.354, 0) == 32.0
    assert kelvin_to_fahrenheit(273.15) == 32.0
    assert kelvin_to_fahrenheit(300) == 80.33
    assert kelvin_to_fahrenheit("315.5") == 108.23
    assert kelvin_to_rankine(273.354, 3) == 492.037
    assert kelvin_to_rankine(273.354, 0) == 492.0
    assert kelvin_to_rankine(0) == 0.0
    assert kelvin_to_rankine(20.0) == 36.0
    assert kelvin_to_rankine("40") == 72.0
    assert rankine_to_celsius(273.354, 3) == -121.287
    assert rankine_to_celsius(273.354, 0) == -121.0
    assert rankine_to_celsius(273.15) == -121.4
    assert rankine_to_celsius(300) == -106.48
    assert rankine_to_celsius("315.5") == -97.87
    assert rankine_to_fahrenheit(273.15) == -186.52
    assert rankine_to_fahrenheit(300) == -159.67
    assert rankine_to_fahrenheit("315.5") == -144.17
    assert rankine_to_kelvin(0) == 0.0
    assert rankine_to_kelvin(20.0) == 11.11
    assert rankine_to_kelvin("40") == 22.22
    assert reaumur_to_kelvin(0) == 273.15
    assert reaumur_to_kelvin(20.0) == 298.15
    assert reaumur_to_kelvin(40) == 323.15
    assert reaumur_to_fahrenheit(0) == 32.0
    assert reaumur_to_fahrenheit(20.0) == 77.0
    assert reaumur_to_fahrenheit(40) == 122.0
    assert reaumur_to_celsius(0) == 0.0
    assert reaumur_to_celsius(20.0) == 25.0
    assert reaumur_to_celsius(40) == 50.0
    assert reaumur_to_rankine(0) == 491.67
    assert reaumur_to_rankine(20.0) == 536.67
    assert reaumur_to_rankine(40) == 581.67
