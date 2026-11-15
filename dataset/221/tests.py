import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("clean", Path(__file__).parent / "clean.py")
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
globals().update({k: v for k, v in vars(_module).items() if not k.startswith("__")})

def test_solution():
    array1 = [5, -1, -1, 5, 5, 24, 0]
    quick_sort_3partition(array1, 0, 6)
    assert array1 == [-1, -1, 0, 5, 5, 5, 24]
    array2 = [9, 0, 2, 6]
    quick_sort_3partition(array2, 0, 3)
    assert array2 == [0, 2, 6, 9]
    array3 = []
    quick_sort_3partition(array3, 0, 0)
    assert array3 == []
    nums1 = [0, 5, 3, 1, 2]
    quick_sort_lomuto_partition(nums1, 0, 4)
    assert nums1 == [0, 1, 2, 3, 5]
    nums2 = []
    quick_sort_lomuto_partition(nums2, 0, 0)
    assert nums2 == []
    nums3 = [-2, 5, 0, -4]
    quick_sort_lomuto_partition(nums3, 0, 3)
    assert nums3 == [-4, -2, 0, 5]
    assert lomuto_partition([1,5,7,6], 0, 3) == 2
    list_unsorted = [7, 3, 5, 4, 1, 8, 6]
    array = list_unsorted.copy()
    assert hoare_partition_by_value(array, 5) == 3
    assert array == [1, 3, 4, 5, 7, 8, 6]
    assert hoare_partition_by_value(list_unsorted.copy(), 0) == 0
    assert hoare_partition_by_value(list_unsorted.copy(), 1) == 0
    assert hoare_partition_by_value(list_unsorted.copy(), 2) == 1
    assert hoare_partition_by_value(list_unsorted.copy(), 8) == 6
    assert hoare_partition_by_value(list_unsorted.copy(), 9) == 7
    array = [7, 3, 5, 4, 1, 8, 6]
    assert array[3] == 4
    assert hoare_partition_by_pivot(array, 3) == 2
    assert array == [1, 3, 4, 6, 7, 8, 5]
    array = [2, 2, 8, 0, 3, 7, 2, 1, 8, 8]
    quicksort_hoare(array)
    assert array == [0, 1, 2, 2, 2, 3, 7, 8, 8, 8]
    assert three_way_radix_quicksort([]) == []
    assert three_way_radix_quicksort([1]) == [1]
    assert three_way_radix_quicksort([-5, -2, 1, -2, 0, 1]) == [-5, -2, -2, 0, 1, 1]
    assert three_way_radix_quicksort([1, 2, 5, 1, 2, 0, 0, 5, 2, -1]) == [-1, 0, 0, 1, 1, 2, 2, 2, 5, 5]
