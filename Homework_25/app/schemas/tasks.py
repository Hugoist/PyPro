from datetime import datetime

from ninja import Schema


class TaskCreateSchema(Schema):
    title: str


class TaskUpdateSchema(Schema):
    title: str = None
    is_completed: bool = None


class TaskReadSchema(Schema):
    id: int
    title: str
    is_completed: bool
    created_at: datetime
    owner_id: int

