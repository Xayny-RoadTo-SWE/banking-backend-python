from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from models.customers_models import (
    CustomerCreate,
    CustomerUpdate
)

class CustomerRepository:
    
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create_customer(
        self,
        customer_data: CustomerCreate
    ):
        pass
   
    async def get_customer_by_id(
       self,
       customer_id: UUID
    ):
          pass
      
    async def list_customers(self):
        pass
    
    async def update_customer(
        self,
        customer_id: UUID,
        customer_data: CustomerUpdate
    ):
        pass 
    
    async def delete_customer(
        self,
        customer_id: UUID
    ):
        pass 
        