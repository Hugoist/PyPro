import json
from typing import List, Dict, Any


class LibraryManager:
    """
    Class for managing a collection of books stored in a JSON file.
    Supports loading, saving, filtering, and adding new books.
    """

    def __init__(self, filename: str):
        self.filename = filename

    def load_books(self) -> List[Dict[str, Any]]:
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self, books: List[Dict[str, Any]]) -> None:
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(books, f, ensure_ascii=False, indent=4)

    def get_available_books(self) -> List[Dict[str, Any]]:
        books = self.load_books()
        return [book for book in books if book.get("наявність", False)]

    def add_book(self, title: str, author: str, year: int, available: bool) -> None:
        books = self.load_books()
        new_book = {
            "назва": title,
            "автор": author,
            "рік": year,
            "наявність": available
        }
        books.append(new_book)
        self.save_books(books)


manager = LibraryManager("books.json")

# Show available books
print("Доступні книги:")
for book in manager.get_available_books():
    print(f"- {book['назва']} ({book['автор']}, {book['рік']})")

# Add a new book
manager.add_book("Книга 3", "Автор 3", 2020, True)
print("\nНова книга додана!")

# Show updated available books
print("\nДоступні книги після оновлення:")
for book in manager.get_available_books():
    print(f"- {book['назва']} ({book['автор']}, {book['рік']})")
