from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.server_array_disk_hot_spare_type import ServerArrayDiskHotSpareType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerArrayDisk")


@attr.s(auto_attribs=True)
class ServerArrayDisk:
    """
    Attributes:
        id (Union[Unset, int]):
        disk_number (Union[Unset, str]):
        vendor_name (Union[Unset, str]):
        status (Union[Unset, int]):
        status_string (Union[Unset, str]):
        model_number (Union[Unset, str]):
        serial_number (Union[Unset, str]):
        sas_address (Union[Unset, str]):
        revision (Union[Unset, str]):
        manufactured_day (Union[Unset, int]):
        manufactured_week (Union[Unset, int]):
        manufactured_year (Union[Unset, int]):
        encryption_ability (Union[Unset, bool]):
        form_factor (Union[Unset, str]):
        part_number (Union[Unset, str]):
        predicted_failure_state (Union[Unset, str]):
        enclosure_id (Union[Unset, str]):
        channel (Union[Unset, int]):
        size (Union[Unset, str]):
        free_space (Union[Unset, str]):
        used_space (Union[Unset, str]):
        bus_type (Union[Unset, str]):
        slot_number (Union[Unset, int]):
        media_type (Union[Unset, str]):
        remaining_read_write_endurance (Union[Unset, str]):
        security_state (Union[Unset, str]):
        raid_status (Union[Unset, str]):
        name (Union[Unset, str]):
        hot_spare_type (Union[Unset, ServerArrayDiskHotSpareType]):
        virtual_disk (Union[Unset, str]):
        controller_id (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    disk_number: Union[Unset, str] = UNSET
    vendor_name: Union[Unset, str] = UNSET
    status: Union[Unset, int] = UNSET
    status_string: Union[Unset, str] = UNSET
    model_number: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    sas_address: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    manufactured_day: Union[Unset, int] = UNSET
    manufactured_week: Union[Unset, int] = UNSET
    manufactured_year: Union[Unset, int] = UNSET
    encryption_ability: Union[Unset, bool] = UNSET
    form_factor: Union[Unset, str] = UNSET
    part_number: Union[Unset, str] = UNSET
    predicted_failure_state: Union[Unset, str] = UNSET
    enclosure_id: Union[Unset, str] = UNSET
    channel: Union[Unset, int] = UNSET
    size: Union[Unset, str] = UNSET
    free_space: Union[Unset, str] = UNSET
    used_space: Union[Unset, str] = UNSET
    bus_type: Union[Unset, str] = UNSET
    slot_number: Union[Unset, int] = UNSET
    media_type: Union[Unset, str] = UNSET
    remaining_read_write_endurance: Union[Unset, str] = UNSET
    security_state: Union[Unset, str] = UNSET
    raid_status: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    hot_spare_type: Union[Unset, ServerArrayDiskHotSpareType] = UNSET
    virtual_disk: Union[Unset, str] = UNSET
    controller_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        disk_number = self.disk_number
        vendor_name = self.vendor_name
        status = self.status
        status_string = self.status_string
        model_number = self.model_number
        serial_number = self.serial_number
        sas_address = self.sas_address
        revision = self.revision
        manufactured_day = self.manufactured_day
        manufactured_week = self.manufactured_week
        manufactured_year = self.manufactured_year
        encryption_ability = self.encryption_ability
        form_factor = self.form_factor
        part_number = self.part_number
        predicted_failure_state = self.predicted_failure_state
        enclosure_id = self.enclosure_id
        channel = self.channel
        size = self.size
        free_space = self.free_space
        used_space = self.used_space
        bus_type = self.bus_type
        slot_number = self.slot_number
        media_type = self.media_type
        remaining_read_write_endurance = self.remaining_read_write_endurance
        security_state = self.security_state
        raid_status = self.raid_status
        name = self.name
        hot_spare_type: Union[Unset, str] = UNSET
        if not isinstance(self.hot_spare_type, Unset):
            hot_spare_type = self.hot_spare_type.value

        virtual_disk = self.virtual_disk
        controller_id = self.controller_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if disk_number is not UNSET:
            field_dict["diskNumber"] = disk_number
        if vendor_name is not UNSET:
            field_dict["vendorName"] = vendor_name
        if status is not UNSET:
            field_dict["status"] = status
        if status_string is not UNSET:
            field_dict["statusString"] = status_string
        if model_number is not UNSET:
            field_dict["modelNumber"] = model_number
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if sas_address is not UNSET:
            field_dict["sasAddress"] = sas_address
        if revision is not UNSET:
            field_dict["revision"] = revision
        if manufactured_day is not UNSET:
            field_dict["manufacturedDay"] = manufactured_day
        if manufactured_week is not UNSET:
            field_dict["manufacturedWeek"] = manufactured_week
        if manufactured_year is not UNSET:
            field_dict["manufacturedYear"] = manufactured_year
        if encryption_ability is not UNSET:
            field_dict["encryptionAbility"] = encryption_ability
        if form_factor is not UNSET:
            field_dict["formFactor"] = form_factor
        if part_number is not UNSET:
            field_dict["partNumber"] = part_number
        if predicted_failure_state is not UNSET:
            field_dict["predictedFailureState"] = predicted_failure_state
        if enclosure_id is not UNSET:
            field_dict["enclosureId"] = enclosure_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if size is not UNSET:
            field_dict["size"] = size
        if free_space is not UNSET:
            field_dict["freeSpace"] = free_space
        if used_space is not UNSET:
            field_dict["usedSpace"] = used_space
        if bus_type is not UNSET:
            field_dict["busType"] = bus_type
        if slot_number is not UNSET:
            field_dict["slotNumber"] = slot_number
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type
        if remaining_read_write_endurance is not UNSET:
            field_dict["remainingReadWriteEndurance"] = remaining_read_write_endurance
        if security_state is not UNSET:
            field_dict["securityState"] = security_state
        if raid_status is not UNSET:
            field_dict["raidStatus"] = raid_status
        if name is not UNSET:
            field_dict["name"] = name
        if hot_spare_type is not UNSET:
            field_dict["hotSpareType"] = hot_spare_type
        if virtual_disk is not UNSET:
            field_dict["virtualDisk"] = virtual_disk
        if controller_id is not UNSET:
            field_dict["controllerId"] = controller_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        disk_number = d.pop("diskNumber", UNSET)

        vendor_name = d.pop("vendorName", UNSET)

        status = d.pop("status", UNSET)

        status_string = d.pop("statusString", UNSET)

        model_number = d.pop("modelNumber", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        sas_address = d.pop("sasAddress", UNSET)

        revision = d.pop("revision", UNSET)

        manufactured_day = d.pop("manufacturedDay", UNSET)

        manufactured_week = d.pop("manufacturedWeek", UNSET)

        manufactured_year = d.pop("manufacturedYear", UNSET)

        encryption_ability = d.pop("encryptionAbility", UNSET)

        form_factor = d.pop("formFactor", UNSET)

        part_number = d.pop("partNumber", UNSET)

        predicted_failure_state = d.pop("predictedFailureState", UNSET)

        enclosure_id = d.pop("enclosureId", UNSET)

        channel = d.pop("channel", UNSET)

        size = d.pop("size", UNSET)

        free_space = d.pop("freeSpace", UNSET)

        used_space = d.pop("usedSpace", UNSET)

        bus_type = d.pop("busType", UNSET)

        slot_number = d.pop("slotNumber", UNSET)

        media_type = d.pop("mediaType", UNSET)

        remaining_read_write_endurance = d.pop("remainingReadWriteEndurance", UNSET)

        security_state = d.pop("securityState", UNSET)

        raid_status = d.pop("raidStatus", UNSET)

        name = d.pop("name", UNSET)

        _hot_spare_type = d.pop("hotSpareType", UNSET)
        hot_spare_type: Union[Unset, ServerArrayDiskHotSpareType]
        if isinstance(_hot_spare_type, Unset):
            hot_spare_type = UNSET
        else:
            hot_spare_type = ServerArrayDiskHotSpareType(_hot_spare_type)

        virtual_disk = d.pop("virtualDisk", UNSET)

        controller_id = d.pop("controllerId", UNSET)

        server_array_disk = cls(
            id=id,
            disk_number=disk_number,
            vendor_name=vendor_name,
            status=status,
            status_string=status_string,
            model_number=model_number,
            serial_number=serial_number,
            sas_address=sas_address,
            revision=revision,
            manufactured_day=manufactured_day,
            manufactured_week=manufactured_week,
            manufactured_year=manufactured_year,
            encryption_ability=encryption_ability,
            form_factor=form_factor,
            part_number=part_number,
            predicted_failure_state=predicted_failure_state,
            enclosure_id=enclosure_id,
            channel=channel,
            size=size,
            free_space=free_space,
            used_space=used_space,
            bus_type=bus_type,
            slot_number=slot_number,
            media_type=media_type,
            remaining_read_write_endurance=remaining_read_write_endurance,
            security_state=security_state,
            raid_status=raid_status,
            name=name,
            hot_spare_type=hot_spare_type,
            virtual_disk=virtual_disk,
            controller_id=controller_id,
        )

        server_array_disk.additional_properties = d
        return server_array_disk

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
