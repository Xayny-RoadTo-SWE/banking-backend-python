import logging
from fastapi import APIRouter, HTTPException
from models.transaction_models import (
    TransactionCreateRequest,
    TransactionResponse
)
from services.transactions_service import TransactionService


router = APIRouter(prefix="/transaction", tags=["Transaction"])

@router.post("/deposit")
def deposit_endpoint(data: TransactionCreateRequest):
    try:
        TransactionService.deposit(data.account_id, data.amount)
        return {"message": "Depósito realizado com sucesso"}
    except Exception as e:
        logging.error(f"Error while trying deposit: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error while trying deposit"
        )



@router.post("/withdraw")
def withdraw_endpoint(data: TransactionCreateRequest):
    try:
        TransactionService.withdraw(data.account_id, data.amount)
        return {"message": "Saque realizado com sucesso"}
    except Exception as e:
        logging.error(f"Error while trying withdraw: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error while trying withdraw"
        )


@router.post("/transfer")
def transfer_endpoint(data: TransactionCreateRequest):
    try:
        TransactionService.transfer(
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

@router.get("/list_transactions_by_customer/{customer_id}")
def list_transactions_by_customer(customer_id: int):
    return TransactionService.list_transactions_by_customer(customer_id)

@router.get("/{transaction_id}")
def get_transaction_by_id(transaction_id: int):
    return TransactionService.get_transaction_by_id(transaction_id)

