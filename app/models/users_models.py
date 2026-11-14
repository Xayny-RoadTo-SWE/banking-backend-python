from uuid import UUID
from datetime import datetime

from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)

class UserCreateRequest(BaseModel):
    person_id: UUID
    username: str = Field(
        ...,
        min_length=3,
        max_length=50
    )
    
    password: str = Field(
        ...,
        min_length=8
    )
    
class UserResponse(BaseModel):
    user_id: UUID
    person_id: UUID
    username: str
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(
        from_attributes=True
    )
    
        
