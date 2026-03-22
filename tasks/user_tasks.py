from repositories.users_repo import UsersRepository
#from models.user_models import RolesEnum, UserCreateRequest, ValidDocumentType
import re

class UserTasks:
    
    """
    @staticmethod
    def __validate_roles(role: str) -> None:
        try:
            RolesEnum(role)
            return
        except:
            raise Exception(f"Role not found {role}")
    
    """
    """
    @staticmethod
    def __validate_document_type(document_type: str) -> None:
        if ValidDocumentType(document_type):
            return None
        raise Exception(f"Document Type not valid {document_type}")
    """
    @staticmethod
    def validate_cpf_number(cpf: str) -> None:
        pattern = r'^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$'
        if not re.match(pattern, cpf):
            raise Exception(f"Cpf {cpf} is invalid format")

        numbers = [int(d) for d in re.sub(r'\D', '', cpf)]

        if len(numbers) != 11 or len(set(numbers)) == 1:
            raise Exception(f"Cpf {cpf} is invalid")

        sum1 = sum([numbers[i] * (10 - i) for i in range(9)])
        digit1 = ((sum1 * 10) % 11) % 10
        if numbers[9] != digit1:
            raise Exception(f"Cpf {cpf} is invalid")

        sum2 = sum([numbers[i] * (11 - i) for i in range(10)])
        digit2 = ((sum2 * 10) % 11) % 10
        if numbers[10] != digit2:
            raise Exception(f"Cpf {cpf} is invalid")

        return None

"""
    @classmethod
    def validate_document_number(cls, document_type: str, document_number: str) -> None:
        document_type_functions = {
            ValidDocumentType.CPF: cls.validate_cpf_number,
        }
        if func_valid := document_type_functions.get(document_type, None ):
            func_valid(document_number)
        else:
            raise Exception(f"Unknown document type {document_type}")
"""

"""
    @classmethod
    def validate_user(cls, user: UserCreateRequest) -> None:
        cls.__validate_roles(user.role)
        cls.__validate_document_type(user.document_type)
        cls.validate_document_number(user.document_type, user.document_number)


    @staticmethod
    def create_user(user: UserCreateRequest) -> None:
        UsersRepository.create_user(user)
        """