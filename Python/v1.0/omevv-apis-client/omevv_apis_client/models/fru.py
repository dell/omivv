from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Fru")


@attr.s(auto_attribs=True)
class Fru:
    """
    Attributes:
        id (Union[Unset, int]):
        manufacturer (Union[Unset, str]): displays the name of the manufacturer.
        name (Union[Unset, str]): displays the FRU part name.
        part_number (Union[Unset, str]): displays the FRU part number.
        serial_number (Union[Unset, str]): displays the serial number of the manufacturer.
    """

    id: Union[Unset, int] = UNSET
    manufacturer: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    part_number: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        manufacturer = self.manufacturer
        name = self.name
        part_number = self.part_number
        serial_number = self.serial_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if name is not UNSET:
            field_dict["name"] = name
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        name = d.pop("name", UNSET)

        part_number = d.pop("partNumber", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        fru = cls(
            id=id,
            manufacturer=manufacturer,
            name=name,
            part_number=part_number,
            serial_number=serial_number,
        )

        fru.additional_properties = d
        return fru

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
