import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    observations = ["normal", "cold", "dizzy"]
    states = ["Healthy", "Fever"]
    start_p = {"Healthy": 0.6, "Fever": 0.4}
    trans_p = {
    "Healthy": {"Healthy": 0.7, "Fever": 0.3},
    "Fever": {"Healthy": 0.4, "Fever": 0.6},
}
    emit_p = {
    "Healthy": {"normal": 0.5, "cold": 0.4, "dizzy": 0.1},
    "Fever": {"normal": 0.1, "cold": 0.3, "dizzy": 0.6},
}
    assert viterbi(observations, states, start_p, trans_p, emit_p) == ['Healthy', 'Healthy', 'Fever']
    observations = ["normal", "cold", "dizzy"]
    states = ["Healthy", "Fever"]
    start_p = {"Healthy": 0.6, "Fever": 0.4}
    trans_p = {
    "Healthy": {"Healthy": 0.7, "Fever": 0.3},
    "Fever": {"Healthy": 0.4, "Fever": 0.6},
}
    emit_p = {
    "Healthy": {"normal": 0.5, "cold": 0.4, "dizzy": 0.1},
    "Fever": {"normal": 0.1, "cold": 0.3, "dizzy": 0.6},
}
    _validation(observations, states, start_p, trans_p, emit_p)
    _validate_not_empty(["a"], ["b"], {"c":0.5},
{"d": {"e": 0.6}}, {"f": {"g": 0.7}})
    _validate_lists(["a"], ["b"])
    _validate_list(["a"], "mock_name")
    _validate_dicts({"c":0.5}, {"d": {"e": 0.6}}, {"f": {"g": 0.7}})
    _validate_nested_dict({"a":{"b": 0.5}}, "mock_name")
    _validate_dict({"b": 0.5}, "mock_name", float)
