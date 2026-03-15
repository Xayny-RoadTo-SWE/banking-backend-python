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
    customer_origin: int
    customer_destination: Optional[int] = None


class TransactionResponse(BaseModel):
    id: int
    amount: float
    transaction_type: TransactionType
    customer_origin: int
    customer_destination: Optional[int]
    created_at: datetime

class TransactionModel(BaseModel):
    customer_origin: int
    customer_destination: Optional[int] = None
    amount: float
    transaction_type: TransactionType
    
class singleTransactionResponse(BaseModel):
   transaction: TransactionResponse
class TransactionListResponse(BaseModel):
    transactions: list[singleTransactionResponse]
