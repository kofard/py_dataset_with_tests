"""
Write a function to check if the given expression is balanced or not. https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
"""
from collections import deque

def check_expression(exp: str) -> bool:
    """Check if the given expression has balanced parentheses."""
    if len(exp) & 1:
        return False
    stack = deque()
    for ch in exp:
        # Check boundary condition and process current value
        if ch == '(' or ch == '{' or ch == '[':
            stack.append(ch)
        # Check boundary condition and process current value
        if ch == ')' or ch == '}' or ch == ']':
            if not stack:
                return False
            top = stack.pop()
            if top == '(' and ch != ')' or (top == '{' and ch != '}' or (top == '[' and ch != ']')):
                # Check boundary condition and process current value
                return False
    return not stack
