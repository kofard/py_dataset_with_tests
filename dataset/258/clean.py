"""
https://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm
The Smith-Waterman algorithm is a dynamic programming algorithm used for sequence
alignment. It is particularly useful for finding similarities between two sequences,
such as DNA or protein sequences. In this implementation, gaps are penalized
linearly, meaning that the score is reduced by a fixed amount for each gap introduced
in the alignment. However, it's important to note that the Smith-Waterman algorithm
supports other gap penalty methods as well.
"""

def score_function(source_char: str, target_char: str, match: int=1, mismatch: int=-1, gap: int=-2) -> int:
    """Calculate the score for a character pair based on whether they match or mismatch.
    Returns 1 if the characters match, -1 if they mismatch, and -2 if either of the
    characters is a gap."""
    if '-' in (source_char, target_char):
        return gap
    return match if source_char == target_char else mismatch

def smith_waterman(query: str, subject: str, match: int=1, mismatch: int=-1, gap: int=-2) -> list[list[int]]:
    """Perform the Smith-Waterman local sequence alignment algorithm.
    Returns a 2D list representing the score matrix. Each value in the matrix
    corresponds to the score of the best local alignment ending at that point."""
    query = query.upper()
    subject = subject.upper()
    m = len(query)
    n = len(subject)
    score = [[0] * (n + 1) for _ in range(m + 1)]
    kwargs = {'match': match, 'mismatch': mismatch, 'gap': gap}
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match = score[i - 1][j - 1] + score_function(query[i - 1], subject[j - 1], **kwargs)
            delete = score[i - 1][j] + gap
            insert = score[i][j - 1] + gap
            score[i][j] = max(0, match, delete, insert)
    return score

def traceback(score: list[list[int]], query: str, subject: str) -> str:
    """Perform traceback to find the optimal local alignment.
    Starts from the highest scoring cell in the matrix and traces back recursively
    until a 0 score is found. Returns the alignment strings."""
    query = query.upper()
    subject = subject.upper()
    max_value = float('-inf')
    i_max = j_max = 0
    for i, row in enumerate(score):
        for j, value in enumerate(row):
            if value > max_value:
                max_value = value
                i_max, j_max = (i, j)
    i = i_max
    j = j_max
    align1 = ''
    align2 = ''
    gap = score_function('-', '-')
    if i == 0 or j == 0:
        return ''
    while i > 0 and j > 0:
        if score[i][j] == score[i - 1][j - 1] + score_function(query[i - 1], subject[j - 1]):
            align1 = query[i - 1] + align1
            align2 = subject[j - 1] + align2
            i -= 1
            j -= 1
        elif score[i][j] == score[i - 1][j] + gap:
            align1 = query[i - 1] + align1
            align2 = f'-{align2}'
            i -= 1
        else:
            align1 = f'-{align1}'
            align2 = subject[j - 1] + align2
            j -= 1
    return f'{align1}\n{align2}'