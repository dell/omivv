from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.compliance_deviation import ComplianceDeviation
from ..models.host_compliance_scan_info_fw_compliance import HostComplianceScanInfoFwCompliance
from ..models.host_compliance_scan_info_fw_stage_status import HostComplianceScanInfoFwStageStatus
from ..models.host_compliance_scan_info_internal_integrity import HostComplianceScanInfoInternalIntegrity
from ..models.remediation_impact import RemediationImpact
from ..types import UNSET, Unset

T = TypeVar("T", bound="HostComplianceScanInfo")


@attr.s(auto_attribs=True)
class HostComplianceScanInfo:
    """
    Attributes:
        fw_compliance (HostComplianceScanInfoFwCompliance):  Example: COMPLIANT.
        impact (RemediationImpact):
        messages (List[str]):
        fw_stage_status (Union[Unset, HostComplianceScanInfoFwStageStatus]):  Example: STAGED.
        internal_integrity (Union[Unset, HostComplianceScanInfoInternalIntegrity]):  Example: COMPLIANT.
        deviations (Union[Unset, List[ComplianceDeviation]]):
    """

    fw_compliance: HostComplianceScanInfoFwCompliance
    impact: RemediationImpact
    messages: List[str]
    fw_stage_status: Union[Unset, HostComplianceScanInfoFwStageStatus] = UNSET
    internal_integrity: Union[Unset, HostComplianceScanInfoInternalIntegrity] = UNSET
    deviations: Union[Unset, List[ComplianceDeviation]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fw_compliance = self.fw_compliance.value

        impact = self.impact.to_dict()

        messages = self.messages

        fw_stage_status: Union[Unset, str] = UNSET
        if not isinstance(self.fw_stage_status, Unset):
            fw_stage_status = self.fw_stage_status.value

        internal_integrity: Union[Unset, str] = UNSET
        if not isinstance(self.internal_integrity, Unset):
            internal_integrity = self.internal_integrity.value

        deviations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.deviations, Unset):
            deviations = []
            for deviations_item_data in self.deviations:
                deviations_item = deviations_item_data.to_dict()

                deviations.append(deviations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fwCompliance": fw_compliance,
                "impact": impact,
                "messages": messages,
            }
        )
        if fw_stage_status is not UNSET:
            field_dict["fwStageStatus"] = fw_stage_status
        if internal_integrity is not UNSET:
            field_dict["internalIntegrity"] = internal_integrity
        if deviations is not UNSET:
            field_dict["deviations"] = deviations

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fw_compliance = HostComplianceScanInfoFwCompliance(d.pop("fwCompliance"))

        impact = RemediationImpact.from_dict(d.pop("impact"))

        messages = cast(List[str], d.pop("messages"))

        _fw_stage_status = d.pop("fwStageStatus", UNSET)
        fw_stage_status: Union[Unset, HostComplianceScanInfoFwStageStatus]
        if isinstance(_fw_stage_status, Unset):
            fw_stage_status = UNSET
        else:
            fw_stage_status = HostComplianceScanInfoFwStageStatus(_fw_stage_status)

        _internal_integrity = d.pop("internalIntegrity", UNSET)
        internal_integrity: Union[Unset, HostComplianceScanInfoInternalIntegrity]
        if isinstance(_internal_integrity, Unset):
            internal_integrity = UNSET
        else:
            internal_integrity = HostComplianceScanInfoInternalIntegrity(_internal_integrity)

        deviations = []
        _deviations = d.pop("deviations", UNSET)
        for deviations_item_data in _deviations or []:
            deviations_item = ComplianceDeviation.from_dict(deviations_item_data)

            deviations.append(deviations_item)

        host_compliance_scan_info = cls(
            fw_compliance=fw_compliance,
            impact=impact,
            messages=messages,
            fw_stage_status=fw_stage_status,
            internal_integrity=internal_integrity,
            deviations=deviations,
        )

        host_compliance_scan_info.additional_properties = d
        return host_compliance_scan_info

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
