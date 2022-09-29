from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error_object import ErrorObject
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    client: AuthenticatedClient,
    show_invisible_nodes: Union[Unset, None, bool] = True,
    show_hosts: Union[Unset, None, bool] = True,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/Hierarchy".format(client.base_url, uuid=uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["showInvisibleNodes"] = show_invisible_nodes

    params["showHosts"] = show_hosts

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ErrorObject]:
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


def _build_response(*, response: httpx.Response) -> Response[ErrorObject]:
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
    show_invisible_nodes: Union[Unset, None, bool] = True,
    show_hosts: Union[Unset, None, bool] = True,
) -> Response[ErrorObject]:
    """Get the hierarchy of vCenter containers and hosts(excluding folders)

     Get the vCenter tree hierarchy

    Args:
        uuid (str):
        show_invisible_nodes (Union[Unset, None, bool]):  Default: True.
        show_hosts (Union[Unset, None, bool]):  Default: True.

    Returns:
        Response[ErrorObject]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        show_invisible_nodes=show_invisible_nodes,
        show_hosts=show_hosts,
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
    show_invisible_nodes: Union[Unset, None, bool] = True,
    show_hosts: Union[Unset, None, bool] = True,
) -> Optional[ErrorObject]:
    """Get the hierarchy of vCenter containers and hosts(excluding folders)

     Get the vCenter tree hierarchy

    Args:
        uuid (str):
        show_invisible_nodes (Union[Unset, None, bool]):  Default: True.
        show_hosts (Union[Unset, None, bool]):  Default: True.

    Returns:
        Response[ErrorObject]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        show_invisible_nodes=show_invisible_nodes,
        show_hosts=show_hosts,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    show_invisible_nodes: Union[Unset, None, bool] = True,
    show_hosts: Union[Unset, None, bool] = True,
) -> Response[ErrorObject]:
    """Get the hierarchy of vCenter containers and hosts(excluding folders)

     Get the vCenter tree hierarchy

    Args:
        uuid (str):
        show_invisible_nodes (Union[Unset, None, bool]):  Default: True.
        show_hosts (Union[Unset, None, bool]):  Default: True.

    Returns:
        Response[ErrorObject]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        show_invisible_nodes=show_invisible_nodes,
        show_hosts=show_hosts,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
    show_invisible_nodes: Union[Unset, None, bool] = True,
    show_hosts: Union[Unset, None, bool] = True,
) -> Optional[ErrorObject]:
    """Get the hierarchy of vCenter containers and hosts(excluding folders)

     Get the vCenter tree hierarchy

    Args:
        uuid (str):
        show_invisible_nodes (Union[Unset, None, bool]):  Default: True.
        show_hosts (Union[Unset, None, bool]):  Default: True.

    Returns:
        Response[ErrorObject]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            show_invisible_nodes=show_invisible_nodes,
            show_hosts=show_hosts,
        )
    ).parsed
