import heapq
import random
'\nKirkpatrick-Reisch sorting algorithm.\nDivides input into sqrt(n) blocks, sorts each, then merges using a min-heap.\n\nTime Complexity:\n- Average case: O(n * sqrt(n))\n- Worst case: O(n * sqrt(n))\n- Best case: O(n * sqrt(n))\n\nSpace Complexity: O(n)\n\nExplanation Links:\nhttps://en.wikipedia.org/wiki/Kirkpatrick%E2%80%93Reisch_sort\nhttps://sortingsearching.com/2020/06/06/kirkpatrick-reisch.html\n'

def kirkpatrick_reisch_sort(arr: list[int]) -> list[int]:
    """Implements the Kirkpatrick-Reisch sorting algorithm.

    Args:
    arr (list): The input list to be sorted.

    Returns:
    list: A new list containing the sorted elements.

    Examples:"""
    n = len(arr)
    if n <= 1:
        return arr
    block_size = int(n ** 0.5)
    blocks = [arr[i:i + block_size] for i in range(0, n, block_size)]
    for block in blocks:
        block.sort()
    heap = [(block[0], i, 0) for i, block in enumerate(blocks) if block]
    heapq.heapify(heap)
    sorted_arr = []
    while heap:
        val, block_index, element_index = heapq.heappop(heap)
        sorted_arr.append(val)
        if element_index + 1 < len(blocks[block_index]):
            next_element = blocks[block_index][element_index + 1]
            heapq.heappush(heap, (next_element, block_index, element_index + 1))
    return sorted_arr