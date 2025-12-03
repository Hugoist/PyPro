from ninja import Schema
from typing import List


class TagSchema(Schema):
    id: int
    name: str


class TagCreateSchema(Schema):
    name: str


class CommentSchema(Schema):
    id: int
    author: str
    text: str
    created_at: str


class CommentCreateSchema(Schema):
    text: str


class PostSchema(Schema):
    id: int
    title: str
    content: str
    tags: List[TagSchema]
    author: str
    created_at: str


class PostCreateSchema(Schema):
    title: str
    content: str
    tag_ids: List[int] = []


class PostUpdateSchema(Schema):
    title: str | None = None
    content: str | None = None
    tag_ids: List[int] | None = None
