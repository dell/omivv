from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.entity_type import EntityType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConsoleEntity")


@attr.s(auto_attribs=True)
class ConsoleEntity:
    """
    Attributes:
        entity_id (Union[Unset, str]):
        parent_entity_id (Union[Unset, str]):
        type (Union[Unset, EntityType]):
        name (Union[Unset, str]):
        visible (Union[Unset, bool]):
    """

    entity_id: Union[Unset, str] = UNSET
    parent_entity_id: Union[Unset, str] = UNSET
    type: Union[Unset, EntityType] = UNSET
    name: Union[Unset, str] = UNSET
    visible: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_id = self.entity_id
        parent_entity_id = self.parent_entity_id
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        name = self.name
        visible = self.visible

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if parent_entity_id is not UNSET:
            field_dict["parentEntityId"] = parent_entity_id
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name
        if visible is not UNSET:
            field_dict["visible"] = visible

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        entity_id = d.pop("entityId", UNSET)

        parent_entity_id = d.pop("parentEntityId", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, EntityType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = EntityType(_type)

        name = d.pop("name", UNSET)

        visible = d.pop("visible", UNSET)

        console_entity = cls(
            entity_id=entity_id,
            parent_entity_id=parent_entity_id,
            type=type,
            name=name,
            visible=visible,
        )

        console_entity.additional_properties = d
        return console_entity

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
