from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.firmware_update_request_enter_maintenance_mode_option import (
    FirmwareUpdateRequestEnterMaintenanceModeOption,
)
from ..models.firmware_update_request_reboot_options import FirmwareUpdateRequestRebootOptions
from ..models.host_firmware_components import HostFirmwareComponents
from ..types import UNSET, Unset

T = TypeVar("T", bound="FirmwareUpdateRequest")


@attr.s(auto_attribs=True)
class FirmwareUpdateRequest:
    """Firmware update request model.

    Attributes:
        reboot_options (Union[Unset, FirmwareUpdateRequestRebootOptions]): Host reboot option for firmware update
        checkv_san_health (Union[Unset, bool]): To check VSAN health whilst update
        exit_maintenance_mode (Union[Unset, bool]): Whether to exit MM mode after Update
        drs_check (Union[Unset, bool]): (cluster applicable) Check if cluster's DRS is enabled
        maintenance_mode_count_check (Union[Unset, bool]): (vSAN Applicable) Check if any host in cluster is in MM mode
        evacuate_v_ms (Union[Unset, bool]): When host is powered off, move the VM to other host.
        reset_i_drac (Union[Unset, bool]): Reset iDrac while performing firmware update.
        delete_jobs_queue (Union[Unset, bool]): Delete job queue in iDrac while performing firmware update.
        enter_maintenance_mode_option (Union[Unset, FirmwareUpdateRequestEnterMaintenanceModeOption]): (vSAN Applicable)
            During MM mode, VM migration polic
        enter_maintenance_modetimeout (Union[Unset, int]): (vSAN Applicable) During MM mode, time out
        targets (Union[Unset, List[HostFirmwareComponents]]):
    """

    reboot_options: Union[Unset, FirmwareUpdateRequestRebootOptions] = UNSET
    checkv_san_health: Union[Unset, bool] = UNSET
    exit_maintenance_mode: Union[Unset, bool] = UNSET
    drs_check: Union[Unset, bool] = UNSET
    maintenance_mode_count_check: Union[Unset, bool] = UNSET
    evacuate_v_ms: Union[Unset, bool] = UNSET
    reset_i_drac: Union[Unset, bool] = UNSET
    delete_jobs_queue: Union[Unset, bool] = UNSET
    enter_maintenance_mode_option: Union[Unset, FirmwareUpdateRequestEnterMaintenanceModeOption] = UNSET
    enter_maintenance_modetimeout: Union[Unset, int] = UNSET
    targets: Union[Unset, List[HostFirmwareComponents]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reboot_options: Union[Unset, str] = UNSET
        if not isinstance(self.reboot_options, Unset):
            reboot_options = self.reboot_options.value

        checkv_san_health = self.checkv_san_health
        exit_maintenance_mode = self.exit_maintenance_mode
        drs_check = self.drs_check
        maintenance_mode_count_check = self.maintenance_mode_count_check
        evacuate_v_ms = self.evacuate_v_ms
        reset_i_drac = self.reset_i_drac
        delete_jobs_queue = self.delete_jobs_queue
        enter_maintenance_mode_option: Union[Unset, str] = UNSET
        if not isinstance(self.enter_maintenance_mode_option, Unset):
            enter_maintenance_mode_option = self.enter_maintenance_mode_option.value

        enter_maintenance_modetimeout = self.enter_maintenance_modetimeout
        targets: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()

                targets.append(targets_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reboot_options is not UNSET:
            field_dict["rebootOptions"] = reboot_options
        if checkv_san_health is not UNSET:
            field_dict["checkvSANHealth"] = checkv_san_health
        if exit_maintenance_mode is not UNSET:
            field_dict["exitMaintenanceMode"] = exit_maintenance_mode
        if drs_check is not UNSET:
            field_dict["drsCheck"] = drs_check
        if maintenance_mode_count_check is not UNSET:
            field_dict["maintenanceModeCountCheck"] = maintenance_mode_count_check
        if evacuate_v_ms is not UNSET:
            field_dict["evacuateVMs"] = evacuate_v_ms
        if reset_i_drac is not UNSET:
            field_dict["resetIDrac"] = reset_i_drac
        if delete_jobs_queue is not UNSET:
            field_dict["deleteJobsQueue"] = delete_jobs_queue
        if enter_maintenance_mode_option is not UNSET:
            field_dict["enterMaintenanceModeOption"] = enter_maintenance_mode_option
        if enter_maintenance_modetimeout is not UNSET:
            field_dict["enterMaintenanceModetimeout"] = enter_maintenance_modetimeout
        if targets is not UNSET:
            field_dict["targets"] = targets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _reboot_options = d.pop("rebootOptions", UNSET)
        reboot_options: Union[Unset, FirmwareUpdateRequestRebootOptions]
        if isinstance(_reboot_options, Unset):
            reboot_options = UNSET
        else:
            reboot_options = FirmwareUpdateRequestRebootOptions(_reboot_options)

        checkv_san_health = d.pop("checkvSANHealth", UNSET)

        exit_maintenance_mode = d.pop("exitMaintenanceMode", UNSET)

        drs_check = d.pop("drsCheck", UNSET)

        maintenance_mode_count_check = d.pop("maintenanceModeCountCheck", UNSET)

        evacuate_v_ms = d.pop("evacuateVMs", UNSET)

        reset_i_drac = d.pop("resetIDrac", UNSET)

        delete_jobs_queue = d.pop("deleteJobsQueue", UNSET)

        _enter_maintenance_mode_option = d.pop("enterMaintenanceModeOption", UNSET)
        enter_maintenance_mode_option: Union[Unset, FirmwareUpdateRequestEnterMaintenanceModeOption]
        if isinstance(_enter_maintenance_mode_option, Unset):
            enter_maintenance_mode_option = UNSET
        else:
            enter_maintenance_mode_option = FirmwareUpdateRequestEnterMaintenanceModeOption(
                _enter_maintenance_mode_option
            )

        enter_maintenance_modetimeout = d.pop("enterMaintenanceModetimeout", UNSET)

        targets = []
        _targets = d.pop("targets", UNSET)
        for targets_item_data in _targets or []:
            targets_item = HostFirmwareComponents.from_dict(targets_item_data)

            targets.append(targets_item)

        firmware_update_request = cls(
            reboot_options=reboot_options,
            checkv_san_health=checkv_san_health,
            exit_maintenance_mode=exit_maintenance_mode,
            drs_check=drs_check,
            maintenance_mode_count_check=maintenance_mode_count_check,
            evacuate_v_ms=evacuate_v_ms,
            reset_i_drac=reset_i_drac,
            delete_jobs_queue=delete_jobs_queue,
            enter_maintenance_mode_option=enter_maintenance_mode_option,
            enter_maintenance_modetimeout=enter_maintenance_modetimeout,
            targets=targets,
        )

        firmware_update_request.additional_properties = d
        return firmware_update_request

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
