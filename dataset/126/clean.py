"""https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance"""
from collections import defaultdict, deque

def jaro_winkler(str1: str, str2: str) -> float:
    """Jaro-Winkler distance is a string metric measuring an edit distance between two
    sequences.
    Output value is between 0.0 and 1.0."""

    def get_matched_characters(_str1: str, _str2: str) -> str:
        matched = []
        character_positions: defaultdict[str, deque[int]] = defaultdict(deque)
        for index, char in enumerate(_str2):
            character_positions[char].append(index)
        limit = min(len(_str1), len(_str2)) // 2
        for i, char in enumerate(_str1):
            positions = character_positions.get(char)
            if not positions:
                continue
            left = int(max(0, i - limit))
            right = int(min(i + limit + 1, len(_str2)))
            while positions and positions[0] < left:
                positions.popleft()
            if positions and positions[0] < right:
                matched.append(char)
                positions.popleft()
        return ''.join(matched)
    matching_1 = get_matched_characters(str1, str2)
    matching_2 = get_matched_characters(str2, str1)
    match_count = len(matching_1)
    transpositions = len([(c1, c2) for c1, c2 in zip(matching_1, matching_2) if c1 != c2]) // 2
    if not match_count:
        jaro = 0.0
    else:
        jaro = 1 / 3 * (match_count / len(str1) + match_count / len(str2) + (match_count - transpositions) / match_count)
    prefix_len = 0
    for c1, c2 in zip(str1[:4], str2[:4]):
        if c1 == c2:
            prefix_len += 1
        else:
            break
    return jaro + 0.1 * prefix_len * (1 - jaro)