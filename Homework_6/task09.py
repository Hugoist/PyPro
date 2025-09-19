import shutil
from pathlib import Path


class BackupManager:
    """
    Context manager that creates file backup before processing
    """

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.backup_path = self.file_path.with_suffix(self.file_path.suffix + ".bak")

    def __enter__(self) -> Path:
        shutil.copy2(self.file_path, self.backup_path)
        print(f"Backup created: {self.backup_path}")
        return self.file_path

    def __exit__(self, exc_type, exc_val):
        if exc_type:
            print(f"Something went wrong. File restored from {self.backup_path}")
        else:
            self.backup_path.unlink()
            print(f"Processing successful. File backup deleted: {self.backup_path}")
        return False


file_path = "lorem.txt"

# successful processing
try:
    with BackupManager(file_path) as fpath:
        with open(fpath, "a", encoding="utf-8") as f:
            f.write("New content\n")
        raise RuntimeError("Simulated error")
except Exception as e:
    print(f"Error during processing: {e}\n")

with open(file_path, "r", encoding="utf-8") as f:
    print(f.read())

# failed processing
try:
    with BackupManager(file_path) as fpath:
        with open(fpath, "a", encoding="utf-8") as f:
            f.write("New content\n")
        raise RuntimeError("Simulated error")
except Exception as e:
    print(f"Error during processing: {e}\n")

with open(file_path, "r", encoding="utf-8") as f:
    print(f.read())
