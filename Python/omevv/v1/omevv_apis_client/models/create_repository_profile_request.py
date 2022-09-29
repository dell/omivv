from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.profile_type import ProfileType
from ..models.protocol_type import ProtocolType
from ..models.share_credential import ShareCredential
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateRepositoryProfileRequest")


@attr.s(auto_attribs=True)
class CreateRepositoryProfileRequest:
    """Model for creating the repository profile

    Attributes:
        profile_name (str): name of the repository profile
        protocol_type (ProtocolType): type of protocol
        share_path (str): Provide the share path of catalog
        description (Union[Unset, str]):
        profile_type (Union[Unset, ProfileType]):
        check_certificate (Union[Unset, bool]):
        share_credential (Union[Unset, ShareCredential]): Share credential details
        created_by (Union[Unset, str]): Provide the createdby user
    """

    profile_name: str
    protocol_type: ProtocolType
    share_path: str
    description: Union[Unset, str] = UNSET
    profile_type: Union[Unset, ProfileType] = UNSET
    check_certificate: Union[Unset, bool] = UNSET
    share_credential: Union[Unset, ShareCredential] = UNSET
    created_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        profile_name = self.profile_name
        protocol_type = self.protocol_type.value

        share_path = self.share_path
        description = self.description
        profile_type: Union[Unset, str] = UNSET
        if not isinstance(self.profile_type, Unset):
            profile_type = self.profile_type.value

        check_certificate = self.check_certificate
        share_credential: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.share_credential, Unset):
            share_credential = self.share_credential.to_dict()

        created_by = self.created_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "profileName": profile_name,
                "protocolType": protocol_type,
                "sharePath": share_path,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if profile_type is not UNSET:
            field_dict["profileType"] = profile_type
        if check_certificate is not UNSET:
            field_dict["checkCertificate"] = check_certificate
        if share_credential is not UNSET:
            field_dict["shareCredential"] = share_credential
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        profile_name = d.pop("profileName")

        protocol_type = ProtocolType(d.pop("protocolType"))

        share_path = d.pop("sharePath")

        description = d.pop("description", UNSET)

        _profile_type = d.pop("profileType", UNSET)
        profile_type: Union[Unset, ProfileType]
        if isinstance(_profile_type, Unset):
            profile_type = UNSET
        else:
            profile_type = ProfileType(_profile_type)

        check_certificate = d.pop("checkCertificate", UNSET)

        _share_credential = d.pop("shareCredential", UNSET)
        share_credential: Union[Unset, ShareCredential]
        if isinstance(_share_credential, Unset):
            share_credential = UNSET
        else:
            share_credential = ShareCredential.from_dict(_share_credential)

        created_by = d.pop("createdBy", UNSET)

        create_repository_profile_request = cls(
            profile_name=profile_name,
            protocol_type=protocol_type,
            share_path=share_path,
            description=description,
            profile_type=profile_type,
            check_certificate=check_certificate,
            share_credential=share_credential,
            created_by=created_by,
        )

        create_repository_profile_request.additional_properties = d
        return create_repository_profile_request

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
