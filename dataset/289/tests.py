import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert term_frequency("to", "To be, or not to be") == 2
    assert document_frequency("first", "This is the first document in the corpus.\nThIsis the second document in the corpus.\nTHIS is the third document in the corpus.") == (1, 3)
    assert inverse_document_frequency(1, 3) == 0.477
    assert inverse_document_frequency(0, 3,True) == 1.477
    assert tf_idf(2, 0.477) == 0.954
