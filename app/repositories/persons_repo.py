from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from models.persons_models import PersonCreate, PersonUpdate


class PersonRepository:
    
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create_person(self, person_data: PersonCreate):
        pass
    
    async def get_person_by_id(self, person_id: UUID):
        pass
    
    async def list_persons(self):
        pass
    
    async def update_person(
        self, 
        person_id: UUID,
        person_data: PersonUpdate
    
    ):
        pass

    async def delete_person(self, person_id: UUID):
        pass
    
    