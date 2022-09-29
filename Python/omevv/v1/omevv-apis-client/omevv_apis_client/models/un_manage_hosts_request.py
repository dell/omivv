from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnManageHostsRequest")


@attr.s(auto_attribs=True)
class UnManageHostsRequest:
    """
    Attributes:
        host_i_ds (List[int]): List of vCenter host-IDs associated with unmanage host job.
        job_name (str): Name of the unmanage host job.
        job_description (Union[Unset, str]): Description of the unmanage host job
    """

    host_i_ds: List[int]
    job_name: str
    job_description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host_i_ds = self.host_i_ds

        job_name = self.job_name
        job_description = self.job_description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hostIDs": host_i_ds,
                "jobName": job_name,
            }
        )
        if job_description is not UNSET:
            field_dict["jobDescription"] = job_description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host_i_ds = cast(List[int], d.pop("hostIDs"))

        job_name = d.pop("jobName")

        job_description = d.pop("jobDescription", UNSET)

        un_manage_hosts_request = cls(
            host_i_ds=host_i_ds,
            job_name=job_name,
            job_description=job_description,
        )

        un_manage_hosts_request.additional_properties = d
        return un_manage_hosts_request

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
