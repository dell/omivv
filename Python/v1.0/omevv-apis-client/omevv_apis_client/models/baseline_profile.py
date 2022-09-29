import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.cluster_info import ClusterInfo
from ..types import UNSET, Unset

T = TypeVar("T", bound="BaselineProfile")


@attr.s(auto_attribs=True)
class BaselineProfile:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        description (Union[Unset, str]):
        console_id (Union[Unset, str]):
        console_address (Union[Unset, str]):
        firmware_repo_id (Union[Unset, int]):
        firmware_repo_name (Union[Unset, str]):
        configuration_repo_id (Union[Unset, int]):
        configuration_repo_name (Union[Unset, str]):
        driver_repo_id (Union[Unset, int]):
        driver_repo_name (Union[Unset, str]):
        drift_job_id (Union[Unset, int]):
        drift_job_name (Union[Unset, str]):
        date_created (Union[Unset, datetime.datetime]):
        date_modified (Union[Unset, datetime.datetime]):
        lastmodified_by (Union[Unset, str]):
        version (Union[Unset, str]):
        last_successful_updated_time (Union[Unset, datetime.datetime]):
        cluster_info (Union[Unset, List[ClusterInfo]]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    console_id: Union[Unset, str] = UNSET
    console_address: Union[Unset, str] = UNSET
    firmware_repo_id: Union[Unset, int] = UNSET
    firmware_repo_name: Union[Unset, str] = UNSET
    configuration_repo_id: Union[Unset, int] = UNSET
    configuration_repo_name: Union[Unset, str] = UNSET
    driver_repo_id: Union[Unset, int] = UNSET
    driver_repo_name: Union[Unset, str] = UNSET
    drift_job_id: Union[Unset, int] = UNSET
    drift_job_name: Union[Unset, str] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    date_modified: Union[Unset, datetime.datetime] = UNSET
    lastmodified_by: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    last_successful_updated_time: Union[Unset, datetime.datetime] = UNSET
    cluster_info: Union[Unset, List[ClusterInfo]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        name = self.name
        description = self.description
        console_id = self.console_id
        console_address = self.console_address
        firmware_repo_id = self.firmware_repo_id
        firmware_repo_name = self.firmware_repo_name
        configuration_repo_id = self.configuration_repo_id
        configuration_repo_name = self.configuration_repo_name
        driver_repo_id = self.driver_repo_id
        driver_repo_name = self.driver_repo_name
        drift_job_id = self.drift_job_id
        drift_job_name = self.drift_job_name
        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_modified: Union[Unset, str] = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        lastmodified_by = self.lastmodified_by
        version = self.version
        last_successful_updated_time: Union[Unset, str] = UNSET
        if not isinstance(self.last_successful_updated_time, Unset):
            last_successful_updated_time = self.last_successful_updated_time.isoformat()

        cluster_info: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cluster_info, Unset):
            cluster_info = []
            for cluster_info_item_data in self.cluster_info:
                cluster_info_item = cluster_info_item_data.to_dict()

                cluster_info.append(cluster_info_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if console_id is not UNSET:
            field_dict["consoleId"] = console_id
        if console_address is not UNSET:
            field_dict["consoleAddress"] = console_address
        if firmware_repo_id is not UNSET:
            field_dict["firmwareRepoId"] = firmware_repo_id
        if firmware_repo_name is not UNSET:
            field_dict["firmwareRepoName"] = firmware_repo_name
        if configuration_repo_id is not UNSET:
            field_dict["configurationRepoId"] = configuration_repo_id
        if configuration_repo_name is not UNSET:
            field_dict["configurationRepoName"] = configuration_repo_name
        if driver_repo_id is not UNSET:
            field_dict["driverRepoId"] = driver_repo_id
        if driver_repo_name is not UNSET:
            field_dict["driverRepoName"] = driver_repo_name
        if drift_job_id is not UNSET:
            field_dict["driftJobId"] = drift_job_id
        if drift_job_name is not UNSET:
            field_dict["driftJobName"] = drift_job_name
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if date_modified is not UNSET:
            field_dict["dateModified"] = date_modified
        if lastmodified_by is not UNSET:
            field_dict["lastmodifiedBy"] = lastmodified_by
        if version is not UNSET:
            field_dict["version"] = version
        if last_successful_updated_time is not UNSET:
            field_dict["lastSuccessfulUpdatedTime"] = last_successful_updated_time
        if cluster_info is not UNSET:
            field_dict["clusterInfo"] = cluster_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        console_id = d.pop("consoleId", UNSET)

        console_address = d.pop("consoleAddress", UNSET)

        firmware_repo_id = d.pop("firmwareRepoId", UNSET)

        firmware_repo_name = d.pop("firmwareRepoName", UNSET)

        configuration_repo_id = d.pop("configurationRepoId", UNSET)

        configuration_repo_name = d.pop("configurationRepoName", UNSET)

        driver_repo_id = d.pop("driverRepoId", UNSET)

        driver_repo_name = d.pop("driverRepoName", UNSET)

        drift_job_id = d.pop("driftJobId", UNSET)

        drift_job_name = d.pop("driftJobName", UNSET)

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _date_modified = d.pop("dateModified", UNSET)
        date_modified: Union[Unset, datetime.datetime]
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = isoparse(_date_modified)

        lastmodified_by = d.pop("lastmodifiedBy", UNSET)

        version = d.pop("version", UNSET)

        _last_successful_updated_time = d.pop("lastSuccessfulUpdatedTime", UNSET)
        last_successful_updated_time: Union[Unset, datetime.datetime]
        if isinstance(_last_successful_updated_time, Unset):
            last_successful_updated_time = UNSET
        else:
            last_successful_updated_time = isoparse(_last_successful_updated_time)

        cluster_info = []
        _cluster_info = d.pop("clusterInfo", UNSET)
        for cluster_info_item_data in _cluster_info or []:
            cluster_info_item = ClusterInfo.from_dict(cluster_info_item_data)

            cluster_info.append(cluster_info_item)

        baseline_profile = cls(
            id=id,
            name=name,
            description=description,
            console_id=console_id,
            console_address=console_address,
            firmware_repo_id=firmware_repo_id,
            firmware_repo_name=firmware_repo_name,
            configuration_repo_id=configuration_repo_id,
            configuration_repo_name=configuration_repo_name,
            driver_repo_id=driver_repo_id,
            driver_repo_name=driver_repo_name,
            drift_job_id=drift_job_id,
            drift_job_name=drift_job_name,
            date_created=date_created,
            date_modified=date_modified,
            lastmodified_by=lastmodified_by,
            version=version,
            last_successful_updated_time=last_successful_updated_time,
            cluster_info=cluster_info,
        )

        baseline_profile.additional_properties = d
        return baseline_profile

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
