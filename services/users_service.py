"""
Camada de regras de negócio para USUÁRIOS INTERNOS do banco.

Este arquivo será responsável por:
- validar criação de usuários internos
- aplicar regras de permissão e acesso
- orquestrar operações relacionadas a funcionários do banco
"""

"""
Regras de negócio relacionadas aos USERS (funcionários do banco).
"""

from models.user_models import UserCreateRequest, UserCreateResponse
from tasks.user_tasks import UserTasks
class UserServices:

    @staticmethod
    def create_user(user: UserCreateRequest):
        """
        Cria um usuário interno do banco.
        """
        UserTasks.validate_user(user)
        UserTasks.create_user(user)
        return UserCreateResponse(message="usuario criado com sucesso", http_code="ok")


    @staticmethod
    def authenticate_user(login: str, password: str):
        """
        Autentica um usuário interno do banco.
        """
        # TODO: validar credenciais
        pass
    