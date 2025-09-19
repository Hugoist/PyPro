from typing import Generator


def filter_lines(file_path: str, keyword: str) -> Generator[str, None, None]:
    """
    Generator that yields only lines containing the given keyword from a file
    """
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if keyword.lower() in line.lower():
                yield line.rstrip("\n")


# test
input_file = "lorem.txt"
output_file = "filtered.txt"
keyword = input("type keyword: ")

with open(output_file, "w", encoding="utf-8") as out:
    for line in filter_lines(input_file, keyword):
        out.write(line + "\n")

with open(output_file, "r", encoding="utf-8") as f:
    print(f"Строки с '{keyword}':")
    print(f.read())
