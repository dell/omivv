from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterInfo")


@attr.s(auto_attribs=True)
class ClusterInfo:
    """
    Attributes:
        cluster_id (Union[Unset, str]):
        cluster_name (Union[Unset, str]):
        group_id (Union[Unset, int]):
    """

    cluster_id: Union[Unset, str] = UNSET
    cluster_name: Union[Unset, str] = UNSET
    group_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cluster_id = self.cluster_id
        cluster_name = self.cluster_name
        group_id = self.group_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster_id is not UNSET:
            field_dict["clusterID"] = cluster_id
        if cluster_name is not UNSET:
            field_dict["clusterName"] = cluster_name
        if group_id is not UNSET:
            field_dict["groupID"] = group_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cluster_id = d.pop("clusterID", UNSET)

        cluster_name = d.pop("clusterName", UNSET)

        group_id = d.pop("groupID", UNSET)

        cluster_info = cls(
            cluster_id=cluster_id,
            cluster_name=cluster_name,
            group_id=group_id,
        )

        cluster_info.additional_properties = d
        return cluster_info

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
