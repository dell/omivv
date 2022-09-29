from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.task_info import TaskInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    task: str,
    *,
    client: Client,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/vsphere-lcm/hw-support/v1/tasks/{task}".format(client.base_url, task=task)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(v_center_instance_guid, Unset):
        headers["VCenter-Instance-GUID"] = v_center_instance_guid

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorResponse, TaskInfo]]:
    if response.status_code == 200:
        response_200 = TaskInfo.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorResponse, TaskInfo]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    task: str,
    *,
    client: Client,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, TaskInfo]]:
    """Get information on a particular task

    Args:
        task (str):
        v_center_instance_guid (Union[Unset, str]):

    Returns:
        Response[Union[ErrorResponse, TaskInfo]]
    """

    kwargs = _get_kwargs(
        task=task,
        client=client,
        v_center_instance_guid=v_center_instance_guid,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    task: str,
    *,
    client: Client,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, TaskInfo]]:
    """Get information on a particular task

    Args:
        task (str):
        v_center_instance_guid (Union[Unset, str]):

    Returns:
        Response[Union[ErrorResponse, TaskInfo]]
    """

    return sync_detailed(
        task=task,
        client=client,
        v_center_instance_guid=v_center_instance_guid,
    ).parsed


async def asyncio_detailed(
    task: str,
    *,
    client: Client,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, TaskInfo]]:
    """Get information on a particular task

    Args:
        task (str):
        v_center_instance_guid (Union[Unset, str]):

    Returns:
        Response[Union[ErrorResponse, TaskInfo]]
    """

    kwargs = _get_kwargs(
        task=task,
        client=client,
        v_center_instance_guid=v_center_instance_guid,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    task: str,
    *,
    client: Client,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, TaskInfo]]:
    """Get information on a particular task

    Args:
        task (str):
        v_center_instance_guid (Union[Unset, str]):

    Returns:
        Response[Union[ErrorResponse, TaskInfo]]
    """

    return (
        await asyncio_detailed(
            task=task,
            client=client,
            v_center_instance_guid=v_center_instance_guid,
        )
    ).parsed
