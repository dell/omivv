from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupForCluster")


@attr.s(auto_attribs=True)
class GroupForCluster:
    """
    Attributes:
        group_id (Union[Unset, int]): Id of the group with which given cluster is associated.
        clust_id (Union[Unset, str]): Id of the cluster associated with group.
        console_id (Union[Unset, str]): vCenter console ID given by OMEVV.
    """

    group_id: Union[Unset, int] = UNSET
    clust_id: Union[Unset, str] = UNSET
    console_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_id = self.group_id
        clust_id = self.clust_id
        console_id = self.console_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if clust_id is not UNSET:
            field_dict["clustId"] = clust_id
        if console_id is not UNSET:
            field_dict["consoleId"] = console_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_id = d.pop("groupId", UNSET)

        clust_id = d.pop("clustId", UNSET)

        console_id = d.pop("consoleId", UNSET)

        group_for_cluster = cls(
            group_id=group_id,
            clust_id=clust_id,
            console_id=console_id,
        )

        group_for_cluster.additional_properties = d
        return group_for_cluster

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
