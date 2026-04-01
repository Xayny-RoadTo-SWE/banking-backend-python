from database import DatabaseAdapter
import logging 
from repositories.repo_queries import CREATE_USER, GET_BALANCE

class BankRepo:
    @staticmethod
    def create_user(nome: str) -> None: 
        if DatabaseAdapter.insert(CREATE_USER, nome):
            logging.info(f"Usuário '{nome}' criado com sucesso!")
        else:
            logging.error("Erro ao criar usuário:")
    
    @staticmethod
    def get_balance(user_id: str) -> float:
        return DatabaseAdapter.fetchone(GET_BALANCE, user_id)

