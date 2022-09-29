from enum import Enum


class RepositoryProfileStatus(str, Enum):
    PARSING = "Parsing"
    SUCCESS = "Success"
    FAILED = "Failed"
    UNAVAILABLE = "Unavailable"

    def __str__(self) -> str:
        return str(self.value)
