import json
from pathlib import Path

from typing import Dict, Any


class JsonConfigManager:
    """
    Context manager for reading and writing JSON configuration files
    """

    def __init__(self, path: str):
        self.path = path
        self.config: Dict[str, Any] = {}

    def __enter__(self) -> Dict[str, Any]:
        filename = Path(self.path)

        if filename.suffix != ".json":
            raise ValueError("Configuration file must be a JSON file")

        if filename.exists() and filename.stat().st_size > 0:
            with open(self.path, "r", encoding="utf-8") as f:
                try:
                    self.config = json.load(f)
                except json.JSONDecodeError:
                    print(f"Warning: {self.path} is not a valid JSON. Using empty config.")
                    self.config = {}
        else:
            # empty or missing file
            self.config = {}

        return self.config

    def __exit__(self, exc_type, exc_value, traceback):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=4)


# test
try:
    with JsonConfigManager("config.json") as cm:
        print(f"Username before change: {cm.get('username', 'guest')}")
        cm["username"] = "kokoko" if cm.get("username") != "kokoko" else "ololo"
        print(f"Username after change: {cm.get('username')}")
except ValueError as e:
    print("Error:", e)

print(json.dumps("config.json"))

try:
    with JsonConfigManager("lorem.txt") as cm:
        print(f"Username before change: {cm.get('username', 'guest')}")
except ValueError as e:
    print("Error:", e)
