import hvac
import logging

class SecretManager:
    def __init__(self):
        self.client = hvac.Client(
            url='http://localhost:8200',
            token='dev-only-token'
        )
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            filename='secret_access.log',
            level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )

    def store_secret(self, path: str, secret: dict):
        try:
            self.client.secrets.kv.v2.create_or_update_secret(
                path=path,
                secret=secret
            )
            logging.info(f"Secret stored at {path}")
            return True
        except Exception as e:
            logging.error(f"Error storing secret: {e}")
            return False

    def get_secret(self, path: str):
        try:
            secret = self.client.secrets.kv.v2.read_secret_version(path=path)
            logging.info(f"Secret retrieved from {path}")
            return secret['data']['data']
        except Exception as e:
            logging.error(f"Error retrieving secret: {e}")
            return None