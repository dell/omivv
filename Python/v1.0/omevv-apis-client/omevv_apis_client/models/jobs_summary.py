from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.jobs_summary_job_type import JobsSummaryJobType
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobsSummary")


@attr.s(auto_attribs=True)
class JobsSummary:
    """
    Attributes:
        job_type (Union[Unset, JobsSummaryJobType]):
        total_jobs (Union[Unset, int]):
        scheduled_jobs (Union[Unset, int]):
        in_progress_jobs (Union[Unset, int]):
        failure_jobs (Union[Unset, int]):
        completed_jobs (Union[Unset, int]):
        cancelled_jobs (Union[Unset, int]):
    """

    job_type: Union[Unset, JobsSummaryJobType] = UNSET
    total_jobs: Union[Unset, int] = UNSET
    scheduled_jobs: Union[Unset, int] = UNSET
    in_progress_jobs: Union[Unset, int] = UNSET
    failure_jobs: Union[Unset, int] = UNSET
    completed_jobs: Union[Unset, int] = UNSET
    cancelled_jobs: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_type: Union[Unset, str] = UNSET
        if not isinstance(self.job_type, Unset):
            job_type = self.job_type.value

        total_jobs = self.total_jobs
        scheduled_jobs = self.scheduled_jobs
        in_progress_jobs = self.in_progress_jobs
        failure_jobs = self.failure_jobs
        completed_jobs = self.completed_jobs
        cancelled_jobs = self.cancelled_jobs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_type is not UNSET:
            field_dict["jobType"] = job_type
        if total_jobs is not UNSET:
            field_dict["totalJobs"] = total_jobs
        if scheduled_jobs is not UNSET:
            field_dict["scheduledJobs"] = scheduled_jobs
        if in_progress_jobs is not UNSET:
            field_dict["inProgressJobs"] = in_progress_jobs
        if failure_jobs is not UNSET:
            field_dict["failureJobs"] = failure_jobs
        if completed_jobs is not UNSET:
            field_dict["completedJobs"] = completed_jobs
        if cancelled_jobs is not UNSET:
            field_dict["cancelledJobs"] = cancelled_jobs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _job_type = d.pop("jobType", UNSET)
        job_type: Union[Unset, JobsSummaryJobType]
        if isinstance(_job_type, Unset):
            job_type = UNSET
        else:
            job_type = JobsSummaryJobType(_job_type)

        total_jobs = d.pop("totalJobs", UNSET)

        scheduled_jobs = d.pop("scheduledJobs", UNSET)

        in_progress_jobs = d.pop("inProgressJobs", UNSET)

        failure_jobs = d.pop("failureJobs", UNSET)

        completed_jobs = d.pop("completedJobs", UNSET)

        cancelled_jobs = d.pop("cancelledJobs", UNSET)

        jobs_summary = cls(
            job_type=job_type,
            total_jobs=total_jobs,
            scheduled_jobs=scheduled_jobs,
            in_progress_jobs=in_progress_jobs,
            failure_jobs=failure_jobs,
            completed_jobs=completed_jobs,
            cancelled_jobs=cancelled_jobs,
        )

        jobs_summary.additional_properties = d
        return jobs_summary

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
