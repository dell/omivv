from enum import Enum


class JobJobType(str, Enum):
    DRIFTJOB = "DriftJob"
    FWUPDATE = "FWUpdate"
    DISCOVERYJOB = "DiscoveryJob"

    def __str__(self) -> str:
        return str(self.value)
