from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.device_device_type import DeviceDeviceType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Device")


@attr.s(auto_attribs=True)
class Device:
    """
    Attributes:
        id (Union[Unset, int]):
        device_type (Union[Unset, DeviceDeviceType]):
    """

    id: Union[Unset, int] = UNSET
    device_type: Union[Unset, DeviceDeviceType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        device_type: Union[Unset, str] = UNSET
        if not isinstance(self.device_type, Unset):
            device_type = self.device_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _device_type = d.pop("deviceType", UNSET)
        device_type: Union[Unset, DeviceDeviceType]
        if isinstance(_device_type, Unset):
            device_type = UNSET
        else:
            device_type = DeviceDeviceType(_device_type)

        device = cls(
            id=id,
            device_type=device_type,
        )

        device.additional_properties = d
        return device

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
