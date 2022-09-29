from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RACResponse")


@attr.s(auto_attribs=True)
class RACResponse:
    """
    Attributes:
        ip_address (Union[Unset, str]): display the IP address for the remote access card.
        mac_address (Union[Unset, str]): displays the MAC address for the remote access card.
        url (Union[Unset, str]): displays the live URL for the iDRAC associated with this host.
    """

    ip_address: Union[Unset, str] = UNSET
    mac_address: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ip_address = self.ip_address
        mac_address = self.mac_address
        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ip_address = d.pop("ipAddress", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        url = d.pop("url", UNSET)

        rac_response = cls(
            ip_address=ip_address,
            mac_address=mac_address,
            url=url,
        )

        rac_response.additional_properties = d
        return rac_response

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
