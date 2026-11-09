from uuid import UUID
from datetime import datetime, date

from pydantic import(
    BaseModel,
    Field,
    ConfigDict
)

class EmployeeCreate(BaseModel):
    person_id: UUID
    employee_code: str = Field(
        ...,
        min_length=3,
        max_length=20
    )
    
    hire_date: date
    
class EmployeeResponse(BaseModel):
    person_id: UUID
    employee_code: str
    hire_date: date
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(
        from_attributes=True
    )