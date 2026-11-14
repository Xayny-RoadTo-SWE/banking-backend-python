from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from models.transactions_models import TransactionCreate


class TransactionRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def create_transaction(
        self,
        transaction_data: TransactionCreate
    ):
        pass
    
    async def get_transaction_by_id(
        self,
        transaction_id: UUID
    ):
        pass
    
    async def list_transactions(self):
        pass
    
    async def list_transactions_by_account(
        self,
        account_id: UUID
    ):
        pass
    
    async def delete_transaction(
        self,
        transaction_id: UUID
    ):
        pass