from enum import Enum


class HostComplianceConnectionState(str, Enum):
    UNKNOWN = "UNKNOWN"
    DISCONNECTED = "DISCONNECTED"
    CONNECTED = "CONNECTED"

    def __str__(self) -> str:
        return str(self.value)
