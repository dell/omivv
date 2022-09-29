from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rac_response import RACResponse
from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupDeviceHardwareDetails")


@attr.s(auto_attribs=True)
class GroupDeviceHardwareDetails:
    """
    Attributes:
        host (Union[Unset, str]):
        service_tag (Union[Unset, str]):
        frus (Union[Unset, Any]):
        processors (Union[Unset, Any]):
        power_supplies (Union[Unset, Any]):
        memory (Union[Unset, Any]):
        nics (Union[Unset, Any]):
        pci_slots (Union[Unset, Any]):
        remote_access_card (Union[Unset, RACResponse]):
    """

    host: Union[Unset, str] = UNSET
    service_tag: Union[Unset, str] = UNSET
    frus: Union[Unset, Any] = UNSET
    processors: Union[Unset, Any] = UNSET
    power_supplies: Union[Unset, Any] = UNSET
    memory: Union[Unset, Any] = UNSET
    nics: Union[Unset, Any] = UNSET
    pci_slots: Union[Unset, Any] = UNSET
    remote_access_card: Union[Unset, RACResponse] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host = self.host
        service_tag = self.service_tag
        frus = self.frus
        processors = self.processors
        power_supplies = self.power_supplies
        memory = self.memory
        nics = self.nics
        pci_slots = self.pci_slots
        remote_access_card: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.remote_access_card, Unset):
            remote_access_card = self.remote_access_card.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host is not UNSET:
            field_dict["host"] = host
        if service_tag is not UNSET:
            field_dict["serviceTag"] = service_tag
        if frus is not UNSET:
            field_dict["frus"] = frus
        if processors is not UNSET:
            field_dict["processors"] = processors
        if power_supplies is not UNSET:
            field_dict["powerSupplies"] = power_supplies
        if memory is not UNSET:
            field_dict["memory"] = memory
        if nics is not UNSET:
            field_dict["nics"] = nics
        if pci_slots is not UNSET:
            field_dict["pciSlots"] = pci_slots
        if remote_access_card is not UNSET:
            field_dict["remoteAccessCard"] = remote_access_card

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        host = d.pop("host", UNSET)

        service_tag = d.pop("serviceTag", UNSET)

        frus = d.pop("frus", UNSET)

        processors = d.pop("processors", UNSET)

        power_supplies = d.pop("powerSupplies", UNSET)

        memory = d.pop("memory", UNSET)

        nics = d.pop("nics", UNSET)

        pci_slots = d.pop("pciSlots", UNSET)

        _remote_access_card = d.pop("remoteAccessCard", UNSET)
        remote_access_card: Union[Unset, RACResponse]
        if isinstance(_remote_access_card, Unset):
            remote_access_card = UNSET
        else:
            remote_access_card = RACResponse.from_dict(_remote_access_card)

        group_device_hardware_details = cls(
            host=host,
            service_tag=service_tag,
            frus=frus,
            processors=processors,
            power_supplies=power_supplies,
            memory=memory,
            nics=nics,
            pci_slots=pci_slots,
            remote_access_card=remote_access_card,
        )

        group_device_hardware_details.additional_properties = d
        return group_device_hardware_details

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
