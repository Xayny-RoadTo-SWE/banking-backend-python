import logging
from fastapi import APIRouter, HTTPException
from models.user_models import UserCreateRequest
from services.users_service import UserServices


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
        raise HTTPException(status_code=500, detail="Erro na tentativa de criar usuário.")

