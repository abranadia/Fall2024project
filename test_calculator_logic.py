import pytest
from calculator_logic import CalculatorLogic
from pytest import approx

# Test for regression calculation (compute_regression)
def test_regression():
    x_values = [1.47, 1.5, 1.52, 1.55]
    y_values = [52.21, 53.12, 54.48, 55.84]
    
    # Calculate slope (m) and intercept (b)
    m, b = CalculatorLogic.compute_regression(x_values, y_values)
    
    # Debugging print statements for intermediate values
    print(f"Calculated m: {m}, Calculated b: {b}")
    
    # Assert for slope and intercept with approximate values
    assert m == approx(46.70588235294806, rel=1e-9)
    assert b == approx(1.65129729907159, rel=1e-9)

# Test for predicting y values based on regression formula
def test_predict_y():
    m = 46.70588235294806
    b = 1.65129729907159
    x_value = 1.535
    
    # Predict y based on regression formula
    result = CalculatorLogic.predict_y(x_value, m, b)
    expected_result = m * x_value + b
    
    # Debugging print statement for predicted value
    print(f"Predicted y for x = {x_value}: {result}")
    
    # Assert predicted y matches the expected result
    assert result == approx(expected_result, rel=1e-6)

# Test for sample standard deviation calculation
def test_sample_standard_deviation():
    values = [9, 6, 8, 5, 7]
    result = CalculatorLogic.compute_sample_standard_deviation(values)
    
    # Assert for correct sample standard deviation
    assert result == approx(1.5811388300841898, rel=1e-9)

# Test for population standard deviation calculation
def test_population_standard_deviation():
    values = [9, 6, 8, 5, 7]
    result = CalculatorLogic.compute_population_standard_deviation(values)
    
    # Assert for correct population standard deviation
    assert result == approx(1.4142135623731, rel=1e-9)

# Test for mean calculation
def test_mean():
    values = [9, 6, 8, 5, 7]
    result = CalculatorLogic.compute_mean(values)
    
    # Assert for correct mean value
    assert result == approx(7.0, rel=1e-9)

# Test for z-score calculation
def test_z_score():
    value = 11.5
    mean = 7
    std_dev = 1.5811388300841898
    result = CalculatorLogic.compute_z_score(value, mean, std_dev)
    
    # Assert for correct z-score value
    assert result == approx(2.846049894151541, rel=1e-9)

# Test for handling invalid inputs (non-numeric values in data)
def test_invalid_input():
    invalid_values = ["9", "6", "8", "invalid", "7"]
    
    with pytest.raises(ValueError):
        CalculatorLogic.compute_mean(invalid_values)

# Test for handling empty input data
def test_empty_input():
    empty_values = []
    
    with pytest.raises(ValueError):
        CalculatorLogic.compute_mean(empty_values)



