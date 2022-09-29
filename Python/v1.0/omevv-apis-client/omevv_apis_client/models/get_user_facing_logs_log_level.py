from enum import Enum


class GetUserFacingLogsLogLevel(str, Enum):
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    ALL = "ALL"

    def __str__(self) -> str:
        return str(self.value)
