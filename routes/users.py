"""
Rotas relacionadas aos USUÁRIOS INTERNOS do banco.

Users representam funcionários do banco, como:
- gerente
- administrador
- atendente

Aqui ficarão endpoints para:
- criar usuário interno
- autenticação
- controle de permissões e níveis de acesso
"""

from fastapi import APIRouter, HTTPException

from services.users_service import UserServices
from models.user_models import UserCreateRequest, UserCreateResponse
import logging

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/create")
def create_user_endpoint(user: UserCreateRequest):
    try:
        return UserServices.create_user(user)
    except Exception as e:
        logging.error(f"Erro ao criar usuário {e}")
        raise HTTPException(status_code=500, detail=f"Erro na tentativa de criar usuário.")
