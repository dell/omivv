from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.firmware import Firmware
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupDeviceFirmwareDetails")


@attr.s(auto_attribs=True)
class GroupDeviceFirmwareDetails:
    """
    Attributes:
        host (Union[Unset, str]):
        service_tag (Union[Unset, str]):
        firmware (Union[Unset, Firmware]):
    """

    host: Union[Unset, str] = UNSET
    service_tag: Union[Unset, str] = UNSET
    firmware: Union[Unset, Firmware] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host = self.host
        service_tag = self.service_tag
        firmware: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.firmware, Unset):
            firmware = self.firmware.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if service_tag is not UNSET:
            field_dict["serviceTag"] = service_tag
        if firmware is not UNSET:
            field_dict["firmware"] = firmware

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host = d.pop("host", UNSET)

        service_tag = d.pop("serviceTag", UNSET)

        _firmware = d.pop("firmware", UNSET)
        firmware: Union[Unset, Firmware]
        if isinstance(_firmware, Unset):
            firmware = UNSET
        else:
            firmware = Firmware.from_dict(_firmware)

        group_device_firmware_details = cls(
            host=host,
            service_tag=service_tag,
            firmware=firmware,
        )

        group_device_firmware_details.additional_properties = d
        return group_device_firmware_details

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
