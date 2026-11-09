from datetime import datetime
from uuid import UUID
from typing import Literal

from pydantic import BaseModel, ConfigDict

class AccountCreate(BaseModel):
    
    customer_id: UUID
    account_number: str
    
class AccountResponse(BaseModel):
    
    account_id: UUID
    customer_id: UUID
    account_number: str
    balance: float
    status: Literal[
        "ACTIVE",
        "BLOCKED",
        "CLOSED"
    ]
    
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(
        from_attributes=True
    )