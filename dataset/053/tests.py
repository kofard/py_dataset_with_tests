import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    g = Graph(graph, "G")
    g.breath_first_search()
    assert g.parent == {'G': None, 'C': 'G', 'A': 'C', 'F': 'C', 'B': 'A', 'E': 'A', 'D': 'B'}
    g = Graph(graph, "G")
    g.breath_first_search()
    assert g.shortest_path("D") == 'G->C->A->B->D'
    assert g.shortest_path("G") == 'G'
