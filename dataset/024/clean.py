"""
https://en.wikipedia.org/wiki/Check_digit#Algorithms
"""

def get_check_digit(barcode: int) -> int:
    """Returns the last digit of barcode by excluding the last digit first
    and then computing to reach the actual last digit from the remaining
    12 digits."""
    barcode //= 10
    checker = False
    s = 0
    while barcode != 0:
        mult = 1 if checker else 3
        s += mult * (barcode % 10)
        barcode //= 10
        checker = not checker
    return (10 - s % 10) % 10

def is_valid(barcode: int) -> bool:
    """Checks for length of barcode and last-digit
    Returns boolean value of validity of barcode"""
    return len(str(barcode)) == 13 and get_check_digit(barcode) == barcode % 10

def get_barcode(barcode: str) -> int:
    """Returns the barcode as an integer"""
    if str(barcode).isalpha():
        msg = f"Barcode '{barcode}' has alphabetic characters."
        raise ValueError(msg)
    if int(barcode) < 0:
        raise ValueError('The entered barcode has a negative value. Try again.')
    return int(barcode)