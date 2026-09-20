from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def list_tasks():
    """Return tasks, optionally filtered by plan/date range."""
    # TODO: query DB
    return {"tasks": []}


@router.patch("/{task_id}")
def update_task(task_id: str):
    """Check off, edit, or reschedule a task."""
    # TODO: update DB record
    return {"message": f"task {task_id} updated"}
