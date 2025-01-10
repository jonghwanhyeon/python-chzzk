from typing import Optional

from chzzk.client import ChzzkClient, Credential, GameClient
from chzzk.models import (
    Channel,
    ChannelSearchRecord,
    LiveDetail,
    LiveSearchRecord,
    LiveStatus,
    SearchCursor,
    User,
    Video,
    VideoSearchRecord,
)


class ChzzkLive:
    def __init__(self, client: ChzzkClient):
        self._client = client

    async def status(self, channel_id: str, **kwargs) -> Optional[LiveStatus]:
        response = await self._client.get(f"polling/v2/channels/{channel_id}/live-status", **kwargs)
        return response and LiveStatus(**response)

    async def detail(self, channel_id: str, **kwargs) -> Optional[LiveDetail]:
        response = await self._client.get(f"service/v2/channels/{channel_id}/live-detail", **kwargs)
        return response and LiveDetail(**response)


class ChzzkSearch:
    def __init__(self, client: ChzzkClient):
        self._client = client

    async def channels(self, keyword: str, size: int = 12, offset: int = 0) -> SearchCursor[ChannelSearchRecord]:
        response = await self._client.get(
            "service/v1/search/channels",
            params={
                "keyword": keyword,
                "size": size,
                "offset": offset,
            },
        )
        return SearchCursor[ChannelSearchRecord](**response)

    async def lives(self, keyword: str, size: int = 12, offset: int = 0) -> SearchCursor[LiveSearchRecord]:
        response = await self._client.get(
            "service/v1/search/lives",
            params={
                "keyword": keyword,
                "size": size,
                "offset": offset,
            },
        )
        return SearchCursor[LiveSearchRecord](**response)

    async def videos(self, keyword: str, size: int = 12, offset: int = 0) -> SearchCursor[VideoSearchRecord]:
        response = await self._client.get(
            "service/v1/search/videos",
            params={
                "keyword": keyword,
                "size": size,
                "offset": offset,
            },
        )
        return SearchCursor[VideoSearchRecord](**response)


class Chzzk:
    def __init__(self, credential: Optional[Credential] = None):
        self._client = ChzzkClient(credential)
        self._game = Game(credential)

        self._search = ChzzkSearch(self._client)
        self._live = ChzzkLive(self._client)

    @property
    def search(self) -> ChzzkSearch:
        return self._search

    @property
    def live(self) -> ChzzkLive:
        return self._live

    async def me(self) -> User:
        return await self._game.me()

    async def channel(self, id: str, **kwargs) -> Channel:
        response = await self._client.get(f"service/v1/channels/{id}", **kwargs)
        return Channel(**response)

    async def video(self, no: int, **kwargs) -> Video:
        response = await self._client.get(f"service/v2/videos/{no}", **kwargs)
        return Video(**response)


class Game:
    def __init__(self, credential: Optional[Credential] = None):
        self._client = GameClient(credential)

    async def me(self) -> User:
        response = await self._client.get("v1/user/getUserStatus")
        return User(**response)
