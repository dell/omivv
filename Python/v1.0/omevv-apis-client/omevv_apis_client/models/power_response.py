from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PowerResponse")


@attr.s(auto_attribs=True)
class PowerResponse:
    """
    Attributes:
        peak_power (Union[Unset, str]):
        peak_power_start_time_stamp (Union[Unset, str]):
        peak_power_end_time_stamp (Union[Unset, str]):
        peak_power_unit (Union[Unset, str]):
        system_energy_consumption (Union[Unset, str]):
        system_energy_consumption_start_time_stamp (Union[Unset, str]):
        system_energy_consumption_end_time_stamp (Union[Unset, str]):
        system_energy_consumption_unit (Union[Unset, str]):
        instantaneous_headroom (Union[Unset, str]):
        instantaneous_headroom_unit (Union[Unset, str]):
        peak_headroom (Union[Unset, str]):
        peak_headroom_unit (Union[Unset, str]):
    """

    peak_power: Union[Unset, str] = UNSET
    peak_power_start_time_stamp: Union[Unset, str] = UNSET
    peak_power_end_time_stamp: Union[Unset, str] = UNSET
    peak_power_unit: Union[Unset, str] = UNSET
    system_energy_consumption: Union[Unset, str] = UNSET
    system_energy_consumption_start_time_stamp: Union[Unset, str] = UNSET
    system_energy_consumption_end_time_stamp: Union[Unset, str] = UNSET
    system_energy_consumption_unit: Union[Unset, str] = UNSET
    instantaneous_headroom: Union[Unset, str] = UNSET
    instantaneous_headroom_unit: Union[Unset, str] = UNSET
    peak_headroom: Union[Unset, str] = UNSET
    peak_headroom_unit: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        peak_power = self.peak_power
        peak_power_start_time_stamp = self.peak_power_start_time_stamp
        peak_power_end_time_stamp = self.peak_power_end_time_stamp
        peak_power_unit = self.peak_power_unit
        system_energy_consumption = self.system_energy_consumption
        system_energy_consumption_start_time_stamp = self.system_energy_consumption_start_time_stamp
        system_energy_consumption_end_time_stamp = self.system_energy_consumption_end_time_stamp
        system_energy_consumption_unit = self.system_energy_consumption_unit
        instantaneous_headroom = self.instantaneous_headroom
        instantaneous_headroom_unit = self.instantaneous_headroom_unit
        peak_headroom = self.peak_headroom
        peak_headroom_unit = self.peak_headroom_unit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if peak_power is not UNSET:
            field_dict["peakPower"] = peak_power
        if peak_power_start_time_stamp is not UNSET:
            field_dict["peakPowerStartTimeStamp"] = peak_power_start_time_stamp
        if peak_power_end_time_stamp is not UNSET:
            field_dict["peakPowerEndTimeStamp"] = peak_power_end_time_stamp
        if peak_power_unit is not UNSET:
            field_dict["peakPowerUnit"] = peak_power_unit
        if system_energy_consumption is not UNSET:
            field_dict["systemEnergyConsumption"] = system_energy_consumption
        if system_energy_consumption_start_time_stamp is not UNSET:
            field_dict["systemEnergyConsumptionStartTimeStamp"] = system_energy_consumption_start_time_stamp
        if system_energy_consumption_end_time_stamp is not UNSET:
            field_dict["systemEnergyConsumptionEndTimeStamp"] = system_energy_consumption_end_time_stamp
        if system_energy_consumption_unit is not UNSET:
            field_dict["systemEnergyConsumptionUnit"] = system_energy_consumption_unit
        if instantaneous_headroom is not UNSET:
            field_dict["instantaneousHeadroom"] = instantaneous_headroom
        if instantaneous_headroom_unit is not UNSET:
            field_dict["instantaneousHeadroomUnit"] = instantaneous_headroom_unit
        if peak_headroom is not UNSET:
            field_dict["peakHeadroom"] = peak_headroom
        if peak_headroom_unit is not UNSET:
            field_dict["peakHeadroomUnit"] = peak_headroom_unit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        peak_power = d.pop("peakPower", UNSET)

        peak_power_start_time_stamp = d.pop("peakPowerStartTimeStamp", UNSET)

        peak_power_end_time_stamp = d.pop("peakPowerEndTimeStamp", UNSET)

        peak_power_unit = d.pop("peakPowerUnit", UNSET)

        system_energy_consumption = d.pop("systemEnergyConsumption", UNSET)

        system_energy_consumption_start_time_stamp = d.pop("systemEnergyConsumptionStartTimeStamp", UNSET)

        system_energy_consumption_end_time_stamp = d.pop("systemEnergyConsumptionEndTimeStamp", UNSET)

        system_energy_consumption_unit = d.pop("systemEnergyConsumptionUnit", UNSET)

        instantaneous_headroom = d.pop("instantaneousHeadroom", UNSET)

        instantaneous_headroom_unit = d.pop("instantaneousHeadroomUnit", UNSET)

        peak_headroom = d.pop("peakHeadroom", UNSET)

        peak_headroom_unit = d.pop("peakHeadroomUnit", UNSET)

        power_response = cls(
            peak_power=peak_power,
            peak_power_start_time_stamp=peak_power_start_time_stamp,
            peak_power_end_time_stamp=peak_power_end_time_stamp,
            peak_power_unit=peak_power_unit,
            system_energy_consumption=system_energy_consumption,
            system_energy_consumption_start_time_stamp=system_energy_consumption_start_time_stamp,
            system_energy_consumption_end_time_stamp=system_energy_consumption_end_time_stamp,
            system_energy_consumption_unit=system_energy_consumption_unit,
            instantaneous_headroom=instantaneous_headroom,
            instantaneous_headroom_unit=instantaneous_headroom_unit,
            peak_headroom=peak_headroom,
            peak_headroom_unit=peak_headroom_unit,
        )

        power_response.additional_properties = d
        return power_response

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
