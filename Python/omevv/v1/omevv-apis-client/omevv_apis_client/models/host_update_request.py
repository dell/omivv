from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.host_update_request_action import HostUpdateRequestAction
from ..models.target_image_info import TargetImageInfo

T = TypeVar("T", bound="HostUpdateRequest")


@attr.s(auto_attribs=True)
class HostUpdateRequest:
    """
    Attributes:
        action (HostUpdateRequestAction): action=UPDATE_PRE_CHECK-check to pre-check, action=STAGE_UPDATE to stage
            update, action=PRE_IMAGE_UPDATE to apply update before image update, action=POST_IMAGE_UPDATE to apply update
            following image update.
        target_package (str): Name of the desired HW support package Example: System Update 2019-07.
        target_package_version (str): Version of the desired HW support package Example: v1.
        target_image (TargetImageInfo):
    """

    action: HostUpdateRequestAction
    target_package: str
    target_package_version: str
    target_image: TargetImageInfo
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action.value

        target_package = self.target_package
        target_package_version = self.target_package_version
        target_image = self.target_image.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "targetPackage": target_package,
                "targetPackageVersion": target_package_version,
                "targetImage": target_image,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action = HostUpdateRequestAction(d.pop("action"))

        target_package = d.pop("targetPackage")

        target_package_version = d.pop("targetPackageVersion")

        target_image = TargetImageInfo.from_dict(d.pop("targetImage"))

        host_update_request = cls(
            action=action,
            target_package=target_package,
            target_package_version=target_package_version,
            target_image=target_image,
        )

        host_update_request.additional_properties = d
        return host_update_request

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
