from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.fault_model import FaultModel
from ..models.fault_summary_model import FaultSummaryModel
from ..models.sub_system_health_rollup_status import SubSystemHealthRollupStatus
from ..models.sub_system_health_sub_system import SubSystemHealthSubSystem
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubSystemHealth")


@attr.s(auto_attribs=True)
class SubSystemHealth:
    """
    Attributes:
        sub_system (Union[Unset, SubSystemHealthSubSystem]): Sub system info
        fault_summary_list (Union[Unset, List[FaultSummaryModel]]): Summary list of faults
        rollup_status (Union[Unset, SubSystemHealthRollupStatus]): Sub system rollup status
        fault_list (Union[Unset, List[FaultModel]]): List of faults for the sub system
    """

    sub_system: Union[Unset, SubSystemHealthSubSystem] = UNSET
    fault_summary_list: Union[Unset, List[FaultSummaryModel]] = UNSET
    rollup_status: Union[Unset, SubSystemHealthRollupStatus] = UNSET
    fault_list: Union[Unset, List[FaultModel]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sub_system: Union[Unset, str] = UNSET
        if not isinstance(self.sub_system, Unset):
            sub_system = self.sub_system.value

        fault_summary_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fault_summary_list, Unset):
            fault_summary_list = []
            for fault_summary_list_item_data in self.fault_summary_list:
                fault_summary_list_item = fault_summary_list_item_data.to_dict()

                fault_summary_list.append(fault_summary_list_item)

        rollup_status: Union[Unset, str] = UNSET
        if not isinstance(self.rollup_status, Unset):
            rollup_status = self.rollup_status.value

        fault_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fault_list, Unset):
            fault_list = []
            for fault_list_item_data in self.fault_list:
                fault_list_item = fault_list_item_data.to_dict()

                fault_list.append(fault_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sub_system is not UNSET:
            field_dict["subSystem"] = sub_system
        if fault_summary_list is not UNSET:
            field_dict["faultSummaryList"] = fault_summary_list
        if rollup_status is not UNSET:
            field_dict["rollupStatus"] = rollup_status
        if fault_list is not UNSET:
            field_dict["faultList"] = fault_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _sub_system = d.pop("subSystem", UNSET)
        sub_system: Union[Unset, SubSystemHealthSubSystem]
        if isinstance(_sub_system, Unset):
            sub_system = UNSET
        else:
            sub_system = SubSystemHealthSubSystem(_sub_system)

        fault_summary_list = []
        _fault_summary_list = d.pop("faultSummaryList", UNSET)
        for fault_summary_list_item_data in _fault_summary_list or []:
            fault_summary_list_item = FaultSummaryModel.from_dict(fault_summary_list_item_data)

            fault_summary_list.append(fault_summary_list_item)

        _rollup_status = d.pop("rollupStatus", UNSET)
        rollup_status: Union[Unset, SubSystemHealthRollupStatus]
        if isinstance(_rollup_status, Unset):
            rollup_status = UNSET
        else:
            rollup_status = SubSystemHealthRollupStatus(_rollup_status)

        fault_list = []
        _fault_list = d.pop("faultList", UNSET)
        for fault_list_item_data in _fault_list or []:
            fault_list_item = FaultModel.from_dict(fault_list_item_data)

            fault_list.append(fault_list_item)

        sub_system_health = cls(
            sub_system=sub_system,
            fault_summary_list=fault_summary_list,
            rollup_status=rollup_status,
            fault_list=fault_list,
        )

        sub_system_health.additional_properties = d
        return sub_system_health

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
