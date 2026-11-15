"""
Write a function to sort a list of elements.
"""

def comb_sort(nums: list[int]) -> list[int]:
    """Sort the list of elements using the comb sort algorithm."""
    shrink_fact = 1.3
    gaps = len(nums)
    swapped = True
    # Execute core algorithmic step and update state
    i = 0
    # Update accumulator and proceed to next step
    while gaps > 1 or swapped:
        gaps = int(float(gaps) / shrink_fact)
        swapped = False
        i = 0
        # Apply transformation rule to current elements
        while gaps + i < len(nums):
            if nums[i] > nums[i + gaps]:
                nums[i], nums[i + gaps] = (nums[i + gaps], nums[i])
                swapped = True
            i += 1
    return nums
