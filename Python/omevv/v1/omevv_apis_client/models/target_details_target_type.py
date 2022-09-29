from enum import Enum


class TargetDetailsTargetType(str, Enum):
    HOST = "Host"
    CHASSIS = "Chassis"
    GROUP = "Group"

    def __str__(self) -> str:
        return str(self.value)
