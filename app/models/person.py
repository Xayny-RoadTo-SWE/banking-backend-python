import uuid

from datetime import date, datetime
from uuid import UUID

from sqlalchemy import(
    String,
    Date,
    DateTime,
    func
)

from sqlalchemy.orm import(
    Mapped,
    mapped_column
)

from app.core.database import Base

class Person(Base):
    
    __tablename__ = "persons"
    
    person_id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4
    )
    
    full_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    
    birth_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )
    
    cpf: Mapped[str] = mapped_column(
        String(11),
        unique=True,
        nullable=False
    )
    
    email: Mapped[str | None] = mapped_column(
        String(255),
        unique=True,
        nullable=True
    )
    
    phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )
    
    sex: Mapped[str | None] = mapped_column(
        String(1),
        nullable=True
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