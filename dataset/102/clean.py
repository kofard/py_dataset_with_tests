from dataclasses import dataclass
from operator import attrgetter

@dataclass
class Item:
    weight: int
    value: int

    @property
    def ratio(self) -> float:
        """Return the value-to-weight ratio for the item.

        Returns:
            float: The value-to-weight ratio for the item.

        Examples:"""
        return self.value / self.weight

def fractional_cover(items: list[Item], capacity: int) -> float:
    """Solve the Fractional Cover Problem.

    Args:
        items: A list of items, where each item has weight and value attributes.
        capacity: The maximum weight capacity of the knapsack.

    Returns:
        The maximum value that can be obtained by selecting fractions of items to cover
        the knapsack's capacity.

    Raises:
        ValueError: If capacity is negative.

    Examples:"""
    if capacity < 0:
        raise ValueError('Capacity cannot be negative')
    total_value = 0.0
    remaining_capacity = capacity
    for item in sorted(items, key=attrgetter('ratio'), reverse=True):
        if remaining_capacity == 0:
            break
        weight_taken = min(item.weight, remaining_capacity)
        total_value += weight_taken * item.ratio
        remaining_capacity -= weight_taken
    return total_value