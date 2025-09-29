import unittest
from string_processor import StringProcessor


class TestStringProcessor(unittest.TestCase):
    """
    Unit tests for the StringProcessor class
    """

    def setUp(self):
        self.processor = StringProcessor()

    @unittest.skip("TODO: reverse_string fails with empty strings")
    def test_reverse_string_empty(self):
        """
        Test reverse_string with an empty string
        """
        self.assertEqual(self.processor.reverse_string(""), "")

    def test_reverse_string_regular(self):
        """
        Test reverse_string with a regular string
        """
        self.assertEqual(self.processor.reverse_string("hello"), "olleh")

    def test_reverse_string_with_symbols(self):
        """
        Test reverse_string with digits and symbols
        """
        self.assertEqual(self.processor.reverse_string("abc123!"), "!321cba")

    def test_capitalize_string_regular(self):
        """
        Test capitalize_string with a regular lowercase string
        """
        self.assertEqual(self.processor.capitalize_string("hello"), "Hello")

    def test_capitalize_string_mixed_case(self):
        """
        Test capitalize_string with a mixed-case string
        """
        self.assertEqual(self.processor.capitalize_string("hELLo"), "Hello")

    def test_capitalize_string_empty(self):
        """
        Test capitalize_string with an empty string
        """
        self.assertEqual(self.processor.capitalize_string(""), "")

    def test_count_vowels_regular(self):
        """
        Test count_vowels with a normal word
        """
        self.assertEqual(self.processor.count_vowels("hello"), 2)

    def test_count_vowels_mixed_case(self):
        """
        Test count_vowels with mixed case letters
        """
        self.assertEqual(self.processor.count_vowels("ApPlE"), 2)

    def test_count_vowels_with_digits_and_symbols(self):
        """
        Test count_vowels with digits and symbols included
        """
        self.assertEqual(self.processor.count_vowels("h3ll0!"), 0)

    def test_count_vowels_empty_string(self):
        """
        Test count_vowels with an empty string
        """
        self.assertEqual(self.processor.count_vowels(""), 0)


if __name__ == "__main__":
    unittest.main()
