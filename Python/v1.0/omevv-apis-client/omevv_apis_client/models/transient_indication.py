from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransientIndication")


@attr.s(auto_attribs=True)
class TransientIndication:
    """
    Attributes:
        is_transient (Union[Unset, bool]): This field indicates whether or not an error is transient.
    """

    is_transient: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_transient = self.is_transient

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_transient is not UNSET:
            field_dict["isTransient"] = is_transient

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        is_transient = d.pop("isTransient", UNSET)

        transient_indication = cls(
            is_transient=is_transient,
        )

        transient_indication.additional_properties = d
        return transient_indication

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
