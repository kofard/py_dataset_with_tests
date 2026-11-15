import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert max_load_current(rf=2 , rs=4 , rl=6 , vm=15 ) == Result(name='max_load_current', value=1.25)
    assert max_load_current(rf=2 , rs=4 , rl=6 , vm=0 ) == Result(name='max_load_current', value=0.0)
    assert dc_current(im=2) == Result(name='Idc', value=1.272)
    assert dc_current(im=0) == Result(name='Idc', value=0.0)
    assert dc_voltage(vm=2) == Result(name='Vdc', value=1.272)
    assert dc_voltage(vm=0) == Result(name='Vdc', value=0.0)
    assert max_current(vm=2, rl=5) == Result(name='Max_current_Im', value=0.4)
    assert rms_current(im=10) == Result(name='Irms', value=7.069999999999999)
    assert rms_current(im=0) == Result(name='Irms', value=0.0)
    assert rms_voltage(vm=20) == Result(name='Vrms', value=14.139999999999999)
    assert rms_voltage(vm=0) == Result(name='Vrms', value=0.0)
