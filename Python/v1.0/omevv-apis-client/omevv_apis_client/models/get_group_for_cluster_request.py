from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGroupForClusterRequest")


@attr.s(auto_attribs=True)
class GetGroupForClusterRequest:
    """
    Attributes:
        clust_ids (Union[Unset, List[str]]): List of cluster IDs.
    """

    clust_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        clust_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.clust_ids, Unset):
            clust_ids = self.clust_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if clust_ids is not UNSET:
            field_dict["clustIds"] = clust_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        clust_ids = cast(List[str], d.pop("clustIds", UNSET))

        get_group_for_cluster_request = cls(
            clust_ids=clust_ids,
        )

        get_group_for_cluster_request.additional_properties = d
        return get_group_for_cluster_request

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
