import logging
from models.user_models import UserCreateRequest, UserCreateResponse
from tasks.user_tasks import UserTasks
from repositories.repo import BankRepo
import uuid6
class UserServices:

    @staticmethod
    def create_user(user: UserCreateRequest):
        """
        Cria um usuário interno do banco.
        """
        logging.info(f"Iniciando criação de usuário: {user.nome}")
        
        user.id = str(uuid6.uuid7())
        
        UserTasks.validate_user(user)
        UserTasks.create_user(user)
        
        return UserCreateResponse(message="usuario criado com sucesso", http_code="ok")

@staticmethod
def get_user_balance(user_id: str):
    """Busca o saldo de um usuário específico.
       Trazido da lógica antiga do services.py para manter a organização.
    """
    result = BankRepo.get_balance(str(user_id))
    
    if result is None:
        logging.error(f"Usuário {user_id} não encontrado para consulta de saldo.")
        return None
    
    return result[0]

    @staticmethod
    def authenticate_user(login: str, password: str):
        """
        Autentica um usuário interno do banco.
        """
        # TODO: validar credenciais
        pass
    