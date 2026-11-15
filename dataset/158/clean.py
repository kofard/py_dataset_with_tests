class MaxFenwickTree:
    """Maximum Fenwick Tree

    More info: https://cp-algorithms.com/data_structures/fenwick.html
    ---------"""

    def __init__(self, size: int) -> None:
        """
        Create empty Maximum Fenwick Tree with specified size

        Parameters:
            size: size of Array

        Returns:
            None
        """
        self.size = size
        self.arr = [0] * size
        self.tree = [0] * size

    @staticmethod
    def get_next(index: int) -> int:
        """
        Get next index in O(1)
        """
        return index | index + 1

    @staticmethod
    def get_prev(index: int) -> int:
        """
        Get previous index in O(1)
        """
        return (index & index + 1) - 1

    def update(self, index: int, value: int) -> None:
        """
        Set index to value in O(lg^2 N)

        Parameters:
            index: index to update
            value: value to set

        Returns:
            None
        """
        old_value = self.arr[index]
        if value == old_value:
            return
        self.arr[index] = value
        while index < self.size:
            old_maximum = self.tree[index]
            if value > old_maximum:
                self.tree[index] = value
            elif old_value == old_maximum:
                current_left_border = self.get_prev(index) + 1
                maximum = self.arr[index]
                if current_left_border != index:
                    maximum = max(0, maximum)
                child = index - 1
                while child >= current_left_border:
                    maximum = max(maximum, self.tree[child])
                    if maximum == old_maximum:
                        break
                    child = self.get_prev(child)
                self.tree[index] = maximum
                if maximum == old_maximum:
                    break
            else:
                break
            index = self.get_next(index)

    def query(self, left: int, right: int) -> int:
        """
        Answer the query of maximum range [l, r) in O(lg^2 N)

        Parameters:
            left: left index of query range (inclusive)
            right: right index of query range (exclusive)

        Returns:
            Maximum value of range [left, right)
        """
        right -= 1
        result = 0
        while left <= right:
            current_left = self.get_prev(right)
            if left <= current_left:
                result = max(result, self.tree[right])
                right = current_left
            else:
                result = max(result, self.arr[right])
                right -= 1
        return result