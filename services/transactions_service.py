from fastapi import HTTPException
from repositories.transactions_repo import TransactionsRepository
class TransactionService:

    @staticmethod
    def deposit(account_id: int, amount: float):
        """
        Realiza um depósito em uma conta.
        """
        # TODO: validar valor
        # TODO: atualizar saldo da conta
        # TODO: registrar transação
        pass

    @staticmethod
    def withdraw(account_id: int, amount: float):
        """
        Realiza um saque em uma conta.
        """
        # TODO: validar saldo disponível
        # TODO: atualizar saldo da conta
        # TODO: registrar transação
        pass

    @staticmethod
    def transfer(from_account_id: int, to_account_id: int, amount: float):
        """
        Realiza uma transferência entre contas.
        """
        # TODO: validar saldo
        # TODO: debitar conta origem
        # TODO: creditar conta destino
        # TODO: registrar transação
        pass

    @staticmethod   
    def get_transaction_by_id(transaction_id: int):
        transaction = TransactionsRepository.get_transaction_by_id(transaction_id) 
        
        if not transaction:
            raise HTTPException(status_code=404, detail="Transaction not found")
        
        return {
            "transaction": {
                "customer_origin" : transaction["customer_origin"],
                "customer_dest" : transaction["customer_destination"],
                "operation" : transaction["transaction_type"],
                "amount" : transaction["amount"]
            }
        }
        
    @staticmethod
    def list_transactions_by_customer(customer_id: int):
        transactions = TransactionsRepository.list_transactions_by_customer(customer_id)
        
        return {
            "transactions": [
                {
                    "customer_origin" : transaction["customer_origin"],
                    "customer_dest" : transaction["customer_destination"],
                    "operation" : transaction["transaction_type"],
                    "amount" : transaction["amount"]
                }
                for transaction in transactions
            ]
        }
