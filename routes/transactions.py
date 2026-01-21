"""
Rotas relacionadas às TRANSAÇÕES bancárias.

Transactions representam toda movimentação financeira do sistema, como:
- depósito
- saque
- transferência

Aqui ficarão endpoints para registrar e consultar movimentações financeiras.
"""
from fastapi import APIRouter
from pydantic import BaseModel

from services.transactions_service import deposit, withdraw, transfer

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


class DepositRequest(BaseModel):
    account_id: int
    amount: float


class WithdrawRequest(BaseModel):
    account_id: int
    amount: float


class TransferRequest(BaseModel):
    from_account_id: int
    to_account_id: int
    amount: float


@router.post("/deposit")
def deposit_endpoint(data: DepositRequest):
    deposit(data.account_id, data.amount)
    return {"message": "Depósito realizado com sucesso"}


@router.post("/withdraw")
def withdraw_endpoint(data: WithdrawRequest):
    withdraw(data.account_id, data.amount)
    return {"message": "Saque realizado com sucesso"}


@router.post("/transfer")
def transfer_endpoint(data: TransferRequest):
    transfer(
        data.from_account_id,
        data.to_account_id,
        data.amount
    )
    return {"message": "Transferência realizada com sucesso"}
