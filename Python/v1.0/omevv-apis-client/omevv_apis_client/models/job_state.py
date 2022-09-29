from enum import Enum


class JobState(str, Enum):
    SCHEDULED = "SCHEDULED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    CANCELLING = "CANCELLING"
    ABORTED = "ABORTED"

    def __str__(self) -> str:
        return str(self.value)
