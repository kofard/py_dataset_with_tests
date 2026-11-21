"""Dynamic-programming solution to weighted interval scheduling."""

from bisect import bisect_right
from math import isfinite


def select_weighted_intervals(
    intervals: list[tuple[float, float, float]],
) -> tuple[float, list[int]]:
    """Maximize weight for non-overlapping [start, end) intervals.

    The returned indices refer to the original input order. Negative-value
    intervals may be omitted, and a result with zero total weight is valid.
    """
    jobs: list[tuple[float, float, float, int]] = []
    for index, item in enumerate(intervals):
        if not isinstance(item, (tuple, list)) or len(item) != 3:
            raise ValueError("each interval must have start, end and weight")
        start, end, weight = item
        if any(isinstance(x, bool) or not isinstance(x, (int, float))
               or not isfinite(x) for x in (start, end, weight)):
            raise ValueError("interval fields must be finite real numbers")
        if start > end:
            raise ValueError("start cannot exceed end")
        jobs.append((start, end, weight, index))

    jobs.sort(key=lambda job: (job[1], job[0], job[3]))
    if not jobs:
        return 0, []

    ends = [job[1] for job in jobs]
    predecessors: list[int] = []
    for position, (start, _, _, _) in enumerate(jobs):
        # Entries in best[] are shifted by one; bisect_right gives that count.
        predecessors.append(bisect_right(ends, start, hi=position))

    best: list[tuple[float, tuple[int, ...]]] = [(0, ())]
    for position, (_, _, weight, original_index) in enumerate(jobs):
        previous_value, previous_path = best[predecessors[position]]
        take = (previous_value + weight, (*previous_path, original_index))
        skip = best[-1]
        if take[0] > skip[0] or (take[0] == skip[0] and take[1] < skip[1]):
            best.append(take)
        else:
            best.append(skip)

    optimum, selected = best[-1]
    return optimum, list(selected)


def compatible_intervals(intervals: list[tuple[float, float, float]], indices: list[int]) -> bool:
    """Check chronological compatibility of a selected subset."""
    selected = [intervals[index] for index in indices]
    for earlier, later in zip(selected, selected[1:]):
        if earlier[1] > later[0]:
            return False
    return True


def total_weight(intervals: list[tuple[float, float, float]], indices: list[int]) -> float:
    return sum(intervals[index][2] for index in indices)
