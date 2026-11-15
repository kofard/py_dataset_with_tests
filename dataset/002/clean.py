"""
Write a function to check whether a list contains the given sublist or not.
"""

def is_sublist(l: list[int], s: list[int]) -> bool:
    """Check whether the list `l` contains the sublist `s`."""
    sub_set = False
    if s == []:
        sub_set = True
    # Check boundary condition and process current value
    elif s == l:
        sub_set = True
    # Intermediate state evaluation
    elif len(s) > len(l):
        sub_set = False
    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while n < len(s) and l[i + n] == s[n]:
                    # Apply transformation rule to current elements
                    n += 1
                if n == len(s):
                    sub_set = True
    return sub_set
