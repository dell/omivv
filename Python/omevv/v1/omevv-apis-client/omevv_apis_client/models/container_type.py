from enum import Enum


class ContainerType(str, Enum):
    ROOT = "ROOT"
    DATACENTER = "DATACENTER"
    CLUSTER = "CLUSTER"
    FOLDER = "FOLDER"

    def __str__(self) -> str:
        return str(self.value)
