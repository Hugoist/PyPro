def read_tokens(path: str) -> list[str]:
    """Reads tokens from a file"""

    with open(path, "r", encoding='utf-8') as file:
        content = file.read()
        return content.split()


def convert_tokens_to_numbers(tokens: list[str]) -> list[float]:
    """Converts a list of tokens to numbers."""

    numbers = []
    for token in tokens:
        try:
            numbers.append(float(token))
        except ValueError:
            raise ValueError(f"Invalid number: {token}")
    return numbers


def get_average(numbers: list[float]) -> float:
    """Returns the average of numbers."""

    if not numbers:
        raise ValueError("No numbers to average")
    return sum(numbers) / len(numbers)


files = [
    "task02-text.txt",  # Average: 27.7857
    "task02-text-value-error.txt",  # Value error: Invalid number: 56we
    "task02-text-empty.txt",  # Value error: No numbers to average
    "task02-text-ololo.txt"  # File error: [Errno 2] No such file or directory: 'task02-text-ololo.txt'
]

for path in files:
    print(f"\nReading file: {path}")
    try:
        tokens = read_tokens(path)
        numbers = convert_tokens_to_numbers(tokens)
        average = get_average(numbers)
        print(f"Average: {average:.4f}")
    except FileNotFoundError as e:
        print(f"File error: {e}")
    except ValueError as e:
        print(f"Value error: {e}")
