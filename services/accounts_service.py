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

def open_account(customer_id: int, account_type: str):
    """
    Abre uma nova conta bancária para um customer.
    """
    # TODO: verificar se customer existe
    # TODO: validar tipo de conta
    # TODO: criar conta com saldo inicial
    pass


def get_accounts_by_customer(customer_id: int):
    """
    Lista todas as contas de um customer.
    """
    # TODO: buscar contas associadas ao customer
    pass
