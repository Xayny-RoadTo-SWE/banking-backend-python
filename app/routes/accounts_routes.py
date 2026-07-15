from uuid import UUID
from fastapi import APIRouter, status
from models.account_models import AccountCreate, AccountResponse
from services.accounts_service import AccountServices


router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"]
)

@router.post("/", response_model=AccountResponse, status_code=status.HTTP_201_CREATED)
def open_account(account: AccountCreate) -> AccountResponse:
    return AccountServices.open_account(account)

@router.get("/customer/{customer_id}", response_model=list[AccountResponse])
def list_accounts_by_customer(customer_id: UUID) -> list[AccountResponse]:
    return AccountServices.get_accounts_by_customer(customer_id)

# ==========================================
# Esqueletos para futuras implementações REST
# ==========================================

@router.get("/{account_id}", response_model= AccountResponse)
def get_account(account_id: UUID) -> AccountResponse:
    pass

@router.put("/{account_id}", response_model=AccountResponse)
def update_account(account_id: UUID) ->AccountResponse:

@router.delete("/{account_id}", status_code=status.HTTP_204_NO_CONTENT)
def close_account(account_id: UUID):
    pass