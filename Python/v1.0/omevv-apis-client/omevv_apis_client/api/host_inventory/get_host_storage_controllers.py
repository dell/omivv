from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.controller import Controller
from ...models.error_object import ErrorObject
from ...types import Response


def _get_kwargs(
    uuid: str,
    omevv_host_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/ManagedHosts/{omevv_host_id}/Controllers".format(
        client.base_url, uuid=uuid, omevv_host_id=omevv_host_id
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorObject, List[Controller]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Controller.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorObject, List[Controller]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    uuid: str,
    omevv_host_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorObject, List[Controller]]]:
    """Get Host Storage Controllers

     Get Host Storage Controllers

    Args:
        uuid (str):
        omevv_host_id (int):

    Returns:
        Response[Union[ErrorObject, List[Controller]]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        omevv_host_id=omevv_host_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    uuid: str,
    omevv_host_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorObject, List[Controller]]]:
    """Get Host Storage Controllers

     Get Host Storage Controllers

    Args:
        uuid (str):
        omevv_host_id (int):

    Returns:
        Response[Union[ErrorObject, List[Controller]]]
    """

    return sync_detailed(
        uuid=uuid,
        omevv_host_id=omevv_host_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    omevv_host_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorObject, List[Controller]]]:
    """Get Host Storage Controllers

     Get Host Storage Controllers

    Args:
        uuid (str):
        omevv_host_id (int):

    Returns:
        Response[Union[ErrorObject, List[Controller]]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        omevv_host_id=omevv_host_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    omevv_host_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorObject, List[Controller]]]:
    """Get Host Storage Controllers

     Get Host Storage Controllers

    Args:
        uuid (str):
        omevv_host_id (int):

    Returns:
        Response[Union[ErrorObject, List[Controller]]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            omevv_host_id=omevv_host_id,
            client=client,
        )
    ).parsed
