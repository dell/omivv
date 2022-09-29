from typing import Any, Dict, List, Type, TypeVar, cast

import attr

from ..models.compliance_deviation_compliance import ComplianceDeviationCompliance
from ..models.system_component_base_info import SystemComponentBaseInfo

T = TypeVar("T", bound="ComplianceDeviation")


@attr.s(auto_attribs=True)
class ComplianceDeviation:
    """
    Attributes:
        system_component (SystemComponentBaseInfo):
        compliance (ComplianceDeviationCompliance): Compliance status for the individual system component Example:
            COMPLIANT.
        current_version (str): Current version of the component firmware found during scan Example: 24.1.
        target_version (str): Version of the component firmware specified in desired image Example: 25.0.
        messages (List[str]):
    """

    system_component: SystemComponentBaseInfo
    compliance: ComplianceDeviationCompliance
    current_version: str
    target_version: str
    messages: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        system_component = self.system_component.to_dict()

        compliance = self.compliance.value

        current_version = self.current_version
        target_version = self.target_version
        messages = self.messages

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "systemComponent": system_component,
                "compliance": compliance,
                "currentVersion": current_version,
                "targetVersion": target_version,
                "messages": messages,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        system_component = SystemComponentBaseInfo.from_dict(d.pop("systemComponent"))

        compliance = ComplianceDeviationCompliance(d.pop("compliance"))

        current_version = d.pop("currentVersion")

        target_version = d.pop("targetVersion")

        messages = cast(List[str], d.pop("messages"))

        compliance_deviation = cls(
            system_component=system_component,
            compliance=compliance,
            current_version=current_version,
            target_version=target_version,
            messages=messages,
        )

        compliance_deviation.additional_properties = d
        return compliance_deviation

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
