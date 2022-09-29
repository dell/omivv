from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.share_credential import ShareCredential
from ..types import UNSET, Unset

T = TypeVar("T", bound="ModifyRepositoryProfileRequest")


@attr.s(auto_attribs=True)
class ModifyRepositoryProfileRequest:
    """Model having repository details

    Attributes:
        profile_name (Union[Unset, str]): name of the repository profile
        description (Union[Unset, str]):
        share_path (Union[Unset, str]): Provide the share path of catalog
        modified_by (Union[Unset, str]): Provide the modifiedby user
        share_credential (Union[Unset, ShareCredential]): Share credential details
    """

    profile_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    share_path: Union[Unset, str] = UNSET
    modified_by: Union[Unset, str] = UNSET
    share_credential: Union[Unset, ShareCredential] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        profile_name = self.profile_name
        description = self.description
        share_path = self.share_path
        modified_by = self.modified_by
        share_credential: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.share_credential, Unset):
            share_credential = self.share_credential.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if profile_name is not UNSET:
            field_dict["profileName"] = profile_name
        if description is not UNSET:
            field_dict["description"] = description
        if share_path is not UNSET:
            field_dict["sharePath"] = share_path
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if share_credential is not UNSET:
            field_dict["shareCredential"] = share_credential

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        profile_name = d.pop("profileName", UNSET)

        description = d.pop("description", UNSET)

        share_path = d.pop("sharePath", UNSET)

        modified_by = d.pop("modifiedBy", UNSET)

        _share_credential = d.pop("shareCredential", UNSET)
        share_credential: Union[Unset, ShareCredential]
        if isinstance(_share_credential, Unset):
            share_credential = UNSET
        else:
            share_credential = ShareCredential.from_dict(_share_credential)

        modify_repository_profile_request = cls(
            profile_name=profile_name,
            description=description,
            share_path=share_path,
            modified_by=modified_by,
            share_credential=share_credential,
        )

        modify_repository_profile_request.additional_properties = d
        return modify_repository_profile_request

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
