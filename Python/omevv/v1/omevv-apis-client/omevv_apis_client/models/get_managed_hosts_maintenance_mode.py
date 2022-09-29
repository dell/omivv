from enum import Enum


class GetManagedHostsMaintenanceMode(str, Enum):
    INSIDE_MAINTENANCEMODE = "INSIDE_MAINTENANCEMODE"
    OUTSIDE_MAINTENANCEMODE = "OUTSIDE_MAINTENANCEMODE"

    def __str__(self) -> str:
        return str(self.value)
