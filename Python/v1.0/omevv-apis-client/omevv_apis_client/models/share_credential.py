from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ShareCredential")


@attr.s(auto_attribs=True)
class ShareCredential:
    """Share credential details

    Attributes:
        username (str):
        password (str):
        domain (Union[Unset, str]):
    """

    username: str
    password: str
    domain: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        username = self.username
        password = self.password
        domain = self.domain

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "password": password,
            }
        )
        if domain is not UNSET:
            field_dict["domain"] = domain

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        username = d.pop("username")

        password = d.pop("password")

        domain = d.pop("domain", UNSET)

        share_credential = cls(
            username=username,
            password=password,
            domain=domain,
        )

        share_credential.additional_properties = d
        return share_credential

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
