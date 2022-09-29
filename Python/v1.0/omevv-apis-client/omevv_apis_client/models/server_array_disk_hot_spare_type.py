from enum import Enum


class ServerArrayDiskHotSpareType(str, Enum):
    GLOBAL = "Global"
    DEDICATED = "Dedicated"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
