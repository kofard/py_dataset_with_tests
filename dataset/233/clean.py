def get_reverse_bit_string(number: int) -> str:
    """Return the reverse bit string of a 32 bit integer"""
    if not isinstance(number, int):
        msg = f'operation can not be conducted on an object of type {type(number).__name__}'
        raise TypeError(msg)
    bit_string = ''
    for _ in range(32):
        bit_string += str(number % 2)
        number >>= 1
    return bit_string

def reverse_bit(number: int) -> int:
    """Take in a 32 bit integer, reverse its bits, return a 32 bit integer result"""
    if not isinstance(number, int):
        raise TypeError("Input value must be an 'int' type")
    if number < 0:
        raise ValueError('The value of input must be non-negative')
    result = 0
    for _ in range(32):
        result <<= 1
        end_bit = number & 1
        number >>= 1
        result |= end_bit
    return result