from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.console import Console
from ...models.console_extension_request import ConsoleExtensionRequest
from ...models.error_object import ErrorObject
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    client: AuthenticatedClient,
    json_body: ConsoleExtensionRequest,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/addExtensions".format(client.base_url, uuid=uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Console, ErrorObject]]:
    if response.status_code == 200:
        response_200 = Console.from_dict(response.json())

        return response_200
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


def _build_response(*, response: httpx.Response) -> Response[Union[Console, ErrorObject]]:
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
    json_body: ConsoleExtensionRequest,
) -> Response[Union[Console, ErrorObject]]:
    """Register new extensions

     Register new extensions

    Args:
        uuid (str):
        json_body (ConsoleExtensionRequest): console extension request object for
            register/unregistering extensions

    Returns:
        Response[Union[Console, ErrorObject]]
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
    client: AuthenticatedClient,
    json_body: ConsoleExtensionRequest,
) -> Optional[Union[Console, ErrorObject]]:
    """Register new extensions

     Register new extensions

    Args:
        uuid (str):
        json_body (ConsoleExtensionRequest): console extension request object for
            register/unregistering extensions

    Returns:
        Response[Union[Console, ErrorObject]]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    json_body: ConsoleExtensionRequest,
) -> Response[Union[Console, ErrorObject]]:
    """Register new extensions

     Register new extensions

    Args:
        uuid (str):
        json_body (ConsoleExtensionRequest): console extension request object for
            register/unregistering extensions

    Returns:
        Response[Union[Console, ErrorObject]]
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
    client: AuthenticatedClient,
    json_body: ConsoleExtensionRequest,
) -> Optional[Union[Console, ErrorObject]]:
    """Register new extensions

     Register new extensions

    Args:
        uuid (str):
        json_body (ConsoleExtensionRequest): console extension request object for
            register/unregistering extensions

    Returns:
        Response[Union[Console, ErrorObject]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            json_body=json_body,
        )
    ).parsed
