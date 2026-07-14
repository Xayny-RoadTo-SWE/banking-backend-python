from uuid import UUID
from fastapi import APIRouter, Depends, status
from models.user_models import (
    UserCreateRequest,
    UserUpdateRequest,
    UserResponse,
)
from security.auth_bearer import get_current_user
from security.permissions import require_role
from services.users_service import UserServices


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreateRequest)-> UserResponse:
    return UserServices.create_user(user)

@router.put("/me", response_model=UserResponse)
def update_my_profile(data: UserUpdateRequest, current_user= Depends(get_current_user)) -> UserResponse:
    return UserServices.update_user(current_user.id, data)

@router.get("/me", response_model=UserResponse)
def get_my_profile(current_user= Depends(get_current_user)) -> UserResponse:
    return UserServices.get_user_by_id(current_user.id)

@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
def delete_my_account(current_user = Depends(get_current_user)):
    return UserServices.deactivate_user(current_user.id)

@router.get("/", response_model=list[UserResponse], dependencies=[Depends(require_role("admin"))])
def list_all_users(skip: int = 0, limit: int = 100) -> list[UserResponse]:
    return UserServices.get_all_users(skip, limit)

@router.get("/{user_id}", response_model=UserResponse, dependencies=[Depends(require_role("admin"))])
def get_user_by_id(user_id: UUID) -> UserResponse:
    return UserServices.get_user_by_id(user_id)
#Controle de permissão.Isso deixa claro que somente administradores podem acessar essa rota.