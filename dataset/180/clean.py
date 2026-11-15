"""
Move-to-front transform.

The move-to-front transform encodes each symbol as its current index in an
ordered alphabet, then moves that symbol to the front of the alphabet.
It is commonly used after the Burrows-Wheeler transform in lossless
compression pipelines.

Reference: https://en.wikipedia.org/wiki/Move-to-front_transform
"""

def _validated_alphabet(alphabet: str) -> list[str]:
    """Return a mutable alphabet list after validating uniqueness."""
    if not isinstance(alphabet, str):
        raise TypeError('alphabet must be a string')
    if len(set(alphabet)) != len(alphabet):
        raise ValueError('alphabet must contain unique characters')
    return list(alphabet)

def move_to_front_encode(text: str, alphabet: str) -> list[int]:
    """Encode text using the move-to-front transform."""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    symbols = _validated_alphabet(alphabet)
    encoded_text: list[int] = []
    for char in text:
        try:
            char_index = symbols.index(char)
        except ValueError:
            message = f'character {char!r} is not in the alphabet'
            raise ValueError(message) from None
        encoded_text.append(char_index)
        symbols.insert(0, symbols.pop(char_index))
    return encoded_text

def move_to_front_decode(encoded_text: list[int], alphabet: str) -> str:
    """Decode a move-to-front encoded list of indexes."""
    symbols = _validated_alphabet(alphabet)
    decoded_text = []
    for index in encoded_text:
        if not 0 <= index < len(symbols):
            message = f'index {index} is not valid for alphabet size {len(symbols)}'
            raise ValueError(message)
        decoded_text.append(symbols[index])
        symbols.insert(0, symbols.pop(index))
    return ''.join(decoded_text)