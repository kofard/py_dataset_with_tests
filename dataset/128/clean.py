"""
Calculate joint probability distribution
https://en.wikipedia.org/wiki/Joint_probability_distribution
"""

def joint_probability_distribution(x_values: list[int], y_values: list[int], x_probabilities: list[float], y_probabilities: list[float]) -> dict:
    return {(x, y): x_prob * y_prob for x, x_prob in zip(x_values, x_probabilities) for y, y_prob in zip(y_values, y_probabilities)}

def expectation(values: list, probabilities: list) -> float:
    return sum((x * p for x, p in zip(values, probabilities)))

def variance(values: list[int], probabilities: list[float]) -> float:
    mean = expectation(values, probabilities)
    return sum(((x - mean) ** 2 * p for x, p in zip(values, probabilities)))

def covariance(x_values: list[int], y_values: list[int], x_probabilities: list[float], y_probabilities: list[float]) -> float:
    mean_x = expectation(x_values, x_probabilities)
    mean_y = expectation(y_values, y_probabilities)
    return sum(((x - mean_x) * (y - mean_y) * px * py for x, px in zip(x_values, x_probabilities) for y, py in zip(y_values, y_probabilities)))

def standard_deviation(variance: float) -> float:
    return variance ** 0.5