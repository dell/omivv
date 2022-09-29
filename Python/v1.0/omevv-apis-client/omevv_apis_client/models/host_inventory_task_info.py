from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.host_inventory_entry import HostInventoryEntry
from ..models.task_info_action import TaskInfoAction
from ..models.task_info_status import TaskInfoStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="HostInventoryTaskInfo")


@attr.s(auto_attribs=True)
class HostInventoryTaskInfo:
    """
    Attributes:
        id (str): Unique ID for task Example: task-24.
        action (TaskInfoAction): Operation that started the task Example: ComplianceScan.
        status (TaskInfoStatus): Status of operation Example: INPROGRESS.
        progress (int): percentage complete of operation (0-100, 100 when task is COMPLETED) Example: 66.
        messages (List[str]):
        host_inventory_list (List[HostInventoryEntry]):
        description (Union[Unset, str]): Name of task Example: host-96 post-image update.
        start_time (Union[Unset, str]): Start time of operation Example: 2019-06-25 22:44:00.801000+00:00.
        estimated_time_remaining (Union[Unset, int]): Estimated time remaining for operation, in seconds Example: 36000.
        hosts (Union[Unset, List[str]]): List of hosts for the task Example: ['host-9', 'host-10', 'host-11'].
        operation_status_code (Union[Unset, int]): Http Status code for the task Example: 200.
    """

    id: str
    action: TaskInfoAction
    status: TaskInfoStatus
    progress: int
    messages: List[str]
    host_inventory_list: List[HostInventoryEntry]
    description: Union[Unset, str] = UNSET
    start_time: Union[Unset, str] = UNSET
    estimated_time_remaining: Union[Unset, int] = UNSET
    hosts: Union[Unset, List[str]] = UNSET
    operation_status_code: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        action = self.action.value

        status = self.status.value

        progress = self.progress
        messages = self.messages

        host_inventory_list = []
        for host_inventory_list_item_data in self.host_inventory_list:
            host_inventory_list_item = host_inventory_list_item_data.to_dict()

            host_inventory_list.append(host_inventory_list_item)

        description = self.description
        start_time = self.start_time
        estimated_time_remaining = self.estimated_time_remaining
        hosts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = self.hosts

        operation_status_code = self.operation_status_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "action": action,
                "status": status,
                "progress": progress,
                "messages": messages,
                "hostInventoryList": host_inventory_list,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if estimated_time_remaining is not UNSET:
            field_dict["estimatedTimeRemaining"] = estimated_time_remaining
        if hosts is not UNSET:
            field_dict["hosts"] = hosts
        if operation_status_code is not UNSET:
            field_dict["operationStatusCode"] = operation_status_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        action = TaskInfoAction(d.pop("action"))

        status = TaskInfoStatus(d.pop("status"))

        progress = d.pop("progress")

        messages = cast(List[str], d.pop("messages"))

        host_inventory_list = []
        _host_inventory_list = d.pop("hostInventoryList")
        for host_inventory_list_item_data in _host_inventory_list:
            host_inventory_list_item = HostInventoryEntry.from_dict(host_inventory_list_item_data)

            host_inventory_list.append(host_inventory_list_item)

        description = d.pop("description", UNSET)

        start_time = d.pop("startTime", UNSET)

        estimated_time_remaining = d.pop("estimatedTimeRemaining", UNSET)

        hosts = cast(List[str], d.pop("hosts", UNSET))

        operation_status_code = d.pop("operationStatusCode", UNSET)

        host_inventory_task_info = cls(
            id=id,
            action=action,
            status=status,
            progress=progress,
            messages=messages,
            host_inventory_list=host_inventory_list,
            description=description,
            start_time=start_time,
            estimated_time_remaining=estimated_time_remaining,
            hosts=hosts,
            operation_status_code=operation_status_code,
        )

        host_inventory_task_info.additional_properties = d
        return host_inventory_task_info

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
