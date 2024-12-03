# calculator_logic.py

import math

class CalculatorLogic:
    @staticmethod
    def compute_mean(values):
        if not values:
            raise ValueError("No valid numeric values provided.")
        return sum(values) / len(values)

    @staticmethod
    def compute_sample_std_dev(values):
        if len(values) < 2:
            raise ValueError("At least two values are required for sample standard deviation.")
        mean = CalculatorLogic.compute_mean(values)
        variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
        return math.sqrt(variance)

    @staticmethod
    def compute_population_std_dev(values):
        if len(values) < 2:
            raise ValueError("At least two values are required for population standard deviation.")
        mean = CalculatorLogic.compute_mean(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        return math.sqrt(variance)

    @staticmethod
    def compute_z_score(value, mean, std_dev):
        if std_dev == 0:
            raise ValueError("Standard deviation cannot be zero.")
        return (value - mean) / std_dev

    @staticmethod
    def compute_regression(x_values, y_values):
        if len(x_values) != len(y_values):
            raise ValueError("x and y values must have the same length.")
        n = len(x_values)
        numerator = n * sum(x * y for x, y in zip(x_values, y_values)) - sum(x_values) * sum(y_values)
        denominator = n * sum(x ** 2 for x in x_values) - sum(x_values) ** 2
        m = numerator / denominator
        b = (sum(y_values) - m * sum(x_values)) / n
        return m, b

    @staticmethod
    def predict_y(x, m, b):
        return m * x + b
