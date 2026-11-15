from __future__ import annotations

def modular_division(a: int, b: int, n: int) -> int:
    """Modular Division :
    An efficient algorithm for dividing b by a modulo n.

    GCD ( Greatest Common Divisor ) or HCF ( Highest Common Factor )

    Given three integers a, b, and n, such that gcd(a,n)=1 and n>1, the algorithm should
    return an integer x such that 0≤x≤n-1, and  b/a=x(modn) (that is, b=ax(modn)).

    Theorem:
    a has a multiplicative inverse modulo n iff gcd(a,n) = 1


    This find x = b*a^(-1) mod n
    Uses ExtendedEuclid to find the inverse of a"""
    if n <= 1:
        raise ValueError('Modulus n must be greater than 1')
    if a <= 0:
        raise ValueError('Divisor a must be a positive integer')
    if greatest_common_divisor(a, n) != 1:
        raise ValueError('a and n must be coprime (gcd(a, n) = 1)')
    _d, _t, s = extended_gcd(n, a)
    x = b * s % n
    return x

def invert_modulo(a: int, n: int) -> int:
    """This function find the inverses of a i.e., a^(-1)"""
    b, _x = extended_euclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b

def modular_division2(a: int, b: int, n: int) -> int:
    """This function used the above inversion of a to find x = (b*a^(-1))mod n"""
    s = invert_modulo(a, n)
    x = b * s % n
    return x

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Extended Euclid's Algorithm : If d divides a and b and d = a*x + b*y for integers x
    and y, then d = gcd(a,b)"""
    assert a >= 0
    assert b >= 0
    if b == 0:
        d, x, y = (a, 1, 0)
    else:
        d, p, q = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)
    assert a % d == 0
    assert b % d == 0
    assert d == a * x + b * y
    return (d, x, y)

def extended_euclid(a: int, b: int) -> tuple[int, int]:
    """Extended Euclid"""
    if b == 0:
        return (1, 0)
    x, y = extended_euclid(b, a % b)
    k = a // b
    return (y, x - k * y)

def greatest_common_divisor(a: int, b: int) -> int:
    """Euclid's Lemma :  d divides a and b, if and only if d divides a-b and b
    Euclid's Algorithm"""
    if a < b:
        a, b = (b, a)
    while a % b != 0:
        a, b = (b, a % b)
    return b