from enum import Enum


class FirmwareUpdateRequestRebootOptions(str, Enum):
    FORCEREBOOT = "FORCEREBOOT"
    SAFEREBOOT = "SAFEREBOOT"
    NEXTREBOOT = "NEXTREBOOT"

    def __str__(self) -> str:
        return str(self.value)
