from datetime import date, datetime
from typing import List

from ninja import Schema
from pydantic import Field


# Genre
class GenreCreateSchema(Schema):
    name: str


class GenreReadSchema(Schema):
    id: int
    name: str


# Movie
class MovieCreateSchema(Schema):
    title: str
    description: str | None = None
    release_date: date | None = None
    genre_ids: List[int] | None = None


class MovieUpdateSchema(Schema):
    title: str | None = None
    description: str | None = None
    release_date: date | None = None
    genre_ids: List[int] | None = None


class MovieReadSchema(Schema):
    id: int
    title: str
    description: str | None
    release_date: date | None
    genres: List[str]
    average_rating: float | None
    created_at: datetime


# Review
class ReviewCreateSchema(Schema):
    movie_id: int
    text: str | None = None
    score: int = Field(..., ge=1, le=10)


class ReviewReadSchema(Schema):
    id: int
    movie_id: int
    user_id: int
    username: str
    text: str | None
    score: int = Field(..., ge=1, le=10)
    created_at: datetime
