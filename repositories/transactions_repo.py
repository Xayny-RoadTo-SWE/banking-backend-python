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
from repositories.repo_queries import TRANSACTION_DEPOSIT, TRANSACTION_TRANSFER, TRANSACTION_WITHDRAW, TRANSACTION_GET_CUSTOMER_AMOUNT
import logging
from models.transaction_models import TransactionModel
class TransactionsRepository:

    @staticmethod
    def transaction_withdraw(
        transaction: TransactionModel
    ):
        try:
            DatabaseAdapter.insert(
                TRANSACTION_WITHDRAW,
                (transaction.customer_origin_id, transaction.amount)
            )
        except Exception as e:
            logging.error("Erro ao registrar transação de saque:", e)
            raise
    @staticmethod
    def transaction_deposit(
        transaction: TransactionModel
    ):
        try:
            DatabaseAdapter.insert(
                TRANSACTION_DEPOSIT,
                (transaction.customer_origin_id, transaction.amount)
            )
        except Exception as e:
            logging.error("Erro ao registrar transação de deposito:", e)
            raise
    @staticmethod
    def transaction_transfer(
        transaction: TransactionModel
    ):
        try:
            DatabaseAdapter.insert(
                TRANSACTION_TRANSFER,
                (transaction.customer_origin_id,transaction.customer_destination_id, transaction.amount)
            )
        except Exception as e:
            logging.error("Erro ao registrar transação de deposito:", e)
            raise

    @staticmethod
    def get_customer_ammount(customer_id: int) -> float:
        try:
            result = DatabaseAdapter.fetchone(
                TRANSACTION_GET_CUSTOMER_AMOUNT,
                (customer_id,)
            )
            return result[0] if result else 0.0
        except Exception as e:
            logging.error("Erro ao consultar o total de transações do cliente:", e)
            raise