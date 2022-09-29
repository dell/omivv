from enum import Enum


class HostComplianceState(str, Enum):
    UNKNOWN = "UNKNOWN"
    UNDISCOVERED = "UNDISCOVERED"
    NONCOMPLIANT = "NONCOMPLIANT"
    COMPLIANT = "COMPLIANT"
    UNSUPPORTED = "UNSUPPORTED"
    MANAGEDWITHOUTALERTS = "MANAGEDWITHOUTALERTS"
    MANAGED = "MANAGED"

    def __str__(self) -> str:
        return str(self.value)
