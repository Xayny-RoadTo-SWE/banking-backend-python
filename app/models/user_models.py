from uuid import UUID
from datetime import datetime
from typing import Optional
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
        
class UserUpdateRequest(UserBase):
    name: Optional[str] = None
    email: Optional[str] = None
    login: Optional[str] = None