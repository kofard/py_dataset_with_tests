"""
Sieve of Atkin algorithm for finding all prime numbers up to a given limit.

The Sieve of Atkin is a modern variant of the ancient Sieve of Eratosthenes
that is optimized for finding primes. It has better theoretical asymptotic
complexity, especially for large ranges.  This is the basic, non-segmented
form.

Time Complexity: O(n / log log n)
Space Complexity: O(n)

Reference: https://en.wikipedia.org/wiki/Sieve_of_Atkin
"""
import math

def sieve_of_atkin(limit: int) -> list[int]:
    """Generate all prime numbers up to a given limit using the Sieve of Atkin.

    The Sieve of Atkin is an optimized version of the Sieve of Eratosthenes.
    It uses a different set of quadratic forms to identify potential primes.

    Args:
        limit: Upper bound for finding primes (inclusive)

    Returns:
        List of prime numbers up to the given limit

    Raises:
        ValueError: If limit is negative

    Examples:"""
    if limit < 0:
        msg = f'{limit}: Invalid input, please enter a non-negative integer.'
        raise ValueError(msg)
    if limit < 2:
        return []
    sieve = [False] * (limit + 1)
    if limit >= 2:
        sieve[2] = True
    if limit >= 3:
        sieve[3] = True
    sqrt_limit = int(math.sqrt(limit)) + 1
    for x in range(1, sqrt_limit):
        for y in range(1, sqrt_limit):
            n = 4 * x * x + y * y
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * x * x + y * y
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            if x > y:
                n = 3 * x * x - y * y
                if n <= limit and n % 12 == 11:
                    sieve[n] = not sieve[n]
    for r in range(5, sqrt_limit):
        if sieve[r]:
            square = r * r
            for i in range(square, limit + 1, square):
                sieve[i] = False
    primes = []
    for i in range(2, limit + 1):
        if sieve[i]:
            primes.append(i)
    return primes