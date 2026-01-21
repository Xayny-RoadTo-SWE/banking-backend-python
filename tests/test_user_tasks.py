from unittest import TestCase
from tasks.user_tasks import UserTasks

class TestUserTasks(TestCase):
    def test_valid_role(self) -> None:
        nome = "doe"
        role = "Gerente"
        self.assertIsNone(UserTasks.validate_user(nome, role))

    def test_invalid_role(self) -> None:
        role = "gerenteee_invalid"
        with self.assertRaises(Exception) as cm:
            UserTasks.validate_user("doe", role)
        self.assertIn("Role not found", str(cm.exception))

    def test_empty_role(self) -> None:
        role = ""
        with self.assertRaises(Exception) as cm:
            UserTasks.validate_user("doe", role)
        self.assertIn("Role not found", str(cm.exception))

    def test_none_role(self) -> None:
        role = None
        with self.assertRaises(Exception) as cm:
            UserTasks.validate_user("doe", role)
        self.assertIn("Role not found", str(cm.exception))

    def test_case_sensitive_role(self) -> None:
        # Assuming RolesEnum is case-sensitive and "gerente" is invalid
        role = "gerente"
        with self.assertRaises(Exception) as cm:
            UserTasks.validate_user("doe", role)
        self.assertIn("Role not found", str(cm.exception))

    def test_valid_role_with_spaces(self) -> None:
        # Assuming "Gerente" is valid, but " Gerente " is not
        role = " Gerente "
        with self.assertRaises(Exception) as cm:
            UserTasks.validate_user("doe", role)
        self.assertIn("Role not found", str(cm.exception))