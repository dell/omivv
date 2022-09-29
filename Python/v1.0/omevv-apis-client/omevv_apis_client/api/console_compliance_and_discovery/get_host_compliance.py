from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error_object import ErrorObject
from ...models.host_compliance import HostCompliance
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/Compliance".format(client.base_url, uuid=uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorObject, List[HostCompliance]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = HostCompliance.from_dict(response_200_item_data)

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


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorObject, List[HostCompliance]]]:
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
) -> Response[Union[ErrorObject, List[HostCompliance]]]:
    """Get compliance for all host for given console

     Get compliance for all host for given console

    Args:
        uuid (str):

    Returns:
        Response[Union[ErrorObject, List[HostCompliance]]]
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
    client: AuthenticatedClient,
) -> Optional[Union[ErrorObject, List[HostCompliance]]]:
    """Get compliance for all host for given console

     Get compliance for all host for given console

    Args:
        uuid (str):

    Returns:
        Response[Union[ErrorObject, List[HostCompliance]]]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorObject, List[HostCompliance]]]:
    """Get compliance for all host for given console

     Get compliance for all host for given console

    Args:
        uuid (str):

    Returns:
        Response[Union[ErrorObject, List[HostCompliance]]]
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
    client: AuthenticatedClient,
) -> Optional[Union[ErrorObject, List[HostCompliance]]]:
    """Get compliance for all host for given console

     Get compliance for all host for given console

    Args:
        uuid (str):

    Returns:
        Response[Union[ErrorObject, List[HostCompliance]]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
        )
    ).parsed
