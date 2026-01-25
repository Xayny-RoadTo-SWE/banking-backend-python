from pydantic import BaseModel
from datetime import date

class CustomerCreate(BaseModel):
    nome_completo: str
    data_nascimento: date
    tipo_documento: str
    numero_documento: str
