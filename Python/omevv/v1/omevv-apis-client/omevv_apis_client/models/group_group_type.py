from enum import Enum


class GroupGroupType(str, Enum):
    OMIVV_PLUGIN_GROUP = "OMIVV_PLUGIN_GROUP"
    VCENTER = "VCENTER"
    DATACENTER = "DATACENTER"
    CLUSTER = "CLUSTER"
    CHASSIS = "CHASSIS"
    BAREMETALS = "BAREMETALS"
    DATACENTER_NONCLUSTER = "DATACENTER_NONCLUSTER"

    def __str__(self) -> str:
        return str(self.value)
