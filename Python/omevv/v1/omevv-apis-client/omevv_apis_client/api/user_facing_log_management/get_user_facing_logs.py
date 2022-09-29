import datetime
from typing import Any, Dict, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.get_user_facing_logs_log_level import GetUserFacingLogsLogLevel
from ...models.get_user_facing_logs_sort_by import GetUserFacingLogsSortBy
from ...models.get_user_facing_logs_sort_order import GetUserFacingLogsSortOrder
from ...models.user_facing_logs_page import UserFacingLogsPage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, None, int] = 0,
    top: Union[Unset, None, int] = 100,
    log_level: Union[Unset, None, GetUserFacingLogsLogLevel] = GetUserFacingLogsLogLevel.ALL,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
    sort_by: Union[Unset, None, GetUserFacingLogsSortBy] = GetUserFacingLogsSortBy.CREATEDDATE,
    sort_order: Union[Unset, None, GetUserFacingLogsSortOrder] = GetUserFacingLogsSortOrder.ASC,
) -> Dict[str, Any]:
    url = "{}/UserFacingLogs".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["skip"] = skip

    params["top"] = top

    json_log_level: Union[Unset, None, str] = UNSET
    if not isinstance(log_level, Unset):
        json_log_level = log_level.value if log_level else None

    params["logLevel"] = json_log_level

    json_start_date: Union[Unset, None, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat() if start_date else None

    params["startDate"] = json_start_date

    json_end_date: Union[Unset, None, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat() if end_date else None

    params["endDate"] = json_end_date

    json_sort_by: Union[Unset, None, str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value if sort_by else None

    params["sortBy"] = json_sort_by

    json_sort_order: Union[Unset, None, str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = sort_order.value if sort_order else None

    params["sortOrder"] = json_sort_order

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[UserFacingLogsPage]:
    if response.status_code == 200:
        response_200 = UserFacingLogsPage.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[UserFacingLogsPage]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, None, int] = 0,
    top: Union[Unset, None, int] = 100,
    log_level: Union[Unset, None, GetUserFacingLogsLogLevel] = GetUserFacingLogsLogLevel.ALL,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
    sort_by: Union[Unset, None, GetUserFacingLogsSortBy] = GetUserFacingLogsSortBy.CREATEDDATE,
    sort_order: Union[Unset, None, GetUserFacingLogsSortOrder] = GetUserFacingLogsSortOrder.ASC,
) -> Response[UserFacingLogsPage]:
    """Get User Facing Log Messages

    Args:
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):  Default: 100.
        log_level (Union[Unset, None, GetUserFacingLogsLogLevel]):  Default:
            GetUserFacingLogsLogLevel.ALL.
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):
        sort_by (Union[Unset, None, GetUserFacingLogsSortBy]):  Default:
            GetUserFacingLogsSortBy.CREATEDDATE.
        sort_order (Union[Unset, None, GetUserFacingLogsSortOrder]):  Default:
            GetUserFacingLogsSortOrder.ASC.

    Returns:
        Response[UserFacingLogsPage]
    """

    kwargs = _get_kwargs(
        client=client,
        skip=skip,
        top=top,
        log_level=log_level,
        start_date=start_date,
        end_date=end_date,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, None, int] = 0,
    top: Union[Unset, None, int] = 100,
    log_level: Union[Unset, None, GetUserFacingLogsLogLevel] = GetUserFacingLogsLogLevel.ALL,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
    sort_by: Union[Unset, None, GetUserFacingLogsSortBy] = GetUserFacingLogsSortBy.CREATEDDATE,
    sort_order: Union[Unset, None, GetUserFacingLogsSortOrder] = GetUserFacingLogsSortOrder.ASC,
) -> Optional[UserFacingLogsPage]:
    """Get User Facing Log Messages

    Args:
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):  Default: 100.
        log_level (Union[Unset, None, GetUserFacingLogsLogLevel]):  Default:
            GetUserFacingLogsLogLevel.ALL.
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):
        sort_by (Union[Unset, None, GetUserFacingLogsSortBy]):  Default:
            GetUserFacingLogsSortBy.CREATEDDATE.
        sort_order (Union[Unset, None, GetUserFacingLogsSortOrder]):  Default:
            GetUserFacingLogsSortOrder.ASC.

    Returns:
        Response[UserFacingLogsPage]
    """

    return sync_detailed(
        client=client,
        skip=skip,
        top=top,
        log_level=log_level,
        start_date=start_date,
        end_date=end_date,
        sort_by=sort_by,
        sort_order=sort_order,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, None, int] = 0,
    top: Union[Unset, None, int] = 100,
    log_level: Union[Unset, None, GetUserFacingLogsLogLevel] = GetUserFacingLogsLogLevel.ALL,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
    sort_by: Union[Unset, None, GetUserFacingLogsSortBy] = GetUserFacingLogsSortBy.CREATEDDATE,
    sort_order: Union[Unset, None, GetUserFacingLogsSortOrder] = GetUserFacingLogsSortOrder.ASC,
) -> Response[UserFacingLogsPage]:
    """Get User Facing Log Messages

    Args:
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):  Default: 100.
        log_level (Union[Unset, None, GetUserFacingLogsLogLevel]):  Default:
            GetUserFacingLogsLogLevel.ALL.
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):
        sort_by (Union[Unset, None, GetUserFacingLogsSortBy]):  Default:
            GetUserFacingLogsSortBy.CREATEDDATE.
        sort_order (Union[Unset, None, GetUserFacingLogsSortOrder]):  Default:
            GetUserFacingLogsSortOrder.ASC.

    Returns:
        Response[UserFacingLogsPage]
    """

    kwargs = _get_kwargs(
        client=client,
        skip=skip,
        top=top,
        log_level=log_level,
        start_date=start_date,
        end_date=end_date,
        sort_by=sort_by,
        sort_order=sort_order,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    skip: Union[Unset, None, int] = 0,
    top: Union[Unset, None, int] = 100,
    log_level: Union[Unset, None, GetUserFacingLogsLogLevel] = GetUserFacingLogsLogLevel.ALL,
    start_date: Union[Unset, None, datetime.datetime] = UNSET,
    end_date: Union[Unset, None, datetime.datetime] = UNSET,
    sort_by: Union[Unset, None, GetUserFacingLogsSortBy] = GetUserFacingLogsSortBy.CREATEDDATE,
    sort_order: Union[Unset, None, GetUserFacingLogsSortOrder] = GetUserFacingLogsSortOrder.ASC,
) -> Optional[UserFacingLogsPage]:
    """Get User Facing Log Messages

    Args:
        skip (Union[Unset, None, int]):
        top (Union[Unset, None, int]):  Default: 100.
        log_level (Union[Unset, None, GetUserFacingLogsLogLevel]):  Default:
            GetUserFacingLogsLogLevel.ALL.
        start_date (Union[Unset, None, datetime.datetime]):
        end_date (Union[Unset, None, datetime.datetime]):
        sort_by (Union[Unset, None, GetUserFacingLogsSortBy]):  Default:
            GetUserFacingLogsSortBy.CREATEDDATE.
        sort_order (Union[Unset, None, GetUserFacingLogsSortOrder]):  Default:
            GetUserFacingLogsSortOrder.ASC.

    Returns:
        Response[UserFacingLogsPage]
    """

    return (
        await asyncio_detailed(
            client=client,
            skip=skip,
            top=top,
            log_level=log_level,
            start_date=start_date,
            end_date=end_date,
            sort_by=sort_by,
            sort_order=sort_order,
        )
    ).parsed
