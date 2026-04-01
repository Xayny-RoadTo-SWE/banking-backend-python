from unittest import TestCase
from tasks.user_tasks import UserTasks
from models.user_models import UserCreateRequest, ValidDocumentType
from unittest.mock import patch


class TestUserTasks(TestCase):
    def test_valid_role(self) -> None:
        user = UserCreateRequest(
        nome = "doe",
        role = "Gerente",
        document_type=ValidDocumentType.CPF,
        document_number="123.456.789-09"
        )
        self.assertIsNone(UserTasks.validate_user(user))

    def test_invalid_role(self) -> None:
        user = UserCreateRequest(
        nome = "doe",
        role = "gerenteee_invalid",
        document_type=ValidDocumentType.CPF,
        document_number="123.456.789-09"
        )
        with self.assertRaises(Exception) as cm:
            UserTasks.validate_user(user)

        self.assertIn("Role not found", str(cm.exception))

    def test_empty_role(self) -> None:
        user = UserCreateRequest(
            nome="doe",
            role="",  # role vazio (o que estamos testando)
            document_type=ValidDocumentType.CPF,
            document_number="123.456.789-09"  # CPF válido
        )

        with self.assertRaises(Exception) as cm:
            UserTasks.validate_user(user)

        self.assertIn("Role not found", str(cm.exception))

    def test_case_sensitive_role(self) -> None:
        # RolesEnum é case-sensitive e "gerente" é inválido
        user = UserCreateRequest(
            nome="doe",
            role="gerente",  # inválido
            document_type=ValidDocumentType.CPF,
            document_number="52998224725"
        )

        with self.assertRaises(Exception) as cm:
            UserTasks.validate_user(user)

        self.assertIn("Role not found", str(cm.exception))

    def test_valid_role_with_spaces(self) -> None:
        # "Gerente" é válido, mas com espaços não
        user = UserCreateRequest(
            nome="doe",
            role=" Gerente ",  # inválido por espaços
            document_type=ValidDocumentType.CPF,
            document_number="52998224725"
        )

        with self.assertRaises(Exception) as cm:
            UserTasks.validate_user(user)

        self.assertIn("Role not found", str(cm.exception))

    def test_valid_document_type(self) -> None:
      user = UserCreateRequest(
          nome ="doe",
          role="Gerente",
          document_type=ValidDocumentType.CPF,
          document_number="123.456.789-09"
        )
      result = UserTasks.validate_user(user)
      self.assertIsNone(result)

    def test_invalid_document_type(self) -> None:
        user = UserCreateRequest(
            nome ="doe",
            role="Gerente",
            document_type="RG",
            document_number="123.456.789-09"
            )
        with self.assertRaises(Exception) as cm:
            UserTasks.validate_user(user)
        self.assertIn("Document Type not valid", str(cm.exception))


    def test_valid_cpf_number(self) -> None:
        user = UserCreateRequest(
            nome ="doe",
            role="Gerente",
            document_type=ValidDocumentType.CPF,
            document_number="123.456.789-09"
            )
        result = UserTasks.validate_user(user)
        self.assertIsNone(result)

    def test_invalid_cpf_number_format(self) -> None:
        user = UserCreateRequest(
            nome ="doe",
            role="Gerente",
            document_type=ValidDocumentType.CPF,
            document_number="123ABC45678"
            )
        with self.assertRaises(Exception) as cm:
            UserTasks.validate_user(user)
        self.assertIn("Cpf", str(cm.exception))

    def test_invalid_document_length(self) -> None:
        user = UserCreateRequest(
            nome ="doe",
            role="Gerente",
            document_type=ValidDocumentType.CPF,
            document_number="123.456.78-90"
            )
        with self.assertRaises(Exception) as cm:
            UserTasks.validate_user(user)
        self.assertIn("Cpf", str(cm.exception)
        )

    def test_invalid_cpf_repeated_digits(self) -> None:
        user = UserCreateRequest(
            nome ="doe",
            role="Gerente",
            document_type=ValidDocumentType.CPF,
            document_number="111.111.111-11"
            )
        with self.assertRaises(Exception) as cm:
            UserTasks.validate_user(user)
        self.assertIn("Cpf", str(cm.exception))

    def test_invalid_cpf_checksum(self) -> None:
        user = UserCreateRequest(
            nome ="doe",
            role="Gerente",
            document_type=ValidDocumentType.CPF,
            document_number="123.456.789-00"
            )
        with self.assertRaises(Exception) as cm:
            UserTasks.validate_user(user)
        self.assertIn("Cpf", str(cm.exception))

    def test_create_user_calls_validation(self) -> None:
        user = UserCreateRequest(
            nome ="doe",
            role="Gerente",
            document_type=ValidDocumentType.CPF,
            document_number="123.456.789-09"
            )
        with patch("tasks.user_tasks.UsersRepository.create_user") as mock_create:
            UserTasks.create_user(user)

            mock_create.assert_called_once_with(user)