from enum import Enum


class GetAllUpdateServiceJobsByTypeJobtype(str, Enum):
    DRIFTJOB = "DriftJob"
    FWUPDATE = "FWUpdate"

    def __str__(self) -> str:
        return str(self.value)
