from uuid import UUID
from pydantic import BaseModel

class AccountCreate(BaseModel):
    customer_id: UUID
    account_type: str
