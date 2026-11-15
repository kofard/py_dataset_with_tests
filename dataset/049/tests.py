import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    ids = [73, 32, 97, 109, 32, 74, 111, 110, 83, 110, 111, 119, 46]
    assert get_byte_pair_counts(ids) == {(73, 32): 1, (32, 97): 1, (97, 109): 1, (109, 32): 1, (32, 74): 1, (74, 111): 1, (111, 110): 1, (110, 83): 1, (83, 110): 1, (110, 111): 1, (111, 119): 1, (119, 46): 1}
    ids = [2, 3, 6, 2, 3, 6, 2, 5]
    assert get_byte_pair_counts(ids) == {(2, 3): 2, (3, 6): 2, (6, 2): 2, (2, 5): 1}
    ids = [2, 3, 6, 2, 3, 6, 2, 5]
    pair = (2, 3)
    idx = 256
    assert merge(ids, pair, idx) == [256, 6, 256, 6, 2, 5]
    t = Tokenizer()
    text = "I am JonSnow."
    assert t.encode(text) == [73, 32, 97, 109, 32, 74, 111, 110, 83, 110, 111, 119, 46]
    t = Tokenizer()
    text = ""
    assert t.encode(text) == []
    t = Tokenizer()
    ids = [73, 32, 97, 109, 32, 74, 111, 110, 83, 110, 111, 119, 46]
    assert t.decode(ids) == 'I am JonSnow.'
    t = Tokenizer()
    ids = []
    assert t.decode(ids) == ''
