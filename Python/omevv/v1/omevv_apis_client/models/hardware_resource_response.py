from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="HardwareResourceResponse")


@attr.s(auto_attribs=True)
class HardwareResourceResponse:
    """
    Attributes:
        cpu_count (Union[Unset, int]):
        virtual_disk_size (Union[Unset, str]):
        total_energy_conumption (Union[Unset, str]):
        total_memory (Union[Unset, str]):
    """

    cpu_count: Union[Unset, int] = UNSET
    virtual_disk_size: Union[Unset, str] = UNSET
    total_energy_conumption: Union[Unset, str] = UNSET
    total_memory: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cpu_count = self.cpu_count
        virtual_disk_size = self.virtual_disk_size
        total_energy_conumption = self.total_energy_conumption
        total_memory = self.total_memory

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpu_count is not UNSET:
            field_dict["cpuCount"] = cpu_count
        if virtual_disk_size is not UNSET:
            field_dict["virtualDiskSize"] = virtual_disk_size
        if total_energy_conumption is not UNSET:
            field_dict["totalEnergyConumption"] = total_energy_conumption
        if total_memory is not UNSET:
            field_dict["totalMemory"] = total_memory

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cpu_count = d.pop("cpuCount", UNSET)

        virtual_disk_size = d.pop("virtualDiskSize", UNSET)

        total_energy_conumption = d.pop("totalEnergyConumption", UNSET)

        total_memory = d.pop("totalMemory", UNSET)

        hardware_resource_response = cls(
            cpu_count=cpu_count,
            virtual_disk_size=virtual_disk_size,
            total_energy_conumption=total_energy_conumption,
            total_memory=total_memory,
        )

        hardware_resource_response.additional_properties = d
        return hardware_resource_response

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
