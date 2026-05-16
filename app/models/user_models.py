from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
class UserBase(BaseModel):
    name: str
    email: str
    login: str
class UserCreateRequest(UserBase):
    password: str
class UserResponse(UserBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True
