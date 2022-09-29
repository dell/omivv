from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.sub_system_sensor_health import SubSystemSensorHealth
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeviceSensorHealth")


@attr.s(auto_attribs=True)
class DeviceSensorHealth:
    """
    Attributes:
        device_id (Union[Unset, int]):
        sub_system_sensor_health (Union[Unset, List[SubSystemSensorHealth]]):
    """

    device_id: Union[Unset, int] = UNSET
    sub_system_sensor_health: Union[Unset, List[SubSystemSensorHealth]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        device_id = self.device_id
        sub_system_sensor_health: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sub_system_sensor_health, Unset):
            sub_system_sensor_health = []
            for sub_system_sensor_health_item_data in self.sub_system_sensor_health:
                sub_system_sensor_health_item = sub_system_sensor_health_item_data.to_dict()

                sub_system_sensor_health.append(sub_system_sensor_health_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if sub_system_sensor_health is not UNSET:
            field_dict["subSystemSensorHealth"] = sub_system_sensor_health

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        sub_system_sensor_health = []
        _sub_system_sensor_health = d.pop("subSystemSensorHealth", UNSET)
        for sub_system_sensor_health_item_data in _sub_system_sensor_health or []:
            sub_system_sensor_health_item = SubSystemSensorHealth.from_dict(sub_system_sensor_health_item_data)

            sub_system_sensor_health.append(sub_system_sensor_health_item)

        device_sensor_health = cls(
            device_id=device_id,
            sub_system_sensor_health=sub_system_sensor_health,
        )

        device_sensor_health.additional_properties = d
        return device_sensor_health

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
