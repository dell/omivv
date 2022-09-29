from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.storage_identifier_identifier_type import StorageIdentifierIdentifierType

T = TypeVar("T", bound="StorageIdentifier")


@attr.s(auto_attribs=True)
class StorageIdentifier:
    """
    Attributes:
        identifier (str): Worldwide persistent name of the resource Example: 5002e10000000000.
        identifier_type (StorageIdentifierIdentifierType): Indicates the format and assignment authority for the
            identifier. Example: NAA.
    """

    identifier: str
    identifier_type: StorageIdentifierIdentifierType
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifier = self.identifier
        identifier_type = self.identifier_type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "identifierType": identifier_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifier = d.pop("identifier")

        identifier_type = StorageIdentifierIdentifierType(d.pop("identifierType"))

        storage_identifier = cls(
            identifier=identifier,
            identifier_type=identifier_type,
        )

        storage_identifier.additional_properties = d
        return storage_identifier

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
