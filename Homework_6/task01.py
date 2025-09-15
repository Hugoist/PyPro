class ReverseFileIterator:
    """Iterator that reads a file from the end """

    def __init__(self, path: str):
        self.filepath = path
        self.lines = []
        self.index = 0

        with open(path, "r", encoding="utf-8") as file:
            self.lines = file.readlines()

        self.index = len(self.lines) - 1  # begin from the last line

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.index < 0:
            raise StopIteration
        line = self.lines[self.index]
        self.index -= 1
        return line.rstrip("\n")


for line in ReverseFileIterator("lorem.txt"):
    print(line)
