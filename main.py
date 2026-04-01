from fastapi import FastAPI
import logging
import logging_conf
from services import create_user
from models.customer_models import CustomerCreateRequest, CustomerResponse

app = FastAPI(title="Banking Backend API")


@app.post("/users")
def create_user_endpoint(nome: str):
    logging.info(f"Recebida requisição para criar usuário: {nome}")
    create_user(nome)
    return {"message": f"Usuário '{nome}' criado com sucesso"}

@app.post("/customers", response_model=CustomerResponse, status_code=201)
def create_customer_endpoint(customer: CustomerCreateRequest):
    return CustomerResponse(
        id=1,
        name=customer.name,
        manager_id=customer.manager_id,
        balance=0.0
    )

from routes import customers, users, accounts, transactions

app = FastAPI(title="Banking Backend API")

app.include_router(customers.router)
app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(transactions.router)
