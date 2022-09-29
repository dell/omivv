from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="HostFirmwareComponents")


@attr.s(auto_attribs=True)
class HostFirmwareComponents:
    """Host firmware components to update.

    Attributes:
        id (int): ID of target to update
        firmwarecomponents (List[str]): List of host firmware components to update.
    """

    id: int
    firmwarecomponents: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        firmwarecomponents = self.firmwarecomponents

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "firmwarecomponents": firmwarecomponents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        firmwarecomponents = cast(List[str], d.pop("firmwarecomponents"))

        host_firmware_components = cls(
            id=id,
            firmwarecomponents=firmwarecomponents,
        )

        host_firmware_components.additional_properties = d
        return host_firmware_components

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
