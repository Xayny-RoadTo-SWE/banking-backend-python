"""
Rotas relacionadas às CONTAS BANCÁRIAS.

Accounts representam as contas que pertencem aos customers.
Um customer pode possuir múltiplas contas.

Aqui ficarão endpoints para:
- abrir conta bancária
- listar contas de um customer
- encerrar conta
"""

from fastapi import APIRouter
from pydantic import BaseModel

from services.accounts_service import open_account, get_accounts_by_customer

router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"]
)


class AccountCreate(BaseModel):
    customer_id: int
    account_type: str


@router.post("/")
def open_account_endpoint(account: AccountCreate):
    open_account(account.customer_id, account.account_type)
    return {"message": "Conta bancária criada com sucesso"}


@router.get("/customer/{customer_id}")
def list_accounts_by_customer(customer_id: int):
    return get_accounts_by_customer(customer_id)
