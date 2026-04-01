from pydantic import BaseModel

class AccountCreate(BaseModel):
    customer_id: int
    account_type: str
