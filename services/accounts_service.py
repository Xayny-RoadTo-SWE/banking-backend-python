"""
Camada de regras de negócio para CONTAS BANCÁRIAS.

Este arquivo será responsável por:
- validar abertura de conta
- garantir regras como saldo inicial, status da conta, etc.
- orquestrar operações entre accounts, customers e transactions
"""

"""
Regras de negócio relacionadas às CONTAS BANCÁRIAS.
"""
class AccountServices:


@staticmethod
def open_account(account):
    pass

    """
    Abre uma nova conta bancária para um customer.
    """
    # TODO: verificar se customer existe
    # TODO: validar tipo de conta
    # TODO: criar conta com saldo inicial


@staticmethod
def get_accounts_by_customer(customer_id: int):
    pass

    """
    Lista todas as contas de um customer.
    """
    # TODO: buscar contas associadas ao customer

