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

class TransactionServices:

    @staticmethod
    def deposit(account_id: int, amount: float):
        pass

    """
    Realiza um depósito em uma conta.
    """
    # TODO: validar valor
    # TODO: atualizar saldo da conta
    # TODO: registrar transação


@staticmethod
    def withdraw(account_id: int, amount: float):
        pass

    """
    Realiza um saque em uma conta.
    """
    # TODO: validar saldo disponível
    # TODO: atualizar saldo da conta
    # TODO: registrar transação



@staticmethod
    def transfer(from_account_id: int, to_account_id: int, amount: float):
        pass

    """
    Realiza uma transferência entre contas.
    """
    # TODO: validar saldo
    # TODO: debitar conta origem
    # TODO: creditar conta destino
    # TODO: registrar transação

