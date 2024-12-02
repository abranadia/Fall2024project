import math

# Computes the mean
def compute_mean(values):
    if not values:
        raise ValueError("Input list must contain at least one numeric value.")
    return sum(values) / len(values)

# Computes the sample standard deviation
def compute_sample_std_dev(values):
    if len(values) < 2:
        raise ValueError("Input list must contain at least two numeric values.")
    mean = compute_mean(values)
    variance = sum((x - mean) ** 2 for x in values) / (len(values) - 1)
    return math.sqrt(variance)

# Computes the population standard deviation
def compute_population_std_dev(values):
    if len(values) < 2:
        raise ValueError("Input list must contain at least two numeric values.")
    mean = compute_mean(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return math.sqrt(variance)

# Computes the Z-score
def compute_z_score(value, mean, std_dev):
    if std_dev == 0:
        raise ValueError("Standard deviation cannot be zero.")
    return (value - mean) / std_dev

# Computes the linear regression (slope and intercept)
def compute_linear_regression(pairs):
    if len(pairs) < 2:
        raise ValueError("Input must contain at least two (x, y) pairs.")
    x_values, y_values = zip(*pairs)
    n = len(pairs)
    x_mean = compute_mean(x_values)
    y_mean = compute_mean(y_values)
    m = sum((x - x_mean) * (y - y_mean) for x, y in pairs) / sum((x - x_mean) ** 2 for x in x_values)
    b = y_mean - m * x_mean
    return m, b

# Predicts Y using the regression formula
def predict_y(x, slope, intercept):
    return slope * x + intercept
