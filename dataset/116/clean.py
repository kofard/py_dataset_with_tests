"""
Harmonic mean
Reference: https://en.wikipedia.org/wiki/Harmonic_mean

Harmonic series
Reference: https://en.wikipedia.org/wiki/Harmonic_series(mathematics)
"""

def is_harmonic_series(series: list) -> bool:
    """checking whether the input series is arithmetic series or not"""
    if not isinstance(series, list):
        raise ValueError('Input series is not valid, valid series - [1, 2/3, 2]')
    if len(series) == 0:
        raise ValueError('Input list must be a non empty list')
    if len(series) == 1 and series[0] != 0:
        return True
    rec_series = []
    series_len = len(series)
    for i in range(series_len):
        if series[i] == 0:
            raise ValueError('Input series cannot have 0 as an element')
        rec_series.append(1 / series[i])
    common_diff = rec_series[1] - rec_series[0]
    for index in range(2, series_len):
        if rec_series[index] - rec_series[index - 1] != common_diff:
            return False
    return True

def harmonic_mean(series: list) -> float:
    """return the harmonic mean of series"""
    if not isinstance(series, list):
        raise ValueError('Input series is not valid, valid series - [2, 4, 6]')
    if len(series) == 0:
        raise ValueError('Input list must be a non empty list')
    answer = 0
    for val in series:
        answer += 1 / val
    return len(series) / answer