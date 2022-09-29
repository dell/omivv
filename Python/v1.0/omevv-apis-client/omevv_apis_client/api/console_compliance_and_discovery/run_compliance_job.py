from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.compliance_job_request import ComplianceJobRequest
from ...models.error_object import ErrorObject
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    client: AuthenticatedClient,
    json_body: ComplianceJobRequest,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/Hosts/RunCompliance".format(client.base_url, uuid=uuid)

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
    if response.status_code == 202:
        response_202 = cast(int, response.json())
        return response_202
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


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorObject, int]]:
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
    json_body: ComplianceJobRequest,
) -> Response[Union[ErrorObject, int]]:
    """run compliance job for selected hosts

     Create Job request to run compliance job for selected hosts

    Args:
        uuid (str):
        json_body (ComplianceJobRequest):

    Returns:
        Response[Union[ErrorObject, int]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        json_body=json_body,
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
    json_body: ComplianceJobRequest,
) -> Optional[Union[ErrorObject, int]]:
    """run compliance job for selected hosts

     Create Job request to run compliance job for selected hosts

    Args:
        uuid (str):
        json_body (ComplianceJobRequest):

    Returns:
        Response[Union[ErrorObject, int]]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    json_body: ComplianceJobRequest,
) -> Response[Union[ErrorObject, int]]:
    """run compliance job for selected hosts

     Create Job request to run compliance job for selected hosts

    Args:
        uuid (str):
        json_body (ComplianceJobRequest):

    Returns:
        Response[Union[ErrorObject, int]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
    json_body: ComplianceJobRequest,
) -> Optional[Union[ErrorObject, int]]:
    """run compliance job for selected hosts

     Create Job request to run compliance job for selected hosts

    Args:
        uuid (str):
        json_body (ComplianceJobRequest):

    Returns:
        Response[Union[ErrorObject, int]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            json_body=json_body,
        )
    ).parsed
