"""
Repositório de acesso ao banco de dados para TRANSACTIONS.

Este arquivo será responsável por:
- registrar transações financeiras
- consultar histórico de movimentações
- garantir persistência de todas as operações
"""

"""
Repository responsável pelo acesso a dados de TRANSACTIONS.
"""

from database import DatabaseAdapter
from repositories.repo_queries import CREATE_TRANSACTION


class TransactionsRepository:

    @staticmethod
    def create_transaction(
        account_id: int,
        transaction_type: str,
        amount: float
    ):
        DatabaseAdapter.insert(
            CREATE_TRANSACTION,
            (account_id, transaction_type, amount)
        )
