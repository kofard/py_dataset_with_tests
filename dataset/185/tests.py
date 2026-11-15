import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert needleman_wunsch(
    "GCATGCG", "GATTACA", match_score=1, mismatch_score=-1, gap_score=-1
) == ('GCA-TGCG', 'G-ATTACA', 0)
    assert needleman_wunsch(
    "ACGT", "ACGT", match_score=2, mismatch_score=-1, gap_score=-2
) == ('ACGT', 'ACGT', 8)
    assert needleman_wunsch(
    "AAAA", "TTTT", match_score=1, mismatch_score=-1, gap_score=-2
) == ('AAAA', 'TTTT', -4)
    assert needleman_wunsch("AGTC", "", match_score=1, mismatch_score=-1, gap_score=-1) == ('AGTC', '----', -4)
    assert needleman_wunsch("", "") == ('', '', 0)
    assert needleman_wunsch(
    "HEAGAWGHEE", "PAWHEAE", match_score=2, mismatch_score=-1, gap_score=-2
) == ('HEAGAWGHE-E', '---PAW-HEAE', -1)
