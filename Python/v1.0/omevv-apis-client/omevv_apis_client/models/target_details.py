from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.target_details_target_type import TargetDetailsTargetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TargetDetails")


@attr.s(auto_attribs=True)
class TargetDetails:
    """
    Attributes:
        target_id (Union[Unset, str]): omevv target id(device/group)
        console_address (Union[Unset, str]): vCenter IP/FQDN
        target_type (Union[Unset, TargetDetailsTargetType]):
    """

    target_id: Union[Unset, str] = UNSET
    console_address: Union[Unset, str] = UNSET
    target_type: Union[Unset, TargetDetailsTargetType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        target_id = self.target_id
        console_address = self.console_address
        target_type: Union[Unset, str] = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_id is not UNSET:
            field_dict["targetId"] = target_id
        if console_address is not UNSET:
            field_dict["consoleAddress"] = console_address
        if target_type is not UNSET:
            field_dict["targetType"] = target_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        target_id = d.pop("targetId", UNSET)

        console_address = d.pop("consoleAddress", UNSET)

        _target_type = d.pop("targetType", UNSET)
        target_type: Union[Unset, TargetDetailsTargetType]
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = TargetDetailsTargetType(_target_type)

        target_details = cls(
            target_id=target_id,
            console_address=console_address,
            target_type=target_type,
        )

        target_details.additional_properties = d
        return target_details

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
