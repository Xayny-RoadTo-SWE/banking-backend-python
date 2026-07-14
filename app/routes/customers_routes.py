from uuid import UUID
from fastapi import APIRouter, status
from models.customer_models import CustomerCreateRequest, CustomerResponse
from services.customers_service import CustomersService


router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

@router.post("/", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
def create_customer(customer: CustomerCreateRequest) ->CustomerResponse: 
    return CustomersService.create_customer(customer)

@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: UUID) -> CustomerResponse:
    pass 

@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer(customer_id: UUID) -> CustomerResponse:
    pass

@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(customer_id: UUID):
    pass