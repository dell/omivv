from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="HardwareLog")


@attr.s(auto_attribs=True)
class HardwareLog:
    """
    Attributes:
        severity (Union[Unset, str]):
        timestamp (Union[Unset, str]):
        description (Union[Unset, str]):
    """

    severity: Union[Unset, str] = UNSET
    timestamp: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        severity = self.severity
        timestamp = self.timestamp
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if severity is not UNSET:
            field_dict["severity"] = severity
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        severity = d.pop("severity", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        description = d.pop("description", UNSET)

        hardware_log = cls(
            severity=severity,
            timestamp=timestamp,
            description=description,
        )

        hardware_log.additional_properties = d
        return hardware_log

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
