from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Memory")


@attr.s(auto_attribs=True)
class Memory:
    """
    Attributes:
        name (Union[Unset, str]):
        size (Union[Unset, str]):
        type (Union[Unset, str]):
        speed (Union[Unset, str]):
        current_operating_speed (Union[Unset, str]):
    """

    name: Union[Unset, str] = UNSET
    size: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    speed: Union[Unset, str] = UNSET
    current_operating_speed: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        size = self.size
        type = self.type
        speed = self.speed
        current_operating_speed = self.current_operating_speed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if type is not UNSET:
            field_dict["type"] = type
        if speed is not UNSET:
            field_dict["speed"] = speed
        if current_operating_speed is not UNSET:
            field_dict["currentOperatingSpeed"] = current_operating_speed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        size = d.pop("size", UNSET)

        type = d.pop("type", UNSET)

        speed = d.pop("speed", UNSET)

        current_operating_speed = d.pop("currentOperatingSpeed", UNSET)

        memory = cls(
            name=name,
            size=size,
            type=type,
            speed=speed,
            current_operating_speed=current_operating_speed,
        )

        memory.additional_properties = d
        return memory

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
