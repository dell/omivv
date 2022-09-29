from enum import Enum


class HostComplianceScanInfoFwStageStatus(str, Enum):
    STAGED = "STAGED"
    NOT_STAGED = "NOT-STAGED"

    def __str__(self) -> str:
        return str(self.value)
