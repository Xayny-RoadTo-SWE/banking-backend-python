from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from models.accounts_models import (
    AccountCreate,
    AccountUpdate
)

class AccountRepository:
    
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def create_account(
            self,
            account_data: AccountCreate
        ):
            pass
        
    async def get_account_by_id(
            self,
            account_id: UUID
        ):
            pass
        
    async def list_accounts(self):
            pass
        
    async def update_account(
            self,
            account_id: UUID,
            account_data: AccountUpdate
        ):
            pass
        
    async def delete_account(
            self,
            account_id: UUID
        ):
            pass