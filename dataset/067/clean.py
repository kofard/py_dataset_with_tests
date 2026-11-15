"""
Assumption:
    - The values to compress are assumed to be comparable,
      values can be sorted and compared with '<' and '>' operators.
"""

class CoordinateCompressor:
    """
    A class for coordinate compression.

    This class allows you to compress and decompress a list of values.

    Mapping:
    In addition to compression and decompression, this class maintains a mapping
    between original values and their compressed counterparts using two data
    structures: a dictionary `coordinate_map` and a list `reverse_map`:
    - `coordinate_map`: A dictionary that maps original values to their compressed
      coordinates. Keys are original values, and values are compressed coordinates.
    - `reverse_map`: A list used for reverse mapping, where each index corresponds
      to a compressed coordinate, and the value at that index is the original value.

    Example of mapping:
    Original: 10, Compressed: 0
    Original: 52, Compressed: 1
    Original: 83, Compressed: 2
    Original: 100, Compressed: 3

    This mapping allows for efficient compression and decompression of values within
    the list.
    """

    def __init__(self, arr: list[int | float | str]) -> None:
        """Initialize the CoordinateCompressor with a list.

        Args:
        arr: The list of values to be compressed."""
        self.coordinate_map: dict[int | float | str, int] = {}
        self.reverse_map: list[int | float | str] = [-1] * len(arr)
        self.arr = sorted(arr)
        self.n = len(arr)
        self.compress_coordinates()

    def compress_coordinates(self) -> None:
        """Compress the coordinates in the input list."""
        key = 0
        for val in self.arr:
            if val not in self.coordinate_map:
                self.coordinate_map[val] = key
                self.reverse_map[key] = val
                key += 1

    def compress(self, original: float | str) -> int:
        """Compress a single value.

        Args:
        original: The value to compress.

        Returns:
        The compressed integer.

        Raises:
        KeyError: If ``original`` was not part of the input list."""
        return self.coordinate_map[original]

    def decompress(self, num: int) -> int | float | str:
        """Decompress a single integer.

        Args:
        num: The compressed integer to decompress.

        Returns:
        The original value.

        Raises:
        IndexError: If ``num`` is not a valid compressed coordinate."""
        if not 0 <= num < len(self.reverse_map):
            msg = f'compressed coordinate {num} is out of range'
            raise IndexError(msg)
        return self.reverse_map[num]