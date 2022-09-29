from enum import Enum


class TaskInfoAction(str, Enum):
    GET_HOST_INVENTORY = "GET_HOST_INVENTORY"
    SCAN = "SCAN"
    STAGE_UPDATE = "STAGE_UPDATE"
    UPDATE_PRE_CHECK = "UPDATE_PRE_CHECK"
    PRE_IMAGE_UPDATE = "PRE_IMAGE_UPDATE"
    POST_IMAGE_UPDATE = "POST_IMAGE_UPDATE"

    def __str__(self) -> str:
        return str(self.value)
