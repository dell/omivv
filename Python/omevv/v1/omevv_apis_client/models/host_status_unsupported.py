from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostStatusUnsupported")


@attr.s(auto_attribs=True)
class HostStatusUnsupported:
    """
    Attributes:
        total_unsupported_count (Union[Unset, int]): This will give overall count of unsupported systems states. There
            might be a case where one system might have more than one unsupported status .
        i_drac_license_un_supported (Union[Unset, int]): Count of un supported iDRAC license systems.
        hypervisor_version_un_supported (Union[Unset, int]): count of unsupported hypervisor versions
    """

    total_unsupported_count: Union[Unset, int] = UNSET
    i_drac_license_un_supported: Union[Unset, int] = UNSET
    hypervisor_version_un_supported: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_unsupported_count = self.total_unsupported_count
        i_drac_license_un_supported = self.i_drac_license_un_supported
        hypervisor_version_un_supported = self.hypervisor_version_un_supported

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_unsupported_count is not UNSET:
            field_dict["totalUnsupportedCount"] = total_unsupported_count
        if i_drac_license_un_supported is not UNSET:
            field_dict["iDRACLicenseUnSupported"] = i_drac_license_un_supported
        if hypervisor_version_un_supported is not UNSET:
            field_dict["hypervisorVersionUnSupported"] = hypervisor_version_un_supported

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_unsupported_count = d.pop("totalUnsupportedCount", UNSET)

        i_drac_license_un_supported = d.pop("iDRACLicenseUnSupported", UNSET)

        hypervisor_version_un_supported = d.pop("hypervisorVersionUnSupported", UNSET)

        host_status_unsupported = cls(
            total_unsupported_count=total_unsupported_count,
            i_drac_license_un_supported=i_drac_license_un_supported,
            hypervisor_version_un_supported=hypervisor_version_un_supported,
        )

        host_status_unsupported.additional_properties = d
        return host_status_unsupported

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
