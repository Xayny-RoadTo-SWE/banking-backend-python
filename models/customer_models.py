from pydantic import BaseModel

class CustomerCreate(BaseModel):
    nome: str
