from ninja import Router
from django.shortcuts import get_object_or_404
from typing import List
from django.utils import timezone

from app.models.monitoring import Server, Metric
from app.schemas.monitoring import ServerCreateSchema, ServerUpdateSchema, ServerReadSchema, MetricCreateSchema, MetricReadSchema
from app.api.auth import auth

router = Router(tags=["Monitoring"])


# SERVERS
@router.post("/servers", auth=auth, response=ServerReadSchema)
def create_server(request, data: ServerCreateSchema):
    server = Server.objects.create(**data.dict())
    return server


@router.get("/servers", response=List[ServerReadSchema])
def list_servers(request):
    return Server.objects.all()


@router.get("/servers/{server_id}", response=ServerReadSchema)
def get_server(request, server_id: int):
    server = get_object_or_404(Server, id=server_id)
    return server


@router.put("/servers/{server_id}", auth=auth, response=ServerReadSchema)
def update_server(request, server_id: int, data: ServerUpdateSchema):
    server = get_object_or_404(Server, id=server_id)
    for attr, value in data.dict().items():
        if value is not None:
            setattr(server, attr, value)
    server.updated_at = timezone.now()
    server.save()
    return server


@router.delete("/servers/{server_id}", auth=auth)
def delete_server(request, server_id: int):
    server = get_object_or_404(Server, id=server_id)
    server.delete()
    return {"success": True}


# METRICS
@router.post("/metrics", auth=auth, response=MetricReadSchema)
def create_metric(request, data: MetricCreateSchema):
    server = get_object_or_404(Server, id=data.server_id)
    metric = Metric.objects.create(
        server=server,
        name=data.name,
        value=data.value,
    )
    return metric


@router.get("/servers/{server_id}/metrics", response=List[MetricReadSchema])
def list_metrics(request, server_id: int):
    server = get_object_or_404(Server, id=server_id)
    return server.metrics.all()
