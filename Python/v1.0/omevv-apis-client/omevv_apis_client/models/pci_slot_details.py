from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PCISlotDetails")


@attr.s(auto_attribs=True)
class PCISlotDetails:
    """
    Attributes:
        slot_number (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        description (Union[Unset, str]):
        slot_type (Union[Unset, str]):
        databus_width (Union[Unset, str]):
    """

    slot_number: Union[Unset, str] = UNSET
    manufacturer: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    slot_type: Union[Unset, str] = UNSET
    databus_width: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        slot_number = self.slot_number
        manufacturer = self.manufacturer
        description = self.description
        slot_type = self.slot_type
        databus_width = self.databus_width

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if slot_number is not UNSET:
            field_dict["slotNumber"] = slot_number
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if description is not UNSET:
            field_dict["description"] = description
        if slot_type is not UNSET:
            field_dict["slotType"] = slot_type
        if databus_width is not UNSET:
            field_dict["databusWidth"] = databus_width

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        slot_number = d.pop("slotNumber", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        description = d.pop("description", UNSET)

        slot_type = d.pop("slotType", UNSET)

        databus_width = d.pop("databusWidth", UNSET)

        pci_slot_details = cls(
            slot_number=slot_number,
            manufacturer=manufacturer,
            description=description,
            slot_type=slot_type,
            databus_width=databus_width,
        )

        pci_slot_details.additional_properties = d
        return pci_slot_details

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
