import re
from typing import Iterator


def error_log_parser(file_path: str) -> Iterator[str]:
    """
    Generator that reads log files and yields lines with 4XX and 5XX errors
    """
    status_pattern = re.compile(r'\s(4\d{2}|5\d{2})\s')

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if status_pattern.search(line):
                yield line.rstrip("\n")


# test
input_file = "lorem.txt"
output_file = "errors.log"

with open(output_file, "w", encoding="utf-8") as out:
    for error_line in error_log_parser(input_file):
        out.write(error_line + "\n")

    print(f"Errors extracted to {output_file}")
