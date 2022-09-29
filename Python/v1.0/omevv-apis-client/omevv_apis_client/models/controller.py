from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.virtual_disk import VirtualDisk
from ..types import UNSET, Unset

T = TypeVar("T", bound="Controller")


@attr.s(auto_attribs=True)
class Controller:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]): displays the name of the controller.
        fqdd (Union[Unset, str]): displays the FQDD of the device.
        device_description (Union[Unset, str]):
        status_string (Union[Unset, str]):
        rollup_status_string (Union[Unset, str]):
        firmware_version (Union[Unset, str]): displays the firmware version.
        cache_size_in_mb (Union[Unset, int]): displays the cache size.
        pci_slot (Union[Unset, str]):
        driver_version (Union[Unset, str]): displays the driver version.
        storage_assignment_allowed (Union[Unset, str]):
        raid_current_controller_mode (Union[Unset, str]):
        sas_address (Union[Unset, str]):
        raid_max_capable_speed (Union[Unset, str]):
        security_status (Union[Unset, str]):
        cache_size (Union[Unset, int]):
        virtual_disks (Union[Unset, List[VirtualDisk]]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    fqdd: Union[Unset, str] = UNSET
    device_description: Union[Unset, str] = UNSET
    status_string: Union[Unset, str] = UNSET
    rollup_status_string: Union[Unset, str] = UNSET
    firmware_version: Union[Unset, str] = UNSET
    cache_size_in_mb: Union[Unset, int] = UNSET
    pci_slot: Union[Unset, str] = UNSET
    driver_version: Union[Unset, str] = UNSET
    storage_assignment_allowed: Union[Unset, str] = UNSET
    raid_current_controller_mode: Union[Unset, str] = UNSET
    sas_address: Union[Unset, str] = UNSET
    raid_max_capable_speed: Union[Unset, str] = UNSET
    security_status: Union[Unset, str] = UNSET
    cache_size: Union[Unset, int] = UNSET
    virtual_disks: Union[Unset, List[VirtualDisk]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        fqdd = self.fqdd
        device_description = self.device_description
        status_string = self.status_string
        rollup_status_string = self.rollup_status_string
        firmware_version = self.firmware_version
        cache_size_in_mb = self.cache_size_in_mb
        pci_slot = self.pci_slot
        driver_version = self.driver_version
        storage_assignment_allowed = self.storage_assignment_allowed
        raid_current_controller_mode = self.raid_current_controller_mode
        sas_address = self.sas_address
        raid_max_capable_speed = self.raid_max_capable_speed
        security_status = self.security_status
        cache_size = self.cache_size
        virtual_disks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.virtual_disks, Unset):
            virtual_disks = []
            for virtual_disks_item_data in self.virtual_disks:
                virtual_disks_item = virtual_disks_item_data.to_dict()

                virtual_disks.append(virtual_disks_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if fqdd is not UNSET:
            field_dict["fqdd"] = fqdd
        if device_description is not UNSET:
            field_dict["deviceDescription"] = device_description
        if status_string is not UNSET:
            field_dict["statusString"] = status_string
        if rollup_status_string is not UNSET:
            field_dict["rollupStatusString"] = rollup_status_string
        if firmware_version is not UNSET:
            field_dict["firmwareVersion"] = firmware_version
        if cache_size_in_mb is not UNSET:
            field_dict["cacheSizeInMb"] = cache_size_in_mb
        if pci_slot is not UNSET:
            field_dict["pciSlot"] = pci_slot
        if driver_version is not UNSET:
            field_dict["driverVersion"] = driver_version
        if storage_assignment_allowed is not UNSET:
            field_dict["storageAssignmentAllowed"] = storage_assignment_allowed
        if raid_current_controller_mode is not UNSET:
            field_dict["raidCurrentControllerMode"] = raid_current_controller_mode
        if sas_address is not UNSET:
            field_dict["sasAddress"] = sas_address
        if raid_max_capable_speed is not UNSET:
            field_dict["raidMaxCapableSpeed"] = raid_max_capable_speed
        if security_status is not UNSET:
            field_dict["securityStatus"] = security_status
        if cache_size is not UNSET:
            field_dict["cacheSize"] = cache_size
        if virtual_disks is not UNSET:
            field_dict["virtualDisks"] = virtual_disks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        fqdd = d.pop("fqdd", UNSET)

        device_description = d.pop("deviceDescription", UNSET)

        status_string = d.pop("statusString", UNSET)

        rollup_status_string = d.pop("rollupStatusString", UNSET)

        firmware_version = d.pop("firmwareVersion", UNSET)

        cache_size_in_mb = d.pop("cacheSizeInMb", UNSET)

        pci_slot = d.pop("pciSlot", UNSET)

        driver_version = d.pop("driverVersion", UNSET)

        storage_assignment_allowed = d.pop("storageAssignmentAllowed", UNSET)

        raid_current_controller_mode = d.pop("raidCurrentControllerMode", UNSET)

        sas_address = d.pop("sasAddress", UNSET)

        raid_max_capable_speed = d.pop("raidMaxCapableSpeed", UNSET)

        security_status = d.pop("securityStatus", UNSET)

        cache_size = d.pop("cacheSize", UNSET)

        virtual_disks = []
        _virtual_disks = d.pop("virtualDisks", UNSET)
        for virtual_disks_item_data in _virtual_disks or []:
            virtual_disks_item = VirtualDisk.from_dict(virtual_disks_item_data)

            virtual_disks.append(virtual_disks_item)

        controller = cls(
            id=id,
            name=name,
            fqdd=fqdd,
            device_description=device_description,
            status_string=status_string,
            rollup_status_string=rollup_status_string,
            firmware_version=firmware_version,
            cache_size_in_mb=cache_size_in_mb,
            pci_slot=pci_slot,
            driver_version=driver_version,
            storage_assignment_allowed=storage_assignment_allowed,
            raid_current_controller_mode=raid_current_controller_mode,
            sas_address=sas_address,
            raid_max_capable_speed=raid_max_capable_speed,
            security_status=security_status,
            cache_size=cache_size,
            virtual_disks=virtual_disks,
        )

        controller.additional_properties = d
        return controller

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
