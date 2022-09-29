from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.memory import Memory
from ..types import UNSET, Unset

T = TypeVar("T", bound="MemoryResponse")


@attr.s(auto_attribs=True)
class MemoryResponse:
    """
    Attributes:
        num_slots_used (Union[Unset, int]):
        num_slots_available (Union[Unset, int]):
        installed_size (Union[Unset, str]):
        memory_list (Union[Unset, List[Memory]]):
    """

    num_slots_used: Union[Unset, int] = UNSET
    num_slots_available: Union[Unset, int] = UNSET
    installed_size: Union[Unset, str] = UNSET
    memory_list: Union[Unset, List[Memory]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        num_slots_used = self.num_slots_used
        num_slots_available = self.num_slots_available
        installed_size = self.installed_size
        memory_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.memory_list, Unset):
            memory_list = []
            for memory_list_item_data in self.memory_list:
                memory_list_item = memory_list_item_data.to_dict()

                memory_list.append(memory_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_slots_used is not UNSET:
            field_dict["numSlotsUsed"] = num_slots_used
        if num_slots_available is not UNSET:
            field_dict["numSlotsAvailable"] = num_slots_available
        if installed_size is not UNSET:
            field_dict["installedSize"] = installed_size
        if memory_list is not UNSET:
            field_dict["memoryList"] = memory_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        num_slots_used = d.pop("numSlotsUsed", UNSET)

        num_slots_available = d.pop("numSlotsAvailable", UNSET)

        installed_size = d.pop("installedSize", UNSET)

        memory_list = []
        _memory_list = d.pop("memoryList", UNSET)
        for memory_list_item_data in _memory_list or []:
            memory_list_item = Memory.from_dict(memory_list_item_data)

            memory_list.append(memory_list_item)

        memory_response = cls(
            num_slots_used=num_slots_used,
            num_slots_available=num_slots_available,
            installed_size=installed_size,
            memory_list=memory_list,
        )

        memory_response.additional_properties = d
        return memory_response

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
