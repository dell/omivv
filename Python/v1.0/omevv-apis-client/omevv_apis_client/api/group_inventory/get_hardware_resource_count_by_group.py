from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error_object import ErrorObject
from ...models.hardware_resource_response import HardwareResourceResponse
from ...types import Response


def _get_kwargs(
    uuid: str,
    omevv_group_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/Groups/{omevv_group_id}/HardwareResourceCount".format(
        client.base_url, uuid=uuid, omevv_group_id=omevv_group_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorObject, HardwareResourceResponse]]:
    if response.status_code == 200:
        response_200 = HardwareResourceResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorObject.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ErrorObject.from_dict(response.json())

        return response_401
    if response.status_code == 404:
        response_404 = ErrorObject.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ErrorObject.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorObject, HardwareResourceResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    uuid: str,
    omevv_group_id: int,
    *,
    client: Client,
) -> Response[Union[ErrorObject, HardwareResourceResponse]]:
    """Get Hardware Overview Details for a group

     Get Hardware Overview Details based on omevv_group_id provided

    Args:
        uuid (str):
        omevv_group_id (int):

    Returns:
        Response[Union[ErrorObject, HardwareResourceResponse]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        omevv_group_id=omevv_group_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    uuid: str,
    omevv_group_id: int,
    *,
    client: Client,
) -> Optional[Union[ErrorObject, HardwareResourceResponse]]:
    """Get Hardware Overview Details for a group

     Get Hardware Overview Details based on omevv_group_id provided

    Args:
        uuid (str):
        omevv_group_id (int):

    Returns:
        Response[Union[ErrorObject, HardwareResourceResponse]]
    """

    return sync_detailed(
        uuid=uuid,
        omevv_group_id=omevv_group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    omevv_group_id: int,
    *,
    client: Client,
) -> Response[Union[ErrorObject, HardwareResourceResponse]]:
    """Get Hardware Overview Details for a group

     Get Hardware Overview Details based on omevv_group_id provided

    Args:
        uuid (str):
        omevv_group_id (int):

    Returns:
        Response[Union[ErrorObject, HardwareResourceResponse]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        omevv_group_id=omevv_group_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    omevv_group_id: int,
    *,
    client: Client,
) -> Optional[Union[ErrorObject, HardwareResourceResponse]]:
    """Get Hardware Overview Details for a group

     Get Hardware Overview Details based on omevv_group_id provided

    Args:
        uuid (str):
        omevv_group_id (int):

    Returns:
        Response[Union[ErrorObject, HardwareResourceResponse]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            omevv_group_id=omevv_group_id,
            client=client,
        )
    ).parsed
