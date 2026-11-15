import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert sha256("abc") == 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
    assert len(build_merkle_tree(["a", "b", "c", "d"])[-1][0]) == 64
    r = merkle_root(["tx1", "tx2", "tx3"])
    assert isinstance(r, str) == True
    data = ["a", "b", "c", "d"]
    tree = build_merkle_tree(data)
    root = tree[-1][0]
    leaf = "a"
    proof = [sha256("b"), sha256(sha256("c") + sha256("d"))]
    assert verify_proof(leaf, proof, root) == True
