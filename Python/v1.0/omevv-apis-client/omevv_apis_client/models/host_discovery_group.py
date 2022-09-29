from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostDiscoveryGroup")


@attr.s(auto_attribs=True)
class HostDiscoveryGroup:
    """
    Attributes:
        console_entity_i_ds (Union[Unset, List[str]]): List of vCenter entity IDs that need to be discovered
        user_name (Union[Unset, str]): Username of iDRAC
        pass_word (Union[Unset, str]): Password of iDRAC
        use_global_credentials (Union[Unset, bool]): optional
    """

    console_entity_i_ds: Union[Unset, List[str]] = UNSET
    user_name: Union[Unset, str] = UNSET
    pass_word: Union[Unset, str] = UNSET
    use_global_credentials: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        console_entity_i_ds: Union[Unset, List[str]] = UNSET
        if not isinstance(self.console_entity_i_ds, Unset):
            console_entity_i_ds = self.console_entity_i_ds

        user_name = self.user_name
        pass_word = self.pass_word
        use_global_credentials = self.use_global_credentials

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if console_entity_i_ds is not UNSET:
            field_dict["consoleEntityIDs"] = console_entity_i_ds
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if pass_word is not UNSET:
            field_dict["passWord"] = pass_word
        if use_global_credentials is not UNSET:
            field_dict["useGlobalCredentials"] = use_global_credentials

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        console_entity_i_ds = cast(List[str], d.pop("consoleEntityIDs", UNSET))

        user_name = d.pop("userName", UNSET)

        pass_word = d.pop("passWord", UNSET)

        use_global_credentials = d.pop("useGlobalCredentials", UNSET)

        host_discovery_group = cls(
            console_entity_i_ds=console_entity_i_ds,
            user_name=user_name,
            pass_word=pass_word,
            use_global_credentials=use_global_credentials,
        )

        host_discovery_group.additional_properties = d
        return host_discovery_group

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
