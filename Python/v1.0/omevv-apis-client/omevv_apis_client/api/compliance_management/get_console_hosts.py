from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.device import Device
from ...models.error_object import ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    client: AuthenticatedClient,
    console_entity_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/Hosts".format(client.base_url, uuid=uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["consoleEntityId"] = console_entity_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorObject, List[Device]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Device.from_dict(response_200_item_data)

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
    if response.status_code == 404:
        response_404 = ErrorObject.from_dict(response.json())

        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorObject, List[Device]]]:
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
    console_entity_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorObject, List[Device]]]:
    """Get list of all hosts of given console

     Get all the console hosts by consoleid

    Args:
        uuid (str):
        console_entity_id (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorObject, List[Device]]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        console_entity_id=console_entity_id,
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
    console_entity_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorObject, List[Device]]]:
    """Get list of all hosts of given console

     Get all the console hosts by consoleid

    Args:
        uuid (str):
        console_entity_id (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorObject, List[Device]]]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        console_entity_id=console_entity_id,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    console_entity_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorObject, List[Device]]]:
    """Get list of all hosts of given console

     Get all the console hosts by consoleid

    Args:
        uuid (str):
        console_entity_id (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorObject, List[Device]]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        console_entity_id=console_entity_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
    console_entity_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorObject, List[Device]]]:
    """Get list of all hosts of given console

     Get all the console hosts by consoleid

    Args:
        uuid (str):
        console_entity_id (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorObject, List[Device]]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            console_entity_id=console_entity_id,
        )
    ).parsed
