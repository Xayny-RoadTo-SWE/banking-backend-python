"""
Repositório de acesso ao banco de dados para ACCOUNTS.

Este arquivo será responsável por:
- criar contas bancárias no banco de dados
- buscar contas por customer
- atualizar status e saldo das contas
"""

"""
Repository responsável pelo acesso a dados de ACCOUNTS.
"""

from database import DatabaseAdapter
from repositories.repo_queries import (
    CREATE_ACCOUNT,
    GET_ACCOUNTS_BY_CUSTOMER,
    UPDATE_ACCOUNT_BALANCE,
)


class AccountsRepository:

    @staticmethod
    def create_account(customer_id: int, account_type: str, saldo_inicial: float):
        DatabaseAdapter.insert(
            CREATE_ACCOUNT,
            (customer_id, account_type, saldo_inicial)
        )

    @staticmethod
    def get_accounts_by_customer(customer_id: int):
        return DatabaseAdapter.fetchall(
            GET_ACCOUNTS_BY_CUSTOMER,
            (customer_id,)
        )

    @staticmethod
    def update_balance(account_id: int, amount: float):
        DatabaseAdapter.execute(
            UPDATE_ACCOUNT_BALANCE,
            (amount, account_id)
        )
    @staticmethod
    def get_balance(user_id: str) -> float:
        return DatabaseAdapter.fetchone(GET_BALANCE, user_id)
