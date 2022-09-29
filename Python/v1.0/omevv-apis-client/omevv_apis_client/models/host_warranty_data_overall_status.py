from enum import Enum


class HostWarrantyDataOverallStatus(str, Enum):
    WARNING = "WARNING"
    EXPIRED = "EXPIRED"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
