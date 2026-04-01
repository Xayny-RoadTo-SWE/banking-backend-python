from uuid import UUID
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from enum import Enum

class TransactionType(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    TRANSFER = "transfer"
class TransactionModel(BaseModel):
    customer_origin: UUID
    customer_destination: Optional[UUID] = None
    amount: float = Field(..., gt=0, description="O valor da transação deve ser maior que zero" )
    transaction_type: TransactionType
class TransactionCreateRequest(TransactionModel):
    pass
class TransactionResponse(TransactionModel):
    id: UUID
    transaction_date: datetime
    created_at: datetime
    updated_at: datetime    
    class Config:
        from_attributes = True