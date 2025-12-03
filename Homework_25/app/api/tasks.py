from django.shortcuts import get_object_or_404
from ninja import Router, Query

from app.api.auth import auth
from app.models.tasks import Task
from app.schemas.tasks import TaskCreateSchema, TaskReadSchema, TaskUpdateSchema

router = Router(tags=["Tasks"])


@router.post("/", auth=auth, response=TaskReadSchema)
def create_task(request, data: TaskCreateSchema):
    task = Task.objects.create(title=data.title, owner=request.user)
    return task


@router.get("/", auth=auth, response=list[TaskReadSchema])
def list_tasks(request, status: bool = Query(None), order_by: str = Query("created_at")):
    tasks = Task.objects.all()
    if status is not None:
        tasks = tasks.filter(is_completed=status)
    return tasks.order_by(order_by)


@router.get("/{task_id}", auth=auth, response=TaskReadSchema)
def get_task(request, task_id: int):
    return get_object_or_404(Task, id=task_id)


@router.put("/{task_id}", auth=auth, response=TaskReadSchema)
def update_task(request, task_id: int, data: TaskUpdateSchema):
    task = get_object_or_404(Task, id=task_id)
    if data.title is not None:
        task.title = data.title
    if data.is_completed is not None:
        task.is_completed = data.is_completed
    task.save()
    return task


@router.delete("/{task_id}", auth=auth)
def delete_task(request, task_id: int):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return {"success": True}
