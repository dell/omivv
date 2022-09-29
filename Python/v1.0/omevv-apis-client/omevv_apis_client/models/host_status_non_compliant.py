from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostStatusNonCompliant")


@attr.s(auto_attribs=True)
class HostStatusNonCompliant:
    """
    Attributes:
        total_non_compliant_count (Union[Unset, int]): This will give overall count of non-compliance systems states.
            There might be a case where one system might have more than one non compliant status.
        snmp_status_unconfigured (Union[Unset, int]): This represents the count f snmp un-configured.
    """

    total_non_compliant_count: Union[Unset, int] = UNSET
    snmp_status_unconfigured: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_non_compliant_count = self.total_non_compliant_count
        snmp_status_unconfigured = self.snmp_status_unconfigured

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_non_compliant_count is not UNSET:
            field_dict["totalNonCompliantCount"] = total_non_compliant_count
        if snmp_status_unconfigured is not UNSET:
            field_dict["snmpStatus_UNCONFIGURED"] = snmp_status_unconfigured

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_non_compliant_count = d.pop("totalNonCompliantCount", UNSET)

        snmp_status_unconfigured = d.pop("snmpStatus_UNCONFIGURED", UNSET)

        host_status_non_compliant = cls(
            total_non_compliant_count=total_non_compliant_count,
            snmp_status_unconfigured=snmp_status_unconfigured,
        )

        host_status_non_compliant.additional_properties = d
        return host_status_non_compliant

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
