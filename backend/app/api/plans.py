"""Plans CRUD — always scoped to the authenticated user."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.core.deps import get_current_user
from app.models.plan import Plan
from app.models.user import User
from app.schemas import PlanCreate, PlanOut

router = APIRouter()


@router.get("/", response_model=list[PlanOut])
def list_plans(
    scope: str | None = None,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    query = db.query(Plan).filter(Plan.user_id == user.id)
    if scope in ("day", "week", "month"):
        query = query.filter(Plan.scope == scope)
    return query.order_by(Plan.created_at.desc()).all()


@router.post("/", response_model=PlanOut, status_code=201)
def create_plan(
    payload: PlanCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    if payload.scope not in ("day", "week", "month"):
        raise HTTPException(status_code=422, detail="scope must be day, week or month")
    plan = Plan(user_id=user.id, **payload.model_dump())
    db.add(plan)
    db.commit()
    db.refresh(plan)
    return plan


@router.get("/{plan_id}", response_model=PlanOut)
def get_plan(
    plan_id: str,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    plan = db.query(Plan).filter(Plan.id == plan_id, Plan.user_id == user.id).first()
    if plan is None:
        raise HTTPException(status_code=404, detail="Plan not found")
    return plan


@router.delete("/{plan_id}", status_code=204)
def delete_plan(
    plan_id: str,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    plan = db.query(Plan).filter(Plan.id == plan_id, Plan.user_id == user.id).first()
    if plan is None:
        raise HTTPException(status_code=404, detail="Plan not found")
    db.delete(plan)
    db.commit()
