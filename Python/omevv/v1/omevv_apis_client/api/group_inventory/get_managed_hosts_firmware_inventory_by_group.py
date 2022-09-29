from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.group_firmware_inventory_collection_model import GroupFirmwareInventoryCollectionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    omevv_group_id: int,
    *,
    client: Client,
    skip: Union[Unset, None, int] = UNSET,
    top: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/Groups/{omevv_group_id}/FirmwareInventoryDetails".format(
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


def _parse_response(*, response: httpx.Response) -> Optional[GroupFirmwareInventoryCollectionModel]:
    if response.status_code == 200:
        response_200 = GroupFirmwareInventoryCollectionModel.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[GroupFirmwareInventoryCollectionModel]:
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
) -> Response[GroupFirmwareInventoryCollectionModel]:
    """Get Host Inventory for a group

     Get Host Inventory based on OMEVV group id provided

    Args:
        uuid (str):
        omevv_group_id (int):
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Returns:
        Response[GroupFirmwareInventoryCollectionModel]
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
) -> Optional[GroupFirmwareInventoryCollectionModel]:
    """Get Host Inventory for a group

     Get Host Inventory based on OMEVV group id provided

    Args:
        uuid (str):
        omevv_group_id (int):
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Returns:
        Response[GroupFirmwareInventoryCollectionModel]
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
) -> Response[GroupFirmwareInventoryCollectionModel]:
    """Get Host Inventory for a group

     Get Host Inventory based on OMEVV group id provided

    Args:
        uuid (str):
        omevv_group_id (int):
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Returns:
        Response[GroupFirmwareInventoryCollectionModel]
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
) -> Optional[GroupFirmwareInventoryCollectionModel]:
    """Get Host Inventory for a group

     Get Host Inventory based on OMEVV group id provided

    Args:
        uuid (str):
        omevv_group_id (int):
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):

    Returns:
        Response[GroupFirmwareInventoryCollectionModel]
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
