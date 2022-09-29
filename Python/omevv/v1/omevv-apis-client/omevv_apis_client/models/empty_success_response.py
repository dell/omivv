from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="EmptySuccessResponse")


@attr.s(auto_attribs=True)
class EmptySuccessResponse:
    """
    Attributes:
        messages (List[str]):
    """

    messages: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        messages = self.messages

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messages": messages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        messages = cast(List[str], d.pop("messages"))

        empty_success_response = cls(
            messages=messages,
        )

        empty_success_response.additional_properties = d
        return empty_success_response

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
