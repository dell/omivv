from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.console_entity import ConsoleEntity
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    client: Client,
    pid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    entityid: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/Clusters".format(client.base_url, uuid=uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["pid"] = pid

    params["name"] = name

    params["entityid"] = entityid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[ConsoleEntity]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ConsoleEntity.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[ConsoleEntity]]:
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
    pid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    entityid: Union[Unset, None, str] = UNSET,
) -> Response[List[ConsoleEntity]]:
    """Get Clusters

     Gets the console clusters

    Args:
        uuid (str):
        pid (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        entityid (Union[Unset, None, str]):

    Returns:
        Response[List[ConsoleEntity]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        pid=pid,
        name=name,
        entityid=entityid,
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
    pid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    entityid: Union[Unset, None, str] = UNSET,
) -> Optional[List[ConsoleEntity]]:
    """Get Clusters

     Gets the console clusters

    Args:
        uuid (str):
        pid (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        entityid (Union[Unset, None, str]):

    Returns:
        Response[List[ConsoleEntity]]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        pid=pid,
        name=name,
        entityid=entityid,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: Client,
    pid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    entityid: Union[Unset, None, str] = UNSET,
) -> Response[List[ConsoleEntity]]:
    """Get Clusters

     Gets the console clusters

    Args:
        uuid (str):
        pid (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        entityid (Union[Unset, None, str]):

    Returns:
        Response[List[ConsoleEntity]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        pid=pid,
        name=name,
        entityid=entityid,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    *,
    client: Client,
    pid: Union[Unset, None, str] = UNSET,
    name: Union[Unset, None, str] = UNSET,
    entityid: Union[Unset, None, str] = UNSET,
) -> Optional[List[ConsoleEntity]]:
    """Get Clusters

     Gets the console clusters

    Args:
        uuid (str):
        pid (Union[Unset, None, str]):
        name (Union[Unset, None, str]):
        entityid (Union[Unset, None, str]):

    Returns:
        Response[List[ConsoleEntity]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            pid=pid,
            name=name,
            entityid=entityid,
        )
    ).parsed
