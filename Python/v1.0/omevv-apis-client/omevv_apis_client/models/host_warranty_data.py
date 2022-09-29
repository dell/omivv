from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.host_warranty_data_overall_status import HostWarrantyDataOverallStatus
from ..models.host_warranty_detail import HostWarrantyDetail
from ..types import UNSET, Unset

T = TypeVar("T", bound="HostWarrantyData")


@attr.s(auto_attribs=True)
class HostWarrantyData:
    """
    Attributes:
        device_id (Union[Unset, int]):
        service_tag (Union[Unset, str]):
        device_name (Union[Unset, str]):
        overall_status (Union[Unset, HostWarrantyDataOverallStatus]):
        warranty_details (Union[Unset, List[HostWarrantyDetail]]):
    """

    device_id: Union[Unset, int] = UNSET
    service_tag: Union[Unset, str] = UNSET
    device_name: Union[Unset, str] = UNSET
    overall_status: Union[Unset, HostWarrantyDataOverallStatus] = UNSET
    warranty_details: Union[Unset, List[HostWarrantyDetail]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        device_id = self.device_id
        service_tag = self.service_tag
        device_name = self.device_name
        overall_status: Union[Unset, str] = UNSET
        if not isinstance(self.overall_status, Unset):
            overall_status = self.overall_status.value

        warranty_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warranty_details, Unset):
            warranty_details = []
            for warranty_details_item_data in self.warranty_details:
                warranty_details_item = warranty_details_item_data.to_dict()

                warranty_details.append(warranty_details_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if service_tag is not UNSET:
            field_dict["serviceTag"] = service_tag
        if device_name is not UNSET:
            field_dict["deviceName"] = device_name
        if overall_status is not UNSET:
            field_dict["overallStatus"] = overall_status
        if warranty_details is not UNSET:
            field_dict["warrantyDetails"] = warranty_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        device_id = d.pop("deviceId", UNSET)

        service_tag = d.pop("serviceTag", UNSET)

        device_name = d.pop("deviceName", UNSET)

        _overall_status = d.pop("overallStatus", UNSET)
        overall_status: Union[Unset, HostWarrantyDataOverallStatus]
        if isinstance(_overall_status, Unset):
            overall_status = UNSET
        else:
            overall_status = HostWarrantyDataOverallStatus(_overall_status)

        warranty_details = []
        _warranty_details = d.pop("warrantyDetails", UNSET)
        for warranty_details_item_data in _warranty_details or []:
            warranty_details_item = HostWarrantyDetail.from_dict(warranty_details_item_data)

            warranty_details.append(warranty_details_item)

        host_warranty_data = cls(
            device_id=device_id,
            service_tag=service_tag,
            device_name=device_name,
            overall_status=overall_status,
            warranty_details=warranty_details,
        )

        host_warranty_data.additional_properties = d
        return host_warranty_data

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
