"""Convert a Decimal Number to a Binary Number."""

def decimal_to_binary_iterative(num: int) -> str:
    """Convert an Integer Decimal Number to a Binary Number as str."""
    if isinstance(num, float):
        raise TypeError("'float' object cannot be interpreted as an integer")
    if isinstance(num, str):
        raise TypeError("'str' object cannot be interpreted as an integer")
    if num == 0:
        return '0b0'
    negative = False
    if num < 0:
        negative = True
        num = -num
    binary: list[int] = []
    while num > 0:
        binary.insert(0, num % 2)
        num >>= 1
    if negative:
        return '-0b' + ''.join((str(e) for e in binary))
    return '0b' + ''.join((str(e) for e in binary))

def decimal_to_binary_recursive_helper(decimal: int) -> str:
    """Take a positive integer value and return its binary equivalent."""
    decimal = int(decimal)
    if decimal in (0, 1):
        return str(decimal)
    div, mod = divmod(decimal, 2)
    return decimal_to_binary_recursive_helper(div) + str(mod)

def decimal_to_binary_recursive(number: str) -> str:
    """Take an integer value and raise ValueError for wrong inputs,
    call the function above and return the output with prefix "0b" & "-0b"
    for positive and negative integers respectively."""
    number = str(number).strip()
    if not number:
        raise ValueError('No input value was provided')
    negative = '-' if number.startswith('-') else ''
    number = number.lstrip('-')
    if not number.isnumeric():
        raise ValueError('Input value is not an integer')
    return f'{negative}0b{decimal_to_binary_recursive_helper(int(number))}'