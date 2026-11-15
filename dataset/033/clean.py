"""
Arithmetic mean
Reference: https://en.wikipedia.org/wiki/Arithmetic_mean

Arithmetic series
Reference: https://en.wikipedia.org/wiki/Arithmetic_series
(The URL above will redirect you to arithmetic progression)
"""

def is_arithmetic_series(series: list) -> bool:
    """checking whether the input series is arithmetic series or not"""
    if not isinstance(series, list):
        raise ValueError('Input series is not valid, valid series - [2, 4, 6]')
    if len(series) == 0:
        raise ValueError('Input list must be a non empty list')
    if len(series) == 1:
        return True
    common_diff = series[1] - series[0]
    for index in range(len(series) - 1):
        if series[index + 1] - series[index] != common_diff:
            return False
    return True

def arithmetic_mean(series: list) -> float:
    """return the arithmetic mean of series"""
    if not isinstance(series, list):
        raise ValueError('Input series is not valid, valid series - [2, 4, 6]')
    if len(series) == 0:
        raise ValueError('Input list must be a non empty list')
    answer = 0
    for val in series:
        answer += val
    return answer / len(series)