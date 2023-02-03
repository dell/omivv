import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.days_and_time_of_week import DaysAndTimeOfWeek
from ..models.job_execution_history import JobExecutionHistory
from ..models.job_job_type import JobJobType
from ..models.job_state import JobState
from ..models.target_details import TargetDetails
from ..types import UNSET, Unset

T = TypeVar("T", bound="Job")


@attr.s(auto_attribs=True)
class Job:
    """
    Attributes:
        job_id (Union[Unset, int]):
        job_name (Union[Unset, str]):
        job_type (Union[Unset, JobJobType]):
        job_description (Union[Unset, str]):
        job_targets (Union[Unset, List[TargetDetails]]):
        console_id (Union[Unset, str]):
        console_address (Union[Unset, str]):
        schedule (Union[Unset, DaysAndTimeOfWeek]):
        next_run (Union[Unset, datetime.datetime]):
        last_run (Union[Unset, datetime.datetime]):
        enabled (Union[Unset, str]):
        state (Union[Unset, JobState]):
        visible (Union[Unset, bool]):
        editable (Union[Unset, bool]):
        is_internal (Union[Unset, bool]):
        created (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, str]): Unique id of the administrative user responsible for the job.
        collection_size (Union[Unset, int]):
        last_execution_history (Union[Unset, JobExecutionHistory]):
    """

    job_id: Union[Unset, int] = UNSET
    job_name: Union[Unset, str] = UNSET
    job_type: Union[Unset, JobJobType] = UNSET
    job_description: Union[Unset, str] = UNSET
    job_targets: Union[Unset, List[TargetDetails]] = UNSET
    console_id: Union[Unset, str] = UNSET
    console_address: Union[Unset, str] = UNSET
    schedule: Union[Unset, DaysAndTimeOfWeek] = UNSET
    next_run: Union[Unset, datetime.datetime] = UNSET
    last_run: Union[Unset, datetime.datetime] = UNSET
    enabled: Union[Unset, str] = UNSET
    state: Union[Unset, JobState] = UNSET
    visible: Union[Unset, bool] = UNSET
    editable: Union[Unset, bool] = UNSET
    is_internal: Union[Unset, bool] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, str] = UNSET
    collection_size: Union[Unset, int] = UNSET
    last_execution_history: Union[Unset, JobExecutionHistory] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_id = self.job_id
        job_name = self.job_name
        job_type: Union[Unset, str] = UNSET
        if not isinstance(self.job_type, Unset):
            job_type = self.job_type.value

        job_description = self.job_description
        job_targets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.job_targets, Unset):
            job_targets = []
            for job_targets_item_data in self.job_targets:
                job_targets_item = job_targets_item_data.to_dict()

                job_targets.append(job_targets_item)

        console_id = self.console_id
        console_address = self.console_address
        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        next_run: Union[Unset, str] = UNSET
        if not isinstance(self.next_run, Unset):
            next_run = self.next_run.isoformat()

        last_run: Union[Unset, str] = UNSET
        if not isinstance(self.last_run, Unset):
            last_run = self.last_run.isoformat()

        enabled = self.enabled
        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        visible = self.visible
        editable = self.editable
        is_internal = self.is_internal
        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        created_by = self.created_by
        collection_size = self.collection_size
        last_execution_history: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.last_execution_history, Unset):
            last_execution_history = self.last_execution_history.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if job_type is not UNSET:
            field_dict["jobType"] = job_type
        if job_description is not UNSET:
            field_dict["jobDescription"] = job_description
        if job_targets is not UNSET:
            field_dict["jobTargets"] = job_targets
        if console_id is not UNSET:
            field_dict["consoleId"] = console_id
        if console_address is not UNSET:
            field_dict["consoleAddress"] = console_address
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if next_run is not UNSET:
            field_dict["nextRun"] = next_run
        if last_run is not UNSET:
            field_dict["lastRun"] = last_run
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if state is not UNSET:
            field_dict["state"] = state
        if visible is not UNSET:
            field_dict["visible"] = visible
        if editable is not UNSET:
            field_dict["editable"] = editable
        if is_internal is not UNSET:
            field_dict["isInternal"] = is_internal
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if collection_size is not UNSET:
            field_dict["collectionSize"] = collection_size
        if last_execution_history is not UNSET:
            field_dict["lastExecutionHistory"] = last_execution_history

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_id = d.pop("jobId", UNSET)

        job_name = d.pop("jobName", UNSET)

        _job_type = d.pop("jobType", UNSET)
        job_type: Union[Unset, JobJobType]
        if isinstance(_job_type, Unset):
            job_type = UNSET
        else:
            job_type = JobJobType(_job_type)

        job_description = d.pop("jobDescription", UNSET)

        job_targets = []
        _job_targets = d.pop("jobTargets", UNSET)
        for job_targets_item_data in _job_targets or []:
            job_targets_item = TargetDetails.from_dict(job_targets_item_data)

            job_targets.append(job_targets_item)

        console_id = d.pop("consoleId", UNSET)

        console_address = d.pop("consoleAddress", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, DaysAndTimeOfWeek]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = DaysAndTimeOfWeek.from_dict(_schedule)

        _next_run = d.pop("nextRun", UNSET)
        next_run: Union[Unset, datetime.datetime]
        if isinstance(_next_run, Unset):
            next_run = UNSET
        else:  # Added below code to handle when _next_run is none
            if _next_run is None:
                next_run = None
            else:
                next_run = isoparse(_next_run)

        _last_run = d.pop("lastRun", UNSET)
        last_run: Union[Unset, datetime.datetime]
        if isinstance(_last_run, Unset):
            last_run = UNSET
        else:  # Added below code to handle when _last_run is none
            if _last_run is None:
                last_run = None
            else:
                last_run = isoparse(_last_run)


        enabled = d.pop("enabled", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, JobState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = JobState(_state)

        visible = d.pop("visible", UNSET)

        editable = d.pop("editable", UNSET)

        is_internal = d.pop("isInternal", UNSET)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        created_by = d.pop("createdBy", UNSET)

        collection_size = d.pop("collectionSize", UNSET)

        _last_execution_history = d.pop("lastExecutionHistory", UNSET)
        last_execution_history: Union[Unset, JobExecutionHistory]
        if isinstance(_last_execution_history, Unset):
            last_execution_history = UNSET
        else:
            last_execution_history = JobExecutionHistory.from_dict(_last_execution_history)

        job = cls(
            job_id=job_id,
            job_name=job_name,
            job_type=job_type,
            job_description=job_description,
            job_targets=job_targets,
            console_id=console_id,
            console_address=console_address,
            schedule=schedule,
            next_run=next_run,
            last_run=last_run,
            enabled=enabled,
            state=state,
            visible=visible,
            editable=editable,
            is_internal=is_internal,
            created=created,
            created_by=created_by,
            collection_size=collection_size,
            last_execution_history=last_execution_history,
        )

        job.additional_properties = d
        return job

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
