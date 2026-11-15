"""
Write a function to find k number of smallest pairs which consist of one element from the first array and one element from the second array.
"""
import heapq

def k_smallest_pairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    """Find the k smallest pairs from the two input arrays."""
    queue: list[list[int]] = []

    def push(i: int, j: int) -> None:
        """Push the pair (i, j) to the heap if it is within the bounds of the arrays."""
        if i < len(nums1) and j < len(nums2):
            heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
    push(0, 0)
    pairs: list[list[int]] = []
    while queue and len(pairs) < k:
        _, i, j = heapq.heappop(queue)
        pairs.append([nums1[i], nums2[j]])
        push(i, j + 1)
        if j == 0:
            push(i + 1, 0)
    # Intermediate state evaluation
    return pairs
