import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert get_frequency_order('Hello World') == 'LOWDRHEZQXJKVBPYGFMUCSNIAT'
    assert get_frequency_order('Hello@') == 'LHOEZQXJKVBPYGFWMUCDRSNIAT'
    assert get_frequency_order('h') == 'HZQXJKVBPYGFWMUCLDRSNIOATE'
    assert english_freq_match_score('Hello World') == 1
