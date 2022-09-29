from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error_object import ErrorObject
from ...models.firmware_update_settings import FirmwareUpdateSettings
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/FirmwareUpdateSettings".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorObject, FirmwareUpdateSettings]]:
    if response.status_code == 200:
        response_200 = FirmwareUpdateSettings.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorObject.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ErrorObject.from_dict(response.json())

        return response_401
    if response.status_code == 500:
        response_500 = ErrorObject.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorObject, FirmwareUpdateSettings]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorObject, FirmwareUpdateSettings]]:
    """Get idracReset and clearIdracJob status flag

     Gives flag value to indicate if idracReset or ClearIdracJob is enabled for firmware update jobs.

    Returns:
        Response[Union[ErrorObject, FirmwareUpdateSettings]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorObject, FirmwareUpdateSettings]]:
    """Get idracReset and clearIdracJob status flag

     Gives flag value to indicate if idracReset or ClearIdracJob is enabled for firmware update jobs.

    Returns:
        Response[Union[ErrorObject, FirmwareUpdateSettings]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorObject, FirmwareUpdateSettings]]:
    """Get idracReset and clearIdracJob status flag

     Gives flag value to indicate if idracReset or ClearIdracJob is enabled for firmware update jobs.

    Returns:
        Response[Union[ErrorObject, FirmwareUpdateSettings]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorObject, FirmwareUpdateSettings]]:
    """Get idracReset and clearIdracJob status flag

     Gives flag value to indicate if idracReset or ClearIdracJob is enabled for firmware update jobs.

    Returns:
        Response[Union[ErrorObject, FirmwareUpdateSettings]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
