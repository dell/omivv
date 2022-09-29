from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PagingInformation")


@attr.s(auto_attribs=True)
class PagingInformation:
    """Information provided in paged collection query responses, only when the response is partial, meaning that not all
    queried instances are returned. The return code will be 206 when this is returned.

        Attributes:
            total_instances (Union[Unset, int]): The number of instances in the complete queried collection (not just the
                size of the current response). If the request was filtered, then this is the size of the complete filtered
                collection.
            first (Union[Unset, str]): The URL to fetch the first page of this collection (including filtering and sorting
                parameters).
            last (Union[Unset, str]): The URL to fetch the last page of this collection (including filtering and sorting
                parameters).
            next_ (Union[Unset, str]): The URL to fetch the next page of this collection (including filtering and sorting
                parameters). This will not be returned with the last page of a collection.
            prev (Union[Unset, str]): The URL to fetch the previous page of this collection (including filtering and sorting
                parameters). This will not be returned with the first page of a collection.
    """

    total_instances: Union[Unset, int] = UNSET
    first: Union[Unset, str] = UNSET
    last: Union[Unset, str] = UNSET
    next_: Union[Unset, str] = UNSET
    prev: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        total_instances = self.total_instances
        first = self.first
        last = self.last
        next_ = self.next_
        prev = self.prev

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_instances is not UNSET:
            field_dict["totalInstances"] = total_instances
        if first is not UNSET:
            field_dict["first"] = first
        if last is not UNSET:
            field_dict["last"] = last
        if next_ is not UNSET:
            field_dict["next"] = next_
        if prev is not UNSET:
            field_dict["prev"] = prev

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        total_instances = d.pop("totalInstances", UNSET)

        first = d.pop("first", UNSET)

        last = d.pop("last", UNSET)

        next_ = d.pop("next", UNSET)

        prev = d.pop("prev", UNSET)

        paging_information = cls(
            total_instances=total_instances,
            first=first,
            last=last,
            next_=next_,
            prev=prev,
        )

        paging_information.additional_properties = d
        return paging_information

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
