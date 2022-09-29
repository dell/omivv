from enum import Enum


class GetGroupsByConsoleGroupType(str, Enum):
    VCENTER_ROOT = "VCENTER_ROOT"
    DATACENTER = "DATACENTER"
    DATACENTER_NONCLUSTER = "DATACENTER_NONCLUSTER"
    CLUSTER = "CLUSTER"

    def __str__(self) -> str:
        return str(self.value)
