"""
Program to evaluate a prefix expression.
https://en.wikipedia.org/wiki/Polish_notation
"""
operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}

def is_operand(c) -> bool:
    """Return True if the given char c is an operand, e.g. it is a number"""
    return c.isdigit()

def evaluate(expression) -> float:
    """Evaluate a given expression in prefix notation.
    Asserts that the given expression is valid."""
    stack = []
    for c in expression.split()[::-1]:
        if is_operand(c):
            stack.append(int(c))
        else:
            o1 = stack.pop()
            o2 = stack.pop()
            stack.append(operators[c](o1, o2))
    return stack.pop()

def evaluate_recursive(expression: list[str]) -> float:
    """Alternative recursive implementation"""
    op = expression.pop(0)
    if is_operand(op):
        return int(op)
    operation = operators[op]
    a = evaluate_recursive(expression)
    b = evaluate_recursive(expression)
    return operation(a, b)