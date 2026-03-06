"""
Regras de negócio relacionadas aos CUSTOMERS (clientes do banco).
"""
from models.customer_models import CustomerCreate


class CustomersService:
    """
    Regras de negócio relacionadas aos CUSTOMERS (clientes do banco).
    """

    @staticmethod
    def create_customer(customer: CustomerCreate):

    @staticmethod
    def get_accounts_by_customer(customer_id: int):
        pass

        """
        Cria um novo customer no sistema.
        """
        # TODO: validar dados do customer
        # TODO: persistir customer no banco



    @staticmethod
        def get_customer_by_id(customer_id: int):
            pass

        """
        Busca um customer pelo ID.
        """
        # TODO: buscar customer no banco

