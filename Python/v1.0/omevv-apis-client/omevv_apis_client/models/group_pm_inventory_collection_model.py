from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.paging_information import PagingInformation
from ..models.power_response import PowerResponse
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupPMInventoryCollectionModel")


@attr.s(auto_attribs=True)
class GroupPMInventoryCollectionModel:
    """
    Attributes:
        group_power_response_list (Union[Unset, List[PowerResponse]]):
        paging_info (Union[Unset, PagingInformation]): Information provided in paged collection query responses, only
            when the response is partial, meaning that not all queried instances are returned. The return code will be 206
            when this is returned.
    """

    group_power_response_list: Union[Unset, List[PowerResponse]] = UNSET
    paging_info: Union[Unset, PagingInformation] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_power_response_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.group_power_response_list, Unset):
            group_power_response_list = []
            for group_power_response_list_item_data in self.group_power_response_list:
                group_power_response_list_item = group_power_response_list_item_data.to_dict()

                group_power_response_list.append(group_power_response_list_item)

        paging_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.paging_info, Unset):
            paging_info = self.paging_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_power_response_list is not UNSET:
            field_dict["groupPowerResponseList"] = group_power_response_list
        if paging_info is not UNSET:
            field_dict["pagingInfo"] = paging_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_power_response_list = []
        _group_power_response_list = d.pop("groupPowerResponseList", UNSET)
        for group_power_response_list_item_data in _group_power_response_list or []:
            group_power_response_list_item = PowerResponse.from_dict(group_power_response_list_item_data)

            group_power_response_list.append(group_power_response_list_item)

        _paging_info = d.pop("pagingInfo", UNSET)
        paging_info: Union[Unset, PagingInformation]
        if isinstance(_paging_info, Unset):
            paging_info = UNSET
        else:
            paging_info = PagingInformation.from_dict(_paging_info)

        group_pm_inventory_collection_model = cls(
            group_power_response_list=group_power_response_list,
            paging_info=paging_info,
        )

        group_pm_inventory_collection_model.additional_properties = d
        return group_pm_inventory_collection_model

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
