from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error_object import ErrorObject
from ...models.group import Group
from ...types import Response


def _get_kwargs(
    uuid: str,
    gid: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/Groups/{gid}".format(client.base_url, uuid=uuid, gid=gid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorObject, Group]]:
    if response.status_code == 200:
        response_200 = Group.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorObject.from_dict(response.json())

        return response_400
    if response.status_code == 500:
        response_500 = ErrorObject.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorObject, Group]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    uuid: str,
    gid: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorObject, Group]]:
    """Get a group by OMEVV groupId

     Get a group details by groupID

    Args:
        uuid (str):
        gid (int):

    Returns:
        Response[Union[ErrorObject, Group]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        gid=gid,
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
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorObject, Group]]:
    """Get a group by OMEVV groupId

     Get a group details by groupID

    Args:
        uuid (str):
        gid (int):

    Returns:
        Response[Union[ErrorObject, Group]]
    """

    return sync_detailed(
        uuid=uuid,
        gid=gid,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    gid: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorObject, Group]]:
    """Get a group by OMEVV groupId

     Get a group details by groupID

    Args:
        uuid (str):
        gid (int):

    Returns:
        Response[Union[ErrorObject, Group]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        gid=gid,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    gid: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorObject, Group]]:
    """Get a group by OMEVV groupId

     Get a group details by groupID

    Args:
        uuid (str):
        gid (int):

    Returns:
        Response[Union[ErrorObject, Group]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            gid=gid,
            client=client,
        )
    ).parsed
