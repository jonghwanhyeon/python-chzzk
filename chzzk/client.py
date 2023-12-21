from dataclasses import dataclass
from typing import Any, ClassVar, Mapping, Optional
from urllib.parse import urljoin

import httpx

from chzzk.errors import ChzzkHTTPError


@dataclass
class Credential:
    nid_auth: str
    nid_session: str

    def as_cookie(self) -> dict[str, str]:
        return {
            "NID_AUT": self.nid_auth,
            "NID_SES": self.nid_session,
        }


class HTTPClient:
    BASE_URL: ClassVar[str]

    def __init__(self, credential: Optional[Credential] = None):
        assert self.BASE_URL.endswith("/")

        self._credential = credential
        self._client = httpx.AsyncClient()

        if self._credential is not None:
            self._client.cookies.update(self._credential.as_cookie())

    async def request(
        self,
        method: str,
        url: str,
        *,
        params: Optional[Mapping[str, Any]] = None,
        data: Optional[Mapping[str, Any]] = None,
        **kwargs,
    ) -> Any:
        raw_response = await self._client.request(
            method=method,
            url=urljoin(self.BASE_URL, url),
            params=params,
            data=data,
            **kwargs,
        )

        if raw_response.status_code != 200:
            raise ChzzkHTTPError(message="Server did not return a successful response", code=raw_response.status_code)

        response = raw_response.json()
        if response["code"] != 200:
            raise ChzzkHTTPError(message=response["message"], code=response["code"])

        return response["content"]

    async def get(
        self,
        url: str,
        *,
        params: Optional[Mapping[str, Any]] = None,
        data: Optional[Mapping[str, Any]] = None,
        **kwargs,
    ) -> Any:
        return await self.request("GET", url, params=params, data=data, **kwargs)

    async def post(
        self,
        url: str,
        *,
        params: Optional[Mapping[str, Any]] = None,
        data: Optional[Mapping[str, Any]] = None,
        **kwargs,
    ) -> Any:
        return await self.request("POST", url, params=params, data=data, **kwargs)


class GameClient(HTTPClient):
    BASE_URL = "https://comm-api.game.naver.com/nng_main/"

    def __init__(self, credential: Optional[Credential] = None):
        super().__init__(credential)


class ChzzkClient(HTTPClient):
    BASE_URL = "https://api.chzzk.naver.com/"

    def __init__(self, credential: Optional[Credential] = None):
        super().__init__(credential)
