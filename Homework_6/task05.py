def even_numbers():
    n = 0
    while True:
        n += 2
        yield n


class LimitGenerator:
    """
    Context manager takes a generator, number of elements, output file path and writes each number to the file
    """

    def __init__(self, generator, limit, file_path):
        self.generator = generator
        self.limit = limit
        self.file_path = file_path
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, "w", encoding="utf-8")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            print(f"Writing data to {self.file_path}")
            self.file.close()

    def run(self):
        count = 0
        for num in self.generator:
            if count >= self.limit:
                break
            self.file.write(str(num) + "\n")
            count += 1


# test
gen = even_numbers()
with LimitGenerator(gen, 100, "even_numbers.txt") as lg:
    lg.run()
