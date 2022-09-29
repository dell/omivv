from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.device_device_type import DeviceDeviceType
from ..models.managed_host_health_status import ManagedHostHealthStatus
from ..models.managed_host_power_state import ManagedHostPowerState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManagedHost")


@attr.s(auto_attribs=True)
class ManagedHost:
    """
    Attributes:
        id (Union[Unset, int]):
        device_type (Union[Unset, DeviceDeviceType]):
        v_center_name (Union[Unset, str]):
        cluster_name (Union[Unset, str]):
        chassis_service_tag (Union[Unset, str]):
        power_state (Union[Unset, ManagedHostPowerState]):
        health_status (Union[Unset, ManagedHostHealthStatus]):
        group_name (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    device_type: Union[Unset, DeviceDeviceType] = UNSET
    v_center_name: Union[Unset, str] = UNSET
    cluster_name: Union[Unset, str] = UNSET
    chassis_service_tag: Union[Unset, str] = UNSET
    power_state: Union[Unset, ManagedHostPowerState] = UNSET
    health_status: Union[Unset, ManagedHostHealthStatus] = UNSET
    group_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        device_type: Union[Unset, str] = UNSET
        if not isinstance(self.device_type, Unset):
            device_type = self.device_type.value

        v_center_name = self.v_center_name
        cluster_name = self.cluster_name
        chassis_service_tag = self.chassis_service_tag
        power_state: Union[Unset, str] = UNSET
        if not isinstance(self.power_state, Unset):
            power_state = self.power_state.value

        health_status: Union[Unset, str] = UNSET
        if not isinstance(self.health_status, Unset):
            health_status = self.health_status.value

        group_name = self.group_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if device_type is not UNSET:
            field_dict["deviceType"] = device_type
        if v_center_name is not UNSET:
            field_dict["vCenterName"] = v_center_name
        if cluster_name is not UNSET:
            field_dict["clusterName"] = cluster_name
        if chassis_service_tag is not UNSET:
            field_dict["chassisServiceTag"] = chassis_service_tag
        if power_state is not UNSET:
            field_dict["powerState"] = power_state
        if health_status is not UNSET:
            field_dict["healthStatus"] = health_status
        if group_name is not UNSET:
            field_dict["groupName"] = group_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        _device_type = d.pop("deviceType", UNSET)
        device_type: Union[Unset, DeviceDeviceType]
        if isinstance(_device_type, Unset):
            device_type = UNSET
        else:
            device_type = DeviceDeviceType(_device_type)

        v_center_name = d.pop("vCenterName", UNSET)

        cluster_name = d.pop("clusterName", UNSET)

        chassis_service_tag = d.pop("chassisServiceTag", UNSET)

        _power_state = d.pop("powerState", UNSET)
        power_state: Union[Unset, ManagedHostPowerState]
        if isinstance(_power_state, Unset):
            power_state = UNSET
        else:
            power_state = ManagedHostPowerState(_power_state)

        _health_status = d.pop("healthStatus", UNSET)
        health_status: Union[Unset, ManagedHostHealthStatus]
        if isinstance(_health_status, Unset):
            health_status = UNSET
        else:
            health_status = ManagedHostHealthStatus(_health_status)

        group_name = d.pop("groupName", UNSET)

        managed_host = cls(
            id=id,
            device_type=device_type,
            v_center_name=v_center_name,
            cluster_name=cluster_name,
            chassis_service_tag=chassis_service_tag,
            power_state=power_state,
            health_status=health_status,
            group_name=group_name,
        )

        managed_host.additional_properties = d
        return managed_host

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
