import uuid6
from database import DatabaseAdapter
from repositories.repo_queries import CREATE_CUSTOMER, GET_CUSTOMER_BY_ID
from models.customer_models import CustomerCreateRequest

class CustomersRepository:

    @staticmethod
    def create_customer(customer: CustomerCreateRequest) -> str:
        new_id_v7 = uuid6.uuid7()
        
        params = (
            str(new_id_v7), 
            customer.full_name,
            customer.birth_date,
            customer.document_type,
            customer.document_number,
            customer.manager_id
        )
        
        DatabaseAdapter.insert(CREATE_CUSTOMER, GET_CUSTOMER_BY_ID, params)
        
        return str(new_id_v7)

    @staticmethod
    def get_customer_by_id(customer_id: str):
        return DatabaseAdapter.fetchone(
            GET_CUSTOMER_BY_ID,
            (customer_id,)
        )
