from datetime import datetime
from uuid import UUID
from decimal import Decimal
from enum import Enum

from pydantic import (
    BaseModel,
    Field,
    ConfigDict
)
class TransactionType(str, Enum):
    DEPOSIT = "DEPOSIT"
    WITHDRAW = "WITHDRAW"
    TRANSFER_IN = "TRANSFER_IN"
    TRANSFER_OUT = "TRANSFER_OUT"

class TransactionCreate(BaseModel):
    
    account_id: UUID
    related_account_id: UUID | None = None
    amount: Decimal = Field(
        ...,
        gt=0,
        description="Transaction amount must be greater than zero"
    )
    
    transaction_type: TransactionType
    
class TransactionResponse(BaseModel):
    transaction_id: UUID
    account_id: UUID
    related_account_id: UUID | None = None
    amount: Decimal
    transaction_type: TransactionType
    created_at: datetime
    
    model_config = ConfigDict(
        from_attributes=True
    )