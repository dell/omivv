from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.target_image_info_sw_components import TargetImageInfoSwComponents
from ..types import UNSET, Unset

T = TypeVar("T", bound="TargetImageInfo")


@attr.s(auto_attribs=True)
class TargetImageInfo:
    """
    Attributes:
        base_image_version (str): Version string of image base system Example: 7.0.0-1.0.
        sw_components (TargetImageInfoSwComponents): map of the SW component name to SW Component version
        add_on_name (Union[Unset, str]): Name of Add-on in target image Example: Frobozz Customizations.
        add_on_version (Union[Unset, str]): Version of Add-on in target image Example: 2.1.
    """

    base_image_version: str
    sw_components: TargetImageInfoSwComponents
    add_on_name: Union[Unset, str] = UNSET
    add_on_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        base_image_version = self.base_image_version
        sw_components = self.sw_components.to_dict()

        add_on_name = self.add_on_name
        add_on_version = self.add_on_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "baseImageVersion": base_image_version,
                "swComponents": sw_components,
            }
        )
        if add_on_name is not UNSET:
            field_dict["addOnName"] = add_on_name
        if add_on_version is not UNSET:
            field_dict["addOnVersion"] = add_on_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        base_image_version = d.pop("baseImageVersion")

        sw_components = TargetImageInfoSwComponents.from_dict(d.pop("swComponents"))

        add_on_name = d.pop("addOnName", UNSET)

        add_on_version = d.pop("addOnVersion", UNSET)

        target_image_info = cls(
            base_image_version=base_image_version,
            sw_components=sw_components,
            add_on_name=add_on_name,
            add_on_version=add_on_version,
        )

        target_image_info.additional_properties = d
        return target_image_info

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
