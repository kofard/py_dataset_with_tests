"""
Hey, we are going to find an exciting number called Catalan number which is use to find
the number of possible binary search trees from tree of a given number of nodes.

We will use the formula: t(n) = SUMMATION(i = 1 to n)t(i-1)t(n-i)

Further details at Wikipedia: https://en.wikipedia.org/wiki/Catalan_number
"""
'\nOur Contribution:\nBasically we Create the 2 function:\n    1. catalan_number(node_count: int) -> int\n        Returns the number of possible binary search trees for n nodes.\n    2. binary_tree_count(node_count: int) -> int\n        Returns the number of possible binary trees for n nodes.\n'

def binomial_coefficient(n: int, k: int) -> int:
    """Since Here we Find the Binomial Coefficient:
    https://en.wikipedia.org/wiki/Binomial_coefficient
    C(n,k) = n! / k!(n-k)!
    :param n: 2 times of Number of nodes
    :param k: Number of nodes
    :return:  Integer Value"""
    result = 1
    k = min(k, n - k)
    for i in range(k):
        result *= n - i
        result //= i + 1
    return result

def catalan_number(node_count: int) -> int:
    """We can find Catalan number many ways but here we use Binomial Coefficient because it
    does the job in O(n)

    return the Catalan number of n using 2nCn/(n+1).
    :param n: number of nodes
    :return: Catalan number of n nodes"""
    return binomial_coefficient(2 * node_count, node_count) // (node_count + 1)

def factorial(n: int) -> int:
    """Return the factorial of a number.
    :param n: Number to find the Factorial of.
    :return: Factorial of n."""
    if n < 0:
        raise ValueError('factorial() not defined for negative values')
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def binary_tree_count(node_count: int) -> int:
    """Return the number of possible of binary trees.
    :param n: number of nodes
    :return: Number of possible binary trees"""
    return catalan_number(node_count) * factorial(node_count)