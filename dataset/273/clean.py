"""Convert between different units of temperature"""

def celsius_to_fahrenheit(celsius: float, ndigits: int=2) -> float:
    """Convert a given value from Celsius to Fahrenheit and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit"""
    return round(float(celsius) * 9 / 5 + 32, ndigits)

def celsius_to_kelvin(celsius: float, ndigits: int=2) -> float:
    """Convert a given value from Celsius to Kelvin and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin"""
    return round(float(celsius) + 273.15, ndigits)

def celsius_to_rankine(celsius: float, ndigits: int=2) -> float:
    """Convert a given value from Celsius to Rankine and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale"""
    return round(float(celsius) * 9 / 5 + 491.67, ndigits)

def fahrenheit_to_celsius(fahrenheit: float, ndigits: int=2) -> float:
    """Convert a given value from Fahrenheit to Celsius and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius"""
    return round((float(fahrenheit) - 32) * 5 / 9, ndigits)

def fahrenheit_to_kelvin(fahrenheit: float, ndigits: int=2) -> float:
    """Convert a given value from Fahrenheit to Kelvin and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin"""
    return round((float(fahrenheit) - 32) * 5 / 9 + 273.15, ndigits)

def fahrenheit_to_rankine(fahrenheit: float, ndigits: int=2) -> float:
    """Convert a given value from Fahrenheit to Rankine and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale"""
    return round(float(fahrenheit) + 459.67, ndigits)

def kelvin_to_celsius(kelvin: float, ndigits: int=2) -> float:
    """Convert a given value from Kelvin to Celsius and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius"""
    return round(float(kelvin) - 273.15, ndigits)

def kelvin_to_fahrenheit(kelvin: float, ndigits: int=2) -> float:
    """Convert a given value from Kelvin to Fahrenheit and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit"""
    return round((float(kelvin) - 273.15) * 9 / 5 + 32, ndigits)

def kelvin_to_rankine(kelvin: float, ndigits: int=2) -> float:
    """Convert a given value from Kelvin to Rankine and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale"""
    return round(float(kelvin) * 9 / 5, ndigits)

def rankine_to_celsius(rankine: float, ndigits: int=2) -> float:
    """Convert a given value from Rankine to Celsius and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale
    Wikipedia reference: https://en.wikipedia.org/wiki/Celsius"""
    return round((float(rankine) - 491.67) * 5 / 9, ndigits)

def rankine_to_fahrenheit(rankine: float, ndigits: int=2) -> float:
    """Convert a given value from Rankine to Fahrenheit and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale
    Wikipedia reference: https://en.wikipedia.org/wiki/Fahrenheit"""
    return round(float(rankine) - 459.67, ndigits)

def rankine_to_kelvin(rankine: float, ndigits: int=2) -> float:
    """Convert a given value from Rankine to Kelvin and round it to 2 decimal places.
    Wikipedia reference: https://en.wikipedia.org/wiki/Rankine_scale
    Wikipedia reference: https://en.wikipedia.org/wiki/Kelvin"""
    return round(float(rankine) * 5 / 9, ndigits)

def reaumur_to_kelvin(reaumur: float, ndigits: int=2) -> float:
    """Convert a given value from reaumur to Kelvin and round it to 2 decimal places.
    Reference:- http://www.csgnetwork.com/temp2conv.html"""
    return round(float(reaumur) * 1.25 + 273.15, ndigits)

def reaumur_to_fahrenheit(reaumur: float, ndigits: int=2) -> float:
    """Convert a given value from reaumur to fahrenheit and round it to 2 decimal places.
    Reference:- http://www.csgnetwork.com/temp2conv.html"""
    return round(float(reaumur) * 2.25 + 32, ndigits)

def reaumur_to_celsius(reaumur: float, ndigits: int=2) -> float:
    """Convert a given value from reaumur to celsius and round it to 2 decimal places.
    Reference:- http://www.csgnetwork.com/temp2conv.html"""
    return round(float(reaumur) * 1.25, ndigits)

def reaumur_to_rankine(reaumur: float, ndigits: int=2) -> float:
    """Convert a given value from reaumur to rankine and round it to 2 decimal places.
    Reference:- http://www.csgnetwork.com/temp2conv.html"""
    return round(float(reaumur) * 2.25 + 32 + 459.67, ndigits)