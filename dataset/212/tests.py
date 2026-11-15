import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert round(_reactive_power_difference(60, 120, 4000, 0.8, 0.95), 6) == 1685.263579
    assert shunt_capacitor_power_factor_correction(120,60,4000,0.8,0.95) == 0.00031043753362948597
    assert shunt_capacitor_power_factor_correction(150,50,2000,0.6,0.87) == 0.00021690547192207782
    assert shunt_inductor_power_factor_correction(120,60,4000,0.8,0.95) == 0.02266540783980564
    assert shunt_inductor_power_factor_correction(120,60,4000,-0.8,-0.4) == 0.006195660726930193
