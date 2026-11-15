from typing import NamedTuple

class Result(NamedTuple):
    name: str
    value: float

def max_load_current(rf: float, rs: float, rl: float, vm: float) -> tuple:
    """This function can calculate the maximum load current(Im)
    in a full-wave rectifier circuit.
    Im = maximum load current
    rf = Forward Resistance of the diode
    rs = Transformer secondary winding resistance
    rl = load resistance
    vm = maximum voltage or peak voltage
    Cases:-"""
    if (rf, rs, rl).count(0) == 3:
        raise ValueError('At least one Resistance must be non-zero')
    if rf < 0 or rs < 0 or rl < 0:
        raise ValueError('Resistance cannot be negative')
    if vm == 0:
        return Result('max_load_current', vm / (rf + rs + rl))
    else:
        return Result('max_load_current', vm / (rf + rs + rl))

def dc_current(im: float) -> tuple:
    """This function can calculate the Average DC Current(Idc) in a circuit.
    In all cases, a negative sign shows
    the opposite direction of current or voltage.
    Idc = average direct current (DC)
    im = maximum current or peak current
    cases:"""
    return Result('Idc', 2 * im * 0.318)

def dc_voltage(vm: float) -> tuple:
    """This function can calculate the Average DC Voltage(Vdc) in a circuit.
    In all cases, a negative sign shows
    the opposite direction of current or voltage.
    Vdc = average direct current (DC)
    vm = maximum voltage or peak voltage
    cases:"""
    return Result('Vdc', 2 * 0.318 * vm)

def max_current(vm: float, rl: float) -> tuple:
    """This function can calculate the maximum current(Im) in a circuit.
    In all cases, a negative sign shows the
    opposite direction of current or voltage.
    vm = maximum voltage or peak voltage
    rl = load resistance
    cases:"""
    if rl <= 0:
        raise ValueError('Resistance cannot be negative or equal to zero')
    return Result('Max_current_Im', vm / rl)

def rms_current(im: float) -> tuple:
    """This function calculates the RMS(Root Mean Square) value of current(Irms).
    In all cases, a negative sign shows
    the opposite direction of current or voltage.
    Irms = Root Mean Square Value of current
    im = maximum current or peak current
    cases:"""
    return Result('Irms', im * 0.707)

def rms_voltage(vm: float) -> tuple:
    """This function calculates the RMS(Root Mean Square) value of voltage(Vrms).
    In all cases, a negative sign shows
    the opposite direction of current or voltage.
    Vrms = Root Mean Square Value of voltage
    vm = maximum voltage or peak voltage
    cases:"""
    return Result('Vrms', vm * 0.707)