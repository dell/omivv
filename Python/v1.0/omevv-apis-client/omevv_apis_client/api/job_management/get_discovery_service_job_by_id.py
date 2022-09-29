from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error_object import ErrorObject
from ...models.job import Job
from ...types import Response


def _get_kwargs(
    uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/DiscoveryJobs/{id}".format(client.base_url, uuid=uuid, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorObject, Job]]:
    if response.status_code == 200:
        response_200 = Job.from_dict(response.json())

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
    if response.status_code == 500:
        response_500 = ErrorObject.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorObject, Job]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorObject, Job]]:
    """Get  Job  job by id

     Gets the jobdetails job by id

    Args:
        uuid (str):
        id (int):

    Returns:
        Response[Union[ErrorObject, Job]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        id=id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorObject, Job]]:
    """Get  Job  job by id

     Gets the jobdetails job by id

    Args:
        uuid (str):
        id (int):

    Returns:
        Response[Union[ErrorObject, Job]]
    """

    return sync_detailed(
        uuid=uuid,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorObject, Job]]:
    """Get  Job  job by id

     Gets the jobdetails job by id

    Args:
        uuid (str):
        id (int):

    Returns:
        Response[Union[ErrorObject, Job]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[ErrorObject, Job]]:
    """Get  Job  job by id

     Gets the jobdetails job by id

    Args:
        uuid (str):
        id (int):

    Returns:
        Response[Union[ErrorObject, Job]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            id=id,
            client=client,
        )
    ).parsed
