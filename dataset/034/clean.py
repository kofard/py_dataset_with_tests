"""
Binary Exponentiation

This is a method to find a^b in O(log b) time complexity and is one of the most commonly
used methods of exponentiation. The method is also useful for modular exponentiation,
when the solution to (a^b) % c is required.

To calculate a^b:
- If b is even, then a^b = (a * a)^(b / 2)
- If b is odd, then a^b = a * a^(b - 1)
Repeat until b = 1 or b = 0

For modular exponentiation, we use the fact that (a * b) % c = ((a % c) * (b % c)) % c
"""

def binary_exp_recursive(base: float, exponent: int) -> float:
    """Computes a^b recursively, where a is the base and b is the exponent"""
    if exponent < 0:
        raise ValueError('Exponent must be a non-negative integer')
    if exponent == 0:
        return 1
    if exponent % 2 == 1:
        return binary_exp_recursive(base, exponent - 1) * base
    b = binary_exp_recursive(base, exponent // 2)
    return b * b

def binary_exp_iterative(base: float, exponent: int) -> float:
    """Computes a^b iteratively, where a is the base and b is the exponent"""
    if exponent < 0:
        raise ValueError('Exponent must be a non-negative integer')
    res: int | float = 1
    while exponent > 0:
        if exponent & 1:
            res *= base
        base *= base
        exponent >>= 1
    return res

def binary_exp_mod_recursive(base: float, exponent: int, modulus: int) -> float:
    """Computes a^b % c recursively, where a is the base, b is the exponent, and c is the
    modulus"""
    if exponent < 0:
        raise ValueError('Exponent must be a non-negative integer')
    if modulus <= 0:
        raise ValueError('Modulus must be a positive integer')
    if exponent == 0:
        return 1
    if exponent % 2 == 1:
        return binary_exp_mod_recursive(base, exponent - 1, modulus) * base % modulus
    r = binary_exp_mod_recursive(base, exponent // 2, modulus)
    return r * r % modulus

def binary_exp_mod_iterative(base: float, exponent: int, modulus: int) -> float:
    """Computes a^b % c iteratively, where a is the base, b is the exponent, and c is the
    modulus"""
    if exponent < 0:
        raise ValueError('Exponent must be a non-negative integer')
    if modulus <= 0:
        raise ValueError('Modulus must be a positive integer')
    res: int | float = 1
    while exponent > 0:
        if exponent & 1:
            res = res % modulus * (base % modulus) % modulus
        base *= base
        exponent >>= 1
    return res