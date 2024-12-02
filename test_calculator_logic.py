import unittest
from calculator_logic import *

class TestCalculatorLogic(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(compute_mean([1, 2, 3]), 2)

    def test_sample_std_dev(self):
        self.assertAlmostEqual(compute_sample_std_dev([9, 6, 8, 5, 7]), 1.5811388300841898)

    def test_population_std_dev(self):
        self.assertAlmostEqual(compute_population_std_dev([9, 6, 8, 5, 7]), 1.4142135623730951)

    def test_z_score(self):
        self.assertAlmostEqual(compute_z_score(11.5, 7, 1.5811388300841898), 2.846049894151541)

    def test_linear_regression(self):
        pairs = [(1, 2), (2, 4), (3, 6)]
        m, b = compute_linear_regression(pairs)
        self.assertEqual((m, b), (2.0, 0.0))

    def test_predict_y(self):
        self.assertEqual(predict_y(3, 2, 0), 6)

if __name__ == "__main__":
    unittest.main()
