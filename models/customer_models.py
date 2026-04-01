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

class CustomerCreate(BaseModel):
    nome_completo: str
    data_nascimento: date
    tipo_documento: str
    numero_documento: str
