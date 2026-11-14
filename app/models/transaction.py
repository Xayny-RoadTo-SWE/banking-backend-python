import uuid

from datetime import datetime
from uuid import UUID

from sqlalchemy import (
    String,
    DateTime,
    ForeignKey,
    Numeric,
    func
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.core.database import Base


class Transaction(Base):

    __tablename__ = "transactions"

    transaction_id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )

    account_id: Mapped[UUID] = mapped_column(
        ForeignKey("accounts.account_id"),
        nullable=False
    )

    related_account_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("accounts.account_id"),
        nullable=True
    )

    amount: Mapped[float] = mapped_column(
        Numeric(15, 2),
        nullable=False
    )

    transaction_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )