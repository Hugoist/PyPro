from datetime import datetime
from typing import List

from ninja import Schema


class GenreSchema(Schema):
    id: int
    name: str


class AuthorSchema(Schema):
    id: int
    name: str


class BookCreateSchema(Schema):
    title: str
    description: str | None = None
    genre_ids: List[int] | None = None
    author_ids: List[int]
    available_copies: int = 1


class BookUpdateSchema(Schema):
    title: str | None = None
    description: str | None = None
    genre_ids: List[int] | None = None
    author_ids: List[int] | None = None
    available_copies: int | None = None


class BookReadSchema(Schema):
    id: int
    title: str
    description: str | None
    genres: List[GenreSchema]
    authors: List[AuthorSchema]
    available_copies: int
    created_at: datetime
    updated_at: datetime


class RentalCreateSchema(Schema):
    book_id: int


class RentalReadSchema(Schema):
    id: int
    user_id: int
    book: BookReadSchema
    rented_at: datetime
    returned_at: datetime | None
