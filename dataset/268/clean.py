"""This module contains a class that
calculates the moving average in real-time.

Reference
---------
https://en.wikipedia.org/wiki/Moving_average
"""
from collections import deque

class StreamingMovingAverage:
    """Streaming Moving Average calculator that updates
    the average in real-time.

    Attributes
    ----------
    window_size : int
        The size of the moving average window.

    Methods
    -------
    update(new_value: float) -> None
        Update the moving average with a new data point.
    mov_avg() -> float
        Return the current moving average value.

    Raises
    ------
    ValueError
        If the window size is less than 1.


    Examples
    --------"""

    def __init__(self, window_size: int) -> None:
        if window_size < 1:
            raise ValueError('Window size must be a positive integer')
        self.window_size = window_size
        self.window: deque[float] = deque(maxlen=window_size)
        self._mov_avg: float = 0.0

    def update(self, new_value: float) -> None:
        """Update the moving average with a new data point.

        Parameters
        ----------
        new_value : float
            The new data point to update the moving average.

        Raises
        ------
        TypeError
            If the type of new value is not float.
        """
        if not isinstance(new_value, float):
            raise TypeError('Type of new_value must be either float.')
        self.window.append(new_value)
        self._mov_avg = sum(self.window) / len(self.window)

    @property
    def mov_avg(self) -> float:
        """Return the current moving average value."""
        return self._mov_avg