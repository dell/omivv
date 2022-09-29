from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.component_compliance_compliance_status import ComponentComplianceComplianceStatus
from ..models.component_compliance_criticality import ComponentComplianceCriticality
from ..models.component_compliance_update_action import ComponentComplianceUpdateAction
from ..models.drift_compliance_status import DriftComplianceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComponentCompliance")


@attr.s(auto_attribs=True)
class ComponentCompliance:
    """
    Attributes:
        drift_status (Union[Unset, DriftComplianceStatus]):
        component_name (Union[Unset, str]):
        current_value (Union[Unset, str]):
        baseline_value (Union[Unset, str]):
        criticality (Union[Unset, ComponentComplianceCriticality]):
        update_action (Union[Unset, ComponentComplianceUpdateAction]):
        source_name (Union[Unset, str]):
        compliance_status (Union[Unset, ComponentComplianceComplianceStatus]):
        reboot_required (Union[Unset, bool]):
    """

    drift_status: Union[Unset, DriftComplianceStatus] = UNSET
    component_name: Union[Unset, str] = UNSET
    current_value: Union[Unset, str] = UNSET
    baseline_value: Union[Unset, str] = UNSET
    criticality: Union[Unset, ComponentComplianceCriticality] = UNSET
    update_action: Union[Unset, ComponentComplianceUpdateAction] = UNSET
    source_name: Union[Unset, str] = UNSET
    compliance_status: Union[Unset, ComponentComplianceComplianceStatus] = UNSET
    reboot_required: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        drift_status: Union[Unset, str] = UNSET
        if not isinstance(self.drift_status, Unset):
            drift_status = self.drift_status.value

        component_name = self.component_name
        current_value = self.current_value
        baseline_value = self.baseline_value
        criticality: Union[Unset, str] = UNSET
        if not isinstance(self.criticality, Unset):
            criticality = self.criticality.value

        update_action: Union[Unset, str] = UNSET
        if not isinstance(self.update_action, Unset):
            update_action = self.update_action.value

        source_name = self.source_name
        compliance_status: Union[Unset, str] = UNSET
        if not isinstance(self.compliance_status, Unset):
            compliance_status = self.compliance_status.value

        reboot_required = self.reboot_required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if drift_status is not UNSET:
            field_dict["driftStatus"] = drift_status
        if component_name is not UNSET:
            field_dict["componentName"] = component_name
        if current_value is not UNSET:
            field_dict["currentValue"] = current_value
        if baseline_value is not UNSET:
            field_dict["baselineValue"] = baseline_value
        if criticality is not UNSET:
            field_dict["criticality"] = criticality
        if update_action is not UNSET:
            field_dict["updateAction"] = update_action
        if source_name is not UNSET:
            field_dict["sourceName"] = source_name
        if compliance_status is not UNSET:
            field_dict["complianceStatus"] = compliance_status
        if reboot_required is not UNSET:
            field_dict["rebootRequired"] = reboot_required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _drift_status = d.pop("driftStatus", UNSET)
        drift_status: Union[Unset, DriftComplianceStatus]
        if isinstance(_drift_status, Unset):
            drift_status = UNSET
        else:
            drift_status = DriftComplianceStatus(_drift_status)

        component_name = d.pop("componentName", UNSET)

        current_value = d.pop("currentValue", UNSET)

        baseline_value = d.pop("baselineValue", UNSET)

        _criticality = d.pop("criticality", UNSET)
        criticality: Union[Unset, ComponentComplianceCriticality]
        if isinstance(_criticality, Unset):
            criticality = UNSET
        else:
            criticality = ComponentComplianceCriticality(_criticality)

        _update_action = d.pop("updateAction", UNSET)
        update_action: Union[Unset, ComponentComplianceUpdateAction]
        if isinstance(_update_action, Unset):
            update_action = UNSET
        else:
            update_action = ComponentComplianceUpdateAction(_update_action)

        source_name = d.pop("sourceName", UNSET)

        _compliance_status = d.pop("complianceStatus", UNSET)
        compliance_status: Union[Unset, ComponentComplianceComplianceStatus]
        if isinstance(_compliance_status, Unset):
            compliance_status = UNSET
        else:
            compliance_status = ComponentComplianceComplianceStatus(_compliance_status)

        reboot_required = d.pop("rebootRequired", UNSET)

        component_compliance = cls(
            drift_status=drift_status,
            component_name=component_name,
            current_value=current_value,
            baseline_value=baseline_value,
            criticality=criticality,
            update_action=update_action,
            source_name=source_name,
            compliance_status=compliance_status,
            reboot_required=reboot_required,
        )

        component_compliance.additional_properties = d
        return component_compliance

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
