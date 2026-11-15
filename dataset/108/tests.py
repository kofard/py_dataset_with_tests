import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    gas_stations = get_gas_stations([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])
    assert len(gas_stations) == 5
    assert gas_stations[0] == GasStation(gas_quantity=1, cost=3)
    assert gas_stations[-1] == GasStation(gas_quantity=5, cost=2)
    assert can_complete_journey(get_gas_stations([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])) == 3
    assert can_complete_journey(get_gas_stations([2, 3, 4], [3, 4, 3])) == -1
