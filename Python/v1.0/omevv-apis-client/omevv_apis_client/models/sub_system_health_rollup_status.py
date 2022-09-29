from enum import Enum


class SubSystemHealthRollupStatus(str, Enum):
    UNKNOWN = "UNKNOWN"
    HEALTHY = "HEALTHY"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"

    def __str__(self) -> str:
        return str(self.value)
