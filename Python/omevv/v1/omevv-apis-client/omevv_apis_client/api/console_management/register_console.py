from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.console import Console
from ...models.console_create_request import ConsoleCreateRequest
from ...models.error_object import ErrorObject
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: ConsoleCreateRequest,
) -> Dict[str, Any]:
    url = "{}/Consoles".format(client.base_url)

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
    if response.status_code == 201:
        response_201 = Console.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = ErrorObject.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ErrorObject.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ErrorObject.from_dict(response.json())

        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Console, ErrorObject]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ConsoleCreateRequest,
) -> Response[Union[Console, ErrorObject]]:
    """RegisterConsole

     Register console

    Args:
        json_body (ConsoleCreateRequest):

    Returns:
        Response[Union[Console, ErrorObject]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: ConsoleCreateRequest,
) -> Optional[Union[Console, ErrorObject]]:
    """RegisterConsole

     Register console

    Args:
        json_body (ConsoleCreateRequest):

    Returns:
        Response[Union[Console, ErrorObject]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ConsoleCreateRequest,
) -> Response[Union[Console, ErrorObject]]:
    """RegisterConsole

     Register console

    Args:
        json_body (ConsoleCreateRequest):

    Returns:
        Response[Union[Console, ErrorObject]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: ConsoleCreateRequest,
) -> Optional[Union[Console, ErrorObject]]:
    """RegisterConsole

     Register console

    Args:
        json_body (ConsoleCreateRequest):

    Returns:
        Response[Union[Console, ErrorObject]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
