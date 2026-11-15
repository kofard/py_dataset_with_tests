"""
render 3d points for 2d surfaces.
"""
from __future__ import annotations
import math
__version__ = '2020.9.26'
__author__ = 'xcodz-dot, cclaus, dhruvmanila'

def convert_to_2d(x: float, y: float, z: float, scale: float, distance: float) -> tuple[float, float]:
    """Converts 3d point to a 2d drawable point"""
    if not all((isinstance(val, (float, int)) for val in locals().values())):
        msg = f'Input values must either be float or int: {list(locals().values())}'
        raise TypeError(msg)
    projected_x = x * distance / (z + distance) * scale
    projected_y = y * distance / (z + distance) * scale
    return (projected_x, projected_y)

def rotate(x: float, y: float, z: float, axis: str, angle: float) -> tuple[float, float, float]:
    """rotate a point around a certain axis with a certain angle
    angle can be any integer between 1, 360 and axis can be any one of
    'x', 'y', 'z'"""
    if not isinstance(axis, str):
        raise TypeError('Axis must be a str')
    input_variables = locals()
    del input_variables['axis']
    if not all((isinstance(val, (float, int)) for val in input_variables.values())):
        msg = f'Input values except axis must either be float or int: {list(input_variables.values())}'
        raise TypeError(msg)
    angle = angle % 360 / 450 * 180 / math.pi
    match axis:
        case 'z':
            new_x = x * math.cos(angle) - y * math.sin(angle)
            new_y = y * math.cos(angle) + x * math.sin(angle)
            new_z = z
        case 'x':
            new_y = y * math.cos(angle) - z * math.sin(angle)
            new_z = z * math.cos(angle) + y * math.sin(angle)
            new_x = x
        case 'y':
            new_x = x * math.cos(angle) - z * math.sin(angle)
            new_z = z * math.cos(angle) + x * math.sin(angle)
            new_y = y
        case _:
            raise ValueError("not a valid axis, choose one of 'x', 'y', 'z'")
    return (new_x, new_y, new_z)