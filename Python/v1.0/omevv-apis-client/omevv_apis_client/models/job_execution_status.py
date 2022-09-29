from enum import Enum


class JobExecutionStatus(str, Enum):
    WAITING = "WAITING"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    SUCCESSFUL = "SUCCESSFUL"
    COMPLETED_WITH_ERRORS = "COMPLETED_WITH_ERRORS"
    FAILED = "FAILED"
    CANCELLING = "CANCELLING"
    CANCELLED = "CANCELLED"
    ABORTED = "ABORTED"

    def __str__(self) -> str:
        return str(self.value)
