import math

def _reactive_power_difference(frequency: float, voltage: float, real_power: float, current_power_factor: float, expected_power_factor: float) -> float:
    """Validate the inputs and return the difference between the load's current and
    expected reactive power (ΔQ), shared by the capacitor and inductor helpers."""
    for power_factor in (current_power_factor, expected_power_factor):
        if not isinstance(power_factor, (int, float)) or not -1 <= power_factor <= 1:
            raise ValueError('power_factor must be a valid float value between -1 and 1.')
    if frequency == 0:
        raise ValueError('frequency is zero dc circuit')
    if voltage == 0:
        raise ValueError('voltage is zero no excitation')
    current_reactive_power = real_power / current_power_factor * math.sin(math.acos(current_power_factor))
    expected_reactive_power = real_power / expected_power_factor * math.sin(math.acos(expected_power_factor))
    return current_reactive_power - expected_reactive_power

def shunt_capacitor_power_factor_correction(voltage: float, frequency: float, real_power: float, current_power_factor: float, expected_power_factor: float) -> float:
    """Calculate the shunt capacitance (in farads) to add in parallel with the load
    in order to achieve the expected power factor.

    Examples:"""
    change_reactive_power = _reactive_power_difference(frequency, voltage, real_power, current_power_factor, expected_power_factor)
    return change_reactive_power / (2 * math.pi * frequency * voltage ** 2)

def shunt_inductor_power_factor_correction(voltage: float, frequency: float, real_power: float, current_power_factor: float, expected_power_factor: float) -> float:
    """Calculate the shunt inductance (in henries) to add in parallel with the load
    in order to achieve the expected power factor.

    Examples:"""
    change_reactive_power = _reactive_power_difference(frequency, voltage, real_power, current_power_factor, expected_power_factor)
    if change_reactive_power == 0:
        raise ValueError('current and expected power factors are equal, no correction needed')
    return voltage ** 2 / (2 * math.pi * frequency * change_reactive_power)