from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.paging_information import PagingInformation
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupStorageInventoryCollectionModel")


@attr.s(auto_attribs=True)
class GroupStorageInventoryCollectionModel:
    """
    Attributes:
        paging_info (Union[Unset, PagingInformation]): Information provided in paged collection query responses, only
            when the response is partial, meaning that not all queried instances are returned. The return code will be 206
            when this is returned.
        group_storage_inventory_device_model (Union[Unset, Any]):
    """

    paging_info: Union[Unset, PagingInformation] = UNSET
    group_storage_inventory_device_model: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        paging_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.paging_info, Unset):
            paging_info = self.paging_info.to_dict()

        group_storage_inventory_device_model = self.group_storage_inventory_device_model

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if paging_info is not UNSET:
            field_dict["pagingInfo"] = paging_info
        if group_storage_inventory_device_model is not UNSET:
            field_dict["groupStorageInventoryDeviceModel"] = group_storage_inventory_device_model

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _paging_info = d.pop("pagingInfo", UNSET)
        paging_info: Union[Unset, PagingInformation]
        if isinstance(_paging_info, Unset):
            paging_info = UNSET
        else:
            paging_info = PagingInformation.from_dict(_paging_info)

        group_storage_inventory_device_model = d.pop("groupStorageInventoryDeviceModel", UNSET)

        group_storage_inventory_collection_model = cls(
            paging_info=paging_info,
            group_storage_inventory_device_model=group_storage_inventory_device_model,
        )

        group_storage_inventory_collection_model.additional_properties = d
        return group_storage_inventory_collection_model

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
