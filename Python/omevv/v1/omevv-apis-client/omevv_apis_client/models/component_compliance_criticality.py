from enum import Enum


class ComponentComplianceCriticality(str, Enum):
    OPTIONAL = "Optional"
    UNKNOWN = "Unknown"
    RECOMMENDED = "Recommended"
    URGENT = "Urgent"
    OK = "Ok"

    def __str__(self) -> str:
        return str(self.value)
