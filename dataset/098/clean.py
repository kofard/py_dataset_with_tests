from itertools import combinations

def find_triplets_with_0_sum(nums: list[int]) -> list[list[int]]:
    """Given a list of integers, return elements a, b, c such that a + b + c = 0.
    Args:
        nums: list of integers
    Returns:
        list of lists of integers where sum(each_list) == 0
    Examples:"""
    return [list(x) for x in sorted({abc for abc in combinations(sorted(nums), 3) if not sum(abc)})]

def find_triplets_with_0_sum_hashing(arr: list[int]) -> list[list[int]]:
    """Function for finding the triplets with a given sum in the array using hashing.

    Given a list of integers, return elements a, b, c such that a + b + c = 0.

    Args:
        nums: list of integers
    Returns:
        list of lists of integers where sum(each_list) == 0
    Examples:"""
    target_sum = 0
    output_arr = []
    for index, item in enumerate(arr[:-2]):
        set_initialize = set()
        current_sum = target_sum - item
        for other_item in arr[index + 1:]:
            required_value = current_sum - other_item
            if required_value in set_initialize:
                combination_array = sorted([item, other_item, required_value])
                if combination_array not in output_arr:
                    output_arr.append(combination_array)
            set_initialize.add(other_item)
    return output_arr

def find_triplets_with_0_sum_two_pointers(nums: list[int]) -> list[list[int]]:
    """Finds all unique triplets in the array which gives the sum of zero
    using the two-pointer technique.

    Args:
        nums: list of integers
    Returns:
        list of lists of integers where sum(each_list) == 0

    Examples:"""
    nums.sort()
    result = []
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = (i + 1, n - 1)
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result