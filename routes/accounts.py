import logging
from fastapi import APIRouter, HTTPException
from models.account_models import AccountCreate
from services.accounts_service import AccountServices


router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"]
)

@router.post("/")
def open_account_endpoint(account: AccountCreate):
    try:
        AccountServices.open_account(account)
        return {"message": "Conta bancária criada com sucesso"}
    except Exception as e:
        logging.error(f"Error while trying open account: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error while trying open account"
        )


@router.get("/customer/{customer_id}")
def list_accounts_by_customer(customer_id: int):
    try:
        return AccountServices.get_accounts_by_customer(customer_id)
    except Exception as e:
        logging.error(f"Error while trying list accounts: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error while trying list accounts"
        )
