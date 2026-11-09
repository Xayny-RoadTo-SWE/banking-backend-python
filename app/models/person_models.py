from datetime import date
from uuid import UUID

from pydantic import (
    BaseModel,
    EmailStr, 
    Field, 
    field_validator
)



class PersonCreate(BaseModel):
    full_name: str = Field(
        ..., 
        min_length=2, 
        max_length=150
    )
    
    birth_date: date
    cpf: str = Field(..., pattern=r'^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$')
    email: EmailStr | None = None
    phone: str | None = None
    sex: str | None = Field(
        default=None,
        pattern=r"^[MFO]$"
    )
    
    @field_validator('cpf')
    @classmethod
    def validate_cpf_digits(cls, v: str) -> str:
        digits = [int(digit) for digit in v if digit.isdigit()]
        if len(digits) != 11 or len(set(digits)) == 1:
            raise ValueError('CPF inválido')
        
        # Validação do 1º dígito
        sum_first = sum(digits[i] * (10 - i) for i in range(9))
        digit_1 = (sum_first * 10 % 11) % 10
        if digits[9] != digit_1:
            raise ValueError('CPF inválido')

        # Validação do 2º dígito
        sum_second = sum(digits[i] * (11 - i) for i in range(10))
        digit_2 = (sum_second * 10 % 11) % 10
        if digits[10] != digit_2:
            raise ValueError('CPF inválido')

        return "".join(str(d) for d in digits)
    
class PersonResponse(PersonCreate):
    person_id: UUID