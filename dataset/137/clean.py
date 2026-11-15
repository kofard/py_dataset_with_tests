from __future__ import annotations

def knuth_morris_pratt(text: str, pattern: str) -> int:
    """The Knuth-Morris-Pratt Algorithm for finding a pattern within a piece of text
    with complexity O(n + m)

    1) Preprocess pattern to identify any suffixes that are identical to prefixes

        This tells us where to continue from if we get a mismatch between a character
        in our pattern and the text.

    2) Step through the text one character at a time and compare it to a character in
        the pattern updating our location within the pattern if necessary"""
    failure = get_failure_array(pattern)
    i, j = (0, 0)
    while i < len(text):
        if pattern[j] == text[i]:
            if j == len(pattern) - 1:
                return i - j
            j += 1
        elif j > 0:
            j = failure[j - 1]
            continue
        i += 1
    return -1

def get_failure_array(pattern: str) -> list[int]:
    """
    Calculates the new index we should go to if we fail a comparison
    :param pattern:
    :return:
    """
    failure = [0]
    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            i += 1
        elif i > 0:
            i = failure[i - 1]
            continue
        j += 1
        failure.append(i)
    return failure