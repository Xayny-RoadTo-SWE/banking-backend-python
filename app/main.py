import uvicorn
from fastapi import FastAPI
from routes import customers, users, accounts, transactions, auth_routes as auth
from security.auth_bearer import JWTBearer  
from fastapi import Depends

tags_metadata = [
    {"name": "Root", "description": "Mensagem de boas-vindas e status da API"},
    {"name": "Auth", "description": "Operações de login e segurança"},
    {"name": "Users", "description": "Gerenciamento de usuários do sistema"},
    {"name": "Customers", "description": "Gestão de clientes bancários"},
    {"name": "Accounts", "description": "Gerenciamento de contas bancárias"},
    {"name": "Transactions", "description": "Processamento de transações financeiras"},
    
]

app = FastAPI(
    title="SunFire Banking ☀️🏦",
    description="Backend banking system built with FastAPI",
    version="1.0.0",
    openapi_tags=tags_metadata,
    swagger_ui_parameters={"syntaxHighlight": True}  
)

<<<<<<< HEAD
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
=======
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(customers.router)
app.include_router(accounts.router, dependencies=[Depends(JWTBearer())])
app.include_router(transactions.router)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the SunFire Banking API! 🔥🏦"}
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
>>>>>>> 5f01a611ad639da564281c656aa3bb3f2f9a2d18
