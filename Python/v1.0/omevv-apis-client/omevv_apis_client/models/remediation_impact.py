from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RemediationImpact")


@attr.s(auto_attribs=True)
class RemediationImpact:
    """
    Attributes:
        maintenance_mode_required (bool): Flag to indicate host should be in Maintenance Mode before update Example:
            True.
        pre_image_update_required (bool): Flag to indicate update required before vSphere image update
        intermediate_reboot_required (bool): Flag to indicate host should be rebooted following vSphere image update
        intermediate_reboot_hw_reset_required (bool): Flag to indicate intermediate reboot should include full HW reset
        post_image_update_required (bool): Flag to indicate update required following vSphere image update Example:
            True.
        final_reboot_required (bool): Flag to indicate host should be rebooted before use after update Example: True.
        final_reboot_hw_reset_required (bool): Flag to indicate final reboot should include full HW reset Example: True.
    """

    maintenance_mode_required: bool
    pre_image_update_required: bool
    intermediate_reboot_required: bool
    intermediate_reboot_hw_reset_required: bool
    post_image_update_required: bool
    final_reboot_required: bool
    final_reboot_hw_reset_required: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        maintenance_mode_required = self.maintenance_mode_required
        pre_image_update_required = self.pre_image_update_required
        intermediate_reboot_required = self.intermediate_reboot_required
        intermediate_reboot_hw_reset_required = self.intermediate_reboot_hw_reset_required
        post_image_update_required = self.post_image_update_required
        final_reboot_required = self.final_reboot_required
        final_reboot_hw_reset_required = self.final_reboot_hw_reset_required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "maintenanceModeRequired": maintenance_mode_required,
                "preImageUpdateRequired": pre_image_update_required,
                "intermediateRebootRequired": intermediate_reboot_required,
                "intermediateRebootHwResetRequired": intermediate_reboot_hw_reset_required,
                "postImageUpdateRequired": post_image_update_required,
                "finalRebootRequired": final_reboot_required,
                "finalRebootHwResetRequired": final_reboot_hw_reset_required,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        maintenance_mode_required = d.pop("maintenanceModeRequired")

        pre_image_update_required = d.pop("preImageUpdateRequired")

        intermediate_reboot_required = d.pop("intermediateRebootRequired")

        intermediate_reboot_hw_reset_required = d.pop("intermediateRebootHwResetRequired")

        post_image_update_required = d.pop("postImageUpdateRequired")

        final_reboot_required = d.pop("finalRebootRequired")

        final_reboot_hw_reset_required = d.pop("finalRebootHwResetRequired")

        remediation_impact = cls(
            maintenance_mode_required=maintenance_mode_required,
            pre_image_update_required=pre_image_update_required,
            intermediate_reboot_required=intermediate_reboot_required,
            intermediate_reboot_hw_reset_required=intermediate_reboot_hw_reset_required,
            post_image_update_required=post_image_update_required,
            final_reboot_required=final_reboot_required,
            final_reboot_hw_reset_required=final_reboot_hw_reset_required,
        )

        remediation_impact.additional_properties = d
        return remediation_impact

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
