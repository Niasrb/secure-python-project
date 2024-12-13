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
        logging.basicConfig(
            filename='audit.log',
            level=logging.INFO,
            format='%(asctime)s - %(message)s'
        )

    def scan_directory(self, directory: str):
        """Scan a directory for potential exposed secrets.
        Args:
            directory: Directory path to scan
        Returns:
            list: List of findings
        """
        findings = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(('.py', '.yml', '.json', '.env')):
                    findings.extend(self.scan_file(os.path.join(root, file)))
        return findings

    def scan_file(self, filepath: str):
        """Scan a single file for potential exposed secrets.
        Args:
            filepath: Path to the file to scan
        Returns:
            list: List of findings in this file
        """
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
        except Exception as error:
            logging.error("Error scanning %s: %s", filepath, error)
        return findings
