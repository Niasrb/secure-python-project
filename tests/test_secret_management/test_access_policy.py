# tests/test_secret_management/test_access_policy.py
import pytest
from src.secret_management.access_policy import PolicyManager, AccessLevel

class TestPolicyManager:
    def setup_method(self):
        self.policy_manager = PolicyManager()

    def test_add_policy(self):
        """Test adding a new policy"""
        self.policy_manager.add_policy(
            user="test_user",
            path="secrets/app1",
            levels=[AccessLevel.READ]
        )
        assert "test_user" in self.policy_manager.policies

    def test_check_access_granted(self):
        """Test access check when access should be granted"""
        self.policy_manager.add_policy(
            user="test_user",
            path="secrets/app1",
            levels=[AccessLevel.READ, AccessLevel.WRITE]
        )
        assert self.policy_manager.check_access(
            user="test_user",
            path="secrets/app1",
            level=AccessLevel.READ
        )

    def test_check_access_denied(self):
        """Test access check when access should be denied"""
        self.policy_manager.add_policy(
            user="test_user",
            path="secrets/app1",
            levels=[AccessLevel.READ]
        )
        assert not self.policy_manager.check_access(
            user="test_user",
            path="secrets/app1",
            level=AccessLevel.ADMIN
        )