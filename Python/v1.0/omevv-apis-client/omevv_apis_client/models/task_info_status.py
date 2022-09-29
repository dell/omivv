from enum import Enum


class TaskInfoStatus(str, Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    CANCELED = "CANCELED"

    def __str__(self) -> str:
        return str(self.value)
