import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="HostWarrantyDetail")


@attr.s(auto_attribs=True)
class HostWarrantyDetail:
    """
    Attributes:
        service_level_code (Union[Unset, str]):
        service_level_description (Union[Unset, str]):
        state (Union[Unset, str]):
        status (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        days_remaining (Union[Unset, int]):
        last_run (Union[Unset, datetime.datetime]):
    """

    service_level_code: Union[Unset, str] = UNSET
    service_level_description: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    days_remaining: Union[Unset, int] = UNSET
    last_run: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        service_level_code = self.service_level_code
        service_level_description = self.service_level_description
        state = self.state
        status = self.status
        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        days_remaining = self.days_remaining
        last_run: Union[Unset, str] = UNSET
        if not isinstance(self.last_run, Unset):
            last_run = self.last_run.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_level_code is not UNSET:
            field_dict["serviceLevelCode"] = service_level_code
        if service_level_description is not UNSET:
            field_dict["serviceLevelDescription"] = service_level_description
        if state is not UNSET:
            field_dict["state"] = state
        if status is not UNSET:
            field_dict["status"] = status
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if days_remaining is not UNSET:
            field_dict["daysRemaining"] = days_remaining
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        service_level_code = d.pop("serviceLevelCode", UNSET)

        service_level_description = d.pop("serviceLevelDescription", UNSET)

        state = d.pop("state", UNSET)

        status = d.pop("status", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        days_remaining = d.pop("daysRemaining", UNSET)

        _last_run = d.pop("lastRun", UNSET)
        last_run: Union[Unset, datetime.datetime]
        if isinstance(_last_run, Unset):
            last_run = UNSET
        else:
            last_run = isoparse(_last_run)

        host_warranty_detail = cls(
            service_level_code=service_level_code,
            service_level_description=service_level_description,
            state=state,
            status=status,
            start_date=start_date,
            end_date=end_date,
            days_remaining=days_remaining,
            last_run=last_run,
        )

        host_warranty_detail.additional_properties = d
        return host_warranty_detail

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
