def decimal_to_fraction(decimal: float | str) -> tuple[int, int]:
    """Return a decimal number in its simplest fraction form"""
    try:
        decimal = float(decimal)
    except ValueError:
        raise ValueError('Please enter a valid number')
    fractional_part = decimal - int(decimal)
    if fractional_part == 0:
        return (int(decimal), 1)
    else:
        number_of_frac_digits = len(str(decimal).split('.')[1])
        numerator = int(decimal * 10 ** number_of_frac_digits)
        denominator = 10 ** number_of_frac_digits
        divisor, dividend = (denominator, numerator)
        while True:
            remainder = dividend % divisor
            if remainder == 0:
                break
            dividend, divisor = (divisor, remainder)
        numerator, denominator = (numerator // divisor, denominator // divisor)
        return (numerator, denominator)