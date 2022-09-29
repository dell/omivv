from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ManagedHostConsole")


@attr.s(auto_attribs=True)
class ManagedHostConsole:
    """
    Attributes:
        console (Union[Unset, str]):
        count (Union[Unset, int]):
    """

    console: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        console = self.console
        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if console is not UNSET:
            field_dict["console"] = console
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        console = d.pop("console", UNSET)

        count = d.pop("count", UNSET)

        managed_host_console = cls(
            console=console,
            count=count,
        )

        managed_host_console.additional_properties = d
        return managed_host_console

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
