import os
import re
import logging

class SecretAuditor:
    def __init__(self):
        self.setup_logging()
        self.patterns = {
            'api_key': r'api[_-]key["\']:\s*["\'][a-zA-Z0-9]+["\']',
            'password': r'password["\']:\s*["\'][^"\']+["\']',
            'token': r'token["\']:\s*["\'][a-zA-Z0-9_\-]+["\']'
        }

    def setup_logging(self):
        logging.basicConfig(
            filename='audit.log',
            level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )

    def scan_directory(self, directory: str):
        findings = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(('.py', '.yml', '.json', '.env')):
                    findings.extend(self.scan_file(os.path.join(root, file)))
        return findings

    def scan_file(self, filepath: str):
        findings = []
        try:
            with open(filepath, 'r') as f:
                content = f.read()
                for secret_type, pattern in self.patterns.items():
                    matches = re.finditer(pattern, content)
                    for match in matches:
                        findings.append({
                            'file': filepath,
                            'type': secret_type,
                            'line': content.count('\n', 0, match.start()) + 1
                        })
        except Exception as e:
            logging.error(f"Error scanning {filepath}: {e}")
        return findings