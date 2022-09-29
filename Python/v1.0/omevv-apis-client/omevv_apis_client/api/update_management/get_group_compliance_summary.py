from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.error_object import ErrorObject
from ...models.group_compliance_summary_report import GroupComplianceSummaryReport
from ...models.group_compliance_summary_request import GroupComplianceSummaryRequest
from ...types import Response


def _get_kwargs(
    uuid: str,
    *,
    client: Client,
    json_body: GroupComplianceSummaryRequest,
) -> Dict[str, Any]:
    url = "{}/Consoles/{uuid}/getGroupComplianceSummary".format(client.base_url, uuid=uuid)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorObject, List[GroupComplianceSummaryReport]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GroupComplianceSummaryReport.from_dict(response_200_item_data)

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
    if response.status_code == 500:
        response_500 = ErrorObject.from_dict(response.json())

        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorObject, List[GroupComplianceSummaryReport]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    uuid: str,
    *,
    client: Client,
    json_body: GroupComplianceSummaryRequest,
) -> Response[Union[ErrorObject, List[GroupComplianceSummaryReport]]]:
    """Get  the drift compliance summary for specified groups(clusters)

     Get  group compliance summary by groupids

    Args:
        uuid (str):
        json_body (GroupComplianceSummaryRequest):

    Returns:
        Response[Union[ErrorObject, List[GroupComplianceSummaryReport]]]
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
    client: Client,
    json_body: GroupComplianceSummaryRequest,
) -> Optional[Union[ErrorObject, List[GroupComplianceSummaryReport]]]:
    """Get  the drift compliance summary for specified groups(clusters)

     Get  group compliance summary by groupids

    Args:
        uuid (str):
        json_body (GroupComplianceSummaryRequest):

    Returns:
        Response[Union[ErrorObject, List[GroupComplianceSummaryReport]]]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: Client,
    json_body: GroupComplianceSummaryRequest,
) -> Response[Union[ErrorObject, List[GroupComplianceSummaryReport]]]:
    """Get  the drift compliance summary for specified groups(clusters)

     Get  group compliance summary by groupids

    Args:
        uuid (str):
        json_body (GroupComplianceSummaryRequest):

    Returns:
        Response[Union[ErrorObject, List[GroupComplianceSummaryReport]]]
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
    client: Client,
    json_body: GroupComplianceSummaryRequest,
) -> Optional[Union[ErrorObject, List[GroupComplianceSummaryReport]]]:
    """Get  the drift compliance summary for specified groups(clusters)

     Get  group compliance summary by groupids

    Args:
        uuid (str):
        json_body (GroupComplianceSummaryRequest):

    Returns:
        Response[Union[ErrorObject, List[GroupComplianceSummaryReport]]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            json_body=json_body,
        )
    ).parsed
