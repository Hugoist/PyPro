from typing import List, Dict


class UserManager:
    """
    Class to manage users in memory
    """

    def __init__(self):
        self._users: List[Dict[str, int]] = []

    def add_user(self, name: str, age: int):
        self._users.append({"name": name, "age": age})

    def remove_user(self, name: str):
        self._users = [user for user in self._users if user["name"] != name]

    def get_all_users(self) -> List[Dict[str, int]]:
        return self._users.copy()
