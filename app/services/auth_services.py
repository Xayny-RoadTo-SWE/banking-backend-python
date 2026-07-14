import logging
from models.user_models import UserCreateRequest, UserCreateResponse
from tasks.user_tasks import UserTasks
from repositories.repo import BankRepo

class AuthServices:

@staticmethod
def lougout_user():
        pass
    
    
@staticmethod
def forgot_password():
        pass
@staticmethod
def change_password():
    pass

@staticmethod
def refresh_token():
        pass
@staticmethod
def login_user(login: str, password: str):
        """
        Autentica um usuário interno do banco.
        """
        # TODO: validar credenciais
        pass