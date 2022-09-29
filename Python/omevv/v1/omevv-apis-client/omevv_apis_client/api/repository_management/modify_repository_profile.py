from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.error_object import ErrorObject
from ...models.modify_repository_profile_request import ModifyRepositoryProfileRequest
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: Client,
    json_body: ModifyRepositoryProfileRequest,
) -> Dict[str, Any]:
    url = "{}/RepositoryProfiles/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorObject, int]]:
    if response.status_code == 200:
        response_200 = cast(int, response.json())
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


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorObject, int]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Client,
    json_body: ModifyRepositoryProfileRequest,
) -> Response[Union[ErrorObject, int]]:
    """Modify a repository profile

     Modify a repository profile in OMEVV

    Args:
        id (int):
        json_body (ModifyRepositoryProfileRequest): Model having repository details

    Returns:
        Response[Union[ErrorObject, int]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: int,
    *,
    client: Client,
    json_body: ModifyRepositoryProfileRequest,
) -> Optional[Union[ErrorObject, int]]:
    """Modify a repository profile

     Modify a repository profile in OMEVV

    Args:
        id (int):
        json_body (ModifyRepositoryProfileRequest): Model having repository details

    Returns:
        Response[Union[ErrorObject, int]]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Client,
    json_body: ModifyRepositoryProfileRequest,
) -> Response[Union[ErrorObject, int]]:
    """Modify a repository profile

     Modify a repository profile in OMEVV

    Args:
        id (int):
        json_body (ModifyRepositoryProfileRequest): Model having repository details

    Returns:
        Response[Union[ErrorObject, int]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: int,
    *,
    client: Client,
    json_body: ModifyRepositoryProfileRequest,
) -> Optional[Union[ErrorObject, int]]:
    """Modify a repository profile

     Modify a repository profile in OMEVV

    Args:
        id (int):
        json_body (ModifyRepositoryProfileRequest): Model having repository details

    Returns:
        Response[Union[ErrorObject, int]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
