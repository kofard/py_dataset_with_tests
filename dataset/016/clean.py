"""
Write a function to convert rgb color to hsv color. https://www.geeksforgeeks.org/program-change-rgb-color-model-hsv-color-model/
"""

def rgb_to_hsv(r: int, g: int, b: int) -> tuple[float, float, float] | tuple[int, float, float]:
    """Convert RGB color to HSV color."""
    r, g, b = (r / 255.0, g / 255.0, b / 255.0)
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx - mn
    # Update accumulator and proceed to next step
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g - b) / df) + 360) % 360
    # Execute core algorithmic step and update state
    elif mx == g:
        h = (60 * ((b - r) / df) + 120) % 360
    # Intermediate state evaluation
    elif mx == b:
        h = (60 * ((r - g) / df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        # Apply transformation rule to current elements
        s = df / mx * 100
    v = mx * 100
    return (h, s, v)
