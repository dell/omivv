from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.create_repository_profile_request import CreateRepositoryProfileRequest
from ...models.error_object import ErrorObject
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: CreateRepositoryProfileRequest,
) -> Dict[str, Any]:
    url = "{}/RepositoryProfiles".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
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
    *,
    client: AuthenticatedClient,
    json_body: CreateRepositoryProfileRequest,
) -> Response[Union[ErrorObject, int]]:
    """Create a repository profile

     Create a repository profile in OMEVV

    Args:
        json_body (CreateRepositoryProfileRequest): Model for creating the repository profile

    Returns:
        Response[Union[ErrorObject, int]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: CreateRepositoryProfileRequest,
) -> Optional[Union[ErrorObject, int]]:
    """Create a repository profile

     Create a repository profile in OMEVV

    Args:
        json_body (CreateRepositoryProfileRequest): Model for creating the repository profile

    Returns:
        Response[Union[ErrorObject, int]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CreateRepositoryProfileRequest,
) -> Response[Union[ErrorObject, int]]:
    """Create a repository profile

     Create a repository profile in OMEVV

    Args:
        json_body (CreateRepositoryProfileRequest): Model for creating the repository profile

    Returns:
        Response[Union[ErrorObject, int]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: CreateRepositoryProfileRequest,
) -> Optional[Union[ErrorObject, int]]:
    """Create a repository profile

     Create a repository profile in OMEVV

    Args:
        json_body (CreateRepositoryProfileRequest): Model for creating the repository profile

    Returns:
        Response[Union[ErrorObject, int]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
