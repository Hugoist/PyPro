class FileProcessor:
    """
    Simple file processor for reading and writing data to file
    """

    def write_to_file(file_path: str, data: str):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(data)

    def read_from_file(file_path: str) -> str:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
