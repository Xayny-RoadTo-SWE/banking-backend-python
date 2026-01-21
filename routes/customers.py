from fastapi import APIRouter
from pydantic import BaseModel
import logging

from services.customers_service import create_customer

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


class CustomerCreate(BaseModel):
    nome: str


@router.post("/")
def create_customer_endpoint(customer: CustomerCreate):
    logging.info(
        f"Recebida requisição para criar customer: {customer.nome}"
    )
    create_customer(customer.nome)
    return {"message": f"Customer '{customer.nome}' criado com sucesso"}
