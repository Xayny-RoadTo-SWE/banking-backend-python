"""
Rotas relacionadas às TRANSAÇÕES bancárias.

Transactions representam toda movimentação financeira do sistema, como:
- depósito
- saque
- transferência

Aqui ficarão endpoints para registrar e consultar movimentações financeiras.
"""
import logging
from fastapi import APIRouter, HTTPException
from models.transaction_models import (
    DepositRequest,
    WithdrawRequest,
    TransferRequest
)
from services.transactions_service import TransactionServices


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

@router.post("/deposit")
def deposit_endpoint(data: DepositRequest):
    try:
        TransactionServices.deposit(data.account_id, data.amount)
        return {"message": "Depósito realizado com sucesso"}
    except Exception as e:
        logging.error(f"Error while trying deposit: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error while trying deposit"
        )



@router.post("/withdraw")
def withdraw_endpoint(data: WithdrawRequest):
    try:
        TransactionServices.withdraw(data.account_id, data.amount)
        return {"message": "Saque realizado com sucesso"}
    except Exception as e:
        logging.error(f"Error while trying withdraw: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error while trying withdraw"
        )


@router.post("/transfer")
def transfer_endpoint(data: TransferRequest):
    try:
        TransactionServices.transfer(
            data.from_account_id,
            data.to_account_id,
            data.amount
        )
        return {"message": "Transferência realizada com sucesso"}
    except Exception as e:
        logging.error(f"Error while trying transfer: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error while trying transfer"
        )

