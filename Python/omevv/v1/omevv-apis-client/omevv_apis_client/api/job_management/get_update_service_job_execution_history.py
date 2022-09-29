from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.error_object import ErrorObject
from ...models.job_execution_history import JobExecutionHistory
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/TestConnectionJobs/{id}/ExecutionHistories".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorObject, List[JobExecutionHistory]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = JobExecutionHistory.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ErrorObject.from_dict(response.json())

        return response_400
    if response.status_code == 500:
        response_500 = ErrorObject.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorObject, List[JobExecutionHistory]]]:
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
) -> Response[Union[ErrorObject, List[JobExecutionHistory]]]:
    """Get  Update Service  job by id

     Gets the list of  the update service job by id

    Args:
        id (int):

    Returns:
        Response[Union[ErrorObject, List[JobExecutionHistory]]]
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
) -> Optional[Union[ErrorObject, List[JobExecutionHistory]]]:
    """Get  Update Service  job by id

     Gets the list of  the update service job by id

    Args:
        id (int):

    Returns:
        Response[Union[ErrorObject, List[JobExecutionHistory]]]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[ErrorObject, List[JobExecutionHistory]]]:
    """Get  Update Service  job by id

     Gets the list of  the update service job by id

    Args:
        id (int):

    Returns:
        Response[Union[ErrorObject, List[JobExecutionHistory]]]
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
) -> Optional[Union[ErrorObject, List[JobExecutionHistory]]]:
    """Get  Update Service  job by id

     Gets the list of  the update service job by id

    Args:
        id (int):

    Returns:
        Response[Union[ErrorObject, List[JobExecutionHistory]]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
