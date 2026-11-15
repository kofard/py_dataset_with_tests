"""
Given an array of integers and an integer k, find the kth largest element in the array.

https://stackoverflow.com/questions/251781
"""

def partition(arr: list[int], low: int, high: int) -> int:
    """Partitions list based on the pivot element.

    This function rearranges the elements in the input list 'elements' such that
    all elements greater than or equal to the chosen pivot are on the right side
    of the pivot, and all elements smaller than the pivot are on the left side.

    Args:
        arr: The list to be partitioned
        low: The lower index of the list
        high: The higher index of the list

    Returns:
        int: The index of pivot element after partitioning

        Examples:"""
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = (arr[j], arr[i])
    arr[i + 1], arr[high] = (arr[high], arr[i + 1])
    return i + 1

def kth_largest_element(arr: list[int], position: int) -> int:
    """Finds the kth largest element in a list.
    Should deliver similar results to:
    ```python
    def kth_largest_element(arr, position):
        return sorted(arr)[-position]
    ```

    Args:
        nums: The list of numbers.
        k: The position of the desired kth largest element.

    Returns:
        int: The kth largest element.

    Examples:"""
    if not arr:
        return -1
    if not isinstance(position, int):
        raise ValueError('The position should be an integer')
    if not 1 <= position <= len(arr):
        raise ValueError("Invalid value of 'position'")
    low, high = (0, len(arr) - 1)
    while low <= high:
        if low > len(arr) - 1 or high < 0:
            return -1
        pivot_index = partition(arr, low, high)
        if pivot_index == position - 1:
            return arr[pivot_index]
        elif pivot_index > position - 1:
            high = pivot_index - 1
        else:
            low = pivot_index + 1
    return -1