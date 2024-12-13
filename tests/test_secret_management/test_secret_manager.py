import unittest
import sys
import os

# Ajouter ces lignes au début du fichier
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.secret_management.secret_manager import SecretManager
from src.secret_management.access_policy import PolicyManager, AccessLevel


class TestSecretManager(unittest.TestCase):
    def setUp(self):
        self.secret_manager = SecretManager()
        self.policy_manager = PolicyManager()

    def test_secret_storage(self):
        # Test storing and retrieving a secret
        test_secret = {'password': 'test123'}
        path = 'test/secret1'

        # Store secret
        result = self.secret_manager.store_secret(path, test_secret)
        self.assertTrue(result)

        # Retrieve secret
        retrieved = self.secret_manager.get_secret(path)
        self.assertEqual(retrieved['password'], 'test123')


class TestPolicyManager(unittest.TestCase):
    def setUp(self):
        self.policy_manager = PolicyManager()

    def test_policy_enforcement(self):
        # Test policy enforcement
        self.policy_manager.add_policy(
            'test_user',
            'test/secret1',
            [AccessLevel.READ]
        )

        # Check access
        self.assertTrue(
            self.policy_manager.check_access(
                'test_user',
                'test/secret1',
                AccessLevel.READ
            )
        )


if __name__ == '__main__':
    unittest.main()
