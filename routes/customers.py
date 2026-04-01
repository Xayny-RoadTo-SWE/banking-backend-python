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
import logging
from fastapi import APIRouter, HTTPException
from models.customer_models import CustomerCreate
from services.customers_service import CustomerServices


router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

@router.post("/")
def create_customer_endpoint(customer: CustomerCreate):
    try:
        CustomerServices.create_customer(customer)
        return {"message": "Customer criado com sucesso"}
    except Exception as e:
        logging.error(f"Error while trying create customer: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error while trying create customer"
        )
