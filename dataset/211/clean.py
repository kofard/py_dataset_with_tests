"""
Reverse Polish Nation is also known as Polish postfix notation or simply postfix
notation.
https://en.wikipedia.org/wiki/Reverse_Polish_notation
Classic examples of simple stack implementations.
Valid operators are +, -, *, /.
Each operand may be an integer or another expression.

Output:

Enter a Postfix Equation (space separated) = 5 6 9 * +
 Symbol  |    Action    | Stack
-----------------------------------
       5 | push(5)      | 5
       6 | push(6)      | 5,6
       9 | push(9)      | 5,6,9
         | pop(9)       | 5,6
         | pop(6)       | 5
       * | push(6*9)    | 5,54
         | pop(54)      | 5
         | pop(5)       |
       + | push(5+54)   | 59

        Result =  59
"""
UNARY_OP_SYMBOLS = ('-', '+')
OPERATORS = {'^': lambda p, q: p ** q, '*': lambda p, q: p * q, '/': lambda p, q: p / q, '+': lambda p, q: p + q, '-': lambda p, q: p - q}

def parse_token(token: str | float) -> float | str:
    """
    Converts the given data to the appropriate number if it is indeed a number, else
    returns the data as it is with a False flag. This function also serves as a check
    of whether the input is a number or not.

    Parameters
    ----------
    token: The data that needs to be converted to the appropriate operator or number.

    Returns
    -------
    float or str
        Returns a float if `token` is a number or a str if `token` is an operator
    """
    if token in OPERATORS:
        return token
    try:
        return float(token)
    except ValueError:
        msg = f'{token} is neither a number nor a valid operator'
        raise ValueError(msg)

def evaluate(post_fix: list[str], verbose: bool=False) -> float:
    """Evaluate postfix expression using a stack."""
    if not post_fix:
        return 0
    valid_expression = [parse_token(token) for token in post_fix]
    if verbose:
        print('Symbol'.center(8), 'Action'.center(12), 'Stack', sep=' | ')
        print('-' * (30 + len(post_fix)))
    stack = []
    for x in valid_expression:
        if x not in OPERATORS:
            stack.append(x)
            if verbose:
                print(f'{x}'.rjust(8), f'push({x})'.ljust(12), stack, sep=' | ')
            continue
        if x in UNARY_OP_SYMBOLS and len(stack) < 2:
            b = stack.pop()
            if x == '-':
                b *= -1
            stack.append(b)
            if verbose:
                print(''.rjust(8), f'pop({b})'.ljust(12), stack, sep=' | ')
                print(str(x).rjust(8), f'push({x}{b})'.ljust(12), stack, sep=' | ')
            continue
        b = stack.pop()
        if verbose:
            print(''.rjust(8), f'pop({b})'.ljust(12), stack, sep=' | ')
        a = stack.pop()
        if verbose:
            print(''.rjust(8), f'pop({a})'.ljust(12), stack, sep=' | ')
        stack.append(OPERATORS[x](a, b))
        if verbose:
            print(f'{x}'.rjust(8), f'push({a}{x}{b})'.ljust(12), stack, sep=' | ')
    if len(stack) != 1:
        raise ArithmeticError('Input is not a valid postfix expression')
    return float(stack[0])