import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert sorted(get_distinct_edge(edge_array)) == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    assert get_nodes([['ab', 5, '11111'], ['ac', 5, '11111'], ['df', 5, '11111'],
           ['bd', 5, '11111'], ['bc', 5, '11111']]) == {'11111': ['ab', 'ac', 'df', 'bd', 'bc']}
    assert get_support({5: {'11111': ['ab', 'ac', 'df', 'bd', 'bc']},
             4: {'11101': ['ef', 'eg', 'de', 'fg'], '11011': ['cd']},
             3: {'11001': ['ad'], '10101': ['dg']},
             2: {'10010': ['dh', 'bh'], '11000': ['be'], '10100': ['gh'],
                 '10001': ['ce']},
             1: {'00100': ['fh', 'eh'], '10000': ['hi']}}) == [100.0, 80.0, 60.0, 40.0, 20.0]
    preprocess([['ab-e1', 'ac-e3', 'ad-e5', 'bc-e4', 'bd-e2', 'be-e6', 'bh-e12',
             'cd-e2', 'ce-e4', 'de-e1', 'df-e8', 'dg-e5', 'dh-e10', 'ef-e3',
             'eg-e2', 'fg-e6', 'gh-e6', 'hi-e3']])
