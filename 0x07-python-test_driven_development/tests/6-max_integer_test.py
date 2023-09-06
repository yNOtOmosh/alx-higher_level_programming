#!/usr/bin/python3
"""Unittests for max_integer([..])."""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines unittests for max_integer([..])."""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]), "Empty list should return None")

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42, "Single-element list should return the element")

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5, "Should return the maximum of positive numbers")

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1, "Should return the maximum of negative numbers")

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-5, 0, 5, -10, 10]), 10, "Should return the maximum of mixed numbers")

    def test_duplicate_max(self):
        self.assertEqual(max_integer([3, 3, 3, 3, 3]), 3, "Should return the maximum if all elements are the same")

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.2, 2.5]), 3.2, "Should return the maximum of float numbers")

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'two', 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
