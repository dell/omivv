from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupDeviceStorageDetails")


@attr.s(auto_attribs=True)
class GroupDeviceStorageDetails:
    """
    Attributes:
        host (Union[Unset, str]):
        service_tag (Union[Unset, str]):
        physical_disks (Union[Unset, Any]):
        controllers (Union[Unset, Any]):
    """

    host: Union[Unset, str] = UNSET
    service_tag: Union[Unset, str] = UNSET
    physical_disks: Union[Unset, Any] = UNSET
    controllers: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host = self.host
        service_tag = self.service_tag
        physical_disks = self.physical_disks
        controllers = self.controllers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if service_tag is not UNSET:
            field_dict["serviceTag"] = service_tag
        if physical_disks is not UNSET:
            field_dict["physicalDisks"] = physical_disks
        if controllers is not UNSET:
            field_dict["controllers"] = controllers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host = d.pop("host", UNSET)

        service_tag = d.pop("serviceTag", UNSET)

        physical_disks = d.pop("physicalDisks", UNSET)

        controllers = d.pop("controllers", UNSET)

        group_device_storage_details = cls(
            host=host,
            service_tag=service_tag,
            physical_disks=physical_disks,
            controllers=controllers,
        )

        group_device_storage_details.additional_properties = d
        return group_device_storage_details

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
