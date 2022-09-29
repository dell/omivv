from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.storage_identifier import StorageIdentifier
from ..models.system_component_base_info_type import SystemComponentBaseInfoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LogicalVolumeComponentInfo")


@attr.s(auto_attribs=True)
class LogicalVolumeComponentInfo:
    """
    Attributes:
        name (str): Name of the system HW component Example: system component name.
        id (str):  Example: 9005:0285:9005:02b7.
        type (SystemComponentBaseInfoType): Type of the system HW component Example: PCI DEVICE.
        durable_names (List[StorageIdentifier]):
        backing_physical_drives (List[str]):
        description (Union[Unset, str]): User-friendly description of object type Example: Storage controller.
        part_number (Union[Unset, str]): The part number for this system component. For components listed on VMware VCG,
            this must match the VCG listing. Example: 35VHD.
    """

    name: str
    id: str
    type: SystemComponentBaseInfoType
    durable_names: List[StorageIdentifier]
    backing_physical_drives: List[str]
    description: Union[Unset, str] = UNSET
    part_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        type = self.type.value

        durable_names = []
        for durable_names_item_data in self.durable_names:
            durable_names_item = durable_names_item_data.to_dict()

            durable_names.append(durable_names_item)

        backing_physical_drives = self.backing_physical_drives

        description = self.description
        part_number = self.part_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
                "type": type,
                "durableNames": durable_names,
                "backingPhysicalDrives": backing_physical_drives,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id")

        type = SystemComponentBaseInfoType(d.pop("type"))

        durable_names = []
        _durable_names = d.pop("durableNames")
        for durable_names_item_data in _durable_names:
            durable_names_item = StorageIdentifier.from_dict(durable_names_item_data)

            durable_names.append(durable_names_item)

        backing_physical_drives = cast(List[str], d.pop("backingPhysicalDrives"))

        description = d.pop("description", UNSET)

        part_number = d.pop("partNumber", UNSET)

        logical_volume_component_info = cls(
            name=name,
            id=id,
            type=type,
            durable_names=durable_names,
            backing_physical_drives=backing_physical_drives,
            description=description,
            part_number=part_number,
        )

        logical_volume_component_info.additional_properties = d
        return logical_volume_component_info

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
