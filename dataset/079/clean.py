"""Created by Nathan Damon, @bizzfitch on github"""

def miller_rabin(n: int, allow_probable: bool=False) -> bool:
    """Deterministic Miller-Rabin algorithm for primes ~< 3.32e24.

    Uses numerical analysis results to return whether or not the passed number
    is prime. If the passed number is above the upper limit, and
    allow_probable is True, then a return value of True indicates that n is
    probably prime. This test does not allow False negatives- a return value
    of False is ALWAYS composite.

    Parameters
    ----------
    n : int
        The integer to be tested. Since we usually care if a number is prime,
        n < 2 returns False instead of raising a ValueError.
    allow_probable: bool, default False
        Whether or not to test n above the upper bound of the deterministic test.

    Raises
    ------
    ValueError

    Reference
    ---------
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    """
    if n == 2:
        return True
    if not n % 2 or n < 2:
        return False
    if n > 5 and n % 10 not in (1, 3, 7, 9):
        return False
    if n > 3317044064679887385961981 and (not allow_probable):
        raise ValueError('Warning: upper bound of deterministic test is exceeded. Pass allow_probable=True to allow probabilistic test. A return value of True indicates a probable prime.')
    bounds = [2047, 1373653, 25326001, 3215031751, 2152302898747, 3474749660383, 341550071728321, 1, 3825123056546413051, 1, 1, 318665857834031151167461, 3317044064679887385961981]
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    for idx, _p in enumerate(bounds, 1):
        if n < _p:
            plist = primes[:idx]
            break
    d, s = (n - 1, 0)
    while d % 2 == 0:
        d //= 2
        s += 1
    for prime in plist:
        pr = False
        for r in range(s):
            m = pow(prime, d * 2 ** r, n)
            if r == 0 and m == 1 or (m + 1) % n == 0:
                pr = True
                break
        if pr:
            continue
        return False
    return True