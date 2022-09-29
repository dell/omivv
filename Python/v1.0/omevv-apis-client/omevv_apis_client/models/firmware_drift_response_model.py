from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.drift_compliance_status import DriftComplianceStatus
from ..models.host_compliance_report import HostComplianceReport
from ..types import UNSET, Unset

T = TypeVar("T", bound="FirmwareDriftResponseModel")


@attr.s(auto_attribs=True)
class FirmwareDriftResponseModel:
    """
    Attributes:
        compliance_status (Union[Unset, DriftComplianceStatus]):
        host_compliance_reports (Union[Unset, List[HostComplianceReport]]):
    """

    compliance_status: Union[Unset, DriftComplianceStatus] = UNSET
    host_compliance_reports: Union[Unset, List[HostComplianceReport]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compliance_status: Union[Unset, str] = UNSET
        if not isinstance(self.compliance_status, Unset):
            compliance_status = self.compliance_status.value

        host_compliance_reports: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.host_compliance_reports, Unset):
            host_compliance_reports = []
            for host_compliance_reports_item_data in self.host_compliance_reports:
                host_compliance_reports_item = host_compliance_reports_item_data.to_dict()

                host_compliance_reports.append(host_compliance_reports_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compliance_status is not UNSET:
            field_dict["complianceStatus"] = compliance_status
        if host_compliance_reports is not UNSET:
            field_dict["hostComplianceReports"] = host_compliance_reports

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _compliance_status = d.pop("complianceStatus", UNSET)
        compliance_status: Union[Unset, DriftComplianceStatus]
        if isinstance(_compliance_status, Unset):
            compliance_status = UNSET
        else:
            compliance_status = DriftComplianceStatus(_compliance_status)

        host_compliance_reports = []
        _host_compliance_reports = d.pop("hostComplianceReports", UNSET)
        for host_compliance_reports_item_data in _host_compliance_reports or []:
            host_compliance_reports_item = HostComplianceReport.from_dict(host_compliance_reports_item_data)

            host_compliance_reports.append(host_compliance_reports_item)

        firmware_drift_response_model = cls(
            compliance_status=compliance_status,
            host_compliance_reports=host_compliance_reports,
        )

        firmware_drift_response_model.additional_properties = d
        return firmware_drift_response_model

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
