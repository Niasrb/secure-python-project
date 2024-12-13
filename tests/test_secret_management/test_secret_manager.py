from unittest.mock import patch, Mock, MagicMock
import pytest
from src.secret_management.secret_manager import SecretManager


class TestSecretManager:
    @patch('hvac.Client')
    def test_secret_storage(self, mock_client_class):
        # Configuration du mock
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        # Configuration du mock pour kv.v2
        mock_kv = MagicMock()
        mock_client.secrets.kv.v2 = mock_kv
        mock_kv.create_or_update_secret.return_value = {
            'data': {
                'success': True
            }
        }

        # Création de l'instance avec le mock
        manager = SecretManager()

        # Test
        result = manager.store_secret('test/secret1', {'password': 'test123'})

        # Vérifications
        mock_kv.create_or_update_secret.assert_called_once_with(
            path='test/secret1',
            secret={"data": {'password': 'test123'}}
        )
        assert result == True

    @patch('hvac.Client')
    def test_secret_retrieval(self, mock_client_class):
        # Configuration du mock
        mock_client = MagicMock()
        mock_client_class.return_value = mock_client

        # Configuration du mock pour kv.v2
        mock_kv = MagicMock()
        mock_client.secrets.kv.v2 = mock_kv
        mock_kv.read_secret_version.return_value = {
            'data': {
                'data': {
                    'password': 'test123'
                }
            }
        }

        # Création de l'instance avec le mock
        manager = SecretManager()

        # Test
        result = manager.get_secret('test/secret1')

        # Vérifications
        mock_kv.read_secret_version.assert_called_once_with(
            path='test/secret1'
        )
        assert result == {'password': 'test123'}