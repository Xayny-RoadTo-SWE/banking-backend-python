import uuid

from datetime import datetime
from uuid import UUID

from sqlalchemy import (
    String,
    DateTime,
    ForeignKey,
    func
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.core.database import Base


class User(Base):

    __tablename__ = "users"

    user_id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )

    person_id: Mapped[UUID] = mapped_column(
        ForeignKey("persons.person_id"),
        nullable=False
    )

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
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