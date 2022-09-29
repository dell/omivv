from typing import Any, Dict, List, Type, TypeVar, cast

import attr

from ..models.multi_host_request_action import MultiHostRequestAction
from ..models.target_image_info import TargetImageInfo

T = TypeVar("T", bound="MultiHostRequest")


@attr.s(auto_attribs=True)
class MultiHostRequest:
    """
    Attributes:
        action (MultiHostRequestAction): SCAN = report results of compliance scan.
        target_hosts (List[str]): List of hosts to be scanned for compliance Example: ['host-9', 'host-10', 'host-11'].
        target_package (str): The name of the desired FW package Example: System Update 2019-07.
        target_package_version (str): Version of the desired HW support package Example: v1.
        target_image (TargetImageInfo):
    """

    action: MultiHostRequestAction
    target_hosts: List[str]
    target_package: str
    target_package_version: str
    target_image: TargetImageInfo
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action.value

        target_hosts = self.target_hosts

        target_package = self.target_package
        target_package_version = self.target_package_version
        target_image = self.target_image.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "targetHosts": target_hosts,
                "targetPackage": target_package,
                "targetPackageVersion": target_package_version,
                "targetImage": target_image,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action = MultiHostRequestAction(d.pop("action"))

        target_hosts = cast(List[str], d.pop("targetHosts"))

        target_package = d.pop("targetPackage")

        target_package_version = d.pop("targetPackageVersion")

        target_image = TargetImageInfo.from_dict(d.pop("targetImage"))

        multi_host_request = cls(
            action=action,
            target_hosts=target_hosts,
            target_package=target_package,
            target_package_version=target_package_version,
            target_image=target_image,
        )

        multi_host_request.additional_properties = d
        return multi_host_request

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
