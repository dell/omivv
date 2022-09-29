from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.package_info import PackageInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pkg: str,
    *,
    client: Client,
    pkg_version: Union[Unset, None, str] = UNSET,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/vsphere-lcm/hw-support/v1/packages/{pkg}".format(client.base_url, pkg=pkg)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(v_center_instance_guid, Unset):
        headers["VCenter-Instance-GUID"] = v_center_instance_guid

    params: Dict[str, Any] = {}
    params["pkgVersion"] = pkg_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[ErrorResponse, PackageInfo]]:
    if response.status_code == 200:
        response_200 = PackageInfo.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if response.status_code == 503:
        response_503 = ErrorResponse.from_dict(response.json())

        return response_503
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[ErrorResponse, PackageInfo]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    pkg: str,
    *,
    client: Client,
    pkg_version: Union[Unset, None, str] = UNSET,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, PackageInfo]]:
    """Retrieve the information for a particular HW support package

    Args:
        pkg (str):
        pkg_version (Union[Unset, None, str]):
        v_center_instance_guid (Union[Unset, str]):

    Returns:
        Response[Union[ErrorResponse, PackageInfo]]
    """

    kwargs = _get_kwargs(
        pkg=pkg,
        client=client,
        pkg_version=pkg_version,
        v_center_instance_guid=v_center_instance_guid,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    pkg: str,
    *,
    client: Client,
    pkg_version: Union[Unset, None, str] = UNSET,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, PackageInfo]]:
    """Retrieve the information for a particular HW support package

    Args:
        pkg (str):
        pkg_version (Union[Unset, None, str]):
        v_center_instance_guid (Union[Unset, str]):

    Returns:
        Response[Union[ErrorResponse, PackageInfo]]
    """

    return sync_detailed(
        pkg=pkg,
        client=client,
        pkg_version=pkg_version,
        v_center_instance_guid=v_center_instance_guid,
    ).parsed


async def asyncio_detailed(
    pkg: str,
    *,
    client: Client,
    pkg_version: Union[Unset, None, str] = UNSET,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, PackageInfo]]:
    """Retrieve the information for a particular HW support package

    Args:
        pkg (str):
        pkg_version (Union[Unset, None, str]):
        v_center_instance_guid (Union[Unset, str]):

    Returns:
        Response[Union[ErrorResponse, PackageInfo]]
    """

    kwargs = _get_kwargs(
        pkg=pkg,
        client=client,
        pkg_version=pkg_version,
        v_center_instance_guid=v_center_instance_guid,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    pkg: str,
    *,
    client: Client,
    pkg_version: Union[Unset, None, str] = UNSET,
    v_center_instance_guid: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, PackageInfo]]:
    """Retrieve the information for a particular HW support package

    Args:
        pkg (str):
        pkg_version (Union[Unset, None, str]):
        v_center_instance_guid (Union[Unset, str]):

    Returns:
        Response[Union[ErrorResponse, PackageInfo]]
    """

    return (
        await asyncio_detailed(
            pkg=pkg,
            client=client,
            pkg_version=pkg_version,
            v_center_instance_guid=v_center_instance_guid,
        )
    ).parsed
