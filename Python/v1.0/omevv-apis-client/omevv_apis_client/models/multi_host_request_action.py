from enum import Enum


class MultiHostRequestAction(str, Enum):
    SCAN = "SCAN"

    def __str__(self) -> str:
        return str(self.value)
