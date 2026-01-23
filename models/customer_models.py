from pydantic import BaseModel

class CustomerCreateRequest(BaseModel):
    name: str
    manager_id: int

class CustomerResponse(BaseModel):
    id: int
    name: str
    manager_id: int
    balance: float

