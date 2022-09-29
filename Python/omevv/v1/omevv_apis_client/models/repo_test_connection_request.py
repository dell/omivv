from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.protocol_type import ProtocolType
from ..models.share_credential import ShareCredential
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepoTestConnectionRequest")


@attr.s(auto_attribs=True)
class RepoTestConnectionRequest:
    """Model for test connection

    Attributes:
        protocol_type (ProtocolType): type of protocol
        catalog_path (str): share path of the catalog
        share_credential (Union[Unset, ShareCredential]): Share credential details
        check_certificate (Union[Unset, bool]): select if certificate check is required
    """

    protocol_type: ProtocolType
    catalog_path: str
    share_credential: Union[Unset, ShareCredential] = UNSET
    check_certificate: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        protocol_type = self.protocol_type.value

        catalog_path = self.catalog_path
        share_credential: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.share_credential, Unset):
            share_credential = self.share_credential.to_dict()

        check_certificate = self.check_certificate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "protocolType": protocol_type,
                "catalogPath": catalog_path,
            }
        )
        if share_credential is not UNSET:
            field_dict["shareCredential"] = share_credential
        if check_certificate is not UNSET:
            field_dict["checkCertificate"] = check_certificate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        protocol_type = ProtocolType(d.pop("protocolType"))

        catalog_path = d.pop("catalogPath")

        _share_credential = d.pop("shareCredential", UNSET)
        share_credential: Union[Unset, ShareCredential]
        if isinstance(_share_credential, Unset):
            share_credential = UNSET
        else:
            share_credential = ShareCredential.from_dict(_share_credential)

        check_certificate = d.pop("checkCertificate", UNSET)

        repo_test_connection_request = cls(
            protocol_type=protocol_type,
            catalog_path=catalog_path,
            share_credential=share_credential,
            check_certificate=check_certificate,
        )

        repo_test_connection_request.additional_properties = d
        return repo_test_connection_request

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
