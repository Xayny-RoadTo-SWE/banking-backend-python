"""
Repositório de acesso ao banco de dados para USERS (funcionários do banco).

Este arquivo será responsável por:
- persistir usuários internos
- buscar usuários por id, login, etc.
- atualizar dados de usuários internos
"""

"""
Repository responsável pelo acesso a dados de USERS (funcionários).
"""

from database import DatabaseAdapter
from models.user_models import UserCreateRequest

class UsersRepository:

    @staticmethod
    def create_user(user: UserCreateRequest) -> None:
        DatabaseAdapter.insert(
            """
            INSERT INTO users (nome, role, document_number, document_type)
            VALUES (%s, %s, %s, %s)
            """,
            (user.nome, user.role, user.document_number, user.document_type)
        )
