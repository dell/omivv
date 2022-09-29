from enum import Enum


class ModifyJobRequestModifyJob(str, Enum):
    MODIFYUPDATEJOB = "ModifyUpdateJob"

    def __str__(self) -> str:
        return str(self.value)
