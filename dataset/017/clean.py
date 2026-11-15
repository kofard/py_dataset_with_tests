"""
In this problem, we want to determine all possible combinations of k
numbers out of 1 ... n. We use backtracking to solve this problem.

Time complexity: O(C(n,k)) which is O(n choose k) = O((n!/(k! * (n - k)!))),
"""
from __future__ import annotations
from itertools import combinations

def combination_lists(n: int, k: int) -> list[list[int]]:
    """Generates all possible combinations of k numbers out of 1 ... n using itertools."""
    return [list(x) for x in combinations(range(1, n + 1), k)]

def generate_all_combinations(n: int, k: int) -> list[list[int]]:
    """Generates all possible combinations of k numbers out of 1 ... n using backtracking."""
    if k < 0:
        raise ValueError('k must not be negative')
    if n < 0:
        raise ValueError('n must not be negative')
    result: list[list[int]] = []
    create_all_state(1, n, k, [], result)
    return result

def create_all_state(increment: int, total_number: int, level: int, current_list: list[int], total_list: list[list[int]]) -> None:
    """Helper function to recursively build all combinations."""
    if level == 0:
        total_list.append(current_list[:])
        return
    for i in range(increment, total_number - level + 2):
        current_list.append(i)
        create_all_state(i + 1, total_number, level - 1, current_list, total_list)
        current_list.pop()