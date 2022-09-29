from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.host_discovery_group import HostDiscoveryGroup
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateHostsDiscoverRequest")


@attr.s(auto_attribs=True)
class CreateHostsDiscoverRequest:
    """
    Attributes:
        job_name (Union[Unset, str]): Name of the job
        job_description (Union[Unset, str]):
        host_discovery_groups (Union[Unset, List[HostDiscoveryGroup]]):
    """

    job_name: Union[Unset, str] = UNSET
    job_description: Union[Unset, str] = UNSET
    host_discovery_groups: Union[Unset, List[HostDiscoveryGroup]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_name = self.job_name
        job_description = self.job_description
        host_discovery_groups: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.host_discovery_groups, Unset):
            host_discovery_groups = []
            for host_discovery_groups_item_data in self.host_discovery_groups:
                host_discovery_groups_item = host_discovery_groups_item_data.to_dict()

                host_discovery_groups.append(host_discovery_groups_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_name is not UNSET:
            field_dict["jobName"] = job_name
        if job_description is not UNSET:
            field_dict["jobDescription"] = job_description
        if host_discovery_groups is not UNSET:
            field_dict["hostDiscoveryGroups"] = host_discovery_groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_name = d.pop("jobName", UNSET)

        job_description = d.pop("jobDescription", UNSET)

        host_discovery_groups = []
        _host_discovery_groups = d.pop("hostDiscoveryGroups", UNSET)
        for host_discovery_groups_item_data in _host_discovery_groups or []:
            host_discovery_groups_item = HostDiscoveryGroup.from_dict(host_discovery_groups_item_data)

            host_discovery_groups.append(host_discovery_groups_item)

        create_hosts_discover_request = cls(
            job_name=job_name,
            job_description=job_description,
            host_discovery_groups=host_discovery_groups,
        )

        create_hosts_discover_request.additional_properties = d
        return create_hosts_discover_request

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
