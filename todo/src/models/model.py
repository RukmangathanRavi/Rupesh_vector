from datetime import datetime
from sqlalchemy import DateTime, String, Integer, Text, func, BOOLEAN
from sqlalchemy.orm import Mapped, mapped_column
from src.utils.base import Base

class Todo(Base):
    __tablename__ = "todos"
    id:Mapped[int] = mapped_column(Integer, primary_key=True)
    title:Mapped[str] = mapped_column(String(200))
    description: Mapped[str | None] = mapped_column(String(200), default=None)
    completed: Mapped[bool] = mapped_column(BOOLEAN, default=False)
    created_at:Mapped[datetime] = mapped_column(DateTime(), server_default=func.now())