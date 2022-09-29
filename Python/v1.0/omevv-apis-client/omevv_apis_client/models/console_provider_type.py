from enum import Enum


class ConsoleProviderType(str, Enum):
    WEBCLIENT_PHA = "WEBCLIENT_PHA"
    VLCM = "VLCM"

    def __str__(self) -> str:
        return str(self.value)
