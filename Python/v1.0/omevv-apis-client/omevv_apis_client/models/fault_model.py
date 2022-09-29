from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FaultModel")


@attr.s(auto_attribs=True)
class FaultModel:
    """
    Attributes:
        sub_system (Union[Unset, str]): Fault sub system information
        fqdd (Union[Unset, str]): Fault FQDD
        severity (Union[Unset, str]): Fault severity
        message_id (Union[Unset, str]): Fault associated message id
        instance_id (Union[Unset, str]): Fault associated instance id
        time_stamp (Union[Unset, str]): Fault timestamp
        message (Union[Unset, str]): Fault message
        message_arguments (Union[Unset, str]): Fault message arguments
        date_format (Union[Unset, str]): Indicates the time format
        recommended_action (Union[Unset, str]): Indicates the recommended action
    """

    sub_system: Union[Unset, str] = UNSET
    fqdd: Union[Unset, str] = UNSET
    severity: Union[Unset, str] = UNSET
    message_id: Union[Unset, str] = UNSET
    instance_id: Union[Unset, str] = UNSET
    time_stamp: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    message_arguments: Union[Unset, str] = UNSET
    date_format: Union[Unset, str] = UNSET
    recommended_action: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sub_system = self.sub_system
        fqdd = self.fqdd
        severity = self.severity
        message_id = self.message_id
        instance_id = self.instance_id
        time_stamp = self.time_stamp
        message = self.message
        message_arguments = self.message_arguments
        date_format = self.date_format
        recommended_action = self.recommended_action

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sub_system is not UNSET:
            field_dict["subSystem"] = sub_system
        if fqdd is not UNSET:
            field_dict["fqdd"] = fqdd
        if severity is not UNSET:
            field_dict["severity"] = severity
        if message_id is not UNSET:
            field_dict["messageId"] = message_id
        if instance_id is not UNSET:
            field_dict["instanceId"] = instance_id
        if time_stamp is not UNSET:
            field_dict["timeStamp"] = time_stamp
        if message is not UNSET:
            field_dict["message"] = message
        if message_arguments is not UNSET:
            field_dict["messageArguments"] = message_arguments
        if date_format is not UNSET:
            field_dict["dateFormat"] = date_format
        if recommended_action is not UNSET:
            field_dict["recommendedAction"] = recommended_action

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sub_system = d.pop("subSystem", UNSET)

        fqdd = d.pop("fqdd", UNSET)

        severity = d.pop("severity", UNSET)

        message_id = d.pop("messageId", UNSET)

        instance_id = d.pop("instanceId", UNSET)

        time_stamp = d.pop("timeStamp", UNSET)

        message = d.pop("message", UNSET)

        message_arguments = d.pop("messageArguments", UNSET)

        date_format = d.pop("dateFormat", UNSET)

        recommended_action = d.pop("recommendedAction", UNSET)

        fault_model = cls(
            sub_system=sub_system,
            fqdd=fqdd,
            severity=severity,
            message_id=message_id,
            instance_id=instance_id,
            time_stamp=time_stamp,
            message=message,
            message_arguments=message_arguments,
            date_format=date_format,
            recommended_action=recommended_action,
        )

        fault_model.additional_properties = d
        return fault_model

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
