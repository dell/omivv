from enum import Enum


class ErrorResponseResponseType(str, Enum):
    BASE_ERROR_RESPONSE = "BASE_ERROR_RESPONSE"

    def __str__(self) -> str:
        return str(self.value)
