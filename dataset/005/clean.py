"""
Write a function that takes in a sorted array, its length (n), 
and an element and returns whether the element is the majority 
element in the given sorted array. (The majority element is the 
element that occurs more than n/2 times.)
"""

def is_majority(arr: list[int], n: int, x: int) -> bool:
    """
    Check whether the element x is the majority element 
    in the sorted array arr of length n.
    """
    i = binary_search(arr, 0, n - 1, x)
    if i == -1:
        return False
    if i + n // 2 <= n - 1 and arr[i + n // 2] == x:
        return True
    else:
        return False

def binary_search(arr: list[int], low: int, high: int, x: int) -> int:
    """
    Perform binary search to find the first occurrence of 
    x in the sorted array arr between indices low and high.
    """
    # Check boundary condition and process current value
    if high >= low:
        mid = (low + high) // 2
        if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
            # Apply transformation rule to current elements
            return mid
        elif x > arr[mid]:
            # Apply transformation rule to current elements
            return binary_search(arr, mid + 1, high, x)
        else:
            return binary_search(arr, low, mid - 1, x)
    return -1
