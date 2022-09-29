from enum import Enum


class GetAllDiscoveryServiceJobsByTypeJobtype(str, Enum):
    DISCOVERYJOB = "DiscoveryJob"

    def __str__(self) -> str:
        return str(self.value)
