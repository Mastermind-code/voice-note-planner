from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def list_plans():
    """Return all plans for the current user (day/week/month)."""
    # TODO: query DB, scope to authenticated user
    return {"plans": []}


@router.post("/")
def create_plan():
    """Create a plan manually from the app (not via voice note)."""
    # TODO: accept plan payload, persist to DB
    return {"message": "plan created"}
