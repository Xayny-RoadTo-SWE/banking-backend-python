from pydantic import(
    BaseModel,
    Field, 
    EmailStr,
    ConfigDict
)
class UserLogin(BaseModel):
    email: EmailStr = Field(
        ..., 
        description="User email"
    )
    
    password: str = Field(
        ...,
        description="User password"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "alex@sunfire.com",
                "password": "senha_secreta_aqui"
            }
        }
    )
    
    # Esquema para a resposta que contém o Token JWT
class TokenSchema(BaseModel):
    access_token: str
    token_type: str