from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.group_group_type import GroupGroupType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Group")


@attr.s(auto_attribs=True)
class Group:
    """
    Attributes:
        group_id (Union[Unset, int]):
        group_type (Union[Unset, GroupGroupType]):
        console_entity_id (Union[Unset, str]): It can be any vCenter entity. E.g Datacenter EntityID, Cluster EntityID,
            Host EntityID, etc.
        console_entity_name (Union[Unset, str]): Name of the vCenter entity. E.g Datacenter name, Cluster name, etc.
        console_id (Union[Unset, str]): vCenter console ID given by OMEVV.
    """

    group_id: Union[Unset, int] = UNSET
    group_type: Union[Unset, GroupGroupType] = UNSET
    console_entity_id: Union[Unset, str] = UNSET
    console_entity_name: Union[Unset, str] = UNSET
    console_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_id = self.group_id
        group_type: Union[Unset, str] = UNSET
        if not isinstance(self.group_type, Unset):
            group_type = self.group_type.value

        console_entity_id = self.console_entity_id
        console_entity_name = self.console_entity_name
        console_id = self.console_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if group_type is not UNSET:
            field_dict["groupType"] = group_type
        if console_entity_id is not UNSET:
            field_dict["consoleEntityId"] = console_entity_id
        if console_entity_name is not UNSET:
            field_dict["consoleEntityName"] = console_entity_name
        if console_id is not UNSET:
            field_dict["consoleId"] = console_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        group_id = d.pop("groupId", UNSET)

        _group_type = d.pop("groupType", UNSET)
        group_type: Union[Unset, GroupGroupType]
        if isinstance(_group_type, Unset):
            group_type = UNSET
        else:
            group_type = GroupGroupType(_group_type)

        console_entity_id = d.pop("consoleEntityId", UNSET)

        console_entity_name = d.pop("consoleEntityName", UNSET)

        console_id = d.pop("consoleId", UNSET)

        group = cls(
            group_id=group_id,
            group_type=group_type,
            console_entity_id=console_entity_id,
            console_entity_name=console_entity_name,
            console_id=console_id,
        )

        group.additional_properties = d
        return group

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
