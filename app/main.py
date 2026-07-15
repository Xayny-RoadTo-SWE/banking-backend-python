import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routes import customers, users, accounts, transactions, cards,loans, investments, auth_routes as auth
from security.auth_bearer import JWTBearer  

tags_metadata = [
    {"name": "Root", "description": "Mensagem de boas-vindas e status da API"},
    {"name": "Auth", "description": "Operações de login e segurança"},
    {"name": "Users", "description": "Gerenciamento de usuários do sistema"},
    {"name": "Customers", "description": "Gestão de clientes bancários"},
    {"name": "Accounts", "description": "Gerenciamento de contas bancárias"},
    {"name": "Transactions", "description": "Processamento de transações financeiras"},
    {"name": "Cards", "description": "Cartões bancários"},
    {"name": "Loans", "description": "Empréstimos"},
    {"name": "Investments", "description": "Investimentos"},
]

app = FastAPI(
    title="SunFire Banking ☀️🏦",
    description="Backend banking system built with FastAPI",
    version="1.0.0",
    openapi_tags=tags_metadata,
    swagger_ui_parameters={"syntaxHighlight": True}  
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(customers.router)
app.include_router(accounts.router, dependencies=[Depends(JWTBearer())])
app.include_router(transactions.router, dependencies=[Depends(JWTBearer())])
app.include_router(cards.router, dependencies=[Depends(JWTBearer())])
app.include_router(loans.router, dependencies=[Depends(JWTBearer())])
app.include_router(investments.router, dependencies=[Depends(JWTBearer())])

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the SunFire Banking API! 🔥🏦"}
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
