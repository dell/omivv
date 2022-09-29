from enum import Enum


class ComponentSensorHealthDataComponentHealth(str, Enum):
    UNKNOWN = "UNKNOWN"
    HEALTHY = "HEALTHY"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"

    def __str__(self) -> str:
        return str(self.value)
