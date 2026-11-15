import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert text_justification("This is an example of text justification.", 16) == ['This    is    an', 'example  of text', 'justification.  ']
    assert text_justification("Two roads diverged in a yellow wood", 16) == ['Two        roads', 'diverged   in  a', 'yellow wood     ']
