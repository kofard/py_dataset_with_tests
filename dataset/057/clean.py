from collections import Counter
from timeit import timeit

def can_string_be_rearranged_as_palindrome_counter(input_str: str='') -> bool:
    """A Palindrome is a String that reads the same forward as it does backwards.
    Examples of Palindromes mom, dad, malayalam"""
    return sum((c % 2 for c in Counter(input_str.replace(' ', '').lower()).values())) < 2

def can_string_be_rearranged_as_palindrome(input_str: str='') -> bool:
    """A Palindrome is a String that reads the same forward as it does backwards.
    Examples of Palindromes mom, dad, malayalam"""
    if len(input_str) == 0:
        return True
    lower_case_input_str = input_str.replace(' ', '').lower()
    character_freq_dict: dict[str, int] = {}
    for character in lower_case_input_str:
        character_freq_dict[character] = character_freq_dict.get(character, 0) + 1
    '\n    Above line of code is equivalent to:\n    1) Getting the frequency of current character till previous index\n    >>> character_freq =  character_freq_dict.get(character, 0)\n    2) Incrementing the frequency of current character by 1\n    >>> character_freq = character_freq + 1\n    3) Updating the frequency of current character\n    >>> character_freq_dict[character] = character_freq\n    '
    "\n    OBSERVATIONS:\n    Even length palindrome\n    -> Every character appears even no.of times.\n    Odd length palindrome\n    -> Every character appears even no.of times except for one character.\n    LOGIC:\n    Step 1: We'll count number of characters that appear odd number of times i.e oddChar\n    Step 2:If we find more than 1 character that appears odd number of times,\n    It is not possible to rearrange as a palindrome\n    "
    odd_char = 0
    for character_count in character_freq_dict.values():
        if character_count % 2:
            odd_char += 1
    return not odd_char > 1

def benchmark(input_str: str='') -> None:
    """
    Benchmark code for comparing above 2 functions
    """
    print('\nFor string = ', input_str, ':')
    print('> can_string_be_rearranged_as_palindrome_counter()', '\tans =', can_string_be_rearranged_as_palindrome_counter(input_str), '\ttime =', timeit('z.can_string_be_rearranged_as_palindrome_counter(z.check_str)', setup='import __main__ as z'), 'seconds')
    print('> can_string_be_rearranged_as_palindrome()', '\tans =', can_string_be_rearranged_as_palindrome(input_str), '\ttime =', timeit('z.can_string_be_rearranged_as_palindrome(z.check_str)', setup='import __main__ as z'), 'seconds')