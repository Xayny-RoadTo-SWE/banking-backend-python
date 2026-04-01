import logging
from uuid import UUID
from database import DatabaseAdapter
from repositories.repo_queries import TRANSACTION_DEPOSIT, TRANSACTION_TRANSFER, TRANSACTION_WITHDRAW, TRANSACTION_GET_CUSTOMER_AMOUNT
from models.transaction_models import TransactionModel
class TransactionsRepository:

    @staticmethod
    def transaction_withdraw( transaction: TransactionModel):
        try:
            DatabaseAdapter.insert(
                TRANSACTION_WITHDRAW,
                (
                    transaction.id,
                    transaction.customer_origin, 
                    transaction.amount
                
                )
            )
        except Exception as e:
            logging.error("Erro ao registrar transação de saque:%s", e)
            raise
    @staticmethod
    def transaction_deposit(transaction: TransactionModel):
        try:
            DatabaseAdapter.insert(
                TRANSACTION_DEPOSIT,
                (
                    transaction.id,
                    transaction.customer_origin, 
                    transaction.amount
                )
            )
        except Exception as e:
            logging.error("Erro ao registrar transação de deposito:", e)
            raise
    @staticmethod
    def transaction_transfer(transaction: TransactionModel):
        try:
            DatabaseAdapter.insert(
                TRANSACTION_TRANSFER,
                (
                    transaction.customer_origin,
                    transaction.customer_destination,
                    transaction.amount
                )
            )
        except Exception as e:
            logging.error("Erro ao registrar transação de deposito:", e)
            raise

    @staticmethod
    def get_customer_amount(customer_id: UUID) -> float:
        try:
            result = DatabaseAdapter.fetchone(
                TRANSACTION_GET_CUSTOMER_AMOUNT,
                (customer_id,)
            )
            return result[0] if result else 0.0
        except Exception as e:
            logging.error("Erro ao consultar o total de transações do cliente:", e)
            raise
        
    @staticmethod
    def get_transaction_by_id(transaction_id: UUID):
        try:
            result = DatabaseAdapter.fetchdict(
                """
                SELECT 
                    customer_origin,
                    customer_destination,
                    transaction_type,
                    amount
                FROM transactions
                WHERE id = %s
                """,
                (transaction_id,)
            )
            return result
        except Exception as e:
            logging.error("Erro ao consultar transação por ID: %s", e)
            raise
        
    @staticmethod
    def list_transactions_by_customer(customer_id: UUID ):
        try:
            return DatabaseAdapter.fetchalldict(
                """
                SELECT
                        id,
                        customer_origin,
                        customer_destination,
                        transaction_type,
                        amount
                        transaction_date
                    FROM transactions
                    WHERE customer_origin = %s
                    OR customer_destination = %s
                    ORDER BY transaction_date DESC
                    """
                    (str(customer_id), str (customer_id))
            )
        except Exception as e:
           logging.exception("Erro ao listar transações do customer %s: %s", customer_id, e)
           raise