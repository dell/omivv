from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.console_provider_type import ConsoleProviderType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsoleExtensionRequest")


@attr.s(auto_attribs=True)
class ConsoleExtensionRequest:
    """console extension request object for register/unregistering extensions

    Attributes:
        extensions (Union[Unset, List[ConsoleProviderType]]):
    """

    extensions: Union[Unset, List[ConsoleProviderType]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        extensions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = []
            for extensions_item_data in self.extensions:
                extensions_item = extensions_item_data.value

                extensions.append(extensions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extensions is not UNSET:
            field_dict["extensions"] = extensions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        extensions = []
        _extensions = d.pop("extensions", UNSET)
        for extensions_item_data in _extensions or []:
            extensions_item = ConsoleProviderType(extensions_item_data)

            extensions.append(extensions_item)

        console_extension_request = cls(
            extensions=extensions,
        )

        console_extension_request.additional_properties = d
        return console_extension_request

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
