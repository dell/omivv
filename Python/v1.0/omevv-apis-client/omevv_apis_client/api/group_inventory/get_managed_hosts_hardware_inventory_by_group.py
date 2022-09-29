from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error_object import ErrorObject
from ...models.group_hardware_inventory_collection_model import GroupHardwareInventoryCollectionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    omevv_group_id: int,
    *,
    client: Client,
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/Groups/{omevv_group_id}/HardwareDetails".format(
        client.base_url, uuid=uuid, omevv_group_id=omevv_group_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["skip"] = skip

    params["top"] = top

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorObject, GroupHardwareInventoryCollectionModel]]:
    if response.status_code == 200:
        response_200 = GroupHardwareInventoryCollectionModel.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorObject, GroupHardwareInventoryCollectionModel]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    uuid: str,
    omevv_group_id: int,
    *,
    client: Client,
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[Union[ErrorObject, GroupHardwareInventoryCollectionModel]]:
    """Get Host Hardware Inventory for a group

     Get Host Hardware Inventory based on OMEVV group id provided

    Args:
        uuid (str):
        omevv_group_id (int):
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Returns:
        Response[Union[ErrorObject, GroupHardwareInventoryCollectionModel]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        omevv_group_id=omevv_group_id,
        client=client,
        skip=skip,
        top=top,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    uuid: str,
    omevv_group_id: int,
    *,
    client: Client,
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ErrorObject, GroupHardwareInventoryCollectionModel]]:
    """Get Host Hardware Inventory for a group

     Get Host Hardware Inventory based on OMEVV group id provided

    Args:
        uuid (str):
        omevv_group_id (int):
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Returns:
        Response[Union[ErrorObject, GroupHardwareInventoryCollectionModel]]
    """

    return sync_detailed(
        uuid=uuid,
        omevv_group_id=omevv_group_id,
        client=client,
        skip=skip,
        top=top,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    omevv_group_id: int,
    *,
    client: Client,
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Response[Union[ErrorObject, GroupHardwareInventoryCollectionModel]]:
    """Get Host Hardware Inventory for a group

     Get Host Hardware Inventory based on OMEVV group id provided

    Args:
        uuid (str):
        omevv_group_id (int):
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Returns:
        Response[Union[ErrorObject, GroupHardwareInventoryCollectionModel]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        omevv_group_id=omevv_group_id,
        client=client,
        skip=skip,
        top=top,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    omevv_group_id: int,
    *,
    client: Client,
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Optional[Union[ErrorObject, GroupHardwareInventoryCollectionModel]]:
    """Get Host Hardware Inventory for a group

     Get Host Hardware Inventory based on OMEVV group id provided

    Args:
        uuid (str):
        omevv_group_id (int):
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Returns:
        Response[Union[ErrorObject, GroupHardwareInventoryCollectionModel]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            omevv_group_id=omevv_group_id,
            client=client,
            skip=skip,
            top=top,
        )
    ).parsed
