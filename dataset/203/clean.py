import secrets
from random import shuffle
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, punctuation

def password_generator(length: int=8) -> str:
    """Password Generator allows you to generate a random password of length N."""
    chars = ascii_letters + digits + punctuation
    return ''.join((secrets.choice(chars) for _ in range(length)))

def alternative_password_generator(chars_incl: str, i: int) -> str:
    i -= len(chars_incl)
    quotient = i // 3
    remainder = i % 3
    chars = chars_incl + random(ascii_letters, quotient + remainder) + random(digits, quotient) + random(punctuation, quotient)
    list_of_chars = list(chars)
    shuffle(list_of_chars)
    return ''.join(list_of_chars)

def random(chars_incl: str, i: int) -> str:
    return ''.join((secrets.choice(chars_incl) for _ in range(i)))

def is_strong_password(password: str, min_length: int=8) -> bool:
    """This will check whether a given password is strong or not. The password must be at
    least as long as the provided minimum length, and it must contain at least 1
    lowercase letter, 1 uppercase letter, 1 number and 1 special character."""
    if len(password) < min_length:
        return False
    upper = any((char in ascii_uppercase for char in password))
    lower = any((char in ascii_lowercase for char in password))
    num = any((char in digits for char in password))
    spec_char = any((char in punctuation for char in password))
    return upper and lower and num and spec_char

def main() -> None:
    length = int(input('Please indicate the max length of your password: ').strip())
    chars_incl = input('Please indicate the characters that must be in your password: ').strip()
    print('Password generated:', password_generator(length))
    print('Alternative Password generated:', alternative_password_generator(chars_incl, length))
    print('[If you are thinking of using this password, You better save it.]')