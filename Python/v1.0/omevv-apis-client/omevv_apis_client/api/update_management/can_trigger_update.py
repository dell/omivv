from typing import Any, Dict, Optional, cast

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    client: Client,
    json_body: int,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/CanTriggerUpdate".format(client.base_url, uuid=uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[bool]:
    if response.status_code == 200:
        response_200 = cast(bool, response.json())
        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[bool]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    uuid: str,
    *,
    client: Client,
    json_body: int,
) -> Response[bool]:
    """Check if update is allowed.

     Will return true if no existing jobs are running/scheduled.

    Args:
        uuid (str):
        json_body (int): Target OMEVV groupId or groupId associated with the target host

    Returns:
        Response[bool]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    uuid: str,
    *,
    client: Client,
    json_body: int,
) -> Optional[bool]:
    """Check if update is allowed.

     Will return true if no existing jobs are running/scheduled.

    Args:
        uuid (str):
        json_body (int): Target OMEVV groupId or groupId associated with the target host

    Returns:
        Response[bool]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: Client,
    json_body: int,
) -> Response[bool]:
    """Check if update is allowed.

     Will return true if no existing jobs are running/scheduled.

    Args:
        uuid (str):
        json_body (int): Target OMEVV groupId or groupId associated with the target host

    Returns:
        Response[bool]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    *,
    client: Client,
    json_body: int,
) -> Optional[bool]:
    """Check if update is allowed.

     Will return true if no existing jobs are running/scheduled.

    Args:
        uuid (str):
        json_body (int): Target OMEVV groupId or groupId associated with the target host

    Returns:
        Response[bool]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            json_body=json_body,
        )
    ).parsed
