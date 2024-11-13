"""
A test case module for the calculator program
"""

from helper import (
    get_input,
    addition,
    subtract,
    division,
    multiply,
)
import unittest
from unittest.mock import patch


class TestCalculator(unittest.TestCase):
    """
    Test cases for calculator functions.
    """

    @patch("helper.input", return_value="2 + 3")
    def test_get_input(self, mock_choice):
        """
        Test get_input for three arguments.
        """
        sample_output = (2, "+", 3)
        self.assertEqual(get_input(), sample_output)

    def test_addition(self):
        """Test addition function"""
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(2, -3), -1)
        self.assertEqual(addition(-2, 3), 1)

    def test_subtraction(self):
        """Test subtraction function"""
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(2, -3), 5)
        self.assertEqual(subtract(-2, 3), -5)

    def test_multiplication(self):
        """Test subtraction function"""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(2, -3), -6)
        self.assertEqual(multiply(-2, 3), -6)

    def test_division(self):
        """Test division function"""
        self.assertEqual(division(2, 3), 0.7)
        self.assertEqual(division(2, -3), -0.7)
        self.assertEqual(division(-2, 3), -0.7)


if __name__ == "__main__":
    unittest.main()
