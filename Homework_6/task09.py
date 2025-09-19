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