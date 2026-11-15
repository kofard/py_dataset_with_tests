import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    assert hsv_to_rgb(0, 0, 0) == [0, 0, 0]
    assert hsv_to_rgb(0, 0, 1) == [255, 255, 255]
    assert hsv_to_rgb(0, 1, 1) == [255, 0, 0]
    assert hsv_to_rgb(60, 1, 1) == [255, 255, 0]
    assert hsv_to_rgb(120, 1, 1) == [0, 255, 0]
    assert hsv_to_rgb(240, 1, 1) == [0, 0, 255]
    assert hsv_to_rgb(300, 1, 1) == [255, 0, 255]
    assert hsv_to_rgb(180, 0.5, 0.5) == [64, 128, 128]
    assert hsv_to_rgb(234, 0.14, 0.88) == [193, 196, 224]
    assert hsv_to_rgb(330, 0.75, 0.5) == [128, 32, 80]
    assert approximately_equal_hsv(rgb_to_hsv(0, 0, 0), [0, 0, 0]) == True
    assert approximately_equal_hsv(rgb_to_hsv(255, 255, 255), [0, 0, 1]) == True
    assert approximately_equal_hsv(rgb_to_hsv(255, 0, 0), [0, 1, 1]) == True
    assert approximately_equal_hsv(rgb_to_hsv(255, 255, 0), [60, 1, 1]) == True
    assert approximately_equal_hsv(rgb_to_hsv(0, 255, 0), [120, 1, 1]) == True
    assert approximately_equal_hsv(rgb_to_hsv(0, 0, 255), [240, 1, 1]) == True
    assert approximately_equal_hsv(rgb_to_hsv(255, 0, 255), [300, 1, 1]) == True
    assert approximately_equal_hsv(rgb_to_hsv(64, 128, 128), [180, 0.5, 0.5]) == True
    assert approximately_equal_hsv(rgb_to_hsv(193, 196, 224), [234, 0.14, 0.88]) == True
    assert approximately_equal_hsv(rgb_to_hsv(128, 32, 80), [330, 0.75, 0.5]) == True
    assert approximately_equal_hsv([0, 0, 0], [0, 0, 0]) == True
    assert approximately_equal_hsv([180, 0.5, 0.3], [179.9999, 0.500001, 0.30001]) == True
    assert approximately_equal_hsv([0, 0, 0], [1, 0, 0]) == False
    assert approximately_equal_hsv([180, 0.5, 0.3], [179.9999, 0.6, 0.30001]) == False
