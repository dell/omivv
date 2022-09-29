from enum import Enum


class EntityType(str, Enum):
    CONSOLEROOT = "ConsoleRoot"
    CONSOLEDATACENTER = "ConsoleDatacenter"
    CONSOLECLUSTER = "ConsoleCluster"
    CONSOLEFOLDER = "ConsoleFolder"
    CONSOLEHOST = "ConsoleHost"

    def __str__(self) -> str:
        return str(self.value)
