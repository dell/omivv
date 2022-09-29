from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error_object import ErrorObject
from ...models.get_managed_hosts_maintenance_mode import GetManagedHostsMaintenanceMode
from ...models.managed_host import ManagedHost
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    client: AuthenticatedClient,
    maintenance_mode: Union[Unset, None, GetManagedHostsMaintenanceMode] = UNSET,
    service_tag: Union[Unset, None, str] = UNSET,
    console_entity_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/ManagedHosts".format(client.base_url, uuid=uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_maintenance_mode: Union[Unset, None, str] = UNSET
    if not isinstance(maintenance_mode, Unset):
        json_maintenance_mode = maintenance_mode.value if maintenance_mode else None

    params["maintenanceMode"] = json_maintenance_mode

    params["serviceTag"] = service_tag

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorObject, List[ManagedHost]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ManagedHost.from_dict(response_200_item_data)

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
    if response.status_code == 500:
        response_500 = ErrorObject.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorObject, List[ManagedHost]]]:
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
    maintenance_mode: Union[Unset, None, GetManagedHostsMaintenanceMode] = UNSET,
    service_tag: Union[Unset, None, str] = UNSET,
    console_entity_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorObject, List[ManagedHost]]]:
    """Get all hosts managed in OMEVV

     Get all the hosts managed in OMEVV

    Args:
        uuid (str):
        maintenance_mode (Union[Unset, None, GetManagedHostsMaintenanceMode]):
        service_tag (Union[Unset, None, str]):
        console_entity_id (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorObject, List[ManagedHost]]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        maintenance_mode=maintenance_mode,
        service_tag=service_tag,
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
    maintenance_mode: Union[Unset, None, GetManagedHostsMaintenanceMode] = UNSET,
    service_tag: Union[Unset, None, str] = UNSET,
    console_entity_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorObject, List[ManagedHost]]]:
    """Get all hosts managed in OMEVV

     Get all the hosts managed in OMEVV

    Args:
        uuid (str):
        maintenance_mode (Union[Unset, None, GetManagedHostsMaintenanceMode]):
        service_tag (Union[Unset, None, str]):
        console_entity_id (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorObject, List[ManagedHost]]]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        maintenance_mode=maintenance_mode,
        service_tag=service_tag,
        console_entity_id=console_entity_id,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    maintenance_mode: Union[Unset, None, GetManagedHostsMaintenanceMode] = UNSET,
    service_tag: Union[Unset, None, str] = UNSET,
    console_entity_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[ErrorObject, List[ManagedHost]]]:
    """Get all hosts managed in OMEVV

     Get all the hosts managed in OMEVV

    Args:
        uuid (str):
        maintenance_mode (Union[Unset, None, GetManagedHostsMaintenanceMode]):
        service_tag (Union[Unset, None, str]):
        console_entity_id (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorObject, List[ManagedHost]]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        maintenance_mode=maintenance_mode,
        service_tag=service_tag,
        console_entity_id=console_entity_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
    maintenance_mode: Union[Unset, None, GetManagedHostsMaintenanceMode] = UNSET,
    service_tag: Union[Unset, None, str] = UNSET,
    console_entity_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[ErrorObject, List[ManagedHost]]]:
    """Get all hosts managed in OMEVV

     Get all the hosts managed in OMEVV

    Args:
        uuid (str):
        maintenance_mode (Union[Unset, None, GetManagedHostsMaintenanceMode]):
        service_tag (Union[Unset, None, str]):
        console_entity_id (Union[Unset, None, str]):

    Returns:
        Response[Union[ErrorObject, List[ManagedHost]]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            maintenance_mode=maintenance_mode,
            service_tag=service_tag,
            console_entity_id=console_entity_id,
        )
    ).parsed
