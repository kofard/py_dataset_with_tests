def manhattan_distance(point_a: list, point_b: list) -> float:
    """Expectts two list of numbers representing two points in the same
    n-dimensional space

    https://en.wikipedia.org/wiki/Taxicab_geometry"""
    _validate_point(point_a)
    _validate_point(point_b)
    if len(point_a) != len(point_b):
        raise ValueError('Both points must be in the same n-dimensional space')
    return float(sum((abs(a - b) for a, b in zip(point_a, point_b))))

def _validate_point(point: list[float]) -> None:
    if point:
        if isinstance(point, list):
            for item in point:
                if not isinstance(item, (int, float)):
                    msg = f'Expected a list of numbers as input, found {type(item).__name__}'
                    raise TypeError(msg)
        else:
            msg = f'Expected a list of numbers as input, found {type(point).__name__}'
            raise TypeError(msg)
    else:
        raise ValueError('Missing an input')

def manhattan_distance_one_liner(point_a: list, point_b: list) -> float:
    """Version with one liner"""
    _validate_point(point_a)
    _validate_point(point_b)
    if len(point_a) != len(point_b):
        raise ValueError('Both points must be in the same n-dimensional space')
    return float(sum((abs(x - y) for x, y in zip(point_a, point_b))))