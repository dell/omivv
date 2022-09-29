from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/vsphere-lcm/hw-support/v1/hosts".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorResponse, List[str]]]:
    if response.status_code == 200:
        response_200 = cast(List[str], response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorResponse, List[str]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, List[str]]]:
    """List the hosts currently being managed

    Args:
        v_center_instance_guid (Union[Unset, str]):

    Returns:
        Response[Union[ErrorResponse, List[str]]]
    """

    kwargs = _get_kwargs(
        client=client,
        v_center_instance_guid=v_center_instance_guid,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, List[str]]]:
    """List the hosts currently being managed

    Args:
        v_center_instance_guid (Union[Unset, str]):

    Returns:
        Response[Union[ErrorResponse, List[str]]]
    """

    return sync_detailed(
        client=client,
        v_center_instance_guid=v_center_instance_guid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, List[str]]]:
    """List the hosts currently being managed

    Args:
        v_center_instance_guid (Union[Unset, str]):

    Returns:
        Response[Union[ErrorResponse, List[str]]]
    """

    kwargs = _get_kwargs(
        client=client,
        v_center_instance_guid=v_center_instance_guid,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, List[str]]]:
    """List the hosts currently being managed

    Args:
        v_center_instance_guid (Union[Unset, str]):

    Returns:
        Response[Union[ErrorResponse, List[str]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            v_center_instance_guid=v_center_instance_guid,
        )
    ).parsed
