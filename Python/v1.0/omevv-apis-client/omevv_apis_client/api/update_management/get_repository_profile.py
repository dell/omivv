from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error_object import ErrorObject
from ...models.repository_profile import RepositoryProfile
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/RepositoryProfiles/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorObject, RepositoryProfile]]:
    if response.status_code == 200:
        response_200 = RepositoryProfile.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorObject.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ErrorObject.from_dict(response.json())

        return response_401
    if response.status_code == 500:
        response_500 = ErrorObject.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorObject, RepositoryProfile]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorObject, RepositoryProfile]]:
    """Get repository profile

    Args:
        id (int):

    Returns:
        Response[Union[ErrorObject, RepositoryProfile]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorObject, RepositoryProfile]]:
    """Get repository profile

    Args:
        id (int):

    Returns:
        Response[Union[ErrorObject, RepositoryProfile]]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorObject, RepositoryProfile]]:
    """Get repository profile

    Args:
        id (int):

    Returns:
        Response[Union[ErrorObject, RepositoryProfile]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorObject, RepositoryProfile]]:
    """Get repository profile

    Args:
        id (int):

    Returns:
        Response[Union[ErrorObject, RepositoryProfile]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
