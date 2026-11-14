from datetime import date, datetime
from uuid import UUID

from sqlalchemy import (
    String,
    Date,
    DateTime,
    ForeignKey,
    func
)

from sqlalchemy.orm import(
    Mapped,
    mapped_column
)

from app.core.database import Base 

class Customer(Base):
    __tablename__= "customers"
    
    person_id: Mapped[UUID] = mapped_column(
        ForeignKey("persons.person_id"),
        primary_key=True
    )
    
    manager_id: Mapped[UUID | None] = mapped_column(
        nullable=True
    )
    
    risk_profile: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        default="LOW"
    )
    
    customer_since: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        server_default=func.current_date()
    )
    
    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="ACTIVE"
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

    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True
    )