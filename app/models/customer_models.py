from pydantic import BaseModel

class CustomerCreateRequest(BaseModel):
    name: str
    manager_id: int

class CustomerResponse(BaseModel):
    id: int
    name: str
    manager_id: int
    balance: float

from datetime import date

class DocumentType(str, Enum):
    CPF = "CPF"
    RG = "RG"
class CustomerBase(BaseModel):
    full_name: str
    birth_date: date
    document_type: DocumentType
    document_number: str = Field(
        min_length=5, 
        max_length=20, 
        pattern=r"^\d+$",
        description="Apenas os números do documento")
    manager_id: Optional[UUID] = None
    amount: float  = 0.0
    
class CustomerCreate(CustomerBase):
    id: Optional[UUID] = None

class CustomerCreateRequest(CustomerBase):
    pass
class CustomerResponse(CustomerBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    class Config:
        from_attributes = True