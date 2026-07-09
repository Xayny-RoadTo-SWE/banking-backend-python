from pydantic import BaseModel,Field, EmailStr

class UserLogin(BaseModel):
    email: EmailStr = Field(..., description="O endereço de email do usuário")
    password: str = Field(..., description="A senha do usuário")
    
class Config:
    json_schema_extra = {
        "example": {
                "email": "alex@sunfire.com",
                "password": "senha_secreta_aqui"
        }       
    }
    
    # Esquema para a resposta que contém o Token JWT
class TokenSchema(BaseModel):
    access_token: str
    token_type: str