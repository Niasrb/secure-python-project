import pytest
import os
from src.secret_management.audit import SecretAuditor

class TestSecretAuditor:
    def setup_method(self):
        self.auditor = SecretAuditor()
        self.test_dir = "test_files"
        os.makedirs(self.test_dir, exist_ok=True)

    def teardown_method(self):
        """Clean up test files"""
        if os.path.exists(self.test_dir):  # Vérifier si le dossier existe
            for file in os.listdir(self.test_dir):
                os.remove(os.path.join(self.test_dir, file))
            os.rmdir(self.test_dir)

    def test_scan_file_with_secrets(self):
        """Test scanning a file containing secrets"""
        test_file = os.path.join(self.test_dir, "test.py")
        with open(test_file, "w") as f:
            f.write('{"api_key": "secret123"}\n')  # Format JSON
            f.write('{"password": "test_pass"}\n')  # Format JSON

        findings = self.auditor.scan_file(test_file)
        assert len(findings) == 2
        assert findings[0]["type"] in ["api_key", "password"]

    def test_scan_directory(self):
        """Test scanning an entire directory"""
        # Create test files
        test_file1 = os.path.join(self.test_dir, "config.json")
        with open(test_file1, "w") as f:
            f.write('{"token": "abc123"}')  # Format JSON

        findings = self.auditor.scan_directory(self.test_dir)
        assert len(findings) > 0