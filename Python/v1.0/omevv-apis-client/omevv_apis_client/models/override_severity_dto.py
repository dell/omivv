from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OverrideSeverityDto")


@attr.s(auto_attribs=True)
class OverrideSeverityDto:
    """
    Attributes:
        id (Union[Unset, int]):
        component (Union[Unset, str]):
        description (Union[Unset, str]):
        default_severity (Union[Unset, str]):
        override_severity (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    component: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    default_severity: Union[Unset, str] = UNSET
    override_severity: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        component = self.component
        description = self.description
        default_severity = self.default_severity
        override_severity = self.override_severity

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if component is not UNSET:
            field_dict["component"] = component
        if description is not UNSET:
            field_dict["description"] = description
        if default_severity is not UNSET:
            field_dict["defaultSeverity"] = default_severity
        if override_severity is not UNSET:
            field_dict["overrideSeverity"] = override_severity

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        component = d.pop("component", UNSET)

        description = d.pop("description", UNSET)

        default_severity = d.pop("defaultSeverity", UNSET)

        override_severity = d.pop("overrideSeverity", UNSET)

        override_severity_dto = cls(
            id=id,
            component=component,
            description=description,
            default_severity=default_severity,
            override_severity=override_severity,
        )

        override_severity_dto.additional_properties = d
        return override_severity_dto

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
