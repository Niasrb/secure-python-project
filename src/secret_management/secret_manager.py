"""Module for managing secrets using HashiCorp Vault."""
import logging
import hvac


class SecretManager:
    """Class for managing secrets in Vault."""

    def __init__(self):
        """Initialize the SecretManager with Vault client."""
        self.client = hvac.Client(
            url='http://localhost:8200',
            token='dev-only-token'
        )
        self.setup_logging()

    def setup_logging(self):
        """Set up logging configuration."""
<<<<<<< HEAD
        self.logger = logging.getLogger('secret_manager')
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler('secret_access.log')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        self.logger.addHandler(handler)

    def store_secret(self, path: str, secret: dict) -> bool:
        """Store a secret in Vault."""
=======
        logging.basicConfig(
            filename='secret_access.log',
            level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )

    def store_secret(self, path: str, secret: dict) -> bool:
        """Store a secret in Vault.
        Args:
            path: Path where to store the secret
            secret: Dictionary containing the secret data
        Returns:
            bool: True if successful, False otherwise
        """
>>>>>>> b7ce77f71fd99c891142df588f290085e99d0504
        try:
            self.client.secrets.kv.v2.create_or_update_secret(
                path=path,
                secret=secret
            )
<<<<<<< HEAD
            self.logger.info("Secret stored at %s", path)
            return True
        except hvac.exceptions.VaultError as error:
            self.logger.error("Error storing secret: %s", error)
            return False

    def get_secret(self, path: str) -> dict:
        """Retrieve a secret from Vault."""
        try:
            secret = self.client.secrets.kv.v2.read_secret_version(path=path)
            self.logger.info("Secret retrieved from %s", path)
            return secret['data']['data']
        except (hvac.exceptions.VaultError, KeyError) as error:
            self.logger.error("Error retrieving secret: %s", error)
            return None
=======
            logging.info("Secret stored at %s", path)
            return True
        except Exception as error:
            logging.error("Error storing secret: %s", error)
            return False

    def get_secret(self, path: str) -> dict:
        """Retrieve a secret from Vault.
        Args:
            path: Path of the secret to retrieve
        Returns:
            dict: The secret data or None if error
        """
        try:
            secret = self.client.secrets.kv.v2.read_secret_version(path=path)
            logging.info("Secret retrieved from %s", path)
            return secret['data']['data']
        except Exception as error:
            logging.error("Error retrieving secret: %s", error)
            return None
>>>>>>> b7ce77f71fd99c891142df588f290085e99d0504
