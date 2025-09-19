import zipfile
from pathlib import Path
from typing import List


class ZipArchiver:
    """
    Context manager for creating and managing a ZIP archive.
    """

    def __init__(self, archive_name: str, files: List[str]):
        self.archive_name = archive_name
        self.files = [Path(f) for f in files]
        self.zip_file = None

    def __enter__(self):
        self.zip_file = zipfile.ZipFile(self.archive_name, mode="w", compression=zipfile.ZIP_DEFLATED)

        print(f"Archive {self.archive_name} created.")

        for file in self.files:
            self.zip_file.write(file, arcname=file.name)
            print(f"Added {file} to archive.")

        return self.zip_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.zip_file:
            self.zip_file.close()

        return False


# test
files_to_archive = ["lorem.txt", "Image_1.png", "Image_2.jpg"]

# Archive archive.zip created.
# Added lorem.txt to archive.
# Added Image_1.png to archive.
# Added Image_2.jpg to archive.
# Archiving completed
with ZipArchiver("archive.zip", files_to_archive):
    print("Archiving completed")
