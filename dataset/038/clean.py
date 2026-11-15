"""
Convert between Binary and Gray Code representations.

Gray Code (also known as reflected binary code) is a binary numeral system where
two successive values differ in only one bit. This property makes it useful in
error correction, digital communications, and position encoders.

Wikipedia: https://en.wikipedia.org/wiki/Gray_code
"""

def binary_to_gray(binary_number: int) -> int:
    """Convert a binary number to its Gray Code equivalent.

    The algorithm works by XORing the binary number with itself right-shifted by 1.
    Formula: gray = binary XOR (binary >> 1)

    Args:
        binary_number: A positive integer representing a binary number

    Returns:
        The Gray Code equivalent as an integer

    Examples:"""
    if not isinstance(binary_number, int):
        raise TypeError('Input must be an integer')
    if binary_number < 0:
        raise ValueError('Input must be a non-negative integer')
    return binary_number ^ binary_number >> 1

def gray_to_binary(gray_number: int) -> int:
    """Convert a Gray Code number to its binary equivalent.

    The algorithm works by repeatedly XORing the gray code with itself right-shifted,
    until the right-shifted value becomes 0.

    Args:
        gray_number: A positive integer representing a Gray Code number

    Returns:
        The binary equivalent as an integer

    Examples:"""
    if not isinstance(gray_number, int):
        raise TypeError('Input must be an integer')
    if gray_number < 0:
        raise ValueError('Input must be a non-negative integer')
    binary_number = gray_number
    gray_number >>= 1
    while gray_number:
        binary_number ^= gray_number
        gray_number >>= 1
    return binary_number

def decimal_to_gray(decimal_number: int) -> str:
    """Convert a decimal number to its Gray Code representation as a binary string.

    Args:
        decimal_number: A positive integer in decimal

    Returns:
        Gray Code representation as a binary string

    Examples:"""
    if not isinstance(decimal_number, int):
        raise TypeError('Input must be an integer')
    if decimal_number < 0:
        raise ValueError('Input must be a non-negative integer')
    gray_code = binary_to_gray(decimal_number)
    return bin(gray_code)[2:]

def gray_to_decimal(gray_string: str) -> int:
    """Convert a Gray Code binary string to its decimal equivalent.

    Args:
        gray_string: A string of 0s and 1s representing Gray Code

    Returns:
        The decimal equivalent as an integer

    Examples:"""
    if not gray_string:
        raise ValueError('Input string cannot be empty')
    if not all((bit in '01' for bit in gray_string)):
        raise ValueError('Invalid binary string')
    gray_number = int(gray_string, 2)
    return gray_to_binary(gray_number)