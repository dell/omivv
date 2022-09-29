from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="GroupComplianceSummaryRequest")


@attr.s(auto_attribs=True)
class GroupComplianceSummaryRequest:
    """
    Attributes:
        target_group_ids (List[int]): List of group IDs associated to the cluster
    """

    target_group_ids: List[int]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        target_group_ids = self.target_group_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetGroupIds": target_group_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        target_group_ids = cast(List[int], d.pop("targetGroupIds"))

        group_compliance_summary_request = cls(
            target_group_ids=target_group_ids,
        )

        group_compliance_summary_request.additional_properties = d
        return group_compliance_summary_request

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
