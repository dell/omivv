from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.component_sensor_health_data_component_health import ComponentSensorHealthDataComponentHealth
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComponentSensorHealthData")


@attr.s(auto_attribs=True)
class ComponentSensorHealthData:
    """
    Attributes:
        component_name (Union[Unset, str]): Name of Component.
        component_health (Union[Unset, ComponentSensorHealthDataComponentHealth]): Health of Component.
    """

    component_name: Union[Unset, str] = UNSET
    component_health: Union[Unset, ComponentSensorHealthDataComponentHealth] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        component_name = self.component_name
        component_health: Union[Unset, str] = UNSET
        if not isinstance(self.component_health, Unset):
            component_health = self.component_health.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if component_name is not UNSET:
            field_dict["componentName"] = component_name
        if component_health is not UNSET:
            field_dict["componentHealth"] = component_health

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        component_name = d.pop("componentName", UNSET)

        _component_health = d.pop("componentHealth", UNSET)
        component_health: Union[Unset, ComponentSensorHealthDataComponentHealth]
        if isinstance(_component_health, Unset):
            component_health = UNSET
        else:
            component_health = ComponentSensorHealthDataComponentHealth(_component_health)

        component_sensor_health_data = cls(
            component_name=component_name,
            component_health=component_health,
        )

        component_sensor_health_data.additional_properties = d
        return component_sensor_health_data

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
