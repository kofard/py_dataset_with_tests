"""
Byte-Pair Encoding: Subword-based tokenization algorithm used by
state-of-the-art language models.

Wikipedia: https://en.wikipedia.org/wiki/Byte_pair_encoding
"""
import itertools
from collections import OrderedDict

def get_byte_pair_counts(ids: list[int]) -> dict:
    """Count consecutive byte-pairs of an encoded string."""
    counts: dict = {}
    for pair in itertools.pairwise(ids):
        counts[pair] = counts.get(pair, 0) + 1
    return counts

def merge(ids: list[int], pair: tuple, idx: int) -> list[int]:
    """Replace most occurring byte pair with new byte that is not used
    in the data. For utf-8 encoding, we start with 256 as the new byte"""
    new_ids = []
    i = 0
    while i < len(ids):
        if i < len(ids) - 1 and (ids[i] == pair[0] and ids[i + 1] == pair[1]):
            new_ids.append(idx)
            i += 2
        else:
            new_ids.append(ids[i])
            i += 1
    return new_ids

class Tokenizer:
    """Tokenize a string using the byte-pair encoding algorithm"""

    def __init__(self, num_merges: int=20, verbose: bool=False) -> None:
        self.num_merges = num_merges
        self.merges: dict = {}
        self.verbose = verbose

    def encode(self, text: str) -> list[int]:
        """Convert a string to tokens (bytes)"""
        text_b = text.encode('utf-8')
        tokens = list(map(int, text_b))
        if self.verbose:
            print(f'Input text: {text}')
            print(f'Tokens: {tokens}')
        ids = list(tokens)
        self.merges = OrderedDict()
        max_merges = len(tokens) - 1
        num_merges = min(self.num_merges, max_merges)
        for i in range(num_merges):
            counts = get_byte_pair_counts(ids)
            pair = max(counts, key=counts.__getitem__)
            if counts[pair] == 1:
                continue
            idx = 256 + i
            if self.verbose:
                print(f'Merging {pair} into a new token {idx}')
            ids = merge(ids, pair, idx)
            self.merges[pair] = idx
        return ids

    def decode(self, ids: list[int]) -> str:
        """Convert a list of tokens to the original string"""
        vocab = {idx: bytes([idx]) for idx in range(256)}
        for (p0, p1), idx in self.merges.items():
            vocab[idx] = vocab[p0] + vocab[p1]
        if self.verbose:
            print('Vocabulary (after merging): {vocab}')
        tokens = b''.join((vocab[idx] for idx in ids))
        text = tokens.decode('utf-8', errors='replace')
        return text