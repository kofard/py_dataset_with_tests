import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert molarity_to_normality(2, 3.1, 0.31) == 20
    assert molarity_to_normality(4, 11.4, 5.7) == 8
    assert moles_to_pressure(0.82, 3, 300) == 90
    assert moles_to_pressure(8.2, 5, 200) == 10
    assert moles_to_volume(0.82, 3, 300) == 90
    assert moles_to_volume(8.2, 5, 200) == 10
    assert pressure_and_volume_to_temperature(0.82, 1, 2) == 20
    assert pressure_and_volume_to_temperature(8.2, 5, 3) == 60
    assert mass_to_moles(36.03, 18.015) == 2.0
    assert mass_to_moles(11.0, 44.01) == 0.25
    assert moles_to_molecules(2) == 1.2044e+24
    assert moles_to_molecules(0.5) == 3.011e+23
