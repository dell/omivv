from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PowerSupply")


@attr.s(auto_attribs=True)
class PowerSupply:
    """
    Attributes:
        id (Union[Unset, int]):
        output_watts (Union[Unset, int]):
        name (Union[Unset, str]):
        location (Union[Unset, str]):
        status (Union[Unset, str]):
        state (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    output_watts: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        output_watts = self.output_watts
        name = self.name
        location = self.location
        status = self.status
        state = self.state

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if output_watts is not UNSET:
            field_dict["outputWatts"] = output_watts
        if name is not UNSET:
            field_dict["name"] = name
        if location is not UNSET:
            field_dict["location"] = location
        if status is not UNSET:
            field_dict["status"] = status
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        output_watts = d.pop("outputWatts", UNSET)

        name = d.pop("name", UNSET)

        location = d.pop("location", UNSET)

        status = d.pop("status", UNSET)

        state = d.pop("state", UNSET)

        power_supply = cls(
            id=id,
            output_watts=output_watts,
            name=name,
            location=location,
            status=status,
            state=state,
        )

        power_supply.additional_properties = d
        return power_supply

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
