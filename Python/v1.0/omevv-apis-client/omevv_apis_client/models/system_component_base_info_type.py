from enum import Enum


class SystemComponentBaseInfoType(str, Enum):
    BIOS = "BIOS"
    PCI_DEVICE = "PCI_DEVICE"
    PCI_SSD_STORAGE = "PCI_SSD_STORAGE"
    NVME_STORAGE = "NVME_STORAGE"
    ATA_STORAGE = "ATA_STORAGE"
    SCSI_STORAGE = "SCSI_STORAGE"
    NVME_SSD = "NVME_SSD"
    LOGICAL_VOLUME = "LOGICAL_VOLUME"
    EXTERNAL = "EXTERNAL"
    OTHER = "OTHER"

    def __str__(self) -> str:
        return str(self.value)
