from uuid import UUID
from fastapi import APIRouter, status, Depends
from models.loan_models import LoanRequest, LoanResponse
from services.loans_service import LoanServices
from security.auth_bearer import get_current_user

router = APIRouter(
    prefix="/loans",
    tags=["Loans"]
)

@router.post("/", response_model=LoanResponse, status_code=status.HTTP_201_CREATED)
def request_loan(data: LoanRequest, current_user = Depends(get_current_user)) -> LoanResponse:
    return LoanServices.request_loan(current_user.id, data)

@router.get("/{loan_id}", response_model=LoanRequest)
def get_loan_status(loan_id: UUID, currente_user = Depends(get_current_user)) -> LoanResponse:
    return LoanServices.get_loan_details(loan_id, currente_user.id)

