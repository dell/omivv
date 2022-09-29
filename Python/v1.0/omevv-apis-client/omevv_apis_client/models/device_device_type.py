from enum import Enum


class DeviceDeviceType(str, Enum):
    DEVICE = "Device"
    HOST = "Host"
    CHASSIS = "Chassis"
    UNKNOWN = "Unknown"

    def __str__(self) -> str:
        return str(self.value)
