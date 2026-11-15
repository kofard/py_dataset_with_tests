import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert load_data() == [['milk'], ['milk', 'butter'], ['milk', 'bread'], ['milk', 'bread', 'chips']]
    itemset = ['X', 'Y', 'Z']
    candidates = [['X', 'Y'], ['X', 'Z'], ['Y', 'Z']]
    assert prune(itemset, candidates, 2) == [['X', 'Y'], ['X', 'Z'], ['Y', 'Z']]
    itemset = ['1', '2', '3', '4']
    candidates = ['1', '2', '4']
    assert prune(itemset, candidates, 3) == []
    data = [['A', 'B', 'C'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C']]
    assert apriori(data, 2) == [(['A', 'B'], 1), (['A', 'C'], 2), (['B', 'C'], 2)]
    data = [['1', '2', '3'], ['1', '2'], ['1', '3'], ['1', '4'], ['2', '3']]
    assert apriori(data, 3) == []
