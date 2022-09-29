from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="FirmwareUpdateSettings")


@attr.s(auto_attribs=True)
class FirmwareUpdateSettings:
    """
    Attributes:
        reseti_drac (bool):
        cleari_drac_jobs (bool):
    """

    reseti_drac: bool
    cleari_drac_jobs: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reseti_drac = self.reseti_drac
        cleari_drac_jobs = self.cleari_drac_jobs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resetiDRAC": reseti_drac,
                "cleariDRACJobs": cleari_drac_jobs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reseti_drac = d.pop("resetiDRAC")

        cleari_drac_jobs = d.pop("cleariDRACJobs")

        firmware_update_settings = cls(
            reseti_drac=reseti_drac,
            cleari_drac_jobs=cleari_drac_jobs,
        )

        firmware_update_settings.additional_properties = d
        return firmware_update_settings

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
