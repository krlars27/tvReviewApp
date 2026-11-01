import unittest
from unittest.mock import patch

import app


class CalculateRatingTests(unittest.TestCase):
    def test_calculates_average_rating(self):
        self.assertEqual(app.calculate_rating(5, 5, 4, 4, 5), 4.6)

    def test_calculates_lowest_valid_rating(self):
        self.assertEqual(app.calculate_rating(1, 1, 1, 1, 1), 1.0)

    def test_calculates_highest_valid_rating(self):
        self.assertEqual(app.calculate_rating(5, 5, 5, 5, 5), 5.0)

    def test_rejects_rating_below_one(self):
        with self.assertRaises(ValueError):
            app.calculate_rating(0, 3, 3, 3, 3)

    def test_rejects_rating_above_five(self):
        with self.assertRaises(ValueError):
            app.calculate_rating(6, 3, 3, 3, 3)

    def test_rejects_non_integer_rating(self):
        with self.assertRaises(ValueError):
            app.calculate_rating(4.5, 3, 3, 3, 3)


class InputValidationTests(unittest.TestCase):
    @patch("builtins.input", side_effect=["not a number", "4"])
    def test_retries_after_non_integer_input(self, mock_input):
        self.assertEqual(app.get_integer("Enter a number: "), 4)
        self.assertEqual(mock_input.call_count, 2)

    @patch("builtins.input", side_effect=["-1", "2"])
    def test_retries_below_minimum(self, mock_input):
        self.assertEqual(app.get_integer("Season: ", minimum=0), 2)
        self.assertEqual(mock_input.call_count, 2)

    @patch("builtins.input", side_effect=["6", "5"])
    def test_retries_above_maximum(self, mock_input):
        self.assertEqual(app.get_integer("Rating: ", minimum=1, maximum=5), 5)
        self.assertEqual(mock_input.call_count, 2)

    @patch("builtins.input", side_effect=["   ", "Breaking Bad"])
    def test_retries_empty_text(self, mock_input):
        self.assertEqual(app.get_non_empty_text("Series: "), "Breaking Bad")
        self.assertEqual(mock_input.call_count, 2)


if __name__ == "__main__":
    unittest.main()
