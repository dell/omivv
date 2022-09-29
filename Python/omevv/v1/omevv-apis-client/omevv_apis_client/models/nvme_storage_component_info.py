from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.storage_identifier import StorageIdentifier
from ..models.system_component_base_info_type import SystemComponentBaseInfoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NvmeStorageComponentInfo")


@attr.s(auto_attribs=True)
class NvmeStorageComponentInfo:
    """
    Attributes:
        name (str): Name of the system HW component Example: system component name.
        id (str):  Example: 9005:0285:9005:02b7.
        type (SystemComponentBaseInfoType): Type of the system HW component Example: PCI DEVICE.
        vendor (str): IEEE OUI Identifier for drive vendor Example: Intel.
        model (str): 40-character (ASCII) model number (MN) string from "Identify" command Example: SSDPE2KX020T8L.
        durable_names (List[StorageIdentifier]):
        description (Union[Unset, str]): User-friendly description of object type Example: Storage controller.
        part_number (Union[Unset, str]): The part number for this system component. For components listed on VMware VCG,
            this must match the VCG listing. Example: 35VHD.
    """

    name: str
    id: str
    type: SystemComponentBaseInfoType
    vendor: str
    model: str
    durable_names: List[StorageIdentifier]
    description: Union[Unset, str] = UNSET
    part_number: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        type = self.type.value

        vendor = self.vendor
        model = self.model
        durable_names = []
        for durable_names_item_data in self.durable_names:
            durable_names_item = durable_names_item_data.to_dict()

            durable_names.append(durable_names_item)

        description = self.description
        part_number = self.part_number

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "id": id,
                "type": type,
                "vendor": vendor,
                "model": model,
                "durableNames": durable_names,
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

        vendor = d.pop("vendor")

        model = d.pop("model")

        durable_names = []
        _durable_names = d.pop("durableNames")
        for durable_names_item_data in _durable_names:
            durable_names_item = StorageIdentifier.from_dict(durable_names_item_data)

            durable_names.append(durable_names_item)

        description = d.pop("description", UNSET)

        part_number = d.pop("partNumber", UNSET)

        nvme_storage_component_info = cls(
            name=name,
            id=id,
            type=type,
            vendor=vendor,
            model=model,
            durable_names=durable_names,
            description=description,
            part_number=part_number,
        )

        nvme_storage_component_info.additional_properties = d
        return nvme_storage_component_info

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
