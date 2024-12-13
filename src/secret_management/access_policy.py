from enum import Enum
from typing import Dict, List

class AccessLevel(Enum):
    READ = "read"
    WRITE = "write"
    ADMIN = "admin"

class PolicyManager:
    def __init__(self):
        self.policies: Dict[str, Dict[str, List[AccessLevel]]] = {}

    def add_policy(self, user: str, path: str, levels: List[AccessLevel]):
        if user not in self.policies:
            self.policies[user] = {}
        self.policies[user][path] = levels

    def check_access(self, user: str, path: str, level: AccessLevel) -> bool:
        if user not in self.policies:
            return False
        if path not in self.policies[user]:
            return False
        return level in self.policies[user][path]