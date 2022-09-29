from enum import Enum


class ComponentComplianceUpdateAction(str, Enum):
    EQUAL = "EQUAL"
    DOWNGRADE = "DOWNGRADE"
    UPGRADE = "UPGRADE"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
