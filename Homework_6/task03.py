import csv
import os
from typing import Iterator, Tuple

from PIL import Image


class ImageStatsIterator:
    """
    Iterator that scans images in a folder and collects metadata
    """

    def __init__(self, folder: str, csv_file: str = "image_stats.csv") -> None:
        self.folder = folder
        self.files = [
            os.path.join(folder, f) for f in os.listdir(folder)
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp"))
        ]
        self.index = 0
        self.csv_file = csv_file

        # prepare CSV file with header
        with open(self.csv_file, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Filename", "Format", "Width", "Height"])

    def __iter__(self) -> Iterator[Tuple[str, str, Tuple[int, int], str]]:
        return self

    def __next__(self) -> Tuple[str, str, Tuple[int, int], str]:
        if self.index >= len(self.files):
            raise StopIteration

        file_path = self.files[self.index]
        self.index += 1

        try:
            with Image.open(file_path) as img:
                data = (os.path.basename(file_path), img.format, img.width, img.height)

                # append to CSV
                with open(self.csv_file, mode="a", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(data)

                return data
        except Exception as e:
            return (os.path.basename(file_path), f"Error: {e}", (), "")


# test
iterator = ImageStatsIterator("./")

for stats in iterator:
# ('Image_1.png', 'PNG', 250, 187)
# ('Image_2.JPG', 'JPEG', 250, 151)
    print(stats)