import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    words = 'banana bananas bandana band apple all beast'.split()
    root = TrieNode()
    root.insert_many(words)
    assert all((root.find(word) for word in words))
    assert root.find('banana')
    assert not root.find('bandanas')
    assert not root.find('apps')
    assert root.find('apple')
    assert root.find('all')
    root.delete('all')
    assert not root.find('all')
    root.delete('banana')
    assert not root.find('banana')
    assert root.find('bananas')
    return True
