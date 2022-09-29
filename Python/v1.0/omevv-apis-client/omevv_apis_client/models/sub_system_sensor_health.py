from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.component_sensor_health_data import ComponentSensorHealthData
from ..models.sub_system_sensor_health_sub_system_name import SubSystemSensorHealthSubSystemName
from ..models.sub_system_sensor_health_sub_system_rollup import SubSystemSensorHealthSubSystemRollup
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubSystemSensorHealth")


@attr.s(auto_attribs=True)
class SubSystemSensorHealth:
    """
    Attributes:
        sub_system_name (Union[Unset, SubSystemSensorHealthSubSystemName]): Subsystem name.
        sub_system_rollup (Union[Unset, SubSystemSensorHealthSubSystemRollup]): Subsystem Health status.
        reason (Union[Unset, str]): Reason.
        component_sensor_health (Union[Unset, List[ComponentSensorHealthData]]): List of subsystem.
    """

    sub_system_name: Union[Unset, SubSystemSensorHealthSubSystemName] = UNSET
    sub_system_rollup: Union[Unset, SubSystemSensorHealthSubSystemRollup] = UNSET
    reason: Union[Unset, str] = UNSET
    component_sensor_health: Union[Unset, List[ComponentSensorHealthData]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sub_system_name: Union[Unset, str] = UNSET
        if not isinstance(self.sub_system_name, Unset):
            sub_system_name = self.sub_system_name.value

        sub_system_rollup: Union[Unset, str] = UNSET
        if not isinstance(self.sub_system_rollup, Unset):
            sub_system_rollup = self.sub_system_rollup.value

        reason = self.reason
        component_sensor_health: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.component_sensor_health, Unset):
            component_sensor_health = []
            for component_sensor_health_item_data in self.component_sensor_health:
                component_sensor_health_item = component_sensor_health_item_data.to_dict()

                component_sensor_health.append(component_sensor_health_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sub_system_name is not UNSET:
            field_dict["subSystemName"] = sub_system_name
        if sub_system_rollup is not UNSET:
            field_dict["subSystemRollup"] = sub_system_rollup
        if reason is not UNSET:
            field_dict["reason"] = reason
        if component_sensor_health is not UNSET:
            field_dict["componentSensorHealth"] = component_sensor_health

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _sub_system_name = d.pop("subSystemName", UNSET)
        sub_system_name: Union[Unset, SubSystemSensorHealthSubSystemName]
        if isinstance(_sub_system_name, Unset):
            sub_system_name = UNSET
        else:
            sub_system_name = SubSystemSensorHealthSubSystemName(_sub_system_name)

        _sub_system_rollup = d.pop("subSystemRollup", UNSET)
        sub_system_rollup: Union[Unset, SubSystemSensorHealthSubSystemRollup]
        if isinstance(_sub_system_rollup, Unset):
            sub_system_rollup = UNSET
        else:
            sub_system_rollup = SubSystemSensorHealthSubSystemRollup(_sub_system_rollup)

        reason = d.pop("reason", UNSET)

        component_sensor_health = []
        _component_sensor_health = d.pop("componentSensorHealth", UNSET)
        for component_sensor_health_item_data in _component_sensor_health or []:
            component_sensor_health_item = ComponentSensorHealthData.from_dict(component_sensor_health_item_data)

            component_sensor_health.append(component_sensor_health_item)

        sub_system_sensor_health = cls(
            sub_system_name=sub_system_name,
            sub_system_rollup=sub_system_rollup,
            reason=reason,
            component_sensor_health=component_sensor_health,
        )

        sub_system_sensor_health.additional_properties = d
        return sub_system_sensor_health

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
