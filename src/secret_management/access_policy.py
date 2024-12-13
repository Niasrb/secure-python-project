"""Module for managing access policies to secrets."""
from enum import Enum
from typing import Dict, List


class AccessLevel(Enum):
    """Enumeration of possible access levels."""
    READ = "read"
    WRITE = "write"
    ADMIN = "admin"


class PolicyManager:
    """Class for managing access policies to secrets."""

    def __init__(self):
        """Initialize the PolicyManager."""
        self.policies: Dict[str, Dict[str, List[AccessLevel]]] = {}

    def add_policy(self, user: str, path: str, levels: List[AccessLevel]):
        """Add a policy for a user.
        Args:
            user: Username
            path: Path to the secret
            levels: List of access levels
        """
        if user not in self.policies:
            self.policies[user] = {}
        self.policies[user][path] = levels

    def check_access(self, user: str, path: str, level: AccessLevel) -> bool:
        """Check if a user has specific access to a path.
        Args:
            user: Username
            path: Path to check
            level: Required access level
        Returns:
            bool: True if access granted, False otherwise
        """
        if user not in self.policies:
            return False
        if path not in self.policies[user]:
            return False
        return level in self.policies[user][path]
