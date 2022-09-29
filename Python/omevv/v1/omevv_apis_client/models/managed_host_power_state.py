from enum import Enum


class ManagedHostPowerState(str, Enum):
    ON = "ON"
    OFF = "OFF"
    UNKNOWN = "UNKNOWN"
    POWERINGON = "POWERINGON"
    POWERINGOFF = "POWERINGOFF"

    def __str__(self) -> str:
        return str(self.value)
