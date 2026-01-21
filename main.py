from fastapi import FastAPI

from routes import customers, users, accounts, transactions

app = FastAPI(title="Banking Backend API")

app.include_router(customers.router)
app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(transactions.router)
