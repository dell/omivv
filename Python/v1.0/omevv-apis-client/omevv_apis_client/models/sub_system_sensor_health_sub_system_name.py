from enum import Enum


class SubSystemSensorHealthSubSystemName(str, Enum):
    CURRENT = "CURRENT"
    VOLTAGE = "VOLTAGE"
    INTRUSION = "INTRUSION"
    POWER_SUPPLY = "POWER_SUPPLY"
    PROCESSOR = "PROCESSOR"
    MEMORY = "MEMORY"
    TEMPERATURE = "TEMPERATURE"
    FAN = "FAN"
    BATTERY = "BATTERY"
    STORAGE = "STORAGE"
    IDSDM = "IDSDM"

    def __str__(self) -> str:
        return str(self.value)
