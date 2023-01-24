import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.job_execution_status import JobExecutionStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobExecutionHistory")


@attr.s(auto_attribs=True)
class JobExecutionHistory:
    """
    Attributes:
        history_id (Union[Unset, int]):
        start_time (Union[Unset, datetime.datetime]):
        end_time (Union[Unset, datetime.datetime]):
        updated_time (Union[Unset, datetime.datetime]):
        progress (Union[Unset, int]): running progress percentage
        status_summary (Union[Unset, JobExecutionStatus]):
        status_summary_message (Union[Unset, str]):
    """

    history_id: Union[Unset, int] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    end_time: Union[Unset, datetime.datetime] = UNSET
    updated_time: Union[Unset, datetime.datetime] = UNSET
    progress: Union[Unset, int] = UNSET
    status_summary: Union[Unset, JobExecutionStatus] = UNSET
    status_summary_message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        history_id = self.history_id
        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        updated_time: Union[Unset, str] = UNSET
        if not isinstance(self.updated_time, Unset):
            updated_time = self.updated_time.isoformat()

        progress = self.progress
        status_summary: Union[Unset, str] = UNSET
        if not isinstance(self.status_summary, Unset):
            status_summary = self.status_summary.value

        status_summary_message = self.status_summary_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if history_id is not UNSET:
            field_dict["historyId"] = history_id
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if updated_time is not UNSET:
            field_dict["updatedTime"] = updated_time
        if progress is not UNSET:
            field_dict["progress"] = progress
        if status_summary is not UNSET:
            field_dict["statusSummary"] = status_summary
        if status_summary_message is not UNSET:
            field_dict["statusSummaryMessage"] = status_summary_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        history_id = d.pop("historyId", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:  # Added below code to handle when next_is is none
            if _end_time is None:
                end_time = None
            else:
                end_time = isoparse(_end_time)

        _updated_time = d.pop("updatedTime", UNSET)
        updated_time: Union[Unset, datetime.datetime]
        if isinstance(_updated_time, Unset):
            updated_time = UNSET
        else:
            updated_time = isoparse(_updated_time)

        progress = d.pop("progress", UNSET)

        _status_summary = d.pop("statusSummary", UNSET)
        status_summary: Union[Unset, JobExecutionStatus]
        if isinstance(_status_summary, Unset):
            status_summary = UNSET
        else:
            status_summary = JobExecutionStatus(_status_summary)

        status_summary_message = d.pop("statusSummaryMessage", UNSET)

        job_execution_history = cls(
            history_id=history_id,
            start_time=start_time,
            end_time=end_time,
            updated_time=updated_time,
            progress=progress,
            status_summary=status_summary,
            status_summary_message=status_summary_message,
        )

        job_execution_history.additional_properties = d
        return job_execution_history

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
