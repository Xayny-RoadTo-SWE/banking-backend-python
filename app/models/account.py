import uuid

from datetime import datetime
from uuid import UUID

from sqlalchemy import(
    String,
    Float,
    Numeric,
    DateTime,
    ForeignKey,
    func
)

from sqlalchemy.orm import(
    Mapped,
    mapped_column
)

from app.core.database import Base


class Account(Base):
    __tablename__ = "accounts"

    account_id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    person_id: Mapped[UUID] = mapped_column(
        ForeignKey("customers.person_id"),
        nullable=False,
    )

    account_number: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
    )

    balance: Mapped[float] = mapped_column(
        Numeric,
        nullable=False,
        default=0.0,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="ACTIVE",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )