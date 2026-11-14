from datetime import datetime, date 
from uuid import UUID
from typing import Literal

from pydantic import BaseModel, ConfigDict

class CustomerCreate(BaseModel):
    
    person_id: UUID
    manager_id: UUID | None = None
    risk_profile: Literal[
        "LOW",
         "MEDIUM",
         "HIGH"
    ] = "LOW"
    
class CustomerUpdate(BaseModel):
    manager_id: UUID | None = None
    risk_profile: Literal[
        "LOW",
        "MEDIUM",
        "HIGH"
    ] | None = None
    
class CustomerResponse(BaseModel):

    person_id: UUID
    manager_id: UUID | None = None
    risk_profile: Literal["LOW", "MEDIUM", "HIGH"]
    customer_since: date
    status: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None
    
    model_config = ConfigDict(from_attributes=True)