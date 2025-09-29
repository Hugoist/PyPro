from typing import Union


def parse_input(data: Union[int, str]) -> Union[int, None]:
    """
    Parsing integer from data input. Returns None if data isn't an integer
    """
    try:
        parsed_data = int(data)
    except ValueError:
        parsed_data = None

    return parsed_data


# tests
print(parse_input(42))  # 42
print(parse_input("100"))  # 100
print(parse_input("hello"))  # None
