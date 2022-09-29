from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.system_component_base_info import SystemComponentBaseInfo

T = TypeVar("T", bound="HostInventoryEntry")


@attr.s(auto_attribs=True)
class HostInventoryEntry:
    """
    Attributes:
        system_component (SystemComponentBaseInfo):
        firmware_version (str): Current installed/running version of the component firmware Example: 2.5.1.
    """

    system_component: SystemComponentBaseInfo
    firmware_version: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        system_component = self.system_component.to_dict()

        firmware_version = self.firmware_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "systemComponent": system_component,
                "firmwareVersion": firmware_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        system_component = SystemComponentBaseInfo.from_dict(d.pop("systemComponent"))

        firmware_version = d.pop("firmwareVersion")

        host_inventory_entry = cls(
            system_component=system_component,
            firmware_version=firmware_version,
        )

        host_inventory_entry.additional_properties = d
        return host_inventory_entry

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
