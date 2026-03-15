from fastapi import FastAPI
from routes import customers, users, accounts, transactions
import logging
import logging_conf
from services.users_service import UserServices
from models.user_models import UserCreateRequest
from models.customer_models import CustomerCreateRequest, CustomerResponse

app = FastAPI(title="Banking Backend API")

app.include_router(customers.router)
app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(transactions.router)

# TODO: ver depois nao gostei está no main
@app.post("/users")
def create_user_endpoint(user: UserCreateRequest):
    logging.info(f"Recebida requisição para criar usuário: {user.nome}")
    return {"message": f"Usuário '{user.nome}' criado com sucesso"}

@app.post("/customers", response_model=CustomerResponse, status_code=201)
def create_customer_endpoint(customer: CustomerCreateRequest):
    return CustomerResponse(
        id=1,
        name=customer.name,
        manager_id=customer.manager_id,
        balance=0.0
    )