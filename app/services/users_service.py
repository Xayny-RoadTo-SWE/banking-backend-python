from uuid import UUID
from fastapi import HTTPException, status
from models.user_models import UserCreateRequest, UserCreateResponse
from tasks.user_tasks import UserTasks
from repositories.repo import BankRepo
class UserServices:
    """CRUD de usuários - dados cadastrais"""

    @staticmethod
    def create_user(user: UserCreateRequest):
        """
        Cria um usuário interno do banco.
        """
        logging.info(f"Iniciando criação de usuário: {user.nome}")
        UserTasks.validate_user(user)
        UserTasks.create_user(user)
        return UserCreateResponse(message="usuario criado com sucesso", http_code="ok")

    
    @staticmethod
    def update_user():
        pass

    @staticmethod
    def get_user_by_id(user_id: UUID):
        pass
    
    @staticmethod
    def get_user_by_email(user_id: UUID):
        pass
    
    @staticmethod
    def delete_user():
        pass
    
    @staticmethod
    def deactivate_user():
        pass
    
    @staticmethod
    def activate_user():
        pass
    
    
    @staticmethod
    def verify_email():
        pass