# TODO: define with your ORM of choice (SQLAlchemy / SQLModel / Django-style if using DRF instead)
#
# class Plan:
#     id: UUID
#     user_id: UUID
#     scope: str  # "day" | "week" | "month"
#     start_date: date
#     end_date: date
#     source: str  # "voice" | "manual"
#     created_at: datetime
#
# class Task:
#     id: UUID
#     plan_id: UUID
#     title: str
#     due_date: date | None
#     is_done: bool
#     source: str  # "voice" | "manual"
