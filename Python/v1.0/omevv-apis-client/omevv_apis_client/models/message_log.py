import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MessageLog")


@attr.s(auto_attribs=True)
class MessageLog:
    """
    Attributes:
        updated_time (Union[Unset, datetime.datetime]):
        message (Union[Unset, str]):
    """

    updated_time: Union[Unset, datetime.datetime] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        updated_time: Union[Unset, str] = UNSET
        if not isinstance(self.updated_time, Unset):
            updated_time = self.updated_time.isoformat()

        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if updated_time is not UNSET:
            field_dict["updatedTime"] = updated_time
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _updated_time = d.pop("updatedTime", UNSET)
        updated_time: Union[Unset, datetime.datetime]
        if isinstance(_updated_time, Unset):
            updated_time = UNSET
        else:
            updated_time = isoparse(_updated_time)

        message = d.pop("message", UNSET)

        message_log = cls(
            updated_time=updated_time,
            message=message,
        )

        message_log.additional_properties = d
        return message_log

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
