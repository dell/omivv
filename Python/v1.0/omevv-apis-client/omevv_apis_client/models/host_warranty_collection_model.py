from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.host_warranty_data import HostWarrantyData
from ..models.paging_information import PagingInformation
from ..types import UNSET, Unset

T = TypeVar("T", bound="HostWarrantyCollectionModel")


@attr.s(auto_attribs=True)
class HostWarrantyCollectionModel:
    """
    Attributes:
        paging_info (Union[Unset, PagingInformation]): Information provided in paged collection query responses, only
            when the response is partial, meaning that not all queried instances are returned. The return code will be 206
            when this is returned.
        warranty_data (Union[Unset, List[HostWarrantyData]]):
    """

    paging_info: Union[Unset, PagingInformation] = UNSET
    warranty_data: Union[Unset, List[HostWarrantyData]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        paging_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.paging_info, Unset):
            paging_info = self.paging_info.to_dict()

        warranty_data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warranty_data, Unset):
            warranty_data = []
            for warranty_data_item_data in self.warranty_data:
                warranty_data_item = warranty_data_item_data.to_dict()

                warranty_data.append(warranty_data_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if paging_info is not UNSET:
            field_dict["pagingInfo"] = paging_info
        if warranty_data is not UNSET:
            field_dict["warrantyData"] = warranty_data

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

        warranty_data = []
        _warranty_data = d.pop("warrantyData", UNSET)
        for warranty_data_item_data in _warranty_data or []:
            warranty_data_item = HostWarrantyData.from_dict(warranty_data_item_data)

            warranty_data.append(warranty_data_item)

        host_warranty_collection_model = cls(
            paging_info=paging_info,
            warranty_data=warranty_data,
        )

        host_warranty_collection_model.additional_properties = d
        return host_warranty_collection_model

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
