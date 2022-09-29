from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.storage_identifier import StorageIdentifier
from ..models.system_component_base_info_type import SystemComponentBaseInfoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ScsiStorageComponentInfo")


@attr.s(auto_attribs=True)
class ScsiStorageComponentInfo:
    """
    Attributes:
        name (str): Name of the system HW component Example: system component name.
        id (str):  Example: 9005:0285:9005:02b7.
        type (SystemComponentBaseInfoType): Type of the system HW component Example: PCI DEVICE.
        device_type (str): 2 hex digit PERIPHERAL DEVICE TYPE
        vendor (str): 8 ASCII character T10 VENDOR IDENTIFIACATION Example: SEAGATE.
        product (str): 16 ASCII character T10 PRODUCT IDENTIFICATION Example: Frobozz magic drive.
        description (Union[Unset, str]): User-friendly description of object type Example: Storage controller.
        part_number (Union[Unset, str]): The part number for this system component. For components listed on VMware VCG,
            this must match the VCG listing. Example: 35VHD.
        disk_ids (Union[Unset, List[str]]): List device IDs from VPD page Example: ['naa.23434e78f98d7097b98c134',
            't10.34233462099874'].
        durable_names (Union[Unset, List[StorageIdentifier]]):
    """

    name: str
    id: str
    type: SystemComponentBaseInfoType
    device_type: str
    vendor: str
    product: str
    description: Union[Unset, str] = UNSET
    part_number: Union[Unset, str] = UNSET
    disk_ids: Union[Unset, List[str]] = UNSET
    durable_names: Union[Unset, List[StorageIdentifier]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        type = self.type.value

        device_type = self.device_type
        vendor = self.vendor
        product = self.product
        description = self.description
        part_number = self.part_number
        disk_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.disk_ids, Unset):
            disk_ids = self.disk_ids

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
                "deviceType": device_type,
                "vendor": vendor,
                "product": product,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if disk_ids is not UNSET:
            field_dict["diskIds"] = disk_ids
        if durable_names is not UNSET:
            field_dict["durableNames"] = durable_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id")

        type = SystemComponentBaseInfoType(d.pop("type"))

        device_type = d.pop("deviceType")

        vendor = d.pop("vendor")

        product = d.pop("product")

        description = d.pop("description", UNSET)

        part_number = d.pop("partNumber", UNSET)

        disk_ids = cast(List[str], d.pop("diskIds", UNSET))

        durable_names = []
        _durable_names = d.pop("durableNames", UNSET)
        for durable_names_item_data in _durable_names or []:
            durable_names_item = StorageIdentifier.from_dict(durable_names_item_data)

            durable_names.append(durable_names_item)

        scsi_storage_component_info = cls(
            name=name,
            id=id,
            type=type,
            device_type=device_type,
            vendor=vendor,
            product=product,
            description=description,
            part_number=part_number,
            disk_ids=disk_ids,
            durable_names=durable_names,
        )

        scsi_storage_component_info.additional_properties = d
        return scsi_storage_component_info

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
