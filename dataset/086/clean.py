class DynamicArray:

    def __init__(self) -> None:
        self.size = 0
        self.capacity = 1
        self.array = [None] * self.capacity

    def append(self, item: int) -> None:
        """The function adds an item to the end of the dynamic array.

        Runtime : O(1) amortized
        Space: O(1) amortized"""
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = item
        self.size += 1

    def _resize(self, new_capacity: int) -> None:
        """Resizes the array to the new capacity.

        Runtime : O(n)
        Space: O(n)"""
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def get(self, index: int) -> int:
        """The function returns the item at the specified index.

        Runtime : O(1)
        Space: O(1)"""
        if index < 0 or index >= self.size:
            raise IndexError('index out of range')
        return self.array[index]

    def __setitem__(self, index: int, value: int) -> None:
        if index < 0 or index >= self.size:
            raise IndexError('index out of range')
        self.array[index] = value

    def __len__(self) -> int:
        """Returns the number of elements in the dynamic array.

        Runtime : O(1)
        Space: O(1)"""
        return self.size

    def __str__(self) -> str:
        """Returns a string representation of the dynamic array."""
        return '[' + ', '.join((str(self.array[i]) for i in range(self.size))) + ']'