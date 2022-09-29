from enum import Enum


class HostComplianceIdracLicenseStatus(str, Enum):
    SUPPORTED = "SUPPORTED"
    UNSUPPORTED = "UNSUPPORTED"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
