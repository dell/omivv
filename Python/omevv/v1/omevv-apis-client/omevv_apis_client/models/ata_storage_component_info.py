from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.storage_identifier import StorageIdentifier
from ..models.system_component_base_info_type import SystemComponentBaseInfoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AtaStorageComponentInfo")


@attr.s(auto_attribs=True)
class AtaStorageComponentInfo:
    """
    Attributes:
        name (str): Name of the system HW component Example: system component name.
        id (str):  Example: 9005:0285:9005:02b7.
        type (SystemComponentBaseInfoType): Type of the system HW component Example: PCI DEVICE.
        model (str): 2-hex digit class code Example: ST3600057SS.
        serial_number (str): disk serial number string Example: 3SL1DBA00.
        description (Union[Unset, str]): User-friendly description of object type Example: Storage controller.
        part_number (Union[Unset, str]): The part number for this system component. For components listed on VMware VCG,
            this must match the VCG listing. Example: 35VHD.
        durable_names (Union[Unset, List[StorageIdentifier]]):
    """

    name: str
    id: str
    type: SystemComponentBaseInfoType
    model: str
    serial_number: str
    description: Union[Unset, str] = UNSET
    part_number: Union[Unset, str] = UNSET
    durable_names: Union[Unset, List[StorageIdentifier]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        type = self.type.value

        model = self.model
        serial_number = self.serial_number
        description = self.description
        part_number = self.part_number
        durable_names: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.durable_names, Unset):
            durable_names = []
            for durable_names_item_data in self.durable_names:
                durable_names_item = durable_names_item_data.to_dict()

                durable_names.append(durable_names_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
                "type": type,
                "model": model,
                "serialNumber": serial_number,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if durable_names is not UNSET:
            field_dict["durableNames"] = durable_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id")

        type = SystemComponentBaseInfoType(d.pop("type"))

        model = d.pop("model")

        serial_number = d.pop("serialNumber")

        description = d.pop("description", UNSET)

        part_number = d.pop("partNumber", UNSET)

        durable_names = []
        _durable_names = d.pop("durableNames", UNSET)
        for durable_names_item_data in _durable_names or []:
            durable_names_item = StorageIdentifier.from_dict(durable_names_item_data)

            durable_names.append(durable_names_item)

        ata_storage_component_info = cls(
            name=name,
            id=id,
            type=type,
            model=model,
            serial_number=serial_number,
            description=description,
            part_number=part_number,
            durable_names=durable_names,
        )

        ata_storage_component_info.additional_properties = d
        return ata_storage_component_info

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
