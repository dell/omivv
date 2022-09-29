from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="ConsoleEventSettings")


@attr.s(auto_attribs=True)
class ConsoleEventSettings:
    """
    Attributes:
        event_enabled (bool):
        alarm_enabled (bool):
        mpr_alarm_enabled (bool):
    """

    event_enabled: bool
    alarm_enabled: bool
    mpr_alarm_enabled: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        event_enabled = self.event_enabled
        alarm_enabled = self.alarm_enabled
        mpr_alarm_enabled = self.mpr_alarm_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventEnabled": event_enabled,
                "alarmEnabled": alarm_enabled,
                "mprAlarmEnabled": mpr_alarm_enabled,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        event_enabled = d.pop("eventEnabled")

        alarm_enabled = d.pop("alarmEnabled")

        mpr_alarm_enabled = d.pop("mprAlarmEnabled")

        console_event_settings = cls(
            event_enabled=event_enabled,
            alarm_enabled=alarm_enabled,
            mpr_alarm_enabled=mpr_alarm_enabled,
        )

        console_event_settings.additional_properties = d
        return console_event_settings

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
