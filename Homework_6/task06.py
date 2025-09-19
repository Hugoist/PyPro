import os


class DirectoryIterator:
    """
    Iterator that yields file's name and size for every file in the directory
    """

    def __init__(self, path: str):
        self.path = path
        self.files = self.get_files()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.files):
            raise StopIteration

        file_name = self.files[self.index]
        file_size = os.path.getsize(os.path.join(self.path, file_name))
        self.index += 1
        return file_name, file_size

    def get_files(self) -> list:
        files = []
        for f in os.listdir(self.path):
            if os.path.isfile(os.path.join(self.path, f)):
                files.append(f)
        return files


# test
for name, size in DirectoryIterator("."):
    print(f"File: {name}, Size: {size} bytes")
