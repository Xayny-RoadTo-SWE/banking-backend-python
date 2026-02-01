from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from enum import Enum


class TransactionType(str, Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    TRANSFER = "transfer"


class TransactionCreateRequest(BaseModel):
    amount: float
    transaction_type: TransactionType
    customer_origin_id: int
    customer_destination_id: Optional[int] = None


class TransactionResponse(BaseModel):
    id: int
    amount: float
    transaction_type: TransactionType
    customer_origin_id: int
    customer_destination_id: Optional[int]
    created_at: datetime