from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.component_compliance import ComponentCompliance
from ..models.host_compliance_report_compliance_status import HostComplianceReportComplianceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="HostComplianceReport")


@attr.s(auto_attribs=True)
class HostComplianceReport:
    """
    Attributes:
        host_id (Union[Unset, int]):
        host_address (Union[Unset, str]):
        service_tag (Union[Unset, str]):
        device_model (Union[Unset, str]):
        compliance_status (Union[Unset, HostComplianceReportComplianceStatus]):
        component_compliances (Union[Unset, List[ComponentCompliance]]):
    """

    host_id: Union[Unset, int] = UNSET
    host_address: Union[Unset, str] = UNSET
    service_tag: Union[Unset, str] = UNSET
    device_model: Union[Unset, str] = UNSET
    compliance_status: Union[Unset, HostComplianceReportComplianceStatus] = UNSET
    component_compliances: Union[Unset, List[ComponentCompliance]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host_id = self.host_id
        host_address = self.host_address
        service_tag = self.service_tag
        device_model = self.device_model
        compliance_status: Union[Unset, str] = UNSET
        if not isinstance(self.compliance_status, Unset):
            compliance_status = self.compliance_status.value

        component_compliances: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.component_compliances, Unset):
            component_compliances = []
            for component_compliances_item_data in self.component_compliances:
                component_compliances_item = component_compliances_item_data.to_dict()

                component_compliances.append(component_compliances_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host_id is not UNSET:
            field_dict["hostId"] = host_id
        if host_address is not UNSET:
            field_dict["hostAddress"] = host_address
        if service_tag is not UNSET:
            field_dict["serviceTag"] = service_tag
        if device_model is not UNSET:
            field_dict["deviceModel"] = device_model
        if compliance_status is not UNSET:
            field_dict["complianceStatus"] = compliance_status
        if component_compliances is not UNSET:
            field_dict["componentCompliances"] = component_compliances

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host_id = d.pop("hostId", UNSET)

        host_address = d.pop("hostAddress", UNSET)

        service_tag = d.pop("serviceTag", UNSET)

        device_model = d.pop("deviceModel", UNSET)

        _compliance_status = d.pop("complianceStatus", UNSET)
        compliance_status: Union[Unset, HostComplianceReportComplianceStatus]
        if isinstance(_compliance_status, Unset):
            compliance_status = UNSET
        else:
            compliance_status = HostComplianceReportComplianceStatus(_compliance_status)

        component_compliances = []
        _component_compliances = d.pop("componentCompliances", UNSET)
        for component_compliances_item_data in _component_compliances or []:
            component_compliances_item = ComponentCompliance.from_dict(component_compliances_item_data)

            component_compliances.append(component_compliances_item)

        host_compliance_report = cls(
            host_id=host_id,
            host_address=host_address,
            service_tag=service_tag,
            device_model=device_model,
            compliance_status=compliance_status,
            component_compliances=component_compliances,
        )

        host_compliance_report.additional_properties = d
        return host_compliance_report

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
