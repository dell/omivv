from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.hardware_log import HardwareLog
from ..models.paging_information import PagingInformation
from ..types import UNSET, Unset

T = TypeVar("T", bound="HardwareLogResponse")


@attr.s(auto_attribs=True)
class HardwareLogResponse:
    """
    Attributes:
        paging_info (Union[Unset, PagingInformation]): Information provided in paged collection query responses, only
            when the response is partial, meaning that not all queried instances are returned. The return code will be 206
            when this is returned.
        log_messages (Union[Unset, List[HardwareLog]]):
    """

    paging_info: Union[Unset, PagingInformation] = UNSET
    log_messages: Union[Unset, List[HardwareLog]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        paging_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.paging_info, Unset):
            paging_info = self.paging_info.to_dict()

        log_messages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.log_messages, Unset):
            log_messages = []
            for log_messages_item_data in self.log_messages:
                log_messages_item = log_messages_item_data.to_dict()

                log_messages.append(log_messages_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if paging_info is not UNSET:
            field_dict["pagingInfo"] = paging_info
        if log_messages is not UNSET:
            field_dict["logMessages"] = log_messages

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

        log_messages = []
        _log_messages = d.pop("logMessages", UNSET)
        for log_messages_item_data in _log_messages or []:
            log_messages_item = HardwareLog.from_dict(log_messages_item_data)

            log_messages.append(log_messages_item)

        hardware_log_response = cls(
            paging_info=paging_info,
            log_messages=log_messages,
        )

        hardware_log_response.additional_properties = d
        return hardware_log_response

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
