from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.host_compliance_connection_state import HostComplianceConnectionState
from ..models.host_compliance_idrac_license_status import HostComplianceIdracLicenseStatus
from ..models.host_compliance_snmp_trap_status import HostComplianceSnmpTrapStatus
from ..models.host_compliance_state import HostComplianceState
from ..models.license_details import LicenseDetails
from ..types import UNSET, Unset

T = TypeVar("T", bound="HostCompliance")


@attr.s(auto_attribs=True)
class HostCompliance:
    """
    Attributes:
        hostid (Union[Unset, int]): unquie identifier of the host
        host_name (Union[Unset, str]): ipaddress or fqdn of the host
        model (Union[Unset, str]): model name of the host, Ex. PowerEdge R750, PowerEdge T130
        service_tag (Union[Unset, str]): service tag of a server or chassis
        console_id (Union[Unset, str]):
        console_entity_id (Union[Unset, str]): vCenter console entity. E.g. Datacenter EntityID, Cluster EntityID, Host
            EntityID, etc.
        hypervisor (Union[Unset, str]): hypervisor name, E.g. VMWare ESXi 7.0.3 build-17637351
        idrac_ip (Union[Unset, str]): ip address of iDRAC
        idrac_firmware_version (Union[Unset, str]): firmware version of iDRAC
        license_details (Union[Unset, List[LicenseDetails]]): List of license details
        idrac_license_status (Union[Unset, HostComplianceIdracLicenseStatus]): idrac license support status
        snmp_trap_status (Union[Unset, HostComplianceSnmpTrapStatus]): snmp trap configuration status of the host
        state (Union[Unset, HostComplianceState]): indicates the compliance state of the host
        connection_state (Union[Unset, HostComplianceConnectionState]):
    """

    hostid: Union[Unset, int] = UNSET
    host_name: Union[Unset, str] = UNSET
    model: Union[Unset, str] = UNSET
    service_tag: Union[Unset, str] = UNSET
    console_id: Union[Unset, str] = UNSET
    console_entity_id: Union[Unset, str] = UNSET
    hypervisor: Union[Unset, str] = UNSET
    idrac_ip: Union[Unset, str] = UNSET
    idrac_firmware_version: Union[Unset, str] = UNSET
    license_details: Union[Unset, List[LicenseDetails]] = UNSET
    idrac_license_status: Union[Unset, HostComplianceIdracLicenseStatus] = UNSET
    snmp_trap_status: Union[Unset, HostComplianceSnmpTrapStatus] = UNSET
    state: Union[Unset, HostComplianceState] = UNSET
    connection_state: Union[Unset, HostComplianceConnectionState] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hostid = self.hostid
        host_name = self.host_name
        model = self.model
        service_tag = self.service_tag
        console_id = self.console_id
        console_entity_id = self.console_entity_id
        hypervisor = self.hypervisor
        idrac_ip = self.idrac_ip
        idrac_firmware_version = self.idrac_firmware_version
        license_details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.license_details, Unset):
            license_details = []
            for license_details_item_data in self.license_details:
                license_details_item = license_details_item_data.to_dict()

                license_details.append(license_details_item)

        idrac_license_status: Union[Unset, str] = UNSET
        if not isinstance(self.idrac_license_status, Unset):
            idrac_license_status = self.idrac_license_status.value

        snmp_trap_status: Union[Unset, str] = UNSET
        if not isinstance(self.snmp_trap_status, Unset):
            snmp_trap_status = self.snmp_trap_status.value

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        connection_state: Union[Unset, str] = UNSET
        if not isinstance(self.connection_state, Unset):
            connection_state = self.connection_state.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hostid is not UNSET:
            field_dict["hostid"] = hostid
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if model is not UNSET:
            field_dict["model"] = model
        if service_tag is not UNSET:
            field_dict["serviceTag"] = service_tag
        if console_id is not UNSET:
            field_dict["console_id"] = console_id
        if console_entity_id is not UNSET:
            field_dict["consoleEntityId"] = console_entity_id
        if hypervisor is not UNSET:
            field_dict["hypervisor"] = hypervisor
        if idrac_ip is not UNSET:
            field_dict["idracIp"] = idrac_ip
        if idrac_firmware_version is not UNSET:
            field_dict["idracFirmwareVersion"] = idrac_firmware_version
        if license_details is not UNSET:
            field_dict["licenseDetails"] = license_details
        if idrac_license_status is not UNSET:
            field_dict["idracLicenseStatus"] = idrac_license_status
        if snmp_trap_status is not UNSET:
            field_dict["snmpTrapStatus"] = snmp_trap_status
        if state is not UNSET:
            field_dict["state"] = state
        if connection_state is not UNSET:
            field_dict["connectionState"] = connection_state

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        hostid = d.pop("hostid", UNSET)

        host_name = d.pop("hostName", UNSET)

        model = d.pop("model", UNSET)

        service_tag = d.pop("serviceTag", UNSET)

        console_id = d.pop("console_id", UNSET)

        console_entity_id = d.pop("consoleEntityId", UNSET)

        hypervisor = d.pop("hypervisor", UNSET)

        idrac_ip = d.pop("idracIp", UNSET)

        idrac_firmware_version = d.pop("idracFirmwareVersion", UNSET)

        license_details = []
        _license_details = d.pop("licenseDetails", UNSET)
        for license_details_item_data in _license_details or []:
            license_details_item = LicenseDetails.from_dict(license_details_item_data)

            license_details.append(license_details_item)

        _idrac_license_status = d.pop("idracLicenseStatus", UNSET)
        idrac_license_status: Union[Unset, HostComplianceIdracLicenseStatus]
        if isinstance(_idrac_license_status, Unset):
            idrac_license_status = UNSET
        else:
            idrac_license_status = HostComplianceIdracLicenseStatus(_idrac_license_status)

        _snmp_trap_status = d.pop("snmpTrapStatus", UNSET)
        snmp_trap_status: Union[Unset, HostComplianceSnmpTrapStatus]
        if isinstance(_snmp_trap_status, Unset):
            snmp_trap_status = UNSET
        else:
            snmp_trap_status = HostComplianceSnmpTrapStatus(_snmp_trap_status)

        _state = d.pop("state", UNSET)
        state: Union[Unset, HostComplianceState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = HostComplianceState(_state)

        _connection_state = d.pop("connectionState", UNSET)
        connection_state: Union[Unset, HostComplianceConnectionState]
        if isinstance(_connection_state, Unset):
            connection_state = UNSET
        else:
            connection_state = HostComplianceConnectionState(_connection_state)

        host_compliance = cls(
            hostid=hostid,
            host_name=host_name,
            model=model,
            service_tag=service_tag,
            console_id=console_id,
            console_entity_id=console_entity_id,
            hypervisor=hypervisor,
            idrac_ip=idrac_ip,
            idrac_firmware_version=idrac_firmware_version,
            license_details=license_details,
            idrac_license_status=idrac_license_status,
            snmp_trap_status=snmp_trap_status,
            state=state,
            connection_state=connection_state,
        )

        host_compliance.additional_properties = d
        return host_compliance

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
