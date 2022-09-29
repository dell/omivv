from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SupportedReleaseManifest")


@attr.s(auto_attribs=True)
class SupportedReleaseManifest:
    """
    Attributes:
        release (str): vSphere release version supported Example: 7.1.0-1.
        manifest (Union[Unset, str]): name of the manifest for specified vSphere release Example:
            systemupdate-2019-07-manifest.
        manifest_version (Union[Unset, str]): version of the manifest for specified vSphere release Example: v7.0.
    """

    release: str
    manifest: Union[Unset, str] = UNSET
    manifest_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        release = self.release
        manifest = self.manifest
        manifest_version = self.manifest_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "release": release,
            }
        )
        if manifest is not UNSET:
            field_dict["manifest"] = manifest
        if manifest_version is not UNSET:
            field_dict["manifestVersion"] = manifest_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        release = d.pop("release")

        manifest = d.pop("manifest", UNSET)

        manifest_version = d.pop("manifestVersion", UNSET)

        supported_release_manifest = cls(
            release=release,
            manifest=manifest,
            manifest_version=manifest_version,
        )

        supported_release_manifest.additional_properties = d
        return supported_release_manifest

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
