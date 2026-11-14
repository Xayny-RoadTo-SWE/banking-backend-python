from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from models.users_models import(
    UserCreateRequest,
    UserUpdate
)

class UserRepository:
    
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def create_user(
        self,
        user_data: UserCreateRequest
    ):
        pass
    
    async def get_user_by_id(
        self,
        user_id: UUID
    ):
        pass

    async def list_users(self):
        pass
    
    async def update_user(
        self,
        user_id: UUID,
        user_data: UserUpdate
    ):
        pass
    
    async def delete_user(
        self,
        user_id: UUID
    ):
        pass