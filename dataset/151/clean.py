def floyd(n):
    """Print the upper half of a diamond pattern with '*' characters.

    Args:
        n (int): Size of the pattern.

    Examples:"""
    result = ''
    for i in range(n):
        for _ in range(n - i - 1):
            result += ' '
        for _ in range(i + 1):
            result += '* '
        result += '\n'
    return result

def reverse_floyd(n):
    """Print the lower half of a diamond pattern with '*' characters.

    Args:
        n (int): Size of the pattern.

    Examples:"""
    result = ''
    for i in range(n, 0, -1):
        for _ in range(i, 0, -1):
            result += '* '
        result += '\n'
        for _ in range(n - i + 1, 0, -1):
            result += ' '
    return result

def pretty_print(n):
    """Print a complete diamond pattern with '*' characters.

    Args:
        n (int): Size of the pattern.

    Examples:"""
    if n <= 0:
        return '       ...       ....        nothing printing :('
    upper_half = floyd(n)
    lower_half = reverse_floyd(n)
    return upper_half + lower_half