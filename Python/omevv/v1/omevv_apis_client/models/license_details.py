import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseDetails")


@attr.s(auto_attribs=True)
class LicenseDetails:
    """
    Attributes:
        idrac_license_type (Union[Unset, str]): iDRAC license type
        idrac_license_description (Union[Unset, str]):
        idrac_license_expiration_date (Union[Unset, datetime.datetime]): iDRAC license expiration date and time
        license_entitlement_id (Union[Unset, str]): identifer of the license
    """

    idrac_license_type: Union[Unset, str] = UNSET
    idrac_license_description: Union[Unset, str] = UNSET
    idrac_license_expiration_date: Union[Unset, datetime.datetime] = UNSET
    license_entitlement_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        idrac_license_type = self.idrac_license_type
        idrac_license_description = self.idrac_license_description
        idrac_license_expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.idrac_license_expiration_date, Unset):
            idrac_license_expiration_date = self.idrac_license_expiration_date.isoformat()

        license_entitlement_id = self.license_entitlement_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if idrac_license_type is not UNSET:
            field_dict["idracLicenseType"] = idrac_license_type
        if idrac_license_description is not UNSET:
            field_dict["idracLicenseDescription"] = idrac_license_description
        if idrac_license_expiration_date is not UNSET:
            field_dict["idracLicenseExpirationDate"] = idrac_license_expiration_date
        if license_entitlement_id is not UNSET:
            field_dict["licenseEntitlementID"] = license_entitlement_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        idrac_license_type = d.pop("idracLicenseType", UNSET)

        idrac_license_description = d.pop("idracLicenseDescription", UNSET)

        _idrac_license_expiration_date = d.pop("idracLicenseExpirationDate", UNSET)
        idrac_license_expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_idrac_license_expiration_date, Unset):
            idrac_license_expiration_date = UNSET
        else:
            if _idrac_license_expiration_date is None:
                idrac_license_expiration_date = None
            else:
                idrac_license_expiration_date = isoparse(_idrac_license_expiration_date)

        license_entitlement_id = d.pop("licenseEntitlementID", UNSET)

        license_details = cls(
            idrac_license_type=idrac_license_type,
            idrac_license_description=idrac_license_description,
            idrac_license_expiration_date=idrac_license_expiration_date,
            license_entitlement_id=license_entitlement_id,
        )

        license_details.additional_properties = d
        return license_details

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
