from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.console_event_settings import ConsoleEventSettings
from ...models.error_object import ErrorObject
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/EventSettings".format(client.base_url, uuid=uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ConsoleEventSettings, ErrorObject]]:
    if response.status_code == 200:
        response_200 = ConsoleEventSettings.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[ConsoleEventSettings, ErrorObject]]:
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
) -> Response[Union[ConsoleEventSettings, ErrorObject]]:
    """Your GET endpoint

     Get the Event Settings

    Args:
        uuid (str):

    Returns:
        Response[Union[ConsoleEventSettings, ErrorObject]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
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
) -> Optional[Union[ConsoleEventSettings, ErrorObject]]:
    """Your GET endpoint

     Get the Event Settings

    Args:
        uuid (str):

    Returns:
        Response[Union[ConsoleEventSettings, ErrorObject]]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: Client,
) -> Response[Union[ConsoleEventSettings, ErrorObject]]:
    """Your GET endpoint

     Get the Event Settings

    Args:
        uuid (str):

    Returns:
        Response[Union[ConsoleEventSettings, ErrorObject]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    *,
    client: Client,
) -> Optional[Union[ConsoleEventSettings, ErrorObject]]:
    """Your GET endpoint

     Get the Event Settings

    Args:
        uuid (str):

    Returns:
        Response[Union[ConsoleEventSettings, ErrorObject]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
