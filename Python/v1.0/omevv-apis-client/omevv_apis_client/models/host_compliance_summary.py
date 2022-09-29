from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.host_status_non_compliant import HostStatusNonCompliant
from ..models.host_status_unsupported import HostStatusUnsupported
from ..types import UNSET, Unset

T = TypeVar("T", bound="HostComplianceSummary")


@attr.s(auto_attribs=True)
class HostComplianceSummary:
    """
    Attributes:
        host_status_undiscovered (Union[Unset, int]): count of System states that are discovered in OMEVV but not yet in
            OME.
        host_status_unknown (Union[Unset, int]): count of initial states of Systems
        host_status_noncompliant (Union[Unset, HostStatusNonCompliant]):
        host_status_compliant (Union[Unset, int]): count of systems that are snmp configured, iDRAC license supported &
            iDARC Firmware supported
        host_status_unsupported (Union[Unset, HostStatusUnsupported]):
        snmp_status_configured (Union[Unset, int]): count of snmp configured systems
        i_drac_status_licensesupported (Union[Unset, int]): count of license supported.
        hypervisor_version_supported (Union[Unset, int]): count of hypervisor version supported
    """

    host_status_undiscovered: Union[Unset, int] = UNSET
    host_status_unknown: Union[Unset, int] = UNSET
    host_status_noncompliant: Union[Unset, HostStatusNonCompliant] = UNSET
    host_status_compliant: Union[Unset, int] = UNSET
    host_status_unsupported: Union[Unset, HostStatusUnsupported] = UNSET
    snmp_status_configured: Union[Unset, int] = UNSET
    i_drac_status_licensesupported: Union[Unset, int] = UNSET
    hypervisor_version_supported: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host_status_undiscovered = self.host_status_undiscovered
        host_status_unknown = self.host_status_unknown
        host_status_noncompliant: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.host_status_noncompliant, Unset):
            host_status_noncompliant = self.host_status_noncompliant.to_dict()

        host_status_compliant = self.host_status_compliant
        host_status_unsupported: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.host_status_unsupported, Unset):
            host_status_unsupported = self.host_status_unsupported.to_dict()

        snmp_status_configured = self.snmp_status_configured
        i_drac_status_licensesupported = self.i_drac_status_licensesupported
        hypervisor_version_supported = self.hypervisor_version_supported

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host_status_undiscovered is not UNSET:
            field_dict["hostStatus_UNDISCOVERED"] = host_status_undiscovered
        if host_status_unknown is not UNSET:
            field_dict["hostStatus_UNKNOWN"] = host_status_unknown
        if host_status_noncompliant is not UNSET:
            field_dict["hostStatus_NONCOMPLIANT"] = host_status_noncompliant
        if host_status_compliant is not UNSET:
            field_dict["hostStatus_COMPLIANT"] = host_status_compliant
        if host_status_unsupported is not UNSET:
            field_dict["hostStatus_UNSUPPORTED"] = host_status_unsupported
        if snmp_status_configured is not UNSET:
            field_dict["snmpStatus_CONFIGURED"] = snmp_status_configured
        if i_drac_status_licensesupported is not UNSET:
            field_dict["iDRACStatus_LICENSESUPPORTED"] = i_drac_status_licensesupported
        if hypervisor_version_supported is not UNSET:
            field_dict["hypervisorVersion_Supported"] = hypervisor_version_supported

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host_status_undiscovered = d.pop("hostStatus_UNDISCOVERED", UNSET)

        host_status_unknown = d.pop("hostStatus_UNKNOWN", UNSET)

        _host_status_noncompliant = d.pop("hostStatus_NONCOMPLIANT", UNSET)
        host_status_noncompliant: Union[Unset, HostStatusNonCompliant]
        if isinstance(_host_status_noncompliant, Unset):
            host_status_noncompliant = UNSET
        else:
            host_status_noncompliant = HostStatusNonCompliant.from_dict(_host_status_noncompliant)

        host_status_compliant = d.pop("hostStatus_COMPLIANT", UNSET)

        _host_status_unsupported = d.pop("hostStatus_UNSUPPORTED", UNSET)
        host_status_unsupported: Union[Unset, HostStatusUnsupported]
        if isinstance(_host_status_unsupported, Unset):
            host_status_unsupported = UNSET
        else:
            host_status_unsupported = HostStatusUnsupported.from_dict(_host_status_unsupported)

        snmp_status_configured = d.pop("snmpStatus_CONFIGURED", UNSET)

        i_drac_status_licensesupported = d.pop("iDRACStatus_LICENSESUPPORTED", UNSET)

        hypervisor_version_supported = d.pop("hypervisorVersion_Supported", UNSET)

        host_compliance_summary = cls(
            host_status_undiscovered=host_status_undiscovered,
            host_status_unknown=host_status_unknown,
            host_status_noncompliant=host_status_noncompliant,
            host_status_compliant=host_status_compliant,
            host_status_unsupported=host_status_unsupported,
            snmp_status_configured=snmp_status_configured,
            i_drac_status_licensesupported=i_drac_status_licensesupported,
            hypervisor_version_supported=hypervisor_version_supported,
        )

        host_compliance_summary.additional_properties = d
        return host_compliance_summary

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
