from enum import Enum


class StorageIdentifierIdentifierType(str, Enum):
    VENDOR_SPECIFIC = "VENDOR_SPECIFIC"
    T10 = "T10"
    EUI64 = "EUI64"
    NAA = "NAA"
    REL_TARGET_PORT = "REL_TARGET_PORT"
    TARGET_PORT_GRP = "TARGET_PORT_GRP"
    LOGICAL_UNIT_GRP = "LOGICAL_UNIT_GRP"
    MD5 = "MD5"
    SNS = "SNS"
    UUID = "UUID"
    SERIAL_NUMBER = "SERIAL_NUMBER"
    OTHER = "OTHER"

    def __str__(self) -> str:
        return str(self.value)
