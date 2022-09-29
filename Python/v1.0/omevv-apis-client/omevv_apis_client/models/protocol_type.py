from enum import Enum


class ProtocolType(str, Enum):
    CIFS = "CIFS"
    NFS = "NFS"
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    UNAVAILABLE = "UNAVAILABLE"

    def __str__(self) -> str:
        return str(self.value)
