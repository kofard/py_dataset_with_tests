from timeit import timeit
test_data = {'MALAYALAM': True, 'String': False, 'rotor': True, 'level': True, 'A': True, 'BB': True, 'ABC': False, 'amanaplanacanalpanama': True, 'abcdba': False, 'AB': False}
assert all(((key == key[::-1]) == value for key, value in test_data.items()))

def is_palindrome(s: str) -> bool:
    """Return True if s is a palindrome otherwise return False."""
    start_i = 0
    end_i = len(s) - 1
    while start_i < end_i:
        if s[start_i] == s[end_i]:
            start_i += 1
            end_i -= 1
        else:
            return False
    return True

def is_palindrome_traversal(s: str) -> bool:
    """Return True if s is a palindrome otherwise return False."""
    end = len(s) // 2
    n = len(s)
    return all((s[i] == s[n - i - 1] for i in range(end)))

def is_palindrome_recursive(s: str) -> bool:
    """Return True if s is a palindrome otherwise return False."""
    if len(s) <= 1:
        return True
    if s[0] == s[len(s) - 1]:
        return is_palindrome_recursive(s[1:-1])
    else:
        return False

def is_palindrome_slice(s: str) -> bool:
    """Return True if s is a palindrome otherwise return False."""
    return s == s[::-1]

def is_palindrome_ignore_case_and_spaces(s: str) -> bool:
    """Return True if s is a palindrome, ignoring case, spaces, and punctuation.
    Otherwise return False."""
    s = ''.join((char.lower() for char in s if char.isalnum()))
    return s == s[::-1]
test_data_ignore_case_and_spaces = {'A man a plan a canal Panama': True, 'Was it a car or a cat I saw?': True, 'Hello World': False, 'Never Odd or Even': True, '': True}

def benchmark_function(name: str) -> None:
    stmt = f'all({name}(key) == value for key, value in test_data.items())'
    setup = f'from __main__ import test_data, {name}'
    number = 500000
    result = timeit(stmt=stmt, setup=setup, number=number)
    print(f'{name:<35} finished {number:,} runs in {result:.5f} seconds')