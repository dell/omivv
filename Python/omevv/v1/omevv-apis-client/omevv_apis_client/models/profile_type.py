from enum import Enum


class ProfileType(str, Enum):
    FIRMWARE = "Firmware"
    DRIVER = "Driver"

    def __str__(self) -> str:
        return str(self.value)
