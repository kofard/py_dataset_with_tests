"""
The Simple Moving Average (SMA) is a statistical calculation used to analyze data points
by creating a constantly updated average price over a specific time period.
In finance, SMA is often used in time series analysis to smooth out price data
and identify trends.

Reference: https://en.wikipedia.org/wiki/Moving_average
"""
from collections.abc import Sequence

def simple_moving_average(data: Sequence[float], window_size: int) -> list[float | None]:
    """Calculate the simple moving average (SMA) for some given time series data.

    :param data: A list of numerical data points.
    :param window_size: An integer representing the size of the SMA window.
    :return: A list of SMA values with the same length as the input data.

    Examples:"""
    if window_size < 1:
        raise ValueError('Window size must be a positive integer')
    sma: list[float | None] = []
    for i in range(len(data)):
        if i < window_size - 1:
            sma.append(None)
        else:
            window = data[i - window_size + 1:i + 1]
            sma_value = sum(window) / window_size
            sma.append(sma_value)
    return sma