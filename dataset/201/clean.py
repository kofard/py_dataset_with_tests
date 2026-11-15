def orbital_transfer_work(mass_central: float, mass_object: float, r_initial: float, r_final: float) -> str:
    """Calculates the work required to move an object from one orbit to another in a
    gravitational field based on the change in total mechanical energy.

    The formula used is:
        W = (G * M * m / 2) * (1/r_initial - 1/r_final)

    where:
        W = work done (Joules)
        G = gravitational constant (6.67430 * 10^-11 m^3 kg^-1 s^-2)
        M = mass of the central body (kg)
        m = mass of the orbiting object (kg)
        r_initial = initial orbit radius (m)
        r_final = final orbit radius (m)

    Args:
        mass_central (float): Mass of the central body (kg)
        mass_object (float): Mass of the object being moved (kg)
        r_initial (float): Initial orbital radius (m)
        r_final (float): Final orbital radius (m)

    Returns:
        str: Work done in Joules as a string in scientific notation (3 decimals)

    Examples:"""
    gravitational_constant = 6.6743e-11
    if r_initial <= 0 or r_final <= 0:
        raise ValueError('Orbital radii must be greater than zero.')
    work = gravitational_constant * mass_central * mass_object / 2 * (1 / r_initial - 1 / r_final)
    return f'{work:.3e}'