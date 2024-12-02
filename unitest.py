import unittest
from statistics import mean, stdev, pstdev

# Define the Calculator class methods (for simplicity, testing only the calculation methods)
class CalculatorLogic:

    @staticmethod
    def compute_mean(numbers):
        return mean(numbers)

    @staticmethod
    def compute_stdev(numbers, sample=True):
        if sample:
            return stdev(numbers)
        return pstdev(numbers)

    @staticmethod
    def compute_z_score(value, mean_val, stdev_val):
        return (value - mean_val) / stdev_val

    @staticmethod
    def compute_regression(x_vals, y_vals):
        n = len(x_vals)
        m = (n * sum(x * y for x, y in zip(x_vals, y_vals)) - sum(x_vals) * sum(y_vals)) / (n * sum(x ** 2 for x in x_vals) - sum(x_vals) ** 2)
        b = (sum(y_vals) - m * sum(x_vals)) / n
        return m, b


class TestCalculatorLogic(unittest.TestCase):

    # Test compute_mean
    def test_calculator_compute_mean_given_numbers_list_returns_mean(self):
        # Arrange
        numbers = [1, 2, 3, 4, 5]
        
        # Act
        result = CalculatorLogic.compute_mean(numbers)
        
        # Assert
        self.assertEqual(result, 3.0)

    # Test compute_stdev (Sample)
    def test_calculator_compute_stdev_given_sample_list_returns_sample_stdev(self):
        # Arrange
        numbers = [1, 2, 3, 4, 5]
        
        # Act
        result = CalculatorLogic.compute_stdev(numbers, sample=True)
        
        # Assert
        self.assertEqual(result, 1.58, places=2)

    # Test compute_stdev (Population)
    def test_calculator_compute_stdev_given_population_list_returns_population_stdev(self):
        # Arrange
        numbers = [1, 2, 3, 4, 5]
        
        # Act
        result = CalculatorLogic.compute_stdev(numbers, sample=False)
        
        # Assert
        self.assertEqual(result, 1.41, places=2)

    # Test compute_z_score
    def test_calculator_compute_z_score_given_value_mean_and_stdev_returns_z_score(self):
        # Arrange
        value = 5
        mean_val = 3
        stdev_val = 1.58
        
        # Act
        result = CalculatorLogic.compute_z_score(value, mean_val, stdev_val)
        
        # Assert
        self.assertEqual(result, 1.27, places=2)

    # Test compute_regression
    def test_calculator_compute_regression_given_x_and_y_values_returns_slope_and_intercept(self):
        # Arrange
        x_vals = [1, 2, 3, 4, 5]
        y_vals = [2, 4, 5, 4, 5]
        
        # Act
        m, b = CalculatorLogic.compute_regression(x_vals, y_vals)
        
        # Assert
        self.assertEqual(round(m, 2), 0.4)
        self.assertEqual(round(b, 2), 2.0)


# Run the tests
if __name__ == "__main__":
    unittest.main()
