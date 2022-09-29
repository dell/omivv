from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.error_response_response_type import ErrorResponseResponseType
from ..models.transient_indication import TransientIndication
from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorResponse")


@attr.s(auto_attribs=True)
class ErrorResponse:
    """
    Attributes:
        messages (List[str]):
        response_type (ErrorResponseResponseType):
        transient_indication (Union[Unset, TransientIndication]):
    """

    messages: List[str]
    response_type: ErrorResponseResponseType
    transient_indication: Union[Unset, TransientIndication] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        messages = self.messages

        response_type = self.response_type.value

        transient_indication: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.transient_indication, Unset):
            transient_indication = self.transient_indication.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "messages": messages,
                "responseType": response_type,
            }
        )
        if transient_indication is not UNSET:
            field_dict["transientIndication"] = transient_indication

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        messages = cast(List[str], d.pop("messages"))

        response_type = ErrorResponseResponseType(d.pop("responseType"))

        _transient_indication = d.pop("transientIndication", UNSET)
        transient_indication: Union[Unset, TransientIndication]
        if isinstance(_transient_indication, Unset):
            transient_indication = UNSET
        else:
            transient_indication = TransientIndication.from_dict(_transient_indication)

        error_response = cls(
            messages=messages,
            response_type=response_type,
            transient_indication=transient_indication,
        )

        error_response.additional_properties = d
        return error_response

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
