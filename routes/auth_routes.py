from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from models.auth_models import UserLogin, TokenSchema
from security.auth_handler import sign_jwt

router = APIRouter(prefix="/auth", tags=["Auth"])

login = [
    {
        "email": "alex@sunfire.com",
        "password": "senha_secreta_aqui"
    }
]


# Função temporária para validar o login (Mude para o seu email de teste!)
def check_user(data: UserLogin) -> bool:
    if data.email == login[0]["email"] and data.password == login[0]["password"]:
        return True
    return False

@router.post("/login", response_model=TokenSchema)
async def user_login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == login[0]["email"] and form_data.password == login[0]["password"]:
            token_data = sign_jwt(form_data.username)
            return TokenSchema(**token_data)
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="Invalid email or password"
        )   