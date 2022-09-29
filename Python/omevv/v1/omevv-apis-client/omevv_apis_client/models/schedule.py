import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

T = TypeVar("T", bound="Schedule")


@attr.s(auto_attribs=True)
class Schedule:
    """Schedule of request model

    Attributes:
        run_now (bool): Should be true, if the job has to run instantly.
        date_time (datetime.datetime): Date and time of the schedule.
    """

    run_now: bool
    date_time: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        run_now = self.run_now
        date_time = self.date_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runNow": run_now,
                "dateTime": date_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        run_now = d.pop("runNow")

        date_time = isoparse(d.pop("dateTime"))

        schedule = cls(
            run_now=run_now,
            date_time=date_time,
        )

        schedule.additional_properties = d
        return schedule

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
