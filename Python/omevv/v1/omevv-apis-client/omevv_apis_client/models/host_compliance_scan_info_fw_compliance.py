from enum import Enum


class HostComplianceScanInfoFwCompliance(str, Enum):
    COMPLIANT = "COMPLIANT"
    NON_COMPLIANT = "NON-COMPLIANT"
    INCOMPATIBLE = "INCOMPATIBLE"
    UNAVAILABLE = "UNAVAILABLE"

    def __str__(self) -> str:
        return str(self.value)
