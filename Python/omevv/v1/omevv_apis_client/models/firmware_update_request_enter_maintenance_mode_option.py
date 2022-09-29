from enum import Enum


class FirmwareUpdateRequestEnterMaintenanceModeOption(str, Enum):
    FULL_DATA_MIGRATION = "FULL_DATA_MIGRATION"
    ENSURE_ACCESSIBILITY = "ENSURE_ACCESSIBILITY"
    NO_DATA_MIGRATION = "NO_DATA_MIGRATION"

    def __str__(self) -> str:
        return str(self.value)
