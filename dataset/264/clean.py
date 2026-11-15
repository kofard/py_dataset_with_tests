def star_to_delta(impedance_a: complex, impedance_b: complex, impedance_c: complex) -> list[complex]:
    """Convert's star impedance arrangement to delta

    Examples:
    1.) Impedance with resistances and zero reactance"""
    if abs(impedance_a) == 0 or abs(impedance_b) == 0 or abs(impedance_c) == 0:
        raise ValueError('entered impedance value is zero')
    if impedance_a.real < 0 or impedance_b.real < 0 or impedance_c.real < 0:
        raise ValueError('entered resistance value is negative')
    delta_arrangement = []
    impedance_chain = impedance_a * impedance_b + impedance_b * impedance_c + impedance_c * impedance_a
    delta_arrangement.append(impedance_chain / impedance_a)
    delta_arrangement.append(impedance_chain / impedance_b)
    delta_arrangement.append(impedance_chain / impedance_c)
    return delta_arrangement

def delta_to_star(impedance_a: complex, impedance_b: complex, impedance_c: complex) -> list[complex]:
    """Convert's delta impedance arrangement to star

    Examples:
    1.) Impedance with resistances and zero reactance"""
    if abs(impedance_a) == 0 or abs(impedance_b) == 0 or abs(impedance_c) == 0:
        raise ValueError('entered impedance value is zero')
    if impedance_a.real < 0 or impedance_b.real < 0 or impedance_c.real < 0:
        raise ValueError('entered resistance value is negative')
    star_arrangement = []
    impedance_sum = impedance_a + impedance_b + impedance_c
    star_arrangement.append(impedance_b * impedance_c / impedance_sum)
    star_arrangement.append(impedance_c * impedance_a / impedance_sum)
    star_arrangement.append(impedance_a * impedance_b / impedance_sum)
    return star_arrangement