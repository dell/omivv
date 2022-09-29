from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.supported_release_manifest import SupportedReleaseManifest

T = TypeVar("T", bound="PackageInfo")


@attr.s(auto_attribs=True)
class PackageInfo:
    """
    Attributes:
        name (str): name of the HW support package for display in UI Example: System Update 2019-07.
        description (str): expanded description of the HW support package Example: July 20, 2018 Update, recommended for
            all systems.
        version (str): version of the HW support package Example: 2.5.
        supported_releases (List[SupportedReleaseManifest]):
    """

    name: str
    description: str
    version: str
    supported_releases: List[SupportedReleaseManifest]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        version = self.version
        supported_releases = []
        for supported_releases_item_data in self.supported_releases:
            supported_releases_item = supported_releases_item_data.to_dict()

            supported_releases.append(supported_releases_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "version": version,
                "supportedReleases": supported_releases,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        description = d.pop("description")

        version = d.pop("version")

        supported_releases = []
        _supported_releases = d.pop("supportedReleases")
        for supported_releases_item_data in _supported_releases:
            supported_releases_item = SupportedReleaseManifest.from_dict(supported_releases_item_data)

            supported_releases.append(supported_releases_item)

        package_info = cls(
            name=name,
            description=description,
            version=version,
            supported_releases=supported_releases,
        )

        package_info.additional_properties = d
        return package_info

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
