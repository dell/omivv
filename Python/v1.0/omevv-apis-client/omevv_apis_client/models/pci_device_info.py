from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PciDeviceInfo")


@attr.s(auto_attribs=True)
class PciDeviceInfo:
    """
    Attributes:
        class_code (str): 2-hex digit PCI class code Example: 1.
        vid (str): 4-digit PCI vendor ID (VID) Example: 1077.
        did (str): 4-digit PCI device ID (DID) Example: 2020.
        svid (str): 4-digit PCI subsystem vendor ID (SVID) Example: 103c.
        ssid (str): 4-digit PCI subsystem ID (SSID) Example: 170000000.
        class_sub_code (Union[Unset, str]): 2-hex digit PCI sub-class code Example: 4.
        prog_if (Union[Unset, str]): 2-hex digit PCI programmaing interface Example: 20.
    """

    class_code: str
    vid: str
    did: str
    svid: str
    ssid: str
    class_sub_code: Union[Unset, str] = UNSET
    prog_if: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        class_code = self.class_code
        vid = self.vid
        did = self.did
        svid = self.svid
        ssid = self.ssid
        class_sub_code = self.class_sub_code
        prog_if = self.prog_if

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "classCode": class_code,
                "vid": vid,
                "did": did,
                "svid": svid,
                "ssid": ssid,
            }
        )
        if class_sub_code is not UNSET:
            field_dict["classSubCode"] = class_sub_code
        if prog_if is not UNSET:
            field_dict["progIf"] = prog_if

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        class_code = d.pop("classCode")

        vid = d.pop("vid")

        did = d.pop("did")

        svid = d.pop("svid")

        ssid = d.pop("ssid")

        class_sub_code = d.pop("classSubCode", UNSET)

        prog_if = d.pop("progIf", UNSET)

        pci_device_info = cls(
            class_code=class_code,
            vid=vid,
            did=did,
            svid=svid,
            ssid=ssid,
            class_sub_code=class_sub_code,
            prog_if=prog_if,
        )

        pci_device_info.additional_properties = d
        return pci_device_info

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
