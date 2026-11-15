import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    g1 = GraphUndirectedWeighted[int]()
    g1.add_edge(1, 2, 1)
    g1.add_edge(2, 3, 2)
    g1.add_edge(3, 4, 1)
    g1.add_edge(3, 5, 100) # Removed in MST
    g1.add_edge(4, 5, 5)
    assert 5 in g1.connections[3]
    mst = g1.kruskal()
    assert 5 not in mst.connections[3]
    g2 = GraphUndirectedWeighted[str]()
    g2.add_edge('A', 'B', 1)
    g2.add_edge('B', 'C', 2)
    g2.add_edge('C', 'D', 1)
    g2.add_edge('C', 'E', 100) # Removed in MST
    g2.add_edge('D', 'E', 5)
    assert 'E' in g2.connections["C"]
    mst = g2.kruskal()
    assert 'E' not in mst.connections['C']
