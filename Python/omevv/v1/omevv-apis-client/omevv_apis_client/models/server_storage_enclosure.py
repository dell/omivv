from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServerStorageEnclosure")


@attr.s(auto_attribs=True)
class ServerStorageEnclosure:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        status (Union[Unset, int]):
        status_type_string (Union[Unset, str]):
        channel_number (Union[Unset, str]):
        backplane_part_num (Union[Unset, str]):
        number_of_fan_packs (Union[Unset, int]):
        version (Union[Unset, str]):
        rollup_status (Union[Unset, int]):
        slot_count (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, int] = UNSET
    status_type_string: Union[Unset, str] = UNSET
    channel_number: Union[Unset, str] = UNSET
    backplane_part_num: Union[Unset, str] = UNSET
    number_of_fan_packs: Union[Unset, int] = UNSET
    version: Union[Unset, str] = UNSET
    rollup_status: Union[Unset, int] = UNSET
    slot_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        status = self.status
        status_type_string = self.status_type_string
        channel_number = self.channel_number
        backplane_part_num = self.backplane_part_num
        number_of_fan_packs = self.number_of_fan_packs
        version = self.version
        rollup_status = self.rollup_status
        slot_count = self.slot_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if status_type_string is not UNSET:
            field_dict["statusTypeString"] = status_type_string
        if channel_number is not UNSET:
            field_dict["channelNumber"] = channel_number
        if backplane_part_num is not UNSET:
            field_dict["backplanePartNum"] = backplane_part_num
        if number_of_fan_packs is not UNSET:
            field_dict["numberOfFanPacks"] = number_of_fan_packs
        if version is not UNSET:
            field_dict["version"] = version
        if rollup_status is not UNSET:
            field_dict["rollupStatus"] = rollup_status
        if slot_count is not UNSET:
            field_dict["slotCount"] = slot_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        status = d.pop("status", UNSET)

        status_type_string = d.pop("statusTypeString", UNSET)

        channel_number = d.pop("channelNumber", UNSET)

        backplane_part_num = d.pop("backplanePartNum", UNSET)

        number_of_fan_packs = d.pop("numberOfFanPacks", UNSET)

        version = d.pop("version", UNSET)

        rollup_status = d.pop("rollupStatus", UNSET)

        slot_count = d.pop("slotCount", UNSET)

        server_storage_enclosure = cls(
            id=id,
            name=name,
            status=status,
            status_type_string=status_type_string,
            channel_number=channel_number,
            backplane_part_num=backplane_part_num,
            number_of_fan_packs=number_of_fan_packs,
            version=version,
            rollup_status=rollup_status,
            slot_count=slot_count,
        )

        server_storage_enclosure.additional_properties = d
        return server_storage_enclosure

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
