class StringProcessor:
    """
    A class for processing strings with various utility methods
    """

    def reverse_string(self, s: str) -> str:
        """
        Reverse the given string.
        """
        return s[::-1]

    def capitalize_string(self, s: str) -> str:
        """
        Capitalize the first letter of the given string
        """
        return s.capitalize()

    def count_vowels(self, s: str) -> int:
        """
        Count the number of vowels in the given string.
        """
        vowels = "уеїіаоєяиюУЕЇІАОЄЯИЮeuioaEUIOA"
        return sum(1 for char in s if char in vowels)
