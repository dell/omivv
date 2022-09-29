from enum import Enum


class UserFacingLogLevel(str, Enum):
    INFO = "INFO"
    ERROR = "ERROR"
    WARN = "WARN"
    DEBUG = "DEBUG"

    def __str__(self) -> str:
        return str(self.value)
