import logging
from fastapi import APIRouter, HTTPException
from models.customer_models import CustomerCreateRequest
from models.customer_models import CustomerCreate
from services.customers_service import CustomersService


router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

@router.post("/")
def create_customer_endpoint(customer: CustomerCreateRequest):
    try:
        CustomersService.create_customer(customer)
        return {"message": "Customer criado com sucesso"}
    except Exception as e:
        logging.error(f"Error while trying create customer: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error while trying create customer"
        )
