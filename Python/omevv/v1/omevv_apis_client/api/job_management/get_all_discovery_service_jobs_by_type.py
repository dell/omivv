from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error_object import ErrorObject
from ...models.get_all_discovery_service_jobs_by_type_jobtype import GetAllDiscoveryServiceJobsByTypeJobtype
from ...models.job import Job
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    client: AuthenticatedClient,
    jobtype: Union[Unset, None, GetAllDiscoveryServiceJobsByTypeJobtype] = UNSET,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/DiscoveryJobs".format(client.base_url, uuid=uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_jobtype: Union[Unset, None, str] = UNSET
    if not isinstance(jobtype, Unset):
        json_jobtype = jobtype.value if jobtype else None

    params["jobtype"] = json_jobtype

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorObject, List[Job]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Job.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ErrorObject.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ErrorObject.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ErrorObject.from_dict(response.json())

        return response_403
    if response.status_code == 500:
        response_500 = ErrorObject.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorObject, List[Job]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    jobtype: Union[Unset, None, GetAllDiscoveryServiceJobsByTypeJobtype] = UNSET,
) -> Response[Union[ErrorObject, List[Job]]]:
    """Get all jobs by type

     Gets the list of  the discovery service jobs

    Args:
        uuid (str):
        jobtype (Union[Unset, None, GetAllDiscoveryServiceJobsByTypeJobtype]):

    Returns:
        Response[Union[ErrorObject, List[Job]]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        jobtype=jobtype,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    uuid: str,
    *,
    client: AuthenticatedClient,
    jobtype: Union[Unset, None, GetAllDiscoveryServiceJobsByTypeJobtype] = UNSET,
) -> Optional[Union[ErrorObject, List[Job]]]:
    """Get all jobs by type

     Gets the list of  the discovery service jobs

    Args:
        uuid (str):
        jobtype (Union[Unset, None, GetAllDiscoveryServiceJobsByTypeJobtype]):

    Returns:
        Response[Union[ErrorObject, List[Job]]]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        jobtype=jobtype,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    jobtype: Union[Unset, None, GetAllDiscoveryServiceJobsByTypeJobtype] = UNSET,
) -> Response[Union[ErrorObject, List[Job]]]:
    """Get all jobs by type

     Gets the list of  the discovery service jobs

    Args:
        uuid (str):
        jobtype (Union[Unset, None, GetAllDiscoveryServiceJobsByTypeJobtype]):

    Returns:
        Response[Union[ErrorObject, List[Job]]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        jobtype=jobtype,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
    jobtype: Union[Unset, None, GetAllDiscoveryServiceJobsByTypeJobtype] = UNSET,
) -> Optional[Union[ErrorObject, List[Job]]]:
    """Get all jobs by type

     Gets the list of  the discovery service jobs

    Args:
        uuid (str):
        jobtype (Union[Unset, None, GetAllDiscoveryServiceJobsByTypeJobtype]):

    Returns:
        Response[Union[ErrorObject, List[Job]]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            jobtype=jobtype,
        )
    ).parsed
