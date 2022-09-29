from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.driver_update_request import DriverUpdateRequest
from ..models.firmware_update_request import FirmwareUpdateRequest
from ..models.schedule import Schedule
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateRequest")


@attr.s(auto_attribs=True)
class UpdateRequest:
    """Update request model.

    Attributes:
        job_name (Union[Unset, str]): Update job name
        job_description (Union[Unset, str]): Update job description
        schedule (Union[Unset, Schedule]): Schedule of request model
        firmware (Union[Unset, FirmwareUpdateRequest]): Firmware update request model.
        driver (Union[Unset, DriverUpdateRequest]):
    """

    job_name: Union[Unset, str] = UNSET
    job_description: Union[Unset, str] = UNSET
    schedule: Union[Unset, Schedule] = UNSET
    firmware: Union[Unset, FirmwareUpdateRequest] = UNSET
    driver: Union[Unset, DriverUpdateRequest] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_name = self.job_name
        job_description = self.job_description
        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        firmware: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.firmware, Unset):
            firmware = self.firmware.to_dict()

        driver: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.driver, Unset):
            driver = self.driver.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if job_description is not UNSET:
            field_dict["jobDescription"] = job_description
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if firmware is not UNSET:
            field_dict["firmware"] = firmware
        if driver is not UNSET:
            field_dict["driver"] = driver

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_name = d.pop("jobName", UNSET)

        job_description = d.pop("jobDescription", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, Schedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = Schedule.from_dict(_schedule)

        _firmware = d.pop("firmware", UNSET)
        firmware: Union[Unset, FirmwareUpdateRequest]
        if isinstance(_firmware, Unset):
            firmware = UNSET
        else:
            firmware = FirmwareUpdateRequest.from_dict(_firmware)

        _driver = d.pop("driver", UNSET)
        driver: Union[Unset, DriverUpdateRequest]
        if isinstance(_driver, Unset):
            driver = UNSET
        else:
            driver = DriverUpdateRequest.from_dict(_driver)

        update_request = cls(
            job_name=job_name,
            job_description=job_description,
            schedule=schedule,
            firmware=firmware,
            driver=driver,
        )

        update_request.additional_properties = d
        return update_request

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
