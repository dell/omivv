from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.console_provider_type import ConsoleProviderType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Console")


@attr.s(auto_attribs=True)
class Console:
    """
    Attributes:
        uuid (Union[Unset, str]): universal unique identifier(UUID) for the vCenter
        console_address (Union[Unset, str]): console address for the vCenter
        description (Union[Unset, str]):
        registered_extensions (Union[Unset, List[ConsoleProviderType]]):
    """

    uuid: Union[Unset, str] = UNSET
    console_address: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    registered_extensions: Union[Unset, List[ConsoleProviderType]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        console_address = self.console_address
        description = self.description
        registered_extensions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.registered_extensions, Unset):
            registered_extensions = []
            for registered_extensions_item_data in self.registered_extensions:
                registered_extensions_item = registered_extensions_item_data.value

                registered_extensions.append(registered_extensions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if console_address is not UNSET:
            field_dict["consoleAddress"] = console_address
        if description is not UNSET:
            field_dict["description"] = description
        if registered_extensions is not UNSET:
            field_dict["registeredExtensions"] = registered_extensions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid", UNSET)

        console_address = d.pop("consoleAddress", UNSET)

        description = d.pop("description", UNSET)

        registered_extensions = []
        _registered_extensions = d.pop("registeredExtensions", UNSET)
        for registered_extensions_item_data in _registered_extensions or []:
            registered_extensions_item = ConsoleProviderType(registered_extensions_item_data)

            registered_extensions.append(registered_extensions_item)

        console = cls(
            uuid=uuid,
            console_address=console_address,
            description=description,
            registered_extensions=registered_extensions,
        )

        console.additional_properties = d
        return console

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
