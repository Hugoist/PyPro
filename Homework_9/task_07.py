from typing import TypedDict, Protocol, Optional, Dict


class User(TypedDict):
    id: int
    name: str
    is_admin: bool


class UserDatabase(Protocol):
    def get_user(self, user_id: int) -> Optional[User]:
        """Get user by id"""

    def save_user(self, user: User) -> None:
        """Save user to database"""


class InMemoryUserDB(UserDatabase):
    def __init__(self) -> None:
        self._users: Dict[int, User] = {}

    def get_user(self, user_id: int) -> Optional[User]:
        return self._users.get(user_id)

    def save_user(self, user: User) -> None:
        self._users[user["id"]] = user


if __name__ == "__main__":
    db = InMemoryUserDB()
    db.save_user({"id": 1, "name": "Alice", "is_admin": False})
    print(db.get_user(1))  # {"id": 1, "name": "Alice", "is_admin": False}
    print(db.get_user(2))  # None
