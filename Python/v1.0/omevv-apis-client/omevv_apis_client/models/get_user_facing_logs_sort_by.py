from enum import Enum


class GetUserFacingLogsSortBy(str, Enum):
    CREATEDDATE = "CREATEDDATE"
    LEVEL = "LEVEL"
    MESSAGE = "MESSAGE"

    def __str__(self) -> str:
        return str(self.value)
