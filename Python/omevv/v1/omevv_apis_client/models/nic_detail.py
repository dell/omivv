from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NICDetail")


@attr.s(auto_attribs=True)
class NICDetail:
    """
    Attributes:
        product_name (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        mac_address (Union[Unset, str]):
        fqdd (Union[Unset, str]):
        link_status (Union[Unset, str]):
    """

    product_name: Union[Unset, str] = UNSET
    manufacturer: Union[Unset, str] = UNSET
    mac_address: Union[Unset, str] = UNSET
    fqdd: Union[Unset, str] = UNSET
    link_status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        product_name = self.product_name
        manufacturer = self.manufacturer
        mac_address = self.mac_address
        fqdd = self.fqdd
        link_status = self.link_status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if mac_address is not UNSET:
            field_dict["macAddress"] = mac_address
        if fqdd is not UNSET:
            field_dict["fqdd"] = fqdd
        if link_status is not UNSET:
            field_dict["linkStatus"] = link_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        product_name = d.pop("productName", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        mac_address = d.pop("macAddress", UNSET)

        fqdd = d.pop("fqdd", UNSET)

        link_status = d.pop("linkStatus", UNSET)

        nic_detail = cls(
            product_name=product_name,
            manufacturer=manufacturer,
            mac_address=mac_address,
            fqdd=fqdd,
            link_status=link_status,
        )

        nic_detail.additional_properties = d
        return nic_detail

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
