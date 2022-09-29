import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.user_facing_log_level import UserFacingLogLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserFacingLog")


@attr.s(auto_attribs=True)
class UserFacingLog:
    """User facing log object

    Attributes:
        id (Union[Unset, int]): Database ID of the user facing log object
        message (Union[Unset, str]): User facing log message
        level (Union[Unset, UserFacingLogLevel]): Log level or severity of the log message
        created_date (Union[Unset, datetime.datetime]): Log message creation date and time
    """

    id: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET
    level: Union[Unset, UserFacingLogLevel] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        message = self.message
        level: Union[Unset, str] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if message is not UNSET:
            field_dict["message"] = message
        if level is not UNSET:
            field_dict["level"] = level
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        message = d.pop("message", UNSET)

        _level = d.pop("level", UNSET)
        level: Union[Unset, UserFacingLogLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = UserFacingLogLevel(_level)

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        user_facing_log = cls(
            id=id,
            message=message,
            level=level,
            created_date=created_date,
        )

        user_facing_log.additional_properties = d
        return user_facing_log

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
