import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.device_component_type import DeviceComponentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Firmware")


@attr.s(auto_attribs=True)
class Firmware:
    """
    Attributes:
        version (Union[Unset, str]):
        installation_date (Union[Unset, datetime.datetime]):
        status (Union[Unset, str]):
        software_type (Union[Unset, str]):
        component_type (Union[Unset, DeviceComponentType]):
        component_id (Union[Unset, str]):
        vendor_id (Union[Unset, str]):
        sub_device_id (Union[Unset, str]):
        sub_vendor_id (Union[Unset, str]):
        pci_device_id (Union[Unset, str]):
        device_description (Union[Unset, str]):
        instance_id (Union[Unset, str]):
    """

    version: Union[Unset, str] = UNSET
    installation_date: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, str] = UNSET
    software_type: Union[Unset, str] = UNSET
    component_type: Union[Unset, DeviceComponentType] = UNSET
    component_id: Union[Unset, str] = UNSET
    vendor_id: Union[Unset, str] = UNSET
    sub_device_id: Union[Unset, str] = UNSET
    sub_vendor_id: Union[Unset, str] = UNSET
    pci_device_id: Union[Unset, str] = UNSET
    device_description: Union[Unset, str] = UNSET
    instance_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        installation_date: Union[Unset, str] = UNSET
        if not isinstance(self.installation_date, Unset):
            installation_date = self.installation_date.isoformat()

        status = self.status
        software_type = self.software_type
        component_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.component_type, Unset):
            component_type = self.component_type.to_dict()

        component_id = self.component_id
        vendor_id = self.vendor_id
        sub_device_id = self.sub_device_id
        sub_vendor_id = self.sub_vendor_id
        pci_device_id = self.pci_device_id
        device_description = self.device_description
        instance_id = self.instance_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if installation_date is not UNSET:
            field_dict["installationDate"] = installation_date
        if status is not UNSET:
            field_dict["status"] = status
        if software_type is not UNSET:
            field_dict["softwareType"] = software_type
        if component_type is not UNSET:
            field_dict["componentType"] = component_type
        if component_id is not UNSET:
            field_dict["componentId"] = component_id
        if vendor_id is not UNSET:
            field_dict["vendorId"] = vendor_id
        if sub_device_id is not UNSET:
            field_dict["subDeviceId"] = sub_device_id
        if sub_vendor_id is not UNSET:
            field_dict["subVendorId"] = sub_vendor_id
        if pci_device_id is not UNSET:
            field_dict["pciDeviceId"] = pci_device_id
        if device_description is not UNSET:
            field_dict["deviceDescription"] = device_description
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("version", UNSET)

        _installation_date = d.pop("installationDate", UNSET)
        installation_date: Union[Unset, datetime.datetime]
        if isinstance(_installation_date, Unset):
            installation_date = UNSET
        else:
            installation_date = isoparse(_installation_date)

        status = d.pop("status", UNSET)

        software_type = d.pop("softwareType", UNSET)

        _component_type = d.pop("componentType", UNSET)
        component_type: Union[Unset, DeviceComponentType]
        if isinstance(_component_type, Unset):
            component_type = UNSET
        else:
            component_type = DeviceComponentType.from_dict(_component_type)

        component_id = d.pop("componentId", UNSET)

        vendor_id = d.pop("vendorId", UNSET)

        sub_device_id = d.pop("subDeviceId", UNSET)

        sub_vendor_id = d.pop("subVendorId", UNSET)

        pci_device_id = d.pop("pciDeviceId", UNSET)

        device_description = d.pop("deviceDescription", UNSET)

        instance_id = d.pop("instanceId", UNSET)

        firmware = cls(
            version=version,
            installation_date=installation_date,
            status=status,
            software_type=software_type,
            component_type=component_type,
            component_id=component_id,
            vendor_id=vendor_id,
            sub_device_id=sub_device_id,
            sub_vendor_id=sub_vendor_id,
            pci_device_id=pci_device_id,
            device_description=device_description,
            instance_id=instance_id,
        )

        firmware.additional_properties = d
        return firmware

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
