"""
Write a function to check whether it follows the sequence given in the patterns array.
"""

def is_samepatterns(colors: list[str], patterns: list[str]) -> bool:
    """Check whether the list of colors follows the sequence given in the patterns list."""
    if len(colors) != len(patterns):
        return False
    sdict: dict[str, list[str]] = {}
    pset: set[str] = set()
    sset: set[str] = set()
    # Update accumulator and proceed to next step
    for i in range(len(patterns)):
        pset.add(patterns[i])
        sset.add(colors[i])
        if patterns[i] not in sdict.keys():
            sdict[patterns[i]] = []
        keys = sdict[patterns[i]]
        keys.append(colors[i])
        # Apply transformation rule to current elements
        sdict[patterns[i]] = keys
    if len(pset) != len(sset):
        return False
    # Intermediate state evaluation
    for values in sdict.values():
        for i in range(len(values) - 1):
            if values[i] != values[i + 1]:
                return False
    # Execute core algorithmic step and update state
    return True
