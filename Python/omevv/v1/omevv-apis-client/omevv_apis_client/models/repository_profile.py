import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.factory_type import FactoryType
from ..models.profile_type import ProfileType
from ..models.protocol_type import ProtocolType
from ..models.repository_profile_status import RepositoryProfileStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepositoryProfile")


@attr.s(auto_attribs=True)
class RepositoryProfile:
    """Model having repository details

    Attributes:
        id (int):
        profile_name (str): name of the repository profile
        description (str):
        profile_type (ProfileType):
        share_path (str): share path of catalog
        status (RepositoryProfileStatus):
        factory_type (FactoryType): whether the catalog is internal(omevv created) or external(user created)
        file_name (Union[Unset, str]): name of the catalog file
        factory_created (Union[Unset, bool]): whether the catalog is internal(omevv created) or external(user created)
        catalog_created_date (Union[Unset, datetime.datetime]): Date when catalog is created
        catalog_last_checked (Union[Unset, datetime.datetime]): Date when catalog got modified
        check_certificate (Union[Unset, bool]):
        protocol_type (Union[Unset, ProtocolType]): type of protocol
        created_by (Union[Unset, str]): CreatedBy can be vsphere user or omevv
    """

    id: int
    profile_name: str
    description: str
    profile_type: ProfileType
    share_path: str
    status: RepositoryProfileStatus
    factory_type: FactoryType
    file_name: Union[Unset, str] = UNSET
    factory_created: Union[Unset, bool] = UNSET
    catalog_created_date: Union[Unset, datetime.datetime] = UNSET
    catalog_last_checked: Union[Unset, datetime.datetime] = UNSET
    check_certificate: Union[Unset, bool] = UNSET
    protocol_type: Union[Unset, ProtocolType] = UNSET
    created_by: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        profile_name = self.profile_name
        description = self.description
        profile_type = self.profile_type.value

        share_path = self.share_path
        status = self.status.value

        factory_type = self.factory_type.value

        file_name = self.file_name
        factory_created = self.factory_created
        catalog_created_date: Union[Unset, str] = UNSET
        if not isinstance(self.catalog_created_date, Unset):
            catalog_created_date = self.catalog_created_date.isoformat()

        catalog_last_checked: Union[Unset, str] = UNSET
        if not isinstance(self.catalog_last_checked, Unset):
            catalog_last_checked = self.catalog_last_checked.isoformat()

        check_certificate = self.check_certificate
        protocol_type: Union[Unset, str] = UNSET
        if not isinstance(self.protocol_type, Unset):
            protocol_type = self.protocol_type.value

        created_by = self.created_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "profileName": profile_name,
                "description": description,
                "profileType": profile_type,
                "sharePath": share_path,
                "status": status,
                "factoryType": factory_type,
            }
        )
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if factory_created is not UNSET:
            field_dict["factoryCreated"] = factory_created
        if catalog_created_date is not UNSET:
            field_dict["catalogCreatedDate"] = catalog_created_date
        if catalog_last_checked is not UNSET:
            field_dict["catalogLastChecked"] = catalog_last_checked
        if check_certificate is not UNSET:
            field_dict["checkCertificate"] = check_certificate
        if protocol_type is not UNSET:
            field_dict["protocolType"] = protocol_type
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        profile_name = d.pop("profileName")

        description = d.pop("description")

        profile_type = ProfileType(d.pop("profileType"))

        share_path = d.pop("sharePath")

        status = RepositoryProfileStatus(d.pop("status"))

        factory_type = FactoryType(d.pop("factoryType"))

        file_name = d.pop("fileName", UNSET)

        factory_created = d.pop("factoryCreated", UNSET)

        _catalog_created_date = d.pop("catalogCreatedDate", UNSET)
        catalog_created_date: Union[Unset, datetime.datetime]
        if isinstance(_catalog_created_date, Unset):
            catalog_created_date = UNSET
        else:
            catalog_created_date = isoparse(_catalog_created_date)

        _catalog_last_checked = d.pop("catalogLastChecked", UNSET)
        catalog_last_checked: Union[Unset, datetime.datetime]
        if isinstance(_catalog_last_checked, Unset):
            catalog_last_checked = UNSET
        else:
            catalog_last_checked = isoparse(_catalog_last_checked)

        check_certificate = d.pop("checkCertificate", UNSET)

        _protocol_type = d.pop("protocolType", UNSET)
        protocol_type: Union[Unset, ProtocolType]
        if isinstance(_protocol_type, Unset):
            protocol_type = UNSET
        else:
            protocol_type = ProtocolType(_protocol_type)

        created_by = d.pop("createdBy", UNSET)

        repository_profile = cls(
            id=id,
            profile_name=profile_name,
            description=description,
            profile_type=profile_type,
            share_path=share_path,
            status=status,
            factory_type=factory_type,
            file_name=file_name,
            factory_created=factory_created,
            catalog_created_date=catalog_created_date,
            catalog_last_checked=catalog_last_checked,
            check_certificate=check_certificate,
            protocol_type=protocol_type,
            created_by=created_by,
        )

        repository_profile.additional_properties = d
        return repository_profile

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
