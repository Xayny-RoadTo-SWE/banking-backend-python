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
    