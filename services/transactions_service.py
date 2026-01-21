"""
Camada de regras de negócio para TRANSAÇÕES.

Este arquivo será responsável por:
- validar operações financeiras
- garantir regras como saldo suficiente
- registrar corretamente cada movimentação no sistema
"""


"""
Regras de negócio relacionadas às TRANSAÇÕES bancárias.
"""

def deposit(account_id: int, amount: float):
    """
    Realiza um depósito em uma conta.
    """
    # TODO: validar valor
    # TODO: atualizar saldo da conta
    # TODO: registrar transação
    pass


def withdraw(account_id: int, amount: float):
    """
    Realiza um saque em uma conta.
    """
    # TODO: validar saldo disponível
    # TODO: atualizar saldo da conta
    # TODO: registrar transação
    pass


def transfer(from_account_id: int, to_account_id: int, amount: float):
    """
    Realiza uma transferência entre contas.
    """
    # TODO: validar saldo
    # TODO: debitar conta origem
    # TODO: creditar conta destino
    # TODO: registrar transação
    pass
