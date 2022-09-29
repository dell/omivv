from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.drift_compliance_status import DriftComplianceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupComplianceSummaryReport")


@attr.s(auto_attribs=True)
class GroupComplianceSummaryReport:
    """
    Attributes:
        omevvp_group_id (Union[Unset, int]): Group ID associated to the cluster
        status (Union[Unset, DriftComplianceStatus]):
        count_critical_devices (Union[Unset, int]): Count of hosts whose compliance status is critical
        count_warning_devices (Union[Unset, int]): Count of hosts whose compliance status is warning
        count_normal_devices (Union[Unset, int]): Count of hosts whose compliance status is normal
        count_downgraded_devices (Union[Unset, int]): Count of hosts whose firmware version is ahead of baseline
        count_unknown_devices (Union[Unset, int]): Count of hosts whose compliance status is unknown
        count_notapplicable_devices (Union[Unset, int]): Count of hosts whose catalog is not recommended
    """

    omevvp_group_id: Union[Unset, int] = UNSET
    status: Union[Unset, DriftComplianceStatus] = UNSET
    count_critical_devices: Union[Unset, int] = UNSET
    count_warning_devices: Union[Unset, int] = UNSET
    count_normal_devices: Union[Unset, int] = UNSET
    count_downgraded_devices: Union[Unset, int] = UNSET
    count_unknown_devices: Union[Unset, int] = UNSET
    count_notapplicable_devices: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        omevvp_group_id = self.omevvp_group_id
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        count_critical_devices = self.count_critical_devices
        count_warning_devices = self.count_warning_devices
        count_normal_devices = self.count_normal_devices
        count_downgraded_devices = self.count_downgraded_devices
        count_unknown_devices = self.count_unknown_devices
        count_notapplicable_devices = self.count_notapplicable_devices

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if omevvp_group_id is not UNSET:
            field_dict["omevvpGroupId"] = omevvp_group_id
        if status is not UNSET:
            field_dict["status"] = status
        if count_critical_devices is not UNSET:
            field_dict["countCriticalDevices"] = count_critical_devices
        if count_warning_devices is not UNSET:
            field_dict["countWarningDevices"] = count_warning_devices
        if count_normal_devices is not UNSET:
            field_dict["countNormalDevices"] = count_normal_devices
        if count_downgraded_devices is not UNSET:
            field_dict["countDowngradedDevices"] = count_downgraded_devices
        if count_unknown_devices is not UNSET:
            field_dict["countUnknownDevices"] = count_unknown_devices
        if count_notapplicable_devices is not UNSET:
            field_dict["countNotapplicableDevices"] = count_notapplicable_devices

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        omevvp_group_id = d.pop("omevvpGroupId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, DriftComplianceStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DriftComplianceStatus(_status)

        count_critical_devices = d.pop("countCriticalDevices", UNSET)

        count_warning_devices = d.pop("countWarningDevices", UNSET)

        count_normal_devices = d.pop("countNormalDevices", UNSET)

        count_downgraded_devices = d.pop("countDowngradedDevices", UNSET)

        count_unknown_devices = d.pop("countUnknownDevices", UNSET)

        count_notapplicable_devices = d.pop("countNotapplicableDevices", UNSET)

        group_compliance_summary_report = cls(
            omevvp_group_id=omevvp_group_id,
            status=status,
            count_critical_devices=count_critical_devices,
            count_warning_devices=count_warning_devices,
            count_normal_devices=count_normal_devices,
            count_downgraded_devices=count_downgraded_devices,
            count_unknown_devices=count_unknown_devices,
            count_notapplicable_devices=count_notapplicable_devices,
        )

        group_compliance_summary_report.additional_properties = d
        return group_compliance_summary_report

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
