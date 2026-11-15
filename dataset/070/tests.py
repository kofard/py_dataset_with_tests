import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert get_set_bits_count_using_brian_kernighans_algorithm(25) == 3
    assert get_set_bits_count_using_brian_kernighans_algorithm(37) == 3
    assert get_set_bits_count_using_brian_kernighans_algorithm(21) == 3
    assert get_set_bits_count_using_brian_kernighans_algorithm(58) == 4
    assert get_set_bits_count_using_brian_kernighans_algorithm(0) == 0
    assert get_set_bits_count_using_brian_kernighans_algorithm(256) == 1
    assert get_set_bits_count_using_brian_kernighans_algorithm(1023) == 10
    assert get_set_bits_count_using_modulo_operator(25) == 3
    assert get_set_bits_count_using_modulo_operator(37) == 3
    assert get_set_bits_count_using_modulo_operator(21) == 3
    assert get_set_bits_count_using_modulo_operator(58) == 4
    assert get_set_bits_count_using_modulo_operator(0) == 0
    assert get_set_bits_count_using_modulo_operator(256) == 1
    assert get_set_bits_count_using_modulo_operator(1024) == 1
    assert get_set_bits_count_using_lookup_table(25) == 3
    assert get_set_bits_count_using_lookup_table(37) == 3
    assert get_set_bits_count_using_lookup_table(21) == 3
    assert get_set_bits_count_using_lookup_table(58) == 4
    assert get_set_bits_count_using_lookup_table(0) == 0
    assert get_set_bits_count_using_lookup_table(256) == 1
