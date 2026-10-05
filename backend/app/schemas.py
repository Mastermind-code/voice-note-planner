from datetime import date, datetime

from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: str
    email: str
    created_at: datetime


class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"


class PlanCreate(BaseModel):
    title: str = "Untitled plan"
    scope: str = "week"
    source: str = "manual"
    transcript: str | None = None


class PlanOut(BaseModel):
    id: str
    title: str
    scope: str
    source: str
    created_at: datetime


class TaskCreate(BaseModel):
    plan_id: str
    title: str
    due_date: date | None = None
    source: str = "manual"


class TaskUpdate(BaseModel):
    title: str | None = None
    due_date: date | None = None
    is_done: bool | None = None


class TaskOut(BaseModel):
    id: str
    plan_id: str
    title: str
    due_date: date | None
    is_done: bool
    source: str
