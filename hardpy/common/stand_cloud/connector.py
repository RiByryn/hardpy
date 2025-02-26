# Copyright (c) 2024 Everypin
# GNU General Public License v3.0 (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from logging import getLogger
from typing import TYPE_CHECKING

from oauthlib.oauth2.rfc6749.errors import (
    InvalidGrantError,
    MissingTokenError,
    TokenExpiredError,
)
from requests.exceptions import (
    ConnectionError as RequestConnectionError,
    HTTPError,
    InvalidURL,
)
from requests_oauth2client import ApiClient, BearerToken
from requests_oauth2client.tokens import ExpiredAccessToken
from requests_oauthlib import OAuth2Session

from hardpy.common.stand_cloud.exception import StandCloudError
from hardpy.common.stand_cloud.token_storage import get_token_store

if TYPE_CHECKING:
    from requests import Response


class StandCloudConnector:
    """StandCloud API connector."""

    def __init__(
        self,
        addr: str,
    ) -> None:
        """Create StandCLoud loader.

        Args:
            addr (str | None, optional): StandCloud address.
            The option only for development and debug. Defaults to True.
        """
        self._api_addr = addr + "/api/v1"
        self._auth_addr = "/auth"
        self._api_url = f"https://{self._api_addr}/"
        self._verify_ssl = not __debug__
        self._log = getLogger(__name__)

    def get_api(self, endpoint: str) -> ApiClient:
        """Get StandCloud API client.

        Args:
            endpoint (str): endpoint address.

        Returns:
            ApiClient: API clinet
        """
        return self._get_api(endpoint)

    def healthcheck(self) -> Response:
        """Healthcheck of StandCloud API.

        Returns:
            Response: healthcheck response

        Raises:
            StandCloudError: if StandCloud is unavailable
        """
        api = self._get_api("healthcheck")

        try:
            resp = api.get(verify=self._verify_ssl)
        except ExpiredAccessToken as exc:
            raise StandCloudError(str(exc))
        except TokenExpiredError as exc:
            raise StandCloudError(exc.description)
        except InvalidGrantError as exc:
            raise StandCloudError(exc.description)
        except HTTPError as exc:
            raise StandCloudError(exc.strerror) # type: ignore

        return resp

    def _token_update(self, token: BearerToken) -> None:
        storage_keyring, mem_keyring = get_token_store()

        _access_token = "access_token"  # noqa: S105
        _expires_at = "expires_at"
        _refresh_token = "refresh_token"  # noqa: S105
        _hardpy = "HardPy"

        storage_keyring.set_password(_hardpy, _refresh_token, token[_refresh_token])
        mem_keyring.set_password(_hardpy, _access_token, token[_access_token])

        token_data = {
            _access_token: token[_access_token],
            _expires_at: token[_expires_at],
        }

        mem_keyring.set_password(_hardpy, _access_token, json.dumps(token_data))

    def _get_expires_in(self, expires_at: float | None) -> int:
        if expires_at is None:
            return -1
        expires_at_datetime = datetime.fromtimestamp(expires_at, timezone.utc)

        now_datetime = datetime.now(timezone.utc)

        expires_in_datetime = expires_at_datetime - now_datetime
        return int(expires_in_datetime.total_seconds())

    def _get_access_token_info(self) -> tuple[str | None, float | None]:
        _, mem_keyring = get_token_store()

        _access_token = "access_token"  # noqa: S105
        _expires_at = "expires_at"

        token_info = mem_keyring.get_password("HardPy", _access_token)
        if token_info is None:
            return None, None
        token_dict = json.loads(token_info)
        access_token = token_dict[_access_token]
        expired_at = token_dict[_expires_at]

        return access_token, expired_at

    def _get_refresh_token(self) -> str | None:
        (storage_keyring, _) = get_token_store()

        refresh_token = storage_keyring.get_password("HardPy", "refresh_token")
        self._log.debug("Got refresh token from the storage keyring")
        return refresh_token

    def _get_api(self, endpoint: str) -> ApiClient:
        token = self._get_token()
        client_id = "hardpy-report-uploader"

        extra = {
            "client_id": client_id,
            "audience": self._api_url,
            "redirect_uri": "http://localhost/oauth2/callback",
        }

        session = OAuth2Session(
            client_id,
            token=token.as_dict(),
            token_updater=self._token_update,
        )

        is_need_refresh = False
        early_refresh = timedelta(seconds=30)

        if token.expires_in and token.expires_in < early_refresh.seconds:
            is_need_refresh = True

        if token.access_token is None:
            self._log.debug("Want to refresh token since don't have access token")
            is_need_refresh = True

        if is_need_refresh:
            try:
                ret = session.refresh_token(
                    token_url=f"https://{self._auth_addr}/api/oidc/token",
                    refresh_token=self._get_refresh_token(),
                    verify=False,
                    **extra,
                )
            except InvalidGrantError as exc:
                raise StandCloudError(exc.description)
            except RequestConnectionError as exc:
                raise StandCloudError(exc.strerror)  # type: ignore
            except MissingTokenError as exc:
                raise StandCloudError(exc.description)
            except InvalidURL:
                msg = "Authentication URL is not available"
                raise StandCloudError(msg)
            self._token_update(ret)  # type: ignore

        return ApiClient(self._api_url + endpoint, session=session, timeout=10)

    def _get_token(self) -> BearerToken:
        access_token, expires_at = self._get_access_token_info()
        expires_in = self._get_expires_in(expires_at)

        return BearerToken(
            scope=["authelia.bearer.authz", "offline_access"],
            token_type="bearer",  # noqa: S106
            access_token=access_token,
            expires_at=expires_at,
            expires_in=expires_in,
        )
