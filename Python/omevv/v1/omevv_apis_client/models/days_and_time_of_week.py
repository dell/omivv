from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DaysAndTimeOfWeek")


@attr.s(auto_attribs=True)
class DaysAndTimeOfWeek:
    """
    Attributes:
        monday (Union[Unset, bool]):
        tuesday (Union[Unset, bool]):
        wednesday (Union[Unset, bool]):
        thursday (Union[Unset, bool]):
        friday (Union[Unset, bool]):
        saturday (Union[Unset, bool]):
        time (Union[Unset, str]):
        sunday (Union[Unset, bool]):
    """

    monday: Union[Unset, bool] = UNSET
    tuesday: Union[Unset, bool] = UNSET
    wednesday: Union[Unset, bool] = UNSET
    thursday: Union[Unset, bool] = UNSET
    friday: Union[Unset, bool] = UNSET
    saturday: Union[Unset, bool] = UNSET
    time: Union[Unset, str] = UNSET
    sunday: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        monday = self.monday
        tuesday = self.tuesday
        wednesday = self.wednesday
        thursday = self.thursday
        friday = self.friday
        saturday = self.saturday
        time = self.time
        sunday = self.sunday

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monday is not UNSET:
            field_dict["monday"] = monday
        if tuesday is not UNSET:
            field_dict["tuesday"] = tuesday
        if wednesday is not UNSET:
            field_dict["wednesday"] = wednesday
        if thursday is not UNSET:
            field_dict["thursday"] = thursday
        if friday is not UNSET:
            field_dict["friday"] = friday
        if saturday is not UNSET:
            field_dict["saturday"] = saturday
        if time is not UNSET:
            field_dict["time"] = time
        if sunday is not UNSET:
            field_dict["sunday"] = sunday

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        monday = d.pop("monday", UNSET)

        tuesday = d.pop("tuesday", UNSET)

        wednesday = d.pop("wednesday", UNSET)

        thursday = d.pop("thursday", UNSET)

        friday = d.pop("friday", UNSET)

        saturday = d.pop("saturday", UNSET)

        time = d.pop("time", UNSET)

        sunday = d.pop("sunday", UNSET)

        days_and_time_of_week = cls(
            monday=monday,
            tuesday=tuesday,
            wednesday=wednesday,
            thursday=thursday,
            friday=friday,
            saturday=saturday,
            time=time,
            sunday=sunday,
        )

        days_and_time_of_week.additional_properties = d
        return days_and_time_of_week

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
