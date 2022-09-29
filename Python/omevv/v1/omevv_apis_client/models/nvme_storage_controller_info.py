from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.storage_identifier import StorageIdentifier
from ..models.system_component_base_info_type import SystemComponentBaseInfoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="NvmeStorageControllerInfo")


@attr.s(auto_attribs=True)
class NvmeStorageControllerInfo:
    """
    Attributes:
        name (str): Name of the system HW component Example: system component name.
        id (str):  Example: 9005:0285:9005:02b7.
        type (SystemComponentBaseInfoType): Type of the system HW component Example: PCI DEVICE.
        class_code (str): 2-hex digit PCI class code Example: 1.
        vid (str): 4-digit PCI vendor ID (VID) Example: 1077.
        did (str): 4-digit PCI device ID (DID) Example: 2020.
        svid (str): 4-digit PCI subsystem vendor ID (SVID) Example: 103c.
        ssid (str): 4-digit PCI subsystem ID (SSID) Example: 170000000.
        description (Union[Unset, str]): User-friendly description of object type Example: Storage controller.
        part_number (Union[Unset, str]): The part number for this system component. For components listed on VMware VCG,
            this must match the VCG listing. Example: 35VHD.
        class_sub_code (Union[Unset, str]): 2-hex digit PCI sub-class code Example: 4.
        prog_if (Union[Unset, str]): 2-hex digit PCI programmaing interface Example: 20.
        vendor (Union[Unset, str]): IEEE OUI Identifier for controller vendor Example: 6AB6F2.
        model (Union[Unset, str]): 40-character (ASCII) model number (MN) string from "Identify" command Example:
            Seagate.
        serial_number (Union[Unset, str]): 20-character (ASCII) serial Number (SN) string from "Identify" command
            Example: 1067985645890.
        durable_names (Union[Unset, List[StorageIdentifier]]):
    """

    name: str
    id: str
    type: SystemComponentBaseInfoType
    class_code: str
    vid: str
    did: str
    svid: str
    ssid: str
    description: Union[Unset, str] = UNSET
    part_number: Union[Unset, str] = UNSET
    class_sub_code: Union[Unset, str] = UNSET
    prog_if: Union[Unset, str] = UNSET
    vendor: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    durable_names: Union[Unset, List[StorageIdentifier]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        id = self.id
        type = self.type.value

        class_code = self.class_code
        vid = self.vid
        did = self.did
        svid = self.svid
        ssid = self.ssid
        description = self.description
        part_number = self.part_number
        class_sub_code = self.class_sub_code
        prog_if = self.prog_if
        vendor = self.vendor
        model = self.model
        serial_number = self.serial_number
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
                "classCode": class_code,
                "vid": vid,
                "did": did,
                "svid": svid,
                "ssid": ssid,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if class_sub_code is not UNSET:
            field_dict["classSubCode"] = class_sub_code
        if prog_if is not UNSET:
            field_dict["progIf"] = prog_if
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if model is not UNSET:
            field_dict["model"] = model
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if durable_names is not UNSET:
            field_dict["durableNames"] = durable_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        id = d.pop("id")

        type = SystemComponentBaseInfoType(d.pop("type"))

        class_code = d.pop("classCode")

        vid = d.pop("vid")

        did = d.pop("did")

        svid = d.pop("svid")

        ssid = d.pop("ssid")

        description = d.pop("description", UNSET)

        part_number = d.pop("partNumber", UNSET)

        class_sub_code = d.pop("classSubCode", UNSET)

        prog_if = d.pop("progIf", UNSET)

        vendor = d.pop("vendor", UNSET)

        model = d.pop("model", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        durable_names = []
        _durable_names = d.pop("durableNames", UNSET)
        for durable_names_item_data in _durable_names or []:
            durable_names_item = StorageIdentifier.from_dict(durable_names_item_data)

            durable_names.append(durable_names_item)

        nvme_storage_controller_info = cls(
            name=name,
            id=id,
            type=type,
            class_code=class_code,
            vid=vid,
            did=did,
            svid=svid,
            ssid=ssid,
            description=description,
            part_number=part_number,
            class_sub_code=class_sub_code,
            prog_if=prog_if,
            vendor=vendor,
            model=model,
            serial_number=serial_number,
            durable_names=durable_names,
        )

        nvme_storage_controller_info.additional_properties = d
        return nvme_storage_controller_info

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
