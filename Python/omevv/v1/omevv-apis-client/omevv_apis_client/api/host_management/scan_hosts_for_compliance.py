from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.multi_host_request import MultiHostRequest
from ...models.request_accepted_response import RequestAcceptedResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: MultiHostRequest,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/vsphere-lcm/hw-support/v1/hosts".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(v_center_instance_guid, Unset):
        headers["VCenter-Instance-GUID"] = v_center_instance_guid

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorResponse, RequestAcceptedResponse]]:
    if response.status_code == 202:
        response_202 = RequestAcceptedResponse.from_dict(response.json())

        return response_202
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409
    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorResponse, RequestAcceptedResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: MultiHostRequest,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, RequestAcceptedResponse]]:
    """Scan a set of hosts for firmware compliance and report remediation impact

    Args:
        v_center_instance_guid (Union[Unset, str]):
        json_body (MultiHostRequest):

    Returns:
        Response[Union[ErrorResponse, RequestAcceptedResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        v_center_instance_guid=v_center_instance_guid,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: MultiHostRequest,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, RequestAcceptedResponse]]:
    """Scan a set of hosts for firmware compliance and report remediation impact

    Args:
        v_center_instance_guid (Union[Unset, str]):
        json_body (MultiHostRequest):

    Returns:
        Response[Union[ErrorResponse, RequestAcceptedResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        v_center_instance_guid=v_center_instance_guid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: MultiHostRequest,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, RequestAcceptedResponse]]:
    """Scan a set of hosts for firmware compliance and report remediation impact

    Args:
        v_center_instance_guid (Union[Unset, str]):
        json_body (MultiHostRequest):

    Returns:
        Response[Union[ErrorResponse, RequestAcceptedResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        v_center_instance_guid=v_center_instance_guid,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: MultiHostRequest,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, RequestAcceptedResponse]]:
    """Scan a set of hosts for firmware compliance and report remediation impact

    Args:
        v_center_instance_guid (Union[Unset, str]):
        json_body (MultiHostRequest):

    Returns:
        Response[Union[ErrorResponse, RequestAcceptedResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            v_center_instance_guid=v_center_instance_guid,
        )
    ).parsed
