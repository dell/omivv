from enum import Enum


class HostComplianceSnmpTrapStatus(str, Enum):
    CONFIGURED = "CONFIGURED"
    UNCONFIGURED = "UNCONFIGURED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
