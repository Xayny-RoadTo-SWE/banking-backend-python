
from enum import StrEnum
from pydantic import BaseModel


class UserCreateRequest(BaseModel):
    nome: str
    role: str
    document_number: str
    document_type: str

class UserCreateResponse(BaseModel):
    message: str
    http_code: str


class ValidDocumentType(StrEnum):
    CPF = "CPF"

class RolesEnum(StrEnum):
    MANAGER = "Gerente"
    ADMIN = "admin"
    DEV = "developer"
