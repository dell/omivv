from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.system_component_base_info_type import SystemComponentBaseInfoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemComponentBaseInfo")


@attr.s(auto_attribs=True)
class SystemComponentBaseInfo:
    """
    Attributes:
        name (str): Name of the system HW component Example: system component name.
        id (str):  Example: 9005:0285:9005:02b7.
        type (SystemComponentBaseInfoType): Type of the system HW component Example: PCI DEVICE.
        description (Union[Unset, str]): User-friendly description of object type Example: Storage controller.
        part_number (Union[Unset, str]): The part number for this system component. For components listed on VMware VCG,
            this must match the VCG listing. Example: 35VHD.
    """

    name: str
    id: str
    type: SystemComponentBaseInfoType
    description: Union[Unset, str] = UNSET
    part_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        type = self.type.value

        description = self.description
        part_number = self.part_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
                "type": type,
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

        description = d.pop("description", UNSET)

        part_number = d.pop("partNumber", UNSET)

        system_component_base_info = cls(
            name=name,
            id=id,
            type=type,
            description=description,
            part_number=part_number,
        )

        system_component_base_info.additional_properties = d
        return system_component_base_info

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
