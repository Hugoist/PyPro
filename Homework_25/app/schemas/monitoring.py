from datetime import datetime

from ninja import Schema


# SERVER
class ServerCreateSchema(Schema):
    name: str
    ip_address: str
    is_online: bool = True


class ServerUpdateSchema(Schema):
    name: str | None = None
    ip_address: str | None = None
    is_online: bool | None = None


class ServerReadSchema(Schema):
    id: int
    name: str
    ip_address: str
    is_online: bool
    created_at: datetime
    updated_at: datetime


# METRIC
class MetricCreateSchema(Schema):
    server_id: int
    name: str
    value: float


class MetricReadSchema(Schema):
    id: int
    server_id: int
    name: str
    value: float
    created_at: datetime
