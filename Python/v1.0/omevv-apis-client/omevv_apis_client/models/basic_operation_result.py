from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BasicOperationResult")


@attr.s(auto_attribs=True)
class BasicOperationResult:
    """
    Attributes:
        messages (List[str]):
        operation_status_code (Union[Unset, int]): Http Status code for the task Example: 200.
    """

    messages: List[str]
    operation_status_code: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        messages = self.messages

        operation_status_code = self.operation_status_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messages": messages,
            }
        )
        if operation_status_code is not UNSET:
            field_dict["operationStatusCode"] = operation_status_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        messages = cast(List[str], d.pop("messages"))

        operation_status_code = d.pop("operationStatusCode", UNSET)

        basic_operation_result = cls(
            messages=messages,
            operation_status_code=operation_status_code,
        )

        basic_operation_result.additional_properties = d
        return basic_operation_result

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
