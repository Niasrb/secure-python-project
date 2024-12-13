import unittest
from unittest.mock import Mock, patch
from src.secret_management.secret_manager import SecretManager


class TestSecretManager(unittest.TestCase):
    def setUp(self):
        self.manager = SecretManager()

    @patch('hvac.Client')
    def test_secret_storage(self, mock_client):
        # Configure le mock
        mock_vault = Mock()
        mock_client.return_value = mock_vault
        mock_vault.secrets.kv.v2.create_or_update_secret.return_value = True

        # Test le stockage
        result = self.manager.store_secret('test/secret1', {'password': 'test123'})
        self.assertTrue(result)
        mock_vault.secrets.kv.v2.create_or_update_secret.assert_called_once()

    @patch('hvac.Client')
    def test_secret_retrieval(self, mock_client):
        # Configure le mock
        mock_vault = Mock()
        mock_client.return_value = mock_vault
        mock_vault.secrets.kv.v2.read_secret_version.return_value = {
            'data': {'data': {'password': 'test123'}}
        }

        # Test la récupération
        result = self.manager.get_secret('test/secret1')
        self.assertEqual(result, {'password': 'test123'})
        mock_vault.secrets.kv.v2.read_secret_version.assert_called_once()


if __name__ == '__main__':
    unittest.main()