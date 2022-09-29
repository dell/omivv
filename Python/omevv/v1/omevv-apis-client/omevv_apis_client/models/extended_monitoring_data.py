from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtendedMonitoringData")


@attr.s(auto_attribs=True)
class ExtendedMonitoringData:
    """
    Attributes:
        extended_monitoring_enabled (Union[Unset, bool]): Flag for enabling/disabling extended monitoring.
        snmp_trap_monitoring_enabled (Union[Unset, bool]): Flag for enabling/disabling SNMP trap monitoring.
    """

    extended_monitoring_enabled: Union[Unset, bool] = UNSET
    snmp_trap_monitoring_enabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        extended_monitoring_enabled = self.extended_monitoring_enabled
        snmp_trap_monitoring_enabled = self.snmp_trap_monitoring_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if extended_monitoring_enabled is not UNSET:
            field_dict["extendedMonitoringEnabled"] = extended_monitoring_enabled
        if snmp_trap_monitoring_enabled is not UNSET:
            field_dict["SNMPTrapMonitoringEnabled"] = snmp_trap_monitoring_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        extended_monitoring_enabled = d.pop("extendedMonitoringEnabled", UNSET)

        snmp_trap_monitoring_enabled = d.pop("SNMPTrapMonitoringEnabled", UNSET)

        extended_monitoring_data = cls(
            extended_monitoring_enabled=extended_monitoring_enabled,
            snmp_trap_monitoring_enabled=snmp_trap_monitoring_enabled,
        )

        extended_monitoring_data.additional_properties = d
        return extended_monitoring_data

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
