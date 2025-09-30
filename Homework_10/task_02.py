import re


def find_phone_numbers(text: str) -> list[str]:
    """

    Search phone number from text
    """
    pattern = re.compile(r"(?:\(\d{3}\)\s*|\d{3}[-.]?)\d{3}[-.]?\d{4}")
    return re.findall(pattern, text)


# tests
text = """
My number is (123) 456-7890 or 345-644-4534. I live in app.73
Also my numbers 123.456.7890 or 4567899034.
"""

#  ['(123) 456-7890', '345-644-4534', '123.456.7890', '4567899034']
print(find_phone_numbers(text))
