from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorObject")


@attr.s(auto_attribs=True)
class ErrorObject:
    """
    Attributes:
        error_code (Union[Unset, str]): custom defined error codes
        message (Union[Unset, str]): message indiciating the error or exception.
    """

    error_code: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_code = self.error_code
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_code = d.pop("errorCode", UNSET)

        message = d.pop("message", UNSET)

        error_object = cls(
            error_code=error_code,
            message=message,
        )

        error_object.additional_properties = d
        return error_object

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
