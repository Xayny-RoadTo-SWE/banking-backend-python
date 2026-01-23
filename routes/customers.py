from fastapi import APIRouter, status

from models.customer_models import (
    CustomerCreateRequest,
    CustomerCreateResponse
)

router = APIRouter(
    prefix="/customers",
    tags=["customers"]
)

@router.post(
    response_model=CustomerCreateResponse,
    status_code=status.HTTP_201_CREATED
)

def create_customer(customer: CustomerCreateRequest):
    return CustomerCreateResponse(
        message="Customer created successfully",
        http_code="201"
    )