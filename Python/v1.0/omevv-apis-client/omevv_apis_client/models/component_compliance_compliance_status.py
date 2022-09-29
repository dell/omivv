from enum import Enum


class ComponentComplianceComplianceStatus(str, Enum):
    OK = "OK"
    WARNING = "WARNING"
    UPGRADE = "UPGRADE"
    DOWNGRADE = "DOWNGRADE"
    CRITICAL = "CRITICAL"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
