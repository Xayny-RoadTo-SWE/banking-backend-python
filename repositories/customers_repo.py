"""
Repositório de acesso ao banco de dados para CUSTOMERS.

Este arquivo será responsável por:
- inserir customers no banco
- buscar customers
- atualizar dados de customers

Nenhuma regra de negócio deve ficar aqui.
"""

"""
Repository responsável pelo acesso a dados de CUSTOMERS.
"""

from database import DatabaseAdapter
from repositories.repo_queries import (
    CREATE_CUSTOMER,
    GET_CUSTOMER_BY_ID,
)


class CustomersRepository:

    @staticmethod
    def create_customer(nome: str) -> None:
        DatabaseAdapter.insert(
            CREATE_CUSTOMER,
            (nome,)
        )

    @staticmethod
    def get_customer_by_id(customer_id: int):
        return DatabaseAdapter.fetchone(
            GET_CUSTOMER_BY_ID,
            (customer_id,)
        )
