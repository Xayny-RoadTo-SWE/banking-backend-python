from uuid import UUID
from fastapi import APIRouter, status
from models.transaction_models import (
    DepositRequest,
    WithdrawRequest,
    TransferRequest,
    TransactionResponse
)
from services.transactions_service import TransactionServices


router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)

@router.post("/{account_id}/deposit", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
def deposit(account_id: UUID, data: DepositRequest) ->TransactionResponse:
    return TransactionServices.deposit(account_id, data)

@router.post("/{account_id}/withdraw", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
def withdraw(account_id: UUID, data: WithdrawRequest) ->TransactionResponse:
    return TransactionServices.withdraw(account_id, data)


@router.post("/{account_id}/transfer", response_model=TransactionResponse, status_code=status.HTTP_201_CREATED)
def transfer(account_id: UUID, data: TransferRequest) -> TransactionResponse:
    return TransactionServices.transfer(account_id, data)