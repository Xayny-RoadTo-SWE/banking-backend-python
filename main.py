from fastapi import FastAPI
import logging
import logging_conf

from services import create_user

app = FastAPI(title="Banking Backend API")


@app.post("/users")
def create_user_endpoint(nome: str):
    logging.info(f"Recebida requisição para criar usuário: {nome}")
    create_user(nome)
    return {"message": f"Usuário '{nome}' criado com sucesso"}
