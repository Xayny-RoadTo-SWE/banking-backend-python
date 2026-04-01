from models.customer_models import CustomerCreateRequest


class CustomersService:
    """
    Regras de negócio relacionadas aos CUSTOMERS (clientes do banco).
    """

    @staticmethod
    def create_customer(customer: CustomerCreateRequest):
    def create_customer(customer: CustomerCreate):
        """
        Cria um novo customer no sistema.
        """
        # TODO: validar dados do customer
        # TODO: persistir customer no banco
        pass

    @staticmethod
    def get_accounts_by_customer(customer_id: int):
        pass



    @staticmethod
    def get_customer_by_id(customer_id: int):

    @staticmethod
    def get_accounts_by_customer(customer_id: int):
        pass

    @staticmethod
    def get_customer_by_id(customer_id: int):
        """
        Busca um customer pelo ID.
        """
        # TODO: buscar customer no banco
        pass

