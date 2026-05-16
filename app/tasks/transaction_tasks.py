from models.transaction_models import TransactionModel, TransactionType
from repositories.transactions_repo import TransactionsRepository
import logging

class TransactionTasks:
    @classmethod
    def process_transaction(cls, transaction: TransactionModel):
        logging.info(
            f"Processing transaction from customer {transaction.customer_origin_id} operation {transaction.transaction_type} of amount {transaction.amount}")
        valid_operations = {
            TransactionType.WITHDRAW: cls._process_withdraw_funds,
            TransactionType.TRANSFER: cls._process_transfer_funds,
            TransactionType.DEPOSIT: cls._process_deposit_funds
        }

        if not cls.validate_transaction(transaction):
            raise Exception("Transaction validation failed.")
        valid_operations[transaction.transaction_type](transaction)

        logging.info(f"Transaction processed successfully for customer {transaction.customer_origin_id}")

        @staticmethod
        def _process_deposit_funds(transaction: TransactionModel) -> None:
            logging.info(f"Depositing {transaction.amount} to customer {transaction.customer_origin_id}")
            TransactionsRepository.transaction_deposit(transaction)

        @staticmethod
        def _process_transfer_funds(transaction: TransactionModel) -> None:
            logging.info(f"Transferring {transaction.amount} from customer {transaction.customer_origin_id} to customer {transaction.customer_destination_id}")
            if TransactionsRepository.get_customer_ammount(transaction.customer_origin_id) >= transaction.amount:
                TransactionsRepository.transaction_transfer(transaction)
                return

            raise Exception(f"Insufficient funds for customer {transaction.customer_origin_id} to transfer {transaction.amount}")

    @staticmethod
    def validate_transaction(transaction: TransactionModel) -> bool:
        if transaction.amount <= 0:
            logging.error("Invalid transaction amount: must be greater than zero.")
            return False

        if transaction.transaction_type == TransactionType.TRANSFER and not transaction.customer_destination_id:
            logging.error("Transfer transactions require a destination customer ID.")
            return False
        return True

    @staticmethod
    def _process_withdraw_funds(transaction: TransactionModel) -> None:
        logging.info(f"Withdrawing {transaction.amount} from customer {transaction.customer_origin_id}")
        if TransactionsRepository.get_customer_ammount(transaction.customer_origin_id) >= transaction.amount:
            TransactionsRepository.transaction_withdraw(transaction)

        raise Exception(f"Insufficient funds for customer {transaction.customer_origin_id} to withdraw {transaction.amount}"))
