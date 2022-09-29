from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.console_provider_type import ConsoleProviderType
from ..models.credential import Credential
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsoleCreateRequest")


@attr.s(auto_attribs=True)
class ConsoleCreateRequest:
    """
    Attributes:
        extensions (List[ConsoleProviderType]):
        credential (Credential):
        console_address (Union[Unset, str]): name or ipaddress or fqdn of the vCenter console
        description (Union[Unset, str]):
    """

    extensions: List[ConsoleProviderType]
    credential: Credential
    console_address: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        extensions = []
        for extensions_item_data in self.extensions:
            extensions_item = extensions_item_data.value

            extensions.append(extensions_item)

        credential = self.credential.to_dict()

        console_address = self.console_address
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "extensions": extensions,
                "credential": credential,
            }
        )
        if console_address is not UNSET:
            field_dict["consoleAddress"] = console_address
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        extensions = []
        _extensions = d.pop("extensions")
        for extensions_item_data in _extensions:
            extensions_item = ConsoleProviderType(extensions_item_data)

            extensions.append(extensions_item)

        credential = Credential.from_dict(d.pop("credential"))

        console_address = d.pop("consoleAddress", UNSET)

        description = d.pop("description", UNSET)

        console_create_request = cls(
            extensions=extensions,
            credential=credential,
            console_address=console_address,
            description=description,
        )

        console_create_request.additional_properties = d
        return console_create_request

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
