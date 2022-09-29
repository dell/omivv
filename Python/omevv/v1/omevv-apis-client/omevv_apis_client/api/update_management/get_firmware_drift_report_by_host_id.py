from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error_object import ErrorObject
from ...models.firmware_drift_response_model import FirmwareDriftResponseModel
from ...types import Response


def _get_kwargs(
    uuid: str,
    gid: int,
    hid: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/Groups/{gid}/ManagedHosts/{hid}/FirmwareDriftReport".format(
        client.base_url, uuid=uuid, gid=gid, hid=hid
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorObject, FirmwareDriftResponseModel]]:
    if response.status_code == 200:
        response_200 = FirmwareDriftResponseModel.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorObject, FirmwareDriftResponseModel]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    uuid: str,
    gid: int,
    hid: int,
    *,
    client: Client,
) -> Response[Union[ErrorObject, FirmwareDriftResponseModel]]:
    """Get  Firmware Drift report by groupid

     Get  Firmware Drift report by groupid

    Args:
        uuid (str):
        gid (int):
        hid (int):

    Returns:
        Response[Union[ErrorObject, FirmwareDriftResponseModel]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        gid=gid,
        hid=hid,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    uuid: str,
    gid: int,
    hid: int,
    *,
    client: Client,
) -> Optional[Union[ErrorObject, FirmwareDriftResponseModel]]:
    """Get  Firmware Drift report by groupid

     Get  Firmware Drift report by groupid

    Args:
        uuid (str):
        gid (int):
        hid (int):

    Returns:
        Response[Union[ErrorObject, FirmwareDriftResponseModel]]
    """

    return sync_detailed(
        uuid=uuid,
        gid=gid,
        hid=hid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    gid: int,
    hid: int,
    *,
    client: Client,
) -> Response[Union[ErrorObject, FirmwareDriftResponseModel]]:
    """Get  Firmware Drift report by groupid

     Get  Firmware Drift report by groupid

    Args:
        uuid (str):
        gid (int):
        hid (int):

    Returns:
        Response[Union[ErrorObject, FirmwareDriftResponseModel]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        gid=gid,
        hid=hid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    gid: int,
    hid: int,
    *,
    client: Client,
) -> Optional[Union[ErrorObject, FirmwareDriftResponseModel]]:
    """Get  Firmware Drift report by groupid

     Get  Firmware Drift report by groupid

    Args:
        uuid (str):
        gid (int):
        hid (int):

    Returns:
        Response[Union[ErrorObject, FirmwareDriftResponseModel]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            gid=gid,
            hid=hid,
            client=client,
        )
    ).parsed
