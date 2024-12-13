import hvac
import logging

logger = logging.getLogger(__name__)

class SecretManager:
    def __init__(self):
        self.client = hvac.Client(
            url='http://localhost:8200',
            token='dev-only-token'
        )

    def store_secret(self, path: str, secret: dict) -> bool:
        try:
            self.client.secrets.kv.v2.create_or_update_secret(
                path=path,
                secret={"data": secret}
            )
            logger.info(f"Secret stored at {path}")
            return True
        except Exception as e:
            logger.error(f"Error storing secret: {e}")
            return False

    def get_secret(self, path: str) -> dict:
        try:
            secret = self.client.secrets.kv.v2.read_secret_version(path=path)
            logger.info(f"Secret retrieved from {path}")
            return secret['data']['data']
        except Exception as e:
            logger.error(f"Error retrieving secret: {e}")
            return {}