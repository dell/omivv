from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Processor")


@attr.s(auto_attribs=True)
class Processor:
    """
    Attributes:
        id (Union[Unset, int]):
        family (Union[Unset, str]): displays the processor family name.
        max_speed (Union[Unset, int]): displays the maximum speed.
        current_speed (Union[Unset, int]): displays the current speed.
        status (Union[Unset, int]):
        number_of_cores (Union[Unset, int]): displays the total number of cores in this processor.
        number_of_enabled_cores (Union[Unset, int]): displays the number of enabled cores in this processor.
        brand_name (Union[Unset, str]): displays the processor brand.
        model_name (Union[Unset, str]): displays the processor model name.
        instance_id (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    family: Union[Unset, str] = UNSET
    max_speed: Union[Unset, int] = UNSET
    current_speed: Union[Unset, int] = UNSET
    status: Union[Unset, int] = UNSET
    number_of_cores: Union[Unset, int] = UNSET
    number_of_enabled_cores: Union[Unset, int] = UNSET
    brand_name: Union[Unset, str] = UNSET
    model_name: Union[Unset, str] = UNSET
    instance_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        family = self.family
        max_speed = self.max_speed
        current_speed = self.current_speed
        status = self.status
        number_of_cores = self.number_of_cores
        number_of_enabled_cores = self.number_of_enabled_cores
        brand_name = self.brand_name
        model_name = self.model_name
        instance_id = self.instance_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if family is not UNSET:
            field_dict["family"] = family
        if max_speed is not UNSET:
            field_dict["maxSpeed"] = max_speed
        if current_speed is not UNSET:
            field_dict["currentSpeed"] = current_speed
        if status is not UNSET:
            field_dict["status"] = status
        if number_of_cores is not UNSET:
            field_dict["numberOfCores"] = number_of_cores
        if number_of_enabled_cores is not UNSET:
            field_dict["numberOfEnabledCores"] = number_of_enabled_cores
        if brand_name is not UNSET:
            field_dict["brandName"] = brand_name
        if model_name is not UNSET:
            field_dict["modelName"] = model_name
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        family = d.pop("family", UNSET)

        max_speed = d.pop("maxSpeed", UNSET)

        current_speed = d.pop("currentSpeed", UNSET)

        status = d.pop("status", UNSET)

        number_of_cores = d.pop("numberOfCores", UNSET)

        number_of_enabled_cores = d.pop("numberOfEnabledCores", UNSET)

        brand_name = d.pop("brandName", UNSET)

        model_name = d.pop("modelName", UNSET)

        instance_id = d.pop("instanceId", UNSET)

        processor = cls(
            id=id,
            family=family,
            max_speed=max_speed,
            current_speed=current_speed,
            status=status,
            number_of_cores=number_of_cores,
            number_of_enabled_cores=number_of_enabled_cores,
            brand_name=brand_name,
            model_name=model_name,
            instance_id=instance_id,
        )

        processor.additional_properties = d
        return processor

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
