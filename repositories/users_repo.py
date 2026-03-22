import uuid6
from database import DatabaseAdapter
from repositories.repo_queries import CREATE_USER
from models.user_models import UserCreateRequest

class UsersRepository:

    @staticmethod
    def create_user(user: UserCreateRequest) -> str:
        new_id_v7 = uuid6.uuid7()
        
        # TODO: Implementar bcrypt ou passlib aqui.  
        hashed_password = user.password  # Replace with actual hashing logic
        
        params = (
            str(new_id_v7),
            user.name, 
            user.email, 
            user.login, 
            hashed_password
        )
        
        DatabaseAdapter.insert(CREATE_USER, params)   
        
        return str(new_id_v7)