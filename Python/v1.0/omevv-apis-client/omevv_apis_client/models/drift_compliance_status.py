from enum import Enum


class DriftComplianceStatus(str, Enum):
    COMPLIANT = "Compliant"
    NONCOMPLIANT = "NonCompliant"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
