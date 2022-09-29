from typing import Any, Dict, List

import httpx

from ...client import Client
from ...models.override_severity_dto import OverrideSeverityDto
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: List[OverrideSeverityDto],
) -> Dict[str, Any]:
    url = "{}/Settings/OverrideSeverity".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = []
    for json_body_item_data in json_body:
        json_body_item = json_body_item_data.to_dict()

        json_json_body.append(json_body_item)

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    json_body: List[OverrideSeverityDto],
) -> Response[Any]:
    """Update the override severity settings

     Update the override severity settings

    Args:
        json_body (List[OverrideSeverityDto]):

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    *,
    client: Client,
    json_body: List[OverrideSeverityDto],
) -> Response[Any]:
    """Update the override severity settings

     Update the override severity settings

    Args:
        json_body (List[OverrideSeverityDto]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
