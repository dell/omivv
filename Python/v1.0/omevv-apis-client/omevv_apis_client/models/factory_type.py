from enum import Enum


class FactoryType(str, Enum):
    DEFAULT = "Default"
    CUSTOM = "Custom"

    def __str__(self) -> str:
        return str(self.value)
