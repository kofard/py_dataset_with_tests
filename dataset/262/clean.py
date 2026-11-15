from collections.abc import Sequence

def assign_ranks(data: Sequence[float]) -> list[float]:
    """Assigns ranks to elements in the array.

    :param data: List of floats.
    :return: List of floats representing the ranks.

    Example:"""
    n = len(data)
    ranked_data = sorted(((value, index) for index, value in enumerate(data)))
    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j < n - 1 and ranked_data[j + 1][0] == ranked_data[i][0]:
            j += 1
        avg_rank = (i + j) / 2.0 + 1
        for k in range(i, j + 1):
            ranks[ranked_data[k][1]] = avg_rank
        i = j + 1
    return ranks

def calculate_spearman_rank_correlation(variable_1: Sequence[float], variable_2: Sequence[float]) -> float:
    """Calculates Spearman's rank correlation coefficient.

    :param variable_1: List of floats representing the first variable.
    :param variable_2: List of floats representing the second variable.
    :return: Spearman's rank correlation coefficient.
    :raises ValueError: If less than 2 data points are provided.

    Example Usage:"""
    n = len(variable_1)
    if n < 2:
        raise ValueError('Need at least 2 data points to calculate correlation')
    rank_var1 = assign_ranks(variable_1)
    rank_var2 = assign_ranks(variable_2)
    d = [rx - ry for rx, ry in zip(rank_var1, rank_var2)]
    d_squared = sum((di ** 2 for di in d))
    rho = 1 - 6 * d_squared / (n * (n ** 2 - 1))
    return round(rho, 1)