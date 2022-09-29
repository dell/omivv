from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VirtualDisk")


@attr.s(auto_attribs=True)
class VirtualDisk:
    """
    Attributes:
        id (Union[Unset, int]):
        raid_controller_id (Union[Unset, int]):
        fqdd (Union[Unset, str]): displays the FQDD.
        state (Union[Unset, str]):
        rollup_status (Union[Unset, str]):
        status (Union[Unset, str]):
        layout (Union[Unset, str]): displays the layout type of the virtual storage, which means the type of RAID that
            was configured for this virtual drive.
        media_type (Union[Unset, str]): displays either Solid-State Drive or Hard Disk  Drive.
        name (Union[Unset, str]):
        read_policy (Union[Unset, str]): displays the default read policy that is supported by the controller.
        write_policy (Union[Unset, str]): displays the default write policy that is supported by the controller.
        cache_policy (Union[Unset, str]): displays if cache policy is enabled.
        stripe_size (Union[Unset, str]): displays the stripe size, which is the amount of space that each stripe
            consumes on a single disk.
        size (Union[Unset, str]):
        target_id (Union[Unset, int]):
        lock_status (Union[Unset, str]):
        physical_disks_count (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    raid_controller_id: Union[Unset, int] = UNSET
    fqdd: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    rollup_status: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    layout: Union[Unset, str] = UNSET
    media_type: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    read_policy: Union[Unset, str] = UNSET
    write_policy: Union[Unset, str] = UNSET
    cache_policy: Union[Unset, str] = UNSET
    stripe_size: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    target_id: Union[Unset, int] = UNSET
    lock_status: Union[Unset, str] = UNSET
    physical_disks_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        raid_controller_id = self.raid_controller_id
        fqdd = self.fqdd
        state = self.state
        rollup_status = self.rollup_status
        status = self.status
        layout = self.layout
        media_type = self.media_type
        name = self.name
        read_policy = self.read_policy
        write_policy = self.write_policy
        cache_policy = self.cache_policy
        stripe_size = self.stripe_size
        size = self.size
        target_id = self.target_id
        lock_status = self.lock_status
        physical_disks_count = self.physical_disks_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if raid_controller_id is not UNSET:
            field_dict["raidControllerId"] = raid_controller_id
        if fqdd is not UNSET:
            field_dict["fqdd"] = fqdd
        if state is not UNSET:
            field_dict["state"] = state
        if rollup_status is not UNSET:
            field_dict["rollupStatus"] = rollup_status
        if status is not UNSET:
            field_dict["status"] = status
        if layout is not UNSET:
            field_dict["layout"] = layout
        if media_type is not UNSET:
            field_dict["mediaType"] = media_type
        if name is not UNSET:
            field_dict["name"] = name
        if read_policy is not UNSET:
            field_dict["readPolicy"] = read_policy
        if write_policy is not UNSET:
            field_dict["writePolicy"] = write_policy
        if cache_policy is not UNSET:
            field_dict["cachePolicy"] = cache_policy
        if stripe_size is not UNSET:
            field_dict["stripeSize"] = stripe_size
        if size is not UNSET:
            field_dict["size"] = size
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if lock_status is not UNSET:
            field_dict["lockStatus"] = lock_status
        if physical_disks_count is not UNSET:
            field_dict["physicalDisksCount"] = physical_disks_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        raid_controller_id = d.pop("raidControllerId", UNSET)

        fqdd = d.pop("fqdd", UNSET)

        state = d.pop("state", UNSET)

        rollup_status = d.pop("rollupStatus", UNSET)

        status = d.pop("status", UNSET)

        layout = d.pop("layout", UNSET)

        media_type = d.pop("mediaType", UNSET)

        name = d.pop("name", UNSET)

        read_policy = d.pop("readPolicy", UNSET)

        write_policy = d.pop("writePolicy", UNSET)

        cache_policy = d.pop("cachePolicy", UNSET)

        stripe_size = d.pop("stripeSize", UNSET)

        size = d.pop("size", UNSET)

        target_id = d.pop("targetId", UNSET)

        lock_status = d.pop("lockStatus", UNSET)

        physical_disks_count = d.pop("physicalDisksCount", UNSET)

        virtual_disk = cls(
            id=id,
            raid_controller_id=raid_controller_id,
            fqdd=fqdd,
            state=state,
            rollup_status=rollup_status,
            status=status,
            layout=layout,
            media_type=media_type,
            name=name,
            read_policy=read_policy,
            write_policy=write_policy,
            cache_policy=cache_policy,
            stripe_size=stripe_size,
            size=size,
            target_id=target_id,
            lock_status=lock_status,
            physical_disks_count=physical_disks_count,
        )

        virtual_disk.additional_properties = d
        return virtual_disk

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
