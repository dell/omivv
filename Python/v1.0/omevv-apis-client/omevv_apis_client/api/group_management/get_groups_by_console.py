from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error_object import ErrorObject
from ...models.get_groups_by_console_group_type import GetGroupsByConsoleGroupType
from ...models.group import Group
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    client: AuthenticatedClient,
    group_type: Union[Unset, None, GetGroupsByConsoleGroupType] = UNSET,
    console_entity_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/Groups".format(client.base_url, uuid=uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_group_type: Union[Unset, None, str] = UNSET
    if not isinstance(group_type, Unset):
        json_group_type = group_type.value if group_type else None

    params["group_type"] = json_group_type

    params["console_entity_id"] = console_entity_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorObject, List[Group]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Group.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ErrorObject.from_dict(response.json())

        return response_400
    if response.status_code == 500:
        response_500 = ErrorObject.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorObject, List[Group]]]:
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
    group_type: Union[Unset, None, GetGroupsByConsoleGroupType] = UNSET,
    console_entity_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorObject, List[Group]]]:
    """Get all groups OMEVV plugin group by Console

     Get all groups of OMEVV plugin

    Args:
        uuid (str):
        group_type (Union[Unset, None, GetGroupsByConsoleGroupType]):
        console_entity_id (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorObject, List[Group]]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        group_type=group_type,
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
    group_type: Union[Unset, None, GetGroupsByConsoleGroupType] = UNSET,
    console_entity_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorObject, List[Group]]]:
    """Get all groups OMEVV plugin group by Console

     Get all groups of OMEVV plugin

    Args:
        uuid (str):
        group_type (Union[Unset, None, GetGroupsByConsoleGroupType]):
        console_entity_id (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorObject, List[Group]]]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        group_type=group_type,
        console_entity_id=console_entity_id,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    group_type: Union[Unset, None, GetGroupsByConsoleGroupType] = UNSET,
    console_entity_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorObject, List[Group]]]:
    """Get all groups OMEVV plugin group by Console

     Get all groups of OMEVV plugin

    Args:
        uuid (str):
        group_type (Union[Unset, None, GetGroupsByConsoleGroupType]):
        console_entity_id (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorObject, List[Group]]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        group_type=group_type,
        console_entity_id=console_entity_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
    group_type: Union[Unset, None, GetGroupsByConsoleGroupType] = UNSET,
    console_entity_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorObject, List[Group]]]:
    """Get all groups OMEVV plugin group by Console

     Get all groups of OMEVV plugin

    Args:
        uuid (str):
        group_type (Union[Unset, None, GetGroupsByConsoleGroupType]):
        console_entity_id (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorObject, List[Group]]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            group_type=group_type,
            console_entity_id=console_entity_id,
        )
    ).parsed
