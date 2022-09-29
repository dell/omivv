from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.days_and_time_of_week import DaysAndTimeOfWeek
from ..types import UNSET, Unset

T = TypeVar("T", bound="BaselineProfileModifyRequest")


@attr.s(auto_attribs=True)
class BaselineProfileModifyRequest:
    """
    Attributes:
        description (Union[Unset, str]): Description for the baseline profile.
        modified_by (Union[Unset, str]): Modified user, if not provided it is OMEVV by default
        firmware_repo_id (Union[Unset, int]): Firmware repository ID to associate the baseline profile.
        driver_repo_id (Union[Unset, int]):
        configuration_repo_id (Union[Unset, int]):
        addgroup_ids (Union[Unset, List[int]]):
        remove_group_ids (Union[Unset, List[int]]):
        job_schedule (Union[Unset, DaysAndTimeOfWeek]):
    """

    description: Union[Unset, str] = UNSET
    modified_by: Union[Unset, str] = UNSET
    firmware_repo_id: Union[Unset, int] = UNSET
    driver_repo_id: Union[Unset, int] = UNSET
    configuration_repo_id: Union[Unset, int] = UNSET
    addgroup_ids: Union[Unset, List[int]] = UNSET
    remove_group_ids: Union[Unset, List[int]] = UNSET
    job_schedule: Union[Unset, DaysAndTimeOfWeek] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        modified_by = self.modified_by
        firmware_repo_id = self.firmware_repo_id
        driver_repo_id = self.driver_repo_id
        configuration_repo_id = self.configuration_repo_id
        addgroup_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.addgroup_ids, Unset):
            addgroup_ids = self.addgroup_ids

        remove_group_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.remove_group_ids, Unset):
            remove_group_ids = self.remove_group_ids

        job_schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.job_schedule, Unset):
            job_schedule = self.job_schedule.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if firmware_repo_id is not UNSET:
            field_dict["firmwareRepoId"] = firmware_repo_id
        if driver_repo_id is not UNSET:
            field_dict["driverRepoId"] = driver_repo_id
        if configuration_repo_id is not UNSET:
            field_dict["configurationRepoId"] = configuration_repo_id
        if addgroup_ids is not UNSET:
            field_dict["addgroupIds"] = addgroup_ids
        if remove_group_ids is not UNSET:
            field_dict["removeGroupIds"] = remove_group_ids
        if job_schedule is not UNSET:
            field_dict["jobSchedule"] = job_schedule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        modified_by = d.pop("modifiedBy", UNSET)

        firmware_repo_id = d.pop("firmwareRepoId", UNSET)

        driver_repo_id = d.pop("driverRepoId", UNSET)

        configuration_repo_id = d.pop("configurationRepoId", UNSET)

        addgroup_ids = cast(List[int], d.pop("addgroupIds", UNSET))

        remove_group_ids = cast(List[int], d.pop("removeGroupIds", UNSET))

        _job_schedule = d.pop("jobSchedule", UNSET)
        job_schedule: Union[Unset, DaysAndTimeOfWeek]
        if isinstance(_job_schedule, Unset):
            job_schedule = UNSET
        else:
            job_schedule = DaysAndTimeOfWeek.from_dict(_job_schedule)

        baseline_profile_modify_request = cls(
            description=description,
            modified_by=modified_by,
            firmware_repo_id=firmware_repo_id,
            driver_repo_id=driver_repo_id,
            configuration_repo_id=configuration_repo_id,
            addgroup_ids=addgroup_ids,
            remove_group_ids=remove_group_ids,
            job_schedule=job_schedule,
        )

        baseline_profile_modify_request.additional_properties = d
        return baseline_profile_modify_request

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
