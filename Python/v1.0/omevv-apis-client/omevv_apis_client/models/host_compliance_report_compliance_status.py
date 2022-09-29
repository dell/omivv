from enum import Enum


class HostComplianceReportComplianceStatus(str, Enum):
    OK = "OK"
    WARNING = "WARNING"
    DOWNGRADE = "DOWNGRADE"
    CRITICAL = "CRITICAL"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
