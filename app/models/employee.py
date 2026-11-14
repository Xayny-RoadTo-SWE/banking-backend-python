import uuid

from datetime import date, datetime
from uuid import UUID

from sqlalchemy import (
    String,
    Date,
    DateTime,
    ForeignKey,
    func
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.core.database import Base


class Employee(Base):

    __tablename__ = "employees"

    person_id: Mapped[UUID] = mapped_column(
        ForeignKey("persons.person_id"),
        primary_key=True
    )

    employee_code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False
    )

    hire_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
    