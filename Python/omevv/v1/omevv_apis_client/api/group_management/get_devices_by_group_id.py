from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.device import Device
from ...models.error_object import ErrorObject
from ...types import Response


def _get_kwargs(
    uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/Groups/{id}/Devices".format(client.base_url, uuid=uuid, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
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
    if response.status_code == 500:
        response_500 = ErrorObject.from_dict(response.json())

        return response_500
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
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorObject, List[Device]]]:
    """Get a group by OMEVV groupId

     Get a group details by groupID

    Args:
        uuid (str):
        id (int):

    Returns:
        Response[Union[ErrorObject, List[Device]]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        id=id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorObject, List[Device]]]:
    """Get a group by OMEVV groupId

     Get a group details by groupID

    Args:
        uuid (str):
        id (int):

    Returns:
        Response[Union[ErrorObject, List[Device]]]
    """

    return sync_detailed(
        uuid=uuid,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorObject, List[Device]]]:
    """Get a group by OMEVV groupId

     Get a group details by groupID

    Args:
        uuid (str):
        id (int):

    Returns:
        Response[Union[ErrorObject, List[Device]]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorObject, List[Device]]]:
    """Get a group by OMEVV groupId

     Get a group details by groupID

    Args:
        uuid (str):
        id (int):

    Returns:
        Response[Union[ErrorObject, List[Device]]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            id=id,
            client=client,
        )
    ).parsed
