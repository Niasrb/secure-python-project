"""Module for auditing secret access and usage."""
import os
import re
import logging


class SecretAuditor:
    """Class for auditing secret access and scanning for exposed secrets."""

    def __init__(self):
        """Initialize the SecretAuditor."""
        self.setup_logging()
        self.patterns = {
            'api_key': r'api[_-]key["\']:\s*["\'][a-zA-Z0-9]+["\']',
            'password': r'password["\']:\s*["\'][^"\']+["\']',
            'token': r'token["\']:\s*["\'][a-zA-Z0-9_\-]+["\']'
        }

    def setup_logging(self):
        """Set up logging configuration."""
        self.logger = logging.getLogger('secret_auditor')
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler('audit.log')
        handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
        self.logger.addHandler(handler)

    def scan_directory(self, directory: str):
        """Scan a directory for potential exposed secrets."""
        findings = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(('.py', '.yml', '.json', '.env')):
                    findings.extend(self.scan_file(os.path.join(root, file)))
        return findings

    def scan_file(self, filepath: str):
        """Scan a single file for potential exposed secrets."""
        findings = []
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                for secret_type, pattern in self.patterns.items():
                    matches = re.finditer(pattern, content)
                    for match in matches:
                        findings.append({
                            'file': filepath,
                            'type': secret_type,
                            'line': content.count('\n', 0, match.start()) + 1
                        })
        except (IOError, OSError) as error:
            self.logger.error("Error scanning %s: %s", filepath, error)
        return findings
