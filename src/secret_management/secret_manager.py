"""
Module for managing secrets using HashiCorp Vault.
This module provides a secure way to store and retrieve secrets.
"""

import logging
import hvac

logger = logging.getLogger(__name__)


class SecretManager:
    """
    A class to manage secrets using HashiCorp Vault.

    This class provides methods to store and retrieve secrets securely
    using Vault's Key-Value store version 2.
    """

    def __init__(self):
        """Initialize the SecretManager with Vault client configuration."""
        self.client = hvac.Client(
            url='http://localhost:8200',
            token='dev-only-token'
        )

    def store_secret(self, path: str, secret: dict) -> bool:
        """
        Store a secret at the specified path.

        Args:
            path: The path where the secret will be stored
            secret: Dictionary containing the secret data

        Returns:
            bool: True if storage was successful, False otherwise
        """
        try:
            self.client.secrets.kv.v2.create_or_update_secret(
                path=path,
                secret={"data": secret}
            )
            logger.info("Secret stored at %s", path)
            return True
        except Exception as error:  # pylint: disable=broad-except
            logger.error("Error storing secret: %s", error)
            return False

    def get_secret(self, path: str) -> dict:
        """
        Retrieve a secret from the specified path.

        Args:
            path: The path from where to retrieve the secret

        Returns:
            dict: The secret data if successful, empty dict otherwise
        """
        try:
            secret = self.client.secrets.kv.v2.read_secret_version(path=path)
            logger.info("Secret retrieved from %s", path)
            return secret['data']['data']
        except Exception as error:  # pylint: disable=broad-except
            logger.error("Error retrieving secret: %s", error)
            return {}
